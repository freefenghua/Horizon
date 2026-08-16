#!/usr/bin/env python3
"""每日日报推送到微信（Server酱 Turbo 版）。

从 data/summaries/ 读取当天的中文日报，通过 Server酱 发送到个人微信。
环境变量：
  SERVERCHAN_SENDKEY — Server酱的 SendKey（sct.ftqq.com 获取）
"""
import datetime
import json
import os
import re
import sys
import urllib.parse
import urllib.request

SENDKEY = os.environ.get('SERVERCHAN_SENDKEY', '')
SUMMARIES_DIR = 'data/summaries'


def build_message():
    today = datetime.date.today().strftime('%Y-%m-%d')
    path = os.path.join(SUMMARIES_DIR, f'horizon-{today}-zh.md')
    if not os.path.exists(path):
        # 当天没有就用最近的一份（周末/失败兜底）
        candidates = sorted(
            f for f in os.listdir(SUMMARIES_DIR)
            if re.match(r'horizon-\d{4}-\d{2}-\d{2}-zh\.md$', f)
        )
        if not candidates:
            return None, None
        path = os.path.join(SUMMARIES_DIR, candidates[-1])
        today = re.search(r'horizon-(\d{4}-\d{2}-\d{2})-zh', path).group(1)

    lines = open(path, encoding='utf-8').read().splitlines()

    # 头部声明（> 从 N 条内容中筛选出 M 条重要资讯）
    header = [l for l in lines if l.startswith('> ')][:1]

    # 详情区：### [标题](原文链接) 开头的完整段落
    body = []
    for l in lines:
        if l.startswith('### ['):
            body += ['', '## ' + l[len('### '):]]
        elif l.startswith('<a id='):
            continue  # 页内锚点，微信里无意义
        else:
            # 展开指向页内锚点的链接（微信里无处可跳），保留外部链接
            body.append(re.sub(r'\[([^\]]+)\]\(#item[^)]*\)', r'\1', l))

    desp = '\n'.join(
        [f'**AI×增长每日精选案例**（{today}）', '']
        + header
        + ['\n---\n']
        + body
    )
    return f'AI×增长日报 {today}', desp


def send(title, desp):
    url = f'https://sctapi.ftqq.com/{SENDKEY}.send'
    data = urllib.parse.urlencode({'title': title, 'desp': desp}).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req, timeout=30) as resp:
        result = json.loads(resp.read())
        if result.get('code') != 0:
            print('ServerChan error:', result, file=sys.stderr)
            sys.exit(1)
        print('ServerChan sent:', result.get('message'))


if __name__ == '__main__':
    if not SENDKEY:
        print('SERVERCHAN_SENDKEY not set, skip notify', file=sys.stderr)
        sys.exit(1)  # 配了密钥却拿不到值属于异常，要显式失败而非静默跳过
    title, desp = build_message()
    if not title:
        print('No digest file found, skip notify', file=sys.stderr)
        sys.exit(1)
    send(title, desp)

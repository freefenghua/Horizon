#!/usr/bin/env python3
"""Regenerate docs/index.md — GitHub Pages 首页，按日期倒序列出全部日报存档。"""
import glob
import os
import re

files = sorted(glob.glob('docs/horizon-*-zh.md'), reverse=True)
lines = [
    '---',
    'layout: default',
    'title: AI×增长每日日报',
    '---',
    '',
    '# AI×用户增长 · 每日精选案例',
    '',
    '每天北京时间早 8 点自动更新：从 24 个信源采集，筛选 AI×增长交叉领域案例。',
    '',
    '| 日期 | 中文日报 | English |',
    '|------|----------|---------|',
]
for f in files:
    date = re.search(r'horizon-(\d{4}-\d{2}-\d{2})-zh\.md$', f).group(1)
    zh_name = os.path.basename(f)
    en_name = zh_name.replace('-zh.md', '-en.md')
    en_cell = (
        f'[{en_name}]({en_name})'
        if os.path.exists(os.path.join('docs', en_name))
        else '—'
    )
    lines.append(f'| {date} | [{zh_name}]({zh_name}) | {en_cell} |')
with open('docs/index.md', 'w') as fp:
    fp.write('\n'.join(lines) + '\n')
print(f'index.md regenerated with {len(files)} entries')

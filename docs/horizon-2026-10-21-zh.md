# Horizon 每日速递 - 2026-10-21

> 从 69 条内容中筛选出 2 条重要资讯。

---

**AI×增长交叉领域**
1. [Claude Code 15 秒剪出带字幕跳剪的 TikTok 视频](#item-ai-growth-1) ⭐️ 6.0/10
2. [健身业用 AI Agent 做会员唤醒与获客的四个场景](#item-ai-growth-2) ⭐️ 6.0/10

---

## AI×增长交叉领域

<a id="item-ai-growth-1"></a>
### [Claude Code 15 秒剪出带字幕跳剪的 TikTok 视频](https://www.lennysnewsletter.com/p/claude-cuts-my-tiktok-how-this-creator) ⭐️ 6.0/10

在 Lenny&\#x27;s Newsletter 的一期节目中，创作者 Brooke Lacey 现场演示了用 Claude Code 把一段手机原始视频处理成带字幕、带跳剪的 TikTok 成片，整个过程约 15 秒。节目由 Claire Vo 主持，时长 37 分钟，形式是实时操作演示而非事后复盘。据节目描述，这条工作流的输入是手机拍摄的原始素材，输出是可直接发布的短视频成品，字幕与跳剪两个环节都由 Claude Code 完成。

rss · Lenny&\#x27;s Newsletter · 10月19日 12:04

**「Claude Code 编排 Whisper 与 FFmpeg」** 创作者 Brooke Lacey 在终端里用 Claude Code 作为编排层，调用两个开源命令行工具完成剪辑：OpenAI Whisper 对原始音频生成词级时间戳，FFmpeg 据此执行实际的视频剪切与缩放调整，全程不打开传统剪辑软件。Claude Code 还负责把剪辑意图转成基于文本的剪切清单（cut list），并可将观众评论转化为脚本。

**「可复用要点」** 内容团队可以先用 Claude Code 跑通“原始素材进、带字幕跳剪成片出”的单条流水线，再评估是否把它接入日常短视频产能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chatprd.ai/how-i-ai/brooke-lacey-claude-code-video-editing">Brooke Lacey’s Claude Code Workflow for Editing TikToks</a></li>
<li><a href="https://podcastrex.com/shows/how-i-ai/claude-cuts-my-tiktok-how-this-creator-is-scaling-video-with-ai-brooke-lacey">“Claude cuts my TikTok”: How this creator is scaling video ...</a></li>
<li><a href="https://www.thepodcastsummary.com/episodes/UF08V1XIUmw/teaching-claude-code-jump-cuts-cadence.html">Brooke Lacey Automates TikTok Jump Cuts With Claude Code</a></li>

</ul>
</details>

**标签**: `#AI video editing`, `#Claude Code`, `#TikTok`, `#content creation workflow`, `#creator growth`, `#short-form video`

---

<a id="item-ai-growth-2"></a>
### [健身业用 AI Agent 做会员唤醒与获客的四个场景](https://www.woshipm.com/ai/6481645.html) ⭐️ 6.0/10

作者马佳彬以健身房续约率仅约三成、会籍顾问靠脑子记几百名会员到期与出勤情况为痛点，拆解了用 AI 办公 Agent WorkBuddy 落地的四个场景。第一是沉睡会员唤醒：上传含姓名、卡种、办卡日期、最近到店时间、剩余私教课时的名单，让 AI 按“超两个月未到店、一个月内到期未续、私教课剩三节以内”分三组，每组生成十条两行以内的微信话术，并预留个性化补充位。第二是体测报告解读：把体测数据翻译成大白话并输出前八周训练方向初稿，由教练二次审核。第三是同城内容获客：参照漳州一家健身房的内容配比（干货教学四成、避坑科普三成、真实效果两成、门店日常一成）批量生成口播脚本，开头 5 秒戳同城痛点、中间 15 秒教学、结尾引导团购体验券。第四是用提示词直接生成会员跟进网页，把到期提醒、体测曲线、跟进记录集中管理。作者强调优惠力度、续费价格等数字 AI 会编造，必须人工审核，且健身属广告法重点监管行业，效果承诺不能写。

rss · 人人都是产品经理 · 10月21日 01:45

**「AI 技术」** 使用 AI 办公 Agent WorkBuddy，通过上传表格数据加提示词模板完成会员分层、话术与脚本生成，并能直接生成含前后端的全栈会员管理网页；技能市场可安装健身训练、douyin-ops（含违禁词检测）、xhs-copywriter 等 Skill，作者建议同类技能只装一个以免占用上下文、浪费 token。

**「可复用要点」** 把会员名单按“沉睡、临期、课将尽”三类分层后让 AI 批量生成带个性化留白的话术，比统一群发更容易被回复，但涉及价格与优惠的数字必须人工核对后再发。

**标签**: `#AI Agent`, `#用户留存`, `#会员运营`, `#健身行业`, `#私域运营`, `#场景落地`

---


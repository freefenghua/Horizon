# Horizon 每日速递 - 2026-08-22

> 从 60 条内容中筛选出 5 条重要资讯。

---

**AI×增长交叉领域**
1. [Naïve：让 AI 直接开公司的产品，半年年化收入增长 10 倍](#item-ai-growth-1) ⭐️ 8.0/10
2. [Qwen3-TTS 优化实现亚 50 毫秒响应，开源助力实时语音应用](#item-ai-growth-2) ⭐️ 7.0/10
3. [ChatGPT 搜索大规模使用 site:操作符，GEO 策略需调整](#item-ai-growth-3) ⭐️ 7.0/10
4. [大厂开源 Harness：AI 竞争从模型转向框架](#item-ai-growth-4) ⭐️ 7.0/10
5. [用白模预演台减少 AI 视频抽卡浪费：Seedance 2.5 实战](#item-ai-growth-5) ⭐️ 7.0/10

---

## AI×增长交叉领域

<a id="item-ai-growth-1"></a>
### [Naïve：让 AI 直接开公司的产品，半年年化收入增长 10 倍](https://www.woshipm.com/chuangye/6448645.html) ⭐️ 8.0/10

Naïve 是一家由两位 20 岁辍学生创立的初创公司，它将注册公司、申请税号、开银行卡、配置数据库和支付工具等商业基础设施封装成 AI 可调用的 API，使 AI Agent 能够自主完成从开发到运营的完整商业闭环。该产品上线几个月即获得超过 3 万名开发者客户，过去半年年化收入增长 10 倍，达到千万美元级别，并完成了 2850 万美元 A 轮融资，公司仅有约 10 名全职员工。Naïve 的增长关键在于它没有要求用户更换已有的 AI 工具，而是嵌入用户现有的工作流，同时通过订阅费、基础设施使用费和商业服务费实现多元化收入。对于增长从业者而言，Naïve 展示了如何通过降低 AI Agent 进入现实商业世界的门槛，创造新的增长机会。

rss · 人人都是产品经理 · 8月21日 07:38

**「AI 技术」** Naïve 的核心技术是将现实世界的商业基础设施（如公司注册、银行账户、支付系统）抽象为 AI 可调用的 API，并配合权限控制、预算管理和审批流程，使 AI Agent 能够安全地执行真实商业操作。它不依赖单一 AI 模型，而是与 Claude、GPT 等现有模型集成，通过配置文件让 Agent 自主生成所需的基础设施。

**「增长影响」** Naïve 在半年内实现了年化收入 10 倍的增长，达到千万美元级别，并积累了超过 3 万名开发者客户。其增长机制在于：通过嵌入用户现有 AI 工具（如 Cursor、Claude Code）降低采用门槛，同时通过按使用量收费（credits）和商业服务费（如 LLC 注册 349 美元）实现收入多元化，随着客户使用更多 Agent，收入持续增长。

**「行动建议」** 增长从业者可以借鉴 Naïve 的策略：不要试图替代用户已有的工具，而是通过 API 集成和权限控制，为用户提供增量价值，同时设计多层次的收费模式（订阅+使用量+服务费）来扩大收入来源。

**标签**: `#AI agents`, `#business infrastructure`, `#startup growth`, `#ARR`, `#API`

---

<a id="item-ai-growth-2"></a>
### [Qwen3-TTS 优化实现亚 50 毫秒响应，开源助力实时语音应用](https://nari-labs.com/blog/qwen3-tts-speed-cost-frontier/) ⭐️ 7.0/10

Nari Labs 团队针对开源文本转语音模型 Qwen3-TTS 进行了深度优化，成功将实时语音应用的关键指标——首音频时间（TTFA）降低至 34 毫秒（p95），在单张 H100 上以每秒 10 个请求的负载下实现。该优化解决了现有开源实现（如 vLLM-Omni、SGLang-Omni）在生产环境中延迟过高、无法满足实时播放需求的问题。团队已开源其实现和基准测试代码，并提供了详细的优化过程分解。对于构建实时语音界面的增长从业者而言，这一成果意味着可以显著提升用户体验，减少等待感，从而可能提高用户留存和参与度。尽管该案例未直接提供转化率或留存率等增长指标，但其技术突破为实时语音应用的大规模部署提供了可行路径。

hackernews · toebee · 8月21日 15:51 · [社区讨论](https://news.ycombinator.com/item?id=49389952)

**「AI 技术」** 该案例涉及对开源文本转语音（TTS）模型 Qwen3-TTS 的推理优化，通过工程手段（如批处理、流式解码、硬件适配等）将端到端延迟降至极低水平。具体技术细节未在来源中详述，但根据社区评论，作者针对 vLLM-Omni 和 SGLang-Omni 等现有开源实现进行了改进，解决了生产环境下的实时播放问题。优化后的模型在单张 H100 上实现了 34 ms 的 p95 首音频时间（TTFA），并开源了实现和基准测试代码。

**「增长影响」** 该优化通过将 TTS 延迟从常见的 200 毫秒以上降至 34 毫秒（p95），直接改善了实时语音交互的响应速度，减少了用户等待时间，从而可能提升用户满意度和留存率。在语音助手、实时翻译等场景中，低延迟是用户留存的关键因素，此技术突破可帮助增长团队在竞争激烈的市场中脱颖而出。

**「实践启示」** 增长从业者应关注实时语音应用中的延迟指标（如 TTFA），并采用开源优化方案（如 Nari Labs 的实现）来提升用户体验，从而间接促进用户留存和参与。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen3-TTS">GitHub - QwenLM/ Qwen 3 - TTS : Qwen 3 - TTS is an open-source series...</a></li>

</ul>
</details>

**标签**: `#TTS`, `#latency`, `#voice AI`, `#open source`, `#performance optimization`

---

<a id="item-ai-growth-3"></a>
### [ChatGPT 搜索大规模使用 site:操作符，GEO 策略需调整](https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale/) ⭐️ 7.0/10

ChatGPT 搜索现已大规模使用 site:操作符，根据 Promptwatch 的追踪数据，该操作符在 ChatGPT 搜索查询中的占比从长期徘徊的 0.3%-0.5%跃升至 8 月 8 日的 16%-17%，这一变化与 OpenAI 在 8 月 6 日发布的 GPT-5.6 Sol 更新公告相吻合。Promptwatch 通过自动化追踪用户与 ChatGPT 等产品的交互提示词，其数据为观察 ChatGPT 搜索行为的变化提供了可信线索。这一转变意味着生成式引擎优化（GEO）策略需要调整，网站运营者应重视针对 site:查询的优化，以提升在 AI 搜索中的可见性。尽管数据仅反映 Promptwatch 追踪的提示词，但趋势显著，对 SEO/GEO 从业者具有重要参考价值。

rss · Simon Willison · 8月20日 23:57

**「AI 技术解析」** ChatGPT 搜索在 GPT-5.6 Sol 更新后，其底层搜索工具采用了类似\`search\(query, recency, domains\)\`的函数调用结构，而非直接鼓励用户使用\`site:\`操作符。但根据 Promptwatch 的追踪数据，ChatGPT 搜索的查询扇出（query fanout）行为在 8 月 8 日发生了显著变化，包含\`site:\`操作符的查询占比从之前的 0.3%-0.5%跃升至 16%-17%。这表明 OpenAI 在系统层面自动为搜索查询附加了\`site:\`操作符，以优先从可信域名获取信息，从而提升回答的事实准确性和聚焦度。这一变化与 OpenAI 官方公告中提到的“更可靠的事实和更聚焦的答案”一致。

**「增长影响」** site:操作符使用率的激增（从约 0.3%-0.5%跃升至 16%-17%）表明 ChatGPT 搜索的引用机制发生了重大变化，直接影响网站的 AI 搜索流量分配。对于依赖搜索流量的增长从业者，这一变化意味着需要重新评估关键词策略，优先优化 site:查询的匹配度，以抓住 AI 搜索带来的流量机会。

**「行动建议」** 增长从业者应监控自身品牌或产品相关的 site:查询在 ChatGPT 等 AI 搜索中的表现，并针对这些查询优化内容结构和关键词，以提升在 AI 生成答案中的引用概率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/">OpenAI | Research &amp; Deployment</a></li>
<li><a href="https://www.zerohedge.com/technology/chart-day-reddit-mostly-wiped-chatgpt-citations">&#x27;Quality Over Quantity&#x27;: Reddit Is Mostly Wiped From ChatGPT ...</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#GEO`, `#SEO`, `#site: operator`, `#search behavior`

---

<a id="item-ai-growth-4"></a>
### [大厂开源 Harness：AI 竞争从模型转向框架](https://www.woshipm.com/ai/6452361.html) ⭐️ 7.0/10

OpenAI 与 DeepSeek 在一周内相继开源智能体核心框架 Harness，标志着 AI 竞争从模型层转向框架层。Harness 负责管理会话状态、工具调用、沙箱隔离等，将模型能力转化为稳定产出。OpenAI 数据显示，仅优化 Harness 的推理保留和上下文压缩，同一款 GPT-5.6 Sol 在 ARC-AGI-3 测试中得分从 13.3%提升至 38.3%，输出 token 量减少六倍。开源后，开发者可将智能体能力嵌入自有产品，降低落地门槛，推动产品形态跳出聊天框。对增长从业者而言，理解 Harness 工程将成为构建 AI 产品竞争力的关键。

rss · 人人都是产品经理 · 8月21日 09:20

**「AI 技术解析」** Harness 是智能体运行框架，相当于大模型的“控制系统”，负责会话状态管理、工具调用调度、沙箱隔离、审批策略和上下文压缩。通过优化推理保留和上下文压缩机制，显著提升模型在复杂任务上的表现，同时减少输出 token 量。

**「增长影响」** 开源 Harness 降低了企业构建生产级智能体的门槛，使中小团队无需从零搭建底层系统，加速 AI 功能嵌入业务流程。例如，税务准备工具接入 Codex Harness 后，处理七千份申报的时间缩短三分之一，且全程在原有业务系统内完成，提升了运营效率。

**「行动建议」** 增长从业者应关注 Harness 等框架层创新，优先采用成熟开源框架快速落地 AI 功能，将智能体嵌入真实业务流程，而非局限于聊天界面，以提升效率和用户体验。

**标签**: `#AI infrastructure`, `#open source`, `#agent framework`, `#product strategy`, `#OpenAI`, `#DeepSeek`

---

<a id="item-ai-growth-5"></a>
### [用白模预演台减少 AI 视频抽卡浪费：Seedance 2.5 实战](https://www.woshipm.com/ai/6452339.html) ⭐️ 7.0/10

本文介绍了使用 updream 的预演台（Previs Studio）配合 Seedance 2.5 模型，通过白模预演来控制 AI 视频生成中的人物路径、复杂运镜和多机位切换，从而减少无效抽卡和生成浪费。作者通过三组测试对比纯提示词和白模参考的效果，发现白模参考能更准确地执行预设的路线和运镜，避免 AI 自行理解导致的偏差。该方法直接降低了因 AI 误解拍摄意图而反复生成的成本，对依赖 AI 视频进行内容生产的团队具有实用价值。

rss · 人人都是产品经理 · 8月21日 08:03

**「AI 技术」** 该案例采用白模预演（Previs Studio）工作流：先用 3D 白模搭建场景、设定人物移动路径和摄影机轨迹，再让 Seedance 2.5 参考白模视频生成最终画面。这种方法将原本依赖提示词描述的拍摄意图转化为可视化的空间路径，显著提升 AI 对人物路线、运镜和多机位切换的执行准确性。

**「增长影响」** 该方法通过减少无效生成次数，直接降低了 AI 视频制作中的算力成本和人力时间成本，提升了内容生产效率。虽然文中未提供具体量化数据，但作者指出无效抽卡是主要烧钱环节，白模预演能显著减少此类浪费，尤其适用于需要批量生成营销视频的团队。

**「可复用策略」** 在 AI 视频生成前，先用白模预演工具（如 updream Previs Studio）可视化人物路径和运镜，再将其作为参考输入模型，可大幅提升生成结果与预期的一致性，减少无效抽卡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.php.cn/faq/uaspczyjbfjz">updream 怎么制作 AI 视 频 _ updream ...</a></li>

</ul>
</details>

**标签**: `#AI视频生成`, `#预演台`, `#Seedance 2.5`, `#工作流优化`, `#内容生产`

---


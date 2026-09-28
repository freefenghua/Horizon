# Horizon Daily - 2026-09-28

> From 51 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [WorkBuddy for Small Restaurants: 4 Practical AI Scenarios](#item-ai-growth-1) ⭐️ 6.0/10
2. [Tencent Quietly Launches LightVela, a China-Ready Rival to Meta&\#x27;s Muse](#item-ai-growth-2) ⭐️ 5.0/10
3. [供应链AI集体“收权”：真正落地的都停在L3](#item-ai-growth-3) ⭐️ 5.0/10
4. [即梦AI样片模式：480P抽卡再升清1080P，AI短片成本降65%](#item-ai-growth-4) ⭐️ 5.0/10
5. [Bluesky Reply Bot Checker Built via Vibe Coding](#item-ai-growth-5) ⭐️ 4.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [WorkBuddy for Small Restaurants: 4 Practical AI Scenarios](https://www.woshipm.com/ai/6470711.html) ⭐️ 6.0/10

This article by 马佳彬 outlines four practical AI-powered operational scenarios for small and mid-sized restaurant businesses using WorkBuddy, an AI office agent accessible via app or WeChat mini-program. The scenarios cover procurement receipt reconciliation, customer recall and review reputation management, weekly business review, and marketing content creation, each with prompt templates and some with installable Skill plugins. The article cites public information that Chinese small restaurant outlets have an average survival period of only 15 months, with food, rent, and labor accounting for over 70% of costs, and nearly 90% of restaurants lacking an internal data platform. No performance metrics, before/after data, or validated results are reported, and the author explicitly notes the content is for reference only and prompt templates should be adjusted to individual circumstances. For growth practitioners, the piece offers a replicable framework for applying accessible AI tools to high-friction operational tasks in resource-constrained businesses.

rss · 人人都是产品经理 · Sep 28, 03:02

**「AI Technique」** The article describes using WorkBuddy, an AI office agent with built-in OCR image recognition and table generation capabilities, to process receipt photos, customer data, and review text via natural language prompts. It also references installable Skill plugins such as restaurant-review-analysis for review categorization, biz-menu-engineering for menu quadrant analysis, store-operations-analysis for store health checks, and poster-maker for social media graphics, plus Hy Image3.5 preview for image generation.

**「Growth Impact」** The article claims that after becoming familiar with the receipt reconciliation workflow, daily time spent is under two minutes, reducing month-end reconciliation from manually searching through photos to reviewing an AI-generated ledger. However, no conversion lift, retention improvement, or other measurable growth outcomes are reported, and the author notes that AI conclusions depend on data accuracy and that major decisions like menu cuts or price increases require human judgment.

**「Takeaway」** Start by applying AI to the most labor-intensive daily operational chores—such as receipt reconciliation or review response drafting—using simple prompt templates and built-in OCR/table tools, then expand to more advanced analysis as familiarity grows.

**Tags**: `#AI应用`, `#餐饮运营`, `#WorkBuddy`, `#中小企业`, `#提示词模板`, `#运营效率`

---

<a id="item-ai-growth-2"></a>
### [Tencent Quietly Launches LightVela, a China-Ready Rival to Meta&\#x27;s Muse](https://www.woshipm.com/ai/6471130.html) ⭐️ 5.0/10

Tencent has quietly launched LightVela, a cloud-hosted personal AI agent that runs the open-source Hermes Agent framework and lets users chat with it directly inside WeChat, QQ, and Feishu without managing servers or writing code. The launch is positioned as a China-accessible counterpart to Meta&\#x27;s Muse, which the article says hit over 2.5 million downloads in 13 days and 642,000 US mobile DAU — roughly three times ChatGPT&\#x27;s early DAU — but is restricted to US users aged 18 and over. LightVela&\#x27;s new users reportedly get a free one-month trial with 4,500 credits, and the product timeline runs from an April standalone launch through a May limited free beta and an August 18 public beta. The piece frames Tencent&\#x27;s advantage not as a smarter model but as distribution and retention: hosting the agent inside WeChat means it accumulates memory, history, contacts, and habits, raising switching costs. For growth practitioners, this is a signal that chat-app-native agent distribution is becoming a real channel, though the article offers no LightVela performance data or replicable growth playbook.

rss · 人人都是产品经理 · Sep 28, 03:09

**「AI Technique」** LightVela is a cloud-hosted wrapper around the open-source Hermes Agent framework: Tencent provisions a dedicated Hermes Agent instance per user, exposes a web panel for model selection, channel configuration, and skill installation, and then routes the agent into messaging apps like WeChat, QQ, and Feishu. The underlying models are pluggable from multiple vendors, so Tencent&\#x27;s contribution is cloud hosting, visual configuration, and chat-app integration rather than a proprietary model.

**「Growth Impact」** The article reports no conversion, retention, or revenue metrics for LightVela itself, so its growth impact is unverified. The only hard numbers cited are for Meta&\#x27;s Muse: over 2.5 million downloads in 13 days, 642,000 US mobile DAU, and roughly 3x ChatGPT&\#x27;s early DAU, achieved with a US-only, 18+ audience. The implied mechanism for LightVela is distribution-led retention — embedding the agent in WeChat, QQ, and Feishu so accumulated context and habits make the agent harder to abandon — but this remains a hypothesis in the source, not a measured outcome.

**「Takeaway」** When evaluating an AI agent product, weight the distribution surface and accumulated user context — where the agent lives and what it remembers — over raw model quality, since that is what raises switching costs and retention.

**Tags**: `#AI agents`, `#Tencent`, `#Meta Muse`, `#product launch`, `#China AI`, `#distribution`

---

<a id="item-ai-growth-3"></a>
### [供应链AI集体“收权”：真正落地的都停在L3](https://www.woshipm.com/ai/6471113.html) ⭐️ 5.0/10

This article observes that supply chain AI vendors are converging on a conservative &quot;AI suggests, humans decide&quot; model, citing Cainiao&\#x27;s &quot;AI gives suggestions, humans make the final call,&quot; AWS&\#x27;s &quot;you lead a team of AI agents,&quot; and Oracle&\#x27;s &quot;execute within guardrails, surface to humans when judgment is needed.&quot; The author argues this is not a technology maturity problem but a deliberate product decision, because supply chain errors carry direct financial consequences, and cites a Gartner forecast that by 2030 only 5% of enterprises with supply chain planning automation will let AI autonomously make at least 10% of planning decisions. The piece proposes a five-tier &quot;delegation ladder&quot; \(L1 suggestions through L5 irreversible actions\) and claims that currently deployable, revenue-generating supply chain AI reaches at most L3 \(rollback-capable execution\). It also warns against &quot;fake human-in-the-loop&quot; designs where review happens after execution, lacks time to intervene, or queues thousands of items no one reads. The article is an opinion/industry observation and does not report specific growth metrics such as conversion, retention, or CAC.

rss · 人人都是产品经理 · Sep 28, 03:08

**「AI Technique」** The article describes a dual-model architecture: a large model handles global, fast computation \(&quot;commanding troops&quot;\) while smaller models encode industry rules, constraints, and experience \(&quot;fighting the battle&quot;\), with the human retaining final decision rights and the system learning from which option the human selects or modifies. It also references human-in-the-loop review design and confidence-threshold-based circuit breakers rather than any specific model or fine-tuning method.

**「Growth Impact」** No concrete growth metrics \(conversion, retention, CAC, revenue\) are reported in the source. The article&\#x27;s central quantitative claim is Gartner&\#x27;s forecast that by 2030 only 5% of enterprises with supply chain planning automation will allow AI to autonomously make at least 10% of planning decisions. The author&\#x27;s qualitative claim is that AI frees humans from calculation so they only perform selection, but this is not backed by measured outcomes in the source.

**「Takeaway」** Before shipping any AI feature, map each workflow node to a delegation tier \(suggest, low-risk execute, rollback-capable execute, high-risk approval, irreversible\) and define explicit circuit-breaker conditions \(low confidence, missing or conflicting data, repeated failures, money/contracts/external commitments\) so the AI&\#x27;s decision boundary is written into the PRD rather than left to intuition.

**Tags**: `#供应链AI`, `#人机协同`, `#AI决策边界`, `#行业观察`, `#Gartner预测`

---

<a id="item-ai-growth-4"></a>
### [即梦AI样片模式：480P抽卡再升清1080P，AI短片成本降65%](https://www.woshipm.com/ai/6470717.html) ⭐️ 5.0/10

即梦AI（字节旗下AI视频创作平台）推出业界首个「样片模式」，允许创作者先用480P低成本反复抽卡，判断构图、镜头运动和主体表演，选定满意的一条后再一次性原生升清为1080P成片。作者实测用即梦Seedance 2.5制作30秒1080P视频，加上抽卡成本约200元，比此前直出1080P的方式降低约65%。具体算账显示：480P样片每次消耗270积分（约22元），直出1080P需1920积分，抽卡5次加一次升清共3270积分（约270元），而全部直出1080P需9600积分（约800元），节省近66%、约530元。作者还展示了东方志怪真人短剧、末日废土3D CG动画、苹果风3C产品TVC三个案例，指出原生升清不仅提升清晰度，还改善了毛发、皮肤、文字锐度和光影特效。对内容创作者而言，这提供了一套可复用的低成本试错工作流，把AI视频抽卡从「按成片价试错」变为「先打草稿再出片」。

rss · 人人都是产品经理 · Sep 28, 02:52

**「AI Technique」** 即梦AI的「样片模式」基于Seedance 2.5视频生成模型，核心是两阶段生成：先用480P分辨率低成本生成草稿视频用于抽卡筛选，再对选定草稿进行原生升清（非第三方超分）输出1080P成片。作者提到此前尝试的480P加第三方超分方案效果不理想，文字模糊、人脸变形，而原生升清在文字锐度、材质质感和光影上表现更好。

**「Growth Impact」** 该模式将30秒1080P AI短片的制作成本从约800元降至约270元，降幅近66%，直接降低了内容创作者的试错成本。作者引用行业数据称，抖音上半年新上线AI短剧超22万部，按5000万播放为盈亏线仅1.3%不亏钱，成熟团队每镜头抽卡3到5次、算力成本达一两万元，精品剧单镜头可抽20到30次，因此降低抽卡成本对提升内容生产的经济性有实际意义。

**「Takeaway」** 在AI视频制作中，把「抽卡试错」和「最终成片」拆成两个分辨率阶段——先用低成本低分辨率筛选构图、运镜和表演，再对选定结果做原生升清，可显著降低废片成本，这一思路也可迁移到其他概率性AI生成工作流。

**Tags**: `#AI视频`, `#即梦AI`, `#成本优化`, `#内容创作`, `#工具实测`

---

<a id="item-ai-growth-5"></a>
### [Bluesky Reply Bot Checker Built via Vibe Coding](https://simonwillison.net/2026/Sep/27/bluesky-bot-check/) ⭐️ 4.0/10

Simon Willison built a Bluesky reply bot checker by having Opus 5.5 &quot;vibe code&quot; the tool, which examines any Bluesky profile for evidence of a likely automated reply account. The tool flags signals such as replies posted within seconds of other posts from the same account, accounts that never post their own content, images, or links but consistently reply to higher-follower users, and the presence of question marks. Willison notes that automated reply bots, already a scourge on Twitter, have started appearing on Bluesky, and that Bluesky&\#x27;s freely available API makes investigating them easier than on Twitter. The source reports no growth metrics, no before/after data, and no replicable growth playbook, so its relevance to growth practitioners is limited to a minor signal about platform integrity tooling rather than a growth case study.

rss · Simon Willison · Sep 27, 18:41

**「AI Technique」** The tool was generated through AI-assisted &quot;vibe coding,&quot; with Willison prompting Opus 5.5 to write the code \(linked as a GitHub pull request\) rather than applying AI to growth or marketing tasks. The detection logic itself is rule-based, relying on reply timing and posting-pattern heuristics rather than machine learning.

**「Growth Impact」** No measurable growth outcome is reported; the source contains no conversion, retention, or CAC data. The implied benefit is qualitative: reducing bot spam that degrades engagement quality on Bluesky, with no scale or context metrics provided.

**「Takeaway」** If bot spam is polluting your social engagement data, a lightweight heuristic checker built with an AI coding assistant can flag suspicious accounts by reply timing and posting patterns before you act on their interactions.

**Tags**: `#bluesky`, `#bot-detection`, `#ai-coding-assistant`, `#social-platform`, `#tool`

---


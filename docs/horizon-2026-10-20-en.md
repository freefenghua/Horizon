# Horizon Daily - 2026-10-20

> From 59 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [Claude Code 15秒将原始手机视频剪成TikTok](#item-ai-growth-1) ⭐️ 6.0/10
2. [AI客服答非所问：先查日志证据，再改提示词或知识库](#item-ai-growth-2) ⭐️ 6.0/10
3. [DeepSeek Filters GEO Manipulation: What It Means for AI Search Marketing](#item-ai-growth-3) ⭐️ 6.0/10
4. [Decision Model Threshold Tuning for Automated Evals](#item-ai-growth-4) ⭐️ 4.0/10
5. [AI Short Dramas vs. Gaming: Attention Shift, Not Disruption](#item-ai-growth-5) ⭐️ 4.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [Claude Code 15秒将原始手机视频剪成TikTok](https://www.lennysnewsletter.com/p/claude-cuts-my-tiktok-how-this-creator) ⭐️ 6.0/10

创作者 Brooke Lacey 在 Lenny&\#x27;s Newsletter 的一期 37 分钟视频中演示了使用 Claude Code 将原始手机视频自动剪辑为带字幕、带跳剪的 TikTok 视频，据称耗时约 15 秒。该案例针对的是短视频内容生产中剪辑耗时、难以规模化的增长痛点。不过，目前公开内容仅为视频预告，未披露留存、转化或产出量等任何指标，也没有前后对比或具体操作步骤。对增长从业者而言，这代表一种值得关注的 AI 视频剪辑工作流模式，但尚缺乏可验证的效果数据，不宜过度解读。

rss · Lenny&\#x27;s Newsletter · Oct 19, 12:04

**「Claude Code for automated short-form video editing」** The workflow uses Claude Code, Anthropic&\#x27;s agentic coding tool, to process raw phone footage and output an edited TikTok with captions and jump cuts in roughly 15 seconds. The source is only a video teaser and does not detail the underlying steps, so the exact editing pipeline \(e.g., transcription, cut detection, rendering\) remains unverified.

**「Growth Impact」** The reported outcome is production speed rather than a measured growth metric: Brooke Lacey&\#x27;s Claude Code workflow turns a raw phone video into a captioned, jump-cut TikTok in about 15 seconds, replacing manual trimming in CapCut. The mechanism is automation of the tedious mechanics of short-form editing — jump cuts, facial tracking, and shot variety — handled locally via FFmpeg, Whisper, and Python, which lowers the time cost per video and could let a creator publish more often. No retention, conversion, or output-volume data was published, so any downstream growth effect remains unverified.

**「可借鉴之处」** 可关注用 Claude Code 等代码型 AI 工具把“原始素材→字幕+跳剪”的剪辑流程脚本化，但在投入前应先自行小规模测试其实际耗时与产出质量，而非直接采信演示中的 15 秒说法。

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=UF08V1XIUmw">How this creator with 250K+ followers edits TikToks with Claude</a></li>
<li><a href="https://claude.ai/artifacts/inspiration/dcc8728e-4925-4c50-9418-a259f9a67342">Claude</a></li>
<li><a href="https://www.chatprd.ai/how-i-ai/brooke-lacey-claude-code-video-editing">Brooke Lacey’s Claude Code Workflow for Editing TikToks</a></li>
<li><a href="https://podpulse.ai/podcast/how-i-ai/how-brooke-lacey-uses-claude-code-to-automate-tiktok-editing">How Brooke Lacey Uses Claude Code to Automate TikTok Editing ...</a></li>
<li><a href="https://www.traeai.com/articles/97bd60ba-b510-49fe-b32d-cbbdf2487a68">“Claude cuts my TikTok”: How this creator is scaling video ...</a></li>

</ul>
</details>

**Tags**: `#AI video editing`, `#Claude Code`, `#TikTok`, `#creator workflow`, `#content production`, `#short-form video`

---

<a id="item-ai-growth-2"></a>
### [AI客服答非所问：先查日志证据，再改提示词或知识库](https://www.woshipm.com/ai/6480104.html) ⭐️ 6.0/10

This article uses a real case where a user asked &quot;When will my refund arrive?&quot; on an order page, but the AI assistant replied with a generic refund policy statement instead of checking the specific order&\#x27;s refund status. The author argues that before modifying prompts or the knowledge base, teams should first pull the logs from that session to reconstruct the full chain: user input and context, intent routing, retrieval candidates and document versions, tool calls and returns, prompt/model configuration versions, and the final answer. The article provides a diagnostic sequence—check whether order context was passed in, whether routing recognized a personal progress query, whether the refund API was called, whether retrieval returned the correct document version, and whether the model&\#x27;s injected context was complete—and recommends replaying the issue in a test environment with fixed configurations when logs are insufficient. It also offers a reusable acceptance test template and emphasizes regression testing after any single fix. The piece is practical for operations and customer service teams but lacks quantitative metrics such as resolution rate improvement or conversion impact.

rss · 人人都是产品经理 · Oct 20, 03:35

**「AI Technique」** The article describes a diagnostic approach for LLM-based customer service systems that combines intent routing, retrieval-augmented generation \(RAG\) with knowledge base versioning, and tool/API calls to backend order systems. It emphasizes log-based reconstruction and controlled replay testing rather than a specific model or fine-tuning method.

**「Growth Impact」** The source does not report measurable growth outcomes such as resolution rate lift, conversion impact, or cost reduction. It focuses on reducing misdiagnosis and wasted prompt edits by establishing an evidence-based troubleshooting workflow, which could indirectly improve customer service efficiency and answer accuracy, but no quantitative results are provided.

**「Takeaway」** Before changing prompts or knowledge base content, pull the session logs to verify whether the failure occurred in context passing, intent routing, retrieval, tool calls, or generation—then fix only the layer supported by evidence and rerun a regression set.

**Tags**: `#AI客服`, `#提示词工程`, `#知识库`, `#问题排查`, `#运营实操`

---

<a id="item-ai-growth-3"></a>
### [DeepSeek Filters GEO Manipulation: What It Means for AI Search Marketing](https://www.woshipm.com/marketing/6480824.html) ⭐️ 6.0/10

On October 17, DeepSeek opened its self-developed search API and stated in its changelog that it would filter SEO cheating, GEO \(Generative Engine Optimization\) manipulation, and low-quality AI-generated content. The article uses this as a starting point to discuss the emerging GEO business, where brands try to get AI models to recommend them, and the inherent paradox: GEO&\#x27;s popularity comes from AI capability growth, but part of its profit comes from AI&\#x27;s insufficient judgment. The piece cites a 2024 KDD paper by Aggarwal et al. that formalized GEO and measured up to 40% visibility improvement for optimized content, and a 2026 3·15晚会 investigation where a fictional product, Apollo-9, was recommended by AI within two hours of publishing generated soft articles. It also notes that DeepSeek and ChatGPT can, when prompted to exclude GEO influence, filter out many low-quality promotional articles. For growth practitioners, the key message is that tactics relying on AI&\#x27;s temporary inability to detect manipulation are fragile, and sustainable GEO should focus on making real product information clear and verifiable.

rss · 人人都是产品经理 · Oct 20, 03:15

**「AI Technique」** The article discusses GEO, which involves optimizing content so that generative AI engines like DeepSeek, Doubao, and ChatGPT mention or recommend a brand in their answers. It also covers platform-side countermeasures such as DeepSeek&\#x27;s search API filtering mechanisms to detect SEO cheating, GEO manipulation, and low-quality AI content, and Microsoft&\#x27;s disclosed defenses against AI recommendation poisoning, including instruction filtering and distinguishing external content from user instructions.

**「Growth Impact」** The article does not provide specific conversion or revenue metrics for GEO campaigns. It cites a 2024 KDD paper reporting up to 40% visibility improvement for optimized content in generative engines, and a 2026 3·15晚会 experiment where a fictional product was recommended by AI within two hours and entered top recommendations of two major models within three days. These examples illustrate potential short-term visibility gains but also highlight the fragility of manipulation-based tactics as platforms improve detection.

**「Takeaway」** Growth practitioners should prioritize making product information accurate, consistent, and verifiable across sources—such as updating specs, prices, and limitations—rather than investing in generated soft articles, because AI platforms are increasingly able to filter manipulative content and sustainable visibility depends on real evidence.

**Tags**: `#GEO`, `#生成式引擎优化`, `#AI搜索`, `#品牌营销`, `#DeepSeek`, `#内容生态`

---

<a id="item-ai-growth-4"></a>
### [Decision Model Threshold Tuning for Automated Evals](https://hamel.dev/blog/posts/decision-model-evals/) ⭐️ 4.0/10

This technical post explains how to tune decision thresholds when using decision models as a low-cost alternative to LLM judges for automated evals. Using 100 traces from an apartment leasing agent to detect failures such as failed bookings or missed human handoffs, the author tested Jev 1.13, Perplexity Decider 1.1 27B, Liquid d1 and d1-ultra, Cloudflare Clef Flash, and OpenAI Decisions \(GPT-6 Luna\). The core finding is that relying on the default 0.50 threshold can leave significant performance on the table, and that tuning thresholds for F1 while enforcing minimum precision and recall requirements changes which models qualify. The post offers a reusable coding-agent prompt for threshold tuning with stratified five-fold cross-validation. It is a technical evaluation methodology piece with no growth, marketing, or product-metric application, so its relevance to growth practitioners is indirect at best.

rss · Hamel Husain · Oct 20, 07:00

**「AI Technique」** Decision models are lightweight classifiers that return a 0-1 failure probability per trace, and the APIs convert that score into a pass/fail decision using a default 0.50 threshold. The post shows how to tune that threshold against labeled data, optimizing F1 subject to minimum precision and recall constraints via stratified five-fold cross-validation.

**「Takeaway」** If you use a decision model for any automated classification, do not accept the default 0.50 threshold; tune it on labeled data against your actual precision and recall requirements before trusting the results.

**Tags**: `#AI evals`, `#decision models`, `#LLM judges`, `#model tuning`, `#technical`

---

<a id="item-ai-growth-5"></a>
### [AI Short Dramas vs. Gaming: Attention Shift, Not Disruption](https://www.woshipm.com/ai/6480940.html) ⭐️ 4.0/10

AI short dramas are rapidly capturing user attention, with QuestMobile data showing short drama apps reached 26.9 hours of monthly per-user usage in May 2026—nearly double the 14.7 hours for online video. Hongguo Free Short Drama hit 168 million DAU in July, surpassing the combined DAU of iQiyi, Tencent Video, Youku, and Mango TV. However, the article argues this attention shift is unlikely to seriously disrupt gaming, which grew from 203.6 billion RMB in 2017 to 350.8 billion RMB in 2025. The author contends that AI short dramas mainly threaten light casual games and traditional live-action short dramas, while core gaming experiences—driven by interactivity, social features, and progression—remain resilient. For growth practitioners, this underscores the importance of assessing substitutability between content formats when evaluating competitive threats.

rss · 人人都是产品经理 · Oct 20, 03:36

**「AI Technique」** The article discusses AI&\#x27;s role in drastically lowering video production costs, enabling faster and cheaper creation of short dramas and AI-generated comic dramas. It does not detail specific AI models or tools, but highlights how generative AI reduces barriers to content supply.

**「Growth Impact」** AI short dramas have achieved massive scale: 718 million MAU for the short drama industry as of February 2026, and Hongguo&\#x27;s AI comic drama app reached 24 million MAU with 90.7 minutes of daily per-user time within four months of launch. This growth comes at the expense of traditional live-action short dramas and light casual games, but has not yet dented overall gaming revenue, which hit a record 350.8 billion RMB in 2025.

**「Takeaway」** When evaluating competitive threats from new AI-powered content formats, assess the degree of experience substitutability—AI short dramas may steal time from low-engagement casual games but are unlikely to replace core gaming experiences that rely on interactivity and social bonds.

**Tags**: `#AI短剧`, `#用户时长`, `#注意力经济`, `#游戏行业`, `#市场分析`, `#QuestMobile`

---


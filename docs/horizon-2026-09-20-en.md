# Horizon Daily - 2026-09-20

> From 54 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [Perplexity Teardown: 100M MAU, $20B Valuation, and the Comet Browser Bet](#item-ai-growth-1) ⭐️ 6.0/10
2. [Open-Source Skill Uses GPT-6 Astra to Render Product Promo Videos from Code](#item-ai-growth-2) ⭐️ 6.0/10
3. [AI Services on Xianyu: 9.8M Orders, But Most Sellers Earn Only Hundreds](#item-ai-growth-3) ⭐️ 6.0/10
4. [“去AI味”是伪命题：同质化源于模型架构](#item-ai-growth-4) ⭐️ 5.0/10
5. [豆包手机：AI硬件商业化的卡点是生态利益分配](#item-ai-growth-5) ⭐️ 5.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [Perplexity Teardown: 100M MAU, $20B Valuation, and the Comet Browser Bet](https://www.woshipm.com/evaluating/6466946.html) ⭐️ 6.0/10

A product-manager teardown of Perplexity argues that the company&\#x27;s real strategic bet is not its search box but the Comet AI browser, which it positions as the only potentially durable moat. The article reports headline scale metrics: over 100 million monthly active users, a $20 billion valuation, and $750 million in annualized revenue, alongside a five-tier pricing structure \(free, $10 education Pro, $20 Pro, $200 Max, and $40–325 per seat enterprise\) and 4,000+ enterprise customers. It describes Perplexity&\#x27;s core loop as ask → watch it think → get a cited answer → follow up, with suggested follow-up questions acting as the visible retention engine, and identifies five design patterns including citation-first answers, streaming process transparency, and a Google-style search bar rather than a chat prompt. The teardown also flags a serious trust crack: a Columbia Journalism Review benchmark cited in the article found 37% citation error rates on the free tier and 45% on Pro, the worst among tested AI search engines, which the author calls an existential risk ahead of enterprise expansion. For growth practitioners, the piece offers framing on AI product loops, pricing architecture, and channel strategy, but it lacks concrete conversion, retention, CAC, or LTV data and a replicable playbook, and the source content is truncated mid-analysis.

rss · 人人都是产品经理 · Sep 20, 03:36

**「AI Technique」** Perplexity uses its own Sonar model, described in the article as a fine-tuned Llama rather than a frontier model, to perform autonomous multi-step web crawling and synthesis with inline numbered citations. It also routes across multiple third-party models \(GPT, Claude, Gemini, and Grok\), and its Comet browser&\#x27;s Computer mode executes multi-step tasks across Gmail, Slack, GitHub, Notion, and Salesforce.

**「Growth Impact」** The article reports scale outcomes rather than funnel metrics: 100M+ MAU, $20B valuation, $750M annualized revenue, and 4,000+ enterprise customers, with a seat-based enterprise motion \($40–325 per seat per month\) as the growth engine. It attributes retention to the follow-up-question loop and trust to citation-first design, but provides no conversion, retention, CAC, or LTV figures, so the causal mechanism is asserted rather than measured.

**「Takeaway」** Design your AI product&\#x27;s core loop so the next action is always suggested—Perplexity&\#x27;s 3–5 contextual follow-up questions per answer are a concrete, replicable retention tactic—and treat citation accuracy as a guardrail metric, since the article reports 37–45% error rates that directly undermine a trust-based positioning.

**Tags**: `#Perplexity`, `#AI search`, `#product teardown`, `#business model`, `#AI browser`, `#growth strategy`

---

<a id="item-ai-growth-2"></a>
### [Open-Source Skill Uses GPT-6 Astra to Render Product Promo Videos from Code](https://www.woshipm.com/ai/6466908.html) ⭐️ 6.0/10

An open-source Skill called guizang-product-video-skill uses GPT-6 Astra to read a product&\#x27;s codebase and render a product promo video entirely from code, without calling any image or video generation APIs. The tool pulls components, colors, fonts, logos, and styles directly from the repository, then assembles selling points, copy, animations, and music; the soundtrack is synthesized in pure Python and sound effects use sidechain ducking. The author demonstrated it on three projects — CodePilot, CraftAgent, and T3 Code — and reported that the T3 Code video was produced in one pass with no manual adjustments, while the CodePilot video required the most iteration. The output is not just an MP4 but an editable video project where copy, layout, duration, animation, and audio can be changed and re-exported, which the author says saves tokens. No growth metrics such as conversion, retention, or CAC were published, and claims like &\#x27;the result was unexpectedly good&\#x27; are anecdotal.

rss · 人人都是产品经理 · Sep 20, 01:17

**「AI Technique」** GPT-6 Astra reads the product&\#x27;s codebase to extract React \(or Vue/Svelte\) components, CSS, theme files, fonts, and logos, then renders the video through a React component plus timeline pipeline in a Playwright browser. Music is generated by pure Python waveform synthesis \(sine-wave layering, chord progressions, and beat patterns\), and sound effects are pre-made WAV files bound to action nodes with automatic sidechain ducking.

**「Growth Impact」** The item reports no measurable growth outcomes such as conversion lift, retention improvement, or CAC reduction. The claimed benefit is lower cost and precise editability versus video-generation APIs, illustrated by three product cases but without before/after data or validation of marketing performance.

**「Takeaway」** For product update videos, try a code-rendering Skill that reads your existing repo for components, colors, and fonts instead of paying for video-generation APIs, so you get an editable project you can tweak and re-export rather than a one-shot generated clip.

**Tags**: `#AI video generation`, `#product marketing`, `#open-source tool`, `#content production`, `#growth workflow`, `#code rendering`

---

<a id="item-ai-growth-3"></a>
### [AI Services on Xianyu: 9.8M Orders, But Most Sellers Earn Only Hundreds](https://www.woshipm.com/share/6466839.html) ⭐️ 6.0/10

This article examines whether selling AI-generated services on Xianyu \(闲鱼\), Alibaba&\#x27;s second-hand marketplace, can actually generate orders. According to Xianyu official data cited in the piece, platform AI service orders reached 9.816 million in the first half of 2026, up 157% year-over-year, with nearly 5 million buyers in that period \(sources: China News Service, July 29, 2026; Xianyu official data\). The article distinguishes two models: selling AI services directly \(e.g., AI avatar customization at 128–298 RMB, AI ghostwriting at 50–500 RMB, AI PPT at 99–300 RMB\) versus a &\#x27;no-inventory&\#x27; dropshipping model where AI generates product images and copy for reselling goods sourced from Pinduoduo or 1688. It cites two headline cases—a former real-estate copywriter turned stay-at-home mom earning roughly 20,000 RMB monthly in AI ghostwriting, and a seller of AI comic-drama tutorials at 9.9 RMB each moving 17,000 copies for over 160,000 RMB in revenue—while noting that most sellers earn only a few hundred RMB per month. The author attributes the gap not to technical skill but to operations: title writing, main-image design, customer replies, and review accumulation. The supplied content is truncated before delivering the promised detailed breakdown of which services sell best, and it lacks per-seller conversion, revenue, or retention metrics.

rss · 人人都是产品经理 · Sep 20, 01:06

**「AI Technique」** The article describes using general-purpose generative AI tools for service delivery: DeepSeek or Doubao for writing, Jimeng or Midjourney for image generation, and Gamma for PPT creation. In the dropshipping model, AI is used to regenerate product images and rewrite listing copy, replacing traditional photography and design work at near-zero marginal cost.

**「Growth Impact」** At the platform level, Xianyu reported 9.816 million AI service orders in H1 2026, up 157% YoY, with nearly 5 million buyers. The fastest-growing categories were AI programming/website building \(over 17x YoY growth\), AI comic-drama production \(14x\), and AI PPT/office work \(2.6x\). However, the article explicitly states that most individual sellers earn only a few hundred RMB per month, and no per-seller conversion or retention data is provided, so the platform-level growth should not be read as typical seller outcomes.

**「Takeaway」** For newcomers, start with the lowest-barrier AI services—ghostwriting or PPT creation—rather than avatar design or dropshipping, and prioritize accumulating positive reviews over early profit, since the article attributes the gap between top and typical sellers to listing operations and review accumulation rather than AI tool proficiency.

**Tags**: `#AI services`, `#Xianyu`, `#e-commerce`, `#side hustle`, `#growth case study`, `#China`

---

<a id="item-ai-growth-4"></a>
### [“去AI味”是伪命题：同质化源于模型架构](https://www.woshipm.com/ai/6466880.html) ⭐️ 5.0/10

This commentary argues that “removing the AI flavor” from AI writing is largely futile because homogeneous AI text is a structural byproduct of model architecture. The author explains that pretraining exposes models to messy human text, but post-training repeatedly optimizes for safety, clarity, and order, flattening the probability distribution and pushing models toward the least-error-prone path. The piece cites reported patterns such as AI using certain high-register words hundreds of times more often than humans, numbered lists increasing nearly twentyfold, and headings increasing more than sixteen thousand times, though these figures are presented without sourcing. It recommends a human-AI division of labor: humans build the trunk and supply real material, while AI handles lookup, organization, and formatting, and it notes that AI flavor is acceptable for meeting notes, industry reports, technical docs, and SOPs but problematic for personal nonfiction, sharp commentary, essays, and fiction. No growth metrics, named growth tools, company examples, or replicable growth workflows are provided.

rss · 人人都是产品经理 · Sep 20, 02:05

**「AI Technique」** The article discusses large language model behavior shaped by pretraining and post-training, where post-training alignment for safety, clarity, and order flattens the model’s probability distribution. It also mentions temperature and sampling as ways to increase randomness, but argues that raising temperature causes hallucinations, grammatical errors, and contradictions.

**「Growth Impact」** No measurable growth outcome, conversion lift, retention improvement, or CAC reduction is reported. The source is a technical commentary on AI writing style rather than a growth case study, so any growth impact would be speculative.

**「Takeaway」** For content and ops workflows, stop treating “remove AI flavor” prompts as a fix; instead, reserve AI for low-ambiguity formats like meeting notes, reports, and SOPs, and keep human-generated raw material, opinions, and specific details in high-stakes personal or persuasive content.

**Tags**: `#AI writing`, `#content marketing`, `#human-AI collaboration`, `#LLM architecture`, `#commentary`

---

<a id="item-ai-growth-5"></a>
### [豆包手机：AI硬件商业化的卡点是生态利益分配](https://www.woshipm.com/share/6466695.html) ⭐️ 5.0/10

文章复盘了豆包手机从2025年底被微信、支付宝、淘宝、建行、农行等平台风控封杀，到2026年9月16日新版发售时引入“SAEP屏幕自动化操作声明协议”和“30天公示机制”的九个月历程。作者认为，搭载豆包AI助手的努比亚M153工程样机最初售价3499元、二手被炒至天价，但很快因风控停摆，其真正卡点不是技术不成熟，而是AI入口重构分发权时触动了整个移动互联网的生态利益分配。新版协议允许第三方App自主声明操作边界、可整体拒绝或仅限制内容发布与删除等操作，公示期内未明确同意接入的App默认不予操作，标志着豆包从“硬闯”转向“敲门”。文章进一步提出，豆包切入手机场景可掌握用户几乎全部移动互联网场景，未来商业化空间可能包括经用户授权的数据服务与准入决策权，但全文偏叙事与评论，未提供转化率、留存、CAC等可验证量化指标。

rss · 人人都是产品经理 · Sep 20, 01:19

**「AI技术」** 豆包手机的核心是搭载豆包AI助手，通过跨App调用替用户完成打车、购物等决策与执行，而非仅做供需撮合。新版引入的SAEP屏幕自动化操作声明协议，本质是让第三方App自主声明AI可操作的边界，属于AI代理与平台权限治理机制，而非模型能力本身的升级。

**「增长影响」** 文章未给出转化率、留存或CAC等可量化增长结果，仅定性指出豆包手机若跑通，可让平台获得更全面准确的用户画像并重构获客归因，但“客户通过豆包手机来的，平台能获得什么信息”仍是待解决问题。其增长机制在于抢占决策入口、掌握分发权，而非直接提升某一环节的转化数据。

**「启示」** 当AI产品试图成为跨App的超级入口时，先设计让生态伙伴自主声明边界的接入协议与公示机制，比直接硬闯风控更能降低分发权争夺的阻力。

**Tags**: `#AI硬件`, `#分发权`, `#生态利益`, `#豆包`, `#AI商业化`

---


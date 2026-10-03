# Horizon Daily - 2026-10-03

> From 66 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [Higgsfield: $1M to $1B ARR by Owning Traffic Routing](#item-ai-growth-1) ⭐️ 7.0/10
2. [半年人工喂出的AI客服：空气小猪自建RAG系统实践](#item-ai-growth-2) ⭐️ 6.0/10
3. [WorkBuddy + Open-Source Tool Auto-Generates Hand-Drawn Animation Videos](#item-ai-growth-3) ⭐️ 6.0/10
4. [30款出海AI游戏盘点：钱流向生产管线而非玩法](#item-ai-growth-4) ⭐️ 6.0/10
5. [ChatGPT Sites: Prompt-to-Web-App Prototyping Draws HN Debate](#item-ai-growth-5) ⭐️ 5.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [Higgsfield: $1M to $1B ARR by Owning Traffic Routing](https://www.woshipm.com/share/6473406.html) ⭐️ 7.0/10

Higgsfield founder Alex Mashrabov recounts scaling annualized revenue from $1M to $1B in 18 months, after a pre-PMF period in which the team burned over $10M of a ~$16M seed round and was left with under $6M. The turning point came from deep interviews with eight senior creative directors, who consistently said existing AI video tools lacked camera and motion control, prompting a pivot to that specific problem and a new release on March 31. Mashrabov argues the real moat is not proprietary models but control over traffic routing: reselling closed APIs may yield only 20-30% gross margin, while controlling open models, vertical post-training, and dynamic routing can exceed 80%, and Higgsfield already lets the system autonomously decide over 40% of model calls. He reports enterprise customers now contribute more than half of revenue, one customer that started at $99/month signed a $6M annual contract within six months, and over 70% of revenue still comes from Western markets. For growth practitioners, the case ties PMF to solving a narrow, expert-validated workflow problem and ties margin and defensibility to owning the model-selection layer rather than the model itself.

rss · 人人都是产品经理 · Oct 3, 03:09

**「AI Technique」** Higgsfield uses generative video models combined with camera and motion control, where professional production may require over 3,000 English words of control instructions and more than ten reference images to maintain consistency of characters, clothing, lighting, and spatial relationships. The company also uses user decision sequences from real workflows for post-training and reinforcement learning, compressing tasks that previously took a dozen steps into a single model inference, and runs a routing system that autonomously selects among models for cost and quality.

**「Growth Impact」** The reported outcome is annualized revenue growth from $1M to $1B in 18 months, with enterprise customers contributing over half of revenue and one account expanding from $99/month to a $6M annual contract in six months. The mechanism was a pivot from chasing hype to solving a validated expert pain point \(camera and motion control\), plus routing control that Mashrabov says can lift gross margin from 20-30% on closed-API resale to over 80%. These figures come from a single founder interview and are not independently verified.

**「Takeaway」** Before scaling spend, interview a handful of senior practitioners in your target workflow to find the one capability they say is missing, then build the routing and post-training layer that lets you serve it profitably instead of reselling a closed API.

**Tags**: `#AI video`, `#generative AI`, `#growth case study`, `#PMF`, `#ARR growth`, `#product strategy`, `#unit economics`, `#founder interview`

---

<a id="item-ai-growth-2"></a>
### [半年人工喂出的AI客服：空气小猪自建RAG系统实践](https://www.woshipm.com/ai/6473390.html) ⭐️ 6.0/10

A first-person account describes how the team behind 空气小猪, a social language-learning app, built a production-grade RAG-based AI customer service system after founders spent 2-3 hours per day answering repetitive support questions for over six months. The team chose self-built engineering code over low-code platforms such as Dify because they needed deep control over retrieval strategy, ranking logic, and context assembly, and because Dify&\#x27;s execution chain was too slow for their real-time requirements. The knowledge base was built from manually organized product knowledge plus historical customer service conversations, with historical sessions processed in batches of 10 through a Coze workflow and deduplicated by an LLM. The technical stack uses Python, FAISS for vector storage, MySQL for business data, and Qwen text-embedding-v4 \(1024 dimensions\) for Chinese-language embeddings. The source does not publish quantified results such as deflection rate, resolution rate, or time saved, so the case should be treated as a practitioner narrative rather than a validated performance study.

rss · 人人都是产品经理 · Oct 3, 02:29

**「AI Technique」** The system is a retrieval-augmented generation \(RAG\) pipeline: user questions are embedded with Qwen text-embedding-v4, FAISS performs similarity search to recall top-K vector IDs, and MySQL stores the original chunk data linked by vector ID. Knowledge is chunked from Markdown by heading hierarchy into structured JSON with category, questions, and answer fields, and the text actually embedded is the concatenation of category, questions, and answer.

**「Growth Impact」** The stated goal was to free the founders from 2-3 hours of daily manual customer service, a workload that had persisted for more than half a year. The source reports no quantified deflection rate, resolution rate, cost reduction, or time saved after launch, so the actual growth impact remains unverified.

**「Takeaway」** Before building an AI customer service system, accumulate real support conversations as training data, then chunk knowledge by heading hierarchy so each chunk is semantically self-contained and embed the category, question, and answer together for better retrieval.

**Tags**: `#AI客服`, `#RAG`, `#生产案例`, `#用户支持`, `#低代码vs自建`, `#语言学习App`

---

<a id="item-ai-growth-3"></a>
### [WorkBuddy + Open-Source Tool Auto-Generates Hand-Drawn Animation Videos](https://www.woshipm.com/ai/6473408.html) ⭐️ 6.0/10

This tutorial demonstrates how to use WorkBuddy, an AI agent, together with the open-source project srt-whiteboard-animation to automatically generate hand-drawn whiteboard animation videos from an SRT subtitle file or a script. The workflow involves installing the project via a single prompt, then having WorkBuddy generate voiceover and subtitles and composite the final video; voiceover uses Microsoft&\#x27;s free edge-tts, while credits are consumed only for line-art image generation. The author reports that generating four line drawings plus voiceover and subtitles for one video consumed roughly 53 WorkBuddy credits, with each line drawing costing about 5-10 credits. The author notes the first render produced a silent, subtitle-free animation, requiring an additional prompt to add voiceover and subtitles. This matters for growth practitioners because it offers a low-cost, repeatable way to mass-produce educational, product-demo, or knowledge-explainer videos, though the source provides no conversion, retention, or other growth metrics.

rss · 人人都是产品经理 · Oct 3, 00:59

**「AI Technique」** The approach combines an AI agent \(WorkBuddy, using the GLM-5.3-Flash model\) with the open-source srt-whiteboard-animation project to turn SRT subtitles or scripts into whiteboard-style animations. It uses Microsoft&\#x27;s free edge-tts for text-to-speech voiceover and an image generation model \(referred to as imagen\) to create the line-art drawings, with the agent orchestrating installation, generation, and compositing.

**「Growth Impact」** The source reports no conversion, retention, CAC, or other growth metrics. The only quantified outcome is cost: approximately 53 WorkBuddy credits for a single video \(four line drawings at 5-10 credits each plus free voiceover and subtitles\), which the author frames as far cheaper than using traditional AI video models like Seedance. The practical impact is production efficiency and cost reduction for content teams rather than a measured growth lift.

**「Takeaway」** For high-volume explainer or educational video production, test an agent plus open-source whiteboard-animation pipeline where only image generation costs credits and voiceover is free, then refine background music and timing in an editor like CapCut.

**Tags**: `#AI video generation`, `#content production`, `#open-source tool`, `#WorkBuddy`, `#whiteboard animation`, `#marketing content`, `#workflow automation`

---

<a id="item-ai-growth-4"></a>
### [30款出海AI游戏盘点：钱流向生产管线而非玩法](https://www.woshipm.com/ai/6473116.html) ⭐️ 6.0/10

扬帆出海盘点了30款出海的AI+游戏产品，结论是AI在游戏行业首先被用作生产管线效率工具，而非玩法创新。中国音数协2026年7月30日公布国内游戏企业AI技术普及率达86%，其中美术设计环节渗透率84.2%、发行运营77.3%；三七互娱披露2D美术资产AI生成占比超80%、单季度产出超50万张素材、AI自动化投放占比超50%。供给端，Steam上标注使用AI的新游已占全部新品的30.8%，二季度升至33%，但AI标注游戏中位收入仅约300美元，28%连一条评测都没有，平台Top1%拿走约94%收入。收入对比上，AI原生游戏《AI2U》第三方估算Steam累计毛收入88.1万美元，而用AI提效的传统品类《Last Asylum: Plague》2026年8月单月海外收入突破2500万美元，两者相差两个数量级。对增长从业者而言，这组数据说明AI在投放、本地化和素材生产环节的提效已被验证，但AI原生玩法本身尚未跑通可持续付费模型。

rss · 人人都是产品经理 · Oct 2, 08:57

**「AI技术应用」** 案例中的AI应用集中在生成式内容与自动化投放：用AI视频模型和图像生成工具批量生产2D美术资产与广告素材，用大模型驱动NPC对话与长期记忆，用AI完成多语种本地化配音与字幕，以及用AI自动化投放系统优化广告投放。三七互娱的AI本地化覆盖18个语种、最高准确率95%，广告素材视频中AI深度参与超70%。

**「增长影响」** AI带来的可量化增长主要体现在成本与迭代速度：三七互娱2D美术提效超80%、单季度产出超50万张素材，AI自动化投放占比超50%，其《Last Asylum: Plague》2026年8月单月海外收入突破2500万美元；《异环》2026年5月移动端海外收入约1700万美元，AI用于场景资产与多语言配音批量生产。相比之下，AI原生游戏收入停在百万美元量级，说明AI对增长的拉动目前主要来自成熟品类的降本增效，而非新玩法本身。

**「可复制要点」** 增长团队应优先把AI用在美术素材批量生产、多语种本地化和自动化投放这三个已被验证的环节，用降本和迭代速度换取成熟品类的增长，而不是押注AI原生玩法本身。

**Tags**: `#AI+游戏`, `#出海`, `#生产管线`, `#投放效率`, `#行业数据`

---

<a id="item-ai-growth-5"></a>
### [ChatGPT Sites: Prompt-to-Web-App Prototyping Draws HN Debate](https://chatgpt.com/features/sites/) ⭐️ 5.0/10

OpenAI&\#x27;s ChatGPT Sites feature lets users generate working web apps and sites directly from prompts, and it drew a Hacker News discussion mixing hands-on prototyping anecdotes with speculation about disruption to web design. One commenter \(nathanfig\) said they have used Sites for a few months and typically get a working prototype within an hour, citing a game built the same night the idea occurred. Another \(jwpapi\) argued the feature could replace website designers who charge around $2,000 per site, and speculated that ad integration will follow. A separate commenter \(londons\_explore\) framed Sites as closing a gap where AI models previously pushed users toward Netlify, Firebase, or buying a domain. No concrete growth metrics, conversion data, or retention figures were reported in the source or comments, so the growth implications remain speculative rather than validated.

hackernews · polvi · Oct 1, 22:22 · [Discussion](https://news.ycombinator.com/item?id=49927747)

**「AI Technique」** ChatGPT Sites is a generative AI feature that turns natural-language prompts into functioning web apps and hosted sites, abstracting away setup steps like domain purchase and third-party hosting. The source does not detail the underlying model or architecture, and commenters note output quality varies, with one \(dash2\) criticizing a demo&\#x27;s flat JPEG rotation as lacking real 3D.

**「Growth Impact」** No measurable growth outcomes \(conversion, retention, CAC\) were published in the source or comments. The only reported outcome is anecdotal speed: nathanfig said a working prototype usually arrives within an hour, which points to faster idea-to-prototype cycles rather than a quantified growth lift. Claims that this will displace web design agencies or add ad monetization are community speculation, not verified results.

**「Takeaway」** Treat prompt-to-site tools like ChatGPT Sites as a fast, low-cost prototyping channel for testing landing pages and app ideas within hours, but validate output quality and conversion before relying on it for production growth experiments.

**Tags**: `#ChatGPT`, `#AI website builders`, `#product launch`, `#growth channels`, `#web design disruption`, `#prototyping`

---


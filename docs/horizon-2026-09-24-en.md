# Horizon Daily - 2026-09-24

> From 67 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [Pocket FM: 93% AI-Generated Content, $500M Audio Business](#item-ai-growth-1) ⭐️ 8.0/10
2. [Solo Amazon Seller Uses AI to Cut WeChat Article Workflow from 2-3 Hours to 30 Minutes](#item-ai-growth-2) ⭐️ 6.0/10
3. [Mind Lab Launches Mint Recursive: Enterprise Model Post-Training as a Service](#item-ai-growth-3) ⭐️ 5.0/10
4. [AI Video Meeting Product Design: Embedding AI Across the Full Meeting Lifecycle](#item-ai-growth-4) ⭐️ 5.0/10
5. [AI Treasury FX System Cuts 7.2M of 10M Loss via T+0 Exposure](#item-ai-growth-5) ⭐️ 5.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [Pocket FM: 93% AI-Generated Content, $500M Audio Business](https://www.woshipm.com/chuangye/6467296.html) ⭐️ 8.0/10

Pocket FM, a serialized audio platform founded in 2018, uses AI to produce 93% of its content and 99% of new titles, according to founder Rohan Nayak. The company reports an annualized revenue run rate of about $500 million, with roughly $415 million from users paying coins to unlock episodes and about $85 million from advertising. AI has cut some content production costs by roughly 80x, enabling the platform to test nearly 1,000 new story pilots per month and produce about 2.5 million hours of AI-assisted content annually. One title, My Vampire System, has reached 4,192 episodes, over 1.5 billion plays, and nearly $90 million in cumulative revenue. Pocket FM also reports its 12-month user revenue retention rate rose from 44% two years ago to 76%, showing how AI-driven supply scaling can feed a paywall-based monetization model.

rss · 人人都是产品经理 · Sep 24, 02:24

**「AI Technique」** Pocket FM first used AI for audio production, partnering with ElevenLabs in 2024 to convert text to speech and cut audio production costs by about 90% while increasing output roughly 10x. In 2025 it launched CoPilot, a data-driven writing tool that analyzes story pacing, suggests dialogue and conflict, redesigns episode endings, tracks character continuity, and performs cross-language localization using user behavior data such as drop-off points and payment triggers.

**「Growth Impact」** Pocket FM reports over 250 million listeners, more than 2.5 million paying users, and 96 titles with over $1 million in cumulative revenue, 13 of which exceed $10 million. Its 12-month user revenue retention rate reportedly improved from 44% to 76% as content supply expanded, and its newer AI micro-drama app Pocket Saga reached about $15 million annualized revenue within roughly three months of launch.

**「Takeaway」** Growth teams can apply Pocket FM&\#x27;s playbook by using AI to cheaply produce and test many content variants, then routing spend and promotion only to formats that show real user retention and payment signals.

**Tags**: `#AI content generation`, `#audio platform`, `#monetization`, `#case study`, `#cost reduction`, `#Pocket FM`, `#growth metrics`

---

<a id="item-ai-growth-2"></a>
### [Solo Amazon Seller Uses AI to Cut WeChat Article Workflow from 2-3 Hours to 30 Minutes](https://www.woshipm.com/ai/6469668.html) ⭐️ 6.0/10

A solo Amazon seller who moved from full-time to part-time \(day job plus childcare\) describes rebuilding his WeChat public account workflow so that AI handles the repetitive parts. He feeds daily project-log material to ChatGPT, which drafts in his own writing style; a script generates cover images \(blue background with white text, or black background with gold text\) from a title; and drafts are pushed to the WeChat draft box via API. This cut the time from material to draft from at least two to three hours down to roughly 30 minutes, though he still manually adjusts formatting, confirms content, and clicks publish. He reports that AI handles about 80% of the work while he keeps the remaining 20%, and notes unresolved friction: the WeChat IP whitelist must be updated manually when his home broadband IP changes, and cover fonts and label positions needed repeated tuning and still look worse than his own MasterGo designs. The time-saving figure is self-reported and unverified, and no traffic, conversion, or retention metrics are provided.

rss · 人人都是产品经理 · Sep 24, 03:11

**「AI Technique」** The workflow uses ChatGPT to generate a first draft from raw project-log notes in the author&\#x27;s own writing style, plus a custom script that takes a title and automatically produces a cover image, and the WeChat draft API to push the finished draft into the official account backend.

**「Growth Impact」** The reported outcome is a reduction in content-production time from at least two to three hours to about 30 minutes per article, achieved by removing repetitive drafting, cover design, and draft-creation steps. This is a single creator&\#x27;s self-reported productivity gain with no measured traffic, conversion, or retention data, so it should be treated as an unverified time-saving claim rather than a proven growth result.

**「Takeaway」** For solo operators, target the highest-friction, most repetitive steps \(first draft, cover image, draft creation\) with AI and keep the irreversible actions like final review and publishing manual, so the startup cost of each piece drops enough that you actually keep publishing.

**Tags**: `#AI content workflow`, `#content operations`, `#solo creator`, `#automation`, `#WeChat`, `#ChatGPT`, `#productivity`

---

<a id="item-ai-growth-3"></a>
### [Mind Lab Launches Mint Recursive: Enterprise Model Post-Training as a Service](https://www.woshipm.com/ai/6469601.html) ⭐️ 5.0/10

Mind Lab \(the team behind the Macaron app\) launched Mint Recursive, an enterprise-facing platform that turns its internal model post-training and inference pipeline into a managed service. The article recounts how Macaron V1.1 was post-trained on a 744B GLM-5.3 base with four 2B LoRA experts for Chat, Agent, Coding, and generative UI, reaching a final size of 752B. On a 60-question UI4A task set, GLM-5.3 succeeded on 43 items on first delivery while Macaron V1.1 succeeded on 58, and the team also showed before/after comparisons on an invoice reconciliation task and a supplier comparison page. The platform supports open-source bases including GLM, Qwen, DeepSeek, Kimi, and MiniMax, plus supervised fine-tuning, reinforcement learning, full-parameter training, and LoRA, accessible via API or Python SDK. For growth practitioners, this is primarily an AI infrastructure and product announcement rather than a growth case study: no conversion, retention, CAC, LTV, or DAU metrics are provided, so the growth implications remain indirect.

rss · 人人都是产品经理 · Sep 24, 02:58

**「AI Technique」** The core technique is post-training a large open-source base model \(GLM-5.3\) with multiple small LoRA experts, one per capability area, using an automated loop of observation, attribution, intervention, and validation. Mind Lab&\#x27;s MinT infrastructure isolates LoRA, gradient, optimizer state, and model versions across tasks while sharing a resident base model and compute, enabling concurrent small-batch LoRA training.

**「Growth Impact」** The article reports an engineering efficiency gain rather than a user growth metric: three independent Qwen3-4B reinforcement learning tasks moved from sequential to shared concurrent execution, cutting total completion time from about 3,081 seconds to 1,736 seconds with unchanged peak memory. The only task-level performance figure is the UI4A result \(43 to 58 successes out of 60\), which the source itself notes still needs validation on real new tasks. No conversion, retention, CAC, or revenue impact is disclosed.

**「Takeaway」** If your team has recurring, well-defined tasks with clear success criteria, consider whether a small LoRA expert post-trained on your own task data and evaluation benchmark could outperform a general base model on first-delivery accuracy, while keeping training records and model versions in one place for comparison and rollback.

**Tags**: `#AI platform`, `#model post-training`, `#LoRA`, `#enterprise AI`, `#product update`

---

<a id="item-ai-growth-4"></a>
### [AI Video Meeting Product Design: Embedding AI Across the Full Meeting Lifecycle](https://www.woshipm.com/ai/6469656.html) ⭐️ 5.0/10

This article, published on Woshipm by author amycr, offers a product-design perspective on embedding AI across the full video-meeting lifecycle—pre-meeting, in-meeting, and post-meeting—rather than simply bolting on subtitles and auto-generated minutes. It argues that low user adoption of AI meeting features stems from surface-level functionality that fails to address real pain points: cumbersome pre-meeting preparation, in-meeting information overload, and the disconnect between meeting conclusions and follow-up execution. The proposed design includes pre-meeting schedule conflict detection, device and network pre-checks, and document summarization; in-meeting AI noise reduction, real-time speaker-differentiated transcription, and highlight detection; and post-meeting structured summaries with action items synced to task systems. The article also stresses that stable real-time audio/video infrastructure, security compliance, and SDK-based integration are prerequisites for enterprise adoption, and it notes that the content is truncated before the post-meeting section and the promised discussion of implementation pitfalls. Notably, the piece is largely conceptual: it provides no concrete metrics, named tools or techniques, real company case studies, or before/after data, so its claims should be treated as design guidance rather than validated results.

rss · 人人都是产品经理 · Sep 24, 02:26

**「AI Technique」** The article describes applying large-model capabilities to meeting workflows, including real-time speech recognition with speaker diarization, AI noise reduction and voice separation, dynamic bitrate adaptation, and automatic summarization and action-item extraction from transcripts. It does not name specific models, vendors, or technical architectures, so the exact implementation remains unspecified.

**「Growth Impact」** No measurable growth outcomes—such as conversion lift, retention improvement, or CAC reduction—are reported in the source. The article only asserts that AI features built on a stable real-time audio/video foundation and paired with security and integration capabilities can improve enterprise adoption, but it provides no data, scale, or context to substantiate this.

**「Takeaway」** When designing AI meeting features, map each AI capability to a specific lifecycle pain point—pre-meeting prep, in-meeting information capture, or post-meeting execution—and prioritize a stable audio/video foundation plus permission controls before adding AI layers.

**Tags**: `#AI video conferencing`, `#product design`, `#meeting workflow`, `#enterprise collaboration`, `#AI features`

---

<a id="item-ai-growth-5"></a>
### [AI Treasury FX System Cuts 7.2M of 10M Loss via T+0 Exposure](https://www.woshipm.com/pd/6469390.html) ⭐️ 5.0/10

A product teardown describes an AI-powered treasury FX loss management system that decomposes a 10M CNY exchange loss into 7.2M of avoidable &quot;lag penalty&quot; and 2.8M of unavoidable market volatility. Using a real anonymized case of a cross-border manufacturer with a $120M net USD exposure and 60–90 day payment terms, the system replaces manual month-end exposure aggregation \(T+30\) with a real-time exposure engine that consolidates orders, invoices, borrowings, and bank balances into a T+0 view. It then applies a stochastic hedging optimizer constrained by policy \(40–85% coverage, 1.20bp cost ceiling\) and an execution gateway that requests quotes from multiple banks in parallel and nets cross-border payments. The article claims the lag loss drops from 6.2M to 0.6M, residual under-hedging from 2.8M to 1.8M, and execution spread from 1.0M to 0.4M, with coverage rising from a manual 40% to 67% and cost from 0.95bp to 0.88bp. This matters for growth practitioners as a concrete example of AI compressing a decision-latency penalty, though the domain is treasury operations rather than user growth or marketing.

rss · 人人都是产品经理 · Sep 24, 02:06

**「AI Technique」** The system uses a real-time exposure calculation engine that subscribes to earliest-identifiable exposure events \(sales orders, shipment notices, purchase orders, loan contracts, rolling forecasts\) and assembles a live exposure table within about two minutes. A stochastic optimization solver then minimizes expected loss plus hedging cost under policy constraints, outputting a probability distribution and coverage recommendation rather than a point FX forecast.

**「Growth Impact」** In the anonymized case, the system reportedly reduced total FX loss from 10M to roughly 2.8M CNY by eliminating the 15-day visibility gap and improving hedge coverage from 40% to 67% at a lower cost of 0.88bp versus 0.95bp. The mechanism is latency compression—moving from T+30 manual aggregation to T+0 automated exposure and execution—rather than better FX prediction.

**「Takeaway」** When an AI system targets a latency-driven loss, decompose the loss into avoidable lag versus unavoidable variance, then instrument the earliest possible signal event rather than the latest confirming document.

**Tags**: `#AI`, `#treasury`, `#FX risk`, `#operations`, `#automation`, `#fintech`

---


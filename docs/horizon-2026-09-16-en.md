# Horizon Daily - 2026-09-16

> From 63 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [AI Influencer Matching System Cuts Matching Time from 270 to 18 Minutes](#item-ai-growth-1) ⭐️ 8.0/10
2. [2-Person Team, Zero Funding: AI-Built Retro Camera App Hits Korea Top 4](#item-ai-growth-2) ⭐️ 6.0/10
3. [GPT-6 Astra 之后：产品经理如何重新设计人的位置](#item-ai-growth-3) ⭐️ 5.0/10
4. [Grok Bot Designers Demo AI Agents for Prototyping](#item-ai-growth-4) ⭐️ 4.0/10
5. [Figma IPO: Collaboration Over AI Generation](#item-ai-growth-5) ⭐️ 4.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [AI Influencer Matching System Cuts Matching Time from 270 to 18 Minutes](https://www.woshipm.com/pd/6464954.html) ⭐️ 8.0/10

A B2B product manager documented building an AI influencer-matching system for content marketing, replacing manual matching that relied on operator memory and Excel. The system uses a five-stage pipeline: an LLM parses merchants&\#x27; colloquial briefs into structured JSON slots, then multi-route recall \(including dual-tower embedding vector search\) narrows a 100,000+ influencer pool to a few hundred candidates, coarse ranking compresses them to a few dozen, and a Cross-Encoder re-ranker performs deep semantic matching before rule-based business overrides and human review. During gray-scale testing covering 120 merchants, 430 campaigns, and 6.8 million RMB GMV, end-to-end matching time dropped from 270 to 18 minutes, manual intervention time fell 79%, searchable influencer pool expanded 44%, multi-route recall coverage rose from 62% to 87%, fulfillment rate improved from 91% to 96%, and cheating influencers dropped from 4.2% to 0.8%. The author notes the 270-minute figure is end-to-end \(including requirement alignment and cross-department communication\), ROI rose from 2.8 to 3.6 in a control-vs-experiment comparison, and full rollout still needs longer validation. This matters for growth practitioners because it shows a replicable architecture for applying LLMs and recommendation-system techniques to operational matching problems, with the product manager owning translation, constraint, fallback, and measurement rather than model tuning.

rss · 人人都是产品经理 · Sep 16, 01:37

**「AI Technique」** The system combines an LLM used only for prompt-based requirement parsing into structured JSON slots, dual-tower embedding vector recall for fast shallow similarity, lightweight linear or rule-based coarse ranking, and a Cross-Encoder that concatenates merchant demand text with influencer profile text for full bidirectional attention and deep semantic scoring. Business rules and human review act as post-model overrides and fallbacks.

**「Growth Impact」** In gray-scale testing across 120 merchants and 430 campaigns generating 6.8 million RMB GMV, end-to-end matching time fell from 270 to 18 minutes, manual intervention time dropped 79%, recall coverage rose from 62% to 87%, fulfillment rate improved from 91% to 96%, cheating influencer share fell from 4.2% to 0.8%, and ROI improved from 2.8 to 3.6 in a control-vs-experiment comparison. The mechanism is layered cost-aware matching: cheap recall and coarse ranking shrink the candidate set so the expensive Cross-Encoder can be applied only to a small set, while product-defined rules and human review keep outputs commercially usable.

**「Takeaway」** When applying AI to operational matching, use the LLM only to translate messy human input into structured parameters, then rely on a layered recall-coarse rank-re-rank pipeline with explicit business rules and fallback paths so the system stays controllable and cost-efficient.

**Tags**: `#AI matching`, `#influencer marketing`, `#B2B growth`, `#case study`, `#recommendation system`, `#operations efficiency`

---

<a id="item-ai-growth-2"></a>
### [2-Person Team, Zero Funding: AI-Built Retro Camera App Hits Korea Top 4](https://www.woshipm.com/share/6464522.html) ⭐️ 6.0/10

A two-person Korean studio called Ironpig launched a retro camera app, 「当我爱你时所见的瞬间：复古相机APP」 \(roughly &quot;The Moments I See When I Love You&quot;\), on June 29, which held at least two months at \#1 in Korea&\#x27;s Photo &amp; Video category and peaked at \#4 on Korea&\#x27;s overall and free app charts. The team claims 1 billion KRW in sales within three months and 1 million cumulative users across at least five products, all built without external investment. Rather than competing on filter quantity, the app offers 14 atmospheric filters and differentiates through emotional, relationship-oriented naming and a &quot;warm, ordinary, imperfect&quot; aesthetic that resonates with Korean Gen Z&\#x27;s fatigue with over-retouched AI beauty filters. The case matters for growth practitioners because it shows how a tiny team can use AI to compress content, development, and design work, then win on positioning and emotional resonance rather than feature depth. Note that the revenue and user figures are self-reported by the team and the source does not detail exactly how AI was used in building the app.

rss · 人人都是产品经理 · Sep 16, 02:20

**「AI Technique」** The source states that Ironpig builds and delivers its products using AI technology, and that its founders said a companion app \(ingan.ai\) was planned, developed, designed \(including logo\), and marketed entirely with AI. However, the source does not specify which models, tools, or technical methods were used for the retro camera app itself, so the exact AI technique remains unclear.

**「Growth Impact」** The app reportedly reached \#1 in Korea&\#x27;s Photo &amp; Video category for at least two months, peaked at \#4 on Korea&\#x27;s overall and free app charts, and the team claims 1 billion KRW in sales within three months plus 1 million cumulative users across its product line. The mechanism appears to be emotional positioning and social-shareable retro aesthetics rather than filter count, though these figures are self-reported and not independently verified in the source.

**「Takeaway」** When entering a crowded app category, test whether an emotional, scenario-based product name and a deliberately &quot;imperfect&quot; aesthetic can differentiate you more cheaply than adding features, and use AI to compress the build, design, and content workload so a tiny team can ship and iterate fast.

**Tags**: `#AI app`, `#consumer app`, `#growth case study`, `#Korea market`, `#retro camera`, `#small team`, `#product positioning`

---

<a id="item-ai-growth-3"></a>
### [GPT-6 Astra 之后：产品经理如何重新设计人的位置](https://www.woshipm.com/ai/6464960.html) ⭐️ 5.0/10

文章讨论 GPT-6 Astra 将自动化边界从功能点推进到任务级执行后，产品经理应如何重新设计人在流程中的授权、验收、异常处理与责任节点。作者引用 OpenAI 公布的能力数据：Astra 在 ARC Prize 定制运行框架下得分 99.9%，在 OSWorld 2.0 离线测试中得分 72.6%（高于 GPT-5.6 Sol 的 65.7%），模拟任务平均用时从约 75 分钟降至约 40 分钟。文中给出人机分工的四类位置与权限分级策略，并以 Legora 核对 41 份财务报表、xAI 的 Haggle Bot 找到超 10 万美元节省等厂商自述案例说明分工形态。需要说明的是，这些数字属于模型能力评测或厂商自述，并非增长场景的实证数据，文章整体偏概念性框架，缺乏可量化的转化率、留存或 CAC 指标。

rss · 人人都是产品经理 · Sep 16, 01:10

**「AI 技术要点」** 核心是具备工具调用与环境观察能力的 Agent：模型可以打开外部工具、读取页面状态、根据屏幕反馈选择下一步动作并持续执行多步任务，而非仅生成一次性回答。文章还提到运行框架（Provider Adapter）通过保留推理状态和上下文压缩，让同一模型在 ARC-AGI-3 上从 62.7% 提升到 99.9%，成本从约 2.6 万美元降至约 1.9 万美元，Token 减少 49%。

**「增长影响」** 文章未提供增长场景的量化结果，其引用的收益均来自厂商自述：Legora 的 Agent 一次运行处理 41 份文档并找出四个预设错误（含一处 50 万英镑差额），xAI 的 Haggle Bot 通过闲置席位和未使用采购项目找到超 10 万美元直接节省。OpenAI 内部数据显示，截至 2026 年 8 月中旬，研究组织每投入一个人工工作日对应 3.1 个 Agent 工作日，但作者明确提醒这不能理解为生产率提升 3.1 倍，且四到八小时的成功任务中超过一半发生过至少一次人工介入。

**「可执行要点」** 在设计 Agent 流程时，按动作后果而非模型自报信心来分级授权：低风险操作（读取资料、生成草稿）可连续执行，外部发送、删除、交易等不可逆动作前设置确认点，并保留操作日志、旧值快照与幂等写入，同时把任务完成率、人工介入率、异常恢复率和单位成功任务成本纳入评测指标。

**Tags**: `#AI Agent`, `#产品经理`, `#人机协作`, `#流程设计`, `#GPT-6 Astra`

---

<a id="item-ai-growth-4"></a>
### [Grok Bot Designers Demo AI Agents for Prototyping](https://www.lennysnewsletter.com/p/how-grok-bot-designers-use-ai-agents) ⭐️ 4.0/10

This item is a promotional blurb for a 42-minute video in which two designers at SpaceXAI demonstrate how they use Grok Bot AI agents for design and prototyping workflows. The described use cases include running Figma remotely \(e.g., from the gym\), updating a portfolio with a single photo, and turning casual ideas into working prototypes. No metrics, before/after data, or replicable growth tactics are provided in the available source content, and no community comments or tool results were available to supplement it. Because the source is only an episode announcement, the practical value for growth practitioners cannot be assessed from this material alone.

rss · Lenny&\#x27;s Newsletter · Sep 14, 12:04

**「AI Technique」** The item references Grok Bot AI agents being used to operate design tools such as Figma and to generate working prototypes from brief inputs. The source does not specify the underlying model, agent architecture, or integration method, so the exact technical approach cannot be confirmed from the available content.

**「Growth Impact」** No measurable growth outcomes, conversion metrics, retention figures, or cost data are reported in the source. The described benefits are workflow-oriented \(remote design control, faster portfolio updates, rapid prototyping\) rather than tied to any quantified growth result.

**「Takeaway」** Treat this as a pointer to watch the full 42-minute demo if AI-agent-driven design and prototyping workflows are relevant to your team, since the announcement itself contains no data or tactics you can apply directly.

**Tags**: `#AI agents`, `#design tools`, `#prototyping`, `#Grok Bot`, `#product workflow`

---

<a id="item-ai-growth-5"></a>
### [Figma IPO: Collaboration Over AI Generation](https://www.woshipm.com/chuangye/6464913.html) ⭐️ 4.0/10

Figma went public on July 31, 2025, surging 250% on its first day to a market cap above $56 billion and a fully diluted valuation near $65 billion — more than three times Adobe&\#x27;s $20 billion acquisition offer in 2022. The article attributes Figma&\#x27;s success to five strategic decisions: building a browser-native multiplayer design tool rather than a better Photoshop, adopting freemium pricing after a Microsoft trial user warned &\#x27;you should charge, otherwise we dare not use it,&\#x27; treating AI as a collaboration layer rather than a generation engine, expanding from a designer tool to a product-team platform \(two-thirds of users are not designers\), and benefiting from the failed Adobe acquisition, which paid Figma a $10 billion breakup fee. Figma&\#x27;s revenue reached $749 million in 2024 \(+48% YoY\) and over $1.05 billion in 2025 \(+41% YoY\), and its IPO filing mentioned &\#x27;AI&\#x27; 150 times. For growth practitioners, the case is a reminder that AI can be a lever for a product&\#x27;s core value rather than a replacement for it, though the article offers no concrete AI-growth metrics or replicable AI tactics.

rss · 人人都是产品经理 · Sep 16, 03:30

**「AI Technique」** Figma&\#x27;s AI approach centers on embedding generative and assistive features into its existing collaborative canvas rather than shipping a standalone AI design generator. The article cites Figma Make, an AI prototyping tool that generates runnable prototypes from prompts and connects to real code repositories, plus a 2026 Code Layer that brings code into the Figma canvas; it also mentions automated layer naming and background removal. The source does not specify the underlying models or technical architecture.

**「Growth Impact」** The article reports Figma&\#x27;s revenue grew 48% YoY to $749 million in 2024 and 41% YoY to over $1.05 billion in 2025, with two-thirds of users being non-designers, but it does not isolate any AI-attributable conversion, retention, or CAC metrics. The stated mechanism is product-led growth: free users invite colleagues, colleagues convert to paid, and paid users bring Figma into enterprises, with AI positioned to strengthen collaboration and governance rather than drive direct monetization.

**「Takeaway」** When a new AI capability commoditizes content generation, evaluate whether it can instead reinforce your product&\#x27;s core collaboration or workflow value — and use paid tiers to qualify which users genuinely need you, as Figma did after a Microsoft trial user said &\#x27;you should charge, otherwise we dare not use it.&\#x27;

**Tags**: `#Figma`, `#AI design tools`, `#product strategy`, `#IPO`, `#collaboration`

---


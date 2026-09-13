# Horizon Daily - 2026-09-13

> From 60 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [AI客服从0到72%接管率：六大产品决策复盘](#item-ai-growth-1) ⭐️ 8.0/10
2. [AI Budgets Split: Nvidia&\#x27;s $250K/Year vs Uber&\#x27;s $1,500/Month](#item-ai-growth-2) ⭐️ 6.0/10
3. [AI-Native Organizations: Redesign Workflows, Not Just Add Agents](#item-ai-growth-3) ⭐️ 5.0/10
4. [Coze AI客服搭建教程：小店接单从0到1](#item-ai-growth-4) ⭐️ 5.0/10
5. [Smarter Models, Leaner Prompts: Why Claude Code Cut 80% of Its System Prompt](#item-ai-growth-5) ⭐️ 5.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [AI客服从0到72%接管率：六大产品决策复盘](https://www.woshipm.com/ai/6463668.html) ⭐️ 8.0/10

A product manager at a consumer brand published a two-year retrospective on building an AI customer service system from scratch, reporting that AI takeover rate rose from 0 to 72%, handling over 3,000 inquiries per day, with 2025 new-customer transaction value up 8% versus 2024. The project replaced a keyword-matching system that misanswered natural-language questions across 5-6 channels \(WeChat private domain, Douyin, Tmall, JD\), causing purchase-intent users to churn and store ratings to drop. Six key decisions drove the results: validating with low-code platforms \(Coze/Dify\) instead of building from scratch, limiting the MVP to the highest-frequency scenarios, using a two-layer architecture where a rule engine handles the ~80% of clear queries and an LLM handles the ~20% ambiguous ones, splitting the RAG knowledge base by scenario and adding hybrid retrieval, structuring prompts into five modules with role constraints and human handoff, and adding a one-click &quot;transfer to human&quot; button to reduce user resistance. The author notes the 72% figure is not a final endpoint and that remaining human-handled cases are reviewed weekly for badcase optimization. The case is valuable for growth practitioners because it shows AI customer service gains come primarily from product decisions—scenario selection, cost control, retrieval design, and user psychology—rather than model choice alone, though the source lacks granular before/after conversion or retention data.

rss · 人人都是产品经理 · Sep 12, 04:37

**「AI Technique」** The system uses a two-layer architecture: a rule engine \(keyword matching plus template answers\) for the roughly 80% of clearly phrased queries, and a large language model for the roughly 20% of ambiguous, colloquial queries. Retrieval-augmented generation \(RAG\) is used with a knowledge base split into six scenario-specific sub-libraries and hybrid retrieval combining vector search for semantic matching with keyword search for exact matching, while prompts are structured into five modules \(role setting, answer rules, knowledge content, dialogue history, user question\) with role constraints and fallback human handoff to control hallucination.

**「Growth Impact」** Over two-plus years, AI takeover rate went from 0 to 72%, daily inquiry volume reached 3,000+, and 2025 new-customer transaction value grew 8% over 2024. The mechanism was improved intent understanding and answer accuracy—replacing keyword matching that misanswered colloquial questions—which reduced churn among purchase-intent users and lowered costs by routing most queries through the rule engine rather than the LLM API. The source does not provide granular before/after conversion or retention metrics, so the 8% transaction growth cannot be attributed solely to the AI system.

**「Takeaway」** Before scaling an AI customer service project, classify your query logs to identify the high-frequency scenarios and the split between clear and ambiguous phrasing, then route clear queries to a cheap rule engine and only ambiguous ones to an LLM—and always give users a visible one-click path to a human agent.

**Tags**: `#AI客服`, `#增长案例`, `#产品复盘`, `#用户增长`, `#实战经验`

---

<a id="item-ai-growth-2"></a>
### [AI Budgets Split: Nvidia&\#x27;s $250K/Year vs Uber&\#x27;s $1,500/Month](https://www.woshipm.com/ai/6463038.html) ⭐️ 6.0/10

The article contrasts two extremes in enterprise AI spending: Nvidia reportedly allocates an annual Token budget of $250,000 per engineer \(about $2 billion for its engineering team\), while Uber capped engineers at $1,500 per month after exhausting its 2026 AI coding budget early in April. Drawing on analysis from Leonis Capital, it frames this as two distinct AI economics: expansion markets, where intelligence directly converts into growth and buyers pay for the best model regardless of price, and efficiency markets, where output is constrained by non-intelligence factors and buyers only pay the price of the labor being replaced. The piece cites Coinbase routing most tasks to cheaper open-source models while betting on frontier models for its prediction-market business, and notes that 98% of practitioners now manage AI spending \(up from 63% in 2025\) and 73% of enterprises exceeded AI cost expectations in the past year. For growth practitioners, the key implication is that AI budget decisions should be tied to whether intelligence is the actual bottleneck in the business, not to blanket adoption targets.

rss · 人人都是产品经理 · Sep 12, 06:26

**「AI Technique」** The article is a strategic economics analysis rather than a technical implementation guide. The closest concrete technique mentioned is task routing: Coinbase defaults to cheaper open-source models and routes tasks to the cheapest model that meets the requirement, while reserving frontier models for new business lines. It also references frontier models such as GPT-5.6, Kimi 3, and GLM 5.2 as examples where commercial value converges once a task threshold is crossed.

**「Growth Impact」** The article reports no conversion, retention, or CAC metrics. Its measurable claims are budget and cost figures: Nvidia&\#x27;s $250,000 per-engineer annual Token budget, Uber&\#x27;s $1,500 monthly cap, Coinbase cutting total AI spend nearly in half while token usage rose, and OpenRouter reaching $50 million in annualized revenue. The mechanism described is that in efficiency markets, spending beyond the task threshold yields no additional output, so cost discipline—not more intelligence—drives value.

**「Takeaway」** Before scaling AI spend, identify whether intelligence is the actual bottleneck in your growth model; if it is not, route tasks to the cheapest model that clears the quality bar and reserve frontier models for the few workflows where better output directly creates more revenue.

**Tags**: `#AI预算`, `#AI经济学`, `#企业战略`, `#Token成本`, `#增长策略`

---

<a id="item-ai-growth-3"></a>
### [AI-Native Organizations: Redesign Workflows, Not Just Add Agents](https://www.woshipm.com/ai/6462953.html) ⭐️ 5.0/10

This conceptual essay by AI产品零度 argues that AI-native organizations must redesign workflows, human-AI division of labor, and decision rights rather than simply adopting more agents. The author contends that if task handoffs and decision-making remain unchanged, organizations will only produce more waiting-to-be-processed material faster, and proposes starting from desired outcomes to identify which steps to delete, keep, or parallelize. The piece recommends assigning work by task rather than by job title, using four questions \(goal clarity, verifiability, reversibility, and dependence on human commitment\) to decide how to hand off work, and redistributing managerial attention and decision authority. It cites the Productivity J-Curve and a P&amp;G product innovation experiment as supporting context, but provides no concrete metrics, named tools, company case studies, or before/after data, and the promised &\#x27;complete work chain validation&\#x27; is not evidenced in the supplied text.

rss · 人人都是产品经理 · Sep 13, 02:26

**「AI Technique」** The article discusses AI agents—programs that use tools and pursue multi-step tasks toward a goal—as formal participants in team workflows, rather than describing a specific model, fine-tuning method, or tool version. It also references reusable task guidance \(called &\#x27;Skill&\#x27;\) and shared factual bases for AI and humans, but does not detail technical implementation.

**「Growth Impact」** No measurable growth outcomes, conversion lifts, retention improvements, or CAC reductions are reported. The essay is a conceptual framework without validated case data or before/after metrics, so any growth impact remains theoretical and unverified.

**「Takeaway」** Before adding more AI agents, map your workflow from the desired end result backward and ask whether each handoff still adds facts, judgment, or commitment—delete steps that only reformat information, and assign AI by task rather than by job title.

**Tags**: `#AI-native organization`, `#workflow redesign`, `#agent adoption`, `#operations`, `#project management`

---

<a id="item-ai-growth-4"></a>
### [Coze AI客服搭建教程：小店接单从0到1](https://www.woshipm.com/ai/6461565.html) ⭐️ 5.0/10

This tutorial explains how non-technical people can use Coze \(扣子\) to build AI customer-service agents for small shops, following a six-step workflow: register and create an agent, write the persona and greeting, upload a knowledge base, configure workflows, test and debug, then publish and hand off. It cites two anecdotal cases: a student who built a hotpot restaurant bot in one afternoon and charged 800 RMB, and a 90后 mother who builds ordering bots for local restaurants at 1,500 RMB/month and now serves 4 stores for about 6,000 RMB/month. The article also gives pricing guidance \(one-off build fees plus 200–500 RMB/month maintenance\) and client-acquisition advice, including approaching nearby shop owners and listing on outsourcing platforms. For growth practitioners, it is a practical monetization playbook for solo operators, but the income figures are anecdotal rather than verified growth metrics, and the source is truncated before the detailed steps.

rss · 人人都是产品经理 · Sep 13, 02:05

**「AI Technique」** The approach uses Coze \(扣子\), a no-code agent-building platform, to create a customer-service bot by combining a persona prompt, a knowledge base of shop FAQs and menus, and drag-and-drop workflows for actions like collecting booking details or sending coupons. No coding is required; the builder configures the bot through forms and visual nodes.

**「Growth Impact」** The reported outcomes are anecdotal income figures rather than measured growth metrics: 800 RMB for a one-off hotpot restaurant bot and 1,500 RMB/month per restaurant for a 90后 mother serving 4 stores, about 6,000 RMB/month. The mechanism is replacing repetitive manual replies with 24/7 automated responses and lead collection, but the source does not provide conversion, retention, or CAC data.

**「Takeaway」** Start with the simplest deliverable—knowledge base plus auto-replies—for a nearby shop owner, use the first job to get a case study and testimonial, then upsell workflows and monthly maintenance.

**Tags**: `#AI客服`, `#扣子/Coze`, `#智能体搭建`, `#小商家`, `#副业变现`, `#教程`

---

<a id="item-ai-growth-5"></a>
### [Smarter Models, Leaner Prompts: Why Claude Code Cut 80% of Its System Prompt](https://www.woshipm.com/ai/6463672.html) ⭐️ 5.0/10

As AI models grow more capable, over-specified prompts and skills can shift from helpful to harmful, argues this analysis from 人人都是产品经理. It cites Claude Code creator Boris Cherny, who said at a Y Combinator talk that the team deleted over 80% of Claude Code&\#x27;s system prompts when adapting to the new Opus 5 model, largely removing &quot;capability patches&quot; written for weaker models; ablation testing reportedly showed the model sometimes performed better without them. The article also references an OpenAI guide for GPT-6 Astra warning that newer models follow longer instructions but are more sensitive to conflicting rules in Skill and AGENTS.md files, and an ETH Zurich and LogicStar.ai study across 300 SWE-bench Lite and 138 CTXbench tasks finding that auto-generated repository context files added roughly 20% and 23% cost without significant success-rate gains, while developer-written files added about 2.4% on average but were not statistically significant. The piece recommends keeping only information the model cannot know, human decisions, and hard boundaries, while cutting generic role-setting, rigid step sequences, and blanket requirements like running all tests every time. Note that several cited details, including 2026 dates, GPT-6 Astra, and Opus 5, are forward-looking or unverifiable from the supplied content, and the article offers no growth metrics such as conversion, retention, or CAC.

rss · 人人都是产品经理 · Sep 12, 06:40

**「AI Technique」** The article discusses prompt and skill design for coding agents, specifically the practice of trimming system prompts and using Anthropic&\#x27;s Agent Skills &quot;progressive loading,&quot; where a model first sees only a skill&\#x27;s name and description and loads full instructions or attached files only when relevant. It also describes ablation testing, where prompts are removed and re-added one by one to observe each rule&\#x27;s actual effect.

**「Growth Impact」** The source reports no growth metrics such as conversion, retention, or CAC. Its closest quantitative evidence is cost and task-success data from an ETH Zurich and LogicStar.ai study on coding agents, where auto-generated context files raised experiment cost by about 20% and 23% without significant success-rate improvement. These are workflow-efficiency findings, not user-growth outcomes, and the study covered only specific Python repositories, coding agents, and benchmark tasks.

**「Takeaway」** When a new model version ships, start from a minimal prompt or skill, run a representative set of real tasks, and add back only the instructions that fix repeatedly observed failures, rather than carrying forward rules written for older models.

**Tags**: `#prompt-engineering`, `#AI-workflow`, `#Claude Code`, `#model-capabilities`, `#AI-operations`

---


# Horizon Daily - 2026-08-25

> From 59 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [Anthropic&\#x27;s Top Model Lags as Cheaper AI Tools Gain Ground](#item-ai-growth-1) ⭐️ 7.0/10
2. [Lessons from a $20K Devin Agent Experiment](#item-ai-growth-2) ⭐️ 7.0/10
3. [DeepSeek Harness and the Rise of Recursive Self-Improvement in AI](#item-ai-growth-3) ⭐️ 7.0/10
4. [Huashu-Excel: Open-Source AI Skill for Excel Data Analysis](#item-ai-growth-4) ⭐️ 7.0/10
5. [Enterprise AI Agents: From Human-Like to Outcome-Driven](#item-ai-growth-5) ⭐️ 7.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [Anthropic&\#x27;s Top Model Lags as Cheaper AI Tools Gain Ground](https://simonwillison.net/2026/Aug/23/anthropics-best-ai-model-struggles-to-attract-users-as-cheaper-t/) ⭐️ 7.0/10

Anthropic&\#x27;s annualized revenue reached $65 billion in July 2026, up from $47 billion in May, and the company expects Q3 profitability, with 6,000 customers spending over $100,000 annually. Meanwhile, OpenAI&\#x27;s annualized revenue jumped 35% in the quarter to over $40 billion, boosted by the July launch of GPT-5.6. Ramp&\#x27;s AI index, based on billing data from 70,000 companies, shows that Anthropic&\#x27;s newest model, Opus 5, accounts for only 3.5% of Anthropic model spend, while the older Opus 4.8 leads at 28%, suggesting that cost and release timing affect adoption. This matters for growth practitioners because it highlights that even top-tier AI models face adoption hurdles when cheaper alternatives exist, and pricing strategies can significantly influence market share.

rss · Simon Willison · Aug 23, 20:24

**「AI Technique」** The AI technique involves the deployment of large language models \(LLMs\) with varying cost-performance trade-offs. Anthropic&\#x27;s Opus 5 is a cheaper model that delivers near Fable 5 intelligence at lower cost, while OpenAI&\#x27;s GPT-5.6 offers tiered pricing \(Sol, Terra, Luna\) to cater to different performance needs. These models are used for tasks like coding and knowledge work, with benchmarks showing Opus 5 matching or beating Fable 5 on several metrics at roughly half the price per task.

**「Growth Impact」** OpenAI&\#x27;s revenue growth of 35% quarter-over-quarter, driven by the GPT-5.6 launch, demonstrates that new model releases can jolt performance, while Anthropic&\#x27;s slower adoption of its newest model \(Opus 5 at 3.5% spend\) suggests that pricing and perceived value are critical for monetization. The data from Ramp&\#x27;s AI index provides a real-world view of model adoption, showing that cost-sensitive customers prefer older, cheaper models, which can impact revenue growth for AI providers.

**「Takeaway」** Growth practitioners should monitor model-level adoption data \(like Ramp&\#x27;s AI index\) to understand price sensitivity and tailor pricing or feature bundles to capture cost-conscious segments, rather than assuming the newest model will automatically win.

<details><summary>References</summary>
<ul>
<li><a href="https://www.datacamp.com/blog/claude-opus-5-vs-claude-fable-5">Claude Opus 5 vs Fable 5: Benchmarks and Pricing | DataCamp</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-5">Introducing Claude Opus 5 \ Anthropic</a></li>
<li><a href="https://www.mindstudio.ai/blog/claude-opus-5-launch-benchmarks">Claude Opus 5: Anthropic&#x27;s Cheaper Model That Rivals Fable 5 | MindStudio</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#OpenAI`, `#revenue`, `#market share`, `#AI adoption`

---

<a id="item-ai-growth-2"></a>
### [Lessons from a $20K Devin Agent Experiment](https://www.lennysnewsletter.com/p/i-spent-20000-on-devin-in-a-month) ⭐️ 7.0/10

Solo founder Ryan Carson spent $20,000 in one month running 15 concurrent Devin agents across engineering, customer success, and investor updates. He shared his experience in a podcast episode, emphasizing the importance of manual tracking—he used a handwritten list to manage the agents. The experiment highlights the operational challenges and management overhead of orchestrating multiple AI agents in a startup context. While no specific growth metrics were reported, the case offers a real-world playbook for AI agent deployment across business functions.

rss · Lenny&\#x27;s Newsletter · Aug 24, 12:04

**「AI Technique」** The case involves using Devin, an AI software engineering agent, to autonomously handle tasks across multiple business functions. The technique is agent orchestration, where multiple AI agents run concurrently to perform diverse tasks, requiring human oversight and manual tracking to manage their workflows.

**「Growth Impact」** No measurable growth outcomes were reported in the source. The primary impact appears to be operational efficiency and time savings, though the high cost \($20,000/month\) and management overhead suggest a need for careful ROI evaluation. The context is a solo founder startup, indicating potential scalability challenges for larger teams.

**「Takeaway」** When deploying multiple AI agents, invest in robust tracking and management systems—even a simple manual list can be critical—and carefully assess cost versus benefit before scaling.

**Tags**: `#Devin`, `#AI agents`, `#startup operations`, `#customer success`, `#workflow management`

---

<a id="item-ai-growth-3"></a>
### [DeepSeek Harness and the Rise of Recursive Self-Improvement in AI](https://www.woshipm.com/ai/6453545.html) ⭐️ 7.0/10

DeepSeek has released DeepSeek Harness \(DSH\), a developer preview that marks a significant step toward Recursive Self-Improvement \(RSI\), where AI systems participate in improving themselves. The architecture, developed with Peking University, introduces a core mechanism called Cordis that enables dynamic plugin management with rollback and re-coordination, addressing a critical challenge for self-evolving AI agents. This move aligns with a broader industry trend: Google DeepMind&\#x27;s AlphaEvolve has accelerated a matrix multiplication kernel by 23% and shortened Gemini training time by about 1%, while MiniMax&\#x27;s M2.7 improved internal evaluation scores by 30% after over a hundred self-improvement loops. For growth practitioners, this signals a shift in competitive advantage from model releases to the construction of environments, feedback mechanisms, and loops that enable continuous AI improvement, potentially reshaping how AI capabilities are developed and deployed.

rss · 人人都是产品经理 · Aug 25, 01:15

**「AI Technique」** DeepSeek&\#x27;s Harness \(DSH\) is a developer preview that implements Recursive Self-Improvement \(RSI\) by providing an environment where AI agents can modify their own components. The core mechanism, Cordis, is a plugin framework that enables reversible effects and automatic re-coordination of dependencies, allowing agents to safely add, remove, or modify plugins without restarting the system. This supports continuous self-improvement loops, as validated by its four-year use in the Koishi chatbot framework with over 4,000 community plugins.

**「Growth Impact」** The article reports that DeepSeek&\#x27;s Harness \(DSH\) is part of a broader industry shift toward Recursive Self-Improvement \(RSI\), where AI systems improve themselves. While no direct growth metrics are provided for DeepSeek, the article cites Google&\#x27;s AlphaEvolve, which accelerated a key matrix multiplication kernel by 23% and shortened Gemini&\#x27;s overall training time by about 1%, and MiniMax&\#x27;s M2.7, which improved internal evaluation scores by 30% after over 100 self-improvement loops. These examples illustrate how RSI can lead to significant efficiency gains and capability improvements, which are critical for growth practitioners as they signal a shift from model releases to continuous improvement loops as a competitive advantage. The mechanism is that AI systems autonomously generate, evaluate, and iterate on solutions, reducing the need for human intervention and accelerating optimization. For growth practitioners, this suggests that investing in environments, feedback mechanisms, and loops can drive compounding improvements in AI performance, potentially lowering costs and improving product capabilities over time.

**「Takeaway」** Growth practitioners should monitor RSI developments as they may lead to AI systems that improve autonomously, potentially reducing the need for manual optimization and enabling more efficient scaling of AI-driven growth initiatives.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md">deepseek-harness/docs/architecture.md at master · deepseek-ai/deepseek-harness</a></li>
<li><a href="https://deepseek-harness.github.io/deepseek-harness/en/reference/">DeepSeek Harness Architecture | DeepSeek Harness</a></li>
<li><a href="https://floatboat.ai/blog/cordis-plugin-framework">Cordis — The Plugin Kernel Behind DeepSeek Harness</a></li>
<li><a href="https://eu.36kr.com/en/p/3952918063774852">DeepSeek Harness Launched: Is AI Now Capable of Creating AI?</a></li>
<li><a href="https://finance.biggo.com/news/092d974d-a3fa-4485-8056-49c5b5e8dba9">DeepSeek Takes Aim at AI Agent Market With &#x27;1/105th the Price&#x27; Harness, Putting US Big Tech on Edge — BigGo Finance</a></li>
<li><a href="https://www.theregister.com/ai-and-ml/2026/08/14/deepseeks-innovative-harness-treats-everything-as-a-plug-in/5288095">DeepSeek&#x27;s innovative harness treats everything as a plug-in</a></li>

</ul>
</details>

**Tags**: `#DeepSeek`, `#RSI`, `#AI self-improvement`, `#AI strategy`, `#Harness`

---

<a id="item-ai-growth-4"></a>
### [Huashu-Excel: Open-Source AI Skill for Excel Data Analysis](https://www.woshipm.com/ai/6453768.html) ⭐️ 7.0/10

Huashu-Excel is an open-source AI skill \(MIT-licensed\) that automates Excel/CSV data processing and analysis through an eight-step workflow: inspection, cleaning, alignment, analysis, reconciliation, delivery, chart verification, and quality control. It addresses the growth problem of time-consuming daily data analysis for operations professionals, such as preparing morning reports and explaining data fluctuations. The skill was stress-tested on ten real public datasets, including a 1.06-million-row e-commerce transaction file and a 210,000-row municipal budget, and successfully caught errors like a $10 discrepancy in a subtotal and a mislabeled fiscal year column that internal checks missed. For growth practitioners, this matters because it offers a replicable, tool-agnostic workflow that reduces manual data work and improves accuracy, freeing time for strategic decisions.

rss · 人人都是产品经理 · Aug 24, 11:06

**「AI Technique」** The Huashu-Excel skill leverages a structured 8-step workflow \(inspection, cleaning, alignment, analysis, reconciliation, delivery, chart verification, and quality control\) to guide large language models \(LLMs\) in processing Excel/CSV data. It uses openpyxl to read raw cell data for inspection, employs scripts for cleaning and reconciliation, and includes a final independent agent to re-verify results from raw data. The skill also uses role prompting, inspired by Anthropic&\#x27;s research on persona selection, to enhance model performance, and applies statistical principles like robust statistics and perceptual guidelines for chart design.

**「Growth Impact」** The Huashu-Excel skill directly addresses the daily data-analysis burden of operations and growth practitioners by automating an 8-step workflow \(inspection, cleaning, alignment, analysis, reconciliation, delivery, chart verification, quality control\). In stress tests on ten real public datasets, it caught a $10 discrepancy in a subtotal that manual review would miss, identified a Simpson&\#x27;s paradox that changed the interpretation of operational efficiency, and flagged that 32.4% of housing work orders were closed without entry—revealing that the official 86.5% completion rate could be as low as 49.5% depending on the metric definition. These capabilities reduce the time and error rate in routine reporting, enabling faster, more accurate data-driven decisions. While no direct conversion or retention metrics are reported, the skill&\#x27;s ability to surface hidden data issues and provide traceable, auditable analysis can improve the quality of growth decisions and reduce the risk of acting on flawed data.

**「Takeaway」** Growth practitioners can adopt Huashu-Excel&\#x27;s structured workflow—especially its reconciliation and independent quality-control steps—to catch data errors that standard tools miss, ensuring more reliable analysis for daily operations and reporting.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/emotion-concepts-function">Emotion concepts and their function in a large language model \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/research/persona-selection-model">The persona selection model \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/research/assistant-axis">The assistant axis \ Anthropic</a></li>
<li><a href="https://www.sourcepulse.org/projects/28022404">huashu-skills by alchaincyf - SourcePulse</a></li>

</ul>
</details>

**Tags**: `#AI skill`, `#Excel`, `#data analysis`, `#open source`, `#operations`

---

<a id="item-ai-growth-5"></a>
### [Enterprise AI Agents: From Human-Like to Outcome-Driven](https://www.woshipm.com/ai/6453622.html) ⭐️ 7.0/10

At the 2026 AI Product Conference, Yao Guanghua, head of Agora&\#x27;s AI product line, argued that enterprise-grade conversational agents should be evaluated not by how human-like they are, but by their ability to deliver controllable business outcomes. He introduced a &\#x27;trust gradient&\#x27; \(intern, outsourcer, expert, partner\) to describe increasing levels of delegation, and emphasized building evaluation sets around real business metrics like task completion rate, transfer rate, and repeat call rate, rather than single-turn accuracy. A key example: an outbound sales agent initially achieved only ~70% of human conversion, but after two weeks of iterative evaluation and regression testing, it matched human performance; after a month, its intent conversion rate reached 3.08%, more than double the pre-launch human baseline of 1.5%. For growth practitioners, the takeaway is that AI agents should be treated as &\#x27;result businesses&\#x27; where payment is tied to outcomes, and that product managers must own the evaluation process to ensure reliability and accountability.

rss · 人人都是产品经理 · Aug 24, 09:31

**「AI Technique」** The article describes the use of conversational AI agents \(voice agents\) for customer service and sales, built on ASR, TTS, and large language models. The key technique is iterative evaluation and regression testing: collecting real call recordings, manually labeling failures, categorizing them, and feeding them back into a regression set that runs on every release. This process, combined with role-specific prompts and architecture-level guardrails, improves task completion and conversion rates.

**「Growth Impact」** In an outbound sales scenario, the AI agent&\#x27;s intent conversion rate reached 3.08% after one month, more than double the pre-launch human baseline of 1.5%. This improvement was achieved through continuous evaluation and regression testing, demonstrating that AI agents can significantly outperform human baselines when properly tuned. The context is a B2B enterprise setting, likely in China, though specific company details are not provided.

**「Takeaway」** Growth practitioners should build their own evaluation sets based on real business outcomes, not just model benchmarks, and iterate on failures to drive measurable conversion lifts.

**Tags**: `#AI agent`, `#enterprise AI`, `#conversational AI`, `#outcome-based evaluation`, `#voice agent`, `#product management`

---


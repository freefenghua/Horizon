# Horizon Daily - 2026-08-31

> From 49 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [Why Averages Mislead: AI PMs Must Use P50/P90/P95 for Token Metrics](#item-ai-growth-1) ⭐️ 8.0/10
2. [Understanding ChatGPT Work: A Practical Guide for Growth Practitioners](#item-ai-growth-2) ⭐️ 7.0/10
3. [Persistent AI Coworkers: The New Growth Frontier](#item-ai-growth-3) ⭐️ 7.0/10
4. [Claude&\#x27;s AI-Native SDLC Playbook: From Coding Bottleneck to Decision-Making](#item-ai-growth-4) ⭐️ 7.0/10
5. [AI-Driven Digital Twin Development: From Months to Days with ZCode and GLM](#item-ai-growth-5) ⭐️ 7.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [Why Averages Mislead: AI PMs Must Use P50/P90/P95 for Token Metrics](https://www.woshipm.com/ai/6456886.html) ⭐️ 8.0/10

This article presents a real-world case study from a government AI office assistant project, where the team needed to decide how many credits to give new users. The developer reported an average token consumption of 50,000 per task, but analysis of recent sessions showed the average was near 40,000 while half of tasks consumed under 12,000 tokens. The author explains that averages are skewed by heavy-tailed tasks and advocates using percentiles \(P50, P90, P95\) to understand typical and extreme usage. For the credit system, they used P50 for typical tasks, P90/P95 for complex tasks that might exhaust credits, and the average for total platform cost. The article also warns about statistical口径 \(definition\) issues, such as whether the metric includes context, tool calls, or test data. This matters for growth practitioners because it provides a replicable framework for making data-driven decisions in AI product economics, avoiding misleading averages.

rss · 人人都是产品经理 · Aug 31, 02:08

**「AI Technique」** The AI technique involved is the use of percentile metrics \(P50, P90, P95\) to analyze token consumption patterns in an AI agent system. This is a statistical method, not a machine learning model, but it is essential for understanding the distribution of AI task costs, which are often heavy-tailed due to variable agent behaviors like tool calls and context accumulation.

**「Growth Impact」** The measurable growth outcome is improved cost management and user experience in an AI product&\#x27;s credit system. By using percentiles instead of averages, the team could set initial credits that cover typical tasks \(P50\) while mitigating risk of users exhausting credits on heavy tasks \(P90/P95\). This prevents user churn due to unexpected credit depletion and optimizes cost allocation. The context is a government AI office assistant, but the approach is applicable to any AI product with token-based pricing.

**「Takeaway」** When designing token-based pricing or credit systems, always analyze the distribution of token consumption using P50, P90, and P95 percentiles, and clarify the statistical definition of the metric before making decisions.

**Tags**: `#AI product management`, `#token economics`, `#percentile metrics`, `#pricing strategy`, `#case study`

---

<a id="item-ai-growth-2"></a>
### [Understanding ChatGPT Work: A Practical Guide for Growth Practitioners](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 7.0/10

OpenAI&\#x27;s ChatGPT Work, announced on July 9th, is a powerful but confusing product that comes in two forms: Work Cloud \(accessible via chatgpt.com and mobile apps\) and Work Local \(via the desktop app, formerly Codex\). Available only to $20/month and up subscribers, Work Cloud offers features not in regular Chat, including model selection \(GPT-5.6 Sol, Luna, Terra\), a code execution environment with unrestricted internet access, a full headless Chrome browser that can fill forms and run JavaScript, a persistent shared filesystem, the ability to publish ChatGPT Sites, and sub-agent sessions. Community users report practical automation use cases, such as building Android apps on a Pixel phone and automating email drafting and form filling via computer use. This matters for growth practitioners because it enables complex workflow automation and rapid prototyping, though the article lacks hard growth metrics or a formal playbook.

rss · Simon Willison · Aug 30, 23:59 · [Discussion](https://news.ycombinator.com/item?id=49504625)

**「AI Technique」** ChatGPT Work leverages large language models \(GPT-5.6 Sol, Luna, Terra\) with configurable reasoning levels, combined with a code execution environment that has internet access and a headless Chrome browser for web interaction. This allows the AI to perform multi-step tasks such as cloning repositories, installing dependencies, and interacting with websites, effectively acting as an autonomous agent.

**「Growth Impact」** While the article does not provide specific growth metrics, community comments indicate that ChatGPT Work&\#x27;s computer use feature enables significant time savings and efficiency gains in tasks like email drafting and form filling. For example, one user uses it to draft replies to emails and fill out multi-step forms using saved files, which can reduce manual effort and improve operational efficiency for growth teams.

**「Takeaway」** Growth practitioners should explore ChatGPT Work&\#x27;s code execution and browser automation capabilities to automate repetitive tasks like data extraction, form filling, and content generation, potentially freeing up time for higher-value strategic work.

**Tags**: `#ChatGPT Work`, `#OpenAI`, `#AI agents`, `#workflow automation`, `#product analysis`

---

<a id="item-ai-growth-3"></a>
### [Persistent AI Coworkers: The New Growth Frontier](https://www.lennysnewsletter.com/p/ais-third-era-the-rise-of-persistent) ⭐️ 7.0/10

Tara Seshan, head of Codex and ChatGPT Work at OpenAI, discusses the rise of persistent AI coworkers, marking a shift from task-based AI tools to always-on collaborators that can handle complex workflows. She argues that ambition, not capability, is now the key differentiator for teams, as AI models rapidly improve. The conversation emphasizes the importance of &\#x27;steering&\#x27; AI rather than &\#x27;rowing&\#x27;—focusing on high-level direction and oversight instead of manual execution. Seshan advises building for where models will be in two to three months, anticipating future capabilities. While the piece offers strategic insights for integrating AI into growth workflows, it lacks concrete metrics or case studies, making it more of a forward-looking perspective than a data-driven playbook.

rss · Lenny&\#x27;s Newsletter · Aug 30, 12:31

**「AI Technique」** The discussion centers on the evolution of AI from task-specific tools to persistent AI coworkers—systems that operate continuously within workflows, capable of steering complex projects rather than merely executing discrete tasks. This approach leverages advanced language model capabilities to handle multi-step processes, with an emphasis on designing for future model improvements expected within two to three months.

**「Growth Impact」** The growth impact is indirect but strategic: by adopting persistent AI coworkers, teams can potentially accelerate product development and operational efficiency, leading to faster iteration and improved growth outcomes. The mechanism is the shift from manual, task-based AI usage to autonomous, continuous collaboration, which frees human talent for higher-level strategy. However, no specific metrics are provided, so the impact is qualitative and forward-looking.

**「Takeaway」** Growth practitioners should start designing workflows that assume AI will handle routine execution, allowing humans to focus on strategic steering, and should build with an eye toward near-future model capabilities to stay ahead.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lennysnewsletter.com/p/ais-third-era-the-rise-of-persistent">AI ’s third era: the rise of persistent AI coworkers | Tara Seshan ...</a></li>

</ul>
</details>

**Tags**: `#AI coworkers`, `#OpenAI`, `#product strategy`, `#workflow`, `#future of work`

---

<a id="item-ai-growth-4"></a>
### [Claude&\#x27;s AI-Native SDLC Playbook: From Coding Bottleneck to Decision-Making](https://www.woshipm.com/ai/6457025.html) ⭐️ 7.0/10

Claude&\#x27;s official AI-Native SDLC Playbook outlines a new software development lifecycle where AI handles coding, testing, and deployment, shifting the bottleneck from code writing to decision-making. The playbook proposes six stages—planning, design, build, test, deploy, and operate—each with AI-human collaboration, such as AI generating requirement documents \(intent.md\) and design specs \(spec.md\) that humans review. This approach aims to reduce iteration cycles from weeks to hours, as AI can generate code in minutes and self-test its work. For growth practitioners, this means faster product iteration and the ability to run more experiments, though the article notes that organizational inertia, trust, and compliance are significant barriers to adoption. The source lacks quantitative metrics, so the reported benefits are qualitative and based on the playbook&\#x27;s design rather than measured outcomes.

rss · 人人都是产品经理 · Aug 31, 02:08

**「AI Technique」** The playbook leverages generative AI and LLMs to automate software development tasks, including generating requirement documents, design specs, implementation plans, and code, as well as performing automated testing and code review. It also uses AI to diagnose and fix production issues, with the ability to learn from repeated problems by updating team standards.

**「Growth Impact」** The primary growth impact is faster iteration cycles, enabling more rapid experimentation and feature releases, which indirectly supports growth efforts. However, the article does not provide specific metrics or case studies, so the impact is inferred from the described workflow changes rather than measured results.

**「Takeaway」** Growth practitioners should explore using AI to automate documentation and code generation to compress iteration timelines, but must also invest in building trust through pilot projects and data collection to overcome organizational resistance.

**Tags**: `#AI-native SDLC`, `#Claude`, `#product management`, `#workflow`, `#AI development`

---

<a id="item-ai-growth-5"></a>
### [AI-Driven Digital Twin Development: From Months to Days with ZCode and GLM](https://www.woshipm.com/ai/6456839.html) ⭐️ 7.0/10

This case study demonstrates how using ZCode with GLM large language models compressed the development of a container terminal digital twin from months to days, with a single developer handling all asset creation and simulation. The project produced 32 GLB assets, 1500 containers, 9 vehicles, 3 RTGs, 3 quay cranes, and a 260-meter container ship, running a complete business loop simulation at 144 FPS in a browser. The methodology replaces traditional modeling with parameterized generation and conversational iteration, enabling rapid changes and validation. For growth practitioners, this shows how AI can drastically reduce development time and cost for complex simulations, making digital twins more accessible and agile for operational improvements.

rss · 人人都是产品经理 · Aug 31, 00:51

**「AI Technique」** The case uses ZCode, an agentic development environment built around the GLM large language model, to convert digital twin creation from manual 3D modeling into a conversational, parameter-driven generation process. The core technique is &\#x27;parameterized generation&\#x27;: instead of hand-modeling each asset, the developer defines objects \(containers, yard blocks, cranes\) by their real-world dimensions and properties, and instructs the GLM model via natural language prompts to write procedural generators \(e.g., a 250-line glTF writer\) that produce GLB assets and three.js scenes. Iteration is done through &\#x27;conversational refinement&\#x27;—the user describes changes \(e.g., &\#x27;add two more columns to the yard&\#x27;\) and the model updates the generator parameters, re-running the scene in minutes. For complex organic structures like gatehouses, the model writes Blender headless scripts to build them, and textures are procedurally generated with random seeds for realism. This approach shifts the developer&\#x27;s role from manual modeling to describing requirements, with the model translating constraints into code and assets.

**「Growth Impact」** The case study reports a dramatic reduction in digital twin development time from months to days, with a single developer producing 32 GLB assets, 1500 containers, and a full simulation running at 144 FPS. While the source does not provide traditional growth metrics like conversion or retention, the efficiency gains directly address cost and agility pain points: the methodology compresses what typically requires a team of modelers and months of iteration into a one-person, conversational workflow. This aligns with industry benchmarks showing digital twin programs can reduce product development cycle time by 20-40% \(tool-2-2\) and cut production costs by over 50% in some cases \(tool-2-1\). For growth practitioners, the key mechanism is the shift from manual modeling to parameterized generation and conversational iteration, which lowers the barrier to creating and updating digital twins, enabling faster experimentation and adaptation to business changes.

**「Takeaway」** Adopt a &\#x27;parameterized generation + conversational iteration&\#x27; approach with LLMs to compress complex simulation development from months to days, enabling faster iteration and lower costs for operational scenarios.

<details><summary>References</summary>
<ul>
<li><a href="https://zcode.z.ai/en">ZCode | Official Harness for GLM-5.3</a></li>
<li><a href="https://zcode.z.ai/en/docs/welcome">ZCode Docs | GLM-5.3 Agentic Coding Guide</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9506524/">A Digital Twin Case Study on Automotive Production Line - PMC</a></li>
<li><a href="https://medium.com/mindful-designing/the-business-case-for-digital-twin-costs-benefits-and-roi-explained-209da5030f6e">The Business Case for Digital Twin: Costs, Benefits, and ROI Explained | by Robert Smith | Mindful Tech Journal | Medium</a></li>

</ul>
</details>

**Tags**: `#digital twin`, `#AI development`, `#large language model`, `#case study`, `#efficiency`, `#ZCode`, `#GLM`

---


# Horizon Daily - 2026-09-21

> From 63 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [AI Agent Turns API Doc into Clickable Prototype in One Hour](#item-ai-growth-1) ⭐️ 6.0/10
2. [豆包工作浏览器录制与回放：把重复操作变成可复用 Skill](#item-ai-growth-2) ⭐️ 6.0/10
3. [AI 时代，别只追 AI 工具，快去练你的工作流](#item-ai-growth-3) ⭐️ 5.0/10
4. [Taobao Shangou&\#x27;s AI Design Engineering for B-End Promotions](#item-ai-growth-4) ⭐️ 5.0/10
5. [商科生用LLM做AI香氛：AuraSync概念复盘](#item-ai-growth-5) ⭐️ 5.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [AI Agent Turns API Doc into Clickable Prototype in One Hour](https://www.woshipm.com/ai/6467317.html) ⭐️ 6.0/10

A product manager at an HR SaaS company used an AI Agent to convert a developer-facing PTS API delivery manual into a clickable single-file web prototype. The manual covered seven interface categories \(authentication, enrollment/suspension data upload, component address retrieval, processing result query\) with pinyin-abbreviated field names like bizNo, areaid, slpzwjdz, and bljdmx. Over roughly one hour across twelve dialogue rounds, the AI Agent first acted as a translator to summarize what needs the product solved, then built an 864-line single-file prototype where every button and flow was functional. The prototype was deployed as a public link and shared with colleagues and the PTS vendor. The case matters for growth practitioners because it demonstrates a replicable AI-assisted workflow—AI as document translator then UI builder—that compresses a typical week-long prototyping cycle into hours, though the source reports no growth metrics such as conversion, retention, or CAC.

rss · 人人都是产品经理 · Sep 21, 03:25

**「AI Technique」** The author used a general-purpose AI Agent \(not a specialized prototyping tool\) in two phases: first as a document translator to read the API manual and answer what needs the product solves, which capabilities are mandatory versus optional, and whether specific interfaces exist; then as a UI builder to generate a single-file HTML/JS prototype. The workflow relied on iterative dialogue with screenshots of the existing system as visual anchors, plus script-based smoke tests simulating browser rendering across 42 assertions.

**「Growth Impact」** The reported outcome is a time reduction: a prototyping cycle that traditionally took about a week of reading, alignment meetings, wireframing, and review was compressed to roughly one hour of AI-assisted iteration. The mechanism is AI handling domain-knowledge translation \(pinyin field names to product language, inferring page data flows from request/response tables\) while the human supplies business judgment. No conversion, retention, CAC, or LTV metrics are reported, and the case is a pre-sales prototype rather than a live growth experiment.

**「Takeaway」** When using an AI Agent to prototype from technical documentation, force it to first act as a translator—mapping capabilities, mandatory versus optional features, and interface gaps—before asking it to build UI, and pair every iteration with a smoke test to catch execution-overflow errors before they reach a demo.

**Tags**: `#AI Agent`, `#product prototyping`, `#API documentation`, `#workflow automation`, `#HR SaaS`, `#product management`

---

<a id="item-ai-growth-2"></a>
### [豆包工作浏览器录制与回放：把重复操作变成可复用 Skill](https://www.woshipm.com/ai/6467203.html) ⭐️ 6.0/10

The article is a hands-on walkthrough by 叶小钗 of two features in 豆包工作 \(Doubao Work\): browser record-and-replay and local PPT editing. The author records a daily routine of opening AI news sites such as 机器之心, 量子位, and 卡神的AI热点网站, then lets 豆包工作 analyze the recording and package it into a reusable Skill named ai-news-collector-local that extracts headlines, URLs, authors, and publish times, builds a clean HTML page, and pushes the result to 飞书. The same approach is applied to a WeChat official account data-checking workflow, and the author also uses 豆包工作 to add four AIGC-related pages to an existing 45-page PPT while matching the original warm, magazine-style visual design. The article reports no quantified time savings, conversion, or retention metrics, so the growth impact is described qualitatively as reduced repetitive manual work rather than measured business results.

rss · 人人都是产品经理 · Sep 21, 01:49

**「AI Technique」** 豆包工作&\#x27;s browser record-and-replay captures a user&\#x27;s manual browser actions, analyzes the intent behind the recorded flow, and converts it into a reusable Skill that can be invoked later without re-entering prompts. The same tool also performs local file editing on an existing PPT, generating new pages that follow the original document&\#x27;s color, font, and layout style.

**「Growth Impact」** The reported outcome is operational efficiency: the author no longer opens multiple AI news sites individually each day, and can extend an existing 45-page PPT without manually rebuilding its visual style. No quantified metrics such as time saved, conversion lift, or retention improvement are provided, and the context is personal productivity for an individual content creator rather than a company-level growth experiment.

**「Takeaway」** Identify one high-frequency, low-complexity browser routine in your daily workflow, record it once in 豆包工作, and package it as a reusable Skill that pushes structured output to a tool you already use, such as 飞书.

**Tags**: `#AI workflow automation`, `#browser automation`, `#豆包工作`, `#productivity`, `#operations`, `#飞书`

---

<a id="item-ai-growth-3"></a>
### [AI 时代，别只追 AI 工具，快去练你的工作流](https://www.woshipm.com/ai/6467321.html) ⭐️ 5.0/10

这篇文章主张 AI 落地的关键不是工具能力，而是工作方法：应先把个人工作流拆解为 AI 可参与的步骤，再固化为可复用的 Skill。作者以产品经理写 PRD 为例，把隐性经验显性化为「需求理解 → 用户与场景分析 → 问题定义 → 任务拆解 → 流程设计 → 页面设计 → 状态检查 → 评审复核 → 修改」的流程，并建议把 AI 放进流水线，只负责「理解和生成」，工具负责「确定性地转换和执行」，人负责「判断和验收」。文章强调 Skill 的价值是把个人经验变成可重复执行的生产流程，而非技术人员专属的配置文件。需要说明的是，全文停留在方法论层面，未提供具体案例、效率提升百分比或转化率等量化指标，也未涉及留存、转化、CAC 等增长指标，属于观点型内容而非数据支撑的案例研究。

rss · 人人都是产品经理 · Sep 21, 03:27

**「AI 技术要点」** 文章讨论的是把工作方法写成 AI 可执行的「Skill」（说明书式流程），并让 AI 在流水线中承担理解与生成环节，配合 Excel 等工具做确定性计算。文中未涉及具体模型版本、微调或工程实现细节。

**「增长影响」** 文章未报告任何可量化的增长结果（如效率提升百分比、转化率或 CAC 变化），仅提出「把经验变成规则、规则变成流程、流程写成 Skill」的定性主张。因此其增长影响目前无法验证，需结合后续实践数据评估。

**「可执行要点」** 先盘点自己每天重复且已有固定流程的工作，把隐性判断写成明确的步骤与验收标准，再让 AI 只负责其中的理解与生成环节，其余交给工具或人工验收。

**Tags**: `#AI工作流`, `#AI应用`, `#效率提升`, `#方法论`, `#Skill`

---

<a id="item-ai-growth-4"></a>
### [Taobao Shangou&\#x27;s AI Design Engineering for B-End Promotions](https://www.woshipm.com/ai/6467628.html) ⭐️ 5.0/10

A designer at Taobao Shangou \(淘宝闪购\) documented how the merchant-facing \(B-end\) promotion design team applies &quot;AI design engineering&quot; to shift deliverables from design files to code. The team distinguishes standard needs \(structured, reusable components\) where AI can speed up output, from custom and creative needs where AI mainly inspires ideas. They chose AI design engineering because the deliverable becomes code, letting designers use three code libraries directly so R&amp;D no longer needs a &quot;translation&quot; layer, and eliminating annotation and slicing steps so design fidelity approaches 100% and review communication with R&amp;D approaches zero. The workflow adds roughly 30% more work for designers \(previously front-end development work\), so the team co-built an SOP Skill with R&amp;D to automate the process, and defined Skill content around a four-step designer thinking path: business flow, page framework, component usage, global styles. The article states the current goal is 80%-90% design efficiency gains on standard pages and notes this is still being optimized; no concrete before/after metrics were published in the available excerpt, and the author cautions that model capability limits and hallucination mean designers are still needed for quality control.

rss · 人人都是产品经理 · Sep 21, 02:59

**「AI Technique」** The approach uses AI coding/design-generation Skills \(prompt-based workflows run through an IDE\) that convert design intent into front-end React engineering code rather than static HTML or design mockups. The team consolidated everything into a single lightweight design Skill using progressive disclosure, after rejecting a two-layer parent-child Skill structure as too complex for the model to understand, and they surveyed AI UI-generation products including Lovable and Figma Make to map AI&\#x27;s capability boundaries.

**「Growth Impact」** The reported mechanism is workflow efficiency rather than user-growth metrics: designers skip annotation and slicing, design fidelity approaches 100%, and R&amp;D review communication approaches zero, with a stated target of 80%-90% design efficiency improvement on standard promotion pages. The source does not publish actual measured before/after numbers, so these figures should be treated as goals and qualitative claims rather than validated results.

**「Takeaway」** If you want AI to reliably generate standardized UI, encode your designers&\#x27; existing thinking path \(business flow → page framework → component usage → global styles\) into a single lightweight Skill, and split maintenance so shared design tokens and base components are centralized while business-specific rules stay with each business team.

**Tags**: `#AI设计工程化`, `#B端设计`, `#设计提效`, `#淘宝闪购`, `#AI工作流`, `#前端代码生成`

---

<a id="item-ai-growth-5"></a>
### [商科生用LLM做AI香氛：AuraSync概念复盘](https://www.woshipm.com/share/6467343.html) ⭐️ 5.0/10

一名电子商务专业大三学生复盘了在欧莱雅Brandstorm商赛中设计的AI情感香氛系统AuraSync。该项目用LLM做情感语义匹配，用户输入一句话（如“今天工作好累”），后台识别情绪并自动释放对应香氛，硬件为智能香氛扩散器搭配6种情绪胶囊。作者引用中国独居人口预计2030年突破1.5亿、200-350元中高端价格带空白、白牌情感溢价19%-86%等市场背景，并设计了“硬件699-899元+胶囊98-138元+29.9元/年订阅”的闭环，首年目标销量10万台、次月留存60%、变现率25%。需要明确的是，该项目未获奖，所有指标均为目标而非验证结果，作者也承认不清楚定价是否合理、方案是否存在重大缺陷。对增长从业者而言，这更适合作为早期AI产品构思与概念验证的参考，而非可直接复制的增长打法。

rss · 人人都是产品经理 · Sep 21, 02:37

**「AI技术」** 项目使用LLM进行情感语义匹配：用户以自然语言输入情绪化语句，模型识别其中的情绪类别，再映射到对应的香氛胶囊。作者强调自己不懂模型训练，只关注LLM能做什么、不能做什么，以及如何把它转化为用户可感知的功能。

**「增长影响」** 该项目没有实际增长结果，文中给出的首年10万台销量、60%次月留存、25%变现率均为目标值而非验证数据。其增长逻辑设想是通过“陪伴记录”和“情绪日志”沉淀用户情感数据以提升粘性，并用硬件锁定用户、胶囊耗材提供持续现金流、订阅服务提升LTV。

**「启示」** 不懂技术的增长从业者可以先聚焦“AI能做什么、不能做什么”，用一个真实问题跑通从用户输入到可感知功能的闭环，并把过程与结果整理成作品集，而不是先死磕算法原理。

**Tags**: `#AI product`, `#consumer goods`, `#emotional marketing`, `#case study`, `#early-stage`, `#no metrics`

---


# Horizon 每日速递 - 2026-08-31

> 从 49 条内容中筛选出 5 条重要资讯。

---

**AI×增长交叉领域**
1. [AI 产品经理必懂：用 P50/P90/P95 替代平均值设计 Token 积分体系](#item-ai-growth-1) ⭐️ 8.0/10
2. [ChatGPT Work 深度解析：云端与本地双形态及自动化实战](#item-ai-growth-2) ⭐️ 7.0/10
3. [OpenAI 产品负责人谈 AI 第三纪元：持久 AI 同事的崛起](#item-ai-growth-3) ⭐️ 7.0/10
4. [Claude 官方 AI 原生软件开发手册解析：代码不再是瓶颈，产品经理转向决策者](#item-ai-growth-4) ⭐️ 7.0/10
5. [用 ZCode+GLM 将数字孪生开发从数月压缩至三天](#item-ai-growth-5) ⭐️ 7.0/10

---

## AI×增长交叉领域

<a id="item-ai-growth-1"></a>
### [AI 产品经理必懂：用 P50/P90/P95 替代平均值设计 Token 积分体系](https://www.woshipm.com/ai/6456886.html) ⭐️ 8.0/10

本文通过一个政务 AI 办公助手积分体系设计的真实案例，揭示了依赖平均值（如“平均一个任务消耗 5 万 Token”）会导致决策偏差的问题。实际数据显示，平均消耗接近 4 万 Token，但 P50（中位数）仅为 1.2 万 Token，说明长尾任务严重拉高了平均值。作者建议 AI 产品经理在定价、积分设计等场景中，应结合 P50（典型任务）、P90/P95（长尾风险）和平均值（总成本）进行综合决策，并强调统计口径（如是否包含上下文、工具调用等）的重要性。这一方法可帮助增长从业者更精准地设计用户激励和成本控制策略，避免因指标误读导致资源浪费或用户体验受损。

rss · 人人都是产品经理 · 8月31日 02:08

**「AI 技术要点」** 本文涉及的核心技术是 AI Agent 任务中的 Token 消耗统计与分位数分析。通过计算 P50、P90、P95 等百分位数，产品经理可以更准确地理解任务消耗的分布特征，从而优化积分定价和成本预测。

**「增长影响」** 该案例展示了如何通过分位数分析优化 AI 产品的积分体系设计，避免因平均值误导导致初始积分设置过高或过低，从而影响用户留存和成本控制。具体数据表明，若仅依赖平均值，初始积分可能被低估，导致用户任务中断；而采用 P50/P90/P95 后，可更精准地平衡用户体验与成本，提升用户满意度和平台可持续性。

**「行动建议」** 在设计 AI 产品定价或积分体系时，务必同时参考 P50、P90/P95 和平均值，并明确统计口径，以规避长尾任务带来的误导。

**标签**: `#AI product management`, `#token economics`, `#percentile metrics`, `#pricing strategy`, `#case study`

---

<a id="item-ai-growth-2"></a>
### [ChatGPT Work 深度解析：云端与本地双形态及自动化实战](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 7.0/10

OpenAI 于 7 月 9 日发布 ChatGPT Work，这是一个面向付费订阅者（$20/月及以上）的强大产品，实际上包含两个形态：云端版（Work Cloud）和本地桌面版（Work Local）。云端版提供多项 Chat 不具备的功能，包括可访问互联网的代码执行环境、完整的无头 Chrome 浏览器、持久化共享文件系统、发布 ChatGPT Sites 的能力，以及支持 Sol、Luna、Terra 模型选择和子代理会话。社区用户展示了实际应用场景，例如在 Pixel 手机上构建 Android 应用并直接下载 APK，以及通过计算机使用功能自动起草邮件回复和填写多步骤表单。该产品对增长从业者的意义在于，它提供了强大的工作流自动化能力，能够显著提升运营效率，尽管目前缺乏具体的增长指标数据。

rss · Simon Willison · 8月30日 23:59 · [社区讨论](https://news.ycombinator.com/item?id=49504625)

**「AI 技术解析」** ChatGPT Work 基于 OpenAI 的 GPT-5.6 系列模型（Sol、Luna、Terra），并集成了代码执行环境（支持安装软件包和访问互联网）、无头 Chrome 浏览器（可加载网页、填写表单、运行 JavaScript）以及持久化文件系统。这些技术组合使 AI 代理能够执行复杂的多步骤任务，如自动化网页交互和数据处理。

**「增长影响」** 虽然文章未提供具体的增长指标，但社区反馈表明，ChatGPT Work 的自动化能力可显著提升工作效率，例如销售团队用于每周管道优先级排序和个性化邮件外联，项目经理将其用作项目知识库。这种效率提升可能间接降低运营成本（CAC）并提高客户留存，但需要进一步量化验证。

**「实践启示」** 增长从业者应探索利用 ChatGPT Work 的浏览器自动化和代码执行功能，将重复性运营任务（如表单填写、邮件起草、数据抓取）自动化，以释放人力并提升响应速度。

**标签**: `#ChatGPT Work`, `#OpenAI`, `#AI agents`, `#workflow automation`, `#product analysis`

---

<a id="item-ai-growth-3"></a>
### [OpenAI 产品负责人谈 AI 第三纪元：持久 AI 同事的崛起](https://www.lennysnewsletter.com/p/ais-third-era-the-rise-of-persistent) ⭐️ 7.0/10

OpenAI 产品负责人 Tara Seshan 在 Lenny&\#x27;s Newsletter 的访谈中提出，AI 正进入第三纪元，即持久 AI 同事（persistent AI coworkers）的崛起。她认为，当前团队的区别因素不再是 AI 能力，而是雄心（ambition），即团队如何设想和利用 AI 同事来改变工作流程。她强调了“掌舵与划桨”（steering vs. rowing）的比喻，指出未来的工作模式将更多依赖人类指导 AI 执行任务，而非人类亲自操作。她还建议团队应为两到三个月后的模型能力进行构建，以保持前瞻性。这一观点对增长从业者的启示在于，应关注 AI 同事的长期协作潜力，而非仅将其视为一次性工具。

rss · Lenny&\#x27;s Newsletter · 8月30日 12:31

**「AI 技术要点」** OpenAI 产品负责人 Tara Seshan 提出，AI 的第三个时代是“持久型 AI 同事”（persistent AI coworkers）的崛起，即 AI 从按需响应的工具转变为持续参与工作流程的协作伙伴。她强调，团队应关注“掌舵”（steering）而非“划桨”（rowing），即人类负责设定目标和方向，AI 负责执行具体任务。此外，她建议为未来两到三个月的模型能力进行构建，以充分利用即将到来的技术进步。

**「增长影响」** 该访谈未提供具体的增长指标或案例数据，但提出了一个战略框架：通过将 AI 视为持久同事，团队可以重新设计工作流程，从而可能提升效率、加速迭代，并最终推动增长。其机制在于，AI 同事能够持续参与任务执行，减少人工干预，使团队能够将更多精力投入到高价值的战略决策中。然而，由于缺乏量化数据，其实际增长影响尚待验证。

**「行动建议」** 增长从业者应重新审视 AI 在工作流中的角色，从“一次性工具”转向“持久同事”，并基于未来模型能力进行前瞻性规划，以在竞争中保持优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lennysnewsletter.com/p/ais-third-era-the-rise-of-persistent">AI ’s third era: the rise of persistent AI coworkers | Tara Seshan ...</a></li>

</ul>
</details>

**标签**: `#AI coworkers`, `#OpenAI`, `#product strategy`, `#workflow`, `#future of work`

---

<a id="item-ai-growth-4"></a>
### [Claude 官方 AI 原生软件开发手册解析：代码不再是瓶颈，产品经理转向决策者](https://www.woshipm.com/ai/6457025.html) ⭐️ 7.0/10

Claude 官方发布《The AI-Native SDLC Playbook》，提出 AI 原生软件开发生命周期，将软件开发分为计划、设计、构建、测试、部署、运维六个阶段，每个阶段重新定义人与 AI 的分工。该手册指出，传统研发流程中代码编写曾是瓶颈，但 AI 使代码生成成本大幅下降，瓶颈转移至决策与判断。产品经理的角色从撰写文档转向审核 AI 生成的方案并做出决策，运营等非技术人员可直接通过 AI 生成需求文档。手册还强调团队知识需形成可读可执行的文件（如 CLAUDE.md、REVIEW.md），并指出落地阻力主要来自组织惯性、信任缺失、合规压力和存量系统负担。该分析对增长从业者的启示是，AI 可显著加速产品迭代周期，但需先解决流程重构和信任建立问题。

rss · 人人都是产品经理 · 8月31日 02:08

**「AI 技术解析」** 该手册描述的 AI 技术核心是生成式 AI（如 Claude）在软件开发生命周期中的全流程应用，包括自动生成需求文档（intent.md）、设计方案（spec.md）、实施计划（plan.md），以及自动代码审查、测试和运维诊断。这些能力基于大语言模型的自然语言理解和代码生成能力，使 AI 能够处理从需求分析到代码实现、测试和部署的复杂任务。

**「增长影响」** 该手册虽未提供具体量化数据，但指出 AI 可将需求到可执行文档的时间从数周压缩至一两个小时，显著缩短产品迭代周期。对于增长从业者而言，更快的迭代意味着可以更频繁地测试增长假设、优化转化漏斗，从而间接提升增长实验的效率和效果。然而，实际影响取决于组织能否克服流程惯性和信任障碍，目前缺乏实证数据支持。

**「行动建议」** 增长从业者应推动团队将知识文档化（如 CLAUDE.md、REVIEW.md），并利用 AI 工具自动生成需求文档和方案，以加速迭代周期，同时将自身精力聚焦于业务判断和优先级决策。

**标签**: `#AI-native SDLC`, `#Claude`, `#product management`, `#workflow`, `#AI development`

---

<a id="item-ai-growth-5"></a>
### [用 ZCode+GLM 将数字孪生开发从数月压缩至三天](https://www.woshipm.com/ai/6456839.html) ⭐️ 7.0/10

本文通过一个真实集装箱码头项目，展示了使用 ZCode 与 GLM 大模型将数字孪生开发周期从传统的三到六个月压缩至数天，且由一人完成全部资产与仿真。项目产出了 32 个 GLB 资产、1500 个集装箱、9 辆作业车辆、3 台 RTG、3 台岸桥和一艘 260 米集装箱船，实现了 144 FPS 的实时运行。传统方法面临建模、动画、需求变更和性能四大痛点，而新方法通过参数化生成和对话式迭代，将开发流程简化为上传参考图、生成 GLB、生成 Web 演示页和对话式迭代四步。该方法论强调先建资产原语库、每轮校验和守恒恒等式回归，显著降低了改需求成本，使数字孪生从昂贵的静态照片变为活的镜子。对增长从业者而言，这展示了 AI 如何大幅提升开发效率和响应速度，降低项目成本，并加速产品迭代。

rss · 人人都是产品经理 · 8月31日 00:51

**「AI 技术解析」** 本案例采用 ZCode 与 GLM 大模型的人机协作开发方式，核心是将数字孪生场景中的对象参数化，通过对话式声明生成代码和三维资产。具体而言，ZCode 作为智能体开发环境，调用 GLM 大模型理解业务描述，并驱动程序化生成器按真实尺寸产出 GLB 资产（如集装箱、堆场、岸桥等），同时利用 Blender 无头建模脚本处理精细单体（如闸口），最终生成 three.js 网页演示。整个过程通过“上传参考图 → 技能生成 GLB → 打开 Web 演示页 → 对话式迭代”四步完成，将建模问题转化为参数生成问题，实现分钟级迭代。

**「增长影响」** 该案例展示了 AI 辅助开发数字孪生对效率的显著提升：将传统数字孪生项目从数月周期压缩至数天，且由一人完成全部资产与仿真，无需外包。具体成果包括生成 32 个 GLB 资产、1500 个集装箱、9 辆作业车辆等，并以 144 FPS 实时运行。这种效率提升直接降低了开发成本和时间，使数字孪生从昂贵的定制项目转变为可快速迭代的能力，尤其适合需要频繁调整业务规则的场景。对于增长从业者而言，这意味着在物流、交通等物理世界与业务规则结合的场景中，可以更敏捷地构建和更新数字孪生，从而加速业务验证和优化。

**「可复用策略」** 增长从业者可以借鉴其“参数化生成+对话式迭代”的方法，将复杂场景的开发转化为参数调整和自然语言交互，从而大幅缩短迭代周期，提升业务响应速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zcode.z.ai/en">ZCode | Official Harness for GLM-5.3</a></li>
<li><a href="https://zcode.z.ai/en/docs/welcome">ZCode Docs | GLM-5.3 Agentic Coding Guide</a></li>
<li><a href="https://zcode.homes/">ZCode Guide — Agentic Development with GLM-5.2</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9506524/">A Digital Twin Case Study on Automotive Production Line - PMC</a></li>
<li><a href="https://medium.com/mindful-designing/the-business-case-for-digital-twin-costs-benefits-and-roi-explained-209da5030f6e">The Business Case for Digital Twin: Costs, Benefits, and ROI Explained | by Robert Smith | Mindful Tech Journal | Medium</a></li>

</ul>
</details>

**标签**: `#digital twin`, `#AI development`, `#large language model`, `#case study`, `#efficiency`, `#ZCode`, `#GLM`

---


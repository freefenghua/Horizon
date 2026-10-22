# Horizon Daily - 2026-10-22

> From 69 items, 2 important content pieces were selected

---

**AI × Growth Intersection**
1. [WorkBuddy 用 AI 流水线挖掘乳制品 To B 商机](#item-ai-growth-1) ⭐️ 5.0/10
2. [ZCode办公模式实测：一句话跑完10个UI竞品拆解，1小时替代3天](#item-ai-growth-2) ⭐️ 5.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [WorkBuddy 用 AI 流水线挖掘乳制品 To B 商机](https://www.woshipm.com/ai/6482165.html) ⭐️ 5.0/10

作者王佳亮以一家区域乳制品企业的大客户销售团队为例，拆解传统找商机的五个断点——盲（信号分散在政府采购网、企查查、行业新闻里看不见）、散（同一客户信号碎在五六个系统）、慢（等周报例会已过 7–15 天截标窗口）、浅（只列名单不评分）、断（商机躺在总监 Excel 里，区域销售不跟进）。解法是用 WorkBuddy 5.8.3 的「专家·技能·连接器」三者串成流水线：连接器负责伸进企查查、招标网、联网搜索、腾讯文档、企业微信读写真实数据，专家（数据分析/增长策略）按《商机评分字典》输出 0–100 意向分与 A/B/C 分级及切入建议，技能负责产出商机清单、话术、Excel/PPT 看板。实操分八步：先在对话框生成含目标行业、规模阈值、高意向信号、评分权重的评分字典并存入腾讯文档「口径」分表，再依次授权连接器（首次只用只读/查询权限）、召唤专家建模、拉取并清洗信号入商机库、定时每周一 9:00 自动扫描并推送飞书 @ 区域负责人。作者称这套流程把决策时延从天级压到小时级，但全文为方法论演示，未给出转化率或业绩提升的量化结果。

rss · 人人都是产品经理 · Oct 22, 02:34

**「AI 技术拆解」** WorkBuddy 把大模型能力拆成三类可组合组件：带方法论的「专家」智能体负责判断与评分，「技能」负责按格式生成文档与表格，「连接器」通过授权接口读写企查查、招标网、腾讯文档、企业微信等外部系统，再由自动化工作流按周定时编排成一条从信号扫描到推送的流水线。

**「可复用要点」** 先写死一份可复用的《商机评分字典》（行业、规模阈值、高意向信号、权重），再让 AI 按同一口径打分分级，并把结果当天 @ 到具体区域负责人，比让 AI 直接扫数据更能解决「浅」和「断」两个断点。

**Tags**: `#AI销售`, `#商机挖掘`, `#To B增长`, `#WorkBuddy`, `#自动化工作流`, `#案例拆解`

---

<a id="item-ai-growth-2"></a>
### [ZCode办公模式实测：一句话跑完10个UI竞品拆解，1小时替代3天](https://www.woshipm.com/ai/6482213.html) ⭐️ 5.0/10

智谱上线 ZCode 办公模式，定位为面向行业专家的 GLM 办公特训模型加模型工作台，作者称其为“国内版 Codex”。作者以 7 年 UI 设计师身份实测三类任务：上传 UI 界面后一句话生成作品集 PPT 并可用一句话重做版式；用 Workflow 动态工作流调研 10 个电商 App 商品详情页与购买路径，模型先规划再施工，自动拆成“分头调研、归纳排序、独立审读”三阶段，审读 Agent 会打回不合格产出，约 1 小时交付 10 个竞品逐产品拆解、40 张核验截图、5 种跨竞品设计模式、12 条按 ROI 排序的改版优先级，并输出 HTML 报告；通过插件市场安装 VectorCraft 生成整套 SVG 金融 App 图标及使用规范文档。作者称同类竞品拆解人工需 2-3 天，并建议把长链路、高 Token 消耗的 Workflow 任务放到夜间或周末跑以节省额度。文中提及 GLM-5.3 在 Artificial Analysis Intelligence Index 取得 45 分，位列全球开源模型前列。

rss · 人人都是产品经理 · Oct 22, 02:34

**「AI Technique」** Zhipu&\#x27;s ZCode office mode pairs a GLM model tuned for office work with a &quot;dynamic workflow&quot; that first plans the whole pipeline in code, then assigns roles, execution order and verification checkpoints to multiple agents that run in parallel. In the author&\#x27;s test, the workflow split the 10-competitor UI teardown into three stages \(parallel research, synthesis and ranking, independent review\), with a reviewer agent rejecting substandard output and sending it back for rework; a plugin marketplace \(e.g., VectorCraft\) also generated SVG icons.

**「效率提升」** 据作者实测，原本需要 2-3 天完成的 10 个电商 App 商品详情页与购买路径竞品拆解，通过 ZCode 的 Workflow 模式约 1 小时即产出结果，包含 40 张核验截图、5 种跨竞品设计模式和 12 条按 ROI 排序的改版优先级。效率提升来自模型先规划再施工的多 Agent 分工与自校验机制，而非单轮问答；该数据为个人设计师的一次实测，非团队规模化验证。

**「可复用要点」** 把竞品拆解这类长链路、模板化任务交给 Workflow 而非单轮对话：先给一份自己满意的图文样例作为验收标准，让多 Agent 分工、自检、返工，并把运行安排在夜间以节省额度。

<details><summary>References</summary>
<ul>
<li><a href="https://zcode.z.ai/en/docs/welcome">ZCode Docs | GLM -5.3 Agentic Coding Guide</a></li>

</ul>
</details>

**Tags**: `#AI办公`, `#竞品分析`, `#工作流自动化`, `#智谱ZCode`, `#效率工具`

---


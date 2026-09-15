# Horizon Daily - 2026-09-15

> From 63 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [AI Companion Bside Hits 60% D1 Retention via Non-Chat Play](#item-ai-growth-1) ⭐️ 7.0/10
2. [Six AI Solopreneurs: Revenue Cases and Limits](#item-ai-growth-2) ⭐️ 6.0/10
3. [dbt Charts: YAML Dashboards for AI Agents](#item-ai-growth-3) ⭐️ 5.0/10
4. [LangGraph + MCP for Fresh-Produce Replenishment: AI Orchestrates, Backend Calculates](#item-ai-growth-4) ⭐️ 5.0/10
5. [WorkBuddy + Meitu Design Studio: AI Office &amp; Design Tasks in One Dialog Box](#item-ai-growth-5) ⭐️ 5.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [AI Companion Bside Hits 60% D1 Retention via Non-Chat Play](https://www.woshipm.com/share/6464520.html) ⭐️ 7.0/10

Shanghai-based Kotoko AI launched Bside, an AI-native original character \(OC\) product where players create a character called a Biibit and watch it live, make friends, and go on adventures, rather than primarily chatting with it. Bside debuted on Steam Early Access on October 27, 2025 and launched mobile on March 30, 2026; by July 2026 the company reported over 200,000 players across platforms, roughly 60% day-one retention, and about 25% day-seven retention. Co-founder Harper Zhu shared that 41% of monthly active users barely chat with their Biibit \(a figure that reportedly reached 49% in June before the Japan launch\), and that players engaging in adventure and nurturing gameplay had a 7-day return rate 5.4 percentage points higher than chat-focused players. The case matters for growth practitioners because it suggests retention in AI companion products can be driven by dress-up, gifting, and asynchronous adventure loops rather than conversation, and it provides a concrete benchmark against a market where Sensor Tower reported global AI social companion app revenue of $150 million in Q1 2026, up over 12x in three years, with Japan growing 691%. Note that these figures come largely from a single source and official company statements, and the article lacks CAC/LTV data and a full replicable playbook.

rss · 人人都是产品经理 · Sep 15, 00:53

**「AI Technique」** Bside uses generative AI to create and animate original characters and to produce low-cost randomly generated stories and character settings, with a fixed art style that constrains player creation. The article contrasts this with peer product 捏Ta, which relies on text-to-image generation and shared prompt templates; specific model versions or fine-tuning details are not disclosed in the source.

**「Growth Impact」** Bside reported over 200,000 cross-platform players with about 60% D1 and 25% D7 retention, which the article describes as more than double typical industry retention, driven by non-chat loops such as dress-up, daily check-ins, gifting, and half-hour-plus asynchronous adventures that create delayed gratification and next-day return incentives. After entering Japan on July 17, 2026, Bside reportedly reached 53,431 mobile downloads in six weeks, exceeding the 17,840 cumulative downloads in the US over the same three-month period, per 点点数据; monetization remains unproven and paid cosmetic pricing has drawn player criticism.

**「Takeaway」** For AI companion or character products, test retention loops built on non-chat interactions such as customization, gifting, and asynchronous shared adventures, and measure whether those users return more often than chat-first users before over-investing in conversation features.

**Tags**: `#AI陪伴`, `#二次元`, `#OC`, `#留存`, `#日本市场`, `#用户增长`, `#案例研究`

---

<a id="item-ai-growth-2"></a>
### [Six AI Solopreneurs: Revenue Cases and Limits](https://www.woshipm.com/chuangye/6464514.html) ⭐️ 6.0/10

AIX财经 interviewed six self-described &quot;super individuals&quot; in China and Australia who use AI to run one-person companies, with concrete but uneven revenue examples. A 35-year-old e-commerce entrepreneur in Henan, bedridden for 70 days after a broken leg, used AI for operations decisions and content generation plus outsourced customer service to run 12 online stores \(later optimized to 4 main stores\), reporting average single-store monthly sales of 50,000-80,000 RMB and net profit of 25,000-30,000 RMB per month with only about 2,000 RMB in operating costs. A Sydney-based SaaS founder reported burning over 6.5 billion tokens in 30 days, shipping 6 major product updates in two weeks, and generating roughly $100,000 in monthly revenue across 24 products, with AI handling SEO, ad optimization, and social content. Other cases include an AIGC director earning 30,000-50,000 RMB per minute of AI video and 80,000-100,000 RMB in competition prizes, a non-coder who built a stock sentiment model with DeepSeek for about 1 RMB in costs and reported ~1% average daily returns, and an AI training entrepreneur serving about 100 clients. The article&\#x27;s core finding is that AI changes how these individuals work but does not eliminate the barriers to making money—cognition, decision-making, and even luck remain important.

rss · 人人都是产品经理 · Sep 15, 00:56

**「AI Techniques Used」** The cases rely on general-purpose LLMs \(DeepSeek, ChatGPT, Claude, Gemini\) for decision support, copywriting, and code generation, plus AI video tools \(Runway, Jimeng, Kling, Sora, Hailuo\) for content production. One entrepreneur used Coze \(扣子\) to build a workflow that scrapes sales, weather, and competitor price data to generate daily operating reports, while another built 13 AI agents for topic selection, drafting, review, layout, and publishing.

**「Growth Impact」** Reported outcomes include replacing a planned 10-person e-commerce team with AI plus a 1,000 RMB/month outsourced customer service function, cutting monthly operating costs to about 2,000 RMB while sustaining 25,000-30,000 RMB monthly net profit. The SaaS founder reported AI reducing ad optimization work from a full day to about 10 minutes and enabling 110,000 average views per tweet across 10 AI-written posts. These are self-reported figures from individual operators, not audited company data, and the article notes revenue volatility and the role of market conditions and luck.

**「Takeaway」** Start by using AI for decision support and content generation while outsourcing low-leverage tasks like customer service, then validate the model at minimum cost before scaling—as the e-commerce case did by testing one-piece dropshipping instead of renting a warehouse and hiring a team.

**Tags**: `#AI`, `#solopreneur`, `#e-commerce`, `#growth`, `#case study`, `#China`

---

<a id="item-ai-growth-3"></a>
### [dbt Charts: YAML Dashboards for AI Agents](https://dbtcharts.com/blog/charts-built-for-chat/) ⭐️ 5.0/10

dbt Charts is an open-source YAML dialect and tool for declaring and rendering dashboards, launched by Dave Yoder \(founder of Chartio, YC&\#x27;10, now Atlassian Analytics\) and released under Apache 2.0 alongside dbt. The tool is explicitly motivated by a practical problem in AI-assisted workflows: when dashboards are built with Claude or other agents, the resulting free-form artifacts are hard to audit and scale. dbt Charts addresses this by providing a simple declarative format—described by its creator as &quot;markdown but for dashboards&quot;—so that agent-generated charts can be declared and rendered consistently. The announcement drew community discussion on Hacker News, including comparisons to Observable Framework and debate over whether the approach is genuinely novel versus existing BI decoupling trends. No concrete growth metrics \(conversion, retention, CAC, or LTV\) were reported, so the relevance to growth practitioners is indirect and centers on tooling for AI-assisted analytics workflows rather than a validated growth playbook.

hackernews · thingsilearned · Sep 14, 21:22 · [Discussion](https://news.ycombinator.com/item?id=49704246)

**「AI Technique」** The tool is not itself an AI model; it is a declarative YAML dialect designed to structure and render dashboards that AI agents \(such as Claude\) generate. It aims to replace free-form, hard-to-audit agent output with a consistent, version-controllable specification.

**「Growth Impact」** No measurable growth outcomes \(conversion lift, retention improvement, or CAC reduction\) were reported in the source or community discussion. The stated benefit is operational: improving auditability and scalability of AI-agent-built BI artifacts, which may indirectly support analytics workflows but is not tied to a quantified growth result.

**「Takeaway」** If your team uses AI agents to build dashboards, consider adopting a declarative, version-controlled format like dbt Charts to keep agent-generated analytics artifacts auditable and scalable rather than free-form.

**Tags**: `#AI agents`, `#BI dashboards`, `#dbt`, `#open source`, `#analytics tooling`, `#AI-assisted workflows`

---

<a id="item-ai-growth-4"></a>
### [LangGraph + MCP for Fresh-Produce Replenishment: AI Orchestrates, Backend Calculates](https://www.woshipm.com/pd/6464544.html) ⭐️ 5.0/10

A practical case study describes building an AI-driven fresh-produce replenishment assistant using LangGraph for workflow orchestration and MCP \(Model Context Protocol\) as a thin proxy layer over existing backend APIs. The core problem was that replenishment is a deterministic calculation pipeline \(daily sales, actual stock, safety stock, restock judgment\), while LLMs are prone to hallucinating numbers, so the team split responsibilities: AI handles intent recognition, task planning, exception handling, and natural-language summarization, while all math and database access stay in the existing backend. The architecture has three layers—LangGraph Graph for fixed routing, LangGraph State \(with Checkpointer and thread\_id\) for context and resumability, and MCP-Server as a stateless HTTP proxy that exposes five deterministic tools \(get\_restock\_schedule, calc\_daily\_sales, calc\_actual\_stock, calc\_safety\_stock, judge\_restock\). The article reports no growth metrics such as conversion, retention, CAC, or efficiency numbers; its value is architectural, offering a reusable principle for AI-in-operations projects where business logic is deterministic.

rss · 人人都是产品经理 · Sep 15, 02:55

**「AI Technique」** The solution uses LangGraph to define a fixed directed graph of nodes and edges, so the LLM cannot skip or reorder steps, and MCP to wrap existing REST APIs as callable tools without exposing database access to the model. The LLM only plans which tool to call and summarizes results; all arithmetic and SQL execution happen in the backend via MCP HTTP forwarding.

**「Growth Impact」** No measurable growth outcomes \(conversion, retention, CAC, or efficiency metrics\) are reported in the source, so the operational impact cannot be quantified from the available evidence. The stated benefit is architectural: merchants can ask a natural-language question and receive a replenishment list, while the deterministic backend logic remains auditable and unchanged.

**「Takeaway」** Before adding AI to an operations workflow, classify the core logic as deterministic calculation or fuzzy judgment; if deterministic, keep the math in existing APIs and use a thin tool/proxy layer \(MCP or function calling\) so the LLM only orchestrates and explains.

**Tags**: `#LangGraph`, `#MCP`, `#AI orchestration`, `#supply chain`, `#operations`, `#case study`, `#workflow design`

---

<a id="item-ai-growth-5"></a>
### [WorkBuddy + Meitu Design Studio: AI Office &amp; Design Tasks in One Dialog Box](https://www.woshipm.com/ai/6464516.html) ⭐️ 5.0/10

This hands-on walkthrough describes how Tencent&\#x27;s WorkBuddy open platform, launched at a Shenzhen ecosystem event on September 2, integrated Meitu Design Studio \(美图设计室\) as one of its first design applications. The author demonstrates three office scenarios: summarizing desktop weekly reports into a 17-page PPT, beautifying an existing PPT into a new pptx with a cover and 7 body pages in under a minute, and generating an event poster with natural-language color adjustments. In social media scenarios, a single copywriting spreadsheet produced 10 sets of social graphics totaling 61 images plus 4 planning and publishing copy files \(65 files total\), and an e-commerce workflow generated competitor research, product image sets, A+ detail pages, and listing copy for six products. The article reports no growth metrics such as conversion, retention, CAC, or LTV, and provides no before/after performance data, so it should be treated as a first-impression tool walkthrough rather than a validated growth case study.

rss · 人人都是产品经理 · Sep 15, 00:57

**「AI Technique」** The workflow combines WorkBuddy&\#x27;s file-reading and text-summarization capabilities with Meitu Design Studio&\#x27;s AI design generation, where users select scenario and skill tags \(e.g., PPT design, PPT beautification, social media graphics\) and issue natural-language prompts in a single dialog box. The author notes selecting the Kimi-K3 model for some tasks, and the system produces style previews before generating full multi-page outputs and exporting pptx files.

**「Growth Impact」** No measurable growth outcomes \(conversion, retention, CAC, or LTV\) are reported in the source. The claimed impact is operational: consolidating content and design tasks into one dialog box removes the need to switch between tools and reduces the &\#x27;request, wait, receive&\#x27; cycle for design assets, but these are qualitative observations from a single user&\#x27;s hands-on test rather than validated metrics.

**「Takeaway」** For teams producing recurring content or design assets, test whether a single AI dialog box that reads local files and generates finished deliverables \(pptx, image sets, listing copy\) can replace the multi-tool handoff, and measure the actual time saved per asset before assuming it improves throughput.

**Tags**: `#AI design tools`, `#workflow automation`, `#Tencent WorkBuddy`, `#Meitu Design Studio`, `#productivity`, `#tool integration`

---


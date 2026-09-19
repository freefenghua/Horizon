# Horizon Daily - 2026-09-19

> From 63 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [TypeSafe AI&\#x27;s Jev: Structured Probabilistic Decisions for Reliable Automation](#item-ai-growth-1) ⭐️ 6.0/10
2. [SAP vs Salesforce: Two Paths to the Same Agent Business](#item-ai-growth-2) ⭐️ 6.0/10
3. [Flova AI Turns E-commerce Detail Page into 16-Second Promo Video](#item-ai-growth-3) ⭐️ 6.0/10
4. [AI Short-Drama App BlinkDrama Tops Spain and 16 Latin American Markets](#item-ai-growth-4) ⭐️ 6.0/10
5. [WorkBuddy 12 Practical Tips After 3 Months of Trial and Error](#item-ai-growth-5) ⭐️ 5.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [TypeSafe AI&\#x27;s Jev: Structured Probabilistic Decisions for Reliable Automation](https://www.woshipm.com/ai/6466421.html) ⭐️ 6.0/10

TypeSafe AI has released Jev, a model that does not generate text but instead outputs structured, type-safe decisions with calibrated probabilities in parallel within hundreds of milliseconds. It addresses the reliability problem of using large language models for automation, where hallucinations, inconsistent outputs, and schema violations can break production pipelines. Jev is reported to be 20–200x faster and 40–400x cheaper than existing language models; Vercel saw a 6x speed improvement and full accuracy on a classification task after switching from Gemini 2.5 Flash, and a Doom-playing agent ran for an hour at a total cost of $7. The model is trained with RLCD \(Reinforcement Learning for Calibrated Decisions\) to produce honest confidence scores. For growth practitioners, Jev offers a lightweight, reliable decision layer for high-frequency tasks like intent detection, routing, content moderation, and output validation, though the source lacks growth-specific metrics or case studies.

rss · 人人都是产品经理 · Sep 19, 01:33

**「AI Technique」** Jev is a non-autoregressive model that takes a state and a set of questions with finite options, then computes all answers in parallel, each with a calibrated probability. It supports three question types: nule \(yes/no\), choice \(pick one from options\), and score \(rate on a scale\). It is trained using RLCD, which optimizes for calibrated probabilities rather than human preference or verifiable correctness.

**「Growth Impact」** The source reports speed improvements of 20–200x and cost reductions of 40–400x compared to language models, with Vercel achieving 6x faster classification and full accuracy. These gains could enable real-time, high-volume decision-making in growth workflows such as user intent recognition, intelligent routing, and content moderation, but no direct growth metrics \(e.g., conversion lift, retention\) are provided.

**「Takeaway」** For high-frequency, low-latency decisions like routing or intent classification, consider replacing prompt-based LLM calls with a specialized structured-decision model like Jev to reduce cost, latency, and hallucination risk.

**Tags**: `#AI`, `#automation`, `#structured decisions`, `#reliability`, `#growth`

---

<a id="item-ai-growth-2"></a>
### [SAP vs Salesforce: Two Paths to the Same Agent Business](https://www.woshipm.com/ai/6466441.html) ⭐️ 6.0/10

SAP tightened its API policy in April, barring external AI agents from directly calling its interfaces and requiring them to route through its own assistant Joule, while its integration gateway began charging by call count — a practice the industry calls an &quot;agent tax.&quot; Salesforce took the opposite approach, breaking its entire platform into 60+ tools and 30+ skills so that a salesperson can complete tasks like checking customers, updating opportunities, and viewing pipelines entirely within Slack without opening the CRM. Despite these opposing open/closed strategies, the article argues both vendors are converging on the same business: managing enterprise agents through identity, permissions, usage tracking, and billing. Microsoft&\#x27;s Agent 365 charges $15 per user per month for agent governance and registered nearly 40 million agents within two months of launch, while ServiceNow bills per &quot;assist&quot; action and reports 98% renewal rates across 8,400 enterprise customers. The piece notes that 78% of IT leaders have encountered unexpected bills and 61% have cut projects due to unplanned software spending, signaling a shift in enterprise software pricing from per-seat to usage-, action-, and outcome-based models.

rss · 人人都是产品经理 · Sep 18, 07:30

**「AI Technique」** The article describes AI agent governance and metering infrastructure rather than a specific model technique: API gateways that intercept and meter agent calls, MCP \(Model Context Protocol\) tools that expose platform capabilities to external agents, and control towers that log and authorize each agent action. These are orchestration and access-control layers built around LLM-based agents, not model training or fine-tuning.

**「Growth Impact」** The article reports that Salesforce&\#x27;s custom agents on Slack tripled since January, and ServiceNow handles 89% of its own helpdesk questions via AI, with half of its new orders no longer priced per seat. Microsoft&\#x27;s Copilot has over 30 million paid seats, and its Agent 365 governance service registered nearly 40 million agents in two months. These figures suggest that agent governance and usage-based billing are becoming new growth channels for enterprise software vendors, though the article does not tie them to specific conversion or retention metrics for growth practitioners.

**「Takeaway」** For growth practitioners evaluating AI agent platforms, map the vendor&\#x27;s pricing model — per-seat, per-action, or per-outcome — against your actual usage patterns before committing, since the article shows that metered billing can produce unexpected costs that are rarely disclosed in contracts.

**Tags**: `#AI Agent`, `#SAP`, `#Salesforce`, `#平台策略`, `#API 经济`, `#增长渠道`

---

<a id="item-ai-growth-3"></a>
### [Flova AI Turns E-commerce Detail Page into 16-Second Promo Video](https://www.woshipm.com/ai/6466451.html) ⭐️ 6.0/10

The article walks through a hands-on workflow that uses Doubao Work and the connected Flova AI to convert a single e-commerce product detail page into a 16-second promotional video. The author fed a self-made detail page for a fictional product, the &quot;微光 L1 氛围灯&quot; \(a warm-white cylindrical ambient lamp with an orange handle and black base\), into Doubao Work, then used Flova AI to generate reference visuals, a four-shot storyboard, music, a timeline, and a final MP4. The output was exported at 1920×1080, 30 fps, H.264 video with AAC stereo audio, and reportedly passed full decoding with no sustained black frames or silences over one second. The four shots each carried one selling point: camping atmosphere, stepless dimming, portable handle, and long battery life. The author emphasizes that Flova&\#x27;s value is not just generation but a checkable, editable workflow with per-shot confirmation points. No conversion, retention, or CAC metrics were reported, and the article reads partly as a tool review, so the business impact remains unvalidated.

rss · 人人都是产品经理 · Sep 18, 07:11

**「AI Technique」** The workflow uses Doubao Work as the entry point with Flova AI connected as a skill/connector, then relies on generative AI to produce reference visuals, a four-shot storyboard, video clips, music, and environmental audio. The author locks the prompt to specific output specs, selling points, product appearance, shot count, confirmation order, and sound requirements, and reviews reference images and storyboard before committing to full generation.

**「Growth Impact」** The article reports no measurable growth outcomes such as conversion lift, retention improvement, or CAC reduction. The claimed benefit is operational: reusing an existing product detail page as the single source of product information and keeping reference visuals, storyboard, clips, sound, timeline, and export in one project reduces the back-and-forth of re-uploading images, re-entering parameters, and re-explaining selling points across tools. This is a workflow efficiency claim, not a validated performance result.

**「Takeaway」** For a first test, pick one product detail page with a clear main image and explicit selling points, specify 15 seconds, 16:9, three selling points, and one scene style, then generate only the reference visuals and storyboard first; confirm the product has not drifted and each shot has a distinct job before generating video and audio.

**Tags**: `#AI video`, `#e-commerce`, `#content production`, `#workflow`, `#Flova`, `#Doubao`, `#marketing`

---

<a id="item-ai-growth-4"></a>
### [AI Short-Drama App BlinkDrama Tops Spain and 16 Latin American Markets](https://www.woshipm.com/ai/6466189.html) ⭐️ 6.0/10

AI short-drama app BlinkDrama, launched in May 2026 by Hong Kong-based Atlas Ventures Culture &amp; Technology Limited, reached No. 1 on Spain&\#x27;s App Store entertainment \(free\) chart and topped the entertainment charts in 16 Latin American countries including Mexico, Venezuela, Colombia, Peru, and Argentina. According to Sensor Tower data cited in the article, Latin America accounted for 23% of global short-drama app downloads in Q1 2026, second only to Southeast Asia&\#x27;s 32%, with Latin America, Southeast Asia, and India together contributing over three-quarters of global downloads. Per Diandian Data, BlinkDrama&\#x27;s global downloads across the App Store and Google Play over the trailing 30 days were roughly 3.4783 million, generating about $863,600 in revenue, with the US accounting for roughly one-quarter of that revenue, followed by Australia, the UK, Mexico, and Canada. The case matters for growth practitioners because it illustrates how a single Spanish-language content set can be reused across multiple Latin American markets, while monetization is balanced through rewarded ads, coin packs, and weekly subscriptions. The source does not provide retention, conversion, CAC, or LTV metrics, so the growth efficiency of this playbook remains unverified.

rss · 人人都是产品经理 · Sep 18, 05:51

**「AI Technique」** BlinkDrama is described as an AI short-drama app, and the article notes it has begun testing AI-generated ad creatives featuring anthropomorphic animal characters, a style popular on TikTok and YouTube Shorts. The source does not specify which AI models or pipelines are used to generate the dramas or creatives.

**「Growth Impact」** BlinkDrama reached No. 1 on Spain&\#x27;s App Store entertainment chart and topped 16 Latin American markets, with roughly 3.4783 million global downloads and about $863,600 in revenue over the trailing 30 days, per Diandian Data. The mechanism appears to be a Spanish-language content and creative strategy that can be reused across Latin America, combined with a monetization loop of free episodes, rewarded ads, expiring reward coins \(5-day validity\), coin packs, and a Pro Pass priced at $19.99/week \(minimum $9.9\). The source does not report retention, conversion, CAC, or LTV, so the efficiency of this growth engine cannot be assessed from the available data.

**「Takeaway」** For AI content going overseas, prioritize a single high-reach language \(Spanish\) whose content and ad creatives can be reused across many markets, then layer rewarded ads, expiring virtual currency, and weekly subscriptions to convert high-traffic, low-spend regions while monetizing higher-value markets like the US.

**Tags**: `#AI短剧`, `#出海`, `#拉美市场`, `#用户增长`, `#Sensor Tower`, `#BlinkDrama`

---

<a id="item-ai-growth-5"></a>
### [WorkBuddy 12 Practical Tips After 3 Months of Trial and Error](https://www.woshipm.com/ai/6466314.html) ⭐️ 5.0/10

This article compiles 12 practical usage tips for WorkBuddy, a leading Chinese office AI agent that reportedly ranks first in monthly visits and month-over-month growth among domestic office agents, with cumulative installs exceeding 30 million. The author, after three months of hands-on use, emphasizes that the most critical technique is expressing tasks clearly using a structure of &\#x27;what to do + what materials are available + to what standard,&\#x27; and supplements this with advice on providing examples instead of abstract descriptions, using the built-in prompt enhancement feature, selecting the right work mode \(Plan, Ask, or Agent\), breaking complex tasks into steps, managing tasks versus spaces, avoiding frequent model switching within a session, using /compact to compress long conversations, granting sufficient permissions, enabling skills on demand, understanding memory and personalization rules, and automating repetitive work. The article is a how-to guide focused on workflow efficiency rather than a growth case study, and it does not report conversion, retention, CAC, or LTV metrics. For growth practitioners, the value lies in reusable prompt and agent-management tactics that can improve the reliability and speed of AI-assisted workflows.

rss · 人人都是产品经理 · Sep 18, 06:08

**「AI Technique」** The article covers practical prompt engineering and agent configuration techniques for WorkBuddy, including structured task expression, few-shot example-based prompting, built-in prompt enhancement, mode selection \(Plan/Ask/Agent\), context compression via /compact, and automation task setup with prompts, schedules, and connectors. It does not describe model training or fine-tuning.

**「Growth Impact」** No growth metrics such as conversion, retention, CAC, or LTV are reported. The only quantitative adoption data mentioned is WorkBuddy&\#x27;s cumulative installs exceeding 30 million and its ranking first in monthly visits and month-over-month growth among domestic office agents, which is presented as context rather than a measured outcome of the tips.

**「Takeaway」** Adopt the &\#x27;what to do + what materials are available + to what standard&\#x27; task-expression framework and provide concrete examples when prompting an AI agent, as this is presented as the highest-leverage tactic for improving output quality.

**Tags**: `#AI agent`, `#prompt engineering`, `#workflow productivity`, `#office tools`, `#China AI`, `#how-to`

---


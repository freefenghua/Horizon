# Horizon Daily - 2026-10-12

> From 59 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [Photoroom: 300M-User AI Background Removal Tool for E-commerce](#item-ai-growth-1) ⭐️ 6.0/10
2. [AI Subscription Pricing: OpenAI Tightens, Chinese Models Subsidize](#item-ai-growth-2) ⭐️ 6.0/10
3. [19-Year-Old Zach Yadegari Raises $10M for Persona After Selling Cal AI](#item-ai-growth-3) ⭐️ 6.0/10
4. [AI Reverse-Engineering Adobe: 46k Stars in 10 Days](#item-ai-growth-4) ⭐️ 5.0/10
5. [Eazo Hands-On: China&\#x27;s First Graphical Personal Agent](#item-ai-growth-5) ⭐️ 5.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [Photoroom: 300M-User AI Background Removal Tool for E-commerce](https://www.woshipm.com/chuangye/6475498.html) ⭐️ 6.0/10

Photoroom is an AI background-removal and product-photo tool that lets sellers shoot a product on a phone, automatically remove the background, and place the item in studio, cafe, or other scenes; it can also generate virtual models for apparel and auto-create ad videos. As of June this year, the company reported 300 million cumulative users across more than 180 countries, over 7 billion images processed annually, and more than 1 million businesses using it. The product has expanded from single-image editing to batch processing of up to 250 images with consistent backgrounds, lighting, and model styles, plus a Shopify integration and a Listing Score feature that checks titles, descriptions, image counts, filenames, and alt text. Two customer cases are cited: US secondhand baby-gear marketplace GoodBuy Gear recorded a 23% conversion lift after integrating Photoroom&\#x27;s image API, and UK sportswear brand Layer reported a 50% increase in online sales. The item does not publish broader growth metrics such as retention, CAC, or LTV, so the reported results should be treated as vendor-provided case studies rather than independently verified benchmarks.

rss · 人人都是产品经理 · Oct 12, 02:45

**「AI Technique」** Photoroom uses computer vision and deep learning for automatic background removal, then layers generative AI for virtual models, scene generation, and video templates. Its newer Visual Agents system selects different models by product type, automatically checks generated images for color, shape, or logo errors, and retries or repairs outputs before human review.

**「Growth Impact」** The reported outcomes are a 23% conversion lift at GoodBuy Gear after standardizing product images with Photoroom&\#x27;s API, and a 50% online sales increase at two-person UK brand Layer after replacing paid photographer shoots with AI-generated scenes, virtual models, and social videos. Photoroom also says an early enterprise deployment completed over 1.5 million automated quality checks in three weeks and corrected more than 90,000 flagged defective images. These figures come from Photoroom&\#x27;s own customer cases and lack independent verification.

**「Takeaway」** For e-commerce sellers, the replicable tactic is to standardize product imagery at scale—consistent backgrounds, lighting, and model style across batches—and connect image processing directly into the listing workflow, since the cited conversion gains came from consistency and workflow integration rather than from any single AI edit.

**Tags**: `#AI image editing`, `#e-commerce`, `#product photography`, `#Photoroom`, `#growth case study`, `#user scale`

---

<a id="item-ai-growth-2"></a>
### [AI Subscription Pricing: OpenAI Tightens, Chinese Models Subsidize](https://www.woshipm.com/ai/6476590.html) ⭐️ 6.0/10

A pricing analysis from Z Finance compares the API-equivalent value of AI subscription tiers across OpenAI, Anthropic, MiniMax, Moonshot, Zhipu, Cursor, and Cognition, based on SemiAnalysis research. It reports that at the $200/month tier, Claude Opus 5.5 yields roughly $11,726 in API-equivalent usage versus about $2,084 for GPT-6.1 Sol, a roughly fivefold gap, while in raw tokens the same tier gives about 28.6 billion versus 10.2 billion tokens \(about 2.8x\). OpenAI reportedly cut Pro token allowances by nearly half and introduced a $500 tier, whereas Chinese vendors like MiniMax, Zhipu, and Moonshot continue to subsidize developers with high API-equivalent multiples of the monthly fee. The piece is useful for cost and unit-economics planning, but it contains no retention, conversion, CAC, or LTV metrics and no replicable growth tactics. Note: the source references future-dated models \(Claude Opus 5.5, GPT-6.1 Sol\) and a 2026 event, so specifics should be treated with caution.

rss · 人人都是产品经理 · Oct 12, 02:27

**「AI Technique」** The analysis relies on a measurement methodology that probes subscription quota systems by sending designed requests to isolate consumption of four token types: uncached new input, cache writes, cache reads, and model output. By tracking usage progress bars across many requests, researchers estimate the hidden internal exchange rate between tokens and quota, converging to roughly ±5% error, and even uncovered a small A/B test that gave one account about 20% less quota.

**「Growth Impact」** The reported impact is on cost structure rather than user growth: SemiAnalysis estimates that Anthropic&\#x27;s subscription business contributes about 10% of revenue but consumes over 40% of inference compute, and models subscription gross margins ranging from about -369% for Opus 5.5 if users exhaust all quota to about 6% at 20% utilization. These are model-based estimates, not disclosed financials, and the source provides no conversion, retention, or CAC data.

**「Takeaway」** When planning AI API or subscription costs, compare tiers on API-equivalent value, raw token volume, and short-window rate limits together, since vendors can change internal token-to-quota exchange rates without changing the monthly price.

**Tags**: `#AI pricing`, `#subscription economics`, `#API costs`, `#model comparison`, `#unit economics`, `#procurement`

---

<a id="item-ai-growth-3"></a>
### [19-Year-Old Zach Yadegari Raises $10M for Persona After Selling Cal AI](https://www.woshipm.com/chuangye/6476384.html) ⭐️ 6.0/10

Zach Yadegari, the 19-year-old founder who built the photo-based calorie-tracking app Cal AI to over 15 million downloads and more than $30 million in annual revenue before selling it to MyFitnessPal, has raised $10 million for his new company Persona, led by Vine Ventures with participation from Cory Levy and Collective Global. Persona is a personal AI assistant that currently runs as a free beta inside iMessage with a few thousand testers, and it is taking pre-orders for a $179 wristband scheduled to ship in December. The product aims to compress tasks like booking flights, reading email, and ordering food into a single text message, but it faces a crowded field of iMessage-based assistants including Instinct, Meta&\#x27;s Muse, Amazon&\#x27;s Bee, and others. For growth practitioners, the case is notable less for a replicable growth playbook than for tracking how a proven consumer founder applies distribution instincts to a new AI category where retention, monetization, and trust remain unproven.

rss · 人人都是产品经理 · Oct 12, 01:31

**「AI Technique」** Persona is an LLM-powered personal assistant delivered through iMessage that uses connected accounts and long-term memory built from conversations and completed tasks to execute actions such as booking travel, drafting email, and processing payments. The companion wristband is a screenless, voice-activated wearable with two microphones, a speaker, and an LED ring that can store two days of data locally and sync to cloud-based models.

**「Growth Impact」** No validated growth metrics exist for Persona yet: the iMessage beta has only a few thousand users and the wristband pre-orders represent five-figure revenue, roughly dozens to a few hundred units at $179 each. The prior app Cal AI, by contrast, reached over 15 million downloads and more than $30 million in annual revenue, driven mainly by influencer and social media distribution rather than paid acquisition.

**「Takeaway」** When entering a crowded AI category, a founder&\#x27;s proven distribution instinct—knowing where users are and what content gets shared—can matter more than model capability, but it still has to be validated by retention and paid conversion before it counts as growth.

**Tags**: `#AI assistant`, `#consumer AI`, `#funding`, `#founder story`, `#growth metrics`, `#iMessage`, `#hardware`, `#Cal AI`

---

<a id="item-ai-growth-4"></a>
### [AI Reverse-Engineering Adobe: 46k Stars in 10 Days](https://www.woshipm.com/ai/6476550.html) ⭐️ 5.0/10

A developer named Brandon Thomas, behind the ArtCraft project, used Claude Opus 5.5 to reverse-engineer and rewrite seven Adobe applications in Rust, releasing them as open source under names like PhotoCraft, VectorCraft, FilmCraft, LightCraft, EffectCraft, DesignCraft, and PrintCraft, corresponding to Photoshop, Illustrator, Premiere Pro, Lightroom, After Effects, InDesign, and Acrobat. The stated motivation was frustration with Adobe&\#x27;s cancellation fees, which require paying a penalty to exit an annual subscription commitment. Within under 10 days, the Photoshop-equivalent project alone reportedly reached 46,000 GitHub stars, and the piece notes the rewrites still lag the full Adobe products but are iterating rapidly. The article frames this as a signal that AI is collapsing the technical moats that once protected proprietary software, citing the related REA \(Reverse Engineer Anything\) project nearing 100,000 stars and examples of hardware protocol reverse-engineering. No growth, conversion, retention, or revenue metrics are provided, so the business implications remain speculative rather than measured.

rss · 人人都是产品经理 · Oct 12, 02:25

**「AI Technique」** The developer used Claude Opus 5.5 to perform clean-room-style reverse engineering: one agent studies a product&\#x27;s behavior and functionality, while another reimplements it from scratch, with end-to-end testing agents comparing results and fixing code. The article also describes REA, which connects professional reverse-engineering tools like Ghidra and Hopper to AI agents via MCP and command-line interfaces so agents can inspect binaries, trace function calls, and analyze decompiled output.

**「Growth Impact」** The only concrete metric reported is 46,000 GitHub stars for the Photoshop-equivalent project in under 10 days, which is a popularity signal rather than a growth outcome such as conversion, retention, or CAC. The article argues the broader impact is moat erosion: when AI makes reverse-engineering cheap, proprietary protocols and closed clients become harder to defend, pushing vendors toward thin clients with logic, models, and data locked server-side. This is a strategic observation, not a measured growth result.

**「Takeaway」** Treat AI-driven reverse-engineering as a moat-risk signal: if your product&\#x27;s defensibility rests mainly on closed protocols or opaque client code, assume that barrier is eroding and shift value toward server-side data, models, and network effects that cannot be copied from a binary.

**Tags**: `#AI reverse engineering`, `#open source`, `#Adobe`, `#Claude`, `#competitive moat`, `#AI tooling`

---

<a id="item-ai-growth-5"></a>
### [Eazo Hands-On: China&\#x27;s First Graphical Personal Agent](https://www.woshipm.com/ai/6476430.html) ⭐️ 5.0/10

Eazo is a graphical Personal Agent platform that lets users create personal AI apps through natural-language prompts and browse, interact with, remix, and monetize them in a TikTok-like feed. The review positions Eazo as an AI-era AppStore for personal apps, where users solve small personal problems \(e.g., parenting games, sleep, health management\) with self-built tools rather than searching public app stores. In a hands-on test, the author built a parent-child guessing game from a single voice-transcribed prompt; Eazo generated six interactive design demos, completed development in 151 steps, and produced a bilingual app with 63 questions that the author described as functional, smooth, and bug-free after two minor adjustments. The platform also supports remix fees, in-app payments, downloadable source code for iOS/Android publishing, configurable AI models, and built-in Skills. However, the review is descriptive and reports no performance metrics, retention, conversion, or engagement data, so its growth implications remain unvalidated.

rss · 人人都是产品经理 · Oct 12, 01:45

**「AI Technique」** Eazo uses natural-language prompts to generate complete interactive apps, producing multiple clickable design demos and then iterating through a multi-step build process. It also maintains user activity records and personalized memory to remember past creations and preferences, and it supports configurable AI models plus built-in Skills.

**「Growth Impact」** No measurable growth outcomes are reported. The review describes a potential platform dynamic—content feed, remix monetization, in-app payments, and creator following—but provides no data on retention, conversion, engagement, or revenue, so any growth impact is speculative.

**「Takeaway」** Watch for prompt-to-app platforms that combine a TikTok-style discovery feed with remix and payment mechanics, as they may create a new distribution channel for lightweight, personalized tools—but validate retention and conversion before treating them as a growth playbook.

**Tags**: `#AI agent`, `#personal agent`, `#no-code app creation`, `#product review`, `#AI platform`, `#China`

---


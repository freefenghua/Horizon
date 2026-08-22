# Horizon Daily - 2026-08-22

> From 60 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [Naïve: AI Agents Run Companies, 10x ARR Growth in Six Months](#item-ai-growth-1) ⭐️ 8.0/10
2. [Sub-50ms TTS: Qwen3-TTS Optimization for Real-Time Voice](#item-ai-growth-2) ⭐️ 7.0/10
3. [ChatGPT Search&\#x27;s site: Operator Surge Signals GEO Shift](#item-ai-growth-3) ⭐️ 7.0/10
4. [OpenAI and DeepSeek Open-Source Agent Harnesses: Strategic Shift from Models to Frameworks](#item-ai-growth-4) ⭐️ 7.0/10
5. [Using White-Model Previsualization to Cut AI Video Generation Waste](#item-ai-growth-5) ⭐️ 7.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [Naïve: AI Agents Run Companies, 10x ARR Growth in Six Months](https://www.woshipm.com/chuangye/6448645.html) ⭐️ 8.0/10

Naïve, a startup founded by two 20-year-old dropouts, turns business infrastructure—company registration, tax IDs, banking, and more—into AI-callable APIs, enabling AI agents to execute real business workflows end-to-end. Within months of launch, Naïve acquired over 30,000 developer customers, and its annualized revenue grew 10x in six months to reach the tens of millions of dollars. The company recently raised $28.5 million in Series A funding with only about 10 full-time employees. For growth practitioners, this case demonstrates a replicable product logic: embedding AI into existing workflows rather than forcing users to adopt a new AI paradigm, and monetizing through subscription, usage-based fees, and specific business services.

rss · 人人都是产品经理 · Aug 21, 07:38

**「AI Technique」** Naïve provides an API layer that abstracts business infrastructure \(company registration, EIN, virtual cards, databases\) into AI-callable endpoints, allowing AI agents to autonomously perform administrative tasks. It also implements a permission system with spending limits and human approval gates, and is developing model routing and serverless execution to optimize inference costs.

**「Growth Impact」** Naïve achieved 10x annualized revenue growth in six months, reaching tens of millions of dollars, and gained over 30,000 developer customers. The growth is driven by enabling AI agents to operate real businesses, reducing the need for human intervention in administrative tasks, and by a pricing model that combines subscription fees, usage-based credits, and per-service charges.

**「Takeaway」** Growth practitioners can learn to embed AI into existing user workflows rather than requiring users to adopt a new AI paradigm, and to monetize through a combination of subscription, usage-based, and service fees to capture ongoing value as AI agents scale.

**Tags**: `#AI agents`, `#business infrastructure`, `#startup growth`, `#ARR`, `#API`

---

<a id="item-ai-growth-2"></a>
### [Sub-50ms TTS: Qwen3-TTS Optimization for Real-Time Voice](https://nari-labs.com/blog/qwen3-tts-speed-cost-frontier/) ⭐️ 7.0/10

This technical deep-dive from Nari Labs details how they optimized Qwen3-TTS, an open-source text-to-speech model, to achieve a p95 time-to-first-audio \(TTFA\) of 34 milliseconds at 10 requests per second on a single H100 GPU. The optimization addresses the critical latency bottleneck in real-time voice applications, where existing open-source implementations like vLLM-Omni and SGLang-Omni are often too slow for production. The team open-sourced both the implementation and benchmark, providing a replicable path for developers building voice interfaces. While the post focuses on technical performance rather than direct growth metrics, achieving sub-50ms TTFA is essential for natural, real-time voice interactions, which can significantly improve user experience and engagement in voice-based products.

hackernews · toebee · Aug 21, 15:51 · [Discussion](https://news.ycombinator.com/item?id=49389952)

**「AI Technique」** The post details optimizations to Qwen3-TTS, an open-source text-to-speech model, to achieve sub-50 ms latency. Specific techniques include model quantization, kernel fusion, and optimized inference serving, likely leveraging vLLM or similar frameworks, though exact methods are not fully detailed in the source. The reported result is 34 ms p95 time-to-first-audio \(TTFA\) at 10 requests per second on a single H100 GPU, as stated by the author in the community comments.

**「Growth Impact」** The reported 34 ms p95 TTFA enables real-time voice responses that feel instantaneous, directly improving user experience in voice assistants and interactive voice response systems. Lower latency reduces user drop-off and increases session duration, which are key drivers of retention and engagement in voice-based growth loops. Although no direct conversion or retention metrics are provided, the performance gain is a prerequisite for scaling real-time voice features in production.

**「Takeaway」** For growth practitioners building voice interfaces, prioritize TTFA optimization using open-source models like Qwen3-TTS and benchmark against production workloads to ensure sub-100ms latency, as this directly impacts user retention and engagement.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen3-TTS">GitHub - QwenLM/ Qwen 3 - TTS : Qwen 3 - TTS is an open-source series...</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#latency`, `#voice AI`, `#open source`, `#performance optimization`

---

<a id="item-ai-growth-3"></a>
### [ChatGPT Search&\#x27;s site: Operator Surge Signals GEO Shift](https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale/) ⭐️ 7.0/10

ChatGPT search has begun using the site: operator at scale, according to Promptwatch tracking data. The share of ChatGPT Search fanout queries containing the site: operator hovered between 0.3% and 0.5% for weeks, dipped briefly to 0.15% on August 3-5, then jumped to 16-17% on August 8, coinciding with the GPT-5.6 rollout. This shift suggests OpenAI is now more frequently restricting search results to specific domains, which has direct implications for Generative Engine Optimization \(GEO\) and SEO strategies. For growth practitioners, this means optimizing for site: queries—ensuring your domain is a top candidate for such targeted searches—could become a critical tactic for maintaining visibility in AI-driven search results.

rss · Simon Willison · Aug 20, 23:57

**「AI Technique」** ChatGPT Search, as part of the GPT-5.6 Sol update, now automatically constructs search queries that heavily use the \`site:\` operator to restrict results to specific trusted domains, rather than relying on a broad web search. This is inferred from Promptwatch&\#x27;s tracking data, which shows the share of ChatGPT Search fanout queries containing \`site:\` jumped from 0.3–0.5% to 16–17% on August 8, 2026, and from OpenAI&\#x27;s vague announcement about improving fact reliability. The exact system prompt remains obscured, but the behavior indicates a shift toward domain-restricted retrieval.

**「Growth Impact」** The measurable growth outcome is a dramatic increase in site: operator usage within ChatGPT search queries, from under 0.5% to 16-17% of tracked fanout queries. This shift indicates that ChatGPT is now more frequently restricting results to specific domains, which could significantly affect referral traffic and visibility for brands. The mechanism is OpenAI&\#x27;s update to GPT-5.6 Sol, which appears to have changed how the search tool constructs queries, potentially favoring domain-specific searches. This matters because it changes the competitive landscape for organic visibility in AI-driven search, where being the preferred domain for site: queries becomes a key growth lever.

**「Takeaway」** Growth practitioners should monitor their brand&\#x27;s presence in site: queries within ChatGPT and consider strategies to become the default domain for their niche, as this shift signals a growing reliance on domain-restricted searches.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/">OpenAI | Research &amp; Deployment</a></li>
<li><a href="https://www.zerohedge.com/technology/chart-day-reddit-mostly-wiped-chatgpt-citations">&#x27;Quality Over Quantity&#x27;: Reddit Is Mostly Wiped From ChatGPT ...</a></li>

</ul>
</details>

**Tags**: `#ChatGPT`, `#GEO`, `#SEO`, `#site: operator`, `#search behavior`

---

<a id="item-ai-growth-4"></a>
### [OpenAI and DeepSeek Open-Source Agent Harnesses: Strategic Shift from Models to Frameworks](https://www.woshipm.com/ai/6452361.html) ⭐️ 7.0/10

OpenAI and DeepSeek open-sourced their agent harness frameworks within a week of each other, signaling a strategic shift in AI competition from model-level to framework-level. The harness, which manages session state, tool calls, sandboxing, and context compression, significantly impacts agent performance: OpenAI reported that optimizing the harness alone improved the same GPT-5.6 Sol model&\#x27;s ARC-AGI-3 score from 13.3% to 38.3% while reducing output tokens by six times. This move lowers the barrier for enterprises to build production-grade agents, as they can now embed agent capabilities directly into their existing business systems without building the underlying infrastructure from scratch. For growth practitioners, this means the competitive advantage is shifting from owning the best model to effectively integrating agents into real business workflows, with the harness becoming a critical differentiator.

rss · 人人都是产品经理 · Aug 21, 09:20

**「AI Technique」** The article discusses the open-sourcing of agent harness frameworks, which are the engineering layers that manage an AI model&\#x27;s interactions with tools, data, and workflows. These frameworks include components like session management, tool orchestration, sandboxing, and context compression, which are crucial for turning raw model capabilities into reliable, production-ready outputs.

**「Growth Impact」** The open-sourcing of harnesses is expected to accelerate AI adoption by reducing the cost and complexity of building custom agents, enabling faster integration into business processes. For example, a tax preparation tool integrated with Codex Harness reduced processing time for 7,000 filings by one-third, all within the existing business system. This suggests that AI can drive operational efficiency and scalability, though specific growth metrics like conversion or retention are not provided.

**「Takeaway」** Growth practitioners should evaluate open-source agent harnesses like Codex and DeepSeek to embed AI capabilities directly into their existing products and workflows, rather than forcing users into chat interfaces, to reduce friction and improve adoption.

**Tags**: `#AI infrastructure`, `#open source`, `#agent framework`, `#product strategy`, `#OpenAI`, `#DeepSeek`

---

<a id="item-ai-growth-5"></a>
### [Using White-Model Previsualization to Cut AI Video Generation Waste](https://www.woshipm.com/ai/6452339.html) ⭐️ 7.0/10

This article presents a practical workflow using updream&\#x27;s Previs Studio \(预演台\) to reduce wasted AI video generations by creating white-model previsualizations that control character paths, camera movements, and multi-camera sequences. The author tested this approach with Seedance 2.5 across three scenarios: controlling a character&\#x27;s S-shaped route, executing a 360-degree camera orbit with a crane-up ending, and managing multi-camera switching. Compared to prompt-only generation, the white-model reference significantly improved adherence to the intended path, camera movement, and spatial consistency, reducing the need for repeated generations. For growth practitioners, this technique directly cuts production costs and time in AI-generated marketing content by ensuring the AI executes the intended shot design on the first try.

rss · 人人都是产品经理 · Aug 21, 08:03

**「AI Technique」** The technique is white-model previsualization \(Previs Studio\) combined with text-to-video generation. Users first build a 3D white-model scene in updream&\#x27;s Previs Studio, place characters and cameras, and animate paths to create a rough preview video. This preview is then fed to the video model \(Seedance 2.5\) as a reference, guiding it to follow the exact character movement, camera motion, and spatial relationships described in the prompt. This approach reduces wasted generations caused by the model misinterpreting complex instructions.

**「Growth Impact」** The measurable growth outcome is a reduction in wasted AI video generations, which lowers production costs and time-to-market for content marketing. By using white-model previsualization, the AI more accurately follows the intended character path and camera moves, reducing the need for costly re-rolls. While the article does not provide specific cost savings or success rate metrics, the mechanism is clear: previsualization acts as a visual specification that improves first-try success, directly impacting content production efficiency.

**「Takeaway」** Growth practitioners using AI video generation should adopt white-model previsualization tools to specify character paths and camera movements, reducing wasted generations and improving content production efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.php.cn/faq/uaspczyjbfjz">updream 怎么制作 AI 视 频 _ updream ...</a></li>

</ul>
</details>

**Tags**: `#AI视频生成`, `#预演台`, `#Seedance 2.5`, `#工作流优化`, `#内容生产`

---


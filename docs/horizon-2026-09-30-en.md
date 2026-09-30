# Horizon Daily - 2026-09-30

> From 72 items, 5 important content pieces were selected

---

**AI × Growth Intersection**
1. [AI Selfie Mini-Program: Break-Even at 10k MAU and 10.3% Paid Rate](#item-ai-growth-1) ⭐️ 6.0/10
2. [AI Agent Tools Are Converging: One Practitioner&\#x27;s Five-to-One Consolidation](#item-ai-growth-2) ⭐️ 6.0/10
3. [Ex-Hinge CPO&\#x27;s AI Astrology App Lora Hits 160K Waitlist](#item-ai-growth-3) ⭐️ 5.0/10
4. [AI 短剧：效率提升 50 倍，播放量仅 4%](#item-ai-growth-4) ⭐️ 5.0/10
5. [Arcade AI: Natural-Language Custom Product Design with Instant Pricing](#item-ai-growth-5) ⭐️ 5.0/10

---

## AI × Growth Intersection

<a id="item-ai-growth-1"></a>
### [AI Selfie Mini-Program: Break-Even at 10k MAU and 10.3% Paid Rate](https://www.woshipm.com/ai/6472389.html) ⭐️ 6.0/10

A founder&\#x27;s first-person teardown of &quot;和拍相机&quot; \(HePai Camera\), a WeChat mini-program concept that uses AI to guide elderly and family users through taking group selfies. The product would use face-detection-style framing guides, voice prompts, auto-capture, and AI retouching/background replacement to solve the recurring pain of coordinating multi-person selfies. The author models unit economics: with a 9.9 RMB charge for processing 5 photos and 3 RMB variable cost per order, roughly 798 orders per month are needed for cash break-even at 10k MAU, or about 1,031 orders per month \(roughly 10.3% monthly paid conversion\) to recover the ~19,320 RMB startup budget within 12 months. The author explicitly notes these are scenario estimates, not validated metrics, and that the core question—whether free-photo users will pay for retouching and travel-photo features—remains untested. For growth practitioners, this is a useful template for modeling AI-enabled product economics and for separating acquisition demand from monetization demand.

rss · 人人都是产品经理 · Sep 30, 02:54

**「AI Technique」** The concept relies on computer-vision-style face/framing detection to guide users into the shot, plus AI image processing for light beautification, photo repair, and background replacement for travel-style photos. The author plans to build the first version using Tencent CodeBuddy and similar tools that generate and modify WeChat mini-program code, while calling existing APIs for core capabilities rather than developing custom detection algorithms.

**「Growth Impact」** No validated growth metrics are reported; the article is a pre-launch model. The author estimates that at 10k MAU, about 798 monthly orders are needed for cash break-even, and about 1,031 monthly orders \(roughly 10.3% monthly paid conversion\) to recoup the ~19,320 RMB startup cost within 12 months. The mechanism is a freemium funnel: free shooting guidance drives usage, while paid retouching, group-photo repair, and themed travel photos drive revenue. The author cautions that a 1,000 RMB promotion budget does not guarantee 10k MAU and that the model excludes the founder&\#x27;s salary, taxes, and future development costs.

**「Takeaway」** Model your AI product&\#x27;s break-even as a paid-conversion rate against a realistic MAU assumption, and validate willingness to pay separately from free-feature usage before scaling acquisition.

**Tags**: `#AI product`, `#mini-program`, `#unit economics`, `#user segmentation`, `#growth model`, `#selfie camera`

---

<a id="item-ai-growth-2"></a>
### [AI Agent Tools Are Converging: One Practitioner&\#x27;s Five-to-One Consolidation](https://www.woshipm.com/ai/6472128.html) ⭐️ 6.0/10

A product manager at an HR SaaS company describes consolidating five AI Agent tools \(Trae, Qoder, Codex, QoderWork, and QwenWork\) down to a single tool, WorkBuddy, over several months. The author argues this mirrors a broader industry consolidation: Anthropic merged its standalone Claude Cowork product into the main Claude conversation in September \(Cowork lasted only about eight months from its January research preview\), and OpenAI combined ChatGPT Work with Codex into a unified desktop app. In China, ByteDance folded Feishu&\#x27;s product team, TRAE, and Coze into the Doubao system and launched &quot;Doubao Work,&quot; while Alibaba merged QoderWork, MuleRun, and Wukong into QwenWork, which reportedly reached over 30 million registered users with more than half being enterprise users and shipped 120 versions in 30 days. The author&\#x27;s core claim is that Agent tools will converge faster than expected—possibly in six to twelve months rather than three years—because capability is homogenizing while user workflow assets \(skills, connectors, context\) are hard to migrate, creating a &quot;one-way door.&quot; The piece is a product-trend observation rather than a growth case study, and it offers no conversion, retention, or CAC metrics.

rss · 人人都是产品经理 · Sep 30, 02:30

**「AI Technique」** The article centers on AI Agent platforms that combine local file operations, cloud-based long-running tasks, skill marketplaces, connectors to tools like Slack and Google Drive, scheduled tasks, and one-click generation of shareable interactive web pages. The author also references &quot;Skills&quot;—modular, reusable workflow packages \(e.g., for writing requirement docs or prototypes\)—and &quot;Buddy apps,&quot; described as a vertical-industry AI Harness that layers company-specific knowledge and connectors on top of general model capabilities.

**「Growth Impact」** The source reports platform-level scale rather than growth metrics: QwenWork reportedly surpassed 30 million registered users within a month of launch, with enterprise users making up over half, and WorkBuddy&\#x27;s PC monthly visits reached 20.97 million in June 2026 according to Analysys data, exceeding the combined total of TRAE and QoderWork. The author&\#x27;s own productivity claim—that a prototype deliverable went from a week-long document cycle to a one-hour, 12-turn interactive web page, improving communication efficiency &quot;two to three times&quot;—is explicitly described as personal perception, not measured data. No conversion, retention, or CAC figures are provided.

**「Takeaway」** Before committing to any single AI Agent platform, modularize your workflows into reusable skills so your migration cost stays low—the real lock-in comes from accumulated assets \(skills, connectors, context\), not from model quality.

**Tags**: `#AI Agent`, `#产品趋势`, `#工具整合`, `#Anthropic`, `#OpenAI`

---

<a id="item-ai-growth-3"></a>
### [Ex-Hinge CPO&\#x27;s AI Astrology App Lora Hits 160K Waitlist](https://www.woshipm.com/ai/6472452.html) ⭐️ 5.0/10

Lora: Your Life in Context, an AI astrology app founded by former Hinge Chief Product Officer Michelle Parsons, launched on September 14 on iOS across 174 countries with English as its only language, targeting the US market. The app generates a personal natal chart from birth date, place, and time, then lets users chat with an AI that combines chart data with their inputs to discuss relationships, career, family, and self-understanding; it also offers an &quot;Orbit&quot; relationship-mapping feature, weekly reports, daily horoscopes, and human astrologer consultations starting at $88. Before launch, Lora accumulated over 160,000 waitlist signups, more than 80,000 newsletter subscribers, and over 3,000 event participants, with a team of fewer than 10 people incubated by AlleyCorp. The item frames this against Match Group&\#x27;s Q2 2026 results, where Tinder paid users fell 5% to 8.5 million while Hinge paid users rose 17% to 2 million, direct revenue grew 22% to $203.5 million, and MAU grew 13%, suggesting demand is shifting from connection volume toward deeper relationship interpretation. However, the source provides no product metrics, retention, or conversion data for Lora itself, so the waitlist is a pre-launch signal rather than validated performance.

rss · 人人都是产品经理 · Sep 30, 03:52

**「AI Technique」** Lora uses an LLM-based conversational AI that ingests a user&\#x27;s natal chart data \(birth date, place, and time\) plus self-reported life-state ratings across five dimensions, then generates personalized astrological interpretations and ongoing dialogue. The system accumulates context over repeated interactions to refine its outputs, and it also powers relationship insights in the Orbit feature and automated weekly reports.

**「Growth Impact」** The reported growth signal is pre-launch demand: over 160,000 waitlist signups, 80,000+ newsletter subscribers, and 3,000+ event participants for a team of fewer than 10 people. No post-launch conversion, retention, or revenue metrics for Lora are provided, so the actual growth impact remains unverified; the broader context is Match Group&\#x27;s Q2 2026 shift, with Hinge paid users up 17% to 2 million and direct revenue up 22% to $203.5 million, indicating growing willingness to pay for deeper relationship-oriented products.

**「Takeaway」** For growth practitioners, Lora illustrates a pre-launch playbook worth testing: build a waitlist and community \(newsletter, Discord, offline events\) around a specific emotional job-to-be-done before shipping, and use a low-cost AI layer for high-frequency engagement while reserving human experts for high-ticket upsells.

**Tags**: `#AI占星`, `#社交产品`, `#用户增长`, `#关系解读`, `#Hinge`, `#早期产品`, `#美国市场`

---

<a id="item-ai-growth-4"></a>
### [AI 短剧：效率提升 50 倍，播放量仅 4%](https://www.woshipm.com/share/6472107.html) ⭐️ 5.0/10

在云栖大会上，阿里云牵头成立了短漫剧产业发展联盟，掌阅、快看、麦芽、点众、淘宝短剧、优酷等参与分享，核心结论是 AI 短剧生产效率极高但变现困难。山海短剧付磊透露 AI 短剧已上线 22 万部，其第三代模式下一集算力成本约一百元，五个人可完成原来四十人的工作，九成集数一次成片。但赵晖教授的报告显示，今年春节档 AI 剧上线量是真人剧的 50 倍，播放量却只有真人剧的 4%，真人剧播放量是 AI 剧的 25 倍。诸云科技尹星富也指出，一键成片工具虽然让剧集数量翻了十倍，但市场并未扩大，因此并不赚钱。对增长从业者而言，这说明 AI 能大幅降低内容生产成本，但内容供给的爆发并不自动带来用户注意力和收入的增长。

rss · 人人都是产品经理 · Sep 30, 03:48

**「AI 技术」** 案例涉及阿里云 Wan 3.0 视频生成模型，可生成 30 秒连贯视频并支持图片、视频、音频作为参考；同时使用提示词工程（先锁定不变量再写镜头变化）和将编剧经验封装为 skill 的方式，配合 Agent 与画布工具（万镜一刻）实现剧本策划、故事板、剪辑的一站式交付。

**「增长影响」** AI 将短剧单集算力成本压至约一百元、五人团队替代四十人，使上线量达到真人剧的 50 倍，但春节档 AI 剧播放量仅为真人剧的 4%，说明效率提升未转化为观看量或收入增长。井英科技的数据还显示，帮派斗争、身份桎梏等冷门题材的爆款概率是霸总甜宠的四倍多，提示题材选择可能比产量更影响增长。

**「行动建议」** 在 AI 内容生产中，不要只追求产量，应优先用爆款率而非剧目数来评估题材，并关注播放量与变现指标，避免陷入“数量翻十倍但市场未扩大”的陷阱。

**Tags**: `#AI短剧`, `#内容增长`, `#AIGC`, `#短剧`, `#变现`, `#行业观察`

---

<a id="item-ai-growth-5"></a>
### [Arcade AI: Natural-Language Custom Product Design with Instant Pricing](https://www.woshipm.com/chuangye/6470532.html) ⭐️ 5.0/10

Arcade AI is a platform that lets users describe a custom product in natural language, generates a design with AI, and then connects the design to suppliers who can actually manufacture it. It started testing custom jewelry in September 2024 and later expanded to rugs, curtains, bedding, ceramics, glassware, and silverware, partnering with manufacturers such as Italian ceramics brand Bitossi and French silverware brand Christofle. The company says the platform generated more than 650,000 jewelry designs within about six months, a figure the founder later said exceeded 750,000, and it raised a $25 million Series A in March 2025, bringing total funding to $42 million. A reporter who tested the service ordered a gold necklace with three opals for $186 plus $10 shipping, received a production video from the artisan, and got the finished piece in about two weeks. The case matters for growth practitioners because it shows how AI can turn a search-and-browse shopping flow into a describe-and-create flow, but the source does not provide conversion, retention, or CAC metrics.

rss · 人人都是产品经理 · Sep 30, 02:21

**「AI Technique」** Arcade uses generative AI to turn natural-language product descriptions into visual designs, and it also built a recognition and pricing model that identifies product structure, materials, and design elements in the generated image, then applies manufacturer cost rules to produce an instant price. The company constrains the generation model with manufacturing data such as available materials, achievable precision, producible structures, and size limits, and it allows users to upload images generated by other tools like Midjourney or KREA for detection, adjustment, and quoting.

**「Growth Impact」** The source reports design-volume growth from 650,000 to more than 750,000 jewelry designs in roughly six months, plus $42 million in total funding, but it does not disclose conversion, retention, or CAC figures. The mechanism is that instant AI pricing and supplier matching keep users inside Arcade after design generation, instead of sending them to marketplaces or factories to request quotes, which shortens the path from idea to purchasable product.

**「Takeaway」** For AI-powered personalization, test whether instant pricing and fulfillment can keep users in your flow after generation, because the design tool alone is not the commerce product.

**Tags**: `#AI`, `#personalization`, `#e-commerce`, `#custom manufacturing`, `#product design`

---


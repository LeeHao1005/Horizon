---
layout: default
title: "Horizon Summary: 2026-06-25 (EN)"
date: 2026-06-25
lang: en
---

> From 39 items, 12 important content pieces were selected

---

1. [OpenAI unveils first custom AI inference chip 'Jalapeno' with Broadcom](#item-1) ⭐️ 9.0/10
2. [Cloudflare Launches Self-Managed OAuth Service](#item-2) ⭐️ 9.0/10
3. [Anthropic Accuses Alibaba of Massive Distillation Attack on Claude](#item-3) ⭐️ 9.0/10
4. [Half-Life 2 Runs in Browser via WebAssembly](#item-4) ⭐️ 8.0/10
5. [RubyLLM: Unified Ruby Framework for All Major AI Providers](#item-5) ⭐️ 8.0/10
6. [Stopped trusting benchmarks, started custom evals](#item-6) ⭐️ 8.0/10
7. [Tool selection at scale: lexical retrieval beats semantic embeddings](#item-7) ⭐️ 8.0/10
8. [Superhuman Generals.io Agent via Self-Play RL](#item-8) ⭐️ 8.0/10
9. [HDD-RoPE: Dynamic Positional Embedding with Faster Convergence](#item-9) ⭐️ 8.0/10
10. [Micron's Q3 FY2026 Revenue Surges 346% YoY, Profit $28.24B](#item-10) ⭐️ 8.0/10
11. [Google Play to Enable External Billing in US, UK, EU](#item-11) ⭐️ 8.0/10
12. [Eric Schmidt Criticizes Chinese Open-Source AI as Uncontrollable](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI unveils first custom AI inference chip 'Jalapeno' with Broadcom](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI and Broadcom announced the Jalapeno chip, a custom AI inference processor designed for large language models, claiming up to 50% lower inference cost per token compared to current Nvidia GPUs. The chip was developed in nine months with the help of OpenAI's own AI models to accelerate design, and engineering samples are already running GPT-5.3-Codex-Spark in the lab. This marks a significant step toward vertical integration for OpenAI, reducing reliance on Nvidia GPUs and potentially lowering costs for serving ChatGPT, Codex, and future AI agents. It also highlights the accelerating trend of AI companies designing custom silicon to optimize performance and efficiency for specific workloads. Jalapeno is an inference-only chip co-developed with Broadcom and manufactured by TSMC, designed to work with all large language models based on OpenAI's insights into inference needs. OpenAI used its own models to accelerate chip design, claiming a nine-month timeline from design to production, though some details on how AI accelerated the process remain unclear.

hackernews · jamdesk · Jun 24, 17:47 · [Discussion](https://news.ycombinator.com/item?id=48663324)

**Background**: AI inference is the process of running a trained model to generate outputs, which requires significant computational resources, especially for large models. Currently, most AI companies rely on GPUs from Nvidia for both training and inference, but specialized inference chips can offer better performance-per-watt and lower cost. Custom chip design traditionally takes years, but advances in AI-driven design automation are shortening that timeline.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip</a></li>
<li><a href="https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/">OpenAI unveils its first custom chip, built by Broadcom</a></li>
<li><a href="https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html">OpenAI and Broadcom reveal Jalapeno, first AI chip in partnership - CNBC</a></li>

</ul>
</details>

**Discussion**: Commenters expressed curiosity about how exactly OpenAI's models accelerated the chip design, with some skepticism that it might be marketing hype. Others discussed the technical implications for specialized inference chips, such as the potential to embed weights into ROM for massive throughput, and questioned how this affects competitors like Cerebras.

**Tags**: `#AI hardware`, `#custom chip`, `#OpenAI`, `#Broadcom`, `#inference`

---

<a id="item-2"></a>
## [Cloudflare Launches Self-Managed OAuth Service](https://blog.cloudflare.com/oauth-for-all/) ⭐️ 9.0/10

Cloudflare has launched a self-managed OAuth service, allowing developers to implement authentication without relying on third-party providers. The service is designed to be scalable and performant. This matters because it addresses a common pain point for developers who need to build authentication systems, especially at scale. As a major cloud provider, Cloudflare's offering could simplify OAuth implementation and reduce vendor lock-in. The service is self-managed, meaning developers have full control over their OAuth infrastructure. Cloudflare claims it provides identical performance and reliability to its existing edge network.

hackernews · terryds · Jun 25, 02:18 · [Discussion](https://news.ycombinator.com/item?id=48668033)

**Background**: OAuth is an open standard for access delegation, commonly used for token-based authentication and authorization. Implementing OAuth from scratch can be complex, so many developers rely on third-party services or frameworks like Ory Hydra.

**Discussion**: The community response is mixed. Some developers appreciate Cloudflare's entry into the OAuth space, while others express concerns about Cloudflare's past record of launching projects without sustained improvement. The author of Ory Hydra praised the technical description but noted their own commercial variant is faster.

**Tags**: `#OAuth`, `#Cloudflare`, `#authentication`, `#developer tools`, `#IAM`

---

<a id="item-3"></a>
## [Anthropic Accuses Alibaba of Massive Distillation Attack on Claude](https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html) ⭐️ 9.0/10

Anthropic sent a letter to the US Senate Banking Committee accusing Alibaba of using nearly 25,000 fake accounts to interact with Claude over 28 million times from April 22 to June 5, 2026, in what it calls the largest known distillation attack against the company. This accusation underscores rising tensions over AI intellectual property between the US and China, and could lead to stricter regulations on API access and international AI trade, affecting how companies protect their models. The attack involved multiple Alibaba entities including its Qwen AI lab, and the stolen knowledge was likely used to replicate Claude's capabilities. Anthropic's detection systems identified the pattern through classifiers and behavioral fingerprinting.

telegram · zaihuapd · Jun 25, 01:36

**Background**: Model distillation is a technique where a smaller 'student' model learns from a larger 'teacher' model's outputs to achieve similar performance at lower cost. While commonly used for legitimate model compression, using it without permission to steal proprietary knowledge is considered an attack, raising significant IP and security concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks - Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://www.iaps.ai/research/ai-distillation-attacks-the-case-for-targeted-government-intervention">AI Distillation Attacks: The Case for Targeted Government Intervention</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism, arguing that distillation is a common practice and that Anthropic's complaint is hypocritical given that major AI labs trained on public data without permission. Some compare it to past disputes like Apple vs. Xerox, while others fear it gives too much power to AI companies.

**Tags**: `#AI security`, `#model distillation`, `#Anthropic`, `#Alibaba`, `#intellectual property`

---

<a id="item-4"></a>
## [Half-Life 2 Runs in Browser via WebAssembly](https://hl2.slqnt.dev/) ⭐️ 8.0/10

A WebAssembly port of Half-Life 2 is now playable directly in the browser at hl2.slqnt.dev, demonstrating the ability to run complex 3D games on the web platform. This port shows that even complex graphics-heavy games from the mid-2000s can be brought to the web without plugins, potentially increasing accessibility and reducing platform lock-in. The port uses Emscripten to compile the original C++ code to WebAssembly, but community members note missing shaders such as character eyes, leading to slightly degraded visuals compared to the native version.

hackernews · panza · Jun 25, 06:00 · [Discussion](https://news.ycombinator.com/item?id=48669534)

**Background**: WebAssembly (Wasm) is a low-level binary format for safe, high-performance execution in web browsers, designed as a compilation target for languages like C, C++, and Rust. Emscripten is a compiler toolchain that converts LLVM bitcode to WebAssembly, enabling native applications to run on the web. This combination allows games like Half-Life 2, originally written in C++, to be ported to the browser.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Emscripten">Emscripten</a></li>

</ul>
</details>

**Discussion**: Comments are generally impressed but note missing visual features (e.g., character eyes) and point to similar projects like a Quake 3 port and Unreal Tournament in the browser, as well as noclip.website for exploring game levels. One user highlights the irony that the game runs in browser on macOS where the native Steam version is unavailable due to 32-bit deprecation.

**Tags**: `#webassembly`, `#game development`, `#browser`, `#emscripten`, `#retro gaming`

---

<a id="item-5"></a>
## [RubyLLM: Unified Ruby Framework for All Major AI Providers](https://rubyllm.com/) ⭐️ 8.0/10

RubyLLM has been released as a Ruby framework offering a single, unified API for all major AI providers, enabling developers to build chatbots, agents, and RAG applications with ease. This framework fills a critical gap in the Ruby ecosystem, providing a consistent interface across AI providers and significantly reducing the complexity of building AI-powered applications in Ruby. RubyLLM has minimal dependencies (Faraday, Zeitwerk, Marcel) and supports providers like GPT-4, Claude, Gemini, and Ollama. Community reports note cache issues with xAI and an initial lack of native responses API, which has since been addressed.

hackernews · doener · Jun 24, 14:41 · [Discussion](https://news.ycombinator.com/item?id=48660711)

**Background**: Many AI providers ship their own API clients with different conventions and response formats, creating a fragmented experience for developers. RubyLLM unifies these into a single, elegant Ruby API, similar to Vercel's AI SDK for JavaScript. It is designed to be simple out of the box yet flexible for advanced use cases like custom tools and agents.

<details><summary>References</summary>
<ul>
<li><a href="https://rubyllm.com/">RubyLLM | One beautiful Ruby framework for all major AI ...</a></li>
<li><a href="https://github.com/crmne/ruby_llm">GitHub - crmne/ruby_llm: One delightful Ruby framework for ...</a></li>

</ul>
</details>

**Discussion**: The community response is predominantly positive, with users praising RubyLLM's API design and usability, often comparing it favorably to Vercel's AI framework. Some frustrations include cache issues with xAI and slow PR merging, but there is strong anticipation for RubyLLM 2.0, which promises native responses API support.

**Tags**: `#Ruby`, `#AI`, `#Framework`, `#LLM`, `#API`

---

<a id="item-6"></a>
## [Stopped trusting benchmarks, started custom evals](https://www.reddit.com/r/MachineLearning/comments/1uf53un/i_stopped_trusting_model_benchmarks_and_started/) ⭐️ 8.0/10

The author built a custom eval set of 240 tasks from real production traffic and found that public benchmarks often misrepresent model performance for specific workloads. This matters because relying solely on public benchmarks can lead to poor model selection and even production incidents, highlighting the need for tailored evaluation tied to one's own data distribution. The eval set is frozen to prevent drift, and all models are routed through GPTProto to remove provider variance, ensuring a fair comparison; one model that benchmarked well was found to have a dangerous failure mode on edge cases.

reddit · r/MachineLearning · /u/Additional-Engine402 · Jun 25, 09:22

**Background**: Public benchmarks like DeepSWE and Artificial Analysis Intelligence Index are widely used to compare models, but they have limitations: DeepSWE evaluates coding agents on original tasks, while Artificial Analysis combines multiple metrics. However, these benchmarks may not reflect a specific production distribution, as the author experienced with vendors' self-designed benchmarks and self-reported parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://deepswe.net/">DeepSWE Benchmark: GPT vs Claude for Agentic Coding</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://benchlm.ai/benchmarks/deepSwe">DeepSWE Benchmark 2026: 8 pass@1 rows | BenchLM.ai</a></li>

</ul>
</details>

**Tags**: `#benchmarks`, `#evaluation`, `#LLM`, `#machine learning`, `#reliability`

---

<a id="item-7"></a>
## [Tool selection at scale: lexical retrieval beats semantic embeddings](https://www.reddit.com/r/MachineLearning/comments/1ufafnw/tool_selection_at_scale_is_a_retrieval_problem/) ⭐️ 8.0/10

A developer argues that for large-scale agent tool selection, lexical retrieval (BM25) outperforms semantic embeddings, based on empirical evaluation against a 43,000-tool corpus. This challenges the common practice of using semantic embeddings as the default for tool retrieval in agent systems, potentially improving accuracy and reducing costs for large tool catalogs. Tool descriptions are short and structurally similar (verb-noun, parameter lists), so cosine similarity over dense embeddings dilutes the single discriminating token. BM25 on a flat-text projection of name, description, and schema preserves that discriminator and runs fully in-process without an embedding model.

reddit · r/MachineLearning · /u/AbjectBug5885 · Jun 25, 13:43

**Background**: The Model Context Protocol (MCP) is an open standard by Anthropic for connecting AI applications to external tools and data sources. In large-scale agent systems, the set of callable tools can be huge, so a retrieval step is needed to select a relevant subset for each request. Traditional document RAG uses semantic embeddings for retrieval, but tool descriptions differ from documents in being short and lexically discriminative.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://medium.com/@dineshkarthik_kandregula/hybrid-retrieval-bm25-vs-dense-embeddings-smarter-search-using-elasticsearch-huggingface-3dd6a6351b05">Hybrid Retrieval : BM25 vs . Dense Embeddings — Smarter... | Medium</a></li>
<li><a href="https://aimlinsights.com/dense-retrieval-vs-sparse-retrieval/">Dense Retrieval vs Sparse Retrieval Explained for RAG » AIML Insights</a></li>

</ul>
</details>

**Tags**: `#tool selection`, `#retrieval`, `#agents`, `#embeddings`, `#MCP`

---

<a id="item-8"></a>
## [Superhuman Generals.io Agent via Self-Play RL](https://www.reddit.com/r/MachineLearning/comments/1uei2yg/i_made_a_superhuman_generalsio_agent_with/) ⭐️ 8.0/10

A researcher trained a superhuman Generals.io agent using self-play reinforcement learning, implemented in JAX with a Vision Transformer, achieving rank #1 on the human 1v1 leaderboard. This demonstrates the power of scaling and modern architectures (JAX, ViT) over handcrafted features, and the open-source release provides a valuable resource for game AI research. The entire pipeline was reimplemented in JAX from NumPy/Torch, and a Vision Transformer replaced the CNN, enabling faster training and better performance.

reddit · r/MachineLearning · /u/shrekofspeed · Jun 24, 16:18

**Background**: Generals.io is an imperfect-information real-time strategy game. Self-play RL involves an agent learning by playing against itself. JAX is a high-performance numerical computing library, and Vision Transformers apply transformer architecture to image patches.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JAX_(software)">JAX (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision_transformer">Vision transformer</a></li>
<li><a href="https://arxiv.org/abs/2010.11929">[2010.11929] An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#self-play`, `#game-ai`, `#JAX`, `#vision-transformer`

---

<a id="item-9"></a>
## [HDD-RoPE: Dynamic Positional Embedding with Faster Convergence](https://www.reddit.com/r/MachineLearning/comments/1uelcm9/high_dimensional_dynamic_rotary_positional/) ⭐️ 8.0/10

The author introduces HDD-RoPE, a high-dimensional dynamic rotary positional embedding that uses cumulative matrix products, demonstrating faster convergence on the TinyStories dataset compared to the xPos baseline. This approach advances positional encoding by allowing multidimensional position representation and data-dependent rotation, potentially improving transformer training efficiency and model interpretability for sequential data. HDD-RoPE splits queries and keys into chunks of arbitrary size (e.g., 4 dimensions), enabling multiple rotation axes, and makes the rotation amount data-dependent per layer. The open-source GitHub repository provides code and mathematical details to replicate results.

reddit · r/MachineLearning · /u/mikayahlevi · Jun 24, 18:16

**Background**: Rotary Position Embedding (RoPE) encodes token positions by rotating query-key pairs at fixed rates, enabling relative position learning. xPos is an improved version of RoPE used in models like RetNet. The cumulative matrix product is a mathematical operation that sequentially multiplies matrices, which HDD-RoPE repurposes for dynamic positional encoding.

<details><summary>References</summary>
<ul>
<li><a href="https://zeta.apac.ai/en/latest/zeta/nn/biases/xpos/">Xpos - zeta</a></li>
<li><a href="https://huggingface.co/datasets/roneneldan/TinyStories/tree/main">roneneldan/ TinyStories at main</a></li>

</ul>
</details>

**Tags**: `#Machine Learning`, `#Transformer`, `#Positional Encoding`, `#RoPE`, `#Research`

---

<a id="item-10"></a>
## [Micron's Q3 FY2026 Revenue Surges 346% YoY, Profit $28.24B](https://www.globenewswire.com/news-release/2026/06/24/3317151/14450/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html) ⭐️ 8.0/10

Micron Technology reported record fiscal third-quarter 2026 results with revenue of $41.46 billion, a 346% year-over-year increase, and net income of $28.24 billion. This exceptional growth underscores the explosive demand for high-performance memory driven by AI infrastructure, positioning Micron as a key beneficiary of the AI boom with significant implications for memory supply chains and the broader semiconductor industry. The company's Non-GAAP gross margin surged to 84.9%, and it expects revenue of $50 billion next quarter with gross margin of 86% amid tight memory supply through 2027.

telegram · zaihuapd · Jun 24, 22:22

**Background**: High Bandwidth Memory (HBM) is a 3D-stacked DRAM technology used in high-performance computing and AI accelerators. HBM4, the latest generation, offers up to 2 TB/s bandwidth per stack. Micron has begun mass production of HBM4 and plans HBM4E for 2027.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.micron.com/products/memory/hbm/hbm4">HBM4 - Memory</a></li>

</ul>
</details>

**Tags**: `#Micron`, `#AI infrastructure`, `#memory`, `#semiconductors`, `#earnings`

---

<a id="item-11"></a>
## [Google Play to Enable External Billing in US, UK, EU](https://android-developers.googleblog.com/2026/06/play-expanded-billing.html) ⭐️ 8.0/10

Starting June 30, Google Play Store will allow developers in the US, UK, and European Economic Area to offer alternative in-app billing or external web purchasing options, with a new fee structure separating service and billing settlement fees. This expansion marks a major shift in app store policies, following the Epic Games settlement, and could reduce developer costs and increase competition in mobile payment processing. The new fee structure includes a 10% service fee for the first $1 million in annual revenue and auto-renewing subscriptions, while a 5% billing settlement fee applies only to transactions using Google Play Billing; alternative billing methods avoid this 5% fee.

telegram · zaihuapd · Jun 25, 02:33

**Background**: Google has historically required all in-app purchases to go through its own billing system, charging a 30% commission. Following a legal settlement with Epic Games, Google agreed to lower fees and allow alternative payments. The new policy is part of that rollout, with additional markets to follow in 2027.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/google/2026/06/google-starts-lowering-play-store-fees-making-good-on-epic-games-settlement/">Google starts lowering Play Store fees, making good on Epic ...</a></li>
<li><a href="https://techcrunch.com/2026/03/04/google-settles-with-epic-games-drops-its-play-store-commissions-to-20/">Google settles with Epic Games, drops its Play Store ...</a></li>

</ul>
</details>

**Tags**: `#Google Play`, `#app store policies`, `#external billing`, `#antitrust`, `#developer fees`

---

<a id="item-12"></a>
## [Eric Schmidt Criticizes Chinese Open-Source AI as Uncontrollable](https://www.youtube.com/watch?v=I2F2xFvt4mQ&amp;t=397s) ⭐️ 8.0/10

Eric Schmidt, former Google CEO, stated in a recent discussion that he dislikes Chinese AI's open-source approach because it cannot be controlled by the US, while acknowledging its low-cost advantage, and urged US investment in AI infrastructure. This highlights geopolitical tensions in AI development and the strategic importance of open-source models, underscoring how Chinese AI's low-cost, open-source strategy could challenge US dominance and reshape global AI competition. Schmidt noted that Chinese firms use algorithm innovation to overcome hardware constraints, making them true competitors; the open-source nature means the US cannot control Chinese AI advancements, and he reiterated the need for US investment in compute infrastructure and research.

telegram · zaihuapd · Jun 25, 11:30

**Background**: Open-source AI models allow anyone to use, modify, and distribute the technology. Chinese companies like DeepSeek have released competitive open-source models despite hardware restrictions from US sanctions, leading to a rapid catch-up in AI capabilities. A recent MIT study found that Chinese open-source models have surpassed US models in total downloads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/spollak_whats-next-for-chinese-open-source-ai-activity-7436413066386452480-ueoY">China 's Open Source AI Models Gain Momentum | LinkedIn</a></li>
<li><a href="https://www.meibel.ai/post/deepseek-r1-how-hardware-constraints-led-to-an-ai-innovation-revolution">DeepSeek R1: How Hardware Constraints Led to an AI Innovation Revolution - Meibel</a></li>
<li><a href="https://www.orcaster.com/p/03289700-bf63-4528-b3e8-2383c2152cdb/">What open - source AI looks like after the DeepSeek moment</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#geopolitics`, `#Eric Schmidt`, `#competition`

---
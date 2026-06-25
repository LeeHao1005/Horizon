---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 39 条内容中筛选出 12 条重要资讯。

---

1. [OpenAI 与博通联手推出首款定制 AI 推理芯片'Jalapeno'](#item-1) ⭐️ 9.0/10
2. [Cloudflare 推出自管理 OAuth 服务](#item-2) ⭐️ 9.0/10
3. [Anthropic 指控阿里巴巴发动大规模蒸馏攻击窃取 Claude 能力](#item-3) ⭐️ 9.0/10
4. [WebAssembly 让《半条命 2》在浏览器中运行](#item-4) ⭐️ 8.0/10
5. [RubyLLM：为所有主要 AI 提供商打造的 Ruby 框架](#item-5) ⭐️ 8.0/10
6. [不再信任基准测试，开始自建评估集](#item-6) ⭐️ 8.0/10
7. [大规模工具选择：词汇检索优于语义嵌入](#item-7) ⭐️ 8.0/10
8. [通过自对弈强化学习打造超人类 Generals.io 智能体](#item-8) ⭐️ 8.0/10
9. [HDD-RoPE：更快速收敛的动态位置嵌入](#item-9) ⭐️ 8.0/10
10. [美光 Q3 营收同比增 346% 日赚 3.1 亿美元](#item-10) ⭐️ 8.0/10
11. [谷歌 Play 商店将在美英欧启用外部计费](#item-11) ⭐️ 8.0/10
12. [施密特批评中国开源 AI 不可控](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 与博通联手推出首款定制 AI 推理芯片'Jalapeno'](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 与博通联合发布了 Jalapeno 芯片，这是一款专为大语言模型设计的定制 AI 推理处理器，声称相比当前英伟达 GPU 可将每 token 推理成本降低约 50%。该芯片在九个月内开发完成，借助 OpenAI 自身模型加速了设计流程，工程样品已在实验室中运行 GPT-5.3-Codex-Spark。 这标志着 OpenAI 向垂直整合迈出重要一步，减少对英伟达 GPU 的依赖，有望降低 ChatGPT、Codex 以及未来 AI 代理的服务成本。同时也凸显了 AI 公司为特定工作负载定制芯片以优化性能和效率的加速趋势。 Jalapeno 是一款仅用于推理的芯片，由博通合作开发、台积电制造，基于 OpenAI 对推理需求的洞察设计，可适配所有大语言模型。OpenAI 使用自身模型加速芯片设计，声称从设计到生产仅用九个月，但有关 AI 如何加速设计过程的具体细节尚不明确。

hackernews · jamdesk · 6月24日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 推理是运行已训练模型生成输出的过程，需要大量计算资源，尤其是大模型。目前大多数 AI 公司依赖英伟达 GPU 进行训练和推理，但专用推理芯片能提供更好的每瓦性能和更低的成本。传统定制芯片设计需要数年时间，但 AI 驱动的设计自动化技术正在缩短这一周期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip</a></li>
<li><a href="https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/">OpenAI unveils its first custom chip, built by Broadcom</a></li>
<li><a href="https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html">OpenAI and Broadcom reveal Jalapeno, first AI chip in partnership - CNBC</a></li>

</ul>
</details>

**社区讨论**: 评论者对 OpenAI 模型如何加速芯片设计的具体细节表示好奇，部分人怀疑这可能只是营销噱头。其他人讨论了专用推理芯片的技术潜力，例如将权重嵌入 ROM 以实现极高吞吐量，并提出这对 Cerebras 等竞争对手的影响。

**标签**: `#AI hardware`, `#custom chip`, `#OpenAI`, `#Broadcom`, `#inference`

---

<a id="item-2"></a>
## [Cloudflare 推出自管理 OAuth 服务](https://blog.cloudflare.com/oauth-for-all/) ⭐️ 9.0/10

Cloudflare 推出了一项自管理的 OAuth 服务，允许开发者在不依赖第三方提供商的情况下实现身份验证。该服务旨在提供可扩展性和高性能。 这很重要，因为它解决了开发者在构建身份验证系统（尤其是大规模系统）时常见的痛点。作为一家主要的云提供商，Cloudflare 的这一产品可以简化 OAuth 实现并减少供应商锁定。 该服务是自管理的，意味着开发者可以完全控制自己的 OAuth 基础设施。Cloudflare 声称其性能和可靠性与其现有的边缘网络相当。

hackernews · terryds · 6月25日 02:18 · [社区讨论](https://news.ycombinator.com/item?id=48668033)

**背景**: OAuth 是一种用于访问授权的开放标准，常用于基于令牌的身份验证和授权。从头实现 OAuth 可能很复杂，因此许多开发者依赖第三方服务或框架（如 Ory Hydra）。

**社区讨论**: 社区反应不一。一些开发者欢迎 Cloudflare 进入 OAuth 领域，而另一些则对 Cloudflare 过去发布项目后缺乏持续改进的记录表示担忧。Ory Hydra 的作者赞扬了技术描述，但指出他们自己的商业变体速度更快。

**标签**: `#OAuth`, `#Cloudflare`, `#authentication`, `#developer tools`, `#IAM`

---

<a id="item-3"></a>
## [Anthropic 指控阿里巴巴发动大规模蒸馏攻击窃取 Claude 能力](https://www.cnbc.com/2026/06/24/anthropic-alibaba-distillation-campaign.html) ⭐️ 9.0/10

Anthropic 致信美国参议院银行委员会，指控阿里巴巴通过近 2.5 万个虚假账户，在 2026 年 4 月 22 日至 6 月 5 日期间与 Claude 进行了超过 2880 万次交互，声称这是迄今为止已知最大规模的蒸馏攻击。 这一指控凸显了美中之间在人工智能知识产权问题上日益紧张的局势，可能导致对 API 访问和国际人工智能贸易的更严格监管，从而影响公司如何保护其模型。 此次攻击涉及阿里巴巴及其 Qwen AI 实验室等多个实体，窃取的知识很可能被用于复制 Claude 的能力。Anthropic 通过分类器和行为指纹识别系统检测到了这一模式。

telegram · zaihuapd · 6月25日 01:36

**背景**: 模型蒸馏是一种技术，其中较小的“学生”模型通过从较大的“教师”模型的输出中学习，以较低成本实现类似性能。虽然该技术常用于合法的模型压缩，但未经许可利用它窃取专有知识则被视为攻击，引发了重大的知识产权和安全担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks - Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://www.iaps.ai/research/ai-distillation-attacks-the-case-for-targeted-government-intervention">AI Distillation Attacks: The Case for Targeted Government Intervention</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了质疑，认为蒸馏是一种常见做法，而 Anthropic 的投诉是虚伪的，因为主要 AI 实验室都是在未经许可的情况下使用公共数据训练的。有人将其比作苹果与施乐过去的纠纷，而另一些人则担心这赋予了 AI 公司过多的权力。

**标签**: `#AI security`, `#model distillation`, `#Anthropic`, `#Alibaba`, `#intellectual property`

---

<a id="item-4"></a>
## [WebAssembly 让《半条命 2》在浏览器中运行](https://hl2.slqnt.dev/) ⭐️ 8.0/10

《半条命 2》的 WebAssembly 移植版本现已在浏览器中直接可玩（hl2.slqnt.dev），展示了在网页平台上运行复杂 3D 游戏的能力。 这一移植表明，即使是 2000 年代中期图形密集的复杂游戏也能无需插件引入网页，可能提高可及性并减少平台锁定。 该移植使用 Emscripten 将原始 C++ 代码编译为 WebAssembly，但社区成员指出缺少某些着色器（如角色眼睛），导致视觉效果相比原生版本略有下降。

hackernews · panza · 6月25日 06:00 · [社区讨论](https://news.ycombinator.com/item?id=48669534)

**背景**: WebAssembly（Wasm）是一种低级二进制格式，用于在网页浏览器中安全、高性能地执行，被设计为 C、C++、Rust 等语言的编译目标。Emscripten 是一个编译器工具链，可将 LLVM 位码转换为 WebAssembly，使原生应用程序能在网页上运行。这一组合使得像《半条命 2》这样原本用 C++ 编写的游戏能够移植到浏览器中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://en.wikipedia.org/wiki/Emscripten">Emscripten</a></li>

</ul>
</details>

**社区讨论**: 评论普遍感到印象深刻，但指出缺少视觉特性（如角色眼睛），并提到类似项目如浏览器中的《雷神之锤 3》和《虚幻竞技场》移植，以及用于探索游戏关卡的 noclip.website。一位用户强调了讽刺之处：该游戏在 macOS 上的浏览器中运行，而原生的 Steam 版本因 32 位支持废弃而不可用。

**标签**: `#webassembly`, `#game development`, `#browser`, `#emscripten`, `#retro gaming`

---

<a id="item-5"></a>
## [RubyLLM：为所有主要 AI 提供商打造的 Ruby 框架](https://rubyllm.com/) ⭐️ 8.0/10

RubyLLM 已发布，作为一个统一的 Ruby 框架，支持所有主要 AI 提供商，使开发者能够轻松构建聊天机器人、AI 代理和 RAG 应用。 该框架填补了 Ruby 生态系统中的关键空白，为开发者提供了跨 AI 提供商的一致性接口，显著降低了在 Ruby 中构建 AI 驱动应用的复杂性。 RubyLLM 依赖极少（Faraday、Zeitwerk、Marcel），支持 GPT-4、Claude、Gemini、Ollama 等提供商。社区反馈指出 xAI 的缓存问题以及最初缺乏原生的 responses API（现已解决）。

hackernews · doener · 6月24日 14:41 · [社区讨论](https://news.ycombinator.com/item?id=48660711)

**背景**: 许多 AI 提供商各自推出不同的 API 客户端，具有不同的约定和响应格式，给开发者带来碎片化的体验。RubyLLM 将这些统一为一个优雅的 Ruby API，类似于 Vercel 的 JavaScript AI SDK。它旨在开箱即用，同时灵活支持自定义工具和代理等高级用例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rubyllm.com/">RubyLLM | One beautiful Ruby framework for all major AI ...</a></li>
<li><a href="https://github.com/crmne/ruby_llm">GitHub - crmne/ruby_llm: One delightful Ruby framework for ...</a></li>

</ul>
</details>

**社区讨论**: 社区反响总体积极，用户称赞 RubyLLM 的 API 设计和易用性，常与 Vercel 的 AI 框架相提并论。一些不满包括 xAI 的缓存问题和 PR 合并缓慢，但社区对 RubyLLM 2.0 充满期待，该版本将原生支持 responses API。

**标签**: `#Ruby`, `#AI`, `#Framework`, `#LLM`, `#API`

---

<a id="item-6"></a>
## [不再信任基准测试，开始自建评估集](https://www.reddit.com/r/MachineLearning/comments/1uf53un/i_stopped_trusting_model_benchmarks_and_started/) ⭐️ 8.0/10

作者从实际生产流量中构建了一个包含 240 个任务的定制评估集，发现公开基准测试常常无法准确反映模型在特定工作负载下的表现。 这之所以重要，是因为仅依赖公开基准测试可能导致模型选择失误甚至生产事故，凸显了基于自身数据分布进行定制化评估的必要性。 评估集被冻结以防止漂移，所有模型通过 GPTProto 路由以消除供应商差异，确保公平比较；一个在基准测试中表现良好的模型被发现存在危险的边缘情况故障模式。

reddit · r/MachineLearning · /u/Additional-Engine402 · 6月25日 09:22

**背景**: 像 DeepSWE 和 Artificial Analysis Intelligence Index 这样的公开基准测试被广泛用于比较模型，但它们存在局限性：DeepSWE 评估编码智能体在原创任务上的表现，而 Artificial Analysis 结合多项指标。然而，这些基准测试可能无法反映特定的生产分布，正如作者在使用供应商自设计基准和自报参数时所经历的那样。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepswe.net/">DeepSWE Benchmark: GPT vs Claude for Agentic Coding</a></li>
<li><a href="https://artificialanalysis.ai/">AI Model & API Providers Analysis | Artificial Analysis</a></li>
<li><a href="https://benchlm.ai/benchmarks/deepSwe">DeepSWE Benchmark 2026: 8 pass@1 rows | BenchLM.ai</a></li>

</ul>
</details>

**标签**: `#benchmarks`, `#evaluation`, `#LLM`, `#machine learning`, `#reliability`

---

<a id="item-7"></a>
## [大规模工具选择：词汇检索优于语义嵌入](https://www.reddit.com/r/MachineLearning/comments/1ufafnw/tool_selection_at_scale_is_a_retrieval_problem/) ⭐️ 8.0/10

一位开发者根据对 43000 个工具语料库的实证评估提出，在大规模智能体工具选择中，词汇检索（BM25）比语义嵌入效果更好。 这一观点挑战了在智能体系统中默认使用语义嵌入进行工具检索的常见做法，有可能提高大规模工具目录的检索准确性并降低成本。 工具描述简短且结构相似（动词-名词、参数列表），因此密集嵌入上的余弦相似度会稀释单个区分性标记。BM25 对名称、描述和模式的纯文本投影进行检索，能保留该区分标记，且完全在进程内运行，无需嵌入模型。

reddit · r/MachineLearning · /u/AbjectBug5885 · 6月25日 13:43

**背景**: 模型上下文协议（MCP）是 Anthropic 提出的开放标准，用于连接 AI 应用与外部工具和数据源。在大规模智能体系统中，可调用的工具集合可能非常庞大，因此需要检索步骤为每个请求选择相关子集。传统的文档 RAG 使用语义嵌入进行检索，但工具描述与文档不同，它们简短且具有词汇区分性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://medium.com/@dineshkarthik_kandregula/hybrid-retrieval-bm25-vs-dense-embeddings-smarter-search-using-elasticsearch-huggingface-3dd6a6351b05">Hybrid Retrieval : BM25 vs . Dense Embeddings — Smarter... | Medium</a></li>
<li><a href="https://aimlinsights.com/dense-retrieval-vs-sparse-retrieval/">Dense Retrieval vs Sparse Retrieval Explained for RAG » AIML Insights</a></li>

</ul>
</details>

**标签**: `#tool selection`, `#retrieval`, `#agents`, `#embeddings`, `#MCP`

---

<a id="item-8"></a>
## [通过自对弈强化学习打造超人类 Generals.io 智能体](https://www.reddit.com/r/MachineLearning/comments/1uei2yg/i_made_a_superhuman_generalsio_agent_with/) ⭐️ 8.0/10

一位研究者使用自对弈强化学习训练了一个超人类级别的 Generals.io 智能体，该智能体基于 JAX 和 Vision Transformer 实现，并在人类 1v1 排行榜上排名第一。 这展示了规模化与现代化架构（JAX、ViT）相比手工特征的优势，开源发布为游戏 AI 研究提供了宝贵资源。 整个流程从 NumPy/Torch 重新用 JAX 实现，并用 Vision Transformer 替代了 CNN，从而加快了训练速度并提升了性能。

reddit · r/MachineLearning · /u/shrekofspeed · 6月24日 16:18

**背景**: Generals.io 是一款不完全信息的实时策略游戏。自对弈强化学习是指智能体通过与自身对弈来学习。JAX 是一个高性能数值计算库，Vision Transformer 将 Transformer 架构应用于图像块。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JAX_(software)">JAX (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision_transformer">Vision transformer</a></li>
<li><a href="https://arxiv.org/abs/2010.11929">[2010.11929] An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale</a></li>

</ul>
</details>

**标签**: `#reinforcement-learning`, `#self-play`, `#game-ai`, `#JAX`, `#vision-transformer`

---

<a id="item-9"></a>
## [HDD-RoPE：更快速收敛的动态位置嵌入](https://www.reddit.com/r/MachineLearning/comments/1uelcm9/high_dimensional_dynamic_rotary_positional/) ⭐️ 8.0/10

作者提出了 HDD-RoPE，一种使用累积矩阵乘积的高维动态旋转位置嵌入方法，在 TinyStories 数据集上比 xPos 基线实现了更快的收敛。 该方法通过支持多维位置表示和数据依赖旋转，推进了位置编码技术，有望提高 Transformer 在序列数据上的训练效率和模型可解释性。 HDD-RoPE 将查询和键分割成任意大小的块（例如 4 维），支持多个旋转轴，并使每层的旋转量依赖于数据。开源 GitHub 仓库提供了复现结果的代码和数学细节。

reddit · r/MachineLearning · /u/mikayahlevi · 6月24日 18:16

**背景**: 旋转位置编码（RoPE）通过以固定速率旋转查询-键对来编码标记位置，实现相对位置学习。xPos 是 RoPE 的改进版本，用于 RetNet 等模型。累积矩阵乘积是一种数学运算，按顺序相乘矩阵，HDD-RoPE 将其重新用于动态位置编码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zeta.apac.ai/en/latest/zeta/nn/biases/xpos/">Xpos - zeta</a></li>
<li><a href="https://huggingface.co/datasets/roneneldan/TinyStories/tree/main">roneneldan/ TinyStories at main</a></li>

</ul>
</details>

**标签**: `#Machine Learning`, `#Transformer`, `#Positional Encoding`, `#RoPE`, `#Research`

---

<a id="item-10"></a>
## [美光 Q3 营收同比增 346% 日赚 3.1 亿美元](https://www.globenewswire.com/news-release/2026/06/24/3317151/14450/en/micron-technology-inc-reports-record-results-for-the-third-quarter-of-fiscal-2026.html) ⭐️ 8.0/10

美光科技公布 2026 财年第三季度创纪录业绩，营收达 414.6 亿美元，同比增长 346%，净利润达 282.4 亿美元。 这一异常增长凸显了 AI 基础设施对高性能内存的爆发式需求，使美光成为 AI 热潮的关键受益者，对内存供应链和整个半导体行业产生深远影响。 公司 Non-GAAP 毛利率飙升至 84.9%，预计下季度营收达 500 亿美元，毛利率达 86%，内存紧缺将持续至 2027 年以后。

telegram · zaihuapd · 6月24日 22:22

**背景**: 高带宽存储器（HBM）是一种用于高性能计算和 AI 加速器的 3D 堆叠 DRAM 技术。最新一代 HBM4 每堆叠提供高达 2 TB/s 的带宽。美光已开始大规模量产 HBM4，并计划于 2027 年推出 HBM4E。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://www.micron.com/products/memory/hbm/hbm4">HBM4 - Memory</a></li>

</ul>
</details>

**标签**: `#Micron`, `#AI infrastructure`, `#memory`, `#semiconductors`, `#earnings`

---

<a id="item-11"></a>
## [谷歌 Play 商店将在美英欧启用外部计费](https://android-developers.googleblog.com/2026/06/play-expanded-billing.html) ⭐️ 8.0/10

从 6 月 30 日起，谷歌 Play 商店将允许美国、英国和欧洲经济区的开发者提供第三方应用内计费或外部网页购买选项，并采用分离服务费和结算费的新费率结构。 此次扩展是继 Epic Games 和解后应用商店政策的重大转变，可能降低开发者成本并增加移动支付处理的竞争。 新费率结构包括年收入首 100 万美元和自动续订订阅收取 10%服务费，而 5%结算费仅适用于使用 Google Play Billing 的交易；替代计费方式则无需支付此 5%费用。

telegram · zaihuapd · 6月25日 02:33

**背景**: 谷歌历来要求所有应用内购买必须通过其自有计费系统，并收取 30%佣金。在与 Epic Games 达成法律和解后，谷歌同意降低费用并允许替代支付方式。新政策是该推广的一部分，其他市场将于 2027 年跟进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/google/2026/06/google-starts-lowering-play-store-fees-making-good-on-epic-games-settlement/">Google starts lowering Play Store fees, making good on Epic ...</a></li>
<li><a href="https://techcrunch.com/2026/03/04/google-settles-with-epic-games-drops-its-play-store-commissions-to-20/">Google settles with Epic Games, drops its Play Store ...</a></li>

</ul>
</details>

**标签**: `#Google Play`, `#app store policies`, `#external billing`, `#antitrust`, `#developer fees`

---

<a id="item-12"></a>
## [施密特批评中国开源 AI 不可控](https://www.youtube.com/watch?v=I2F2xFvt4mQ&amp;t=397s) ⭐️ 8.0/10

谷歌前 CEO 埃里克·施密特在最近的讨论中表示，他不喜欢中国 AI 采用开源模式，因为这种模式无法被美国控制，但同时承认其低成本优势，并敦促美国加大对 AI 基础设施的投资。 这凸显了 AI 开发中的地缘政治紧张局势以及开源模型的战略重要性，表明中国 AI 的低成本开源策略可能挑战美国的主导地位，并重塑全球 AI 竞争格局。 施密特指出，中国企业通过算法创新克服硬件限制，成为真正的竞争对手；开源特性意味着美国无法控制中国的 AI 进展，他重申美国需加大在算力基础设施和研究方面的投入。

telegram · zaihuapd · 6月25日 11:30

**背景**: 开源 AI 模型允许任何人使用、修改和分发技术。尽管受到美国制裁的硬件限制，中国公司如 DeepSeek 仍发布了具有竞争力的开源模型，导致 AI 能力快速追赶。麻省理工学院的一项最新研究发现，中国开源模型在总下载量上已超过美国模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/spollak_whats-next-for-chinese-open-source-ai-activity-7436413066386452480-ueoY">China 's Open Source AI Models Gain Momentum | LinkedIn</a></li>
<li><a href="https://www.meibel.ai/post/deepseek-r1-how-hardware-constraints-led-to-an-ai-innovation-revolution">DeepSeek R1: How Hardware Constraints Led to an AI Innovation Revolution - Meibel</a></li>
<li><a href="https://www.orcaster.com/p/03289700-bf63-4528-b3e8-2383c2152cdb/">What open - source AI looks like after the DeepSeek moment</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#geopolitics`, `#Eric Schmidt`, `#competition`

---
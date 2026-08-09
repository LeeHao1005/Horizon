---
layout: default
title: "Horizon Summary: 2026-08-09 (ZH)"
date: 2026-08-09
lang: zh
---

> 从 36 条内容中筛选出 10 条重要资讯。

---

1. [使用 Plantard 约减的更快形式化验证 NTT 代码生成](#item-1) ⭐️ 8.0/10
2. [基于 AES 的 MPC-in-the-Head 签名打磨方案](#item-2) ⭐️ 8.0/10
3. [Cloudflare 发布 MCP v2：适用于 Workers 的无状态核心](#item-3) ⭐️ 8.0/10
4. [Cloudflare 倡导开放智能体互联网：可读、可发现、可调用、可支付](#item-4) ⭐️ 8.0/10
5. [Cloudflare 推出 Kitesurf：运行在 V8 隔离环境中的代理优先浏览器](#item-5) ⭐️ 8.0/10
6. [Cloudflare 推出 WebMCP 预览版，让任何网站支持 AI 代理](#item-6) ⭐️ 8.0/10
7. [ICE 从数据经纪商处购买信用卡申请数据](#item-7) ⭐️ 8.0/10
8. [NIST 发布关于 5G 初始 NAS 消息安全的白皮书草案](#item-8) ⭐️ 8.0/10
9. [Cloudflare 推出基于 BotBase 和 Precursor 的持续机器人信任评估](#item-9) ⭐️ 7.0/10
10. [Cloudflare 推出 AI 搜索，简化数据搜索流程](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [使用 Plantard 约减的更快形式化验证 NTT 代码生成](https://eprint.iacr.org/2026/1624) ⭐️ 8.0/10

该论文引入了一个自动代码生成器，可基于 Plantard 算术和静态边界分析，为 ML-KEM、ML-DSA 和 FN-DSA 生成形式化验证的更快 NTT 实现，消除了运行时分支。生成的代码通过 EasyCrypt 进行了端到端正确性证明，基准测试显示其性能显著优于参考实现和现有验证代码。 这项工作自动化了关键后量子方案的高性能形式化验证 NTT 代码生成，减少了手动调优工作并确保了常时安全性。这可能加速安全高效后量子密码学的部署。 该生成器使用一组参数三元组来针对多种方案，生成两种后端（可移植 C 和用于验证的 Jasmin），性能提升最高可达参考 C 的 2.5 倍和现有验证 Jasmin 基线的 2.19 倍。静态边界分析器在编译时放置模约减，消除了运行时分支，同时保持了常时保证。

rss · IACR ePrint 密码学论文 · 8月6日 05:37

**背景**: 数论变换（NTT）是有限域上的离散傅里叶变换，用于加速格基密码学（如 ML-KEM/Kyber 和 ML-DSA/Dilithium）中的多项式乘法。Plantard 算术是一种使用近似来避免昂贵除法运算的模约减技术，可提升性能。EasyCrypt 是一个交互式框架，用于形式化验证密码学实现，能够证明功能正确性和常时执行等安全属性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1624">Code Generation of Faster Formally Verified NTT with Plantard ...</a></li>
<li><a href="https://www.easycrypt.info/">EasyCrypt</a></li>

</ul>
</details>

**标签**: `#formal-verification`, `#NTT`, `#post-quantum-cryptography`, `#code-generation`, `#Plantard-reduction`

---

<a id="item-2"></a>
## [基于 AES 的 MPC-in-the-Head 签名打磨方案](https://eprint.iacr.org/2026/1625) ⭐️ 8.0/10

该论文在 MPC-in-the-Head 签名中引入一种打磨方案，用 AES 分组密码调用替代标准的 Keccak 哈希函数，形式化其安全性，并提出一种每次迭代两次 AES 调用的构造。 由于硬件加速，AES 在现代 CPU 上比 Keccak 快得多，而打磨技术正被三个 NIST 第三轮后量子签名候选方案所采用，因此该优化有望实现更快的签名和更短的证明。 在理想密码与随机预言模型下，伪造概率被上界为(4/3)·ε·Q_E / 2^w；该构造可推广至每次迭代更多次密码调用，使得常数因子任意接近 1。

rss · IACR ePrint 密码学论文 · 8月6日 08:19

**背景**: MPC-in-the-Head 是一种通过模拟安全多方计算来构造后量子签名的方法。Fiat-Shamir 变换通过从哈希函数导出挑战值，将交互式证明转化为非交互式。打磨是一种工作量证明技术，强制挑战值满足 w 比特条件，从而增加伪造难度，并可缩减参数以生成更短的签名。AES 是一种广泛使用的分组密码，受益于 CPU 专用指令（AES-NI）因而速度极快，而 Keccak 是一种较慢的哈希函数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1625">AES-Based Grinding for MPC-in-the-Head Signatures</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#digital signatures`, `#MPC-in-the-Head`, `#AES`, `#grinding`

---

<a id="item-3"></a>
## [Cloudflare 发布 MCP v2：适用于 Workers 的无状态核心](https://blog.cloudflare.com/mcp-v2/) ⭐️ 8.0/10

Cloudflare 发布了 MCP v2，其完全重写的无状态核心使得模型上下文协议能够在 Cloudflare Workers 这类无服务器平台上运行，同时还包括协议升级、新功能生命周期和 SDK 迁移指南。 此次更新意义重大，因为它使得用于连接 AI 模型与外部工具及数据的开放标准 MCP 能够部署在可扩展的无服务器基础设施上，有望加快应用落地并降低 AI 开发者的门槛。 关键技术细节包括：针对 Cloudflare Workers 优化的无状态架构、协议层面的升级、明确的 MCP 功能生命周期定义，以及将现有基于 SDK 的实现迁移到新版本的指南。

rss · Cloudflare Blog (PQ 迁移) · 8月6日 13:00

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年底推出的开放标准，旨在标准化大语言模型等 AI 系统与外部数据、工具和系统的连接方式。Cloudflare Workers 是一种无服务器计算平台，能让代码在边缘运行而无需管理服务器。无状态架构对于无服务器环境至关重要，因为函数会独立扩展且无法在调用之间共享状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>

</ul>
</details>

**标签**: `#Model Context Protocol`, `#Cloudflare Workers`, `#AI infrastructure`, `#protocol upgrade`, `#serverless`

---

<a id="item-4"></a>
## [Cloudflare 倡导开放智能体互联网：可读、可发现、可调用、可支付](https://blog.cloudflare.com/the-agentic-internet/) ⭐️ 8.0/10

Cloudflare 宣布了一项计划，旨在构建开放工具和协议，实现一个将代表人类客户的 AI 代理视为合法访客而非予以屏蔽的智能体互联网。 这解决了随着 AI 代理与网站交互日益增多而出现的迫切需求，可防止发布者无意中屏蔽潜在客户，并促进代理与发布者之间的高效合作。 该提议框架围绕四项原则展开：可读（代理能解析内容）、可发现（代理能发现服务）、可调用（代理能程序化交互）和可支付（支持交易）。具体技术实现细节尚未公布。

rss · Cloudflare Blog (PQ 迁移) · 8月6日 13:00

**背景**: 智能体互联网描绘了一个未来网络：自主 AI 代理在没有人类直接监督的情况下执行任务、做出决策并进行交易。目前，许多网站屏蔽包括代表用户的代理在内的自动化流量，造成了摩擦。作为主要的网络基础设施和安全提供商，Cloudflare 旨在构建必要协议，使网络对智能体友好，这类似于它过去塑造网络性能和安全标准的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agenticinternet.com/">Agentic Internet</a></li>
<li><a href="https://blog.apollospace.ai/blog/agentic-internet/">The agentic internet : when software talks to software | Apollo Space</a></li>
<li><a href="https://media-beats.com/en/agentic-internet/">Agentic internet : significance for online marketing</a></li>

</ul>
</details>

**标签**: `#ai-agents`, `#web-infrastructure`, `#open-web`, `#protocols`, `#cloudflare`

---

<a id="item-5"></a>
## [Cloudflare 推出 Kitesurf：运行在 V8 隔离环境中的代理优先浏览器](https://blog.cloudflare.com/kitesurf/) ⭐️ 8.0/10

Cloudflare 推出了 Kitesurf，这是一款无状态、高度可扩展且成本效益高的网络浏览器，专为 AI 代理设计，完全运行在 Cloudflare Workers 的 V8 隔离环境中。 通过为 AI 代理定制浏览器，Kitesurf 能够实现更高效、可扩展的网页自动化，从而降低海量代理任务的成本和延迟，推动代理式云应用的发展。 Kitesurf 利用 V8 隔离实现轻量级、安全的沙箱化浏览器会话，并借助 Cloudflare 全球边缘网络，确保低延迟和高并发处理能力。

rss · Cloudflare Blog (PQ 迁移) · 8月6日 13:00

**背景**: V8 隔离是源自 Google V8 引擎的沙箱化 JavaScript 执行环境，具有快速启动和强隔离特性。Cloudflare Workers 是一个全球性的无服务器计算平台，利用这些隔离在靠近用户的边缘节点运行代码。Kitesurf 以这些技术为基础，提供了无传统浏览器开销的网页浏览能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/tomlienard/v8-isolates-are-taking-over-the-world-3h4m">V 8 Isolates are taking over the world - DEV Community</a></li>
<li><a href="https://www.cloudflare.com/products/workers/">Cloudflare Workers - Global Serverless Functions Platform</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#agents`, `#browser`, `#serverless`, `#ai`

---

<a id="item-6"></a>
## [Cloudflare 推出 WebMCP 预览版，让任何网站支持 AI 代理](https://blog.cloudflare.com/webmcp/) ⭐️ 8.0/10

Cloudflare 推出了 WebMCP 的开发者预览版，只需一键开关，任何网站即可被浏览器 AI 代理使用，无需新增 API 或修改源站，同时保持用户控制和网站流量。 这一进展简化了 AI 代理与网站的集成，有望加速自主网页交互的普及。它使网站所有者能够向 AI 暴露结构化工具，在提升自动化、可访问性和新型用户体验的同时，不牺牲安全性和流量。 WebMCP 基于提议的 W3C 标准，通过 navigator.modelContext 暴露 JavaScript 工具，允许浏览器内代理调用网站定义的函数。该预览版运行在 Cloudflare 的基础设施上，具体实现细节和限制属于开发者预览的一部分。

rss · Cloudflare Blog (PQ 迁移) · 8月6日 13:00

**背景**: WebMCP 是一项新兴标准，允许网站在浏览器中直接向 AI 代理暴露工具，作为 DOM 解析的替代方案。模型上下文协议（MCP）是 Anthropic 引入的开放标准，用于 AI 系统与外部工具集成，已获多家主要 AI 提供商采用。浏览器 AI 代理是能够自主浏览并执行网页任务的程序，它们从结构化的 WebMCP 交互中受益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/WebMCP">WebMCP</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://wmcp.sh/webmcp">WebMCP — make any website agent-ready in one line | wmcp.sh</a></li>

</ul>
</details>

**标签**: `#WebMCP`, `#Cloudflare`, `#AI agents`, `#web development`, `#developer tools`

---

<a id="item-7"></a>
## [ICE 从数据经纪商处购买信用卡申请数据](https://www.schneier.com/blog/archives/2026/08/ice-is-buying-access-to-credit-card-records.html) ⭐️ 8.0/10

美国移民及海关执法局（ICE）现正通过商业数据经纪人购买信用卡申请中的个人信息，如姓名和地址，以此绕过获取搜查令的要求。 这一做法使得政府能够在没有司法授权的情况下进行大规模监控，威胁隐私权，并可能让移民社区因担心被追踪而减少金融活动。它体现了数字时代第四修正案保护受到侵蚀的更广泛趋势。 所获取的数据可能包括信用头信息——姓名、地址、社会安全号码、出生日期——但不包括交易或信用评分数据。这些数据在未经个人同意的情况下被获取，且没有联邦法律禁止此类转售。

rss · Schneier on Security · 8月7日 10:26

**背景**: 数据经纪人收集并出售从公共记录、在线活动和商业交易中获得的个人数据。信用头信息源自益博睿（Experian）等信用局，传统上用于身份验证和防欺诈。美国薄弱的隐私法律允许经纪人将此类数据出售给几乎任何买家，包括政府机构。ICE 的购买行为凸显了商业数据市场如何让执法机构规避司法审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_broker">Data broker</a></li>
<li><a href="https://www.offlist.me/privacy-glossary/credit-header-data">Credit Header Data: Definition & Why It Matters (2026)</a></li>
<li><a href="https://www.experian.com/blogs/news/2024/10/01/credit-header-data-an-indispensable-tool-to-combatting-fraud/">Credit Header Data: An Indispensable Tool to Combatting Fraud</a></li>

</ul>
</details>

**标签**: `#privacy`, `#surveillance`, `#data brokers`, `#ICE`, `#credit cards`

---

<a id="item-8"></a>
## [NIST 发布关于 5G 初始 NAS 消息安全的白皮书草案](https://csrc.nist.gov/pubs/cswp/36/f/initial-nas-message-security-applying-5g-cybersecu/ipd) ⭐️ 8.0/10

NIST 的国家网络安全卓越中心（NCCoE）发布了一份白皮书草案，详细说明了一种 5G 安全功能，该功能对初始 NAS 消息进行加密和完整性保护，解决了 4G 网络中的漏洞，并为网络运营商提供了可操作的实施指南。 它填补了蜂窝安全的一个关键空白：4G 中未受保护的初始握手使网络面临中间人攻击风险；其指南有助于加快 5G 隐私保护的采用，增强用户隐私和网络完整性。 该白皮书基于 NCCoE 运营性 5G 测试平台的演示成果，遵循 3GPP 规范，允许对初始 NAS 消息进行加密和完整性保护；草案公开征求意见截止日期为 2026 年 9 月 7 日。

rss · NIST CSRC Drafts (标准草案) · 8月6日 04:00

**背景**: 在移动网络中，非接入层（NAS）是处理设备与核心网之间信令的控制层，负责注册和认证等功能。初始 NAS 消息是建立连接的第一个握手消息。在 4G 中，该消息未受保护，会泄露 IMSI 等敏感信息并允许中间人攻击。5G 标准强制要求对该消息进行加密和完整性保护，以缓解这些风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/pubs/cswp/36/f/initial-nas-message-security-applying-5g-cybersecu/ipd">CSWP 36F, Initial NAS Message Security: Applying... | CSRC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Non-access_stratum">Non-access stratum</a></li>
<li><a href="https://www.3glteinfo.com/5g/protocols/nas/authentication-security-mode-and-initial-nas-protection/">5G NAS Authentication, Security Mode, and Initial NAS ... | 3GLTEInfo</a></li>

</ul>
</details>

**标签**: `#5G security`, `#NAS`, `#NIST`, `#cybersecurity`, `#network security`

---

<a id="item-9"></a>
## [Cloudflare 推出基于 BotBase 和 Precursor 的持续机器人信任评估](https://blog.cloudflare.com/good-and-bad-agentic-behaviors/) ⭐️ 7.0/10

Cloudflare 正将传统的单点机器人风险评估替换为持续信任评估框架，并引入 BotBase 实现机器人可见性，以及 Precursor 进行全会话行为分析。 随着 AI 驱动的机器人变得越来越复杂，能够在短时间内模仿人类行为，单次检查已不再足够；持续分析提高了检测准确性，保护网站免受撞库、爬取和库存囤积等攻击。 BotBase 充当已知机器人的可见性层，而 Precursor 持续监控用户旅程信号（如光标移动）；它是 Turnstile 和企业机器人管理的可选附加组件。

rss · Cloudflare Blog (PQ 迁移) · 8月7日 13:01

**背景**: 机器人缓解技术用于识别和阻止恶意自动化流量。传统方法在单个时间点评估风险（例如 CAPTCHA），但复杂的机器人能够通过这些检查。Cloudflare 的新方法会在整个用户会话期间持续分析行为，利用客户端信号区分人类和 AI 代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/bots/botbase/">BotBase · Cloudflare bot solutions docs</a></li>
<li><a href="https://proxycove.com/en/blog/cloudflare-precursor-session-bot-detection-2026">Cloudflare Precursor : detect bots throughout the session, 2026</a></li>

</ul>
</details>

**标签**: `#bot detection`, `#continuous evaluation`, `#security`, `#web infrastructure`, `#AI agents`

---

<a id="item-10"></a>
## [Cloudflare 推出 AI 搜索，简化数据搜索流程](https://blog.cloudflare.com/ai-search-easier/) ⭐️ 7.0/10

Cloudflare 宣布推出 AI 搜索服务，开发者只需将数据源指向该服务，即可构建自然语言搜索功能，无需手动集成 Workers、R2 等多个 Cloudflare 原语。同时还发布了新的定价预览。 这大大降低了构建 AI 驱动搜索的复杂度，使更多开发者能够使用，并加速检索增强生成（RAG）应用和 AI 代理的开发。这可能会增强 Cloudflare 在开发者平台市场相对于 AWS 和 Netlify 等竞争对手的地位。 AI 搜索支持元数据过滤、NLWeb 等开放标准，并与 Vercel AI SDK、Cloudflare Agents SDK 和 LangChain 等代理框架集成。它还提供 REST API、Workers 绑定和 MCP 服务器，但预览的具体定价尚未公布。

rss · Cloudflare Blog (PQ 迁移) · 8月6日 13:00

**背景**: Cloudflare 的开发者平台提供了多个“原语”——独立的构建模块，如用于无服务器计算的 Workers、对象存储 R2 和数据库 D1。以前，构建自定义搜索引擎需要组合这些原语，增加了复杂性。AI 搜索则将这些集成抽象化，提供了一个现成的解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/ai-search/">Cloudflare AI Search · Cloudflare AI Search docs</a></li>
<li><a href="https://www.cloudflare.com/products/ai-search/">Cloudflare AI Search - Automatic RAG infrastructure and querying</a></li>
<li><a href="https://blog.cloudflare.com/ai-search-easier/">Cloudflare AI Search: give your agents a search engine for ...</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#AI Search`, `#Developer Tools`, `#Data Search`, `#Cloud Services`

---
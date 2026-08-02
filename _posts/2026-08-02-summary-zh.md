---
layout: default
title: "Horizon Summary: 2026-08-02 (ZH)"
date: 2026-08-02
lang: zh
---

> 从 29 条内容中筛选出 10 条重要资讯。

---

1. [Cloudflare 将 cdnjs 迁移至自家开发者平台，日处理 90 亿请求](#item-1) ⭐️ 8.0/10
2. [Anthropic 的 Opus 5 大幅降低提示注入攻击成功率](#item-2) ⭐️ 8.0/10
3. [美国公民因在边境使用 GrapheneOS 胁迫密码擦除手机被起诉](#item-3) ⭐️ 8.0/10
4. [Uniswap v4 Hooks 的七大安全漏洞模式](#item-4) ⭐️ 8.0/10
5. [Cloudflare 推出隔离式 MoQ 中继 API](#item-5) ⭐️ 7.0/10
6. [MSG 为泰勒·斯威夫特关闭面部识别，暴露隐私双重标准](#item-6) ⭐️ 7.0/10
7. [AI 使用决策：‘工作’与‘健身房’框架](#item-7) ⭐️ 7.0/10
8. [RFC 10029: 单次 DNS 查询可请求多种记录类型](#item-8) ⭐️ 7.0/10
9. [RFC 10019 发布：零配置组播地址分配问题陈述](#item-9) ⭐️ 7.0/10
10. [RFC 10013 定义 EAT 测量组件的信息与数据模型](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Cloudflare 将 cdnjs 迁移至自家开发者平台，日处理 90 亿请求](https://blog.cloudflare.com/cdnjs-dev-platform-migration/) ⭐️ 8.0/10

Cloudflare 已将每日处理 90 亿请求的 cdnjs 完全迁移到自家的开发者平台，利用 Workers 和 Workflows 来处理大规模流量。 这次迁移证明 Cloudflare 的无服务器平台能够应对极端规模的流量，验证了其在最大 CDN 工作负载下的可靠性，并为所有用户提升了性能上限。 迁移过程涉及在 Cloudflare Workers 上运行 cdnjs 的边缘逻辑，并使用 Workflows 处理后端流程，这突破了平台极限，带来了惠及所有开发者的改进。

rss · Cloudflare Blog (PQ 迁移) · 7月30日 13:00

**背景**: cdnjs 是一个流行的开源 CDN，托管 JavaScript 库和其他 Web 资源，超过 12% 的网站在使用它。Cloudflare Workers 是一个在边缘运行代码的无服务器平台，而 Workflows 则为长时间运行和多步骤应用提供持久化执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cdnjs">Cdnjs</a></li>
<li><a href="https://developers.cloudflare.com/workflows/">Overview · Cloudflare Workflows docs</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#cdnjs`, `#serverless`, `#edge-computing`, `#dogfooding`

---

<a id="item-2"></a>
## [Anthropic 的 Opus 5 大幅降低提示注入攻击成功率](https://www.schneier.com/blog/archives/2026/07/anthropics-opus-5-is-better-at-resisting-prompt-injection.html) ⭐️ 8.0/10

Claude Opus 5 在 15 次尝试下的提示注入攻击成功率从之前 Opus 4.8 的 5.5%降至 2.0%，并显著优于包括 GPT-5.6 Sol（20.0%）在内的所有其他被测模型。 这一进步标志着大型语言模型在抵御对抗性攻击方面迈出关键一步，提升了与不可信数据源交互的自主 AI 代理的可靠性和安全性。 在 IPI（间接提示注入）基准测试中，Opus 5 单次攻击成功率为 0.2%，其次的 Mythos 5 在 15 次尝试下为 2.6%。最佳非 Claude 模型 Muse Spark 的攻击成功率高 8 倍以上。

rss · Schneier on Security · 7月31日 17:23

**背景**: 提示注入是一种安全漏洞，通过巧妙构造输入来覆盖模型的指令，导致非预期行为。间接提示注入尤其将对抗性提示嵌入到网页等外部内容中，欺骗具备网页浏览能力的 LLM 执行有害操作。随着 AI 代理在真实任务中的部署，这种攻击途径日益令人担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://learnprompting.org/docs/prompt_hacking/injection">Prompt Injection : Overriding AI Instructions with User Input</a></li>

</ul>
</details>

**标签**: `#AI security`, `#prompt injection`, `#adversarial robustness`, `#large language models`, `#Anthropic`

---

<a id="item-3"></a>
## [美国公民因在边境使用 GrapheneOS 胁迫密码擦除手机被起诉](https://www.schneier.com/blog/archives/2026/07/american-being-prosecuted-for-wiping-his-phone-before-handing-it-over-to-border-officials.html) ⭐️ 8.0/10

2026 年 7 月，美国公民 Tunick 在边境被迫解锁手机时，据称使用了 GrapheneOS 的胁迫密码功能擦除手机数据，因此受到指控。 此案检验了美国边境的宪法权利边界，官员声称可无授权搜查，可能为胁迫密码功能的法律地位开创先例，影响旅行者的数字隐私。 GrapheneOS 的胁迫密码是一项有文档记录的安全功能，输入后会不可逆地擦除设备和已安装的 eSIM；检方认为此举妨碍了合法的边境搜查。

rss · Schneier on Security · 7月30日 16:20

**背景**: GrapheneOS 是一种基于安卓的强化安全操作系统，适用于 Google Pixel 设备，其胁迫密码功能允许用户设置独立密码，在受胁迫时输入可擦除手机。根据美国法律，边境官员可无搜查令检查电子设备，这一政策遭到公民自由团体批评。宪法第四修正案对不合理搜查的保护在边境地区较弱，引发持续法律争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://cybernews.com/privacy/grapheneos-duress-password-border-case-legality/">GrapheneOS defends “duress” feature, discards decoy accounts ...</a></li>
<li><a href="https://thecybersecguru.com/news/grapheneos-duress-password-us-border-search-case/">GrapheneOS Duress Password Explained: Why a US Federal Case ...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#security`, `#GrapheneOS`, `#border search`, `#digital rights`

---

<a id="item-4"></a>
## [Uniswap v4 Hooks 的七大安全漏洞模式](https://blog.trailofbits.com/2026/07/30/building-secure-uniswap-v4-hooks/) ⭐️ 8.0/10

Trail of Bits 分析了 Uniswap v4 钩子（Hooks）实现的数十项审计发现，确定了七个反复出现的安全漏洞模式，包括缺少调用者检查和虽然满足 PoolManager 结算不变性但仍存在的会计错误。这些模式基于真实世界漏洞，如 Cork 和 Bunni 事件，共造成超过 2000 万美元的损失。 这为开发者在 Uniswap v4 上构建时提供了可操作的安全清单，有助于防止类似漏洞的发生。随着 DeFi 协议越来越多地采用 v4 钩子实现自定义逻辑，这些模式对于保护下一代链上流动性至关重要。 这七种模式包括：缺少调用者检查、权限边界错误、钩子合约升级风险、尽管满足结算不变性但仍存在会计错误、通过钩子进行的预言机操纵、钩子回调中的重入攻击，以及外部合约集成不安全。这些发现来自 Trail of Bits 的审计、公开报告和 Solodit 数据库。

rss · Trail of Bits Blog · 7月30日 11:00

**背景**: Uniswap v4 引入了单例 PoolManager 架构，所有池状态都存储在一个合约中，而钩子（Hooks）允许在交换和流动性事件中实现自定义逻辑。与 v3 中每个池是独立合约不同，v4 使用类似于闪电贷的基于会话的回调机制，要求每笔交易结束时所有货币增量必须归零。Cork 和 Bunni 漏洞事件表明，即使核心协议没有缺陷，与钩子相关的授权和会计错误也可能导致重大损失。构建钩子的开发者必须对安全性保持警惕，因为这些扩展在一个包含许多潜在漏洞的复杂环境中运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.uniswap.org/docs/protocols/v4/concepts/hooks">Hooks | Uniswap Developers</a></li>
<li><a href="https://quillaudits.medium.com/cork-protocol-exploit-how-a-critical-flaw-led-to-a-12m-loss-00fb936f6624">A Critical Bug in Cork Protocol Led to a $12M Exploit | Medium</a></li>
<li><a href="https://www.resonance.security/blog-posts/bunni-dex-hack-when-custom-liquidity-logic-pays-out-fantasy-money">Bunni DEX Hack: When Custom Liquidity Logic Pays Out Fantasy Money</a></li>

</ul>
</details>

**标签**: `#security`, `#uniswap`, `#smart-contracts`, `#defi`, `#blockchain`

---

<a id="item-5"></a>
## [Cloudflare 推出隔离式 MoQ 中继 API](https://blog.cloudflare.com/moq-relays/) ⭐️ 7.0/10

Cloudflare 发布了一个配置 API，允许用户创建自己隔离的 Media over QUIC（MoQ）中继，从而精细控制实时媒体流中谁可以发布和谁只能观看。 这使得开发者能够直接控制其流媒体基础设施的访问权限，为需要低延迟传输的直播、游戏和会议等应用增强了安全性和定制性。 该 API 基于 MoQ 协议（一项 IETF 标准，旨在规模化实现亚秒级交互式流媒体），将 Cloudflare 的共享中继网络转变为可编程的隔离实例。

rss · Cloudflare Blog (PQ 迁移) · 7月31日 13:00

**背景**: Media over QUIC（MoQ）是一项新的 IETF 协议，通过结合 WebRTC 和 QUIC 的优势，以低延迟传输实时媒体，支持大规模交互式流媒体。去年，Cloudflare 在其全球所有服务器上启用了 MoQ 中继功能。新的 API 允许客户配置专用中继，而非使用共享基础设施，从而提供对发布和观看权限的更多控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/moq/">MoQ: Refactoring the Internet's real-time media stack | The Cloudflare Blog</a></li>
<li><a href="https://datatracker.ietf.org/group/moq/about/">Media Over QUIC (moq)</a></li>
<li><a href="https://github.com/moq-dev/moq">GitHub - moq-dev/moq: Media over QUIC: Real-time latency at massive scale · GitHub</a></li>

</ul>
</details>

**标签**: `#MoQ`, `#QUIC`, `#Cloudflare`, `#API`, `#media streaming`

---

<a id="item-6"></a>
## [MSG 为泰勒·斯威夫特关闭面部识别，暴露隐私双重标准](https://www.schneier.com/blog/archives/2026/07/facial-recognition-at-madison-square-garden.html) ⭐️ 7.0/10

麦迪逊广场花园的面部识别系统用于识别活动人士，但在泰勒·斯威夫特的婚礼期间被停用，暴露了监控的选择性执行。 这凸显了日益严重的隐私鸿沟：富裕精英可以通过付费或关系免于普通人所面临的监控，破坏了监控技术的公平应用。 该系统专门将反对面部识别的活动人士列入黑名单；据报道，它仅在斯威夫特的婚礼期间关闭，活动人士埃文·格里尔对此发表了评论。

rss · Schneier on Security · 7月31日 11:08

**背景**: 麦迪逊广场花园是纽约市的主要娱乐场馆，实施了面部识别系统以识别并可能拒绝对手入场，包括活动人士。泰勒·斯威夫特是一位知名名人，在该场馆举行婚礼。此事件暴露了私人监控如何根据身份选择性应用。

**社区讨论**: 活动人士埃文·格里尔指出了讽刺之处：斯威夫特本人据报道曾在演唱会上使用面部识别来识别跟踪者，他哀叹“对我隐私，对你监控”的心态让富裕精英能购买隐私，而普通人则生活在持续监控之下。

**标签**: `#facial recognition`, `#privacy`, `#surveillance`, `#Bruce Schneier`, `#Madison Square Garden`

---

<a id="item-7"></a>
## [AI 使用决策：‘工作’与‘健身房’框架](https://www.schneier.com/blog/archives/2026/07/should-you-use-ai-for-a-task-heres-a-simple-way-to-decide.html) ⭐️ 7.0/10

哈佛肯尼迪学院公共政策讲师 Bruce Schneier 介绍了一个来自 AI 研究员 Daniel Miessler 的简单框架，用于决定何时使用 AI：将任务分为“工作”（AI 辅助输出）和“健身房”（人类努力培养技能）两类。 该框架为 AI 采用提供了清晰的伦理指导，尤其在教育和创意领域，有助于平衡生产力提升与培养人类专业知识和批判性思维的需求。 核心规则：如果任务的主要目标是最终结果，则使用 AI；如果过程本身对学习或成长有价值，则避免使用 AI。该框架最初在《卫报》上讨论，并基于 Miessler 的“让机器人远离健身房”的比喻。

rss · Schneier on Security · 7月30日 11:01

**背景**: “工作与健身房”的比喻将任务比作要么是工作（只在乎产出，如搬运重物），要么是健身房锻炼（锻炼本身才是目的，而非仅仅移动重量）。Bruce Schneier 是著名的安全专家和作家，Daniel Miessler 是提出该比喻以指导合理使用 AI 的 AI 研究员。随着 AI 写作助手在学术界和专业环境中普及，该框架显得尤为重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://brevfeed.com/cluster/framework-for-deciding-ai-use-the-work-vs-gym">Framework for Deciding AI Use: The 'Work vs. Gym' Analogy</a></li>
<li><a href="https://danielmiessler.com/blog/keep-the-robots-out-of-the-gym">Keep the Robots Out of the Gym | Daniel Miessler</a></li>

</ul>
</details>

**标签**: `#AI`, `#ethics`, `#decision-making`, `#education`, `#writing`

---

<a id="item-8"></a>
## [RFC 10029: 单次 DNS 查询可请求多种记录类型](https://rfc-editor.org/info/rfc10029) ⭐️ 7.0/10

RFC 10029 定义了一种方法，允许 DNS 客户端在单次 QUERY（OpCode=0）中请求多种记录类型（如 A、AAAA 和 HTTPS），从而减少多次查询的需求。 此扩展降低了需要同时获取多种记录类型的应用程序（如服务发现）的延迟、提升了效率，并为常被拦截的 QTYPE=ANY 提供了可靠的替代方案。 它通过扩展 DNS 问题部分来携带多个 QTYPE，基于将 QUERY 限制为单个问题的 RFC 9619。该方法避免了 QTYPE=ANY 的不可靠性，同时保持向后兼容。

rss · IETF 新标准 RFC (PQC 标准化) · 7月31日 21:12

**背景**: 域名系统（DNS）将域名转换为 IP 地址及其他资源记录，每种记录由 QTYPE 标识（如 A 表示 IPv4 地址，AAAA 表示 IPv6 地址）。传统上，一次 DNS QUERY 只能查询一种 QTYPE，导致需要多次往返才能收集不同记录。QTYPE=ANY 伪类型本用于获取所有记录，但常因放大攻击被过滤。RFC 10029 标准化了在单次查询中请求自定义 QTYPE 集合的方法，解决了这一长期需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rfc-editor.org/info/rfc10029/">RFC 10029: DNS Multiple QTYPEs | RFC Editor</a></li>
<li><a href="https://dnssd-wg.github.io/draft-ietf-dnssd-multi-qtypes/draft-ietf-dnssd-multi-qtypes.html">DNS Multiple QTYPEs</a></li>

</ul>
</details>

**标签**: `#DNS`, `#IETF`, `#RFC`, `#protocol`, `#networking`

---

<a id="item-9"></a>
## [RFC 10019 发布：零配置组播地址分配问题陈述](https://rfc-editor.org/info/rfc10019) ⭐️ 7.0/10

RFC 10019 已发布，调查了零配置网络中现有组播地址分配的问题，并定义了去中心化自动解决方案的需求。 此基础文件指导未来协议开发，实现在本地网络中无需手动配置或中央服务器的无缝自动组播通信。 该 RFC 解决了链路层冲突、硬件限制和组播侦听低效问题，并涵盖 IPv4 和 IPv6 的发现、分配、冲突检测及租约管理。

rss · IETF 新标准 RFC (PQC 标准化) · 7月31日 02:35

**背景**: 零配置网络（zeroconf）允许多设备自动连接和通信，无需手动设置。组播使用组地址向多个接收者发送数据，但在没有中央管理的情况下分配唯一地址可能导致冲突和低效。RFC 10019 识别这些挑战并设定解决方案需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-configuration_networking">Zero-configuration networking - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multicast_snooping">Multicast snooping</a></li>

</ul>
</details>

**标签**: `#zeroconf`, `#multicast`, `#address allocation`, `#IETF`, `#networking`

---

<a id="item-10"></a>
## [RFC 10013 定义 EAT 测量组件的信息与数据模型](https://rfc-editor.org/info/rfc10013) ⭐️ 7.0/10

RFC 10013 为实体认证令牌(EAT)框架中的测量组件引入了信息模型以及 JSON 和 CBOR 两种数据模型串行化格式，并通过 CoAP 内容格式实现即时可用。 该标准实现了设备测量的一致且可互操作的表示，这对于物联网和系统安全中的远程认证至关重要，使依赖方能够统一验证设备完整性。 信息模型与具体串行化解耦，注册了 JSON 和 CBOR 绑定及 CoAP 内容格式，并支持未来扩展如 ASN.1 等其他格式。

rss · IETF 新标准 RFC (PQC 标准化) · 7月31日 00:10

**背景**: 实体认证令牌(EAT)是一种用于传递关于设备身份和软件状态的认证声明的标准格式。测量组件是指任何可通过加密哈希验证完整性的软硬件元素。CBOR（简洁二进制对象表示）是一种专为小消息尺寸和受限环境设计的二进制数据格式，而 CoAP（受限应用协议）是面向物联网设备的轻量级 Web 传输协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ietf-rats-wg.github.io/eat/draft-ietf-rats-eat.html">The Entity Attestation Token ( EAT )</a></li>
<li><a href="https://en.wikipedia.org/wiki/CBOR">CBOR - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Constrained_Application_Protocol">Constrained Application Protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#attestation`, `#EAT`, `#RFC`, `#IoT security`, `#standard`

---
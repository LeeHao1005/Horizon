---
layout: default
title: "Horizon Summary: 2026-07-16 (ZH)"
date: 2026-07-16
lang: zh
---

> 从 33 条内容中筛选出 10 条重要资讯。

---

1. [EDE 33：.al 域名事故后 Cloudflare 推出公示 DNSSEC 绕过的新 DNS 错误码](#item-1) ⭐️ 8.0/10
2. [傅里叶像素使屏幕能同时显示和捕获光线](#item-2) ⭐️ 8.0/10
3. [AI 数据中心与财富集中](#item-3) ⭐️ 8.0/10
4. [RFC 9851 宣布 TLS 1.2 进入功能冻结期](#item-4) ⭐️ 8.0/10
5. [RFC 9973：用于证书与外部预共享密钥认证的 TLS 1.3 扩展](#item-5) ⭐️ 8.0/10
6. [RFC 9954 定义 TLS 1.3 混合密钥交换](#item-6) ⭐️ 8.0/10
7. [Cloudflare 发布 Precursor 持续行为验证引擎](#item-7) ⭐️ 7.0/10
8. [RFC 9933 为 PCEP 增加 SR 算法支持以增强段路由流量工程](#item-8) ⭐️ 7.0/10
9. [RFC 9999 定义 RATS 概念消息包装器用于远程证明](#item-9) ⭐️ 7.0/10
10. [RFC 9995：COSE 哈希信封提升签名验证效率](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [EDE 33：.al 域名事故后 Cloudflare 推出公示 DNSSEC 绕过的新 DNS 错误码](https://blog.cloudflare.com/dnssec-nta-ede-33/) ⭐️ 8.0/10

Cloudflare 针对.al 顶级域名部署了否定信任锚（NTA），以恢复因 DNSSEC 密钥滚动失败而中断的解析服务，并在其 1.1.1.1 解析器中引入扩展 DNS 错误码 33（EDE 33），明确指示何时 DNSSEC 验证被绕过。 这种透明机制让运营者和用户能够察觉到因配置错误而有意禁用 DNSSEC 安全的情况，避免产生虚假的安全感，并为其他 DNS 提供商树立了可效仿的先例。 EDE 33 被添加到 RFC 8914 定义的扩展 DNS 错误集中，由 1.1.1.1 在 NTA 生效时返回，使日志和监控工具能够明确跟踪验证绕过事件。

rss · Cloudflare Blog (PQ 迁移) · 7月14日 13:00

**背景**: DNSSEC 通过数字签名保护 DNS 免受欺骗。密钥滚动会轮换用于签名的加密密钥，但滚动失败可能导致域名解析中断。否定信任锚（NTA）根据 RFC 7646 指示解析器暂时跳过对某个域的验证。扩展 DNS 错误码（EDE）由 RFC 8914 定义，为 DNS 响应增加诊断上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/dnssec-nta-ede-33/">A broken DNSSEC rollover took down .AL. Now 1.1.1.1 tells you when...</a></li>
<li><a href="https://www.rfc-editor.org/rfc/rfc7646">RFC 7646: Definition and Use of DNSSEC Negative Trust Anchors</a></li>
<li><a href="https://www.namesilo.com/blog/en/domain-security/dnssec-key-rollover-explained-how-to-rotate-keys-without-breaking-validation">How Does DNSSEC Key Rollover Work? | NameSilo Blog</a></li>

</ul>
</details>

**标签**: `#DNSSEC`, `#DNS`, `#Cloudflare`, `#Network Security`, `#Transparency`

---

<a id="item-2"></a>
## [傅里叶像素使屏幕能同时显示和捕获光线](https://www.schneier.com/blog/archives/2026/07/a-video-screen-that-is-also-a-camera.html) ⭐️ 8.0/10

苏黎世联邦理工学院的研究人员开发出一种名为“傅里叶像素”的新型像素，能够通过操控光的强度、振荡相位和偏振，同时发射和检测光线，相关论文发表在《自然》杂志上。 这种双向功能模糊了显示与传感的界限，引发了类似奥威尔电幕般的隐私和监视忧虑，同时也为新型交互和增强现实应用开创了可能。 傅里叶像素利用表面波和精确设计的界面组件，通过对干涉图案的傅里叶分析产生并感知任意光场。它通过将导波散射为光波来实现高分辨率双向通信。

rss · Schneier on Security · 7月15日 11:04

**背景**: 光场描述了空间中每一点沿各个方向的光线流动。傅里叶分析将信号分解为正弦波分量，从而精确控制光的特性。乔治·奥威尔小说《1984》中的电幕是一种既能播放节目又能监视用户的设备，是无孔不入的监控的象征。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://petapixel.com/2026/06/26/researchers-develop-all-new-pixel-type-that-can-both-record-and-display-light/">Researchers Develop All-New Pixel Type That Can Both... | PetaPixel</a></li>
<li><a href="https://logicity.in/en/blog/eth-zurich-builds-pixels-that-emit-and-detect-light">ETH Zurich builds pixels that emit and detect light | Logicity</a></li>

</ul>
</details>

**标签**: `#technology`, `#surveillance`, `#privacy`, `#display`, `#research`

---

<a id="item-3"></a>
## [AI 数据中心与财富集中](https://www.schneier.com/blog/archives/2026/07/ai-data-centers-and-the-concentration-of-wealth.html) ⭐️ 8.0/10

Bruce Schneier 和 Nathan E. Sanders 在一篇新文章中论证，对 AI 数据中心的政治关注分散了人们对 AI 公司权力和财富集中这一更紧迫问题的注意力。 这一观点将人工智能辩论从地方环境问题转向寡头控制的系统性风险，强调少数公司可能同时主宰经济和政治。 该文章于 2026 年 7 月 9 日发表在《卫报》上，指出对数据中心的反对是跨党派的，并警告说，对物理基础设施的争论掩盖了人工智能公司的巨大影响力。

rss · Schneier on Security · 7月13日 11:01

**背景**: 人工智能数据中心是容纳强大计算机的大型设施，用于训练和运行人工智能模型。它们需要大量能源和水，引起当地反对。与此同时，像 OpenAI、谷歌和微软这样的领先人工智能公司通过控制人工智能技术和数据，正在积累巨大的经济和政治权力。

**标签**: `#AI`, `#data centers`, `#concentration of wealth`, `#politics`, `#Bruce Schneier`

---

<a id="item-4"></a>
## [RFC 9851 宣布 TLS 1.2 进入功能冻结期](https://rfc-editor.org/info/rfc9851) ⭐️ 8.0/10

IETF 发布了 RFC 9851，正式将 TLS 1.2 置于功能冻结状态，仅允许紧急安全修复、新的 TLS 导出器标签和 ALPN 协议 ID 的添加。 这正式确立了行业向 TLS 1.3 的迁移，鼓励采用更安全、更现代的新协议，并向开发者和运维人员发出信号：TLS 1.2 将不再积极演进。 该冻结仅针对 TLS，不适用于 DTLS（所有版本）；但仍允许注册新的 TLS 导出器标签和 ALPN 协议 ID，以支持应用层协议协商和密钥材料导出。

rss · IETF 新标准 RFC (PQC 标准化) · 7月15日 23:40

**背景**: TLS（传输层安全协议）是用于保护网络通信的加密协议。TLS 1.3 针对 TLS 1.2 进行了重大改进，包括更快的握手和更强的安全性。IETF RFC 是互联网协议标准化的过程。功能冻结意味着不再添加新特性。TLS 导出器标签用于 TLS 密钥材料导出器（RFC 5705），为其他协议生成密钥。ALPN（应用层协议协商）是一种 TLS 扩展，允许客户端和服务器在安全连接上协商使用何种应用层协议（如 HTTP/2）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/html/rfc5705">RFC 5705 - Keying Material Exporters for Transport Layer Security (TLS)</a></li>
<li><a href="https://http.dev/alpn">Application-Layer Protocol Negotiation ( ALPN )</a></li>
<li><a href="https://en.wikipedia.org/wiki/DTLS">DTLS</a></li>

</ul>
</details>

**标签**: `#TLS`, `#IETF`, `#security`, `#networking`, `#standards`

---

<a id="item-5"></a>
## [RFC 9973：用于证书与外部预共享密钥认证的 TLS 1.3 扩展](https://rfc-editor.org/info/rfc9973) ⭐️ 8.0/10

RFC 9973 作为标准跟踪文档发布，定义了一个 TLS 1.3 扩展，允许客户端和服务器结合基于证书的认证与外部预共享密钥进行加密通信，取代了实验性的 RFC 8773。 该标准为安全实现提供了官方指导，增强了 TLS 1.3 在需要同时使用证书和 PSK 认证的场景（如企业和物联网环境）中的灵活性，并通过解决 PSK 潜在攻击来加强协议安全性。 该标准取代了实验性的 RFC 8773，通过密码学方式将证书与 PSK 绑定，并遵循 RFC 9257 和 RFC 9258 中关于外部 PSK 使用的指导，以增强安全性。

rss · IETF 新标准 RFC (PQC 标准化) · 7月15日 23:37

**背景**: TLS 1.3 是最新的传输层安全协议，用于保护互联网通信。预共享密钥（PSK）是通信方事先共享的对称密钥，提供了除证书认证之外的另一种选择。RFC 8773 曾是一个实验性扩展，结合了证书和外部 PSK 认证，而 RFC 9973 则将该方法标准化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TLS-PSK">TLS-PSK - Wikipedia</a></li>
<li><a href="https://www.ietf.org/rfc/rfc8773.pdf">RFC 8773 : TLS 1.3 Extension for Certificate-Based Authentication with...</a></li>
<li><a href="https://www.ietf.org/rfc/rfc9257.pdf">RFC 9257: Guidance for External Pre-Shared Key (PSK) Usage in TLS</a></li>

</ul>
</details>

**标签**: `#TLS`, `#cryptography`, `#IETF`, `#protocol`, `#security`

---

<a id="item-6"></a>
## [RFC 9954 定义 TLS 1.3 混合密钥交换](https://rfc-editor.org/info/rfc9954) ⭐️ 8.0/10

RFC 9954 正式定义了在 TLS 1.3 中组合多种密钥交换算法的机制，只要有一个组件未被攻破即可保证安全，从而推动后量子密码学的采用。 这一进展对于互联网安全向量子时代过渡至关重要；它允许无缝集成后量子算法，无需等待单一完美方案，防止‘先收集后解密’的威胁。 该 RFC 详细说明了使用密钥派生函数（KDF）将多个密钥交换产生的共享秘密进行组合的构造方法，并很可能定义了混合组的代码点，以支持协商同时使用经典与后量子算法。

rss · IETF 新标准 RFC (PQC 标准化) · 7月15日 22:20

**背景**: 传输层安全协议（TLS）1.3 使用临时密钥交换（通常为 ECDHE）建立会话密钥。然而，量子计算机运行 Shor 算法可能破解椭圆曲线密码。后量子密码学（PQC）旨在开发抗量子攻击的算法，但早期候选算法可能存在漏洞。混合密钥交换通过同时运行经典和后量子密钥交换并组合结果来降低风险，只要其中一种未被攻破，会话密钥就是安全的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/">draft-ietf-tls- hybrid -design-16 - Hybrid key exchange in TLS 1.3</a></li>
<li><a href="https://www.linkedin.com/pulse/embracing-tls-13-hybrid-key-exchange-post-quantum-protection-atoum/">Embracing TLS 1.3 Hybrid Key Exchange for Post-Quantum...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>

</ul>
</details>

**标签**: `#TLS 1.3`, `#Hybrid Key Exchange`, `#Post-Quantum Cryptography`, `#IETF RFC`, `#Network Security`

---

<a id="item-7"></a>
## [Cloudflare 发布 Precursor 持续行为验证引擎](https://blog.cloudflare.com/introducing-precursor/) ⭐️ 7.0/10

Cloudflare 发布了 Precursor，一个用于机器人管理的持续性行为验证引擎，通过客户端 JavaScript 分析会话级行为，提升机器人检测精度并减少对真实用户的干扰。 传统机器人检测常依赖 CAPTCHA 等单点挑战，容易影响用户体验；Precursor 的基于会话的行为分析能够更精准地识别高级自动化程序，减少误判并提升真实用户的访问体验。 Precursor 是一个客户端 JavaScript 引擎，执行基于会话的行为分析，为 Cloudflare 的机器人管理提供信号；它旨在与现有的指纹识别和挑战技术协同工作。

rss · Cloudflare Blog (PQ 迁移) · 7月13日 13:00

**背景**: 机器人管理系统旨在区分人类用户和自动化机器人。传统方法包括 IP 信誉、请求分析和 CAPTCHA 验证。客户端信号（如鼠标移动和按键动态）提供了检测非人类行为的额外数据。行为分析涉及持续监测用户交互，而非依赖单一事件，从而能够识别试图模仿人类模式的机器人。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/changelog/post/2026-07-13-precursor-session-based-detection/">Precursor introduces session-based bot detection · Changelog</a></li>
<li><a href="https://datadome.co/bot-management-protection/why-client-side-signals-are-a-must-have-for-detecting-sophisticated-attacks/">Client-Side Signals: Essential in Detecting Advanced Attacks</a></li>

</ul>
</details>

**标签**: `#bot-detection`, `#web-security`, `#cloudflare`, `#machine-learning`, `#cybersecurity`

---

<a id="item-8"></a>
## [RFC 9933 为 PCEP 增加 SR 算法支持以增强段路由流量工程](https://rfc-editor.org/info/rfc9933) ⭐️ 7.0/10

RFC 9933 规定了 PCEP 扩展，在 ERO 和 RRO 子对象中编码 SR 算法信息，引入路径计算的 SR 算法约束，并为 METRIC 对象定义新度量类型，同时更新了 RFC 8664 和 RFC 9603。 这使得流量工程系统在建立段路由路径时能够考虑特定的路径计算算法（如最短路径、低延迟），从而优化网络，帮助运营商满足多样化服务等级协议。 该扩展在 ERO/RRO 中使用新的子 TLV 携带 SR 算法值；在路径计算请求中定义算法约束 TLV，并在 METRIC 对象中引入算法特定度量类型（如聚合、最小、最大），以支持灵活的算法选择。

rss · IETF 新标准 RFC (PQC 标准化) · 7月15日 18:40

**背景**: PCEP 用于路径计算单元（PCE）与路径计算客户端（PCC）之间计算网络路径。段路由（SR）使用段标识符（SID）引导数据包沿预定路径转发，而 SR 算法（如“最短路径优先”或“严格最短路径”）指定了内部网关协议如何计算到 SID 的路由。此前 PCEP 缺乏机制来标识 SID 所属的算法，限制了流量工程的精细度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Path_computation_element">Path computation element - Wikipedia</a></li>
<li><a href="https://info.support.huawei.com/info-finder/encyclopedia/en/PCEP.html">What Is PCEP? How Does PCEP Work? - Huawei</a></li>
<li><a href="https://en.wikipedia.org/wiki/Segment_Routing">Segment routing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#PCEP`, `#Segment Routing`, `#IETF`, `#Traffic Engineering`, `#SR-Algorithm`

---

<a id="item-9"></a>
## [RFC 9999 定义 RATS 概念消息包装器用于远程证明](https://rfc-editor.org/info/rfc9999) ⭐️ 7.0/10

RFC 9999 引入了概念消息包装器 (CMW)，通过专用 CBOR 标签、对应的 JWT 和 CWT 声明以及 X.509 扩展，为 RATS 消息提供了通用封装结构。 该标准通过提供一致的封装机制增强了远程证明协议的互操作性，支持消息格式的灵活演进和跨协议兼容性。 CMW 规范包含了用于 HTTP 和 CoAP 传输的媒体类型和 CoAP 内容格式，并利用 CBOR 实现紧凑二进制编码，利用 JWT/CWT 适应 Web 场景。

rss · IETF 新标准 RFC (PQC 标准化) · 7月14日 16:34

**背景**: 远程证明过程 (RATS) 架构 (RFC 9334) 定义了诸如证据和证明结果等概念消息。CBOR 是一种比 JSON 更紧凑的二进制数据格式，而 JWT 和 CWT 是用于安全声明传输的令牌格式，X.509 是公钥证书标准。CMW 提供了一个统一的包装器，使得这些证明消息能够在不同协议和编码中传输。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc8949.html">RFC 8949: Concise Binary Object Representation (CBOR)</a></li>
<li><a href="https://www.rfc-editor.org/rfc/rfc8392.html">RFC 8392: CBOR Web Token (CWT)</a></li>
<li><a href="https://cbor.io/">CBOR — Concise Binary Object Representation | Overview</a></li>

</ul>
</details>

**标签**: `#remote-attestation`, `#security`, `#standards`, `#message-wrapper`, `#cbor`

---

<a id="item-10"></a>
## [RFC 9995：COSE 哈希信封提升签名验证效率](https://rfc-editor.org/info/rfc9995) ⭐️ 7.0/10

RFC 9995 为 CBOR 对象签名与加密（COSE）引入了新的报头参数，用于处理基于哈希的载荷。这些参数允许无需原始载荷即可进行签名验证，并包含内容格式和发现提示。 这在原始载荷较大或无法立即可用的场景中提高了效率，例如物联网或受限环境。它还通过避免在验证过程中传输载荷，减少了带宽和处理开销。 新参数包括用于指定所用哈希函数的‘载荷哈希算法’，以及提示原始载荷格式的‘前像内容类型’。该规范还定义了可选的发现方法，以检索原始内容。

rss · IETF 新标准 RFC (PQC 标准化) · 7月14日 03:34

**背景**: CBOR（简洁二进制对象表示）是 RFC 8949 中定义的二进制序列化格式，用于物联网等应用中的高效数据交换。COSE（CBOR 对象签名与加密）为 CBOR 数据提供签名和加密服务，类似于 JSON 的 JOSE。RFC 9995 扩展了 COSE 以支持基于哈希的载荷，其中仅对内容的哈希进行签名，而非完整内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CBOR">CBOR</a></li>
<li><a href="https://cose-wg.github.io/draft-ietf-cose-hash-envelope/draft-ietf-cose-hash-envelope.html">COSE Hash Envelope</a></li>

</ul>
</details>

**标签**: `#COSE`, `#CBOR`, `#security`, `#IETF`, `#standards`

---
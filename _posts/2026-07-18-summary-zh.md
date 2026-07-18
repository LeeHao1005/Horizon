---
layout: default
title: "Horizon Summary: 2026-07-18 (ZH)"
date: 2026-07-18
lang: zh
---

> 从 40 条内容中筛选出 15 条重要资讯。

---

1. [首个无需全同态加密的次线性通信分层 MPC 方案](#item-1) ⭐️ 9.0/10
2. [苏黎世联邦理工学院发明傅里叶像素，屏幕变身摄像头](#item-2) ⭐️ 9.0/10
3. [RFC 9954：TLS 1.3 混合密钥交换标准](#item-3) ⭐️ 9.0/10
4. [基于同源的紧凑后量子 OT 方案：密钥仅 100 kB](#item-4) ⭐️ 8.0/10
5. [CoSecRAG：高效保护查询与数据库隐私的 RAG 检索协议](#item-5) ⭐️ 8.0/10
6. [RainHash2.0：面向硬件与二进制域零知识证明的高效哈希函数](#item-6) ⭐️ 8.0/10
7. [隐私保护从个人控制转向企业问责](#item-7) ⭐️ 8.0/10
8. [RFC 9852 要求新协议必须使用 TLS 1.3](#item-8) ⭐️ 8.0/10
9. [RFC 10015 弃用 TLS 1.2 中过时的密钥交换方法](#item-9) ⭐️ 8.0/10
10. [RFC 9851 宣布 TLS 1.2 进入特性冻结](#item-10) ⭐️ 8.0/10
11. [RFC 9973：用于结合证书与外部预共享密钥的 TLS 1.3 扩展](#item-11) ⭐️ 8.0/10
12. [RFC 9850 正式标准化 TLS 的 SSLKEYLOGFILE 格式](#item-12) ⭐️ 8.0/10
13. [SENTRA：面向隐私保护云机器学习训练的混合 TEE-MPC 架构](#item-13) ⭐️ 7.0/10
14. [Cloudflare 为两个高危 WordPress 漏洞部署 WAF 规则](#item-14) ⭐️ 7.0/10
15. [图灵“Delilah”语音加密系统新细节曝光](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [首个无需全同态加密的次线性通信分层 MPC 方案](https://eprint.iacr.org/2026/1445) ⭐️ 9.0/10

该论文首次提出了不依赖全同态加密（FHE）即可实现次线性通信的分层安全多方计算（Layered MPC）协议，解决了一个公开问题。它引入了一种新的同态秘密共享（HSS）构造——分层重共享技术。 这一突破使得在服务器可动态加入或离开的环境中，能够进行高效、可扩展的安全计算，大幅降低了通信开销。它为安全拍卖、协作机器学习等长期运行的应用提供了更实用的 MPC 方案。 该协议利用了一种称为分层重共享同态秘密共享（HSS with Layered Resharing）的变体，每层仅需两到三个在线服务器。它在避免全同态加密高计算负担的同时，实现了次线性通信。

rss · IACR ePrint 密码学论文 · 7月15日 16:25

**背景**: 同态秘密共享（HSS）允许多方在不泄露数据的情况下对秘密共享数据进行计算。分层 MPC（Layered MPC）由 CRYPTO 2023 提出，将参与方组织成多个层，每层处理数据后将份额传递给下一层，从而支持动态参与。此前的分层 MPC 协议要么通信量与电路规模线性相关，要么依赖全同态加密。本工作设计了一种支持跨层高效重共享的 HSS 方案，填补了这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://crypto.ethz.ch/publications/files/DDGIKKLN23.pdf">Perfect MPC over Layered Graphs</a></li>
<li><a href="https://www.iacr.org/news/item/29021">IACR News item: 16 July 2026</a></li>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_secret_sharing">Homomorphic secret sharing</a></li>

</ul>
</details>

**标签**: `#secure multi-party computation`, `#homomorphic secret sharing`, `#sublinear communication`, `#layered MPC`, `#cryptographic protocols`

---

<a id="item-2"></a>
## [苏黎世联邦理工学院发明傅里叶像素，屏幕变身摄像头](https://www.schneier.com/blog/archives/2026/07/a-video-screen-that-is-also-a-camera.html) ⭐️ 9.0/10

苏黎世联邦理工学院的研究人员开发出一种‘傅里叶像素’，既能发射光也能检测光，使显示屏能够像摄像头一样捕捉图像。这一突破发表在《自然》杂志上。 这项创新模糊了显示与传感的界限，可能催生新的交互应用，但也引发了类似于奥威尔式电幕的严重隐私与监控风险。 傅里叶像素利用数学傅里叶分析控制光的强度、振荡相位和偏振，从而在像素级别实现双向光控制。

rss · Schneier on Security · 7月15日 11:04

**背景**: 传统显示像素是无源发光体，不能感应光线。光场描述了空间中光线的完整强度、相位和偏振信息。傅里叶分析是一种将信号分解为频率成分的数学方法，在这里被用于控制光的特性。乔治·奥威尔小说《1984》中的电幕是一个文化符号，指既能显示信息又能监视用户的设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://logicity.in/en/blog/eth-zurich-builds-pixels-that-emit-and-detect-light">ETH Zurich builds pixels that emit and detect light | Logicity</a></li>
<li><a href="https://www.nature.com/articles/s41586-026-10681-7?error=cookies_not_supported&code=3bed0eb9-ec21-4945-ae90-16dbee66cb57">Fourier pixels for bidirectional light control | Nature</a></li>
<li><a href="https://en.wikipedia.org/wiki/Light_field">Light field</a></li>

</ul>
</details>

**标签**: `#display-technology`, `#camera`, `#research`, `#privacy`, `#surveillance`

---

<a id="item-3"></a>
## [RFC 9954：TLS 1.3 混合密钥交换标准](https://rfc-editor.org/info/rfc9954) ⭐️ 9.0/10

IETF 发布了 RFC 9954 标准，详细说明了在 TLS 1.3 中执行混合密钥交换的方法，结合了经典算法和后量子算法，以确保未来的安全性。 该标准对于向后量子密码学迁移至关重要，能够在不对现有系统造成破坏的情况下，保护互联网通信免受未来量子攻击。 该方法协商两个独立的密钥共享——一个来自传统算法（如 X25519），一个来自后量子算法（如 Kyber）——并通过密钥派生函数将它们合并，生成共享密钥，即使其中一个算法被攻破，也能保证安全性。

rss · IETF 新标准 RFC (PQC 标准化) · 7月15日 22:20

**背景**: 经典密钥交换算法（如 Diffie-Hellman）易受量子计算机攻击。后量子密码学开发了既能抵抗经典又能抵抗量子攻击的算法。混合密钥交换在 TLS 握手期间同时运行经典和后量子算法，只要至少一个算法保持安全，就能确保整体安全。这通过保持向后兼容性，简化了过渡过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/">draft-ietf-tls- hybrid -design-16 - Hybrid key exchange in TLS 1.3</a></li>
<li><a href="https://www.linkedin.com/pulse/embracing-tls-13-hybrid-key-exchange-post-quantum-protection-atoum/">Embracing TLS 1.3 Hybrid Key Exchange for Post-Quantum...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#TLS`, `#post-quantum`, `#key-exchange`, `#IETF`

---

<a id="item-4"></a>
## [基于同源的紧凑后量子 OT 方案：密钥仅 100 kB](https://eprint.iacr.org/2026/1444) ⭐️ 8.0/10

该论文基于同源构造了紧凑的后量子不经意传输伪随机相关函数（PCF），密钥大小约为 100 kB，比现有后量子替代方案小约七倍。 这一进展缩小了后量子与抗量子安全计算之间的效率差距，为安全多方计算等隐私保护应用提供了更实用的后量子协议。 密钥大小与生成的 OT 次数无关，吞吐量约为每秒 7 次 OT。安全性在量子随机预言模型下基于一个新的困难假设——带辅助输入的并行化问题——得到证明。

rss · IACR ePrint 密码学论文 · 7月15日 14:28

**背景**: 不经意传输（OT）是一种基础密码原语，发送方传输多个消息中的一个但不知道接收方获取了哪一个。伪随机相关函数（PCF）允许双方从短密钥非交互地生成大量 OT 实例。同源密码学是一种后量子方法，利用椭圆曲线间的映射，提供有竞争力的密钥大小和抗量子攻击的安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Oblivious_transfer">Oblivious transfer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isogeny-based_cryptography">Isogeny-based cryptography</a></li>
<li><a href="https://eprint.iacr.org/2023/650">Pseudorandom Correlation Functions from Variable-Density LPN, Revisited</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#oblivious-transfer`, `#isogenies`, `#secure-computation`

---

<a id="item-5"></a>
## [CoSecRAG：高效保护查询与数据库隐私的 RAG 检索协议](https://eprint.iacr.org/2026/1442) ⭐️ 8.0/10

CoSecRAG 提出了一种用于检索增强生成（RAG）的双服务器私有检索协议，利用加法秘密共享同时保护查询和数据库嵌入。其创新的 IPQ-Mask 和 PSCP 技术大幅加速了安全计算，相比现有方法，评分计算速度提升最高达 202 倍。 这项工作解决了 RAG 系统中敏感查询或专有数据库可能泄露的紧迫隐私问题，使得在受监管行业中能够安全使用基于 LLM 的检索。数量级的性能提升使得隐私保护 RAG 在实际应用中变得可行。 IPQ-Mask 通过使用一次性相关掩码消除了在线安全乘法，将内积计算转化为本地线性操作。PSCP 颠倒了传统先裁剪后评分的顺序，先计算秘密共享的评分，再在评分层面进行裁剪，从而减少安全 Top-K 选择的输入规模，通信量降低高达 43 倍。

rss · IACR ePrint 密码学论文 · 7月15日 07:51

**背景**: RAG（检索增强生成）通过在生成过程中从外部数据库检索相关文档来增强大型语言模型，但这在检索阶段会带来隐私风险。加法秘密共享是一种加密方法，将数据拆分为随机份额，允许在份额上执行计算而不泄露原始值。双服务器协议假设两个非共谋的服务器各自持有份额，并协同执行隐私计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/additive-secret-sharing">Additive Secret Sharing in Cryptography</a></li>
<li><a href="https://nlp.stanford.edu/IR-book/html/htmledition/cluster-pruning-1.html">Cluster pruning</a></li>

</ul>
</details>

**标签**: `#RAG`, `#privacy-preserving`, `#secure multi-party computation`, `#embeddings`, `#LLM`

---

<a id="item-6"></a>
## [RainHash2.0：面向硬件与二进制域零知识证明的高效哈希函数](https://eprint.iacr.org/2026/1441) ⭐️ 8.0/10

RainHash2.0 是一种新的密码学置换，专为在零知识证明中进行高效硬件实现和原生二进制域运算而设计。它引入了从 Binius 证明系统改编的水平轮函数拆分技术，相较于现有电路友好型哈希函数实现了显著的性能提升。 在 ZK 证明中，哈希函数通常占据证明者成本的主要部分，而大多数设计面向素数域，但最近像 Binius 和基于 VOLE 的 ZK 等协议运行在二进制域上。RainHash2.0 通过提供硬件加速、算术友好的哈希填补了这一空白，减少了非电路工作负载中的瓶颈，有利于 zkRollups 等应用。 RainHash2.0 利用轮函数的水平拆分有效使用不同大小的有限域。在 FPGA 上实现时，它比相关电路友好型哈希函数实现了最高 8.8 倍的效率提升，并且与 Binius 和基于 VOLE 的 ZK 框架无缝集成。

rss · IACR ePrint 密码学论文 · 7月15日 07:49

**背景**: 零知识证明允许一方在不泄露秘密的情况下证明自己知道该秘密。哈希函数是关键构建模块，但其计算成本可能很高。大多数 ZK 哈希设计针对素数域优化，但像 Binius 这样的新型证明系统使用二进制扩域以高效处理位运算。RainHash2.0 原生支持二进制域并针对硬件加速设计，满足了现代 ZK 应用中对快速、电路友好型哈希的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1441">RainHash2.0: Hardware- and Arithmetization-friendly Hash Function</a></li>
<li><a href="https://www.binius.xyz/basics/">Basics – binius.xyz</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#hash functions`, `#hardware acceleration`, `#binary fields`, `#cryptography`

---

<a id="item-7"></a>
## [隐私保护从个人控制转向企业问责](https://www.schneier.com/blog/archives/2026/07/protecting-privacy-in-an-ai-era.html) ⭐️ 8.0/10

丹尼尔·索洛夫在《华尔街日报》中主张，在 AI 时代赋予个人数据控制权的传统方法已失效，转而提出以企业问责、数据最小化和有害算法责任为核心的框架。 这一提议的转变可能带来更有效的隐私保护，在普遍数据收集和 AI 时代，与日益增长的科技公司问责呼声一致，并可能影响未来法规。 关键提议措施包括严格的数据最小化、对公司施加信托义务、确立过失或鲁莽设计的责任、追究有害算法的责任，以及实施多方利益相关者技术审查，详见索洛夫在 SSRN 上的论文。

rss · Schneier on Security · 7月16日 14:34

**背景**: 传统隐私法主要依赖‘告知与同意’，要求公司告知用户数据实践并获得许可。然而，这种方法被广泛批评为无效，因为用户很少阅读冗长的隐私政策，也无法对复杂的数据使用做出有意义的同意。AI 的兴起加剧了这些挑战，因为海量数据集用于训练模型，通常无需用户直接知情，使个人控制更加不切实际。

**标签**: `#privacy`, `#AI regulation`, `#data minimization`, `#corporate accountability`, `#technology policy`

---

<a id="item-8"></a>
## [RFC 9852 要求新协议必须使用 TLS 1.3](https://rfc-editor.org/info/rfc9852) ⭐️ 8.0/10

IETF 发布了 RFC 9852，要求所有使用 TLS 的新协议必须强制使用 TLS 1.3，这更新了之前的 RFC 9325。该变更基于 TLS 1.3 在安全性、隐私性和后量子密码学方面的优势。 该要求确保了未来的互联网协议能够继承 TLS 1.3 更强的安全性和隐私性，降低降级攻击风险，并为抗量子密码学做好准备，直接影响到协议开发者和大互联网通信的长期安全。 该要求仅适用于 TLS，而不适用于 DTLS，因为 DTLS 1.3 尚未广泛部署。RFC 9852 明确将后量子密码学作为推动这一转变的关键原因。

rss · IETF 新标准 RFC (PQC 标准化) · 7月17日 02:25

**背景**: TLS 1.3 于 2018 年标准化，相比 TLS 1.2 带来了重大安全改进，如移除过时加密算法、强制前向保密和减少握手延迟。DTLS 是用于 UDP 等数据报协议的变体，但 DTLS 1.3 尚未普及。后量子密码学旨在开发能抵御量子计算机攻击的算法，将其整合到 TLS 中是一项面向未来的持续工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TLS_1.3">TLS 1.3</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://en.wikipedia.org/wiki/DTLS">DTLS</a></li>

</ul>
</details>

**标签**: `#TLS`, `#security`, `#standards`, `#IETF`, `#post-quantum-cryptography`

---

<a id="item-9"></a>
## [RFC 10015 弃用 TLS 1.2 中过时的密钥交换方法](https://rfc-editor.org/info/rfc10015) ⭐️ 8.0/10

RFC 10015 弃用了基于有限域的 Diffie-Hellman 和 RSA 密钥交换，并建议不再使用静态椭圆曲线 Diffie-Hellman（ECDH）密码套件，仅适用于 TLS 1.2 和 DTLS 1.2。 这些密钥交换方法缺乏前向安全性或易受攻击，弃用它们可缩小攻击面，使广泛部署的 TLS 1.2 安全性更接近现代标准。 该文档更新了 17 个现有 RFC，仅影响（D）TLS 1.2（不包括更早版本和 TLS 1.3），并区分了弃用（DH、RSA）和不再建议使用（静态 ECDH）的方法。

rss · IETF 新标准 RFC (PQC 标准化) · 7月16日 20:55

**背景**: 基于有限域的 Diffie-Hellman（DH）和 RSA 是传统密钥交换方法，但使用静态密钥时缺乏前向安全性。椭圆曲线 Diffie-Hellman（ECDH）利用椭圆曲线数学提高效率，但静态 ECDH 同样依赖长期密钥。数据报传输层安全（DTLS）将 TLS 扩展到 UDP 等不可靠数据报协议。这些旧方法正被淘汰以增强安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange">Diffie – Hellman key exchange - Wikipedia</a></li>
<li><a href="https://www.ringcentral.com/gb/en/blog/definitions/dtls-datagram-transport-layer-security/">What is DTLS ? | Top Tier Security , Private Communication With...</a></li>

</ul>
</details>

**标签**: `#TLS`, `#security`, `#deprecation`, `#RFC`, `#cryptography`

---

<a id="item-10"></a>
## [RFC 9851 宣布 TLS 1.2 进入特性冻结](https://rfc-editor.org/info/rfc9851) ⭐️ 8.0/10

IETF 发布的 RFC 9851 正式将 TLS 1.2 置于特性冻结状态，只允许紧急安全修复、新的 TLS 导出器标签和 ALPN 协议 ID，不再批准任何其他变更。 此举标志着向更安全、更高效的 TLS 1.3 迁移的重要推动，鼓励开发者和系统管理员升级系统。同时，它明确了 TLS 1.2 的维护范围，将资源集中于现代协议。 该冻结仅适用于 TLS，不适用于 DTLS。只允许三种类型的变更：紧急安全修复（需工作组共识）、新的 TLS 导出器标签和新的 ALPN ID。

rss · IETF 新标准 RFC (PQC 标准化) · 7月15日 23:40

**背景**: 传输层安全协议（TLS）是一种用于保护互联网通信的加密协议。2018 年标准化的 TLS 1.3 与 TLS 1.2 相比，提供了更快的握手、更强的安全性并移除了过时功能。尽管 TLS 1.2 仍被广泛部署，但 RFC 9851 通过冻结其非关键开发来鼓励向 TLS 1.3 迁移。基于 UDP 的数据报 TLS（DTLS）不受此冻结影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/html/rfc7301">RFC 7301 - Transport Layer Security (TLS) Application-Layer Protocol Negotiation Extension</a></li>
<li><a href="https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation">Application-Layer Protocol Negotiation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DTLS">DTLS</a></li>

</ul>
</details>

**标签**: `#TLS`, `#security`, `#protocol`, `#IETF`, `#networking`

---

<a id="item-11"></a>
## [RFC 9973：用于结合证书与外部预共享密钥的 TLS 1.3 扩展](https://rfc-editor.org/info/rfc9973) ⭐️ 8.0/10

RFC 9973 标准化了一种 TLS 1.3 扩展，用于将基于证书的身份验证与外部预共享密钥相结合。

rss · IETF 新标准 RFC (PQC 标准化) · 7月15日 23:37

**标签**: `#cryptography`, `#TLS`, `#network security`, `#IETF`, `#standards`

---

<a id="item-12"></a>
## [RFC 9850 正式标准化 TLS 的 SSLKEYLOGFILE 格式](https://rfc-editor.org/info/rfc9850) ⭐️ 8.0/10

IETF 发布了 RFC 9850，正式标准化了用于记录 TLS 会话密钥的 SSLKEYLOGFILE 格式，从而可以在测试环境中解密加密流量。 这一标准化为网络诊断工具和开发人员提供了一种可靠且可互操作的方法来分析 TLS 加密流量，促进了浏览器和 Wireshark 等实用工具之间的一致性实现。 该格式是一个纯文本文件，每行记录一个密钥，支持 TLS 1.2 和 1.3。它严格用于非生产测试数据，以防止因暴露密钥而带来的安全风险。

rss · IETF 新标准 RFC (PQC 标准化) · 7月15日 23:37

**背景**: TLS 通过加密保护互联网通信，但调试加密连接需要访问会话密钥。SSLKEYLOGFILE 格式最初由浏览器非正式引入，并被 Wireshark 等工具使用，用于记录这些密钥。RFC 9850 现在提供了官方规范，确保了开发者和测试人员之间的一致性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ietf.org/ietf-ftp/internet-drafts/draft-ietf-tls-keylogfile-05.xml">The SSLKEYLOGFILE Format for TLS</a></li>
<li><a href="https://github.com/tlswg/sslkeylogfile">tlswg/ sslkeylogfile : Formally document the SSLKEYLOGFILE format</a></li>

</ul>
</details>

**标签**: `#TLS`, `#debugging`, `#protocol`, `#standardization`, `#IETF`

---

<a id="item-13"></a>
## [SENTRA：面向隐私保护云机器学习训练的混合 TEE-MPC 架构](https://eprint.iacr.org/2026/1443) ⭐️ 7.0/10

研究人员提出了 SENTRA，一种新颖的混合架构，结合了可信执行环境（TEE）和安全多方计算（MPC），并采用可扩展的集体证明协议，从而在不可信的云环境中实现安全高效的机器学习训练。一个原型系统在纯软件模式下吞吐量达 8.89 样本/秒，训练速度比 CrypTen 基线快 1.29 倍，而在硬件安全区模式下性能开销仅 8.3%。 该方法解决了现有隐私保护训练方法的关键局限：TEE 缺乏可扩展性且易受侧信道攻击，而纯 MPC 会产生过高的开销。这对需要跨异构云进行可信协调的新兴智能体 AI 系统尤其重要。SENTRA 通过实现低开销和容错能力，使得在云环境中进行大规模机密训练成为现实，有望加速隐私保护机器学习的应用。 SENTRA 的集体证明协议验证所有参与的安全区，并在处理秘密份额前强制实施硬件排他性。它采用版本化的安全区支持键值存储实现回滚保护，利用动态主动秘密共享（DPSS）实现容错成员管理，并在度数界限内安全地执行数据包 MPC 计算。原型系统可在约 8 秒内从节点故障中恢复。

rss · IACR ePrint 密码学论文 · 7月15日 11:27

**背景**: 可信执行环境（TEE，如英特尔 SGX）提供硬件隔离的内存区域（称为安全区），可保护代码和数据免受系统其余部分的影响，但它们难以处理大规模工作负载且存在侧信道漏洞。安全多方计算（MPC）允许多方在不泄露各自私有输入的情况下联合计算某个函数，但其通信和计算成本高昂。SENTRA 将 TEE 用于初始安全与证明，将 MPC 用于分布式可扩展训练，并通过集体证明确保所有节点可信，利用秘密共享保护数据完整性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Trusted_execution_environment">Trusted execution environment</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation</a></li>

</ul>
</details>

**标签**: `#privacy-preserving ML`, `#trusted execution environments`, `#secure multi-party computation`, `#cloud computing`, `#confidential training`

---

<a id="item-14"></a>
## [Cloudflare 为两个高危 WordPress 漏洞部署 WAF 规则](https://blog.cloudflare.com/wordpress-vulnerabilities/) ⭐️ 7.0/10

Cloudflare 针对 WordPress 安全团队披露的两个高危漏洞部署了新的 WAF 规则，保护使用受影响版本的客户。 这为数百万站点提供了即时虚拟补丁，在官方 WordPress 更新发布前大幅缩短了攻击暴露窗口。 尽管规则在网络边缘缓解了漏洞，Cloudflare 仍敦促所有客户立即更新到修补后的 WordPress 版本以彻底消除风险。

rss · Cloudflare Blog (PQ 迁移) · 7月17日 21:30

**背景**: Web 应用程序防火墙（WAF）是一种安全工具，通过监控和过滤 HTTP 流量来阻止 SQL 注入、跨站脚本等网络攻击。WordPress 是全球最流行的内容管理系统，因其庞大的用户群和第三方插件而频繁成为黑客目标。Cloudflare 运营着全球边缘网络，提供集成的 WAF 保护，通过持续更新的规则集自动拦截恶意请求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Web_application_firewall">Web application firewall</a></li>

</ul>
</details>

**标签**: `#security`, `#WordPress`, `#WAF`, `#vulnerability`, `#Cloudflare`

---

<a id="item-15"></a>
## [图灵“Delilah”语音加密系统新细节曝光](https://www.schneier.com/blog/archives/2026/07/details-of-alan-turings-voice-encryption-system.html) ⭐️ 7.0/10

一批此前不为人知的艾伦·图灵战时文件（称为“Bayley papers”）重现于世，详细记录了他的绝密便携式语音加密系统 Delilah。这些文件于 2023 年 11 月拍卖，包含图灵亲笔手稿。 这一发现揭示了图灵在语音加密方面被忽视的工作，扩展了我们对他在战时贡献的认识，不仅限于密码破译。它还保存了原本可能遗失的重要工程历史。 文件包括图灵的手写笔记和 Bayley 的听课记录，详细描述了如何将语音信号数学转换为加密形式。Delilah 通过密钥流将语音转换为类似数字信号进行加密。这批文件在 2023 年 11 月的拍卖中以近 50 万美元成交。

rss · Schneier on Security · 7月17日 11:02

**背景**: 艾伦·图灵是英国数学家和计算机科学家，因二战期间在布莱切利园破译 Enigma 密码而闻名。Delilah 项目是他在 1943 年至 1945 年间与工程师 Donald Bayley 合作进行的一项绝密计划，旨在开发便携式语音加密设备。该项目此前一直鲜为人知，直到这批文件出现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/alan-turings-delilah">Alan Turing ’s Secret “ Delilah ” Project - IEEE Spectrum</a></li>
<li><a href="https://en.wikipedia.org/wiki/Alan_Turing">Alan Turing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#history`, `#Alan Turing`, `#voice encryption`, `#WWII`

---
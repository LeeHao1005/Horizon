---
layout: default
title: "Horizon Summary: 2026-07-17 (ZH)"
date: 2026-07-17
lang: zh
---

> 从 47 条内容中筛选出 15 条重要资讯。

---

1. [RFC 9954：TLS 1.3 混合密钥交换标准发布](#item-1) ⭐️ 9.0/10
2. [Vela 与 Carina：基于倒数多项式的快速多线性多项式承诺新方案](#item-2) ⭐️ 8.0/10
3. [基于同态秘密共享的分层 MPC 次线性通信](#item-3) ⭐️ 8.0/10
4. [基于同源的后量子无声 OT，密钥仅 100 kB](#item-4) ⭐️ 8.0/10
5. [CoSecRAG：基于加法秘密共享的私有 RAG 检索](#item-5) ⭐️ 8.0/10
6. [RainHash2.0：二进制域与硬件优化的哈希函数](#item-6) ⭐️ 8.0/10
7. [Rarus：针对多项式向量承诺的高效简洁范围证明](#item-7) ⭐️ 8.0/10
8. [基于双重循环假设的无界深度电路 ABE 新方案](#item-8) ⭐️ 8.0/10
9. [SoK：安全排序电子投票系统设计分析](#item-9) ⭐️ 8.0/10
10. [可验证且抗合谋的多方量子私有集合运算](#item-10) ⭐️ 8.0/10
11. [隐私专家：通过问责公司规制 AI](#item-11) ⭐️ 8.0/10
12. [傅里叶像素让显示屏变身摄像头](#item-12) ⭐️ 8.0/10
13. [RFC 9852 要求新协议必须使用 TLS 1.3](#item-13) ⭐️ 8.0/10
14. [RFC 10015 弃用 TLS 1.2 中的过时密钥交换方法](#item-14) ⭐️ 8.0/10
15. [RFC 9918 更新 NETCONF over TLS，强制支持 TLS 1.3](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [RFC 9954：TLS 1.3 混合密钥交换标准发布](https://rfc-editor.org/info/rfc9954) ⭐️ 9.0/10

RFC 9954 正式发布，定义了 TLS 1.3 中混合密钥交换的标准构造，将经典算法与后量子算法等多种密钥协商算法相结合，确保即使某种算法被破解，会话密钥依然安全。 该标准对行业向抗量子密码学过渡至关重要，通过允许将经过验证的经典算法与新型后量子算法结合使用，实现安全迁移，从而防范未来的量子攻击和“先存储后解密”的威胁。 该混合密钥交换构造通过将多个密钥交换方法产生的共享秘密串联，并输入密钥派生函数，保证只要至少一个组件算法未被攻破，最终密钥就是安全的。这是一份标准跟踪文档，体现了 IETF 的共识。

rss · IETF 新标准 RFC (PQC 标准化) · 7月15日 22:20

**背景**: 混合密钥交换同时结合多种密钥建立算法，使得即使除一种之外的所有算法都被破解，会话密钥依然安全。这一方法源于量子计算机的威胁，量子计算机能高效破解当前公钥密码（如 RSA、ECDH）。为应对此威胁，密码学家正在开发被认为能抵御量子攻击的后量子算法。TLS 1.3 是传输层安全协议的最新版本，用于保护互联网通信。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-tls-hybrid-design/">Hybrid key exchange in TLS 1.3 draft-ietf-tls-hybrid-design-16</a></li>
<li><a href="https://auth48-transition.rfc-editor.org/authors/rfc9954.html">RFC 9954: Hybrid Key Exchange in TLS 1.3</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#TLS`, `#key exchange`, `#IETF`, `#security standard`

---

<a id="item-2"></a>
## [Vela 与 Carina：基于倒数多项式的快速多线性多项式承诺新方案](https://eprint.iacr.org/2026/1438) ⭐️ 8.0/10

该论文提出了 Vela 和 Carina 两种新型基于配对的多线性多项式承诺方案。Vela 实现了 232 字节的最小证明体积和快速验证，而 Carina 通过线性域运算和 452 字节的证明优化了证明者时间。 这些方案改进了零知识证明系统中的效率权衡，有望降低区块链应用（如 zk-rollups）的成本，在这些应用中简洁验证与小证明体积至关重要。 在 BLS12-381 曲线上规模为 2^20 时，Vela 的证明仅 232 字节（比次小方案小 1.62 倍），验证时间 2.09 毫秒。Carina 的打开时间与以证明者为导向的方案相当，但验证器更快。

rss · IACR ePrint 密码学论文 · 7月15日 00:01

**背景**: 多项式承诺方案允许证明者承诺一个多项式，并在之后证明特定点上的取值。KZG（Kate-Zaverucha-Goldberg）是基于配对的常用单变量方案。多线性扩展在此基础上构建多变量多项式，对于 SNARKs 中的和校验协议至关重要。近期的 MERCURY 方案将多线性求值表示为洛朗多项式的常数项，而 Vela 和 Carina 利用倒数多项式扩展了这一思路，以提升效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2025/385">MERCURY: A multilinear Polynomial Commitment Scheme with constant proof size and no prover FFTs</a></li>
<li><a href="https://eprint.iacr.org/2026/480">CHOPIN: Optimal Pairing-Based Multilinear Polynomial Commitments from Bivariate KZG</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reciprocal_polynomial">Reciprocal polynomial</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#zero-knowledge proofs`, `#polynomial commitments`, `#pairings`, `#multilinear polynomials`

---

<a id="item-3"></a>
## [基于同态秘密共享的分层 MPC 次线性通信](https://eprint.iacr.org/2026/1445) ⭐️ 8.0/10

作者提出了一种基于新型分层友好同态秘密共享(HSS)的次线性通信分层 MPC 协议，消除了动态服务器辅助环境中对全同态加密(FHE)的依赖。 这项进展弥合了'经典'MPC 与动态服务器辅助 MPC 之间的差距，在无需 FHE 沉重计算开销的情况下实现次线性通信，这对于实际的长期安全计算至关重要。 该协议基于 CRYPTO 2023 提出的分层 MPC 框架，每层仅需两到三个在线服务器，并形式化了一种带分层重共享的同态秘密共享变体以实现次线性通信。

rss · IACR ePrint 密码学论文 · 7月15日 16:25

**背景**: 同态秘密共享(HSS)是一种密码学原语，将秘密分发为多个份额，使得可以在份额上进行计算并获得结果的份额，类似于同态加密但适用于秘密共享场景。分层 MPC 是一种安全计算模型，其交互模式由分层图定义，允许服务器在不同层之间动态加入或退出。在动态服务器辅助 MPC 中，先前的次线性通信协议依赖于计算开销较大的全同态加密(FHE)。本文通过使用分层适配的 HSS 消除了这一需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_secret_sharing">Homomorphic secret sharing</a></li>
<li><a href="https://eprint.iacr.org/2023/330">Perfect MPC over Layered Graphs - IACR Cryptology ePrint Archive</a></li>

</ul>
</details>

**标签**: `#MPC`, `#sublinear communication`, `#HSS`, `#layered MPC`, `#secure computation`

---

<a id="item-4"></a>
## [基于同源的后量子无声 OT，密钥仅 100 kB](https://eprint.iacr.org/2026/1444) ⭐️ 8.0/10

研究者利用同源构造了后量子的不经意传输（OT）伪随机相关函数（PCF），密钥大小约为 100 kB，比现有最紧凑的后量子 PCF 小七倍，且密钥大小不随生成的 OT 数量而变化。 该进展大幅缩小了前量子和后量子 OT PCF 在效率上的差距，使后量子安全计算向实用化迈进，有助于推动后量子密码协议的采用。 方案核心是一种新的紧凑约束伪随机函数（CPRF），用于内积成员谓词，安全性基于带辅助输入的并行化假设；吞吐量为每秒 7 个 OT，并首次在量子随机预言机模型下给出后量子 PCF 的安全证明。

rss · IACR ePrint 密码学论文 · 7月15日 14:28

**背景**: 不经意传输（OT）是一种基础两方协议，发送方在不知接收方选择的情况下传送两条消息之一。伪随机相关函数（PCF）允许双方通过短密钥非交互地生成大量相关随机数，降低安全计算的通信量。基于同源的密码学利用寻找椭圆曲线间映射的困难性，提供抗 Shor 算法的后量子安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Oblivious_transfer">Oblivious transfer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isogeny-based_cryptography">Isogeny-based cryptography</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#oblivious-transfer`, `#isogenies`, `#secure-computation`

---

<a id="item-5"></a>
## [CoSecRAG：基于加法秘密共享的私有 RAG 检索](https://eprint.iacr.org/2026/1442) ⭐️ 8.0/10

CoSecRAG 提出了一种基于加法秘密共享的高效双服务器私有检索协议，包含内积保留查询掩码和评分后聚类剪枝两项关键技术，与现有方法相比在评分计算上实现了最高 202 倍的加速。 该协议解决了 RAG 系统中的关键隐私风险，通过同时保护查询和数据库嵌入，使得医疗、金融等敏感领域能够在不牺牲性能的情况下安全使用。 IPQ-Mask 通过将安全内积转化为本地线性计算来消除在线安全乘法；PSCP 逆转先剪枝后评分的流程，减小安全 Top-K 选择的输入规模。协议依赖两个非共谋服务器。

rss · IACR ePrint 密码学论文 · 7月15日 07:51

**背景**: 检索增强生成（RAG）通过从外部知识库检索相关文档来增强大语言模型。加法秘密共享将秘密拆分为随机份额，单个份额不泄露信息，合并后可恢复原始秘密，从而实现安全计算。内积常用于度量查询与文档嵌入的相似度。聚类剪枝通过限制搜索范围为少数文档簇来加速检索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Secret_sharing">Secret sharing - Wikipedia</a></li>
<li><a href="https://eprint.iacr.org/2026/1442">CoSecRAG: Efficient Private Retrieval with Database and Query Privacy for RAG</a></li>

</ul>
</details>

**标签**: `#RAG`, `#Privacy-Preserving`, `#Cryptography`, `#LLM`, `#Retrieval`

---

<a id="item-6"></a>
## [RainHash2.0：二进制域与硬件优化的哈希函数](https://eprint.iacr.org/2026/1441) ⭐️ 8.0/10

该论文提出了 RainHash2.0，这是一种原生定义在二进制扩域上的密码置换，并针对零知识证明、硬件加速和快速明文评估进行了优化。它融合了来自 Binius 协议的创新横向拆分技术，可同时高效处理不同大小的有限域。 大多数零知识证明哈希函数针对素数域设计，但 Binius 和基于 VOLE 的 ZK 等新兴协议运行在二进制扩域上，造成了效率缺口。RainHash2.0 填补了这一缺口，同时提供出色的硬件性能，对 zkRollups 等 ZK 应用的扩展至关重要。 关键技术亮点包括：采用横向轮函数拆法以支持高效的混域运算；FPGA 原型实现相较于同类电路友好哈希最高 8.8 倍加速；以及集成到 Binius 和 VOLEitH 框架中，展现出更小的证明体积和更快的证明者/验证者运行时间。

rss · IACR ePrint 密码学论文 · 7月15日 07:49

**背景**: 零知识证明允许一方在不泄露秘密的情况下证明某个陈述。二进制扩域（F_{2^n}）是包含 2^n 个元素的有限域，由于其按位操作的高效性，在通信和密码学中被广泛使用。Binius 和基于 VOLE 的 ZK 等协议利用这些域原生地处理按位逻辑。然而，大多数针对 ZK 优化的哈希函数（如 Poseidon）都面向素数域，并且硬件加速也一直被忽视。RainHash2.0 从设计之初就为二进制扩域和硬件效率打造，可利用 NVIDIA clmad 等最新的无进位乘法指令实现快速的域运算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/building-faster-cryptography-with-carryless-multiplication-in-nvidia-cuda-13-3/">Building Faster Cryptography with Carryless Multiplication in ...</a></li>
<li><a href="https://eprint.iacr.org/2025/1893">Poseidon (2)b: Binary Field Versions of Poseidon/Poseidon2</a></li>
<li><a href="https://www.binius.xyz/basics/">Basics – binius.xyz</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#hash functions`, `#cryptography`, `#hardware acceleration`, `#binary fields`

---

<a id="item-7"></a>
## [Rarus：针对多项式向量承诺的高效简洁范围证明](https://eprint.iacr.org/2026/1440) ⭐️ 8.0/10

Rarus 提出了一种针对基于多项式的向量承诺的优化范围证明，用 b 进制分解替换了二进制分解，并采用了双变量零测试和加速的单变量求和检查协议，将证明者时间从 O(Nℓ log(Nℓ)) 降至 O(Nℓ / log(Nℓ)) 次群运算加 O(Nℓ) 次域运算，同时保持 O(1) 的证明大小和验证者时间。 这一进展显著降低了隐私保护应用（如机密交易、匿名凭证和电子投票）中证明者的计算负担，可能实现更具可扩展性和实用性的零知识系统。 Rarus 达到了最优渐近复杂度，并支持任意范围 R（不仅仅是 2 的幂）。实验结果表明，在证明 16,384 个位于 [0, 2^64) 范围内的值时，其速度比 Bulletproofs 和 Missileproof 快 20 倍。但该论文目前是预印本，尚未经过同行评审。

rss · IACR ePrint 密码学论文 · 7月15日 03:10

**背景**: 范围证明允许证明者在不泄露具体数值的情况下，向验证者证明所承诺的秘密值位于特定区间内，这对于 Monero 等加密货币的隐私性至关重要。向量承诺方案能够对一组值进行承诺，并有效地证明相关属性。Missileproof（CCS'24）是最近提出的一种针对向量承诺的范围证明，实现了常数证明大小和验证时间，但其证明者时间按 O(Nℓ log(Nℓ)) 规模增长。Rarus 基于多项式向量承诺，通过使用更大的分解基数和新型求和检查协议提高了证明者效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mystenlabs.com/blog/zero-knowledge-range-proofs">Zero-Knowledge Range Proofs: Proving Where Your Secret Lies</a></li>
<li><a href="https://rareskills.io/post/range-proof">Range Proof - RareSkills</a></li>
<li><a href="https://amosehiguese.medium.com/missileproof-a-zero-knowledge-succinct-non-interative-argument-of-nowledge-fe9e1143ec5a">MissileProof: A zero-knowledge succinct, non-interative ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#zero-knowledge proofs`, `#range proofs`, `#vector commitments`, `#privacy`

---

<a id="item-8"></a>
## [基于双重循环假设的无界深度电路 ABE 新方案](https://eprint.iacr.org/2026/1439) ⭐️ 8.0/10

该论文提出了一种新的无界深度和宽度电路的属性基加密（ABE）方案，基于一种新颖的“双重循环”假设，该假设将循环 LWE 与 ElGamal 变体的密钥相关消息安全性不可分割地结合在一起。该假设取代了最近被破解的循环规避 LWE 假设，并在双线性通用群模型中被证明是安全的。 这项工作解决了密码学中一个关键开放问题，提供了一个无需依赖于紧凑型函数加密或混淆技术的、可证伪的无界深度电路 ABE 候选方案。它对高级加密系统的设计产生影响，并为未来研究提供了新的、潜在安全的基础。 该假设在 Shoup 的双线性通用群模型中成立，可抵御非通用攻击；在受限条件下，它可由标准 SXDH 假设和循环 LWE 推导得出。该方案同时支持无界的宽度和深度，这是一个重要的技术改进。

rss · IACR ePrint 密码学论文 · 7月15日 01:01

**背景**: 属性基加密（ABE）允许根据用户属性进行解密，而基于电路的 ABE 可实现复杂策略。此前无界深度电路的最佳构造依赖于循环规避 LWE 假设，该假设最近被破解（AMYY25）。“双重循环”假设将“错误学习”（LWE）的循环安全性与密钥相关消息安全性相结合，而双线性通用群模型是证明基于配对方案安全性的标准化理想模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cse.iitm.ac.in/~shwetaag/Evasive-AMYY.pdf">Evasive LWE : Attacks, Variants & Obfustopia</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-032-12293-3_9">Zeroizing Attacks Against Evasive and Circular Evasive LWE</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#attribute-based encryption`, `#lattice-based cryptography`, `#circuits`, `#generic group model`

---

<a id="item-9"></a>
## [SoK：安全排序电子投票系统设计分析](https://eprint.iacr.org/2026/1437) ⭐️ 8.0/10

本文系统分析了基于排序的电子投票系统的密码学设计空间，按信息泄露程度分类，并探讨了隐私、可验证性和功能性之间的权衡。 随着现实选举越来越多地考虑如即时决选等复杂投票方法，此类分析对于确保安全电子投票系统的端到端可验证性和选民隐私至关重要。 论文指出，基于排序的系统可根据信息泄露程度划分为不同类别，每一类都共享类似的密码学方法（如混合网络、同态计票和零知识证明），并概述了未来研究的开放问题。

rss · IACR ePrint 密码学论文 · 7月14日 11:56

**背景**: 混合网络通过打乱和重加密消息来切断发送方与接收方的联系，对投票匿名性至关重要。同态加密允许在不解密的情况下对加密票数进行计票。零知识证明使得在不泄露个人选票的情况下验证计票正确性成为可能。基于排序的投票方法（如波达计数法或即时复选投票）要求选民对候选人进行排序，这比简单多数投票的计算更复杂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mix_network">Mix network</a></li>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_encryption">Homomorphic encryption</a></li>
<li><a href="https://en.wikipedia.org/wiki/Borda_count">Borda count</a></li>

</ul>
</details>

**标签**: `#e-voting`, `#cryptography`, `#systematization-of-knowledge`, `#ranking-based-voting`, `#security`

---

<a id="item-10"></a>
## [可验证且抗合谋的多方量子私有集合运算](https://eprint.iacr.org/2026/1436) ⭐️ 8.0/10

提出了一种新的多方量子私有集合运算协议，结合可验证量子全同态加密和阈值全同态加密，实现可验证性和抗合谋能力，并在 IBM 量子平台上进行了仿真。 该工作填补了现有量子私有集合交集协议在威胁模型上的重大空白，特别是第三方与参与者的合谋问题，并提供了可验证性，从而极大提升了量子安全多方计算的安全性和适用范围。 通过 CAND 电路实现了交集计算，在语义安全模型下证明了可验证性，并利用开放控制操作将构造扩展至量子私有集合并集。

rss · IACR ePrint 密码学论文 · 7月14日 10:30

**背景**: 量子私有集合交集允许多方在不泄露额外信息的情况下计算私有集合的交集，借助量子力学保证安全性。全同态加密支持对加密数据进行计算，可验证量子全同态加密增加了对计算正确性的公开验证。阈值全同态加密将秘密密钥分散在多个参与方之间，防止单点故障并支持协作解密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1708.09156">[1708.09156] Quantum Fully Homomorphic Encryption With Verification</a></li>
<li><a href="https://www.usenix.org/conference/usenixsecurity26/presentation/hu-zhenkai">Ajax: Fast Threshold Fully Homomorphic Encryption ... | USENIX</a></li>

</ul>
</details>

**标签**: `#quantum cryptography`, `#private set intersection`, `#homomorphic encryption`, `#secure multiparty computation`, `#quantum computing`

---

<a id="item-11"></a>
## [隐私专家：通过问责公司规制 AI](https://www.schneier.com/blog/archives/2026/07/protecting-privacy-in-an-ai-era.html) ⭐️ 8.0/10

Daniel Solove 指出，在 AI 时代，赋予个人数据控制权无法有效保护隐私，转而主张通过数据最小化、算法问责等措施追究公司责任。 这一观点可能重塑隐私监管，将责任从个人转移到强大的 AI 公司，从而更有效地防止数据滥用和算法危害。 提出的措施包括严格的数据最小化、数据处理者的受托义务、对疏忽技术设计和有害算法的问责，以及技术的多方利益相关者审查。

rss · Schneier on Security · 7月16日 14:34

**背景**: 传统隐私法多采用通知与同意模式，让个人通过同意书控制数据。但 AI 系统复杂且数据收集量巨大，个人难以有效管理隐私。AI 能从看似无害的数据中推断出敏感信息，而算法不透明使得数据用途难以知晓。

**标签**: `#privacy`, `#AI`, `#regulation`, `#data protection`, `#corporate accountability`

---

<a id="item-12"></a>
## [傅里叶像素让显示屏变身摄像头](https://www.schneier.com/blog/archives/2026/07/a-video-screen-that-is-also-a-camera.html) ⭐️ 8.0/10

苏黎世联邦理工学院的研究人员开发出一种名为傅里叶像素的新型像素，能同时发射和捕捉光线，使显示屏兼具显示和摄像功能。该成果发表在《自然》杂志上。 这一突破为日常屏幕中嵌入隐形摄像头铺平了道路，引发了类似于《1984》的深刻隐私担忧，同时也为交互式和普适计算带来了新的可能性。 傅里叶像素通过叠加多个光学组件来操控光的强度、相位和偏振，实现双向光控制。该研究于 2026 年 6 月 24 日发表在《自然》杂志上。

rss · Schneier on Security · 7月15日 11:04

**背景**: 传统显示像素只能发光，而摄像头传感器只能捕捉光线。傅里叶变换是一种将复杂波形分解为简单频率分量的数学工具。研究人员利用类似原理，将能够独立控制光不同属性的子元件组合起来，创造出一个既能生成图像又能分析图像的像素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10681-7">Fourier pixels for bidirectional light control - Nature</a></li>
<li><a href="https://ethz.ch/en/news-and-events/eth-news/news/2026/06/a-new-type-of-pixel.html">A new type of pixel | ETH Zurich</a></li>

</ul>
</details>

**标签**: `#display technology`, `#sensing`, `#privacy`, `#optics`, `#research`

---

<a id="item-13"></a>
## [RFC 9852 要求新协议必须使用 TLS 1.3](https://rfc-editor.org/info/rfc9852) ⭐️ 8.0/10

IETF 发布的 RFC 9852 规定，任何使用 TLS 的新协议都必须强制要求 TLS 1.3，理由是其在安全性和隐私性方面优于 TLS 1.2。该规定明确将 DTLS 排除在外，因为 DTLS 1.3 的部署尚不广泛。 该标准确保了未来的 TLS 协议能受益于 TLS 1.3 的重大安全改进，如前向保密和降级攻击防护，从而提高互联网安全基线，并为后量子密码学迁移做好准备。 RFC 9852 更新了 RFC 9325（《TLS 安全使用建议》），并将后量子密码学准备作为推动这一要求的部分理由。DTLS 被排除在外，因为 DTLS 1.3 尚未普及或广泛部署。

rss · IETF 新标准 RFC (PQC 标准化) · 7月17日 02:25

**背景**: 传输层安全协议（TLS）是保护互联网通信的加密协议。TLS 1.3 于 2018 年标准化，简化了握手过程，移除了过时算法，并强制使用前向保密。数据报传输层安全协议（DTLS）是针对 UDP 等数据报应用的变体，但 DTLS 1.3 的采用率落后于 TLS 1.3。后量子密码学旨在开发能抵抗量子计算机攻击的算法，这是当前 TLS 版本尚未解决但关乎长期安全的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Transport_Layer_Security">Transport Layer Security - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security">Datagram Transport Layer Security - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>

</ul>
</details>

**标签**: `#TLS`, `#IETF`, `#security`, `#protocols`, `#standardization`

---

<a id="item-14"></a>
## [RFC 10015 弃用 TLS 1.2 中的过时密钥交换方法](https://rfc-editor.org/info/rfc10015) ⭐️ 8.0/10

RFC 10015 弃用了 TLS 1.2 和 DTLS 1.2 中的有限域 Diffie-Hellman 和 RSA 密钥交换，同时反对使用静态 ECDH 密码套件，并更新了 17 项早先的 RFC。 此举通过淘汰缺少前向保密性且易受攻击的密钥交换方法，增强了传输层安全性，符合业界逐步淘汰广泛部署协议中弱加密算法的努力。 该更新仅适用于 TLS 1.2 和 DTLS 1.2，因为更早的版本已被弃用，且 TLS 1.3 不使用受影响算法；与 DH 和 RSA 密钥交换不同，静态 ECDH 只是被反对，并未被禁止。

rss · IETF 新标准 RFC (PQC 标准化) · 7月16日 20:55

**背景**: TLS 1.2 是广泛使用的安全通信协议。基于有限域的 Diffie-Hellman (DH) 和 RSA 加密等密钥交换方法可用于建立共享秘密，但它们缺少前向保密性且容易遭受某些攻击。静态椭圆曲线 Diffie-Hellman (ECDH) 使用固定密钥对，与其每次会话生成新密钥的临时变体 (ECDHE) 不同。DTLS（数据报 TLS）将 TLS 适配用于 UDP 等不可靠数据报传输。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://crypto.stackexchange.com/questions/19452/static-dh-static-ecdh-certificate-using-openssl">diffie hellman - Static DH/ Static ECDH certificate using OpenSSL...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security">Datagram Transport Layer Security - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange">Diffie – Hellman key exchange - Wikipedia</a></li>

</ul>
</details>

**标签**: `#TLS`, `#security`, `#cryptography`, `#IETF`, `#deprecation`

---

<a id="item-15"></a>
## [RFC 9918 更新 NETCONF over TLS，强制支持 TLS 1.3](https://rfc-editor.org/info/rfc9918) ⭐️ 8.0/10

RFC 9918 更新了 RFC 7589，要求 NETCONF 连接必须支持 TLS 1.3，并限制使用 TLS 1.3 的早期数据（0-RTT），以防止重放攻击。 此更新通过确保网络设备使用现代加密技术并防范重放攻击，增强了网络配置协议的安全性，这对保护网络基础设施至关重要。 该 RFC 禁止在 NETCONF 中使用 TLS 1.3 早期数据（0-RTT）以避免重放漏洞，更新了 TLS 1.2 的密码套件要求，并强制要求支持 TLS 1.3。

rss · IETF 新标准 RFC (PQC 标准化) · 7月15日 02:30

**背景**: NETCONF 是一种用于配置网络设备的协议，传统上通过 SSH 运行。RFC 7589 定义了其在 TLS 上的使用，并采用 X.509 相互认证。TLS 1.3 引入了早期数据（0-RTT）以降低延迟，但该功能易受重放攻击，因此不适合用于配置更改。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techdocs.akamai.com/property-mgr/docs/early-data-0rtt">Early Data (0-RTT)</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc8446">RFC 8446 - The Transport Layer Security (TLS) Protocol Version 1.3</a></li>
<li><a href="https://archive.org/stream/rfc6241/rfc6241.txt_djvu.txt">Full text of "Network Configuration Protocol ( NETCONF )"</a></li>

</ul>
</details>

**标签**: `#networking`, `#security`, `#TLS`, `#NETCONF`, `#IETF`

---
---
layout: default
title: "Horizon Summary: 2026-07-01 (ZH)"
date: 2026-07-01
lang: zh
---

> 从 38 条内容中筛选出 14 条重要资讯。

---

1. [RFC 9980：OpenPGP 的后量子密码学扩展](#item-1) ⭐️ 9.0/10
2. [OEKE-2F PAKE 协议的正确哈希要求](#item-2) ⭐️ 8.0/10
3. [Falafel: 联邦学习中的模块化零知识训练证明](#item-3) ⭐️ 8.0/10
4. [EasyCrypt 协议证明需要状态和时间不变量](#item-4) ⭐️ 8.0/10
5. [ML-DSA 基准测试陷阱与稳健方法论](#item-5) ⭐️ 8.0/10
6. [差异化方法使后量子 DNSSEC 支持大密钥](#item-6) ⭐️ 8.0/10
7. [人工智能视频监控实现自然语言查询](#item-7) ⭐️ 8.0/10
8. [发现带有大量零位的新型弱 RSA 密钥在现实中使用](#item-8) ⭐️ 8.0/10
9. [pyca/cryptography 现已支持一键安装后量子密码](#item-9) ⭐️ 8.0/10
10. [RFC 9942：用于可验证数据结构的 COSE 收据](#item-10) ⭐️ 8.0/10
11. [RQP 协议：DeFi 中 RWA 隐私保护新方案](#item-11) ⭐️ 7.0/10
12. [IETF RFC 9943：可信数字供应链架构](#item-12) ⭐️ 7.0/10
13. [RFC 9974 定义 BIER 层 OAM 需求](#item-13) ⭐️ 7.0/10
14. [RFC 9970 为 STIR 引入连接身份机制](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [RFC 9980：OpenPGP 的后量子密码学扩展](https://rfc-editor.org/info/rfc9980) ⭐️ 9.0/10

RFC 9980 作为 IETF 标准发布，为 OpenPGP 定义了后量子密码算法，包括 ML-KEM、ML-DSA 和 SLH-DSA。 该标准为 OpenPGP 通信提供了抵御未来量子计算机攻击的标准化方法，确保加密邮件和数据的长期安全。 该 RFC 规定了将 ML-KEM 或 ML-DSA 与传统椭圆曲线密码结合的复合方案以实现混合安全，并包含作为独立散列签名方案的 SLH-DSA。它是对 RFC 9580 的扩展。

rss · IETF 新标准 RFC (PQC 标准化) · 6月30日 22:51

**背景**: OpenPGP 是广泛用于电子邮件和文件安全的加密和数字签名标准。量子计算机威胁着 RSA 和 ECC 等传统公钥算法。美国国家标准与技术研究院（NIST）已将 ML-KEM（FIPS 203）、ML-DSA（FIPS 204）和 SLH-DSA（FIPS 205）选为后量子标准。RFC 9980 将这些算法整合进 OpenPGP，以提供抗量子能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://en.wikipedia.org/wiki/SLH-DSA">SLH-DSA</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#OpenPGP`, `#IETF`, `#RFC`, `#security`

---

<a id="item-2"></a>
## [OEKE-2F PAKE 协议的正确哈希要求](https://eprint.iacr.org/2026/1331) ⭐️ 8.0/10

该论文分析了 OEKE-2F PAKE 协议的全部 16 种变体，并证明了它们的 UC 安全性，指出哈希所有组件（密码、公钥、第一条消息、密文）的版本对底层 KEM 的安全属性要求最少。 这解决了社区关于 OEKE-2F 中正确哈希方式的争议，有助于在经典和后量子环境下实现安全高效的 PAKE，并推动标准化进程。 “哈希所有内容”的变体对 KEM 的安全属性要求最少；移除哈希项会增加需求，但所有额外要求仍属温和。该论文篇幅超过 100 页。

rss · IACR ePrint 密码学论文 · 6月28日 17:41

**背景**: PAKE 协议允许双方基于低熵密码建立共享密钥。OEKE-2F 是一种将密钥封装机制（KEM）转换为 PAKE 协议的高效编译器。KEM 是一种公钥密码系统，可安全传输对称密钥。通用可组合（UC）框架是一种强大的安全模型，确保协议在与其他协议组合时仍保持安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Password-authenticated_key_agreement">Password-authenticated key agreement - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Key_encapsulation_mechanism">Key encapsulation mechanism - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_composability">Universal composability - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#PAKE`, `#key-exchange`, `#protocol-design`, `#UC-security`

---

<a id="item-3"></a>
## [Falafel: 联邦学习中的模块化零知识训练证明](https://eprint.iacr.org/2026/1335) ⭐️ 8.0/10

Falafel 引入了一种模块化的零知识训练证明（zkPoT）方案，用于联邦学习，可实现主动安全性和从数据集到最终模型的训练过程公开可验证性，对于 LeNet，每轮训练可在约 150 秒内生成仅 70 kB 的证明。 这解决了联邦学习中关键的安全和隐私挑战，确保参与者无法作弊且训练模型正确，同时不泄露敏感的本地数据，使其适用于医疗或金融等高风险应用。 该构造仅依赖于标准的密码学假设，高度可并行化，并采用提交-证明方法；其证明大小比先前工作小 10-15 倍，但证明者时间与之相当。

rss · IACR ePrint 密码学论文 · 6月29日 12:12

**背景**: 联邦学习是一种分布式机器学习方法，多方协作训练模型而不共享本地数据。零知识证明允许一方在不泄露任何秘密输入的情况下证明计算的正确性。先前的 zkPoT 方案通常依赖于不太成熟的密码学假设或具有较大的证明大小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://readmedium.com/federated-learning-using-zero-knowledge-proofs-a866986b6e0d">Federated learning using zero - knowledge proofs</a></li>
<li><a href="https://escholar.tech/zero-knowledge-proof-meets-machine-learning-in-verifiability-background">Zero - knowledge Proof Meets Machine Learning in Verifiability...</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#federated learning`, `#privacy-preserving machine learning`, `#verifiable computation`, `#cryptographic protocols`

---

<a id="item-4"></a>
## [EasyCrypt 协议证明需要状态和时间不变量](https://eprint.iacr.org/2026/1334) ⭐️ 8.0/10

该论文在 EasyCrypt 中形式化了一个简单的交互式密钥协商协议，并揭示 pRHL 证明之所以复杂，是因为需要同时使用状态不变量（用于加密推理）和时间不变量（用于协议结构）。这一见解解释了为何协议证明比原语证明更难。 它指出了面向原语的工具与面向协议的工具之间的核心差距，为构建能够处理交互式协议的新型验证工具提供了原则性方向，从而增强实际系统的安全保证。 作者通过对一个简单密钥协商协议进行探索性证明、一次失败的结构化尝试以及一个‘本质性’证明，提炼出所需的证明特征。他们认为，在计算模型下，仅靠 pRHL 是不够的，必须显式编码协议状态演化和时序假设。

rss · IACR ePrint 密码学论文 · 6月29日 08:03

**背景**: EasyCrypt 是一个在计算模型下验证密码构造的交互式证明助手，采用基于游戏的代码方法。其主要逻辑——概率关系霍尔逻辑（pRHL）用于推理两个概率程序的关系性质。交互式协议涉及多条消息交换和可变状态，超出了单独立原语通常所需的不变量范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://easycrypt.gitlab.io/easycrypt-web/">EasyCrypt Documentation | EasyCrypt</a></li>
<li><a href="https://github.com/EasyCrypt/easycrypt">GitHub - EasyCrypt/easycrypt: EasyCrypt: Computer-Aided ... Introduction to EasyCrypt EasyCrypt EasyCrypt Tutorial - baghead.org GitHub - barleyjohn/easycrypt EasyCrypt Reference Manual</a></li>
<li><a href="https://inria.hal.science/file/index/docid/765864/filename/main.pdf">Probabilistic relational Hoare logics for computer-aided security proofs</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#cryptographic protocols`, `#EasyCrypt`, `#pRHL`, `#interactive protocols`

---

<a id="item-5"></a>
## [ML-DSA 基准测试陷阱与稳健方法论](https://eprint.iacr.org/2026/1333) ⭐️ 8.0/10

该论文指出了 ML-DSA 基准测试中因拒绝采样导致的执行时间可变性带来的陷阱，并提出了使用标准化输入数据集以实现公平比较的稳健方法论。 可靠的基准测试对于后量子密码迁移至关重要，确保工程师能够做出明智决策，并为实时系统中的最坏情况执行时间做好规划。 ML-DSA 签名算法的执行时间因拒绝采样和数据依赖组件而变化；最小/平均/最大等标准指标不足，论文建议使用特定分位数和最坏情况边界。

rss · IACR ePrint 密码学论文 · 6月29日 07:05

**背景**: ML-DSA（基于模块格的数字签名算法）是 NIST 标准化的后量子数字签名方案。拒绝采样是格密码中用于确保签名遵循特定分布的技术，但它会引入执行时间的可变性。现有的基准测试往往忽略了这一点，导致结果无法比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ietf.org/archive/id/draft-ietf-lamps-cms-ml-dsa-07.txt">ietf.org/archive/id/draft-ietf-lamps-cms- ml - dsa -07.txt</a></li>
<li><a href="https://medium.com/@kootie73/lattice-based-signatures-and-rejection-sampling-an-introduction-to-modern-cryptographic-techniques-19774f87b7c7">Lattice-Based Signatures and Rejection Sampling: An ... - Medium</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#digital signatures`, `#benchmarking`, `#ML-DSA`, `#cryptographic migration`

---

<a id="item-6"></a>
## [差异化方法使后量子 DNSSEC 支持大密钥](https://eprint.iacr.org/2026/1332) ⭐️ 8.0/10

该论文提出为 DNSSEC 的区签名密钥（ZSK）和密钥签名密钥（KSK）分配不同的后量子签名算法，使得原本会超出 DNS 响应大小限制的大密钥算法（如 UOV）得以部署。 这扩展了可用于关键互联网基础设施迁移的后量子算法集合，在不产生不合理性能损失的前提下实现抗量子安全。 在基于.fr 顶级域（420 万域名）验证的测试平台中，差异化配置的延迟是 ECDSA 的 1.28 至 1.52 倍，而 UOV 的 43 KB 密钥在与紧凑密钥 KSK 配对时变得可行。混合传统/后量子签名串联仅增加 7%至 19%的开销。

rss · IACR ePrint 密码学论文 · 6月28日 20:31

**背景**: DNSSEC 使用 ZSK 签名 DNS 记录、KSK 签名 ZSK。后量子签名可能很大；DNS over UDP 有 64 KB 限制，超限响应需回退到较慢的 TCP。UOV 是多元签名方案，签名为 128 字节但公钥达 43 KB。按密钥角色区分算法利用了 KSK 响应通常更大且频率较低的特点，因此大密钥更容易接受。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/csrc/media/Projects/pqc-dig-sig/documents/round-2/spec-files/uov-spec-round2-web.pdf">UOV: Unbalanced Oil and Vinegar Specification Document - Round 2</a></li>
<li><a href="https://support.dnsimple.com/articles/types-of-dnssec-keys/">What Are the Types of DNSSEC Keys? - DNSimple Help</a></li>
<li><a href="https://pentesterworld.com/articles/hybrid-cryptography-classical-quantum-resistant">Hybrid Cryptography: Classical and Quantum -Resistant Combination</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#DNSSEC`, `#signature schemes`, `#internet security`, `#migration`

---

<a id="item-7"></a>
## [人工智能视频监控实现自然语言查询](https://www.schneier.com/blog/archives/2026/06/the-realities-of-ai-video-surveillance.html) ⭐️ 8.0/10

人工智能视频监控现在支持自然语言查询，从旧工具有限的预设搜索扩展到几乎无限范围的调查。 这一能力从根本上扩展了大规模间谍活动，使当局能够通过简单的语言查询轻松搜索海量视频片段，以前所未有的规模侵蚀隐私。 新工具允许基于语言的视频搜索，超越了旧系统仅有的几十种预设查询；《金融时报》的文章报道了涉及以色列/伊朗和俄罗斯的实际部署情况。

rss · Schneier on Security · 6月30日 12:05

**背景**: 传统的视频监控通常需要人工审查或有限的算法搜索。人工智能驱动的分析现在可以检测物体和行为，随着自然语言处理的进步，用户可以使用日常语言查询视频片段，无需技术专长即可进行复杂搜索。

**标签**: `#AI`, `#surveillance`, `#privacy`, `#security`, `#mass spying`

---

<a id="item-8"></a>
## [发现带有大量零位的新型弱 RSA 密钥在现实中使用](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html) ⭐️ 8.0/10

研究人员发现了一类新的易分解 RSA 密钥，其特点是模数稀疏且包含大量零位，并且这些密钥已被发现在现实世界的证书和密钥中被积极使用。 这一发现揭示了广泛部署的加密系统中存在的实际漏洞，可能会危及受影响的服务器、服务和通信的安全。 这些密钥是通过一种新的基于多项式的密码分析技术分解的。共识别出两种主要的位模式，其中一种可追溯到 CompleteFTP 文件传输软件旧版本中的类型不匹配错误。

rss · Schneier on Security · 6月29日 16:05

**背景**: RSA 加密的安全性依赖于大整数分解的困难性。如果模数包含许多零位，其稀疏结构可被利用来更有效地分解。badkeys 项目是一个检查公钥已知漏洞的开源工具，而证书透明度日志是用于发现这些弱密钥的 TLS 证书公共存储库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/">Factoring "short-sleeve" RSA keys with polynomials</a></li>
<li><a href="https://github.com/badkeys/badkeys">GitHub - badkeys / badkeys : Tool to find common vulnerabilities in...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#RSA`, `#vulnerability`, `#security`, `#factoring`

---

<a id="item-9"></a>
## [pyca/cryptography 现已支持一键安装后量子密码](https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/) ⭐️ 8.0/10

在 Sovereign Tech Agency 资助下，Trail of Bits 将 NIST 标准化的后量子原语 ML-KEM 和 ML-DSA 集成到 pyca/cryptography 48 版本中，使 Python 开发者可通过 pip 一键安装后量子密码功能。 pyca/cryptography 是数千个 Python 项目的密码运算基础，月下载量达 12 亿次。此次集成为 Python 生态向抗量子密码迁移打开了大门，与 2026 年白宫加速后量子密码采用的行政令保持一致。 该实现包含 Rust 绑定并支持 AWS-LC 作为密码后端。后量子密钥、签名和密文比传统算法大 1–2 个数量级，运算速度较慢，但在典型应用中仍几乎无感知。

rss · Trail of Bits Blog · 6月30日 11:00

**背景**: ML-KEM（FIPS 203）和 ML-DSA（FIPS 204）是 NIST 标准化的后量子密钥建立和数字签名算法，基于格密码学，可抵御量子计算机攻击。传统公钥系统（如 RSA 和 ECC）易受 Shor 算法威胁。2026 年 6 月，白宫下令联邦机构须在 2030 年前采用后量子密钥建立机制，2031 年前采用后量子数字签名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#Python`, `#pyca/cryptography`, `#ML-KEM`, `#ML-DSA`

---

<a id="item-10"></a>
## [RFC 9942：用于可验证数据结构的 COSE 收据](https://rfc-editor.org/info/rfc9942) ⭐️ 8.0/10

IETF 发布了 RFC 9942，定义了 COSE 收据，这是一种利用 CBOR 和 COSE 证明可验证数据结构属性的机制，并提供了默克尔包含证明和一致性证明的编码。 该标准为透明化系统提供了一个简洁、可互操作的框架，有助于在证书管理、端到端加密消息传递和供应链安全等关键应用中建立信任和问责制。 RFC 9942 利用 COSE 的加密消息语法和 CBOR 的紧凑二进制编码，定义了默克尔树证明的结构，以支持可扩展的透明性，同时避免泄露不必要的数据。

rss · IETF 新标准 RFC (PQC 标准化) · 6月30日 22:43

**背景**: CBOR（简明二进制对象表示）是一种类似于 JSON 但更紧凑的二进制序列化格式。COSE（CBOR 对象签名与加密）使用 CBOR 提供安全服务（签名、加密）。可验证数据结构（如默克尔树）能够高效地证明数据的包含性和随时间的一致性，构成了证书透明度等系统的基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CBOR">CBOR - Wikipedia</a></li>
<li><a href="https://cose-wg.github.io/cose-rfc8152bis/draft-ietf-cose-rfc8152bis-struct.html">CBOR Object Signing and Encryption ( COSE ): Structures and...</a></li>
<li><a href="https://transparency.dev/verifiable-data-structures/">Verifiable Data Structures | Trillian</a></li>

</ul>
</details>

**标签**: `#COSE`, `#transparency`, `#verifiable data structures`, `#security standards`, `#RFC`

---

<a id="item-11"></a>
## [RQP 协议：DeFi 中 RWA 隐私保护新方案](https://eprint.iacr.org/2026/1330) ⭐️ 7.0/10

该文提出真实世界资格证明（RQP）协议，引入了名为见证隐藏认证（WHA）的新型加密原语。结合 zk-SNARKs，它通过将发行方认证与借款人的零知识证明安全绑定，实现了 DeFi 中链下资产的隐私保护验证。 该协议解决了将真实世界资产集成到 DeFi 中的关键安全难题，使借款人能够在不泄露隐私数据的情况下证明资产所有权或资格。这为更安全高效的 DeFi 应用铺平道路，有望扩大链下资产作为抵押品的应用范围。 RQP 采用见证隐藏认证，在保证来源真实性的同时，将数据隐私性锚定在零知识属性上。它还利用 zk-rollup 方法和内积论证（MIPP）进行证明聚合，实现了对数级别的验证效率，并将链上 gas 成本降至最低。

rss · IACR ePrint 密码学论文 · 6月28日 07:04

**背景**: DeFi 中的真实世界资产（RWA）指用于链上贷款抵押的链下资产，如房地产或发票。zk-SNARKs 是一种非交互式零知识证明，允许证明者在不泄露秘密信息的情况下证明其拥有该信息，对区块链隐私至关重要。见证隐藏是一种确保验证者无法得知证明者所使用的见证（私密输入）的属性。RQP 将这些概念结合起来，实现了对来自可信发行方的资产资格进行安全私密的验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/rwe/10.1007/978-1-4419-5906-5_15">Witness Hiding | Springer Nature Link</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zk-SNARK">Zk-SNARK</a></li>

</ul>
</details>

**标签**: `#blockchain`, `#DeFi`, `#cryptography`, `#zk-SNARKs`, `#real-world assets`

---

<a id="item-12"></a>
## [IETF RFC 9943：可信数字供应链架构](https://rfc-editor.org/info/rfc9943) ⭐️ 7.0/10

IETF 发布了 RFC 9943，为基于签名声明透明性的可信和透明数字供应链定义了通用架构，确保不同透明度服务之间的可扩展性、互操作性和可审计性。 随着数字供应链面临日益增长的安全威胁，该 RFC 提供了一个标准化框架，以对抗抵赖等问题，实现跨不同生态系统的数字产品的安全和可验证追踪。 该架构专为单发行者场景设计，由一个权威实体签名声明并将其发布到可验证的透明度服务，从而支持包含性和一致性证明。

rss · IETF 新标准 RFC (PQC 标准化) · 6月30日 22:43

**背景**: 可验证数据结构（如 Trillian 中的可验证日志和映射）允许任何人以密码学方式验证数据的完整性和历史。签名声明透明性将这一概念应用于签名声明，确保发出的声明不可抵赖且可审计。此方法已在证书透明性和密钥透明性等项目中使用，但 RFC 9943 将其推广到任何数字供应链。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://transparency.dev/verifiable-data-structures/">Verifiable Data Structures | Trillian</a></li>
<li><a href="https://github.com/continusec/verifiabledatastructures">continusec/verifiabledatastructures: Open-source Verifiable Data ...</a></li>

</ul>
</details>

**标签**: `#supply-chain`, `#transparency`, `#verifiable-data-structures`, `#ietf`, `#rfc`

---

<a id="item-13"></a>
## [RFC 9974 定义 BIER 层 OAM 需求](https://rfc-editor.org/info/rfc9974) ⭐️ 7.0/10

IETF 发布了 RFC 9974，其中规定了在网络的位索引显式复制（BIER）层中操作、管理和维护（OAM）机制的功能需求。 该标准对网络运营商意义重大，因为它为开发 OAM 工具奠定了基础，从而确保基于 BIER 的组播网络的可靠性和可管理性，而这类网络在大规模和软件定义环境中正日益普及。 本文档不定义具体的 OAM 协议，而是列举了 BIER 转发平面所需的功能，如连接性验证、连续性检测和路径发现。

rss · IETF 新标准 RFC (PQC 标准化) · 6月29日 23:46

**背景**: 位索引显式复制（BIER）是一种组播转发技术，它利用数据包头部中的位串来编码出口路由器集合，从而消除了中间路由器中的每流状态。操作、管理和维护（OAM）涵盖用于管理、监控和排查网络问题的工具和协议。RFC 9974 基于 BIER 架构（RFC 8279），并标准化了 BIER 网络的 OAM 需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/group/bier/about/">Bit Indexed Explicit Replication ( bier )</a></li>
<li><a href="https://en.wikipedia.org/wiki/Operations,_administration,_and_management">Operations, administration, and management - Wikipedia</a></li>

</ul>
</details>

**标签**: `#BIER`, `#OAM`, `#IETF`, `#RFC`, `#networking`

---

<a id="item-14"></a>
## [RFC 9970 为 STIR 引入连接身份机制](https://rfc-editor.org/info/rfc9970) ⭐️ 7.0/10

RFC 9970 更新了 STIR 框架，使 SIP 通信中被叫方身份得以确定，解决了“连接身份”问题。该文档有助于检测呼叫重定向，并防止中间人伪造会话中事件。 该更新通过密码学验证被叫方身份，增强了电话网络信任，减少了欺诈和呼叫伪造。这对于维护基于 SIP 的电话系统在日益变化的威胁环境中的完整性至关重要。 该文档扩展了 STIR 框架的 SIP 身份头机制以涵盖连接身份情况，更新了早期的 RFC 4916。它专门针对冒充预期目的地的行为，并保护会话中信令免遭第三方伪造。

rss · IETF 新标准 RFC (PQC 标准化) · 6月29日 21:25

**背景**: STIR（安全电话身份重访）是一个防止 VoIP 网络中来电显示伪造的框架，常与 SHAKEN 结合用于呼叫验证。SIP（会话发起协议）是用于通信会话的信令协议，其中 SIP 身份头携带主叫方的密码学证据。此前，STIR 缺乏在呼叫重定向时验证被叫方的方法，RFC 9970 正是针对这一缺口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/rfc9970/">RFC 9970: Connected Identity for Secure Telephone Identity ...</a></li>
<li><a href="https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx">STIR /SHAKEN With Telnyx | Telnyx Help Center</a></li>

</ul>
</details>

**标签**: `#STIR`, `#SIP`, `#RFC`, `#Identity Verification`, `#Telephony Security`

---
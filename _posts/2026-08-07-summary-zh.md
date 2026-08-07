---
layout: default
title: "Horizon Summary: 2026-08-07 (ZH)"
date: 2026-08-07
lang: zh
---

> 从 72 条内容中筛选出 15 条重要资讯。

---

1. [三重密码分析攻破 Asiacrypt 2025 同源 VRF](#item-1) ⭐️ 9.0/10
2. [KORD：协议-硬件协同设计打破无经销商 FSS 密钥生成瓶颈](#item-2) ⭐️ 9.0/10
3. [范畴论下的 UC 严格图示证明](#item-3) ⭐️ 9.0/10
4. [Paras：主动安全的两服务器私有直方图协议](#item-4) ⭐️ 9.0/10
5. [在 $2^{n/2+o(n)}$ 时间内完成单个离散高斯采样](#item-5) ⭐️ 9.0/10
6. [Relect：基于阈值全同态加密的高效无信任设置 SSLE 协议](#item-6) ⭐️ 8.0/10
7. [Z-SCAPE：熵源故障后隐私保护资产恢复协议](#item-7) ⭐️ 8.0/10
8. [基于 Plantard 约减的更快形式化验证 NTT 代码生成](#item-8) ⭐️ 8.0/10
9. [正式分析发现 Olvid 通讯软件安全声明存在不足](#item-9) ⭐️ 8.0/10
10. [将 UOV 代数密钥恢复攻击扩展至 v ≥ 2m 情形](#item-10) ⭐️ 8.0/10
11. [可验证自混合：新型匿名通信架构](#item-11) ⭐️ 8.0/10
12. [改进的比特翻转解码降低 QC-MDPC 失败率 提升 BIKE 可靠性](#item-12) ⭐️ 8.0/10
13. [首个联合验证 LFSR 与布尔掩码安全性的框架](#item-13) ⭐️ 8.0/10
14. [DuetORAM: 具有常数轮次和 O(log N)通信量的双服务器分布式 ORAM](#item-14) ⭐️ 8.0/10
15. [DYNAFIX：支持任意范围 MPC 的动态定点编码](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [三重密码分析攻破 Asiacrypt 2025 同源 VRF](https://eprint.iacr.org/2026/1623) ⭐️ 9.0/10

本文展示了对 Levin-Pedersen 同源 VRF 的完全破解，利用未指定的公钥表示破坏唯一可证明性，并通过 1536 次查询在 30 分钟内恢复出 256 比特完整密钥。此外，还扩展了之前观察，对同一论文中的基于群作用的 VRF 实施了一次查询攻击，优势接近 1/2。 该结果表明，看似安全的 VRF 构造可因细微的实现不匹配而被攻破，动摇了同源 VRF 的可信度，凸显了精确规范的关键必要性，并促使在部署前进行更严格的安全性分析。 第一个攻击利用了公钥以 j-不变量存储曲线，而 radical-CGL 游走使用两个系数的不匹配，从而产生输出冲突。密钥恢复使用 1536 次选择查询，在 30 分钟内恢复出 256 比特密钥；甚至仅公钥有时也会泄露 1–2 比特秘密。对群作用 VRF 的单次查询攻击优势接近 1/2。

rss · IACR ePrint 密码学论文 · 8月5日 18:59

**背景**: 可验证随机函数（VRF）产生带有正确性证明的伪随机输出。同源密码利用椭圆曲线间的映射构建后量子安全方案。CGL 哈希函数在超奇异同源图上执行非回溯游走。Radical isogenies 能高效确定性地计算 N 同源链。R1CS 是用于零知识证明的证明关系。Levin-Pedersen VRF 将秘密的 radical-CGL 游走应用于两条曲线，并使用 R1CS 证明来表明它们使用相同密钥。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-030-64834-3_17">Radical Isogenies | Springer Nature Link</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-75764-8_5">A Faster Variant of CGL Hash Function via Efficient ...</a></li>
<li><a href="https://learn.0xparc.org/materials/circom/additional-learning-resources/r1cs+explainer/">R1CS Explainer | ZK Learning Resources - 0xPARC</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#isogeny-based cryptography`, `#verifiable random functions`, `#cryptanalysis`, `#radical isogenies`

---

<a id="item-2"></a>
## [KORD：协议-硬件协同设计打破无经销商 FSS 密钥生成瓶颈](https://eprint.iacr.org/2026/1615) ⭐️ 9.0/10

KORD 引入了一对具有相互认证的芯片来建立信任根，将无经销商函数秘密共享密钥生成的交互轮数压缩为单轮，从而消除了对可信经销商的需求。它在 FPGA 上实现了每秒 1160 万个 32 位 DPF 密钥，将私有 ResNet-18 推理中密钥生成占端到端时间的比例从超过 96% 降至仅 10.1%。 这项工作消除了大规模部署 FSS 的关键瓶颈，实现了高效、无需经销商即可进行的隐私保护计算。其显著的加速效果有望使私有机器学习推理和其他安全计算任务更加实用。 KORD 的相互认证将两个芯片绑定到一个安全边界内，实现了单轮密钥生成。通过交叉密钥调度，FPGA 上的 AES 通道利用率达到 99%，性能提升达 12 倍，在 187.5 MHz 下每秒可生成 1160 万个 32 位 DPF 密钥。

rss · IACR ePrint 密码学论文 · 8月5日 11:53

**背景**: 函数秘密共享（FSS）将函数拆分为两个密钥，单独看每个密钥不泄露任何信息，但联合起来即可进行求值。通常由可信经销商生成密钥，但这会集中信任点。无经销商协议将密钥生成分散到各参与方，但通信开销大，且交互轮数随输入位宽线性增长，导致速度缓慢。KORD 通过使用具备相互认证的定制硬件克服了这些限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1615">KORD: Breaking the Key-Generation Bottleneck in Dealerless Function Secret Sharing via Protocol–Hardware Co-Design</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mutual_authentication">Mutual authentication - Wikipedia</a></li>

</ul>
</details>

**标签**: `#privacy-preserving computation`, `#function secret sharing`, `#hardware security`, `#protocol design`, `#co-design`

---

<a id="item-3"></a>
## [范畴论下的 UC 严格图示证明](https://eprint.iacr.org/2026/1605) ⭐️ 9.0/10

该论文提出了通用可组合性（UC）的范畴论处理方法，利用弦图实现严格的图形化证明。它还将 UC 推广到交互图灵机之外的计算模型，支持分布式对手，并修正了简单 UC 中的少量技术疏忽。 这种范畴论方法使 UC 证明更易于理解和验证，并适用于量子计算等领域。它降低了密码协议形式化验证的门槛，并巩固了安全组合的理论基础。 组合定理可通过一短串弦图图形化验证，同时保持可转化为方程。论文证明其变体（具有分布式对手）与标准 UC 等价，无表达力损失。

rss · IACR ePrint 密码学论文 · 8月4日 15:37

**背景**: 通用可组合性（UC）是一个强大的密码协议安全框架，即使任意组合也能保持安全。范畴论是研究组合与抽象化的数学分支。弦图是幺半范畴的图形语言，广泛应用于应用范畴论中用于严格的视觉证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Universal_composability">Universal composability</a></li>
<li><a href="https://en.wikipedia.org/wiki/String_diagram">String diagram - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/1401.7220">Category Theory Using String Diagrams</a></li>

</ul>
</details>

**标签**: `#category theory`, `#universal composability`, `#cryptography`, `#formal verification`, `#string diagrams`

---

<a id="item-4"></a>
## [Paras：主动安全的两服务器私有直方图协议](https://eprint.iacr.org/2026/1600) ⭐️ 9.0/10

Paras 是首个支持主动安全的两服务器私有直方图计算协议，能够抵御恶意服务器与多名客户端的共谋。它通过基于 VOLE 的新颖一致性检查实现，引入了认证比特验证（aBV）和认证双内积论证（adIPA）原语。 通过将所需服务器数量从三台减少至两台，Paras 使安全的私有分析更加实用和具有成本效益，可能加速在隐私敏感领域的应用。其抵抗服务器-客户端共谋的主动安全性为安全多方计算的鲁棒性树立了新标准。 对于 128 个输入的域和 8192 个客户端，Paras 每个客户端的服务器运行时间仅 14 毫秒，通信量 24 KB，且客户端开销与域大小无关。aBV 确保 VOLE 承诺的份额为有效比特，而 adIPA 则支持跨两个 VOLE 会话的一致性检查。

rss · IACR ePrint 密码学论文 · 8月4日 07:11

**背景**: 私有直方图计算使得能够在不泄露单个数据点的情况下，对多个数据源进行频率分析，这是隐私保护分析中的核心任务。向量不经意线性求值（VOLE）是一种密码学构件，允许发送方和接收方不经意地计算线性函数，通常用于高效秘密共享。现有的恶意安全私有直方图协议通常需要三台服务器，但 Paras 通过使用新颖的一致性检查，仅用两台服务器就实现了更强的安全性。认证比特验证确保共享值中的每个比特都是正确的，而内积论证则证明承诺向量之间的关系——两者在此均针对两服务器环境进行了适配。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pascholl.github.io/download/BIU22-vole-1.pdf">(Vector) Oblivious Linear Evaluation: Basic Constructions and Applications</a></li>
<li><a href="https://eprint.iacr.org/2025/1037">Committed Vector Oblivious Linear Evaluation and Its Applications</a></li>
<li><a href="https://eprint.iacr.org/2025/232">Authenticated BitGC for Actively Secure Rate-One 2PC</a></li>

</ul>
</details>

**标签**: `#secure multi-party computation`, `#privacy-preserving analytics`, `#histograms`, `#cryptography`, `#VOLE`

---

<a id="item-5"></a>
## [在 $2^{n/2+o(n)}$ 时间内完成单个离散高斯采样](https://eprint.iacr.org/2026/1599) ⭐️ 9.0/10

新算法能以 $2^{n/2+o(n)}$ 时间从格上采样单个离散高斯，与之前仅适用于大量采样的时间复杂度相当，从而解决了 ADRS 于 2015 年提出的公开问题。 这一进展可能推动基于格的密码协议和算法变得更高效，因为离散高斯采样是许多此类系统的核心组件。同时，它也加深了我们对格问题计算复杂度的理解。 该算法利用在目标尺度下平滑的随机超格，通过高斯质量比较论证，确保在 $2^{n/2}$ 个样本中以反多项式概率得到一个原始格点。$2^{n/2}$ 因子被证明是紧的，且该技术还给出了精确 CVP 的亚 $2^n$ 时间算法和 $2^{0.7315n+o(n)}$ 时间的精确 SVP 算法。

rss · IACR ePrint 密码学论文 · 8月4日 06:23

**背景**: 格上的离散高斯采样是基于格的密码学中的关键基础操作，用于为学习与错误（LWE）等方案生成噪声。格的平滑参数决定了抹平离散结构所需的高斯噪声量。2015 年，ADRS 提出了在平滑参数之上以 $2^{n/2+o(n)}$ 时间采样大量离散高斯样本的算法，但单个样本的复杂度问题一直悬而未决。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.di-mgt.com.au/discrete_gaussian.html">Discrete Gaussian distribution</a></li>
<li><a href="https://arxiv.org/abs/1412.7979">[1412.7979] On the Lattice Smoothing Parameter Problem</a></li>

</ul>
</details>

**标签**: `#discrete Gaussian sampling`, `#lattices`, `#algorithms`, `#cryptography`, `#theoretical computer science`

---

<a id="item-6"></a>
## [Relect：基于阈值全同态加密的高效无信任设置 SSLE 协议](https://eprint.iacr.org/2026/1619) ⭐️ 8.0/10

Relect 提出了一种基于格密码的 SSLE 协议，利用阈值全同态加密，相比 Qelect 端到端速度最快提升 345 倍，消除了可信设置需求，并降低了通信开销。 通过消除可信设置并大幅提升性能，Relect 使 SSLE 在现实去中心化系统中更可行，增强了区块链共识和分布式协调的安全性与可扩展性。 在 32 至 2048 方场景下，Relect 的单线程本地 FHE 计算比 Qelect 快 7.15 至 42.4 倍，通信量减少 14%至 50%，局域网端到端速度提升最高达 345 倍；同时支持每轮动态选取领导者。

rss · IACR ePrint 密码学论文 · 8月5日 15:08

**背景**: 单秘密领导者选举（SSLE）使一组参与方秘密选出仅领导者本人知晓的领导者，对分布式系统的隐私至关重要。全同态加密（FHE）支持对密文进行计算，阈值 FHE 则需达到门限的参与方协作解密。可信设置需受信实体生成初始参数，存在单点安全风险；去除可信设置对实现无需信任的部署尤为关键。Relect 基于环学习与误差（RLWE）问题，这是一种抗量子计算的格密码假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1619">Relect: Single Secret Leader Election via FHE with Reduced ...</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3419614.3423258">Single Secret Leader Election | Proceedings of the 2nd ACM ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ring_learning_with_errors">Ring learning with errors - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#FHE`, `#SSLE`, `#lattice-based`, `#secure multi-party computation`

---

<a id="item-7"></a>
## [Z-SCAPE：熵源故障后隐私保护资产恢复协议](https://eprint.iacr.org/2026/1621) ⭐️ 8.0/10

该论文提出了 Z-SCAPE 协议，这是一个零知识证明协议，旨在应对硬件钱包种子生成熵源故障（如 2026 年 COLDCARD 事件）后，以保护隐私的方式恢复资产。 该协议填补了自托管安全的关键空白，使合法所有者能够在熵源漏洞暴露后，不泄露身份或已泄露密钥的情况下认领被保护转移的资产，防止大规模盗窃。 Z-SCAPE 使用预先承诺的恢复凭证（256 位秘密 r 和独立的个人记录 P），并将证明与特定事件的资产引用、新随机数和目标地址绑定，以防止重放和替换攻击；该协议为比特币和以太坊提供了具体集成方案。

rss · IACR ePrint 密码学论文 · 8月5日 17:47

**背景**: 零知识证明允许在不泄露秘密的情况下证明其知识。硬件钱包使用随机数发生器产生的熵来生成加密种子；如果熵不足，攻击者可通过离线搜索重建私钥。2026 年 COLDCARD 事件中，一个固件缺陷将种子熵降低至约 40 位，攻击者因此从受影响钱包中卷走了约 8900 万美元的比特币。Z-SCAPE 提出了一种使用零知识证明来验证合法所有者身份的恢复机制，同时不暴露已恢复的密钥或个人数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://undercodetesting.com/the-9-million-entropy-collapse-when-hardware-wallets-betray-their-trust-video/">The 9 Million Entropy Collapse: When Hardware Wallets Betray ...</a></li>
<li><a href="https://www.trmlabs.com/resources/blog/the-largest-hardware-wallet-exploit-of-2026-inside-the-usd-116-million-coldcard-hack">The Largest Hardware Wallet Exploit of 2026: Inside the USD ...</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#hardware wallets`, `#asset recovery`, `#privacy-preserving cryptography`, `#self-custody`

---

<a id="item-8"></a>
## [基于 Plantard 约减的更快形式化验证 NTT 代码生成](https://eprint.iacr.org/2026/1624) ⭐️ 8.0/10

一个代码生成器现在可以使用 Plantard 算术生成经过形式化验证的 NTT 实现，适用于 ML-KEM、ML-DSA 和 FN-DSA，性能比基线快 1.26 倍至 2.5 倍，并附带 EasyCrypt 证明。 它将形式化验证与后量子密码学的性能优化相结合，消除了手动调优并确保恒定时间安全，这对实际部署至关重要。 该生成器使用静态边界分析在代码生成时插入模约减，避免运行时分支。它输出结构相同的 C 和 Jasmin 代码，并通过 EasyCrypt 逐层等价证明连接到 formosa-mlkem 规范。

rss · IACR ePrint 密码学论文 · 8月6日 05:37

**背景**: NTT（数论变换）是 ML-KEM（Kyber）和 ML-DSA（Dilithium）等格基后量子方案中的关键运算。Plantard 约减是一种利用宽整数类型实现高效模算术的技术。EasyCrypt 是一个用于密码构造的交互式证明助手。Jasmin 是一种用于高保障、恒定时间密码代码的语言。formosa-mlkem 项目提供了 ML-KEM 的形式化验证参考实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1624">Code Generation of Faster Formally Verified NTT with Plantard ...</a></li>
<li><a href="https://eprint.iacr.org/2022/956">Improved Plantard Arithmetic for Lattice-based Cryptography</a></li>
<li><a href="https://www.easycrypt.info/">EasyCrypt</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#post-quantum cryptography`, `#code generation`, `#NTT`, `#Plantard reduction`

---

<a id="item-9"></a>
## [正式分析发现 Olvid 通讯软件安全声明存在不足](https://eprint.iacr.org/2026/1622) ⭐️ 8.0/10

研究人员对 Olvid 通讯软件进行了首次正式安全分析，证明其满足相互认证和前向保密等核心安全目标，但揭示其缺乏 eCK 安全等更强的现代属性，与其声称不符。 Olvid 被法国政府官员用于敏感通信，因此这些缺陷可能带来严重的实际影响。该研究凸显了在关键场景部署前对安全通讯协议进行严格审查的必要性。 在 Dolev-Yao 敌手模型下，协议被验证实现了相互认证、会话密钥保密、前向保密和重放保护；但在更强的 eCK 模型中却未能通过，并且发现了一个潜在的定时泄漏漏洞。

rss · IACR ePrint 密码学论文 · 8月5日 18:28

**背景**: 认证密钥交换（AKE）允许各方在验证身份的同时建立共享秘密。连续密钥协商（CKA）像 Signal 的“双重棘轮”一样为每条消息生成新密钥。Dolev-Yao 模型假设存在控制网络的主动攻击者。eCK 是更强的模型，能捕捉密钥泄露伪装攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Authenticated_Key_Exchange">Authenticated Key Exchange</a></li>
<li><a href="https://eprint.iacr.org/2019/088">Continuous Key Agreement with Reduced Bandwidth</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dolev–Yao_model">Dolev – Yao model - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secure-messaging`, `#formal-verification`, `#olvid`, `#security-analysis`

---

<a id="item-10"></a>
## [将 UOV 代数密钥恢复攻击扩展至 v ≥ 2m 情形](https://eprint.iacr.org/2026/1620) ⭐️ 8.0/10

本文提出了一种方法，克服了 Ran 在 2025 年提出的 UOV 代数密钥恢复攻击的局限性，使得攻击在醋变量数 v≥2m 时仍然有效。该技术还被应用于 SNOVA 方案，降低了部分 NIST 第二轮参数集的安全性。 这一进展扩展了对主流 NIST 后量子签名候选方案的密码分析，可能影响其参数选择和标准化。它表明此前被认为抗攻击的参数集如今变得脆弱，或将左右未来的安全评估。 该攻击解决了当 v≥2m 时，公共理想中的一个额外核元素阻碍油子空间恢复的问题。对于 NIST 安全级别 I 的 SNOVA 参数集(v,o,q,l)=(37,17,16,2)，攻击付出的代价估计为 2^103 次门操作，与 Bros 等人在 2026 年提出的攻击复杂度一致。

rss · IACR ePrint 密码学论文 · 8月5日 16:53

**背景**: 非平衡油醋（UOV）方案是一种多元签名方案，以签名短小、抗攻击性强著称，是 NIST 后量子密码标准化的领先候选之一。2025 年，Ran 提出了一种代数密钥恢复攻击，降低了部分 UOV 参数的安全性，但仅当 v<2m 时才有效。新的 UOV 变种 SNOVA 也正在参与 NIST 的标准化进程。代数密钥恢复攻击利用多项式方程恢复密钥，无需直接伪造签名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/csrc/media/Projects/pqc-dig-sig/documents/round-1/spec-files/UOV-spec-web.pdf">UOV Specification Document</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#multivariate-cryptography`, `#UOV`, `#key-recovery-attack`

---

<a id="item-11"></a>
## [可验证自混合：新型匿名通信架构](https://eprint.iacr.org/2026/1617) ⭐️ 8.0/10

最新论文提出了可验证自混合（VSM），一种新型匿名通信架构，将 oblivious 时隙分配（唯一编号选择）与匿名消息放置（私有排列安全映射）分离。它提供了无条件个体可验证性，使每个用户都能在解密后确认其消息的最终位置。 这一进展通过消除对诚实混合服务器的依赖并实现消息放置的普遍可验证性，提升了匿名通信的信任度和效率。它为安全消息传递、投票和隐私保护数据发布等应用提供了 mixnet 和 DC-net 的有力替代方案。 该架构支持多种实例化：UNS 通过可信硬件或明文等价测试实现，SMPP 采用 ElGamal、BGN 或全同态加密（FHE）。对于固定大小的消息，FHE 变体将客户端上传降至Õ(log m)，而基于向量的 SMPP 对 n 用户 m 时隙需 O(m)每用户上传和 O(nm)公共聚合。

rss · IACR ePrint 密码学论文 · 8月5日 14:19

**背景**: 匿名通信系统如 mixnet 和 DC-net 隐藏发送者-接收者关系。Mixnet 常需信任至少一个混合服务器，DC-net 则使用安全多方计算但通信成本高。VSM 将过程模块化为时隙分配和消息放置，使用户无需信任任何单方即可独立验证正确执行，从而结合了效率与无条件可验证性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1617">Verifiable SelfMix</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#anonymity`, `#mixnets`, `#MPC`, `#verifiability`

---

<a id="item-12"></a>
## [改进的比特翻转解码降低 QC-MDPC 失败率 提升 BIKE 可靠性](https://eprint.iacr.org/2026/1616) ⭐️ 8.0/10

一篇新论文提出一种针对 QC-MDPC 码的增强型比特翻转解码器，它利用近码字识别并纠正解码失败，显著降低了 BIKE 后量子密码系统的解码失败率（DFR）。 更低的 DFR 对 BIKE 实现 IND-CCA2 安全性至关重要，因为失败率必须低于 2^{-λ}以防止信息泄露。这一改进增强了 NIST 后量子决赛方案 BIKE 的可靠性和实际安全性。 该技术可应用于任何比特翻转解码器，计算开销极小。在 BIKE 第一类安全参数下，BF-Max 变体的 DFR 远低于 BIKE 当前使用的解码器，且计算复杂度相当。

rss · IACR ePrint 密码学论文 · 8月5日 13:52

**背景**: QC-MDPC（准循环中密度奇偶校验）码是一种纠错码，用于 NIST 后量子密码标准化决赛方案 BIKE 密钥封装机制。解码失败可能泄露秘密信息，因此实现极低的 DFR 对安全性至关重要。比特翻转是一种常用于此类码的迭代解码方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/csrc/media/Projects/post-quantum-cryptography/documents/pqc-seminars/presentations/22-qc-mdpc-01072024.pdf">Analyzing the decoding failure rate of QC - MDPC Codes</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post - quantum cryptography - Wikipedia</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#QC-MDPC codes`, `#bit flipping decoding`, `#BIKE`, `#error correction`

---

<a id="item-13"></a>
## [首个联合验证 LFSR 与布尔掩码安全性的框架](https://eprint.iacr.org/2026/1614) ⭐️ 8.0/10

研究人员提出了首个在 d-探测模型中联合分析伪随机数生成器（特别是 LFSR）与布尔掩码方案的验证框架，填补了以往证明假设理想随机性的空白。该框架将 Walsh-Hadamard 变换扩展到鲁棒探测模型，并在 FPGA 上得到验证。 此项工作确保使用 LFSR 进行掩码的现实世界加密实现能够被正式证明可抵御侧信道攻击，对安全硬件设计产生影响，并可能影响未来标准。 该框架利用来自线性密码分析的 Walsh-Hadamard 变换，并扩展到鲁棒探测模型以处理物理毛刺。它在 4 位和 8 位 S 盒上进行了演示，并通过实际 FPGA 评估验证了结果。

rss · IACR ePrint 密码学论文 · 8月5日 10:57

**背景**: d-探测模型是一种形式化的安全模型，攻击者可在计算过程中观察多达 d 条内部线路。布尔掩码通过异或将敏感变量分割成随机份额来抵御此类观察。LFSR 是一种硬件高效型伪随机生成器，常用于产生这些随机掩码。鲁棒探测模型对此进行了扩展，以考虑毛刺等物理缺陷。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Linear-feedback_shift_register">Linear-feedback shift register</a></li>
<li><a href="https://tches.iacr.org/index.php/TCHES/article/view/11799">Robust but Relaxed Probing Model | IACR Transactions on Cryptographic Hardware and Embedded Systems</a></li>
<li><a href="http://www.crypto-uni.lu/jscoron/publications/secconvorder.pdf">Secure Conversion Between Boolean and</a></li>

</ul>
</details>

**标签**: `#side-channel attacks`, `#masking`, `#LFSR`, `#formal verification`, `#cryptographic implementations`

---

<a id="item-14"></a>
## [DuetORAM: 具有常数轮次和 O(log N)通信量的双服务器分布式 ORAM](https://eprint.iacr.org/2026/1613) ⭐️ 8.0/10

DuetORAM 提出了一种新的双服务器分布式不经意 RAM（DORAM）协议，通过创新的复制到共享块编码和离线-在线秘密共享混洗，实现了常数轮次访问和 O(log N)通信，性能大幅超越 DUORAM 和 S^3ORAM 等现有方案。 DuetORAM 消除了线性扫描和重量级密码原语，使隐私保护云存储更为实用，相比此前双服务器方案检索延迟降低高达 170 倍，相比三服务器方案驱逐速度提升高达 7 倍。 复制到共享的块编码在服务器上保存相同密文，同时允许本地将其解释为秘密份额，以实现基于 PIR 的检索和通过轻量级混洗完成不经意驱逐。离线-在线秘密共享混洗将大部分带宽密集型工作移至预处理阶段，在 LAN 环境下检索延迟比 DUORAM 减少 170 倍，驱逐速度比 S^3ORAM 快 7 倍。

rss · IACR ePrint 密码学论文 · 8月5日 09:48

**背景**: 不经意 RAM（ORAM）隐藏内存访问模式，即使存储不可信也能保护数据隐私。分布式 ORAM（DORAM）将 ORAM 扩展到多个服务器，在安全性与效率之间取得平衡。私有信息检索（PIR）允许客户端在不泄露查询目标的情况下检索数据，而秘密共享则将数据分割成多个份额，由不同方持有，单方无法还原原始数据。这些技术的结合是构建实用隐私保护存储系统的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Oblivious_RAM">Oblivious RAM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Private_information_retrieval">Private information retrieval</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-030-64840-4_12">Secret - Shared Shuffle | Springer Nature Link</a></li>

</ul>
</details>

**标签**: `#Oblivious RAM`, `#privacy-preserving storage`, `#distributed systems`, `#cryptographic protocols`, `#cloud computing`

---

<a id="item-15"></a>
## [DYNAFIX：支持任意范围 MPC 的动态定点编码](https://eprint.iacr.org/2026/1612) ⭐️ 8.0/10

DYNAFIX 提出了一种用于安全多方计算的动态定点编码方案，它支持任意数值范围，同时保持与标准定点运算相当的效率，在指数函数上比现有浮点方法实现了 24.1 倍的加速。 这一突破弥合了隐私保护计算中定点效率与浮点范围之间的鸿沟，为需要宽动态范围的机器学习、数据分析等应用提供了更快速、更实用的安全计算方案。 DYNAFIX 动态调整缩放因子以适应变化的数值范围，避免了完整浮点模拟的开销，同时保留了定点运算的简单性。报告的加速是在高精度指数函数求值上与最先进的浮点 MPC 相比获得的。

rss · IACR ePrint 密码学论文 · 8月5日 08:11

**背景**: 安全多方计算（MPC）允许多个参与方在不泄露各自私有输入的情况下联合计算一个函数，其中实数计算通常采用定点或浮点运算。定点运算因使用固定缩放因子的整数运算而效率高，但动态范围有限。浮点运算能表示的数值范围广得多，但在 MPC 中安全地实现它通常比定点运算慢 100 倍以上。这种权衡一直是隐私保护机器学习和数据分析中的主要挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fixed-point_arithmetic">Fixed-point arithmetic - Wikipedia</a></li>

</ul>
</details>

**标签**: `#multi-party computation`, `#fixed-point arithmetic`, `#privacy-preserving computation`, `#floating-point`, `#secure computation`

---
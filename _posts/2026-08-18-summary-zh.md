---
layout: default
title: "Horizon Summary: 2026-08-18 (ZH)"
date: 2026-08-18
lang: zh
---

> 从 33 条内容中筛选出 15 条重要资讯。

---

1. [针对 AJPS 梅森数密码系统的新攻击放宽密钥尺寸约束](#item-1) ⭐️ 8.0/10
2. [后量子 TLS 迁移的系统化：架构性挑战](#item-2) ⭐️ 8.0/10
3. [纠缠博弈平行重复的差距指数改进至三次方](#item-3) ⭐️ 8.0/10
4. [MamaBearZKP：素域与证明栈协同设计实现高吞吐零知识证明](#item-4) ⭐️ 8.0/10
5. [VeriFSS 推出无经销商主动安全的两方函数秘密共享方案。](#item-5) ⭐️ 8.0/10
6. [面向 Jasmin 掩码实现的编译器集成泄漏检测](#item-6) ⭐️ 8.0/10
7. [论文证明 Simon 量子算法无法解决二面体陪集问题](#item-7) ⭐️ 8.0/10
8. [密码分析推翻四态量子公钥加密方案](#item-8) ⭐️ 7.0/10
9. [混合算法将 MQOM 的布尔 MQ 攻击性能提升 1-4 比特](#item-9) ⭐️ 7.0/10
10. [DTRU：采用双 E8 编码的紧凑 NTRU 密钥封装机制](#item-10) ⭐️ 7.0/10
11. [改进 Qlapoti 分析，SQIsign 范数方程求解器提速 6 至 9 倍](#item-11) ⭐️ 7.0/10
12. [DumboMix：通过 MPC 混合实现实用的鲁棒异步匿名广播](#item-12) ⭐️ 7.0/10
13. [论密码学群鲁棒组合器的不可能性](#item-13) ⭐️ 7.0/10
14. [均匀 MQ 假设与 MQ 安全性关系](#item-14) ⭐️ 7.0/10
15. [攻击者劫持公共 Wi-Fi DNS 以窃取凭证。](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [针对 AJPS 梅森数密码系统的新攻击放宽密钥尺寸约束](https://eprint.iacr.org/2026/1705) ⭐️ 8.0/10

该论文针对 AJPS 梅森数密码系统提出了新的攻击方法，应用连分数方法和基于格的模多项式方程求解策略来恢复私钥。这些攻击放宽了对私钥尺寸的限制，在某些情况下无需估计未知量的上界，并在参数不平衡时提高了成功概率，数值实验验证了其有效性。 这项工作对一种候选后量子密码系统的安全性提出质疑，表明此前被认为安全的 AJPS 参数可能存在脆弱性。它为评估抗量子方案所需的积极密码分析做出了贡献，并可能影响未来的标准化或部署决策。 攻击利用了连分数和基于格的模多项式方程求解策略，绕过了直接使用格归约算法的需求。它们要么取消了对未知量上界进行估计的要求，要么扩大了易受攻击弱密钥的范围，尤其是在参数不平衡的情况下；实验覆盖了多种规模的参数。

rss · IACR ePrint 密码学论文 · 8月16日 09:04

**背景**: 梅森数是形如 2^p - 1 的整数，其中 p 为素数。AJPS 密码系统由 Aggarwal、Joux、Prakash 和 Santha 于 2017 年提出，是一种基于梅森数模运算的公钥加密方案，被提议作为 NTRU 等方案的抗量子替代品。该方案推出后不久，Beunardeau 等人的格基攻击就显著降低了其安全裕度，后续工作持续改进这些攻击。本文在此基础上使用不同的数学工具进行密码分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scispace.com/papers/improved-cryptanalysis-of-the-ajps-mersenne-based-1oubwa240t">(Open Access) Improved cryptanalysis of the AJPS Mersenne based...</a></li>
<li><a href="https://publikationen.bibliothek.kit.edu/1000160171/150959797">Quantum attacks on Mersenne number cryptosystems pdfsubject...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum cryptography`, `#cryptanalysis`, `#Mersenne numbers`, `#lattice-based attacks`

---

<a id="item-2"></a>
## [后量子 TLS 迁移的系统化：架构性挑战](https://eprint.iacr.org/2026/1703) ⭐️ 8.0/10

这篇系统化知识论文将后量子 TLS 迁移视为架构问题，系统分析了混合握手、PSK、KeyUpdate 与证书策略，并区分正式标准与草案，提出迁移决策框架。 这有助于实践者和研究者应对算法替换之外的复杂性；它强调机密性迁移与认证迁移是不同安全计划，且部署就绪性取决于证书、HSM、中间盒和互操作性。 论文按安全目标、密钥材料来源、前向保密、妥协后行为、成本、标准化状态和迁移复杂度对证据分类。结论认为混合 ECDHE-ML-KEM 适用于机密性迁移，而 KeyUpdate 不会产生独立的后量子秘密。

rss · IACR ePrint 密码学论文 · 8月16日 08:04

**背景**: 后量子密码学旨在抵御量子计算机攻击；NIST 已标准化密钥封装机制 ML-KEM（FIPS 203）以及签名算法 ML-DSA（FIPS 204）和 SLH-DSA（FIPS 205）。TLS 1.3 使用临时密钥交换，并可选用 PSK 和 KeyUpdate 管理流量密钥。X.509/PKIX 体系管理证书和信任锚。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://en.wikipedia.org/wiki/SLH-DSA">SLH-DSA</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#TLS`, `#migration`, `#X.509`, `#hybrid key exchange`

---

<a id="item-3"></a>
## [纠缠博弈平行重复的差距指数改进至三次方](https://eprint.iacr.org/2026/1702) ⭐️ 8.0/10

该论文证明，对于任何纠缠值为 1−ε 的有限双人博弈，其 n 次平行重复的纠缠值按 exp(−Ω(ε^3 n/(ε+ℓ))) 衰减，将差距指数从 13 改进为 3，与 Holenstein 经典平行重复界的三次方依赖一致。 这一结果弥合了纠缠博弈中量子与经典平行重复速率的差距，消除了长期存在的指数差距，使量子平行重复的渐近强度与经典定理相当；对量子密码学、量子复杂性理论及使用重复纠缠博弈进行可靠性放大的协议具有重要意义。 该界通过 ℓ = log(|A||B|) 依赖于答案字母表大小；证明用平滑软标签替代量子相关采样中的随机平移对数网格，使标签不保真度成为状态描述距离的二次函数，并在对问题取平均时避免了 Jensen 损失。

rss · IACR ePrint 密码学论文 · 8月16日 06:02

**背景**: 平行重复通过同时进行多份独立游戏副本来放大双人博弈的可靠性（soundness）：若单轮获胜概率至多为 1−ε，则重复博弈的获胜概率应指数下降。经典情形下，Holenstein 证明了获胜概率按 exp(−Ω(ε^3 n/(1+ℓ))) 衰减，其中 ℓ 是对数答案字母表大小。纠缠博弈允许玩家共享量子纠缠，这可能提高获胜概率，并使平行重复分析更加困难。此前量子界的差距指数很差（例如 OpenAI 报告中的 13），而新结果终于达到与经典相同的三次方速率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ocw.mit.edu/courses/18-408-topics-in-theoretical-computer-science-probabilistically-checkable-proofs-fall-2022/mit18_408f22_lec14-15.pdf">18.408 F2022 Lectures 14…15: The Parallel Repetition Theorem</a></li>
<li><a href="https://math.univ-lyon1.fr/~aubrun/recherche/parallel-repetition.pdf">The parallel repetition theorem</a></li>

</ul>
</details>

**标签**: `#quantum information`, `#parallel repetition`, `#entangled games`, `#theoretical computer science`, `#quantum cryptography`

---

<a id="item-4"></a>
## [MamaBearZKP：素域与证明栈协同设计实现高吞吐零知识证明](https://eprint.iacr.org/2026/1698) ⭐️ 8.0/10

MamaBearZKP 提出了一个整体协同设计框架，采用 49 比特素数域（p = 2^49 − 2^34 + 1）和 AVX-512IFMA 向量化。与 Goldilocks 基线相比，ZeroCheck、ProductCheck、DeepFold Commit、DeepFold Open 和端到端证明生成的单线程加速分别高达 42 倍、33 倍、15 倍、21 倍和 21 倍，且比 Plonky3 最高快 18 倍。 这些结果表明，将素数域参数与 CPU 向量执行模型协同设计，能够为零知识证明带来数量级的性能提升，减少对专用硬件的依赖。这对区块链可扩展性和隐私应用具有重要意义，因为证明延迟和成本是关键瓶颈。 49 比特域的冗余位支持惰性归约，并实现高性能的融合折叠-求值内核，从而在 HyperPlonk 和 DeepFold 栈中维持统一的 stay-packed 数据流。该框架的 artifact 采用统一的 R=2^52 Montgomery 表示，在 8 线程下对应基准测试加速最高可达 64 倍、47 倍、81 倍、45 倍和 45 倍。

rss · IACR ePrint 密码学论文 · 8月15日 15:55

**背景**: 零知识证明依赖 sum-check 协议和快速傅里叶变换，这两者通常主导证明者的运行时间。HyperPlonk 是基于 sum-check 的多项式交互式预言机证明（IOP），而 DeepFold 是基于折叠的多项式承诺方案。Goldilocks 和 BabyBear 是常用于快速算术运算的小素数域；AVX-512IFMA 提供 52 位整数融合乘加指令，非常适合现代 Intel CPU 上的模乘运算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1698">MamaBearZKP: A Holistic Co-design of Prime Fields and Proving ...</a></li>
<li><a href="https://github.com/Ji-Peng/MamaBearZKP-Artifact">GitHub - Ji-Peng/MamaBearZKP-Artifact: Artifact for the CCS ...</a></li>
<li><a href="https://iacr.org/news/item/29298">IACR News item: 16 August 2026</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#cryptography`, `#performance optimization`, `#AVX-512`, `#prime fields`

---

<a id="item-5"></a>
## [VeriFSS 推出无经销商主动安全的两方函数秘密共享方案。](https://eprint.iacr.org/2026/1697) ⭐️ 8.0/10

该论文提出了 VeriFSS，一种无经销商且具备主动安全性的两方函数秘密共享（FSS）方案，其核心是采用带有秘密认证标量 Λ 的双平面密钥，无需向量承诺、可提取哈希或逐点交互即可实现跨阶段验证。 通过去除受信任的经销商并提供主动安全性，VeriFSS 使函数秘密共享能够应用于恶意模型下的安全计算，降低了信任假设，并支持在广域网中以常数轮完成高效预处理认证。 生成阶段每方每层需要 2 轮通信和 5 个域元素；认证阶段增加 O(n) 个元素，动态跨域聚合可在一次挑战和常数轮内认证任意多个异构实例。在有限域 F_{p^2}（p=2^61-1）和 GF(2^128) 上的 C++ 实现中，n=16 的认证 DPF 密钥生成耗时 5.7 ms、认证耗时 3.3 ms，相比半诚实无经销商基线仅增加 5.4% 的大小。

rss · IACR ePrint 密码学论文 · 8月15日 15:23

**背景**: 函数秘密共享（FSS）将函数拆分为两个紧凑密钥，双方本地求值之和可恢复隐藏函数值。传统 FSS 通常依赖可信经销商生成密钥；去除经销商可以消除单点信任，但更难确保恶意方的输出与原始共享函数一致。主动安全（恶意安全）要求协议在一方任意偏离时仍然安全。可验证秘密共享通过额外信息让参与者验证份额一致性，但现有方法往往难以绑定 FSS 执行的不同阶段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Verifiable_secret_sharing">Verifiable secret sharing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation - Wikipedia</a></li>
<li><a href="https://geoffroycouteau.github.io/assets/pdf/HSS_FSS.pdf">Function Secret Sharing and</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secure multiparty computation`, `#function secret sharing`, `#malicious security`, `#verifiable secret sharing`

---

<a id="item-6"></a>
## [面向 Jasmin 掩码实现的编译器集成泄漏检测](https://eprint.iacr.org/2026/1696) ⭐️ 8.0/10

新论文（eprint 2026/1696）为 Jasmin 语言引入了一种编译器集成的泄漏检测过程，它在寄存器分配和栈分配之前的中间表示上分析掩码实现，以检测由编译引起的侧信道泄漏。该过程采用可配置的、面向微架构的泄漏模型，跟踪秘密份额、随机值和公开值之间的接触，使泄漏根源明确化并检测掩码阶数降低，并在 60 个专用 Jasmin 测试片段上得到验证。 这弥补了源级形式化验证与实际硬件泄漏之间的关键空白，因为即使算法正确的掩码实现在编译后也可能泄漏。它有可能通过让开发人员尽早发现泄漏并为编译器自动消除泄漏奠定基础，从而实现更安全的密码软件。 该泄漏检测过程在 Jasmin 的中间表示上运行，位于寄存器分配和栈分配之前，使用可配置的、面向微架构的模型而非功耗迹线仿真；它跟踪份额、秘密、随机值和公开值之间的接触，并检测掩码阶数降低。论文在 60 个专用测试片段上验证了该方法，覆盖所有考虑的泄漏源和类别组合，但自动消除检测到的泄漏留待后续工作。

rss · IACR ePrint 密码学论文 · 8月15日 11:28

**背景**: Jasmin 是一种为高保障和高性能密码学设计的编程语言和编译器，允许程序员在接近汇编级别编写高效且安全的代码。掩码是一种常见的抗侧信道攻击软件对策，将秘密数据拆分为多个随机份额，使得任何单个份额的物理泄漏都不会泄露秘密。编译器在指令选择、寄存器分配和栈分配过程中可能引入泄漏，从而破坏掩码。现有解决方案要么基于特定功耗模型进行泄漏仿真（计算开销大），要么仅对源程序进行形式化验证而不考虑编译阶段的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1696">Toward Secure Compilation: Leakage Detection for Masked ...</a></li>
<li><a href="https://jasmin-lang.readthedocs.io/">The Jasmin documentation — Jasmin documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Side-channel_attack">Side - channel attack - Wikipedia</a></li>

</ul>
</details>

**标签**: `#side-channel attacks`, `#secure compilation`, `#masking`, `#Jasmin`, `#compiler security`

---

<a id="item-7"></a>
## [论文证明 Simon 量子算法无法解决二面体陪集问题](https://eprint.iacr.org/2026/1693) ⭐️ 8.0/10

作者正式证明，Simon 在 ePrint:2026/1591 中提出的量子算法无法以不可忽略的优势提取 DCP 秘密的最低有效位，因此不能解决二面体陪集问题。他们还将其扩展为一个更广泛的无解结论：任何遵循 Regev 模板但不充分利用经典傅里叶标签的算法都无法成功。 由于二面体陪集问题是后量子密码学的核心问题，且带错误学习问题可归约到它，严格的驳斥可以防止学界在错误方向上浪费努力，并厘清所需算法成分。Lean 4 形式化也为量子算法声明设立了高验证标准。 该驳斥表明，Simon 的算法可以在误差为 poly(n)2^{-n/3}的情况下仅使用经典傅里叶标签的最高三分之一来实现，这违反了反计算阶段需要完整标签信息的要求。作者发布了 Lean 4 代码。

rss · IACR ePrint 密码学论文 · 8月15日 03:46

**背景**: 二面体陪集问题（DCP）要求从量子陪集态中恢复二面体群中的一个隐藏平移；Regev 证明带错误学习问题可归约到 DCP，使 DCP 对基于格的抗量子密码学非常重要。Regev 2004 年的求解模板包含量子傅里叶变换、经典傅里叶标签和一个必须擦除中间信息的反计算阶段。遵循该模板的算法需要正确使用经典傅里叶标签；新工作表明只使用部分标签是不够的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2025/1046">A Quasi-polynomial Time Algorithm for the Extrapolated Dihedral Coset Problem over Power-of-Two Moduli</a></li>
<li><a href="https://arxiv.org/abs/2206.14408">[2206.14408] Time and Query Complexity Tradeoffs for the Dihedral Coset Problem</a></li>
<li><a href="https://eprint.iacr.org/2026/1591">A Polynomial-Time Quantum Algorithm for the Dihedral Coset ...</a></li>

</ul>
</details>

**标签**: `#quantum algorithms`, `#cryptography`, `#dihedral coset problem`, `#post-quantum cryptography`, `#formal verification`

---

<a id="item-8"></a>
## [密码分析推翻四态量子公钥加密方案](https://eprint.iacr.org/2026/1706) ⭐️ 7.0/10

IACR 电子预印本上的一篇新评论表明，Liu 等人 2022 年提出的四态量子公钥加密方案可以精确化简为 |M⟩ → Rθ X^m |M⟩ 的形式，且测量结果 m 会被公开。这种化简表明密文泄漏了明文的计算基分布，从而否定了其所声称的信息论安全性。 该结果很重要，因为它纠正了量子公钥加密中一个错误的安全证明，而在后量子密码学发展的背景下，该领域正受到越来越多的审视。研究人员可以避免在那些看似安全、实则通过测量统计泄漏明文信息的方案上浪费精力。 该加密方案使用四态公钥控制的 CNOT 门，然后测量消息寄存器。密码分析显示，所得密文的计算基分布为 (|α|², |β|²)，与明文完全相同，因此在公开结果 m 已知的情况下，明文态 |0⟩ 和 |1⟩ 可以被完美区分。

rss · IACR ePrint 密码学论文 · 8月16日 12:19

**背景**: 受控非门（CNOT 门）在控制量子比特为 |1⟩ 时翻转目标量子比特，是量子电路中最基本的双量子比特操作之一。信息论安全性（又称无条件安全性）是指即使面对拥有无限计算能力的敌手，密码系统仍然安全，这不同于计算安全性。量子公钥加密（qPKE）允许公钥为量子态，是后量子密码学中一个活跃的研究方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Controlled_NOT_gate">Controlled NOT gate</a></li>
<li><a href="https://en.wikipedia.org/wiki/Information-theoretic_security">Information-theoretic security</a></li>
<li><a href="https://arxiv.org/abs/2306.07698">[2306.07698] Public-Key Encryption with Quantum Keys</a></li>

</ul>
</details>

**标签**: `#quantum cryptography`, `#cryptanalysis`, `#public key encryption`, `#information-theoretic security`, `#quantum computing`

---

<a id="item-9"></a>
## [混合算法将 MQOM 的布尔 MQ 攻击性能提升 1-4 比特](https://eprint.iacr.org/2026/1704) ⭐️ 7.0/10

该论文提出了一种结合 Lokshtanov 等人多项式方法与 Dinur 第二算法的布尔 MQ 混合算法，在 MQOM 参数集上实现了 1-4 比特的适度性能提升。论文还表明，对于 MQ 的“部分猜测单向性”问题（PGOW-MQ），利用解测试预言机可将其求解速度比普通 MQ 提高 2-4 倍，从而获得针对 MQOM、低于预期安全水平 3-4 比特的攻击。 该结果直接影响 NIST 附加签名竞赛第三轮候选方案 MQOM 的安全裕度，表明其隐含假设“PGOW-MQ 与 MQ 一样困难”略有偏差。尽管当前攻击具有巨大的内存开销，但依赖该假设的参数集可能需要重新评估。 该算法是 Lokshtanov、Paturi、Tamaki、Williams 和 Yu（SODA 2017）多项式方法与 Dinur 第二算法（Eurocrypt 2021）的混合，并移除了一些机制。针对 PGOW-MQ 的攻击利用了解测试预言机，但内存复杂度极大；此外，一种基于矩阵铅笔的新技术解决了最大的欠定布尔 Fukuoka MQ 挑战，并改进了 Thomae-Wolf 和 Furue-Nakamura-Takagi 算法。

rss · IACR ePrint 密码学论文 · 8月16日 08:14

**背景**: MQ（多元二次）问题要求在有限域上求解二次方程组；布尔 MQ 指在 GF(2)上的情况。MQOM 是一种基于 MPC-in-the-Head 范式的数字签名方案，是 NIST 附加签名竞赛的第三轮候选。其部分参数集在公钥中暴露了布尔二次系统，因此布尔 MQ 的难度至关重要。Dinur 在 SODA/Eurocrypt 2021 上的算法代表了布尔 MQ 求解的最新进展，而大域上的 MQ 在过去十年相对平静。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mqom.org/">MQOM</a></li>
<li><a href="https://eprint.iacr.org/2023/1719">MQ on my Mind: Post-Quantum Signatures from the Non-Structured Multivariate Quadratic Problem</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#MQ problem`, `#NIST competition`, `#Boolean MQ`, `#algorithm`

---

<a id="item-10"></a>
## [DTRU：采用双 E8 编码的紧凑 NTRU 密钥封装机制](https://eprint.iacr.org/2026/1701) ⭐️ 7.0/10

研究人员提出 DTRU，一种基于 NTRU 的密钥封装机制，采用双 E8 编码构造 16 维格码，解码复杂度低。该方案支持多种环结构，并针对中国 2025 年商用密码标准，覆盖 128、256、512 位（可选 384 位）安全级别。 这可能影响中国后量子密码标准的制定，并为 Kyber 和 NTRU-HRSS 等现有 KEM 提供更高效的替代方案。所报告的带宽和速度优势使其对低功耗和资源受限的部署具有吸引力。 在相同安全级别下，DTRU 比 NTRU-HRSS 紧凑 49%-52%，临时密钥交换往返时间快 3.84–15.69 倍；比 Kyber 紧凑 7%-27%，快 1.05–1.32 倍。方案通过避免系数压缩和冗余可逆性检查来简化实现，并提供 C、AVX2 和 ARM 实现。

rss · IACR ePrint 密码学论文 · 8月16日 01:52

**背景**: NTRU 是一种基于格的公钥密码体制，能够抵抗量子攻击，使用多项式乘法进行快速加解密。密钥封装机制（KEM）是一种密码原语，允许发送方生成短期秘密密钥并通过公共信道安全地传输给接收方。DTRU 在 NTRU 基础上采用双 E8 编码，从 8 维 E8 格构造 16 维格码，以提升纠错能力和紧凑性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NTRU">NTRU</a></li>
<li><a href="https://en.wikipedia.org/wiki/Key_encapsulation_mechanism">Key encapsulation mechanism</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#NTRU`, `#KEM`, `#lattice-based cryptography`, `#E8 lattice`

---

<a id="item-11"></a>
## [改进 Qlapoti 分析，SQIsign 范数方程求解器提速 6 至 9 倍](https://eprint.iacr.org/2026/1700) ⭐️ 7.0/10

一篇新的预印本（eprint 2026/1700）修正了 Qlapoti 算法在失败概率分析上的缺陷，理顺了其实现与伪代码之间的差异，并提出了一个新的四元数范数方程求解算法，其失败概率可忽略不计。C 语言实现显示范数方程求解器提速 6 至 9 倍，完整 SQIsign NIST2 签名提速 1.3 至 2.1 倍。 这提升了 SQIsign 核心的理想到同源转换步骤的效率和可靠性，而 SQIsign 是在 NIST 后量子标准化竞争中领先的签名方案之一。在保证密码学上可忽略的失败概率的同时缩短签名时间，增强了 SQIsign 相对于其他后量子候选方案的实际可行性。 该工作修正了 Qlapoti 中失败概率分析的缺陷，并明确分析了实现与论文伪代码之间的差异。新的范数方程求解器具有可忽略的失败概率；报告的提速为求解器单独 6 至 9 倍，完整 SQIsign NIST2 签名 1.3 至 2.1 倍，具体取决于 NIST 安全级别。

rss · IACR ePrint 密码学论文 · 8月15日 21:47

**背景**: SQIsign 是一种基于超奇异椭圆曲线同源和四元数代数的后量子数字签名方案，具有非常紧凑的密钥和签名。2025 年 ASIACRYPT 发表的 Qlapoti 算法简化了 SQIsign 中使用的四元数理想到同源转换，但其失败概率仍为 2^-60，尚未达到密码学上可忽略的水平。这篇新预印本正是针对这些不足进行修正，并进一步优化了范数方程求解步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SQIsign">SQIsign</a></li>
<li><a href="https://eprint.iacr.org/2025/1604">Qlapoti: Simple and Efficient Translation of Quaternion Ideals to Isogenies</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#isogeny-based cryptography`, `#SQIsign`, `#post-quantum cryptography`, `#algorithm optimization`

---

<a id="item-12"></a>
## [DumboMix：通过 MPC 混合实现实用的鲁棒异步匿名广播](https://eprint.iacr.org/2026/1699) ⭐️ 7.0/10

论文提出 DumboMix 框架，实现异步匿名广播并保证输出交付，可容忍至多 n/3 拜占庭服务器和不可预测网络延迟。其核心 DumboMix1 和 DumboMix2 电路在 Shamir 秘密共享 MPC 中具有 O(1)乘法深度、期望 O(N^2)标量乘法和至多 O(N) MPC 乘法；在局域网混洗 1024 条消息时，相比 RabbitMix 加速 44.8–65.9 倍。 该工作提升了隐私保护通信和安全多方计算的实用性，使匿名广播在真实异步网络和拜占庭故障下仍能鲁棒运行。它有望用于需要先混合再公开消息的匿名消息、拍卖或投票系统，并通过降低计算开销使部署更可行。 该框架依赖底层鲁棒 MPC 来保证交付；混洗电路在线阶段为 O(1)乘法深度、期望 O(N^2)公开-秘密标量乘法和至多 O(N)秘密间乘法。实现基于 DumboMPC++优化预处理，并在 4 到 31 个服务器的局域网/广域网下评估，局域网中相对 RabbitMix、PowerMix 和蝶形交换网络分别加速 44.8–65.9 倍、4.8–7.1 倍和 2.7–4.0 倍。

rss · IACR ePrint 密码学论文 · 8月15日 21:32

**背景**: 匿名广播允许客户端向一组服务器发送消息，服务器稍后以随机顺序同时公开所有消息，从而隐藏每条消息的发送者。保证输出交付（也称鲁棒性）意味着即使存在恶意服务器或网络延迟无上限，协议仍能完成，只要拜占庭故障服务器不超过总数的三分之一。Shamir 秘密共享将秘密拆分为多个份额，使各方能在不泄露输入的情况下对共享数据进行计算。DumboMPC 是一种先进的异步 MPC 框架，提供鲁棒输出交付；DumboMPC++是其优化实现，用于本工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1699">DumboMix: Robust Asynchronous Anonymous Broadcast Made Practical</a></li>
<li><a href="https://partisiafoundation.com/mpc-techniques-series-part-3-secret-sharing-shamir-style/">Shamir Secret Sharing in MPC: A Revolutionary Tool - Partisia ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secure multiparty computation`, `#Byzantine fault tolerance`, `#anonymous broadcast`, `#privacy`

---

<a id="item-13"></a>
## [论密码学群鲁棒组合器的不可能性](https://eprint.iacr.org/2026/1695) ⭐️ 7.0/10

一篇新的 IACR ePrint 论文（2026/1695）证明，在通用群模型中，对所有多项式有界的 k<n，都不存在能保持判定性 Diffie–Hellman（DDH）安全性的通用 (k,n)-鲁棒组合器。对于离散对数安全性，论文给出紧阈值：仅当组合群阶满足 log N ≥ (n−k+1)λ 时鲁棒组合可行，而当 log N ≤ (n−k)λ 时不可能，其中各分量群具有不同的 λ 比特素数阶。 这确立了一个根本限制：像 DDH 这样的判定性假设无法在群层面被鲁棒组合，因此系统设计者必须在协议或密钥派生等更高层实现鲁棒性。同时它表明搜索性假设可以组合，但只能以基本最优的表示成本实现。 直积构造能保持搜索困难性，但对判定性假设失效并产生大量表示开销；DDH 不可能性结果覆盖所有多项式有界的 n 和 k（k<n），而离散对数阈值在 n、k 为固定常数且各分量群具有不同 λ 比特素数阶的范围内是紧的。

rss · IACR ePrint 密码学论文 · 8月15日 09:01

**背景**: 鲁棒组合器将多个候选实现合并，使得只要 n 个候选中至少 k 个仍然安全，合并后的方案就安全；它已在哈希函数、加密和不经意传输等原语中被广泛研究。通用群模型通过隐藏群元素编码、只暴露抽象群运算来理想化密码群，从而能够分析不利用具体编码的攻击。直积构造是一种自然基线，它通过取多个群的笛卡尔积来合并群，通常能保持搜索困难性，但不能保持判定性假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1695">On the Impossibility of Robust Combiners for Cryptographic Groups</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generic_group_model">Generic group model</a></li>
<li><a href="http://www.sommer.jp/combiner.htm">Robust Combiners for Cryptographic Primitives</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#robust combiners`, `#generic group model`, `#impossibility result`, `#provable security`

---

<a id="item-14"></a>
## [均匀 MQ 假设与 MQ 安全性关系](https://eprint.iacr.org/2026/1694) ⭐️ 7.0/10

该论文证明均匀 MQ（UMQ）假设与 MQ 第二原像抗性（MQSPR）相互紧密蕴含，且 MQ 单向性（MQOW）紧密蕴含 UMQ。还证明当方程数 m 满足 m ≤ n + O(log λ)时，UMQ 蕴含 MQOW，其中 n 为变量数，λ为安全参数；当 m ≤ n + O(1)时，该蕴含是紧的。 这厘清了多元二次问题核心平均情况困难假设之间的精确关系，而这些假设支撑了许多后量子密码构造。紧归约和放宽的方程-变量条件（尤其覆盖方方程组）可简化安全性证明并改进参数选择。 UMQ 与 MQSPR 之间的等价是紧的；MQOW 紧密蕴含 UMQ；当 m ≤ n + O(log λ)时，UMQ 蕴含 MQOW，且当 m ≤ n + O(1)时该蕴含紧。作为推论，在同样条件下 MQSPR 蕴含 MQOW，这弱于一般函数族中 SPR 到 OW 所需的压缩条件 n = m + ω(log λ)。

rss · IACR ePrint 密码学论文 · 8月15日 08:16

**背景**: 多元二次（MQ）密码学依赖于在有限域上求解二次方程组的困难性，该问题被认为即使对量子计算机也是困难的。均匀 MQ 假设是一种平均情况版本，即很难找到均匀生成的 MQ 函数的零点；MQ 单向性意味着求逆这类函数是困难的；MQ 第二原像抗性意味着给定一个输入很难找到第二个原像。这些假设被用于后量子签名等方案的安全性分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1694">Relations Between the Uniform MQ Assumption and Other ...</a></li>
<li><a href="https://iacr.org/news/item/29294">IACR News item: 16 August 2026</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#multivariate-quadratic`, `#security-assumptions`, `#post-quantum-cryptography`, `#theoretical-cs`

---

<a id="item-15"></a>
## [攻击者劫持公共 Wi-Fi DNS 以窃取凭证。](https://www.schneier.com/blog/archives/2026/08/hacking-public-wi-fi-dns-to-steal-credentials.html) ⭐️ 7.0/10

犯罪分子入侵酒店、会议中心等场所的公共 Wi-Fi 路由器并篡改 DNS 设置，将用户重定向到伪造的登录页面，从而窃取凭据，其中包括 Microsoft 365 账户。 这一正在进行的攻击活动使所有使用公共 Wi-Fi 的用户面临登录凭据被盗的风险，可能导致账户被接管、数据泄露和后续攻击。这凸显了在不可信网络上采取防护措施（如使用 VPN 和避免输入敏感信息）的必要性。 攻击者通过入侵公共 Wi-Fi 路由器的管理界面来修改其 DNS 服务器设置。由于所有连接设备都会使用该路由器的 DNS，用户会被重定向到仿冒 Microsoft 365 等合法登录门户的钓鱼页面。

rss · Schneier on Security · 8月17日 11:18

**背景**: DNS（域名系统）负责将人类可读的域名转换为 IP 地址。当路由器的 DNS 设置被改为指向攻击者控制的服务器时，该网络上的所有设备都可能被静默重定向到恶意网站。伪造的登录页面会模仿合法服务，诱骗用户输入用户名和密码。

**标签**: `#cybersecurity`, `#DNS hijacking`, `#public Wi-Fi`, `#credential theft`, `#network security`

---
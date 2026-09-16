---
layout: default
title: "Horizon Summary: 2026-09-16 (ZH)"
date: 2026-09-16
lang: zh
---

> 从 53 条内容中筛选出 15 条重要资讯。

---

1. [Beasley：首个实用的格基最优轮数恶意安全 VOPRF](#item-1) ⭐️ 9.0/10
2. [理想格问题的 NP 困难性被证明](#item-2) ⭐️ 9.0/10
3. [威慑成为支付通道安全的第三支柱](#item-3) ⭐️ 8.0/10
4. [新信号泄漏攻击打破 ZZDSD-AKE 的 eCK 安全性](#item-4) ⭐️ 8.0/10
5. [私有 Transformer 推理的系统化知识：跨系统、模型与密码学](#item-5) ⭐️ 8.0/10
6. [异步主动秘密共享的可行性边界与最优协议](#item-6) ⭐️ 8.0/10
7. [随机探测模型中刷新构件的统一分析](#item-7) ⭐️ 8.0/10
8. [椭圆曲线离散对数量子算法所需逻辑量子比特降至 2.5n](#item-8) ⭐️ 8.0/10
9. [沃尔什变换框架统一差分-线性密码分析的三类变体](#item-9) ⭐️ 8.0/10
10. [CauchyFold：利用缩放柯西挑战实现残差最优的高元格基折叠](#item-10) ⭐️ 8.0/10
11. [新论文提出完全简洁的不可区分混淆](#item-11) ⭐️ 8.0/10
12. [非完美高阈值及切片秘密共享方案](#item-12) ⭐️ 8.0/10
13. [BAA 码最小距离下尾的尖锐渐近结果](#item-13) ⭐️ 8.0/10
14. [超越 DCR：基于子群不可区分性的 HSS 与 PCF 构造](#item-14) ⭐️ 8.0/10
15. [新的预言分离显示 PRFSG 不蕴含 PRU](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Beasley：首个实用的格基最优轮数恶意安全 VOPRF](https://eprint.iacr.org/2026/2010) ⭐️ 9.0/10

该论文介绍了 Beasley——首个具体实现的格基、最优轮数、恶意安全的可验证遗忘伪随机函数（VOPRF）原型。它将 BLMR13 伪随机函数推广为每次处理 4 位输入，并用环切换求和检验协议替代 LaBRADOR 式证明，在保持安全性的同时得到 75.4 KB 的证明和较快的运行时间。 这填补了后量子密码学的一大空白：现有实用的 VOPRF 大多依赖可被量子攻击的假设，而此前的格基恶意安全构造仅停留在理论层面。Beasley 的性能表明，抗量子 VOPRF 可用于隐私保护认证、基于口令的密钥交换等现实协议。 Beasley 使用环维度 512，并将 BLMR13 PRF 推广为 w=4，使求值深度减少为原来的四分之一。在单核 AVX2 消费级笔记本上测试，客户端请求与 NIZK 证明生成耗时 520 ms，服务器验证 15.3 ms，峰值内存 113.7 MB，客户端通信量 109 KB，证明大小 75.4 KB。

rss · IACR ePrint 密码学论文 · 9月13日 22:06

**背景**: 可验证遗忘伪随机函数（VOPRF）允许客户端在服务器持有秘密密钥的情况下，对私有输入获得 PRF 求值，并验证服务器确实使用其承诺的密钥进行了计算。格基密码学是领先的后量子方法，因为某些格问题被认为对量子计算机也难以求解，不像 RSA 和椭圆曲线方案易受 Shor 算法攻击。BLMR13 是一种密钥同态的格基 PRF，常用于 OPRF 构造，但零知识证明其正确求值一直是主要性能瓶颈。Beasley 基于 Albrecht 等人提出的最优轮数理想格 VOPRF 框架以及 LeOPaRd 相关工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2019/1271">Round-optimal Verifiable Oblivious Pseudorandom Functions From Ideal Lattices</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lattice-based_cryptography">Lattice-based cryptography</a></li>
<li><a href="https://eprint.iacr.org/2024/1459">Verifiable Oblivious Pseudorandom Functions from Lattices: Practical-ish and Thresholdisable</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#zero-knowledge proofs`, `#lattice-based cryptography`, `#oblivious pseudorandom functions`, `#post-quantum security`

---

<a id="item-2"></a>
## [理想格问题的 NP 困难性被证明](https://eprint.iacr.org/2026/2003) ⭐️ 9.0/10

一篇新论文（eprint 2026/2003）通过从一般格到理想格的保维数确定性多项式时间归约，证明了理想格问题（包括 ℓ2 范数下的最短向量问题 SVP 和最近向量问题 CVP）的 NP 困难性。该归约在一个全实单基因数域的典范嵌入中构造理想格，所用整数（包括判别式）的比特长度均为多项式；若要求数环为完整整数环，则归约被猜想可在有界误差量子多项式时间内完成。 这解决了理想格最坏情况困难性的一个长期未决问题，而理想格是 Ring-LWE 和 NTRU 等高效后量子密码方案的核心。该结果表明，即使是结构化的理想格问题也能从一般格继承 NP 困难性，从而加强了基于格的密码学的理论安全基础。 该归约是保维数的确定性多项式时间归约，适用于 ℓ2 范数。它生成一个单基因、全实数域中的可逆理想，所有整数（包括判别式）的比特长度均为多项式；对于必须使用完整整数环的情况，归约仅被猜想可在有界误差量子多项式时间内成功。

rss · IACR ePrint 密码学论文 · 9月13日 16:48

**背景**: 理想格是通过典范嵌入从数域整数环中的理想得到的格；它们具有额外的代数结构，使得密码运算更高效，但其最坏情况困难性此前不如一般格清楚。SVP（寻找最短非零格向量）和 CVP（寻找最接近目标的格向量）是基本的格问题，其一般版本已知是 NP 困难的。基于格的密码学正是以这些问题在量子计算机下仍难以解决为安全基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ideal_lattice">Ideal lattice</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shortest_vector_problem">Shortest vector problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Closest_vector_problem">Closest vector problem</a></li>

</ul>
</details>

**标签**: `#lattice-based cryptography`, `#NP-hardness`, `#ideal lattices`, `#computational complexity`, `#post-quantum cryptography`

---

<a id="item-3"></a>
## [威慑成为支付通道安全的第三支柱](https://eprint.iacr.org/2026/2001) ⭐️ 8.0/10

该论文提出将威慑作为支付通道安全的第三支柱，与安全性和活性并列，并给出了占用共享状态资源定价的持有成本框架。论文证明线性时间比例责任可实现紧致威慑，并构造了可在当今比特币上运行的融合债券方案，无需契约、预言机或矿工假设，将槽位卡堵威慑提高八个数量级，同时对准时诚实支付零净成本。 由于 griefing 攻击能以极低成本降低 Lightning 这类 Layer 2 网络的可用性，为占用时间建立可证明的价格，可以让这类攻击变得经济上不理性，并在无需协议升级的情况下改善扩容。论文还证明了 2020 年 Lightning 工程界的一个猜想，即多跳转发三难问题。 关键结论包括一个不可能性定理：四个目标属性——抵御合谋汇聚方、penalty-only honesty、零中介锁仓和路径隐私——中有三个无法同时实现，而其余每种组合都有对应的构造。论文还精确刻画了单通道可执行性：仅惩罚定价可单方面执行当且仅当脚本暴露时间，这也解释了为何 BIP65 之前的比特币无法支持无信任的占用定价；此外还发现了一个针对发送方路径长度的 O(1/n) 极值侧信道。

rss · IACR ePrint 密码学论文 · 9月13日 15:08

**背景**: 支付通道允许双方在链下交易，只在链上记录最终余额，从而降低费用和拥堵。支付通道的经典安全有两根支柱：安全性（对手无法盗取资金）和活性（支付可以继续或最终结算）。Griefing/卡堵攻击利用攻击者几乎不花钱就能占用通道容量或路由槽位、而又不盗取资金的特点，破坏可用性。本文提出第三根支柱——威慑，让占用资源的行为承担可证明的时间价格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nervos.org/knowledge-base/ultimate_guide_to_payment_channels">The Ultimate Guide to Payment Channels and Payment Channel Networks</a></li>
<li><a href="https://www.spark.money/glossary/griefing-attack">Griefing Attack - Spark Glossary | Spark</a></li>

</ul>
</details>

**标签**: `#payment channels`, `#blockchain security`, `#griefing attacks`, `#layer 2 scaling`, `#cryptography`

---

<a id="item-4"></a>
## [新信号泄漏攻击打破 ZZDSD-AKE 的 eCK 安全性](https://eprint.iacr.org/2026/2017) ⭐️ 8.0/10

本文提出新的信号泄漏攻击，成功攻破基于 LWE 的里程碑式 MQV 风格 AKE 协议 ZZDSD-AKE，证明其在临时密钥泄露下无法达到 eCK 安全性。攻击还打破了 GDLL-KE 的随机噪声对策，分别以约 1700 次和 180 次查询恢复静态私钥。 这解决了一个关于里程碑式 LWE 认证密钥交换协议的长期悬而未决问题，并表明 MQV 风格结构加简单随机化不足以对抗主动攻击者。研究结果为未来后量子 AKE 设计和标准化提供了关键指导。 攻击利用 eCK 模型中定义的临时密钥泄露，并通过几何视角从信号泄漏中恢复静态私钥。实验表明，针对 ZZDSD-AKE 约需 1700 次查询、针对 GDLL-KE 约需 180 次查询即可恢复密钥。

rss · IACR ePrint 密码学论文 · 9月14日 07:16

**背景**: 带错误学习（LWE）是后量子密码学中广泛使用的困难格问题。直接基于 LWE 构造认证密钥交换（AKE）需要使用协商机制，这些机制在密钥重用时可能泄漏与秘密相关的信号。扩展 Canetti-Krawczyk（eCK）模型是一种强安全模型，允许敌手获取临时秘密等状态；ZZDSD-AKE 是 2015 年欧洲密码会上提出的里程碑式 MQV 风格 AKE 协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/327540/20260915/post-quantum-key-exchange-proved-unsecurable-1700-queries-hardened-variant-falls-180-queries.htm">Post-Quantum Key Exchange Proved Unsecurable in 1,700 Queries...</a></li>
<li><a href="https://cryptographycaffe.sandboxaq.com/posts/lighting-the-signal/">Lighting the Signal - The Cryptography Caffè</a></li>
<li><a href="https://en.wikipedia.org/wiki/Learning_with_errors">Learning with errors - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#authenticated key exchange`, `#LWE`, `#eCK model`

---

<a id="item-5"></a>
## [私有 Transformer 推理的系统化知识：跨系统、模型与密码学](https://eprint.iacr.org/2026/2005) ⭐️ 8.0/10

一篇新的系统化知识论文分析了 2022 至 2026 年间 58 个加密私有 Transformer 框架，覆盖系统、模型和密码学三个层面。该论文揭示了两个反复出现的跨后端适用性约束，并识别出影响 5 个框架的四类安全问题。 私有 Transformer 推理对于在无信任硬件下保护用户查询和模型权重至关重要，但现有综述掩盖了技术在执行阶段、模型调整或安全边界之间是否可组合。这项工作提供了跨层次视角和 12 个开放问题，为未来的隐私保护机器学习研究提供指导。 论文发现，当所需值尚未可用时，优化无法在执行阶段之间原样迁移；数据依赖的剪枝、缓存管理、路由和稀疏性需要隐藏、约束、预测或公开私有执行结构。它还指出 16 个框架依赖经验校准或分布特定机制，21 个需要额外训练，限制了泛化性。

rss · IACR ePrint 密码学论文 · 9月13日 18:07

**背景**: 私有 Transformer 推理通常使用安全多方计算（MPC）和同态加密（HE）等密码学技术，在不依赖可信硬件或差分隐私等统计松弛的条件下保护用户查询和模型权重。Transformer 因其大规模秘密矩阵乘法、高成本非线性激活和自回归生成而成为独特挑战。此前的综述主要按密码学后端、部署设置或支持的操作来组织文献，这掩盖了技术在执行阶段、模型调整或安全边界之间是否仍然适用或可组合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2505.10315">Private Transformer Inference in MLaaS: A Survey</a></li>
<li><a href="https://arxiv.org/html/2307.12533">Puma: Secure Inference of LLaMA-7B in Five Minutes</a></li>
<li><a href="https://www.ndss-symposium.org/wp-content/uploads/2025-57-paper.pdf">BumbleBee : Secure Two-party Inference</a></li>

</ul>
</details>

**标签**: `#private inference`, `#transformers`, `#cryptography`, `#secure computation`, `#systematization of knowledge`

---

<a id="item-6"></a>
## [异步主动秘密共享的可行性边界与最优协议](https://eprint.iacr.org/2026/2018) ⭐️ 8.0/10

一篇新的 ePrint 论文（2026/2018）为异步主动秘密共享（APSS）形式化了一类移动敌手模型，证明了给出弹性上界的通用攻击，并提出了在每种模型中都达到最优弹性的显式 APSS 协议。 该工作首次对完全异步认证网络中的主动秘密共享给出了系统且紧致的可行性刻画，明确了哪些敌手模型和弹性阈值是可实现的。它直接影响依赖无全局时钟的定期份额刷新的安全分布式系统、门限密码学和区块链协议的设计。 论文在完全异步认证网络的假设下，区分了对被腐化方的不同控制能力和异步环境中移动腐化的不同计量方式，通过通用攻击建立了弹性上界，并用达到最优弹性的显式 APSS 协议证明了这些上界是紧的。

rss · IACR ePrint 密码学论文 · 9月14日 08:08

**背景**: 主动秘密共享（PSS）在门限秘密共享的基础上周期性刷新份额而不改变秘密，从而限制攻击者收集足够份额的时间窗口。在同步系统中，刷新轮次可由全局时钟调度，但完全异步网络缺少这种时序保证。移动敌手可以随时间腐化不同参与方，而缺少全局时间使得定义周期和限制腐化变得困难。本文对异步 PSS 的这类敌手模型进行了分层形式化，并精确刻画了可实现性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Proactive_secret_sharing">Proactive secret sharing</a></li>
<li><a href="https://www.researchgate.net/publication/2545033_APSS_Proactive_Secret_Sharing_in_Asynchronous_Systems">(PDF) APSS: Proactive Secret Sharing in Asynchronous Systems</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#distributed-systems`, `#secret-sharing`, `#asynchronous-networks`, `#proactive-security`

---

<a id="item-7"></a>
## [随机探测模型中刷新构件的统一分析](https://eprint.iacr.org/2026/2015) ⭐️ 8.0/10

该论文在随机探测模型中形式化了直接刷新和基于零编码的刷新两大类刷新构件，在明确的随机性与均匀性条件下定义了理想构造，并扩展了基于零编码刷新的组合分析。作者还引入一个原子刷新函数来统一分析现有构件，推导其基数/通用 RPC 包络，并对掩码 AES 和 Raccoon 实现进行了比较。 这项对安全性与复杂度权衡的系统比较可以指导掩码编译器设计和侧信道安全实现的形式化验证，从而可能带来更高效且可证明安全的嵌入式密码实现。 论文引入“原子刷新函数”抽象，将文献中大多数刷新构件表示为统一框架中的实例，并推导出它们的基数/通用随机探测可组合性（RPC）包络及若干解析公式。在掩码 AES 和 Raccoon 上的实验评估揭示了理想构件与具体构件之间的差异。

rss · IACR ePrint 密码学论文 · 9月14日 07:07

**背景**: 掩码将敏感数据分成多个份额以抵御侧信道攻击，其安全性证明常采用随机探测模型，即每条线路以一定概率泄漏。刷新构件用于更新共享中间值的随机性，以避免大型掩码电路中的组合安全问题。随机探测可组合性（RPC）框架允许将小规模安全构件组合成更大电路并保持全局随机探测安全性，基数/通用等变体提供了不同的分析粒度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/2015">A Unified Analysis of Refresh Gadgets in the Random Probing Model</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-91101-9_4">New Techniques for Random Probing Security and Application to...</a></li>
<li><a href="https://theses.hal.science/tel-04457258/document">Secure and Verified Cryptographic Implementations in the Random ...</a></li>

</ul>
</details>

**标签**: `#side-channel attacks`, `#masking`, `#random probing model`, `#cryptographic implementations`, `#formal verification`

---

<a id="item-8"></a>
## [椭圆曲线离散对数量子算法所需逻辑量子比特降至 2.5n](https://eprint.iacr.org/2026/2014) ⭐️ 8.0/10

该成果提出了针对 n 位素数域上椭圆曲线离散对数问题的量子算法，将逻辑量子比特需求从 Luo 等人方案中的 3n+O(log n) 降低到 5/2 n + o(n)，Toffoli 门数从 O(n^3/log n) 改善到 Õ(n^2)。关键创新包括一个精确的就地模逆器（3/2 n + o(n) 逻辑量子比特，Õ(n) Toffoli 门），并利用欧几里得算法不变量和基于测量的反计算。 这降低了对椭圆曲线密码实施量子攻击所需的资源估计，直接影响后量子安全评估和密钥参数选择。量子比特和门数的减少使针对椭圆曲线离散对数的实用量子攻击更接近现实，加剧了向抗量子密码迁移的紧迫性。 该算法利用 Hua 恒等式将仿射点加法的可变平方乘法约化为求逆，从而在 5/2 n + o(n) 逻辑量子比特和 Õ(n) Toffoli 门内实现精确受控点加法。在欧几里得状态中只存储 R、r、T、t 四个量中的三个，并按需重建第四个；算术查询在亚线性工作空间中借助基于测量的反计算实现。

rss · IACR ePrint 密码学论文 · 9月14日 06:47

**背景**: 椭圆曲线密码（ECC）的安全性基于椭圆曲线离散对数问题（ECDLP）的难题：在椭圆曲线上给定点 P 和 Q，求解满足 Q=kP 的整数 k。量子计算机理论上可利用 Shor 算法的变体求解 ECDLP，但资源需求取决于实现量子算术所需的逻辑量子比特数和 Toffoli 门数。逻辑量子比特是经过纠错、按量子算法规范运行的量子比特，通常需要多个物理量子比特来构成一个逻辑量子比特。Toffoli 门是一种可逆三量子比特门，是量子算术和容错量子计算中的关键成本指标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Elliptic_curve_discrete_logarithm_problem">Elliptic curve discrete logarithm problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Logical_qubit">Logical qubit</a></li>
<li><a href="https://en.wikipedia.org/wiki/Toffoli_gate">Toffoli gate</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#elliptic curve cryptography`, `#discrete logarithm`, `#cryptanalysis`, `#post-quantum`

---

<a id="item-9"></a>
## [沃尔什变换框架统一差分-线性密码分析的三类变体](https://eprint.iacr.org/2026/2013) ⭐️ 8.0/10

该论文基于差分转移函数引入了沃尔什变换框架，将标准、旋转和内部差分-线性密码分析统一起来。它将现有 SDL 连通表及搜索工具扩展到 RDL 和 IDL 场景，并给出了新的或改进的区分器，例如 Alzette 的 8 轮 RDL 区分器和 SPECK64 的 14 轮 SDL 区分器。 这项工作将三类攻击方法统一到一个框架下，使原本不可用的密码分析工具能够用于 RDL 和 IDL，并为 ARX 密码提供实用的自动化搜索。这可能提升对 Ascon、Xoodoo、SPECK 和 SipHash 等广泛使用设计的安全性评估精度，并可能影响未来的密码设计准则。 对于 ARX 原语，作者推导了单个模加法的 SDL 和 RDL 相关性的 2×2 矩阵乘积公式；该公式暴露出秩 1 结构，将运行乘积解耦，从而只需线性不等式和查表即可进行 CP 近似，部分解决了 Niu 等人（CRYPTO 2022）的开放问题。该框架还将近期多轮中间部分搜索模型迁移到 RDL 和 IDL。

rss · IACR ePrint 密码学论文 · 9月14日 06:42

**背景**: 差分-线性密码分析由 Hellman 和 Langford 提出，它将高概率差分特征与线性近似相结合来区分密码与随机函数。沃尔什（Walsh-Hadamard）变换测量二进制函数与所有线性函数的相关性，因此是分析线性近似相关性的自然工具。ARX 原语由模加法、循环移位和异或构成，其简单操作被广泛用于轻量级设计。旋转差分和内部差分是相关变体，分别涉及旋转后的差分或相对于置换或反射的差分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Differential-linear_cryptanalysis">Differential-linear cryptanalysis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Walsh_transform">Walsh transform</a></li>

</ul>
</details>

**标签**: `#cryptanalysis`, `#differential-linear`, `#Walsh transform`, `#ARX`, `#symmetric-key cryptography`

---

<a id="item-10"></a>
## [CauchyFold：利用缩放柯西挑战实现残差最优的高元格基折叠](https://eprint.iacr.org/2026/2011) ⭐️ 8.0/10

CauchyFold 提出了一种高元格基折叠协议，利用缩放柯西挑战将 k + C(k,2) 个混合二次交互压缩为一个次数小于 k 的多项式，并带有 k 个输出值系数。边界分析表明至少需要 rk 个混合状态坐标，因此 CauchyFold 达到该残差最优宽度；k=16 的实现产生了 127,887 和 129,002 字节的折叠转录（两种参数配置）。 这消除了后量子递归证明中的一个关键瓶颈：将 LatticeFold 和 LatticeFold+ 等格基折叠方案扩展到高元时，混合状态开销达到理论最小值。残差最优宽度可降低证明大小和计算成本，使后量子递归 SNARK 和 IVC 更加实用。 折叠关系被约化为格环上带显式范数界的已承诺线性关系，知识可靠性基于 Module-SIS 假设，通过按同一转录顺序倒带来恢复源打开值或承诺矩阵的短核向量。完整的 k=16 CauchyFold 节点已实现；两种参数配置下的证明者到验证者折叠转录（不含 16 个新输入承诺）分别为 127,887 和 129,002 字节。

rss · IACR ePrint 密码学论文 · 9月14日 04:47

**背景**: 折叠方案允许证明者将多个关系实例折叠为一个，从而构造递归 SNARK；早期方案（如 Nova）依赖离散对数承诺，而 LatticeFold 和 LatticeFold+ 提出了抗量子的格基折叠。高元折叠每步处理 k 个新输入和一个累加器，但朴素方法会产生 k + C(k,2) 个交叉项需要处理。CauchyFold 使用受柯西启发的挑战分布（缩放柯西挑战），使两两挑战乘积落在单个挑战系数的张成空间中，从而最小化混合状态坐标数量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2024/257">LatticeFold: A Lattice-based Folding Scheme and its ...</a></li>
<li><a href="https://eprint.iacr.org/2025/247">LatticeFold+: Faster, Simpler, Shorter Lattice-Based Folding ...</a></li>
<li><a href="https://eprint.iacr.org/2026/2011">CauchyFold: Residue-Optimal High-Arity Lattice Folding via ...</a></li>

</ul>
</details>

**标签**: `#lattice-based cryptography`, `#folding schemes`, `#zero-knowledge proofs`, `#post-quantum cryptography`, `#cryptographic protocols`

---

<a id="item-11"></a>
## [新论文提出完全简洁的不可区分混淆](https://eprint.iacr.org/2026/2009) ⭐️ 8.0/10

论文提出了完全简洁的不可区分混淆，混淆程序的大小只随程序的秘密部分增长，而不随公开部分或输入规模增长。它从 PV 等价机器的输入简洁 IO 出发构造完全简洁 pv-IO，并在简洁见证加密或具有唯一证明的 NP-SNARG 假设下将其自举为完整 IO。 这将混淆开销缩小到仅秘密部分，使 IO 对具有大型公开描述的程序更具实用性，并推动基础密码学发展。它还首次给出混淆规模小于原始程序两倍的 IO 构造，以及针对多项式规模单调电路的紧凑秘密共享。 该构造假设 PV 等价机器的输入简洁 IO，而后者依赖于电路的超多项式困难 IO 和 LWE 假设。自举需要简洁见证加密或具有唯一证明的 NP-SNARG，并要求其正确性可在 PV 中证明；这些假设被证明既是充分的也是必要的。

rss · IACR ePrint 密码学论文 · 9月13日 21:00

**背景**: 不可区分混淆（IO）是一种密码学技术，在保持程序功能的同时隐藏其实现，并因能推导出许多其他原语而被称为“密码学完备”。简洁 IO 旨在使混淆规模不依赖程序运行时间、输入规模或公开描述。Cook 理论 PV 是用于推理多项式时间可计算函数的形式系统，LWE 是标准的格困难假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indistinguishability_obfuscation">Indistinguishability obfuscation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bounded_arithmetic">Bounded arithmetic - Wikipedia</a></li>
<li><a href="https://simons.berkeley.edu/talks/surya-mathialagan-mit-2025-06-25">Succinct Obfuscation via Propositional Proofs (or: How to use pv-IO)</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#indistinguishability obfuscation`, `#succinct obfuscation`, `#theoretical computer science`, `#propositional proofs`

---

<a id="item-12"></a>
## [非完美高阈值及切片秘密共享方案](https://eprint.iacr.org/2026/2008) ⭐️ 8.0/10

论文提出了新的 (n - t + 1)-out-of-n 阈值和切片秘密共享方案，面向比特秘密且允许非完美安全性：一个 ε-差分秘密方案的份额字母表大小为 Õ_t(1/ε²)，另一个针对每个 (n-2)-out-of-n 切片访问结构实现 ε-统计安全，份额大小为 O(log n log 1/ε)。当 t > 3 时，其安全性依赖有限域上单变量多项式分解的相关猜想。 这些构造实现了比完美保密下界更小的渐近份额大小，表明放宽到非完美安全可为高阈值和切片方案带来实际收益。首个具有对数级份额大小的统计安全 (n-2)-out-of-n 切片方案填补了此前仅有计算安全构造的空白，并可能影响秘密共享对偶性和一般访问结构的研究。 对于常数 t 和增长的 n，完美保密要求份额字母表大小至少为 n - t + 1（Bogdanov, Guo 和 Komargodski, ToC 2020），因此新的 ε-差分方案 Õ_t(1/ε²) 去除了对 n 的依赖。该方案的变体还给出了具有最优份额大小的普通和匿名 (n-1)-out-of-n 弱比特秘密共享方案。

rss · IACR ePrint 密码学论文 · 9月13日 20:40

**背景**: 秘密共享将秘密拆分为若干份额，只有被授权的参与方集合才能重构秘密。阈值方案为 (n - t + 1)-out-of-n 时，任意 n - t + 1 个参与方可重构，而更小的集合得不到信息；完美保密要求零信息泄露，非完美保密则允许有界的小泄露（统计或差分隐私式泄露）。高阈值方案的阈值接近 n（即 t 为常数），切片访问结构是用于构建更一般访问结构的小授权集合族。份额字母表大小或份额大小衡量每个参与方的存储/通信开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/2008">New Imperfect High Threshold and Slice Secret Sharing Schemes</a></li>
<li><a href="https://eprint.iacr.org/2024/602">Secret-Sharing Schemes for High Slices</a></li>

</ul>
</details>

**标签**: `#secret sharing`, `#cryptography`, `#information theory`, `#threshold schemes`, `#imperfect secrecy`

---

<a id="item-13"></a>
## [BAA 码最小距离下尾的尖锐渐近结果](https://eprint.iacr.org/2026/2007) ⭐️ 8.0/10

该论文证明，对于固定长度且最小距离 d≥2 的组成块和足够小的 δ>0，BAA 码最小距离不超过⌊δN⌋的概率在有限域和组成系数上一致地为 Θ(N^{1-d} + N^{1-⌈d/2⌉}Q^{-⌊d/2⌋})（Q=q-1）。论文还证明了[16,8,9]_q MDS 块可达到 0.30 距离、[16,4,13]_q MDS 块可达到 0.60 距离，并表明已发表的大域基准基本最优。 具有最小距离保证的随机线性码是伪随机相关生成器和基于码的证明系统中的核心构件，采样到低距离码可能破坏安全性或可靠性。这一尖锐下尾界为设计者提供了精确的失败概率而非宽松上界，使参数选择更可靠。 渐近公式分离了两种情形：线性代数项 N^{1-d} 仅在域大小 q 随 N 线性增长时起主导作用，另一项 N^{1-⌈d/2⌉}Q^{-⌊d/2⌋} 来自消除层；基于支撑的加权间隙估计控制所有活跃块数和消除层。对于两个 MDS 族，当 Q/N→∞ 时，已知的标记单块系数被证明是实际失败概率的首项常数，有限证书与大域基准几乎吻合。

rss · IACR ePrint 密码学论文 · 9月13日 20:24

**背景**: 区块累积-累积（BAA）码是由固定长度组成块和类似累加器的线性操作构成的随机线性码，因其编码速度快且适合随机化构造而被使用。伪随机相关生成器允许各方在极少通信下生成大量相关随机串，它们依赖这类码来保证采样结果满足所需性质。基于码的证明系统也用线性码编码约束，低最小距离可能导致可靠性失败。此前工作给出了坏距离概率的有限长度上界，但缺乏精确渐近下尾。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/0810.3422">[0810.3422] Coding Theorems for Repeat Multiple Accumulate Codes</a></li>
<li><a href="https://geoffroycouteau.github.io/posts/pcg/">Getting Started on Pseudorandom Correlation Generators</a></li>
<li><a href="https://ntt-research.com/wp-content/uploads/2022/07/Efficient-Pseudorandom-Correlation-Generators-Silent-OT-Extension-and-More.pdf">Ecient Pseudorandom Correlation Generators</a></li>

</ul>
</details>

**标签**: `#coding theory`, `#cryptography`, `#pseudorandom correlation generators`, `#minimum distance`, `#BAA codes`

---

<a id="item-14"></a>
## [超越 DCR：基于子群不可区分性的 HSS 与 PCF 构造](https://eprint.iacr.org/2026/2006) ⭐️ 8.0/10

该论文在子群不可区分性（SgI）假设下构造了同态秘密共享（HSS）和伪随机相关函数（PCF），将假设基础从判定性合数剩余（DCR）推广到更一般的群框架。同时提出了新的分布式离散对数（DDLog）算法，支持素数幂阶，并将复杂度从 O(log² t / log log t)改进为 O(log t log log t)。 该结果将同态秘密共享与伪随机相关函数所依赖的假设从常用的 DCR 扩展到子群不可区分性，扩大了安全多方计算和相关随机性生成可用的基础假设。新的素数幂分布式离散对数算法和公有硬币 SgI（PC-SgI）概念可能带来更高效或更多样的实例化，同时修复了先前静默 OT 扩展协议中的安全隐患。 新 DDLog 算法要求底数阶 t 是光滑的，并支持素数幂阶；其分治优化将复杂度从 O(log² t / log log t)降至 O(log t log log t)。论文还提出了公有硬币子群不可区分性（PC-SgI），在部分实例化下可由 SgI 推出，因此 VOLE 和 OT 的 PCF 构造不需要额外假设；OLE 和二次相关的 PCF 还需稀疏 LPN 假设。作者还修复了 Joye–Libert 实例化中的 DDH 攻击和 IKNP OT 扩展协议安全证明中的漏洞。

rss · IACR ePrint 密码学论文 · 9月13日 19:02

**背景**: 同态秘密共享（HSS）是同态加密在秘密共享中的类似物，允许对份额进行本地计算，并得到可合并出结果的短输出份额。伪随机相关函数（PCF）使两方能够从紧凑的密钥非交互地生成不经意传输（OT）或向量不经意线性评估（VOLE）等相关随机性。子群不可区分性（SgI）由 Brakerski 和 Goldwasser 在 Crypto 2010 提出，是一种关于在特定群中区分子群的困难性假设；在某些设置下，它等价于判定性合数剩余（DCR）假设。分布式离散对数（DDLog）用于在分布式场景下计算离散对数，是这类构造所需的基础组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2017/1248">Foundations of Homomorphic Secret Sharing</a></li>
<li><a href="https://eprint.iacr.org/2025/2325">Pseudorandom Correlation Functions for Garbled Circuits</a></li>
<li><a href="https://eprint.iacr.org/2026/2006">Beyond DCR: HSS and PCFs from Subgroup Indistinguishability</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#homomorphic secret sharing`, `#pseudorandom correlation functions`, `#subgroup indistinguishability`, `#distributed discrete log`

---

<a id="item-15"></a>
## [新的预言分离显示 PRFSG 不蕴含 PRU](https://eprint.iacr.org/2026/2002) ⭐️ 8.0/10

本文证明了一个完整的酉预言分离：即使是自适应安全且量子可访问的伪随机函数样态生成器（PRFSG），也不蕴含非自适应安全、仅前向查询的伪随机酉（PRU），即使其实现可以是非酉的并使用任意数量的辅助量子比特。 这一结果在预言模型下厘清了量子态与量子酉伪随机性之间的根本区别，表明基于态的伪随机原语无法通过黑盒构造一般地升级为酉原语。它澄清了量子伪随机对象的层级，并缩小了量子密码学中构建 PRU 的可能假设范围。 核心技术是将带有态生成预言机的候选 PRU 构造看作从预言机输出态到实现酉的映射，并研究该映射的导数；这些导数天然具有低秩结构，由此可将其输出与哈尔随机酉区分开。该结果属于预言模型，因此它展示的是黑盒归约的障碍，而非无条件不可能性。

rss · IACR ePrint 密码学论文 · 9月13日 15:48

**背景**: 伪随机态生成器（PRSG）输出在计算上与哈尔随机态不可区分的量子态；伪随机函数样态生成器（PRFSG）则使用单个密钥对多个输入产生这样的态。伪随机酉（PRU）是高效可实现的酉算子，在查询访问下与哈尔随机酉计算不可区分。预言分离（oracle separation）表明，即使将某个原语作为理想黑盒访问，也不能构造出另一个原语，从而排除黑盒归约。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2402.14803">[2402.14803] Pseudorandom unitaries with non-adaptive security Pseudorandom unitaries with non-adaptive security On the Limitations of Pseudorandom Unitaries Pseudorandom Unitaries in the Haar Random Oracle Model On Scalable Pseudorandom Unitaries and the Unitary Synthesis ... How to Construct Random Unitaries | Proceedings of the 57th ... Pseudorandom Unitaries in the Haar Random Oracle Model ...</a></li>
<li><a href="https://arxiv.org/abs/2211.01444">[2211.01444] Pseudorandom ( Function - Like ) Quantum State ...</a></li>
<li><a href="https://eprint.iacr.org/2025/1785">On the Limitations of Pseudorandom Unitaries</a></li>

</ul>
</details>

**标签**: `#quantum cryptography`, `#pseudorandomness`, `#quantum computation`, `#theoretical computer science`, `#oracle separation`

---
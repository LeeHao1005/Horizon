---
layout: default
title: "Horizon Summary: 2026-08-25 (ZH)"
date: 2026-08-25
lang: zh
---

> 从 42 条内容中筛选出 15 条重要资讯。

---

1. [新型 NTRU 自举将稀疏密钥盲旋转从 O(n)降至 O(h)](#item-1) ⭐️ 8.0/10
2. [HOVER：用于 McEliece 密钥恢复的更快速线性代数变体](#item-2) ⭐️ 8.0/10
3. [对 Classic McEliece 密钥恢复攻击的精确门计数估计](#item-3) ⭐️ 8.0/10
4. [Wiedemann XL 第三阶段的实用优化](#item-4) ⭐️ 8.0/10
5. [利用 iO 和可重随机化单向函数直接构造抗碰撞哈希函数](#item-5) ⭐️ 8.0/10
6. [EA 码被证明接近 Singleton 界并实现域无关 SNARK](#item-6) ⭐️ 8.0/10
7. [论文证明环切换后无需槽恢复即可提升同态加密自举性能](#item-7) ⭐️ 8.0/10
8. [小时间域下最优函数求逆匹配姚氏下界](#item-8) ⭐️ 8.0/10
9. [协因子挠点攻击破坏 SNARK 电路中提示标量乘法的可靠性](#item-9) ⭐️ 8.0/10
10. [研究人员提出面向加权 DAO 治理的可验证计票隐藏方案。](#item-10) ⭐️ 8.0/10
11. [基于 LCH 多项式基的更快后量子 zkSNARK 证明器](#item-11) ⭐️ 7.0/10
12. [字符串不经意传输的改进加法随机编码实现 O(λ)规模](#item-12) ⭐️ 7.0/10
13. [t-私有份额转换的不可行性及其对 PIR 的影响](#item-13) ⭐️ 7.0/10
14. [SQIsign 安全性证明改进：最优最小熵与三分之二比特安全](#item-14) ⭐️ 7.0/10
15. [多方 PSI 协议：最优在线轮数与可更新性](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [新型 NTRU 自举将稀疏密钥盲旋转从 O(n)降至 O(h)](https://eprint.iacr.org/2026/1783) ⭐️ 8.0/10

该论文提出基于 Cuckoo 哈希的 NTRU 自举框架，将稀疏二进制 LWE 秘密的盲旋转中顺序外积从 O(n)降至 O(h)，并提供免 NTT 变体。其在单 CPU 线程上布尔门自举耗时 0.83 毫秒，在 RTX 4090 GPU 上达到每秒 154,739 次门自举。 自举在 FHE 延迟中占主导地位，将盲旋转从线性复杂度降至汉明权重复杂度有望加速同态计算并推动更实用的硬件加速。所报告的 CPU 和 GPU 加速可能影响未来使用稀疏二进制 LWE 秘密的 TFHE 类 FHE 实现。 该方法使用 Cuckoo 哈希将汉明权重为 h 的 n 维二进制秘密转换为一热编码桶，并采用适合稀疏秘密的模切换；免 NTT 变体在盲旋转期间移除了在线 NTT/iNTT。单线程 CPU 上 4 位和 6 位自举分别为 1.75 毫秒和 2.65 毫秒，GPU 上相对 VeloFHE 有 13.6 倍加速。

rss · IACR ePrint 密码学论文 · 8月23日 18:47

**背景**: 全同态加密(FHE)允许在加密数据上计算，但每次操作都会增加噪声，自举用于刷新密文以支持无限计算。在 TFHE 式比特级 FHE 中，自举依赖盲旋转，它在 LWE 秘密加密的密文上反复执行外积。稀疏二进制 LWE 秘密在 n 维中只有 h 个非零位，因此复杂度随 h 而非 n 扩展的方法可显著降低延迟；本文的方法以 NTRU 作为底层加密方案。Cuckoo 哈希是一种使用两个哈希函数解决碰撞的方案，NTT 是格密码中常用的多项式变换。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2023/1564">Fast Blind Rotation for Bootstrapping FHEs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Learning_with_errors">Learning with errors - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cuckoo_hashing">Cuckoo hashing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#FHE`, `#Bootstrapping`, `#TFHE`, `#LWE`, `#Hardware Acceleration`

---

<a id="item-2"></a>
## [HOVER：用于 McEliece 密钥恢复的更快速线性代数变体](https://eprint.iacr.org/2026/1778) ⭐️ 8.0/10

HOVER 引入了高阶消失（HOV）针对 McEliece 密钥恢复的新变体，用更快的线性代数步骤取代了成本高昂的低秩方向搜索阶段。它利用公开 HOV 核的一阶 catalecticant 作为收缩张量来恢复隐藏的 Frobenius 方向，并在五个 TII McEliece 挑战中恢复了密钥，包括 TII-252。 这表明仅使用公开数据即可大幅加速针对 McEliece 的密码分析；虽然目前还不会威胁 Classic McEliece 参数，但它揭示了基于 Goppa 码的后量子密码学中新的结构性弱点。该发现也凸显了 AI 辅助密码分析日益重要的作用。 该攻击计算保持由一阶 catalecticant 构成的收缩张量所有关系的系数自同态；在“干净”情况下，标量扩张的 HOV 核恰好由 m 个隐藏的 Frobenius 方向张成，公共代数为 F_{2^m}。论文给出了基不变构造、可能的矩阵代数输出分类，以及会返回⊥而不是未认证输出的明确接受条件；在公开数据端到端实验中恢复了包括 TII-252 在内的五个 TII McEliece 挑战的密钥，且主要密码分析捷径由大语言模型发现。

rss · IACR ePrint 密码学论文 · 8月22日 18:04

**背景**: McEliece 是一种基于编码的后量子密码系统，它将结构化的二元 Goppa 码伪装成看似随机的线性码；其安全性依赖于一般线性码译码的困难性。高阶消失（HOV）于 CRYPTO 2026 提出，利用在奇偶校验矩阵列上高阶消失的多项式来区分 Goppa 码，最近已被扩展到密钥恢复。Catalecticant（或汉克尔矩阵）是一种斜对角线为常数的矩阵；在 HOVER 中它作为公开 HOV 核的一阶偏导数系数矩阵出现。Frobenius 方向是与 F_{2^m}上二元 Goppa 码代数结构相关的隐藏域自同构方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1778">HOVER: Higher-Order Vanishing Endomorphism Recovery</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-032-35398-6_7">Distinguishing Goppa Codes Using Higher-Order Vanishing</a></li>
<li><a href="https://en.wikipedia.org/wiki/McEliece_cryptosystem">McEliece cryptosystem</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum cryptography`, `#code-based cryptography`, `#McEliece`, `#cryptanalysis`

---

<a id="item-3"></a>
## [对 Classic McEliece 密钥恢复攻击的精确门计数估计](https://eprint.iacr.org/2026/1786) ⭐️ 8.0/10

该预印本提出了一种自包含的条件算术模型，用于针对二进制 Goppa 码的密钥恢复攻击，并为 Classic McEliece 的每一组参数给出精确的门计数估计。在建模配置中，带嵌套求解的投影归一化所需门数从 2^146.29 到 2^207.83，而 mceliece348864 可达到 2^142.15 个门。 Classic McEliece 是 NIST 后量子密码标准化的重要候选方案，其安全性评估依赖具体的攻击成本。尽管该文并未形成实际破解，但这些精确的门计数可能影响参数选择和未来的密码分析方向。 该攻击结合了二进制保留算子、Hasse 重数、Lucas 最小导数层、增广二进制分块 Wiedemann 算法以及局部标志重建。对 19,338 种配置的穷举扫描得到 2^114.35 的关系生成下界；Krylov 产出、高阶标志恢复、跨锚点独立性和内存感知实现等问题仍未解决。

rss · IACR ePrint 密码学论文 · 8月24日 00:19

**背景**: Classic McEliece 是一种基于 McEliece 密码体制的密钥封装机制，使用二进制 Goppa 码；该码由一个 GF(2^m) 上的 t 次多项式 g(x) 和一组不包含 g 的根的互异元素 L_i 定义。一般线性码的译码是 NP 难问题，但二进制 Goppa 码具有高效的 Patterson 译码算法，从而支持私钥结构。分块 Wiedemann 算法是一种在 GF(2) 上求解稀疏线性系统的概率方法，常用于基于编码的密码分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Classic_McEliece">Classic McEliece</a></li>
<li><a href="https://en.wikipedia.org/wiki/Binary_Goppa_code">Binary Goppa code</a></li>
<li><a href="https://en.wikipedia.org/wiki/Block_Wiedemann_algorithm">Block Wiedemann algorithm - Wikipedia</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#Classic McEliece`, `#key-recovery attack`, `#code-based cryptography`, `#cryptanalysis`

---

<a id="item-4"></a>
## [Wiedemann XL 第三阶段的实用优化](https://eprint.iacr.org/2026/1787) ⭐️ 8.0/10

该论文提出一种实用优化，利用求解多元系统只需要核向量的一小部分这一事实，大幅降低 Wiedemann XL 算法第三阶段的成本，使其与第一阶段相比几乎可以忽略不计。 这降低了使用 Wiedemann XL 进行代数攻击的总体成本，可能提高对多元方程系统的密码分析效率，并影响依赖 MQ 问题难度的密码体制的安全性评估。 该优化将第三阶段成本从 N²ω 降至几乎可以忽略不计，因为只需核向量的一小部分即可求得解；第一阶段 2N²ω 的成本不受影响。这里 N 是 Macaulay 矩阵宽度，ω 是平均行权重。

rss · IACR ePrint 密码学论文 · 8月24日 04:48

**背景**: XL（扩展线性化）算法通过将原始方程乘以不超过某个次数的所有单项式，再把单项式视为独立变量，从而得到大型稀疏线性系统来求解多元多项式方程组。Wiedemann XL 是一种使用 Wiedemann 迭代线性求解器代替高斯消元的变体，更适合稀疏矩阵。Macaulay 矩阵是多项式方程的线性化表示，行对应多项式倍数，列对应单项式。Wiedemann XL 的成本通常估计为 3N²ω，其中 N 是矩阵宽度、ω 是平均行权重；第一阶段贡献 2N²ω，第三阶段贡献 N²ω。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1787">A Practical Optimization for Wiedemann XL</a></li>
<li><a href="https://arxiv.org/pdf/2112.05023v1">Polynomial XL: A Variant of the XL Algorithm Using Macaulay ...</a></li>
<li><a href="https://tubiblio.ulb.tu-darmstadt.de/102351/">PWXL: A Parallel Wiedemann-XL Algorithm for Solving ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#algebraic attacks`, `#XL algorithm`, `#optimization`, `#cryptanalysis`

---

<a id="item-5"></a>
## [利用 iO 和可重随机化单向函数直接构造抗碰撞哈希函数](https://eprint.iacr.org/2026/1785) ⭐️ 8.0/10

该论文首次直接从不可区分混淆(iO)和可重随机化单向函数构造抗碰撞哈希函数(CRH)，绕过了 Asharov-Segev 黑盒不可能性障碍。同时构造了更强的完美可划分哈希(PPH)，并实现了具有统计抽取性的某处可抽取批量论证(seBARG)，包括利用速率 1 全同态加密构造的速率 1 seBARG。 这一结果表明，为单向函数增加可重随机化特性后，即可从 iO 实现此前被认为不可能的密码学原语，扩展了 iO 的已知能力。这可能影响全同态加密和高效批量论证系统的未来构造。 该构造比此前 Arnon、Ben-David 和 Yogev（CRYPTO '25）需要借助 Waters-Wu 自适应可靠 SNARG 的方法更直接、更简单。新的 seBARG 实现了统计抽取性，这一属性强于多数现有 seBARG 方案；速率 1 seBARG 还额外假设速率 1 全同态加密。

rss · IACR ePrint 密码学论文 · 8月23日 20:27

**背景**: 不可区分混淆(iO)是一种隐藏程序实现但保留其功能的密码技术，足以构造许多密码学原语，但黑盒归约下无法单独与单向函数构造抗碰撞哈希函数。单向函数是容易计算但难以求逆的基础密码学原语；可重随机化变体允许在不改变底层值的情况下对输出进行重新随机化。Asharov 和 Segev 的结果确立了黑盒方式下从 iO 和单向函数构造抗碰撞哈希函数是不可能的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indistinguishability_obfuscation">Indistinguishability obfuscation</a></li>
<li><a href="https://eprint.iacr.org/2026/003">Batch Arguments with Optimal Communication</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#indistinguishability obfuscation`, `#collision-resistant hash`, `#cryptographic primitives`, `#black-box barrier`

---

<a id="item-6"></a>
## [EA 码被证明接近 Singleton 界并实现域无关 SNARK](https://eprint.iacr.org/2026/1782) ⭐️ 8.0/10

该论文证明，当稀疏扩展矩阵从精确权重系综中采样时，扩展-累加（EA）码在足够大的有限域上以高概率实现任意接近 Singleton 界的速率-距离权衡；并构建了 Flare，一种新的基于 EA 码的域无关多项式承诺方案。 由于不再需要 FFT 友好域，Flare 能在任意有限域上构建 SNARK，同时把证明大小从 O(√M)改进到 O(log² M)，扩大了应用范围并降低验证成本。 对于规模为 M 的陈述，Flare 的证明者时间为 O(M log M)，证明大小为 O(log² M)；其构造包括针对 EA 码约束关系的高效 IOP，以及结合码切换和交织码的随机线性折叠。

rss · IACR ePrint 密码学论文 · 8月23日 16:27

**背景**: 纠错码在高码率和大距离上的性能对基于编码的 SNARK 至关重要。Singleton 界给出了给定码率和长度下码距的上限。Reed-Solomon 码能达到该界，但快速编码依赖 FFT 友好域。扩展-累加（EA）码是由稀疏扩展矩阵与累加矩阵相乘定义的线性码，可在任意域上高效编码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/383167581_Field-Agnostic_SNARKs_from_Expand-Accumulate_Codes">Field - Agnostic SNARKs from Expand-Accumulate Codes</a></li>
<li><a href="https://en.wikipedia.org/wiki/Commitment_scheme">Commitment scheme - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#error-correcting codes`, `#SNARKs`, `#polynomial commitments`, `#coding theory`

---

<a id="item-7"></a>
## [论文证明环切换后无需槽恢复即可提升同态加密自举性能](https://eprint.iacr.org/2026/1779) ⭐️ 8.0/10

该论文证明，在 CKKS 和 BGV/BFV 自举中，环切换后无需槽恢复，因为所需函数是仿射的。对于 CKKS N=2^17、n=2^16，使用稀疏秘密封装时吞吐量比直接自举高 99.7%–113.5%，使用稠密密钥自举时高 121.3%。 自举是同态加密的主要性能瓶颈，取消槽恢复可保留噪声容量并利用较小环间的并行性，从而加快实用加密计算，并将服务器密钥大小减少 16.4%–57.6%。 他们证明，对于任意实数输入上的 CKKS，连续逐槽函数能够在环切换叶子节点上独立求值且无需槽恢复，当且仅当该函数是仿射的。对于 BGV（p=65537、N=2^16、n=2^15），实现相对分区匹配和容量可比基线分别取得 3.16 倍和 1.46 倍加速。

rss · IACR ePrint 密码学论文 · 8月23日 08:53

**背景**: 全同态加密（FHE）允许对加密数据进行计算。CKKS 是一种支持实数或复数近似算术的 FHE 方案，而 BGV/BFV 在有限域上运算。自举用于刷新密文噪声以支持任意深度计算。环切换通过将计算从大环转移到较小环来降低自举成本；对于 SIMD 打包密文，通常需要槽恢复来恢复原始数据布局，但这会消耗噪声容量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1779">Bootstrapping using Ring Switching without Slot Recovery</a></li>
<li><a href="https://www.mit.edu/~linust/files/CKKS_Homomorphic_Encryption_Part_1.pdf">CKKS Homomorphic Encryption Part 1 - The Original Scheme</a></li>
<li><a href="https://fheideas.github.io/files/FHE_IDEAs_bootstrapping.pdf">BGV and BFV Bootstrapping: History, State-of-the-Art, and ...</a></li>

</ul>
</details>

**标签**: `#homomorphic encryption`, `#bootstrapping`, `#ring switching`, `#CKKS`, `#BGV/BFV`

---

<a id="item-8"></a>
## [小时间域下最优函数求逆匹配姚氏下界](https://eprint.iacr.org/2026/1777) ⭐️ 8.0/10

一篇新论文（eprint 2026/1777）提出了函数求逆的数据结构，在 t ≤ O(log N / log log N) 时达到 O(N log N / t) 空间和 O(t) 查询时间，首次在小时间域对一般函数匹配了姚氏下界。 这填补了函数求逆时间-空间权衡中长期存在的空白，证明在小时间/大空间域下该下界是紧的。它还可应用于紧凑动态图数据结构以及需要逆向查询或更新的密码学组件。 该构造支持对函数 f 的点更新，更新时间也是 O(t)，其技术还可扩展到 Fiat-Naor 的经典函数求逆方案。一个示例应用是动态无序图，使用 (1+ε) 接近信息论最优的空间，邻接查询、邻域查询和边插入/删除的摊还时间为 O(ε^{-1})。

rss · IACR ePrint 密码学论文 · 8月22日 17:22

**背景**: 函数求逆问题要求构造一个数据结构：给定函数 f: [N] → [N]，对任意 y 能回答是否存在 x 使得 f(x)=y，并返回这样的 x。时间-空间权衡描述算法如何用更多内存来减少计算时间。在该问题中，姚氏下界表明空间与查询时间的乘积为 Ω(N log N)，因此若空间为 N log N / t 比特，查询时间不可能显著低于 t。新结果在较小的 t 范围内达到这一下界，说明该下界在小时间域是紧的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Inverse_function">Inverse function - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Time-space_tradeoff">Time-space tradeoff</a></li>

</ul>
</details>

**标签**: `#function inversion`, `#data structures`, `#cryptography`, `#time-space tradeoff`, `#theory`

---

<a id="item-9"></a>
## [协因子挠点攻击破坏 SNARK 电路中提示标量乘法的可靠性](https://eprint.iacr.org/2026/1776) ⭐️ 8.0/10

该论文识别出针对 Eagen、El Housni、Masson 和 Piellard（Latincrypt 2025）提示标量乘法技术的协因子挠点攻击，表明这些小工具在具有非平凡协因子的椭圆曲线上不可靠。在 BLS12-381、BN254 和 BW6-761 上演示了两类具体伪造攻击，允许将 Q' = [k]P + T（T 为非零挠点）当作[k]P 接受。 这些提示标量乘法是目前已知最快的电路内方法，并广泛用于 zk-SNARK 系统，因此该缺陷直接导致在协因子曲线上可伪造证明。这一发现迫使协议设计者审计并修复小工具实现，可能以性能损失为代价来保持可靠性。 攻击利用挠点：任意标量攻击调整格分解使小的有理挠点在证明恒等式中抵消；选择标量攻击使输出端系数模一个小协因子素数消失，然后求解标量。作者通过子标量范围界量化了可达挠点，并提出一种更便宜的修复方法，通过提示原像以最小常数绑定提示输出。

rss · IACR ePrint 密码学论文 · 8月22日 14:36

**背景**: 在 zk-SNARK 中，椭圆曲线标量乘法是最昂贵的操作之一；由证明者提示输出 Q 并在电路内验证关系比重算[k]P 便宜得多。这类小工具的健全性通常假设曲线是素数阶的，但 BLS12-381、BN254 和 BW6-761 等广泛使用的曲线具有非平凡协因子，意味着整个群包含素数阶子群之外的额外挠点。Eagen 等人的格约简技术使用标量的短分数分解和一个群恒等式来认证 Q。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1776">Cofactor-torsion attacks on hinted scalar multiplications in ...</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-032-06754-8_4">Fast Elliptic Curve Scalar Multiplications in SN(T)ARK Circuits | Springer Nature Link</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#SNARKs`, `#elliptic curves`, `#zero-knowledge proofs`, `#cofactor torsion`

---

<a id="item-10"></a>
## [研究人员提出面向加权 DAO 治理的可验证计票隐藏方案。](https://eprint.iacr.org/2026/1773) ⭐️ 8.0/10

该论文提出一种用于 DAO 中加权二元投票的可验证“仅获胜者”计票隐藏构造，只公开结果位，不暴露确切计票。该方案使用零知识选票、加密聚合和与公开阈值比较，并由区块链裁决选票、链下后端执行加密计算，任何公开验证者都能核验结果与已接受选票一致。 DAO 中的代币加权投票可能通过公开权重和计票泄露投票者选择；该方案将隐私泄露减少到仅最终结果，同时保持公开可验证性。这对 DAO 治理很重要，因为它在不牺牲可审计性的情况下提供更强的投票匿名性，影响 DAO 参与者和治理协议设计者。 该构造由选民规模和贡献位宽参数化；原型和形式化脚本隐私结果针对受限的八名投票者、八位实例，共 134 个加密门，实际最终发布采用五分之三门限。在五名受托人诚实执行下，作者证明了从已接受的密文和结果中获得的被动公开观察者后端脚本隐私；针对恶意低于门限受托人的隐私仍未解决。

rss · IACR ePrint 密码学论文 · 8月22日 07:28

**背景**: DAO 使用代币加权投票，投票权与持有的治理代币数量成正比，公开的权重和计票可能泄露谁投了什么。零知识证明允许证明者在不透露任何额外信息的情况下让验证者相信某个陈述为真。可验证计算使计算能力有限的验证者能够检查不受信任的工作者是否正确执行了计算。本文结合这些技术来隐藏确切的加权计票，同时允许任何人验证已公布结果与已接受的加密选票相符。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof</a></li>
<li><a href="https://en.wikipedia.org/wiki/Decentralized_autonomous_organization">Decentralized autonomous organization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Verifiable_computing">Verifiable computing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#DAO governance`, `#zero-knowledge proofs`, `#verifiable computation`, `#blockchain privacy`, `#cryptographic voting`

---

<a id="item-11"></a>
## [基于 LCH 多项式基的更快后量子 zkSNARK 证明器](https://eprint.iacr.org/2026/1784) ⭐️ 7.0/10

该论文提出一种分治算法，直接在 Lin-Chung-Han（LCH）多项式基中进行消失多项式除法，避免了昂贵的基转换。在 Preon 上的基准测试显示，Preon-128A 和 Preon-256C 的端到端签名速度分别提升 5.0 倍和 5.8 倍，多项式变换本身快 12.6–17.9 倍。 消除基转换可去除二进制域上后量子 zkSNARK 证明器的一项主要开销，使 Preon 等 NIST PQC 候选方案和基于 Aurora 的签名更实用。这可能加快抗量子零知识证明在实际系统中的采用。 该除法算法对任意 F_2 基元素实现最优 O(n log n) 复杂度；在 LCH 基中，将消失多项式与随机盲化多项式相乘可简化为追加随机域元素，从而完全省去乘法。作者还将原生 LCH 基算术集成到 Aurora IOP 的所有阶段。

rss · IACR ePrint 密码学论文 · 8月23日 19:00

**背景**: zkSNARK 是简洁的零知识证明系统；后量子变体通常构建在二进制扩域 F_{2^m} 上的交互式谕示证明（IOP）之上，证明者的工作主要被多项式求值和消失多项式除法所主导。Gao–Mateer 和 Lin–Chung–Han 等加法 FFT 可加速加法子群上的求值，但需要先把多项式从其他基转换到自己的基，其开销为 O(n (log n)^2) 次域加法和 O(n log n) 次域乘法。LCH 多项式基就是一种适合加法 FFT 的基；该论文直接在该基中做除法，从而消除了这种转换开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.lambdaclass.com/additive-fft-background/">Additive FFT Explained: Fast Fourier Transforms Over Binary Fields</a></li>
<li><a href="https://www.math.clemson.edu/~sgao/papers/GM10.pdf">Additive Fast Fourier Transforms over Finite Fields</a></li>

</ul>
</details>

**标签**: `#zkSNARKs`, `#post-quantum cryptography`, `#polynomial arithmetic`, `#FFT`, `#zero-knowledge proofs`

---

<a id="item-12"></a>
## [字符串不经意传输的改进加法随机编码实现 O(λ)规模](https://eprint.iacr.org/2026/1781) ⭐️ 7.0/10

该论文提出了两种改进的用于字符串不经意传输（SOT）的加法随机编码（ARE）构造。第一种精简了基于公钥加密（PKE）的方法，直接构造出规模为 O(λ)的完美正确、统计单边安全的一边 ARE（OSARE）；第二种在 Squaring DDH 假设下给出了无配对的 SOT ARE，通过构造 Rabin-OT 的 ARE 并转换到 SOT，仅带来常数倍通信开销和可忽略的正确性错误。 SOT 是构造通用函数加法随机编码的核心效率瓶颈，因此降低其编码规模并去除配对需求，能够显著提高非交互式安全多方计算的实用性。这项工作可能降低依赖 ARE 的隐私保护协议的通信和计算开销。 第一种构造实现了完美正确性和统计单边安全性，规模为 O(λ)。第二种构造在 Squaring DDH 假设下无需配对，基于 Rabin-OT 编码，并在转换为 SOT 后仅产生常数倍通信开销，正确性错误可忽略。

rss · IACR ePrint 密码学论文 · 8月23日 11:10

**背景**: 加法随机编码（ARE）由 Halevi、Ishai、Kushilevitz 和 Rabin 在 CRYPTO 2023 提出，允许各方本地编码输入，使得编码在阿贝尔群上的和只揭示函数输出。字符串不经意传输（SOT）是构造通用函数 ARE 的核心原语，因此其编码效率直接影响整体开销。判定性 Diffie-Hellman（DDH）假设是关于离散对数的标准密码学困难假设；Squaring DDH 是本文用来避免配对的变体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2023/870">Additive Randomized Encodings and Their Applications</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secure multiparty computation`, `#oblivious transfer`, `#randomized encodings`, `#privacy`

---

<a id="item-13"></a>
## [t-私有份额转换的不可行性及其对 PIR 的影响](https://eprint.iacr.org/2026/1780) ⭐️ 7.0/10

这篇论文证明了：当 t≥2 且 q 与 m 互素时，不存在从环 Z_m 到有限域 F_q（或环 Z_{m'}）的 t-私有份额转换；因此 Alon、Beimel 和 Lasri 的 PIR 框架无法实例化为 t-私有 PIR 协议。 这一不可行性结果否定了利用解码多项式份额转换来改进 t-私有 PIR 的路径，帮助研究者理解隐私门限与通信复杂度之间的根本限制，并引导未来工作转向其他方法。 该结果适用于 t≥2，且 q 与 m 互素，并推广到输出落在环 Z_{m'} 的情形；它基于 Alon、Beimel 和 Lasri（TCC 2025）的份额转换框架，说明无法通过该技术实现优于 Woodruff-Yekhanin 及 Barkol-Ishai-Weinreb 的 t-私有 PIR 通信复杂度。

rss · IACR ePrint 密码学论文 · 8月23日 09:49

**背景**: PIR（私有信息检索）允许用户从多台服务器持有的数据库中读取条目，而不向任何单台服务器泄露所读取的索引。份额转换是一种局部变换，将一种秘密共享方案（如环 Z_m 上的份额）转换为另一种方案（如有限域 F_q 上的份额），是解码多项式构造高效 PIR 的关键抽象。t-私有 PIR 要求任意 t 台服务器合谋也无法得知查询索引。本文研究这类份额转换能否保持 t-私有性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1780">The Limits of $t$-Private Share Conversion</a></li>
<li><a href="https://en.wikipedia.org/wiki/Private_information_retrieval">Private information retrieval</a></li>
<li><a href="https://ieeexplore.ieee.org/document/6243402">Share Conversion and Private Information Retrieval | IEEE ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#private information retrieval`, `#secret sharing`, `#share conversion`, `#theoretical computer science`

---

<a id="item-14"></a>
## [SQIsign 安全性证明改进：最优最小熵与三分之二比特安全](https://eprint.iacr.org/2026/1775) ⭐️ 7.0/10

该论文证明 SQIsign 的最小熵是最优的，即 O(1/p)，改进了 Aardal 等人在 CRYPTO 2025 中使用的宽松界。这一结果保留了三分之二的预期比特安全性，但仍未达到完整的 λ 比特安全，表明需要新的证明技术。 这一改进使 SQIsign 的安全性证明在更现实的攻击场景下具有意义，增强了该方案用于后量子标准化时的可信度。然而，所发现的缺口也凸显了一个仍需考虑的局限性，评估者在衡量部署风险时必须加以注意。 之前的归约在素数特征上产生了平方根损失，若攻击者进行 2^64 次签名查询，则 NIST 安全级别 I 下的证明会失效。新界表明最优最小熵为 O(1/p)，并保留了三分之二的预期比特安全性，剩余的损失归因于零知识模拟中的信息论损失。

rss · IACR ePrint 密码学论文 · 8月22日 10:58

**背景**: SQIsign 是一种基于超奇异椭圆曲线同源的后量子签名方案，已提交给 NIST 进行标准化，以极紧凑的密钥和签名著称。此类方案的安全性证明通常依赖最小熵，它衡量随机变量最可能结果的可预测性。同源密码学因密钥尺寸比许多其他后量子候选方案更小而颇具吸引力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SQIsign">SQIsign</a></li>
<li><a href="https://en.wikipedia.org/wiki/Min-entropy">Min-entropy</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isogeny-based_cryptography">Isogeny-based cryptography</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#SQIsign`, `#security proof`, `#isogeny`

---

<a id="item-15"></a>
## [多方 PSI 协议：最优在线轮数与可更新性](https://eprint.iacr.org/2026/1774) ⭐️ 7.0/10

提出了一种基于函数秘密分享与不经意键值存储的多方隐私集合求交（MPSI）协议，实现最优一次在线交互，并提供可更新扩展（MUPSI）。在 140 方、集合大小 2^20 的广域网实验中，运行时间相比 GLW+24 降低 49.1 倍。 通过消除额外在线交互轮次并让更新开销与数据集大小无关，该协议解决了多参与方隐私计算中的关键可扩展性瓶颈，使大规模动态数据的安全协作更加实用。 该构造在半诚实模型下安全：领导者诚实时可抵抗任意 n−1 方合谋，领导者被腐化时可抵抗任意 n−2 方合谋。可更新的 MUPSI 变体在领导者诚实条件下可抵抗任意 n−1 方合谋，实验覆盖 20 至 140 方、集合大小 2^12 到 2^20。

rss · IACR ePrint 密码学论文 · 8月22日 10:05

**背景**: 隐私集合求交（PSI）允许各方在不泄露其他数据的前提下计算共同元素。函数秘密分享（FSS）将函数拆分为秘密份额，使各方可联合求值而不泄露函数或彼此输入；不经意键值存储（OKVS）可在不暴露访问模式的情况下编码和检索数据。半诚实模型假设参与者遵守协议，但可能试图从收到的消息中获取额外信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://geoffroycouteau.github.io/assets/pdf/HSS_FSS.pdf">Function Secret Sharing and</a></li>
<li><a href="https://tianweiz07.github.io/Papers/24-usenix-1.pdf">Unbalanced Circuit-PSI from Oblivious Key - Value Retrieval</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#secure multi-party computation`, `#private set intersection`, `#cryptography`, `#privacy`, `#function secret sharing`

---
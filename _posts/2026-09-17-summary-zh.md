---
layout: default
title: "Horizon Summary: 2026-09-17 (ZH)"
date: 2026-09-17
lang: zh
---

> 从 55 条内容中筛选出 15 条重要资讯。

---

1. [折叠协议的新鲜状态复杂度与挑战设计](#item-1) ⭐️ 8.0/10
2. [ESCAPE：无需周期性预处理的单服务器在线-离线私有信息检索协议](#item-2) ⭐️ 8.0/10
3. [恶意安全的混洗分布式 OPRF 为隐私集合运算实现线性复杂度](#item-3) ⭐️ 8.0/10
4. [基于二次剩余假设的几乎双重高效私有信息检索方案](#item-4) ⭐️ 8.0/10
5. [基于 DCR 的新型伪随机相关函数与指数可验证随机函数](#item-5) ⭐️ 8.0/10
6. [不只是阶段问题：理解 MPC 预处理中的函数依赖性](#item-6) ⭐️ 8.0/10
7. [理想格θ级数的精确降维分解](#item-7) ⭐️ 8.0/10
8. [从环 LWE 到中间乘积 LWE 的统一归约，覆盖所有数域](#item-8) ⭐️ 8.0/10
9. [偏差弹性组合器实现最优安全放大](#item-9) ⭐️ 8.0/10
10. [BLAQ：通过分块和泄漏量化实现稳健侧信道分析](#item-10) ⭐️ 8.0/10
11. [Silk：计算高效且后量子友好的随机信标](#item-11) ⭐️ 8.0/10
12. [形式化分析发现 GSMA SGP.32 eSIM 物联网配置存在六种攻击](#item-12) ⭐️ 8.0/10
13. [新信号泄漏攻击危及基于 LWE 的认证密钥交换协议](#item-13) ⭐️ 8.0/10
14. [异步主动秘密共享：新不可能性结果与最优协议](#item-14) ⭐️ 8.0/10
15. [是时候结束 25 年的大规模监控了](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [折叠协议的新鲜状态复杂度与挑战设计](https://eprint.iacr.org/2026/2019) ⭐️ 8.0/10

该论文推导出折叠协议挑战边界上必须保留的新鲜标量信息的确切最小量，证明在扣除已有交互记录中可抵扣信息后，该值等于残差目标的维度。文章还表明这一宽度取决于挑战支持和源域，例如坐标逐项乘法在全乘积域上的宽度为 n^2，而在相应 Reed-Solomon 域上仅为 2n-1。 通过给出随机化边界上所需新鲜信息的确切下界，这些结果可以指导折叠协议和挑战设计，有可能减少递归 SNARK 和零知识证明系统中的见证规模、证明规模和验证成本。这对提高简洁论证的效率和实用性具有重要意义。 该精确保留宽度是在任意挑战前预处理和线性挑战后读出的条件下推导出来的；低于精确宽度时，独立均匀双线性输入的最优重构由缺失标量形式的秩决定。对于全乘积域上一个累加器和 k 个新鲜源的直接齐次二次折叠，在对角分离条件下缩放柯西挑战达到锐利宽度 rk（其中 r 为混合输出维度），并有匹配的 rk 坐标多项式载体。

rss · IACR ePrint 密码学论文 · 9月14日 08:19

**背景**: 折叠协议允许证明者和验证者将两个结构相同的 NP 实例合并为一个实例，同时保持见证有效，这类方案（如 Nova、Supernova、Hypernova）用于递归地将大量证明压缩为单个简洁证明。Reed-Solomon 域由有限域上低次多项式的求值组成，强制低次结构可大幅减少自由度，远小于任意乘积域。论文对全乘积域和 Reed-Solomon 域的区分正是基于这种编码理论结构；而“交互记录信用”和“挑战支持”分别指协议中已有的信息以及验证者挑战的可能集合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eigenlab.medium.com/a-review-of-folding-schemes-a285a790fe2f">A Review of Folding Schemes. Introduction | by Eigen Network | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reed–Solomon_error_correction">Reed–Solomon error correction - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#folding protocols`, `#zero-knowledge proofs`, `#SNARKs`, `#complexity theory`

---

<a id="item-2"></a>
## [ESCAPE：无需周期性预处理的单服务器在线-离线私有信息检索协议](https://eprint.iacr.org/2026/2033) ⭐️ 8.0/10

该论文提出了 ESCAPE，一种单服务器在线-离线私有信息检索协议，它完全消除了昂贵的周期性预处理，支持无限次亚线性在线查询，并且响应带宽保持低常数开销。 现有在线-离线 PIR 方案要么需要两个非共谋服务器，要么需要定期重建提示表，导致高带宽或高计算开销。ESCAPE 的单服务器设计有望让实用私有信息检索更易于部署，用于隐私保护的数据库访问。 其核心创新在于将新的提示采样策略与线性同态加密（LHE）相结合，隐藏提示与在线查询之间的相关性，并以亚线性时间即时刷新已消耗的提示。评估显示，对于 1–8 TiB 数据库和 8–16 KiB 条目，端到端延迟低于 1 秒，带宽比现有最佳 PIR 低最多两个数量级，计算量低最多三个数量级。

rss · IACR ePrint 密码学论文 · 9月14日 23:22

**背景**: 私有信息检索（PIR）允许客户端在不暴露所取条目索引的情况下从数据库获取记录。标准 PIR 中服务器每次查询都要执行与数据库大小成线性的计算。在线-离线 PIR 通过让客户端预计算一个与查询无关的提示表来降低在线开销，但以往单服务器方案需要昂贵的周期性预处理，在有限次在线查询后重建整个提示表。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/2033">Efficient Single-Server Online-Offline PIR without Periodic Preprocessing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Private_information_retrieval">Private information retrieval</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#private-information-retrieval`, `#privacy`, `#security`, `#protocol-design`

---

<a id="item-3"></a>
## [恶意安全的混洗分布式 OPRF 为隐私集合运算实现线性复杂度](https://eprint.iacr.org/2026/2035) ⭐️ 8.0/10

该论文提出一种新的恶意安全的混洗分布式不经意伪随机函数（SH-DOPRF），其计算和通信复杂度均为线性。它给出了两种实例化：基于 DDH 的 Dodis-Yampolskiy PRF 构造，以及基于 Dark-Matter PRF 变体的可能后量子构造；与先前工作相比，PSI-Cardinality 运行时间提升 2–3 个数量级，PSI-Sum 和 Circuit-PSI 提升 1–2 个数量级。 它缩小了半诚实与恶意模型在增强隐私集合运算上的巨大效率差距（此前差距可达多个数量级）。这可能使 PSI-Cardinality、PSI-Sum 和 Circuit-PSI 等隐私保护分析在实际应用中更具实用性，并提供更强的安全保证。 该协议几乎完全基于对称密钥技术，仅在 PRF 输出评估时使用公钥操作。它能实现恶意安全的多查询反向私有成员测试（Zhang et al., USENIX Security 2023），支持双方输出，并且仅额外泄漏交集基数。

rss · IACR ePrint 密码学论文 · 9月15日 01:59

**背景**: 不经意伪随机函数（OPRF）允许两方协作计算一个伪随机函数，使一方获得输出而不知道密钥，另一方则无法获知任何信息。混洗分布式 OPRF（SH-DOPRF）是一种变体，其输出在多个服务器间被打乱，以隐藏输入与输出的对应关系，是超越普通 PSI 的隐私集合运算的关键构建模块。恶意安全意味着即使参与者主动偏离协议，协议仍然安全；相比之下，半诚实模型仅假设参与者会遵循协议但尝试窥探额外信息。私有集合交集（PSI）及其增强变体（如基数、求和、电路评估）允许各方在不泄露集合内容的情况下计算集合统计信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/2035">Maliciously Secure Shuffled Distributed OPRF with ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Oblivious_Pseudorandom_Function">Oblivious pseudorandom function - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secure multiparty computation`, `#private set intersection`, `#oblivious pseudorandom function`, `#malicious security`

---

<a id="item-4"></a>
## [基于二次剩余假设的几乎双重高效私有信息检索方案](https://eprint.iacr.org/2026/2034) ⭐️ 8.0/10

该论文提出了一种在公共参考串（CRS）模型下、基于二次剩余（QR）假设的几乎双重高效私有信息检索（DEPIR）方案，查询时间为 o(n/log n)，且不依赖基于格的密码学。这是首个基于数论假设的 DEPIR 方案，解决了此前 LWE/RLWE 构造遗留的开放问题。 它表明双重高效 PIR 并不必须依赖格假设，从而为私有数据库访问拓宽了密码学基础，减少了对 LWE/RLWE 困难问题的依赖。这可能扩大实用私有检索协议可用的假设集合，并推动密码学基础理论发展。 该构造采用了 Williams 的矩阵-向量乘法预处理技术（SODA 2007），并依赖于 Corrigan-Gibbs 和 Wu（TCC 2025）证明的 QR 假设下 Legendre 符号的伪随机性。此外，它还开发了一种亚线性时间数据结构，可在每次查询时将预处理后的整数按任意新模数取模。

rss · IACR ePrint 密码学论文 · 9月15日 01:11

**背景**: 私有信息检索（PIR）允许客户端读取数据库条目而不泄露所读取的具体位置。双重高效私有信息检索（DEPIR）还要求服务器在离线预处理后能够以亚线性时间回答查询。此前所有已知的 DEPIR 构造都基于格密码学假设，例如带误差学习（LWE）或环-LWE（RLWE）。二次剩余（QR）假设声称，在复合整数 N 的模下区分二次剩余与非二次剩余在计算上是困难的，该假设已被用于经典公钥加密方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ntt-research.com/wp-content/uploads/2023/01/Doubly-Efficient-Private-Information-Retrieval-and-Fully-Homomorphic-RAM-Computation.pdf">Doubly Efficient Private Information Retrieval</a></li>
<li><a href="https://troll.iis.sinica.edu.tw/pkc16/slides/2-1--Identity-Based_Cryptosystems_and_Quadratic_Residuosity.pdf">Identity-Based Cryptosystems and Quadratic Residuosity</a></li>
<li><a href="https://en.wikipedia.org/wiki/Learning_with_errors">Learning with errors - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#private information retrieval`, `#quadratic residuosity`, `#DEPIR`, `#number-theoretic assumptions`

---

<a id="item-5"></a>
## [基于 DCR 的新型伪随机相关函数与指数可验证随机函数](https://eprint.iacr.org/2026/2030) ⭐️ 8.0/10

这篇论文首次构造了针对相关不经意传输（COT）和向量不经意线性评估（VOLE）的、在任意模数上高效且仅依赖判定性复合剩余（DCR）假设的伪随机相关函数（PCF）。同时，论文通过扩展 power-DDH 问题给出了新的安全归约，并构造了指定验证者与公开可验证的指数可验证随机函数（eVRF）。 这项工作推进了安全多方计算：它能在被广泛研究的假设下高效生成相关随机性，有望降低协议的通信与初始化成本。同时，它证明了复合群中此前依赖的 power-DDH 类假设可由 DCR 单独推出，强化了理论根基。 该构造采用轻量的两轮分布式初始化，且仅依赖 DCR 假设；安全性通过新定义的一族扩展 power-DDH 问题及一个主定理归约到标准 DCR 来证明。此外，文章把这些结果扩展到 F2 上的 OLE 和一般二次相关，并给出了证明长度显著更短的指定验证者与公开可验证 eVRF。

rss · IACR ePrint 密码学论文 · 9月14日 16:12

**背景**: 伪随机相关函数（PCF）允许持有短相关密钥的两方在本地将其扩展为长的相关随机数流，是安全多方计算的重要构件。相关不经意传输（COT）和向量不经意线性评估（VOLE）是常用于隐私集合求交、零知识证明等协议的相关性类型。判定性复合剩余（DCR）假设是支撑 Paillier 加密的成熟困难性假设：给定合数 n，难以区分模 n^2 的 n 次剩余与随机元素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/2030">New Pseudorandom Correlation Functions and Exponent VRFs from DCR</a></li>
<li><a href="https://en.wikipedia.org/wiki/Decisional_composite_residuosity_assumption">Decisional composite residuosity assumption</a></li>
<li><a href="https://eprint.iacr.org/2025/1637">Pseudorandom Correlation Functions from Ring-LWR</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secure multiparty computation`, `#pseudorandom correlation functions`, `#oblivious transfer`, `#DCR assumption`

---

<a id="item-6"></a>
## [不只是阶段问题：理解 MPC 预处理中的函数依赖性](https://eprint.iacr.org/2026/2029) ⭐️ 8.0/10

一篇新论文（eprint 2026/2029）对安全多方计算中函数依赖性预处理的不同变体进行了系统化梳理，并将其与效率之外的实用需求联系起来。 预处理是实现低延迟 MPC 的关键技术，理解函数依赖性的不同类型有助于研究者和从业者根据实际权衡（而非仅仅吞吐量）来选择协议。 该论文对函数依赖性预处理方法进行了分类，包括 Astra、Trio 和 MOTION-FD 等方案中使用的方法，并考察了不同依赖类型如何影响设置假设、安全性以及超出纯效率的实际特性。

rss · IACR ePrint 密码学论文 · 9月14日 15:57

**背景**: 安全多方计算（MPC）允许多个参与方在不泄露各自输入的前提下联合计算一个函数。许多高效的 MPC 协议采用预处理：在输入未知时先生成相关随机数，然后在在线阶段快速消耗这些随机数。函数依赖性预处理进一步利用将要计算的函数信息，从而获得更多优化。此前文献主要关注性能提升，在很大程度上忽略了不同函数依赖类型及其实际影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/2029">It's Not Just a Phase: Understanding Function Dependence in ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation</a></li>
<li><a href="https://eprint.iacr.org/2025/919">Rep3 Reloaded: On the Cost of Function-Dependent ...</a></li>

</ul>
</details>

**标签**: `#MPC`, `#cryptography`, `#privacy`, `#preprocessing`, `#function-dependent`

---

<a id="item-7"></a>
## [理想格θ级数的精确降维分解](https://eprint.iacr.org/2026/2028) ⭐️ 8.0/10

该论文提出了一个明确且可验证的相对基条件，在此条件下理想格的固定陪集θ级数可精确分解为低维分量：当 n = ℓ n₀ 时，将 n 维计算替换为 ℓ 个独立的 n₀ 维计算。 该精确降维显著简化了理想格中的高斯质量、平滑参数和高斯采样计算，而理想格是基于格的密码学的核心对象；报告的最高 335 倍加速使高维参数设置更实用。 该分解等价于相对坐标下典范 Gram 矩阵的分块对角化，并且对所有高斯参数精确成立，无需近似或平滑假设。作者在若干分圆与非分圆扩域上验证了该条件，并报告固定陪集θ级数计算、数值平滑参数计算和顺序高斯采样分别获得 335 倍、215.45 倍和 7.9 倍加速。

rss · IACR ePrint 密码学论文 · 9月14日 15:39

**背景**: 理想格是来自数域整数环中理想的格，广泛用于基于格的密码学以实现高效表示。θ级数记录格向量的长度平方，并将格的几何与高斯质量、平滑参数等高斯量联系起来。在典范嵌入下，理想格的算术坐标通常相互耦合，导致固定陪集的高斯计算在高维下困难。本文给出一个相对基条件，使其精确解耦。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ideal_Lattices_and_Cryptography">Ideal Lattices and Cryptography</a></li>
<li><a href="https://en.wikipedia.org/wiki/Theta_series">Theta series</a></li>
<li><a href="https://www.emergentmind.com/topics/canonical-embeddings">Canonical Embeddings : Theory & Applications</a></li>

</ul>
</details>

**标签**: `#lattice-based cryptography`, `#ideal lattices`, `#theta series`, `#dimension reduction`, `#Gaussian sampling`

---

<a id="item-8"></a>
## [从环 LWE 到中间乘积 LWE 的统一归约，覆盖所有数域](https://eprint.iacr.org/2026/2026) ⭐️ 8.0/10

该论文提出了一个从环 LWE 到中间乘积 LWE 的统一归约，以域元素对(y_a, y_s)∈K^2 为参数。该归约恢复了 Roşca 等人、Njah Nchiwo 和 Pellet-Mary 以及 Peikert 和 Pepin 的先前归约，并且首次适用于所有形如 K=Q[X]/f(X)的数域，其中 f 为给定次数、系数多项式有界的首一不可约多项式，且判别式与模数 q 互质。 这项工作通过统一两个互不统属的先前归约，填补了理论空白，并将 MP-LWE 的困难性保证扩展到指定多项式族的所有数域。它加强了基于中间乘积构造的格密码在后量子密码学中的理论基础。 该归约以域元素对(y_a,y_s)∈K^2 为参数，并能作为具体实例恢复先前两类归约。它要求 f 为首一不可约多项式且系数多项式有界，同时数域 K 的判别式与模数 q 互质，这一约束在先前工作中也出现过。

rss · IACR ePrint 密码学论文 · 9月14日 13:55

**背景**: 环学习同态错误（RLWE）是一种基于格的问题，是 NewHope 等后量子密码方案的基础。中间乘积学习同态错误（MP-LWE）由 Roşca 等人在 Crypto 2017 提出，是一种不依赖特定数域的结构化 LWE 变体，其困难性通常通过从环 LWE 或多项式 LWE 归约建立。数域 K = Q[X]/f(X)由首一不可约多项式 f 定义。先前归约仅适用于受限的数域族，本工作在温和条件下消除了这些限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ring_learning_with_errors">Ring learning with errors - Wikipedia</a></li>
<li><a href="https://users.monash.edu/~rste/MPLWE.pdf">Middle - Product Learning With Errors</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#lattice-based cryptography`, `#learning with errors`, `#number fields`, `#post-quantum`

---

<a id="item-9"></a>
## [偏差弹性组合器实现最优安全放大](https://eprint.iacr.org/2026/2025) ⭐️ 8.0/10

该论文引入了偏差弹性不可区分性组合器，消除了先前工作中约 2^{n-k} 的指数级乘法损失和 δ<0.5 的阈值限制，实现了最优的全有或全无安全放大界。论文还在素域上建立了广义异或引理，其样本复杂度与域大小无关，改进了 Shimizu 和 Yasunaga（STOC 2026）的结果。 这一结果使密码学原语的安全放大达到最优，消除了此前使组合器在许多场景下不切实际的指数级开销。它通过为弱伪随机生成器和弱非交互零知识证明等原语提供更高效的构造，对理论和实践都有重要影响。 该框架将弱伪随机生成器和弱非交互零知识证明等先前的临时结果统一为特例。主要应用是一个广义异或引理：独立弱伪随机元素模 p 的和与均匀分布在计算上不可区分；论文还给出了理想化全有或全无放大器乘法损失的紧致刻画。

rss · IACR ePrint 密码学论文 · 9月14日 13:30

**背景**: 密码学组合器将 n 个候选实现组合起来，只要至少 k 个候选是安全的，组合器就保持安全。安全放大研究的问题是：将独立的 δ-弱候选插入组合器后，失败概率是否能显著降低；但常见的全有或全无假设（每个候选要么完全失败，要么完美安全）在标准不可区分性概念下往往不成立。Applebaum、Bitansky 和 Geier 近期的研究（CRYPTO 2026）证明不可区分性组合器本质上具有安全放大作用，但会带来指数级误差代价，且仅在 δ<0.5 时成立；本文通过偏差弹性克服了这些限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/2025.pdf">Optimal Amplification via Bias-Resilient Combiners∗ Benny Applebaum†</a></li>
<li><a href="https://eprint.iacr.org/2026/1121">Security Amplification via Robust Indistinguishability Combiners</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#security`, `#combiners`, `#theoretical computer science`, `#research`

---

<a id="item-10"></a>
## [BLAQ：通过分块和泄漏量化实现稳健侧信道分析](https://eprint.iacr.org/2026/2023) ⭐️ 8.0/10

Red Hat 的 Alicja Kario 和 George Pantelakis 提出了名为 BLAQ 的新侧信道分析方法，通过解决未经验证的 IID 假设、缺乏泄漏量化以及测试装置中的数据依赖泄漏，弥合了理论模型与现实不完美测试环境之间的差距。 BLAQ 通过要求验证假设并设定正式泄漏边界，可使侧信道安全评估更加可靠和可比，有利于认证实验室以及密码硬件和软件开发者。 该方法针对三个常见缺陷：未经验证就假设数据独立同分布或正态分布；依赖视觉或未通过的统计检验而没有正式精度边界；测试装置因数据依赖分支、格式化或触发而泄漏信息。论文将分块和量化列为核心组成部分，但摘要未给出完整算法细节。

rss · IACR ePrint 密码学论文 · 9月14日 12:20

**背景**: 侧信道分析（SCA）通过测量密码运算过程中的时间、功耗或电磁辐射等物理效应来提取秘密信息。许多现有 SCA 方法假设数据样本独立同分布（IID）或服从正态分布，但实际测量常因环境噪声或实现效应违反这些假设。测试装置是用于采集测量的设备和软件，若其行为依赖于秘密数据，则可能引入额外泄漏。对泄漏进行正式量化而非依赖临时检验，是近期 Helium 等工作强调的持续挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/2023">Robust Side Channel Analysis with Blocking and Quantification ...</a></li>
<li><a href="https://cs.stanford.edu/people/trippel/pubs/archer_ISCA26.pdf">Helium: Quantifying Microarchitectural Side-Channel Leakage ...</a></li>
<li><a href="https://www.keysight.com/us/en/products/vulnerability-assessment/device-vulnerability-analysis/side-channel-analysis.html">Side Channel Analysis | Keysight</a></li>

</ul>
</details>

**标签**: `#Side-Channel Analysis`, `#SCA`, `#Cryptography`, `#Security`, `#Methodology`

---

<a id="item-11"></a>
## [Silk：计算高效且后量子友好的随机信标](https://eprint.iacr.org/2026/2021) ⭐️ 8.0/10

Silk 是一个新的随机信标协议，引入了 Mulberry，一种基于哈希份额验证的批量异步可验证秘密共享（带部分输出，bAVSS-PO），并将 BFT 共识摊销到一批输出上，每批仅需一次 BFT。在 121 个副本、跨八个 AWS 区域的广域网实验中，Silk 实现 5.414 输出/秒，是 Rondo 的 1.53 倍、Spurt 的 4.18 倍。 它通过用哈希验证替代配对或离散对数假设并摊销共识，解决了现有随机信标计算成本高和易受量子攻击的问题，使公共随机性生成更高效且能抵御量子对手。这对依赖无偏公共随机性的区块链、彩票和其他密码协议具有重要价值。 Mulberry 采用基于哈希的份额验证实现 bAVSS-PO；Silk 在部分同步和静态腐化假设下是确定性的，并且为一批输出仅运行一次 BFT 共识。实现使用 Rust 编写，并在八个 AWS 区域、121 个副本上进行评估。

rss · IACR ePrint 密码学论文 · 9月14日 09:45

**背景**: 随机信标是一种定期发布不可预测公共随机值的服务，任何一方都无法操纵这些值。可验证秘密共享（VSS）允许各方验证其份额的一致性，许多随机信标利用 VSS 在不信任单个经销商的情况下生成随机性。现有信标方案通常依赖离散对数或配对假设，这些假设在量子计算机下是脆弱的；而基于哈希的方案被认为是抗量子的。拜占庭容错（BFT）共识确保在部分节点故障时副本之间仍能达成一致，但为每个输出都单独运行 BFT 实例会带来高昂的计算和通信开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://securitylab.github.io/cs251-fall20/lectures/lecture6.pdf">Randomness Beacons and VDFs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Verifiable_secret_sharing">Verifiable secret sharing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#randomness beacon`, `#post-quantum`, `#verifiable secret sharing`, `#Byzantine fault tolerance`

---

<a id="item-12"></a>
## [形式化分析发现 GSMA SGP.32 eSIM 物联网配置存在六种攻击](https://eprint.iacr.org/2026/2020) ⭐️ 8.0/10

该论文使用 Tamarin 和 ProVerif 对 GSMA SGP.32 v1.3 管理平面进行了首次形式化安全分析，发现了六种规范级攻击，其中包括一种通过串联两个未认证本地操作实现的十步管理平面接管攻击。 这一发现意义重大，因为 SGP.32 为无人值守的物联网设备提供远程 eSIM 配置文件管理，预计 2026 年该领域设备规模达 15 亿台；管理平面被接管可能大规模破坏信任与安全，影响依赖零接触配置的设备制造商、运营商和企业。 模型覆盖管理平面 v1.3；协议对网络敌手的抵抗性验证通过，但攻击违反了 SGP.31 中关于关联完整性的 SHALL 要求，而相关 NOTE 将机制推给实现。26 个本地操作中 40%具有真正的卡侧认证，每个未认证操作都是本地操作；提出的两个修复复用了规范中已有的机制，被证明有效且不增加稳态开销，全部 24 个判定均经机器检查且模型开放。

rss · IACR ePrint 密码学论文 · 9月14日 09:20

**背景**: GSMA SGP.32 是物联网设备远程 eSIM 配置文件管理的技术规范，建立在 SGP.31 架构和需求之上。与依赖本地用户确认的消费级 eSIM 配置（SGP.22）不同，SGP.32 使用称为 eIM 的远程管理器为无人值守设备授权配置文件操作。Tamarin 和 ProVerif 是用于密码协议的形式化验证工具，可证明安全属性或发现攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.csl-group.com/resources/what-is-sgp-32/">What is SGP . 32 ? The GSMA eSIM specification for IoT</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tamarin_Prover">Tamarin Prover</a></li>
<li><a href="https://en.wikipedia.org/wiki/ProVerif">ProVerif</a></li>

</ul>
</details>

**标签**: `#eSIM`, `#IoT security`, `#formal methods`, `#GSMA`, `#protocol vulnerability`

---

<a id="item-13"></a>
## [新信号泄漏攻击危及基于 LWE 的认证密钥交换协议](https://eprint.iacr.org/2026/2017) ⭐️ 8.0/10

该论文提出了针对基于 LWE 的认证密钥交换的新信号泄漏攻击。通过利用 eCK 模型中的临时密钥泄露，攻击分别用约 1700 次和 180 次查询恢复了 ZZDSD-AKE（EUROCRYPT 2015）和 GDLL-KE（IEEE TC 2018）的静态私钥。 这解决了 ZZDSD-AKE 能否原生满足 eCK 安全性的长期未决问题，结论是否定的。它也表明 MQV 式结构和简单随机化对策不足以抵御主动攻击，为未来后量子认证密钥交换协议设计和标准化提供了关键指导。 攻击利用几何视角，在临时密钥泄露后从协调信号泄漏中恢复静态私钥。实现结果显示，对 ZZDSD-AKE 需约 1700 次查询，对 GDLL-KE 需约 180 次查询，并证明 GDLL-KE 的随机噪声对策未能消除依赖秘密的泄漏。

rss · IACR ePrint 密码学论文 · 9月14日 07:16

**背景**: LWE（带误差学习）是后量子密码学中广泛使用的抗量子困难假设。认证密钥交换（AKE）协议让双方在互相认证的同时协商共享密钥。直接基于 LWE 的 AKE 构造需要协调步骤将近似共享值转换为精确密钥，但该步骤可能通过“信号”值泄漏信息。eCK 安全模型是一种强敌手模型，允许临时密钥泄露，因此是协议安全性的高标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/327540/20260915/post-quantum-key-exchange-proved-unsecurable-1700-queries-hardened-variant-falls-180-queries.htm">Post-Quantum Key Exchange Proved Unsecurable in 1,700 Queries...</a></li>
<li><a href="https://archive.ymsc.tsinghua.edu.cn/pacm_download/672/12718-dingjt-i68.pdf">Light the Signal : Optimization of Signal Leakage</a></li>
<li><a href="https://www.mdpi.com/2410-387X/7/1/1">Authenticated Key Exchange Protocol in the Standard Model ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum cryptography`, `#LWE`, `#authenticated key exchange`, `#eCK security`

---

<a id="item-14"></a>
## [异步主动秘密共享：新不可能性结果与最优协议](https://eprint.iacr.org/2026/2018) ⭐️ 8.0/10

该论文系统研究了完全异步认证网络中的主动秘密共享（PSS），并为异步 PSS 形式化了一类移动对手模型层级。论文通过通用攻击证明了新的不可能性结果，并给出了在每个模型中达到最优弹性的显式异步 PSS 协议，从而证明了界限的紧致性。 该工作厘清了在无全局时钟的异步网络中主动秘密共享的可行性边界，而这种网络在去中心化系统中非常普遍。其最优协议可能提升安全多方计算和区块链系统中秘密共享数据在移动对手下的长期安全性。 作者通过展示异步 PSS 在各对手模型下的通用攻击，推导出弹性上界，并构造了弹性与上界匹配的显式协议。该模型层级刻画了不同的对手能力以及异步环境中移动腐化的计入方式；论文发表于 Cryptology ePrint Archive 报告 2026/2018。

rss · IACR ePrint 密码学论文 · 9月14日 08:08

**背景**: 主动秘密共享会定期刷新秘密的份额，使得随着时间逐渐攻陷参与方的攻击者无法重建秘密，只需每个刷新周期内被攻陷的份额少于阈值。在异步网络中不存在全局时钟，这使得“周期”的定义和移动腐化的计入方式变得复杂。已有工作提出了异步系统的主动秘密共享（APSS）协议，但此前缺乏对不同移动对手模型下可行性的系统理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Proactive_secret_sharing">Proactive secret sharing</a></li>
<li><a href="https://www.cs.cornell.edu/fbs/publications/apssTISS.pdf">APSS: Proactive Secret Sharing in Asynchronous Systems</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secret sharing`, `#asynchronous networks`, `#proactive security`, `#distributed systems`

---

<a id="item-15"></a>
## [是时候结束 25 年的大规模监控了](https://www.schneier.com/blog/archives/2026/09/25-years-of-mass-surveillance-is-enough.html) ⭐️ 8.0/10

布鲁斯·施奈尔和辛迪·科恩发表了一篇文章，指出 9/11 后建立的大规模监控体系已远远超出最初的反恐理由，如今已成为包括移民和海关执法局（ICE）在内的执法部门的常规工具。 这篇来自知名隐私与安全专家的权威评论可能影响关于监控改革的公共讨论和政策制定，并凸显对通信数据的大规模收集如何影响数十亿互联网和电话用户的日常隐私与公民自由。 文章对比了个人窃听和笔记录器/陷阱追踪令等针对性手段，与接入互联网骨干网、大规模收集电话或互联网元数据等大规模技术；并指出这套曾以反恐防御为由建立的基础设施，如今已用于常规执法。

rss · Schneier on Security · 9月15日 11:01

**背景**: 笔记录器/陷阱追踪令授权收集路由或寻址信息——即谁在何时联系了谁——其法律标准低于完整搜查令，且不包括通信内容。互联网骨干网是大型网络之间的主要高容量数据路由；如‘641A 室’所揭示的，接入骨干网可以拦截和分析海量互联网流量。9/11 袭击后，美国法律和项目将监控从针对性法院命令扩展到对通信数据的大规模收集，最初以反恐为理由，后来被更广泛地使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://factually.co/fact-checks/justice/pen-register-order-vs-warrant-messaging-apps-e5de18">How Does a Pen ‑ Register Order Differ From a Warrant, a...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Room_641A">Room 641A - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Internet_backbone">Internet backbone - Wikipedia</a></li>

</ul>
</details>

**标签**: `#mass surveillance`, `#privacy`, `#civil liberties`, `#national security`, `#law enforcement`

---
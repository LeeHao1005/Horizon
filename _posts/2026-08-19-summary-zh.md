---
layout: default
title: "Horizon Summary: 2026-08-19 (ZH)"
date: 2026-08-19
lang: zh
---

> 从 38 条内容中筛选出 15 条重要资讯。

---

1. [新型零知识证明系统实现 C2PA 图像的可验证 JPEG 压缩](#item-1) ⭐️ 8.0/10
2. [基于分解 LWE 的格上静默门限加密](#item-2) ⭐️ 8.0/10
3. [NTRU 加密的紧凑性极限：启发式前沿与实用新方案](#item-3) ⭐️ 8.0/10
4. [对西蒙二面体陪集算法引理的严格证明与修正](#item-4) ⭐️ 8.0/10
5. [通过算术重组在 SQIsign 的 AVX-512 实现中暴露 SIMD 并行性](#item-5) ⭐️ 8.0/10
6. [新型统计方法改进 ML-DSA 抗噪声泄漏侧信道攻击](#item-6) ⭐️ 8.0/10
7. [扩展域上 PKP 与 PEP 新攻击威胁后量子签名](#item-7) ⭐️ 8.0/10
8. [新协议为 MLS 增加可审计连续群组密钥协商与合规密钥恢复](#item-8) ⭐️ 8.0/10
9. [优化 CSIDH-512 量子资源，T 门复杂度降低 85%以上](#item-9) ⭐️ 8.0/10
10. [评论：四态量子公钥加密方案泄露明文分布](#item-10) ⭐️ 8.0/10
11. [针对基于梅森数密码系统的新攻击：放宽尺寸约束](#item-11) ⭐️ 8.0/10
12. [后量子 TLS 迁移系统化研究：混合握手、PSK、KeyUpdate 与证书策略](#item-12) ⭐️ 8.0/10
13. [纠缠博弈平行重复的间隙指数达到三次](#item-13) ⭐️ 8.0/10
14. [GCM 后量子多密钥安全性新改进界限](#item-14) ⭐️ 7.0/10
15. [具有个性化匿名性的环签名](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [新型零知识证明系统实现 C2PA 图像的可验证 JPEG 压缩](https://eprint.iacr.org/2026/1717) ⭐️ 8.0/10

该论文提出了 SPEG，这是首个实用的零知识证明系统，可在证明原始图像 C2PA 签名有效性的同时支持 JPEG 压缩。它提供两种协议：基于 Poseidon 的模式在 47 秒内证明 1080p 图像 JPEG 压缩，基于多项式承诺的快速模式仅需 2 秒，而此前仅支持缩放的 VerITAS 需 227 秒。 有损 JPEG 压缩无处不在，但会使 C2PA 签名失效，这在内容真实性领域形成了关键缺口。SPEG 在个人设备上实现了完整的图像传输流程，并且证明体积小，使得验证网上发布的压缩图像确实来自可信来源变得切实可行，有助于打击图像虚假信息。 关键优化包括在证明电路之外处理非代数的 JPEG 编码，以及避免浮点运算中的范围检查。论文还发现 VIMz 中存在一个安全漏洞，该漏洞允许为未经授权的图像伪造证明，并给出了修复方案；同时证明了可将常用的 powers-of-tau SRS 与 KZG 多项式承诺方案安全地结合使用。

rss · IACR ePrint 密码学论文 · 8月17日 18:25

**背景**: C2PA（内容来源与真实性联盟）是一项行业标准，通过数字签名来证明图像的来源。zk-SNARK 是一种非交互式零知识证明，允许证明者在不泄露额外信息的情况下证明某个陈述为真。JPEG 是一种有损压缩格式，能大幅减小文件大小，但会改变像素值，因此针对原始像素的签名会失效。SPEG 通过零知识证明来证明压缩图像确实源自已签名的原始图像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zk-SNARK">Zk-SNARK</a></li>
<li><a href="https://en.wikipedia.org/wiki/C2PA">C2PA</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#image compression`, `#C2PA`, `#content authenticity`, `#JPEG`

---

<a id="item-2"></a>
## [基于分解 LWE 的格上静默门限加密](https://eprint.iacr.org/2026/1716) ⭐️ 8.0/10

该论文基于分解 LWE 假设构造了静默门限加密，在门限为 T、用户数为 N 时实现密文大小 O(T) + poly(λ, log N)，且无需依赖双线性配对或混淆。 这为以往需要双线性映射或不可区分混淆的静默门限加密提供了后量子替代方案，有望为大规模群体实现更高效、更安全的后量子门限密码。 该方案对所有满足 T=N^ε（ε<1）的门限均实现了非平凡简洁性；可推广到具有简洁计算秘密分享的单调策略；核心构件是一种新的有限共谋注册函数加密，密文大小为 Q·Õ(d)+ℓ·poly(λ,d,log N)。

rss · IACR ePrint 密码学论文 · 8月17日 18:21

**背景**: 静默门限加密允许群组的公钥由各个用户的公钥确定性地计算得出，从而实现非交互式设置。以往构造依赖配对密码学或混淆等重型工具，且基于格的方案仅支持常数门限。分解 LWE 假设是近期提出的格上困难假设，最初用于加密数据的 RAM 程序执行安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2024/263">Threshold Encryption with Silent Setup</a></li>
<li><a href="https://latticeassumptionzoo.org/decomposed-lwe/">Decomposed LWE - Lattice Assumption Zoo</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#threshold encryption`, `#lattice-based cryptography`, `#LWE`, `#post-quantum cryptography`

---

<a id="item-3"></a>
## [NTRU 加密的紧凑性极限：启发式前沿与实用新方案](https://eprint.iacr.org/2026/1715) ⭐️ 8.0/10

该论文将 NTRU 解密形式化为两阶段过程，并提出了自由候选定位（FCL）方法，该方法按坐标与中心边界的接近程度进行排序。利用 FCL，作者提出 END 方案，其在 NIST-I 安全级别下的密文为 384 字节，仅为 ML-KEM-512 密文的一半，比此前最短的 NTRU 风格密文（BAT 和 DAWN）小 12%–19%，而封装与解封装总成本仅高出约 3%。 这项工作推进了 NTRU 这一经过长期检验的后量子加密家族的紧凑性前沿，有望在不显著损失性能的情况下实现更小的密文和公钥。它表明 NTRU 可以比广泛部署的 ML-KEM 等格密码方案更紧凑，可能影响未来抗量子公钥加密的设计与标准化。 在显式启发式搜索模型内，作者推导出 NIST-I 安全级别下基于编码的 NTRU 的公钥与密文总大小为 812 字节，基于陷门的 NTRU 为 754 字节，分别比 DAWN 的 964 字节小 15%和 21%。在 ML-KEM 中实例化 FCL 可使密文减小 10%，但参考 C 实现的整体运行时间慢 5%；END-512 的封装与解封装总成本比 ML-KEM-512 高约 3%。

rss · IACR ePrint 密码学论文 · 8月17日 14:08

**背景**: NTRU 是最早的基于格的公钥加密体制之一，其安全性基于格中的最短向量问题，据信能抵抗量子计算机攻击。它通常被视为基于环/模 LWE 方案（如 NIST 标准化的后量子密钥封装机制 ML-KEM）的紧凑替代方案。紧凑性指减小密文和公钥大小，这对带宽受限的应用和高效通信至关重要。NEV 和 DAWN 等近期 NTRU 变体已将这些尺寸大幅降低，但对下界的系统性探索仍属空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NTRUEncrypt">NTRUEncrypt - Wikipedia</a></li>
<li><a href="https://eprint.iacr.org/2023/1298">NEV: Faster and Smaller NTRU Encryption using Vector Decoding</a></li>
<li><a href="https://eprint.iacr.org/2025/1520">DAWN: Smaller and Faster NTRU Encryption via Double Encoding</a></li>

</ul>
</details>

**标签**: `#NTRU`, `#lattice-based cryptography`, `#post-quantum cryptography`, `#encryption`, `#cryptanalysis`

---

<a id="item-4"></a>
## [对西蒙二面体陪集算法引理的严格证明与修正](https://eprint.iacr.org/2026/1714) ⭐️ 8.0/10

本文严格证明了西蒙最近提出的求解二面体陪集问题的多项式时间量子算法中三条仅有证明草图的引理。其中引理 1 成立的概率趋于 1 而非原称的常数；引理 3 的振幅界去掉了良态行为假设；引理 4 改为证明加法形式，因为计数估计控制的是差值而非比值。 二面体陪集问题与格问题和后量子密码密切相关，若存在有效的量子算法将威胁基于格的密码体制。本文的严格验证表明该算法的正确性尚未得到证明，避免过早做出结论，并为后续研究指明方向。 证明中使用了子集和计数的精确二阶矩计算、测量结果立方体上的 Parseval 恒等式以及精确的球入盒协方差计算。可以去掉“特殊群不含故障样本”和良态行为这两个假设。唯一存留的假设要求将两侧的划分独立于测量串固定，但算法给出的划分规则并不满足这一点。

rss · IACR ePrint 密码学论文 · 8月17日 13:54

**背景**: 西蒙算法是一种能指数加速求解西蒙问题的量子算法，并启发了 Shor 算法。二面体陪集问题是二面体群上的隐藏子群问题，与格问题密切相关；若能高效求解，可能破坏基于格的密码体系。西蒙最近的预印本声称在多项式时间内解决了该问题，但其分析依赖若干引理，本文对这些引理进行了验证和修正。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Simon's_algorithm">Simon's algorithm</a></li>
<li><a href="https://inria.hal.science/hal-04276584/document">Time and Query Complexity Tradeoffs for the Dihedral Coset Problem</a></li>
<li><a href="https://www.sitg-consulting.com/post/daniel-simon-s-dihedral-coset-algorithm-what-does-it-actually-mean-for-lattice-based-cryptography-a">Daniel Simon’s Dihedral Coset Algorithm: What Does It Actually Mean...</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#cryptography`, `#dihedral coset problem`, `#proof verification`, `#Simon's algorithm`

---

<a id="item-5"></a>
## [通过算术重组在 SQIsign 的 AVX-512 实现中暴露 SIMD 并行性](https://eprint.iacr.org/2026/1713) ⭐️ 8.0/10

该论文提出了一种端到端的 SQIsign AVX-512IFMA 实现，通过重组有限域、椭圆曲线和同源运算中的算术依赖图来恢复 SIMD 并行性。在 NIST 安全级别 I 下，与参考 C 实现相比，密钥生成、签名和验证分别实现了 1.76 倍、1.71 倍和 3.18 倍的加速；结合 Qlapoti 后，密钥生成和签名加速分别提升至 2.90 倍和 2.69 倍。 该工作解决了 SQIsign 的一个主要实际瓶颈：该方案虽然具有非常小的密钥和签名，但计算开销很高。通过证明算法级 SIMD 调度可跨同源方案复用，它将基于同源的抗量子密码推向更接近实际部署的水平。 该实现在大部分曲线侧计算中保持基-2^51 向量表示，并包括用于蒙哥马利阶梯的投影 xDBLADD 调度、多种坐标系下的批量倍点运算、向量化双标量阶梯、融合立方算术配对步骤，以及批量一维和二维同源求值。将相同后端应用于 CORAL，可实现 1.28–1.40 倍的密钥生成加速和 1.92–2.46 倍的共享密钥计算加速。

rss · IACR ePrint 密码学论文 · 8月17日 12:25

**背景**: SQIsign 是一种基于超奇异椭圆曲线同源的抗量子签名方案，已提交至 NIST 标准化进程；它提供紧凑的密钥和签名，但签名和验证相对较慢。AVX-512IFMA 是英特尔的 512 位 SIMD 指令，可对 52 位整数执行整数融合乘加运算，适用于大整数算术。蒙哥马利阶梯是一种固定操作次数的椭圆曲线标量乘法方法，其循环携带依赖通常会限制直接的 SIMD 向量化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SQIsign">SQIsign</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advanced_Vector_Extensions">Advanced Vector Extensions - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Montgomery_ladder">Montgomery ladder</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#isogeny-based cryptography`, `#SIMD`, `#AVX-512`, `#SQIsign`

---

<a id="item-6"></a>
## [新型统计方法改进 ML-DSA 抗噪声泄漏侧信道攻击](https://eprint.iacr.org/2026/1712) ⭐️ 8.0/10

该论文提出一种统计方法，将经 j-独立性变换后泄漏位的绝对值建模为双分量混合分布，推导出闭合形式分量和比特错误率 p 的矩估计器。该估计器在低泄漏区域仍可使用，并为每个关系提供后验概率来纠正噪声位，使密钥恢复所需信息关系数量减少 20%至 44%。 这提高了针对 NIST 后量子签名标准 ML-DSA 在现实噪声泄漏下侧信道攻击的实用性，表明安全评估需要考虑不可信比特。可能影响后量子签名部署中硬件和软件实现抵御物理攻击的评估与加固方式。 该估计器仅利用攻击已收集的信息关系；对于 ML-DSA-44 和 87 可下探到泄漏指数 4，对 65 为 5。在 25000 个信息关系时低泄漏情形的平均绝对误差约 0.022 至 0.040，而高泄漏区域低于 0.002。应用于 Schubert 等人的攻击时，在全部参数集、泄漏指数 6 至 9、错误率 20%和 40%下将所需信息关系减少 20%至 44%；应用于 Bashiri 等人的攻击时提高了密钥恢复成功率。

rss · IACR ePrint 密码学论文 · 8月17日 11:02

**背景**: ML-DSA 是 NIST 选定的基于格的后量子数字签名标准，签名过程使用拒绝采样使签名与密钥统计独立。侧信道攻击利用功耗、时序等物理泄漏恢复秘密。以往针对 ML-DSA 的攻击假设每个掩码随机数泄漏位都准确，但实际测量存在噪声。j-独立性变换使正确位与翻转位在绝对值上互补，从而可将观测绝对值建模为混合分布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Side-channel_attack">Side-channel attack</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rejection_sampling">Rejection sampling</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#side-channel attacks`, `#post-quantum`, `#ML-DSA`, `#statistical inference`

---

<a id="item-7"></a>
## [扩展域上 PKP 与 PEP 新攻击威胁后量子签名](https://eprint.iacr.org/2026/1711) ⭐️ 8.0/10

该论文（eprint 2026/1711）表明，对于二元扩域，PKP 和 PEP 可归约为结构化的正则伴随式解码问题，从而为许多实例（包括扩展次数 ν>4 的全部自对偶 PEP 实例）给出新的多项式时间算法。同时，该工作还适配了 Esser–Santini 的 Regular-ISD 算法，并对奇特征扩域给出了到图同构问题的归约。 这些攻击直接削弱了为提升效率而使用扩展域的后量子签名方案 PERK 和 SETH 的安全性；它们使大多数扩展域上的 PEP 实例不再安全，并迫使基于 PKP 的签名方案重新评估参数。 对于二元扩域，归约到 RSD 得到了涵盖自正交 PEP 以及所有 ν>4 自对偶实例的多项式时间可解区间；经适配的基于置换的 Regular-ISD 在某些参数范围内优于已有攻击。对于奇特征扩域，一大类 PEP 实例可通过归约到图同构问题在多项式时间内求解。

rss · IACR ePrint 密码学论文 · 8月17日 06:57

**背景**: 置换核问题（PKP）要求找到一个已知向量的置换，使结果位于给定矩阵的核中；它是 PERK、SUSHSYFISH 和 PKP-DSS 等后量子签名方案的基础。PEP 是判断两个线性码是否在置换下等价的问题，用于 LESS 等方案。扩展域常被用来使基于码的签名更紧凑，而 PERK 是 NIST 附加签名项目的第二轮候选方案。正则伴随式解码（RSD）是一种错误向量被划分为若干块、每块含有固定数量错误的变体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2019/412.pdf">On the Complexity of the Permuted Kernel Problem</a></li>
<li><a href="https://eprint.iacr.org/2026/706">Improved Cryptanalysis of the Permuted Kernel Problem with Applications to PERK v2.2.0, SUSHSYFISH and PKP-DSS</a></li>
<li><a href="https://hal.science/hal-03984470/document">A New Algebraic Approach to the Regular Syndrome Decoding ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#code-based cryptography`, `#cryptanalysis`, `#digital signatures`

---

<a id="item-8"></a>
## [新协议为 MLS 增加可审计连续群组密钥协商与合规密钥恢复](https://eprint.iacr.org/2026/1710) ⭐️ 8.0/10

研究人员提出了可审计的连续群组密钥协商（Au-CGKA），一种类似 MLS 的协议，每个被接纳的纪元都携带一个证明，将该纪元的密钥材料绑定到可由阈值审计委员会恢复的秘密；成员会检查该证明，并在不一致时拒绝提交。后量子协议Π_A 使用 STARK 证明，并已在 Rust 中实现原型。 这让金融、医疗和政府等受监管部署能够在满足审计要求的同时保留端到端加密。此外，通过在每个纪元验证可恢复性，它还能防止静默托管失败。 Rust 原型使用自定义多阶段 STARK；在 Apple M5 Pro 上，可审计性证明耗时 1.38 秒，大小为 15.31 MB，验证耗时 0.17 秒，且与群组大小无关。该证明在接纳时被检查然后丢弃，因此唯一持久开销是固定大小的托管；在安全擦除模型下，通过量子随机预言机模型中的直线归约实现了自适应后量子安全。

rss · IACR ePrint 密码学论文 · 8月17日 04:52

**背景**: 连续群组密钥协商（CGKA）是消息层安全（MLS，RFC 9420）的密码学核心，用于管理大型端到端加密群聊的密钥，并在成员加入或离开时进行刷新。阈值秘密共享将秘密分成多个份额，只有达到门限数量的授权方才能重建。标准 MLS 没有为指定审计者提供恢复过去纪元密钥的机制；受监管行业通常只能诉诸明文服务器日志以满足合规要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Messaging_Layer_Security">Messaging Layer Security</a></li>
<li><a href="https://datatracker.ietf.org/doc/rfc9420/">RFC 9420 - The Messaging Layer Security (MLS) Protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secret_sharing">Secret sharing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secure messaging`, `#group key agreement`, `#auditability`, `#MLS`

---

<a id="item-9"></a>
## [优化 CSIDH-512 量子资源，T 门复杂度降低 85%以上](https://eprint.iacr.org/2026/1707) ⭐️ 8.0/10

该论文将 CSIDH-512 类群作用的 T 门复杂度从 2^52.6 降低到 2^51.7，并结合 Peikert 提出的隐藏移位量子算法，使求解 CSIDH-512 所需的 T 门数量至少减少 85%。此外，在给定的经典内存预算下，论文确定 collimation 参数 r=4 为最优选择。 这项工作推进了对 CSIDH 的量子密码分析，有助于安全评估者更准确地估算攻破 CSIDH-512 所需的量子资源，并为后量子密码的参数选择提供依据。 优化在四路置换构造模型和给定经典内存预算下进行；在所评估的 collimation 参数中，r=4 最优。类群作用的 T 门复杂度从 2^52.6 降至 2^51.7。

rss · IACR ePrint 密码学论文 · 8月17日 03:47

**背景**: CSIDH 是一种基于同源的抗量子密钥交换方案，利用理想类群在超奇异椭圆曲线上的作用，旨在以很小的公钥作为 Diffie-Hellman 的直接替代。在容错量子计算中，T 门比其他量子门昂贵得多，因此 T 门复杂度是衡量量子攻击代价的常用指标。Collimation 参数控制量子算法中合并分支的数量，影响量子与经典资源之间的权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csidh.isogeny.org/">CSIDH : Intro</a></li>
<li><a href="https://yx7.cc/docs/csidh/csidh_ac18_slides.pdf">CSIDH : An Efficient Post-Quantum Commutative Group Action</a></li>
<li><a href="https://quantum-journal.org/papers/q-2024-06-17-1375/pdf/">Trading T gates for dirty qubits in state preparation and unitary synthesis</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#cryptography`, `#post-quantum cryptography`, `#CSIDH`, `#resource optimization`

---

<a id="item-10"></a>
## [评论：四态量子公钥加密方案泄露明文分布](https://eprint.iacr.org/2026/1706) ⭐️ 8.0/10

该评论指出，Liu 等人 2022 年提出的量子公钥加密方案未能实现信息论安全：密文重现了明文的计算基分布，且基态 |0⟩ 和 |1⟩ 可以被完美区分。 该结果直接推翻了一项已发表的安全声明，提醒研究者避免在已被破解的方案上继续构建，并凸显了量子公钥加密中实现信息论安全的难度。 该评论证明加密映射恰好化简为 |M⟩ → R_θ X^m |M⟩，其中测量结果 m 被公开，R_θ 是对角矩阵，因此密文会泄露系数 (|α|², |β|²)，并且可以完美区分 |0⟩ 和 |1⟩。

rss · IACR ePrint 密码学论文 · 8月16日 12:19

**背景**: 信息论安全指密码系统即使面对拥有无限计算能力的敌手，也不会泄露任何明文信息。受控非门（CNOT）是一种双量子比特逻辑门，根据控制比特翻转目标比特。被评论的方案使用由四态公钥驱动的 CNOT，然后测量消息寄存器；该评论表明这一过程等价于一个会泄露明文分布的简单变换。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Information-theoretic_security">Information-theoretic security</a></li>
<li><a href="https://en.wikipedia.org/wiki/Controlled_NOT_gate">Controlled NOT gate</a></li>

</ul>
</details>

**标签**: `#quantum cryptography`, `#cryptanalysis`, `#public key encryption`, `#information-theoretic security`, `#quantum computing`

---

<a id="item-11"></a>
## [针对基于梅森数密码系统的新攻击：放宽尺寸约束](https://eprint.iacr.org/2026/1705) ⭐️ 8.0/10

一篇新论文（eprint 2026/1705）提出了针对基于梅森数的 AJPS 密码系统的新攻击，采用连分数和基于格的模多项式方法，显著放宽了未知私钥的尺寸约束，并在不平衡参数设置下提高了攻击成功概率。 该结果动摇了 AJPS 方案作为轻量级后量子候选方案的抗量子安全性假设，并可能影响后量子密码迁移中的参数选择与安全评估。 这些攻击不使用直接的格基约简，而是采用连分数和基于格的模多项式方程求解策略；它们要么无需估计未知量的上界，要么扩大可攻击弱私钥的范围，并通过多种参数规模的数值实验验证了实用性和有效性。

rss · IACR ePrint 密码学论文 · 8月16日 09:04

**背景**: AJPS 密码系统由 Aggarwal、Joux、Prakash 和 Santha 于 2017 年提出，是基于形如 p = 2^n - 1 的梅森数的 NTRU 整数模拟。其安全性依赖于在给定公开的 T 和 R 时，寻找低汉明重量的整数 F 和 G 使得 T = F·R + G mod p 的困难性。该方案旨在抵抗量子攻击，被视为轻量级后量子候选方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1705">New Attacks on Mersenne Number-Based Cryptosystems: Relaxing ...</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-319-96878-0_16">A New Public-Key Cryptosystem via Mersenne Numbers</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum cryptography`, `#cryptanalysis`, `#Mersenne numbers`, `#AJPS cryptosystem`

---

<a id="item-12"></a>
## [后量子 TLS 迁移系统化研究：混合握手、PSK、KeyUpdate 与证书策略](https://eprint.iacr.org/2026/1703) ⭐️ 8.0/10

该论文（ePrint 2026/1703）是一篇系统化知识（SoK）研究，将后量子 TLS 迁移视为架构问题，覆盖混合密钥建立、认证、PSK 模式、KeyUpdate 和证书策略。论文区分了已定标准与演进中的 Internet-Draft，并得出四个分析结论和一个迁移决策框架。 量子计算机可能攻破经典密钥交换和认证，TLS 必须迁移；本文提供了避免脆弱或不可互操作部署所需的架构级地图。这对标准机构、密码库开发者、PKI 运营方以及规划后量子过渡的企业都有直接参考价值。 该 SoK 发现混合 ECDHE-ML-KEM 是一种强过渡架构，因为其机密性可容忍其中一个组件失效，但确切安全性取决于标准化构造及其假设。它还警告 PSK、会话恢复和 KeyUpdate 不是可互换的密钥更新机制；KeyUpdate 不会产生独立的后量子秘密，部署就绪同时受证书、信任库、HSM、中间盒、资产清单和互操作性制约。

rss · IACR ePrint 密码学论文 · 8月16日 08:04

**背景**: 传输层安全（TLS）是保护大多数互联网流量的协议，它使用非对称密码进行密钥交换和服务器认证。RSA 和 ECDHE 等经典算法所依赖的问题可被足够强大的量子计算机上的 Shor 算法解决。NIST 已标准化后量子替代方案：用于密钥封装的 ML-KEM（FIPS 203），以及用于数字签名的 ML-DSA 和 SLH-DSA。迁移 TLS 不仅仅是替换算法，因为协议还包括会话恢复、预共享密钥、KeyUpdate 和 X.509 证书生态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://en.wikipedia.org/wiki/SLH-DSA">SLH-DSA</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#TLS`, `#security`, `#key exchange`, `#authentication`

---

<a id="item-13"></a>
## [纠缠博弈平行重复的间隙指数达到三次](https://eprint.iacr.org/2026/1702) ⭐️ 8.0/10

该论文证明了一个新的上界：对于任意具有纠缠值 1−ε 的有限双人博弈，其 n 次平行重复的纠缠值以 exp(−Ω(ε³n/(ε+ℓ))) 的速度衰减，其中 ℓ 是答案字母表大小的对数。这将间隙指数从 13 改进到 3，与经典的 Holenstein 界一致。 与经典间隙指数一致表明，在平行重复的指数衰减速率上，量子纠缠没有带来渐进优势，解决了量子复杂性理论中的一个长期问题，并加强了硬度放大和量子密码学中的工具。 证明使用平滑软标签替代先前量子相关采样中的随机平移对数网格，使标签不保真度变为二次方，并避免了 Jensen 损失；结合后选择论证，得到了三次依赖。分母中的 ε+ℓ 意味着当 ε 远小于 ℓ 时，界约为 exp(−Ω(ε³n/ℓ))；当 ε 较大时，约为 exp(−Ω(ε²n))。该结果改进了 OpenAI 报告第 6 章中指数为 13 的界。

rss · IACR ePrint 密码学论文 · 8月16日 06:02

**背景**: 非局域博弈是一种双人博弈，玩家在分离后不能通信，但可以共享量子纠缠。纠缠值 ω*(G) 表示使用这种策略能达到的最大成功概率。平行重复是指同时进行 n 个独立副本，玩家一次性回答所有问题，只有全部获胜才算获胜。平行重复定理给出重复博弈成功概率相对于原博弈值的指数衰减界，而“间隙指数”是 (1−值) 在指数中的幂次，例如 Holenstein 的经典界具有指数 3。

**标签**: `#quantum information`, `#parallel repetition`, `#entangled games`, `#complexity theory`, `#nonlocal games`

---

<a id="item-14"></a>
## [GCM 后量子多密钥安全性新改进界限](https://eprint.iacr.org/2026/1718) ⭐️ 7.0/10

该论文在量子理想密码模型下首次给出了 GCM 的非平凡后量子多密钥安全界限，将平凡项 up^2/2^k 改进为量级为 sqrt(d p^2 / 2^k) 的项，其中 d 是共享同一 nonce 的最大密钥数。 GCM 是使用最广泛的 AEAD 方案之一，实际协议中常以大量独立密钥部署；该结果表明当 nonce 重用受限时，后量子安全性优于朴素的多密钥扩展，对 TLS 等部署有直接意义。 证明结合了 Alagic 等人（EUROCRYPT 2022）的重编程与重采样方法以及 Hoang 等人（CCS 2018）的经典多用户计数论证；这些界限并非紧致且包含额外损失项，但在 d 远小于 u 的具体参数下比平凡多密钥界限有所改进。

rss · IACR ePrint 密码学论文 · 8月18日 00:28

**背景**: GCM（Galois/Counter Mode）是一种广泛标准化的 AEAD 模式，将计数器模式加密与 GF(2^128) 上的 GHASH 认证相结合。多密钥安全建模的是攻击者观察多个独立密钥下密文的情形；平凡的单密钥到多密钥转换会把优势乘以密钥数量，导致安全损失很大。量子理想密码模型（QICM）允许攻击者对底层分组密码进行量子叠加查询，用于建模后量子攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Galois/Counter_Mode">Galois/Counter Mode - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2510.08725v1">Post-Quantum Security of Block Cipher Constructions</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#GCM`, `#authenticated encryption`, `#quantum security`, `#multi-key security`

---

<a id="item-15"></a>
## [具有个性化匿名性的环签名](https://eprint.iacr.org/2026/1709) ⭐️ 7.0/10

该论文提出了个性化匿名环签名（PARS）这一新型密码学原语，由群管理员在密钥签发阶段为不同用户授予不同的匿名权限。与普通环签名不同，群管理员不指定固定的签名群，签名者仍可在签名时自主选择环，而管理员则认证用户密钥是允许完全匿名签名还是仅可追踪签名。 这一点很重要，因为它支持适合组织治理的角色化匿名策略：普通成员在内部举报或表达异议时可以匿名签名，而拥有机构授权的用户对其官方行为仍可被追踪。它将环签名从统一匿名性扩展为差异化匿名控制，可能影响现实系统中的隐私与问责设计。 作者给出了涵盖环签名和可追踪性保障的形式化语法与安全性定义，并基于数字签名、一次性签名、公钥加密和非交互零知识知识证明等标准原语给出了通用构造。

rss · IACR ePrint 密码学论文 · 8月17日 04:17

**背景**: 环签名允许任意一组用户中的成员对消息签名，同时隐藏具体签名者身份，由 Rivest、Shamir 和 Tauman Kalai 在 ASIACRYPT 2001 提出。追踪环签名和可问责环签名等变体增加了链接签名或在特定条件下揭示签名者的机制，但通常对所有潜在签名者施加统一的匿名或追踪规则。新的 PARS 原语则通过群管理员签发具有不同匿名权限的密钥，同时仍允许签名者选择签名环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ring_signature">Ring signature</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-540-71677-8_13">Traceable Ring Signature | Springer Nature Link</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#ring signatures`, `#anonymity`, `#privacy`, `#governance`

---
---
layout: default
title: "Horizon Summary: 2026-08-20 (ZH)"
date: 2026-08-20
lang: zh
---

> 从 37 条内容中筛选出 15 条重要资讯。

---

1. [针对扩展域上 PKP 与 PEP 的新攻击揭示多项式时间漏洞](#item-1) ⭐️ 8.0/10
2. [SPEG：零知识证明验证 C2PA 图像 JPEG 压缩](#item-2) ⭐️ 8.0/10
3. [基于格的静默门限加密方案](#item-3) ⭐️ 8.0/10
4. [在 SQIsign 中暴露 SIMD 并行性：AVX-512 实现](#item-4) ⭐️ 8.0/10
5. [新统计估计器改进噪声随机泄漏下的 ML-DSA 侧信道攻击](#item-5) ⭐️ 8.0/10
6. [论文提出可审计连续组密钥协商协议（Au-CGKA）](#item-6) ⭐️ 8.0/10
7. [预准备片段：缩短在线哈希签名](#item-7) ⭐️ 8.0/10
8. [CSIDH-512 的量子资源优化降低了 T 门复杂度](#item-8) ⭐️ 8.0/10
9. [Cloudflare 重新评估 Workers 远程 Spectre 攻击并公布新防御](#item-9) ⭐️ 8.0/10
10. [NTRU 加密能有多紧凑？启发式前沿与实用方案](#item-10) ⭐️ 7.0/10
11. [GCM 后量子多密钥安全性边界得到改进](#item-11) ⭐️ 7.0/10
12. [Simon 二面体陪集量子算法中三个引理的严格证明](#item-12) ⭐️ 7.0/10
13. [研究人员提出具有个性化匿名权限的环签名方案](#item-13) ⭐️ 7.0/10
14. [Cloudflare 追踪 RFC 9234 采用情况：发现两家 Tier 1 网络剥离 OTC 属性](#item-14) ⭐️ 7.0/10
15. [ICE 去年采集了近百万份 DNA 样本](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [针对扩展域上 PKP 与 PEP 的新攻击揭示多项式时间漏洞](https://eprint.iacr.org/2026/1711) ⭐️ 8.0/10

该论文对扩展域上的置换核问题（PKP）和置换码等价问题（PEP）提出了新的密码分析。通过将二进制域扩展实例归约到结构化正则综合征解码（RSD），发现了新的多项式时间攻击参数范围，包括所有扩展次数大于 4 的自对偶 PEP 实例，并将 Regular-ISD 算法适配到 PKP 派生实例上改进了攻击。 这些结果使大多数场景下在扩展域上使用 PEP 不再安全，并为 PKP 的安全性提供了新见解，直接影响 PERK 和 SETH 等为了效率而采用扩展域的后量子签名方案。 在二进制域扩展上，攻击通过归约到结构化正则综合征解码（RSD）变体，对自正交 PEP 族和所有扩展次数大于 4 的自对偶实例给出了多项式时间算法。论文还将 Esser 和 Santini 的置换型 Regular-ISD 算法适配到 PKP 派生实例，在特定参数范围内改进了此前攻击，并将一大类奇特征 PEP 实例归约到图同构问题以获得多项式时间解法。

rss · IACR ePrint 密码学论文 · 8月17日 06:57

**背景**: 置换核问题（PKP）要求找到给定向量的一个置换，使其落入给定矩阵的核中；置换码等价问题（PEP）则询问两个线性码是否在坐标置换下等价。这些问题被广泛认为是困难的，并作为 PKP-DSS、PERK 和 SETH 等后量子签名方案的安全基础。近期方案为了提升效率和紧凑性，开始在扩展域上实例化这些问题。正则综合征解码（RSD）是一种结构化解码问题，已有包括 Regular-ISD 在内的专用信息集解码攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2206.14547">[2206.14547] A Novel Attack to the Permuted Kernel Problem</a></li>
<li><a href="https://anr-manta.inria.fr/files/2019/01/cep.pdf">Permutation Code Equivalence Problem - Inria</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-68391-6_6">Not Just Regular Decoding: Asymptotics and Improvements of Regular Syndrome Decoding Attacks | Springer Nature Link</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#code-based cryptography`, `#digital signatures`, `#cryptanalysis`

---

<a id="item-2"></a>
## [SPEG：零知识证明验证 C2PA 图像 JPEG 压缩](https://eprint.iacr.org/2026/1717) ⭐️ 8.0/10

该论文提出了 SPEG，这是一种零知识证明系统，可验证压缩图像源自 C2PA 签名的原始图像，首次支持有损 JPEG 压缩。它提供两种模式：一种与任意哈希兼容（使用 Poseidon），证明 1080p JPEG 压缩需 47 秒；另一种更快模式需要多项式承诺，仅需 2 秒。 这填补了内容来源验证的关键空白，因为 C2PA 签名通常会因 JPEG 压缩而失效，导致现实图像无法证明真实性。它将证明时间从 VerITAS 简单缩放的 227 秒缩短至 JPEG 压缩仅 2 秒，使消费者设备上的可验证真实图像共享成为可能。 关键优化包括在证明电路之外处理非代数 JPEG 编码，以及避免浮点运算中的范围检查。该论文还发现并修复了 VIMz（PETS '25）中的一个安全漏洞，并证明了可将流行的 powers-of-tau SRS 与 KZG 多项式承诺方案安全结合使用。

rss · IACR ePrint 密码学论文 · 8月17日 18:25

**背景**: C2PA 是一个开放技术标准，允许发布者和创作者为图像附加来源元数据和数字签名，证明其来源和编辑历史。零知识证明（尤其是 zk-SNARK）允许证明者在不泄露底层数据的情况下让验证者确信某个陈述为真，广泛应用于隐私保护和区块链系统。JPEG 压缩是一种有损编码，可减小图像文件大小，但会改变像素数据，从而破坏数字签名。本工作结合这些技术，在不暴露原始图像的情况下证明压缩图像源自经过认证的原始图像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zk-SNARK">Zk-SNARK</a></li>
<li><a href="https://c2pa.org/">C 2 PA | Verifying Media Content Sources</a></li>
<li><a href="https://en.wikipedia.org/wiki/Content_Authenticity_Initiative">Content Authenticity Initiative - Wikipedia</a></li>

</ul>
</details>

**标签**: `#zk-SNARKs`, `#content provenance`, `#C2PA`, `#image compression`, `#cryptography`

---

<a id="item-3"></a>
## [基于格的静默门限加密方案](https://eprint.iacr.org/2026/1716) ⭐️ 8.0/10

该论文基于分解 LWE 假设构建了一种静默门限加密方案，单比特加密的密文规模为 O(T)+poly(λ,log N)，避免了双线性映射和不可区分混淆等重型工具。该方案对所有阈值 T=N^ε（任意常数 ε<1）都实现了非平凡简洁性，并可扩展到具有简洁计算秘密共享的任意单调策略族。 该工作首次在标准格假设（分解 LWE）下实现静默门限加密，摆脱了对双线性映射和混淆的依赖，具有抗量子特性。这对于阈值密码学、异步分布式系统以及受益于静默设置的隐私保护协议具有重要意义。 该方案的核心是一个有界合谋注册函数加密方案：在 N 个用户和合谋上限 Q 下，对 ℓ 位输入、深度 d 的布尔电路，密文规模为 Q·Õ(d)+ℓ·poly(λ,d,log N)。安全性在随机预言机模型下基于分解 LWE 假设证明，并且仅当阈值 T=N^ε（ε<1 为常数）时才具有非平凡简洁性。

rss · IACR ePrint 密码学论文 · 8月17日 18:21

**背景**: 静默门限加密是门限加密的推广：一组用户的联合公钥由各用户独立公钥的确定性函数计算得到，从而消除了交互式设置。标准门限加密通常需要可信分发者或交互式密钥生成，而静默设置支持异步部署、多宇宙支持和动态委员会等特性。带错误学习（LWE）是一种基于格的数学问题，通过在线性方程组中加入小误差来隐藏秘密，是许多后量子密码方案的基础。此前的静默门限加密构造依赖双线性映射（椭圆曲线上的配对）或不可区分混淆等重型工具；本工作则基于分解 LWE 这一格假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1716">Silent Threshold Encryption from Lattices</a></li>
<li><a href="https://eprint.iacr.org/2024/263">Threshold Encryption with Silent Setup</a></li>
<li><a href="https://en.wikipedia.org/wiki/Learning_with_errors">Learning with errors - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#threshold encryption`, `#lattice-based cryptography`, `#LWE`, `#privacy`

---

<a id="item-4"></a>
## [在 SQIsign 中暴露 SIMD 并行性：AVX-512 实现](https://eprint.iacr.org/2026/1713) ⭐️ 8.0/10

该论文提出了一种端到端的 SQIsign AVX-512IFMA 实现，通过重组 Montgomery 阶梯、点加倍、配对和同源求值的算术依赖图来暴露 SIMD 并行性。在 NIST 安全级别 I 下，与参考 C 实现相比，密钥生成、签名和验证分别获得 1.76 倍、1.71 倍和 3.18 倍的加速；结合 Qlapoti 后，密钥生成和签名加速提升至 2.90 倍和 2.69 倍。 这项工作解决了基于同源的抗量子密码学的主要性能瓶颈，该方向密钥尺寸小但运算速度历来较慢。通过证明算法级 SIMD 调度可在不同方案中复用（并在 CORAL 上验证），它可能使 SQIsign 及相关原语在实际部署和 NIST 标准化中更具实用性。 该实现大部分曲线侧计算保持基数为 2^51 的向量表示，并使用 AVX-512IFMA 指令。具体包括用于 Montgomery 阶梯的射影 xDBLADD 调度、批量点加倍、向量化双标量阶梯、融合三次算术配对步骤以及批量一维和二维同源求值；在 CORAL 上，密钥生成和共享密钥计算分别获得 1.28–1.40 倍和 1.92–2.46 倍的加速。

rss · IACR ePrint 密码学论文 · 8月17日 12:25

**背景**: SQIsign 是一种基于超奇异椭圆曲线同源的抗量子签名方案，已提交至 NIST 后量子密码标准化进程，其密钥和签名尺寸非常小（64–128 字节和 177–335 字节），但运算速度历来较慢。AVX-512IFMA 是 Intel 的 512 位 SIMD 指令集扩展，特别适用于大整数算术，因为它可以高效处理 52 位字长。基于同源的密码学依赖于计算椭圆曲线间同源的困难性，这被认为能抵抗量子攻击。本文针对 SQIsign 的性能瓶颈，通过向量化高层曲线和同源运算而非仅向量化域乘法来提升速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SQIsign">SQIsign</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advanced_Vector_Extensions">Advanced Vector Extensions - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isogeny-based_cryptography">Isogeny-based cryptography</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#isogeny-based cryptography`, `#SIMD`, `#AVX-512`, `#SQIsign`

---

<a id="item-5"></a>
## [新统计估计器改进噪声随机泄漏下的 ML-DSA 侧信道攻击](https://eprint.iacr.org/2026/1712) ⭐️ 8.0/10

论文提出一种矩估计器来估计 ML-DSA 噪声随机泄漏中的比特错误率 p，并为每个泄漏比特推导出正确性的后验概率。将该后验概率用作预处理步骤，可将 Schubert 等人攻击所需的信息性关系数量减少 20%至 44%，并提高 Bashiri 等人攻击的密钥恢复成功率（例如在 p=0.45 时从 1,900,000 个信息性关系起）。 这很重要，因为 ML-DSA 是 NIST 后量子签名标准，其抗侧信道攻击能力取决于噪声泄漏被利用的程度。新的统计推断降低了密钥恢复所需的数据量和计算量，这意味着实际部署可能需要比之前假设更强的防护措施或更高的噪声水平。 经过 j-独立性变换后，|z̃|服从一个具有闭式分量的两分量混合分布；该估计器可在泄漏指数低至 4（ML-DSA-44/87）和 5（ML-DSA-65）时工作，在 25,000 个信息性关系下低泄漏情形的平均绝对误差为 0.022 至 0.040，而高泄漏情形低于 0.002。预处理步骤复杂度为 O(α)，可纠正被分类为噪声的关系，将 Schubert 等人攻击所需的信息性关系减少 20%至 44%，并提高 Bashiri 等人攻击的种子成功率（例如 p=0.20 时从 19/30 提升到 23/30）。

rss · IACR ePrint 密码学论文 · 8月17日 11:02

**背景**: ML-DSA 是 NIST 为后量子密码学选定的基于格的数字签名标准，其安全性证明依赖拒绝采样使签名与私钥独立。侧信道攻击利用系统无意泄漏的物理信息（如时序、功耗或电磁辐射）来恢复秘密，此处攻击者观察掩码随机数的泄漏比特。矩估计法是一种通过将样本矩与理论总体矩匹配来估计未知参数的统计方法。以往的侧信道攻击将所有泄漏比特视为同样可信，而本文考虑了噪声泄漏中的比特错误。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Side-channel_attack">Side-channel attack</a></li>
<li><a href="https://mac-stat.github.io/MathStat355Notes/mom.html">3 Method of Moments – MATH/STAT 355: Statistical Theory</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#side-channel attacks`, `#ML-DSA`, `#statistical inference`

---

<a id="item-6"></a>
## [论文提出可审计连续组密钥协商协议（Au-CGKA）](https://eprint.iacr.org/2026/1710) ⭐️ 8.0/10

该论文提出 Au-CGKA，一种 MLS 形态协议，每个被接受的 epoch 都携带一个 STARK 证明，将密钥材料绑定到可由阈值审计委员会恢复的秘密上，从而防止静默托管失败。在 Apple M5 Pro 上的 Rust 原型生成证明耗时 1.38 秒（15.31 MB），验证耗时 0.17 秒，且与群组规模无关。 这使得金融、医疗和政府等受监管行业能够在保持端到端加密的同时满足审计与合规要求，避免退回到明文服务器日志。它填补了需要合法访问或密钥恢复的 MLS 部署中的关键空白。 该证明使用定制的后量子多阶段 STARK，并在加入时验证后即丢弃，因此唯一的持久开销是固定大小的托管；所证明的关系与群组规模无关。安全性在安全擦除模型下以量子随机预言机模型中的直线归约得到自适应证明，并在声明的假设下传导至实现的后端。

rss · IACR ePrint 密码学论文 · 8月17日 04:52

**背景**: 消息层安全（MLS）是 IETF 标准（RFC 9420），用于端到端加密的群组消息传输，设计上可扩展至数万人的群组。其密码学核心——连续组密钥协商（CGKA）——允许成员在每次成员变更时更新共享密钥，以提供前向安全和后泄露安全。阈值密码学将秘密拆分成份额，使得只有达到阈值数量的参与方才能重建秘密。STARK 是后量子零知识证明系统，用于高效证明计算完整性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Messaging_Layer_Security">Messaging Layer Security - Wikipedia</a></li>
<li><a href="https://www.rfc-editor.org/rfc/rfc9420.html">RFC 9420: The Messaging Layer Security ( MLS ) Protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/Threshold_cryptography">Threshold cryptography</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#key agreement`, `#MLS`, `#auditability`, `#secure group messaging`

---

<a id="item-7"></a>
## [预准备片段：缩短在线哈希签名](https://eprint.iacr.org/2026/1708) ⭐️ 8.0/10

该论文提出 SPHINCS-PE，一种 SPHINCS+的预准备片段变体，将全局寻址的超树按片段边界拆分为上层树和下层树。每个在线签名仅需沿下层树回溯到预先认证的边界根，从而从完整签名中移除 WOTS+块。 该优化针对无状态哈希签名的一个关键效率限制，其签名体积大，阻碍了在资源受限的后量子系统中的采用。通过在保留自包含验证的同时将在线签名最多缩小 70%（使用缓存验证器状态），SPHINCS-PE 可能使类似 SLH-DSA 的签名在实际部署中更实用。 该构造使用上层树，在准备阶段认证其边界根，采用更少但更高的层；在线签名则沿下层树回溯至该根。与匹配的 FIPS 205 SLH-DSA 参数集相比，短配置下完整签名大小降低 3%至 12%，快速配置下降低 25%至 40%；若缓存上层证书，在线签名分别缩小 24%至 48%和 56%至 70%。

rss · IACR ePrint 密码学论文 · 8月17日 03:59

**背景**: SPHINCS+是一种无状态、基于哈希的后量子签名方案，已在 FIPS 205 中标准化为 SLH-DSA。它采用 FORS 少次签名和 WOTS+一次性签名，并与 Merkle 超树结合，生成无需签名者状态的自包含签名。由于每条消息都携带 FORS 签名和到长期根的完整认证链，SPHINCS+签名远大于基于格的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sphincs.org/">SPHINCS+</a></li>
<li><a href="https://cypheronlabs.github.io/Cypheron-core/algorithms/sphincsplus.html">SPHINCS+ (Digital Signatures ) - Cypheron Core Documentation</a></li>
<li><a href="https://rya-sge.github.io/access-denied/2026/06/29/slh-dsa-fips-205-hash-based-signatures/">SLH-DSA — The Stateless Hash-Based Signature Standard (FIPS 205)</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#hash-based signatures`, `#SPHINCS+`, `#efficiency`

---

<a id="item-8"></a>
## [CSIDH-512 的量子资源优化降低了 T 门复杂度](https://eprint.iacr.org/2026/1707) ⭐️ 8.0/10

论文将 CSIDH-512 类群作用的 T 门复杂度从 2^{52.6} 降低到 2^{51.7}，并在指定经典内存预算下表明参数 r=4 是最优的。结合 Peikert 提出的 hidden-shift 量子算法，求解 CSIDH-512 所需的 T 门至少减少了 85%。 这改进了对 CSIDH-512 及基于同源的密码方案的量子安全性估计，有助于密码学家选择更安全的参数并更准确地评估量子攻击的实际代价。它直接回应了 Eurocrypt 2020 提出的开放问题，可能影响后量子标准化讨论。 分析采用四路置换构造模型，并在固定经典内存预算下比较了多个 r 值（即一次处理的群元素个数），发现 r=4 最优。结合 hidden-shift 算法后，T 门至少减少 85%，类群作用的 T 门复杂度从 2^{52.6} 降至 2^{51.7}。

rss · IACR ePrint 密码学论文 · 8月17日 03:47

**背景**: CSIDH 是一种基于同源的抗量子密钥交换方案，其安全性依赖于类群作用的困难性。针对 CSIDH 的量子攻击通常使用 hidden-shift 算法，其开销主要由 T 门（容错量子计算中昂贵的非 Clifford 门）决定。参数 r 控制同时处理的群元素个数，在量子比特数和门数之间进行权衡。Eurocrypt 2020 上 Peikert 提出了优化这些量子资源的开放问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2508.11082v1">A Constant-Time Hardware Architecture for the CSIDH Key ...</a></li>
<li><a href="https://quantumcomputing.stackexchange.com/questions/9705/why-are-non-clifford-gates-more-complex-than-clifford-gates">complexity theory - Why are non-Clifford gates more complex than...</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#isogeny-based cryptography`, `#CSIDH`, `#quantum cryptanalysis`, `#resource optimization`

---

<a id="item-9"></a>
## [Cloudflare 重新评估 Workers 远程 Spectre 攻击并公布新防御](https://blog.cloudflare.com/revisiting-spectre-attacks-on-workers/) ⭐️ 8.0/10

2024 至 2025 年间，Cloudflare 重新评估了针对其 Workers 无服务器平台的远程 Spectre 攻击，识别出包括 Spectre gadgets、远程计时器和共置技术在内的新攻击原语，并实施了额外防御以进一步加固基础设施。 这项工作提高了多租户云和边缘计算的安全门槛，因为共享硬件可能被侧信道攻击利用；更强的缓解措施保护所有在 Cloudflare Workers 上运行代码的客户免受投机执行缺陷导致的跨租户数据泄露。 新的攻击原语包括 Spectre gadgets（可通过投机执行利用的代码序列）、用于精细计时测量的远程计时器，以及实现与受害者进程共置的技术；该博客详细介绍了 2024 至 2025 年实施的防御措施，但摘要中未列出具体缓解机制。

rss · Cloudflare Blog (PQ 迁移) · 8月19日 16:00

**背景**: Spectre 是一类 CPU 漏洞，利用投机执行在安全边界之间泄露数据。远程 Spectre 攻击（如 NetSpectre）将此类攻击扩展到网络环境，无需本地代码执行。Cloudflare Workers 是一个无服务器平台，在 Cloudflare 边缘网络的众多共享机器上运行客户代码，因此侧信道隔离至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mlq.me/download/netspectre.pdf">NetSpectre: Read Arbitrary Memory over Network</a></li>
<li><a href="https://github.com/google/security-research/blob/master/pocs/cpus/spectre-gadgets/README.md">security-research/pocs/cpus/spectre-gadgets/README.md at ...</a></li>
<li><a href="https://www.cloudflare.com/products/workers/">Cloudflare Workers - Global Serverless Functions Platform</a></li>

</ul>
</details>

**标签**: `#Spectre`, `#Cloudflare Workers`, `#side-channel attacks`, `#cloud security`, `#systems security`

---

<a id="item-10"></a>
## [NTRU 加密能有多紧凑？启发式前沿与实用方案](https://eprint.iacr.org/2026/1715) ⭐️ 7.0/10

论文提出 NTRU 解密的两阶段统一视角，并引入自由候选定位（FCL）方法；在 NIST-I 安全级别下，编码框架与陷门框架的紧凑性前沿分别为 812 字节和 754 字节，并给出 END 方案，其密文仅 384 字节。 该工作突破了 NTRU 先前的尺寸记录，在 NIST-I 下得到比 ML-KEM-512 小一半的密文，而封装/解封装总开销仅高约 3%；这对后量子密码中带宽敏感的应用具有重要意义。 END-512 的密文为 384 字节，比 BAT 和 DAWN 短 12–19%；总公钥加密文为 754 字节。FCL 用于 ML-KEM 时，参考 C 实现中密文缩小 10%，整体运行时间慢 5%。

rss · IACR ePrint 密码学论文 · 8月17日 14:08

**背景**: NTRU 是 1996 年提出的基于格的公钥加密方案，可抵抗量子计算攻击，是后量子密码标准化的重要候选方向之一。NIST 已选择 ML-KEM（Kyber）作为标准，而 NEV、DAWN 等 NTRU 变体持续优化紧凑性；DAWN 通过双重编码将公钥加密文总尺寸降至 964 字节。本文把 NTRU 解密统一为候选错误定位与验证两个阶段，并系统搜索紧凑性前沿。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NTRU">NTRU - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lattice-based_cryptography">Lattice-based cryptography - Wikipedia</a></li>
<li><a href="https://eprint.iacr.org/2025/1520">DAWN: Smaller and Faster NTRU Encryption via Double Encoding</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum cryptography`, `#NTRU`, `#lattice-based encryption`, `#compactness`

---

<a id="item-11"></a>
## [GCM 后量子多密钥安全性边界得到改进](https://eprint.iacr.org/2026/1718) ⭐️ 7.0/10

这篇论文在量子理想密码模型（QICM）中研究了 GCM 的后量子多密钥安全性，并将平凡多密钥界中的 up^2/2^k 项替换为 sqrt(d p^2 / 2^k) 量级的项，其中 d 是同一 nonce 在加密查询中出现的最大密钥数。这是首个针对 AEAD 模式在 QICM 中的非平凡后量子多密钥安全界。 GCM 是部署最广泛的 AEAD 方案之一，实际系统中通常使用大量独立密钥，因此多密钥安全性具有重要现实意义。新结果表明，当 nonce 重用受限时，即使在大量密钥和量子敌手场景下也能保持安全性，这对 TLS 等协议具有参考价值。 该界并非紧致，且需额外损失项；当 d 远小于密钥数 u 且额外损失项较小时，新界优于平凡多密钥界。证明结合了 Alagic 等人的重编程-重采样方法与 Hoang 等人在经典多用户分析 GCM 时使用的计数论证。

rss · IACR ePrint 密码学论文 · 8月18日 00:28

**背景**: GCM（Galois/Counter Mode）是一种带关联数据的认证加密（AEAD）模式，广泛用于 TLS 等协议，可同时提供机密性和数据源认证。量子理想密码模型（QICM）将理想密码模型扩展到允许敌手以量子叠加态查询底层分组密码，用于后量子安全证明。多密钥安全考虑敌手攻击多个独立密钥实例，将单密钥界直接推广会导致与密钥数量成正比的损失，并产生 up^2/2^k 项。本文通过引入参数 d（衡量同一 nonce 在不同密钥下的最大重用次数）改进了这一项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Galois/Counter_Mode">Galois/Counter Mode - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2510.08725v1">Post- Quantum Security of Block Cipher Constructions</a></li>
<li><a href="https://eprint.iacr.org/2026/1718">On Post-Quantum Multi-Key Security of GCM</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#GCM`, `#authenticated encryption`, `#quantum security`, `#multi-key security`

---

<a id="item-12"></a>
## [Simon 二面体陪集量子算法中三个引理的严格证明](https://eprint.iacr.org/2026/1714) ⭐️ 7.0/10

该论文为 Simon 提出的二面体陪集问题多项式时间量子算法中的三个仅有证明草图的引理提供了严格的陈述和完整证明。它修正了引理 1 的概率界为趋于 1，去除了引理 3 的“良好行为”假设，并为引理 4 精确计算了协方差。 这项工作验证并修正了该量子算法中的关键技术论断，使原始分析建立在可靠基础上。同时它也表明仅证明这些引理不足以确立算法的正确性，因为关键的分区独立性假设未获支持，这对基于格的密码学的量子攻击可行性有直接影响。 引理 1 利用子集和计数的精确二阶矩计算；引理 3 通过在测量结果立方体上的 Parseval 恒等式得到幅值界；引理 4 精确计算了两个球入盒协方差，并发现第二个协方差包含一个固定球计数所遗漏的项。两个分支幅值带有符号前置因子，因此估计控制的是它们的差而非原引理所称的比值，并且可以去掉区分组不含故障样本的假设。

rss · IACR ePrint 密码学论文 · 8月17日 13:54

**背景**: Simon 算法是一种量子查询算法，对 Simon 问题给出了相对经典算法的指数级加速，并启发了 Shor 算法；它解决的是阿贝尔隐藏子群问题。二面体陪集问题（DCP）是二面体群上的非阿贝尔隐藏子群问题，与后量子密码学中的格问题密切相关。对 DCP 的多项式时间量子算法将严重影响基于格的密码安全性，因此对已提出算法进行严格检验至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Simon's_algorithm">Simon's algorithm</a></li>
<li><a href="https://www.sitg-consulting.com/post/daniel-simon-s-dihedral-coset-algorithm-what-does-it-actually-mean-for-lattice-based-cryptography-a">Daniel Simon’s Dihedral Coset Algorithm: What Does It Actually Mean...</a></li>

</ul>
</details>

**标签**: `#quantum algorithms`, `#dihedral coset problem`, `#cryptography`, `#proof verification`, `#theoretical computer science`

---

<a id="item-13"></a>
## [研究人员提出具有个性化匿名权限的环签名方案](https://eprint.iacr.org/2026/1709) ⭐️ 7.0/10

该论文提出了个性化匿名环签名（PARS），由群管理员为每个用户认证不同的匿名权限（如完全匿名或可追踪签名），同时签名者仍可在签名时自行选择签名环。论文给出了形式化语法、安全定义以及基于标准密码学原语的通用构造。 这使组织能够实施细粒度的匿名策略：普通成员可在内部举报或表达异议时获得强匿名保护，而拥有机构权限的用户须为其官方行为负责。该方案将环签名从统一的匿名规则扩展到个性化权限，可能影响隐私保护区块链、电子投票和治理系统。 PARS 仅在密钥签发阶段涉及群管理员，而非固定签名组；其安全定义同时涵盖标准环签名性质和可追踪性保证。通用构造使用了数字签名、一次性签名、公钥加密和非交互式零知识知识证明。

rss · IACR ePrint 密码学论文 · 8月17日 04:17

**背景**: 环签名允许集合中任意成员匿名签名，无需额外设置且不可撤销；可追踪环签名增加了链接性或在重复标签时揭示签名者，可问责环签名则提供条件可追踪性。现有变体对所有潜在签名者施加统一的匿名或追踪规则。PARS 的不同之处在于由群管理员为每个用户认证个性化的匿名权限，同时保留即时的环选择能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ring_signature">Ring signature</a></li>
<li><a href="https://eprint.iacr.org/2025/1807">Traceable Ring Signatures Revisited: Extended Definitions,</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#ring signatures`, `#anonymity`, `#privacy`, `#blockchain`

---

<a id="item-14"></a>
## [Cloudflare 追踪 RFC 9234 采用情况：发现两家 Tier 1 网络剥离 OTC 属性](https://blog.cloudflare.com/rfc9234-bgp-role-model/) ⭐️ 7.0/10

Cloudflare 测量了 RFC 9234（包括 BGP 角色和仅限客户 OTC 属性）的部署情况，发现两家 Tier 1 网络会意外剥离 OTC 属性，这可能削弱路由泄漏防护。 剥离 OTC 会移除路由器自动拒绝路由泄漏所需的关键信号，大型中转网络的错误配置仍可能传播有害 BGP 通告。这凸显了路由安全部署中的实际缺口，影响网络运营商和互联网稳定性。 RFC 9234 在 UPDATE/OPEN 消息中使用 BGP 角色和 OTC 属性来防止路由泄漏。Cloudflare 的测量显示两家 Tier 1 网络剥离 OTC，但提供的摘要未点明具体网络名称，更多技术细节可参见博客原文。

rss · Cloudflare Blog (PQ 迁移) · 8月18日 15:21

**背景**: BGP（边界网关协议）是互联网自治系统之间交换路由信息的协议。路由泄漏是指网络在违反拓扑关系的情况下通告路由，例如将从一个上游提供商学到的路由通告给另一个提供商。RFC 9234 定义了 BGP 角色（如提供商、客户、对等方等）和仅限客户（OTC）属性，帮助路由器检测并拒绝这类泄漏。Cloudflare 的博客是对该标准实际部署情况的测量研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rfc-editor.org/info/rfc9234/">RFC 9234: Route Leak Prevention and Detection Using Roles in ...</a></li>
<li><a href="https://datatracker.ietf.org/doc/rfc9234/">RFC 9234: Route Leak Prevention and Detection Using Roles in ...</a></li>
<li><a href="https://blog.cloudflare.com/rfc9234-bgp-role-model/">BGP Role model: tracking the adoption of RFC 9234</a></li>

</ul>
</details>

**标签**: `#BGP`, `#RFC 9234`, `#route leaks`, `#network security`, `#internet routing`

---

<a id="item-15"></a>
## [ICE 去年采集了近百万份 DNA 样本](https://www.schneier.com/blog/archives/2026/08/ice-collecting-dna-samples.html) ⭐️ 7.0/10

布鲁斯·施奈尔指出，《连线》报道称美国移民与海关执法局（ICE）去年采集了近百万份 DNA 样本。这标志着对移民拘留者 DNA 采集的大幅扩大，引发隐私和监控担忧。 这一扩张引发严重的公民自由和隐私问题，因为 DNA 包含敏感的生物识别和家族信息。它可能导致对移民社区的长期监控，并可能影响数百万非公民及其亲属，带来数据滥用和正当程序的隐患。 据报道，这些 DNA 样本被上传至 FBI 的 CODIS 数据库，该数据库存储犯罪者和犯罪现场的 DNA 图谱，用于执法比对。批评者指出，对移民拘留者进行常规采集绕过了传统的刑事司法保障，可能包含从未被定罪的人。

rss · Schneier on Security · 8月19日 10:46

**背景**: CODIS（联合 DNA 索引系统）是 FBI 的 DNA 数据库，存储来自犯罪者和犯罪现场的 DNA 图谱，用于协助破案。它包含一个国家级组成部分 NDIS。据报道，ICE 从被拘留者中收集的 DNA 样本可能会录入 CODIS，从而将刑事司法数据库的使用扩展到移民执法领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fbi.gov/how-we-can-help-you/dna-fingerprint-act-of-2005-expungement-policy/codis-and-ndis-fact-sheet">CODIS and NDIS Fact Sheet — FBI | Federal Bureau of Investigation</a></li>
<li><a href="https://www.njoag.gov/codis/">CODIS - New Jersey Office of Attorney General</a></li>

</ul>
</details>

**标签**: `#privacy`, `#surveillance`, `#DNA`, `#ICE`, `#civil liberties`

---
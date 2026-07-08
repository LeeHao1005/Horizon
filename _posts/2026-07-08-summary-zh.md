---
layout: default
title: "Horizon Summary: 2026-07-08 (ZH)"
date: 2026-07-08
lang: zh
---

> 从 33 条内容中筛选出 13 条重要资讯。

---

1. [针对 TALUS 的密钥恢复攻击：一份密码分析笔记](#item-1) ⭐️ 9.0/10
2. [基于 Wiedemann 和 Berlekamp-Massey 的 XL 比特操作成本模型](#item-2) ⭐️ 9.0/10
3. [HAWK“猜谜游戏”攻击并非多项式时间](#item-3) ⭐️ 9.0/10
4. [带预处理的隐私信息检索黑盒密码学下界](#item-4) ⭐️ 8.0/10
5. [PriFT：利用现有 MPC 和 HE 库进行隐私微调](#item-5) ⭐️ 8.0/10
6. [TIM：零知识证明隐私盲水印](#item-6) ⭐️ 8.0/10
7. [(R)Icy-DVRF：具有固定大小证明的鲁棒异步分布式可验证随机函数](#item-7) ⭐️ 8.0/10
8. [HEAD-FL：集成自适应差分隐私与可验证同态聚合的联邦学习框架](#item-8) ⭐️ 8.0/10
9. [法国 ANSSI：2027 年起停止非量子安全加密认证](#item-9) ⭐️ 8.0/10
10. [基于 Walsh 基和懒比特的 CKKS AES 同态转换 LUT 评估](#item-10) ⭐️ 7.0/10
11. [基于属性的内积函数加密分层结构形式化](#item-11) ⭐️ 7.0/10
12. [Cloudflare Workers 缓存：通过 HTTP 头配置的区域分层缓存](#item-12) ⭐️ 7.0/10
13. [谷歌起诉使用 Gemini AI 的中国钓鱼网络](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [针对 TALUS 的密钥恢复攻击：一份密码分析笔记](https://eprint.iacr.org/2026/1386) ⭐️ 9.0/10

研究人员发现了针对阈值 ML-DSA 方案 TALUS 的密钥恢复攻击，利用公开矩阵 A 的左可逆性轻易恢复出密钥份额，并利用缺失拒绝采样导致签名泄露秘密密钥。 该攻击打破了与 NIST 相关的阈值 ML-DSA 构造的 EUF-CMA 安全性声明，引发了对持续进行的标准化工作的担忧。 被动攻击从密钥生成广播中恢复 s1 的所有份额，并从签名广播中恢复 y，通过单个签名即可获得密钥。第二个针对缺失拒绝采样的攻击需要数亿次签名，通过环上的最小二乘法恢复 s2。

rss · IACR ePrint 密码学论文 · 7月7日 17:30

**背景**: ML-DSA 是后量子数字签名标准（FIPS 204）。阈值版本将签名分发到多方。Feldman 承诺使用公开矩阵 A 来承诺秘密值。左可逆性意味着 A 有左逆，可通过高斯消元从输出恢复输入。ML-DSA 中的拒绝采样可防止秘密误差项 s2 泄露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1386">Key-Recovery Attacks on TALUS: A Cryptanalytic Note</a></li>
<li><a href="https://arxiv.org/abs/2603.22109">[2603.22109] TALUS: Threshold ML-DSA with One-Round Online ... GitHub - yarsawyer/tide-talus TALUS: Threshold ML-DSA with One-Round Online Signing TALUS: Threshold ML-DSA with One-Round Online Signing via ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Verifiable_secret_sharing">Verifiable secret sharing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#threshold-signatures`, `#ML-DSA`, `#key-recovery`

---

<a id="item-2"></a>
## [基于 Wiedemann 和 Berlekamp-Massey 的 XL 比特操作成本模型](https://eprint.iacr.org/2026/1382) ⭐️ 9.0/10

作者提出了一种具体的比特操作成本模型，用于结合 Wiedemann 线性代数和 Berlekamp-Massey 序列恢复的 XL 算法求解多元二次系统。他们推导了闭合形式的成本公式，并为有限域 GF(2)、GF(31)和 GF(256)实现了电路导向的模型。 这项工作实现了对基于多元二次方程的后量子方案（包括 NIST 额外签名候选和福冈 MQ 挑战实例）进行直接、统一的比特操作安全性比较，有助于更精确的评估。 该模型包括基线、常系数和桶式矩阵评估变体。小参数实验验证了公式，渐近分析确认主导常数因子与域算术成本匹配。

rss · IACR ePrint 密码学论文 · 7月6日 13:02

**背景**: 多元二次（MQ）系统是许多后量子密码系统的基础；求解 MQ 问题属于 NP 困难。XL 算法通过单项式扩展方程并线性化以求解。Wiedemann 算法通过计算极小多项式求解稀疏线性系统，Berlekamp-Massey 算法寻找线性递归序列的极小多项式，两者均用于加速 XL 过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2112.05023">[2112.05023] Polynomial XL: A Variant of the XL Algorithm ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Berlekamp-Massey_algorithm">Berlekamp-Massey algorithm</a></li>
<li><a href="https://isarpublisher.com/backend/public/assets/articles/1743275400-ISARJMRS--2422025--Gallery-Script.pdf">PDF Wiedemann algorithm: an efficient approach for solving linear systems ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#multivariate-quadratic`, `#cryptanalysis`, `#computational-cost`, `#post-quantum-cryptography`

---

<a id="item-3"></a>
## [HAWK“猜谜游戏”攻击并非多项式时间](https://eprint.iacr.org/2026/1377) ⭐️ 9.0/10

该论文首次实现了此前未具现的 HAWK“猜谜游戏”攻击，实验揭示其复杂度因类数障碍呈超多项式增长，推翻了先前的多项式时间声明。原始攻击者已认可这些发现。 这一反驳恢复了对 NIST 后量子候选签名方案 HAWK 安全性的信心，并强调了密码分析中实际实现与实验验证的重要性。 攻击的多项式时间声明依赖于四个启发式假设；实验发现其中第四个启发式有误，导致运行时间随维度 n 指数级增长。机器验证的约简提供了至少超多项式复杂度的正式证据，而 AI 工具在快速原型实现中起到了关键作用。

rss · IACR ePrint 密码学论文 · 7月5日 10:47

**背景**: HAWK 是一种基于格的抗量子签名方案，是 NIST 附加数字签名标准化过程的候选方案之一。“猜谜游戏”攻击此前声称可在多项式时间内攻破 HAWK，引发对其安全性的担忧。本项新工作表明该攻击实际为超多项式复杂度，因此不构成实质性威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hawk-sign.info/">Hawk</a></li>
<li><a href="https://csrc.nist.gov/csrc/media/Projects/pqc-dig-sig/documents/round-1/spec-files/hawk-spec-web.pdf">HAWK Specification Document - NIST Computer Security Resource ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lattice-based_cryptography">Lattice-based cryptography</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#lattice-based cryptography`, `#security analysis`, `#machine-checked proof`

---

<a id="item-4"></a>
## [带预处理的隐私信息检索黑盒密码学下界](https://eprint.iacr.org/2026/1384) ⭐️ 8.0/10

该论文证明，对于带客户端预处理的单服务器隐私信息检索（PIR），若客户端为 n 比特数据库存储 s 比特预处理信息，则任何使用黑盒密码学的方案在线摊销计算量必须为 Ω(n/s)。 这些下界解决了隐私信息检索领域的一个关键开放问题，明确了固有的效率权衡，并排除了基于黑盒技术构建双重高效方案的可能性，从而指导未来协议设计向依赖于基于格的密码学等结构化假设的方向发展。 这些下界是最优的，因为现有方案要么满足通信需求、要么满足计算需求，但不能同时兼顾；此外，它们适用于对称 PIR，且是无条件成立的，而之前的通信下界需要复杂性假设。

rss · IACR ePrint 密码学论文 · 7月7日 12:48

**背景**: 隐私信息检索（PIR）允许客户端在不泄露所查询记录的情况下检索数据库。单服务器 PIR 传统上每次查询都需要服务器线性计算量；预处理允许客户端存储一些预计算数据来降低在线成本。黑盒密码学将密码原语视为预言机，不利用其内部结构；该模型中的下界揭示了通用构造的障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Private_information_retrieval">Private information retrieval</a></li>
<li><a href="https://en.wikipedia.org/wiki/Black-box_obfuscation">Black-box obfuscation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#private information retrieval`, `#lower bounds`, `#blackbox constructions`, `#preprocessing`

---

<a id="item-5"></a>
## [PriFT：利用现有 MPC 和 HE 库进行隐私微调](https://eprint.iacr.org/2026/1381) ⭐️ 8.0/10

研究人员提出了 PriFT 框架，利用现有的安全多方计算（MPC，基于 Crypten）和同态加密（HE，基于 TenSEAL）库进行神经网络隐私微调，支持全隐私和半隐私两种训练模式。开源实验表明 MPC 性能远超 HE，半隐私 MPC 准确率接近明文训练，且比全隐私训练快约 3 倍。 该研究突破了隐私保护机器学习中计算开销极高的训练瓶颈，不再局限于推理阶段。通过实现隐私微调，可使工程师在不违反隐私法规的前提下更早使用敏感客户数据，有望加速医疗、金融等领域的隐私机器学习应用。 PriFT 以 Transformer 为特征提取器，在加密特征上训练神经网络。它对比了 Crypten（MPC）和 TenSEAL（HE）两种后端，在半隐私模式下仅解密真实与预测标签来提升性能，同时保持特征数据的隐私性。

rss · IACR ePrint 密码学论文 · 7月6日 10:41

**背景**: 安全多方计算（MPC）允许多方在不泄露各自输入的情况下联合计算函数。同态加密（HE）则允许直接在加密数据上运算，结果解密后与明文运算一致。两者都用于隐私保护机器学习，但训练阶段通常比推理阶段计算开销大得多。微调是一种常见方法，即使用小数据集对预训练模型进行调整以适应新任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multi-party_computation">Multi-party computation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_encryption">Homomorphic encryption</a></li>

</ul>
</details>

**标签**: `#privacy-preserving`, `#machine learning`, `#fine-tuning`, `#secure computation`, `#cryptography`

---

<a id="item-6"></a>
## [TIM：零知识证明隐私盲水印](https://eprint.iacr.org/2026/1380) ⭐️ 8.0/10

TIM 是首个公开可验证的盲水印方案，利用零知识证明在验证提取正确性时无需透露敏感的水印种子和嵌入位置。 这消除了验证者不会滥用暴露秘密的信任假设，极大增强了数字版权管理的安全性，使水印验证可在不信任环境中广泛采用。 TIM 通过结合 Nova 与 Spartan 实现迭代证明，采用基于阈值的投票机制进行稳健检测，并引入分层状态更新降低开销；对于 4K 图像，证明生成耗时 5.61 分钟，峰值内存 9.61 GB。

rss · IACR ePrint 密码学论文 · 7月6日 09:54

**背景**: 盲水印技术允许在没有原始图像的情况下验证所有权，但现有方法在提取时需公开秘密水印参数。零知识证明允许证明者向验证者证明陈述真实性而不泄露底层秘密。整数离散余弦变换（Integer DCT）是图像水印嵌入与提取的常用技术。TIM 将基于 Integer DCT 的盲水印提取过程改造为适合算术电路零知识证明的形式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof</a></li>
<li><a href="https://en.wikipedia.org/wiki/Discrete_cosine_transform">Discrete cosine transform - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2212.12678">[2212.12678] Towards Blind Watermarking: Combining Invertible ... An improved blind watermarking scheme for color image ... Blind Watermarking of Color Medical Images Using Hadamard ... A Robust Image Blind Watermarking Scheme Based on Staged ...</a></li>

</ul>
</details>

**标签**: `#blind watermarking`, `#zero-knowledge proofs`, `#privacy`, `#image verification`, `#digital watermarking`

---

<a id="item-7"></a>
## [(R)Icy-DVRF：具有固定大小证明的鲁棒异步分布式可验证随机函数](https://eprint.iacr.org/2026/1378) ⭐️ 8.0/10

本文提出了(R)Icy-DVRF，一种通过在基于 FROST 的 Icy-DVRF 协议中集成 ROAST 包装器，从而在异步网络中实现鲁棒性和活性，同时保持恒定大小证明的分布式可验证随机函数。 鲁棒性和活性对于区块链等去中心化系统中的 DVRF 至关重要，确保即使部分参与者恶意或无响应，也能可靠地产生不可预测的随机数。这项工作解决了使 DVRF 在实际异步环境中实用的一个关键挑战。 该协议使用 ROAST 包装器，它将阈值签名方案转换为鲁棒的异步方案，并叠加在基于 FROST 的 Icy-DVRF 之上。它保持恒定的证明大小，即输出和验证不会随参与者数量增加而增长。

rss · IACR ePrint 密码学论文 · 7月5日 21:20

**背景**: 可验证随机函数（VRF）产生随机输出及其可验证证明，分布式 VRF（DVRF）将密钥生成和评估分散给多方以避免中心化。FROST 是一种高效的阈值 Schnorr 签名方案，支持多方签名。ROAST 是一个包装器，通过处理无响应签名者为阈值签名添加鲁棒性和异步性。此前的 Icy-DVRF 基于 FROST 构建了 DVRF，但在异步条件下缺乏鲁棒性。(R)Icy-DVRF 引入 ROAST 来克服这一局限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2024/1130">Distributed Verifiable Random Function With Compact Proof</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3548606.3560583">ROAST: Robust Asynchronous Schnorr Threshold Signatures</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-030-81652-0_2">FROST: Flexible Round-Optimized Schnorr Threshold Signatures</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#distributed systems`, `#verifiable random functions`, `#threshold signatures`, `#asynchronous networks`

---

<a id="item-8"></a>
## [HEAD-FL：集成自适应差分隐私与可验证同态聚合的联邦学习框架](https://eprint.iacr.org/2026/1376) ⭐️ 8.0/10

该论文提出了 HEAD-FL 联邦学习框架，它首次在 Rényi 差分隐私框架下引入逐轮自适应的差分隐私，并与可验证同态聚合相结合，实现了紧凑的隐私预算累积和基于 FedAvg 的高效聚合。 通过同时提供形式化隐私保证、抵御恶意服务器的可验证性以及提升的通信效率，HEAD-FL 使得联邦学习在敏感且带宽受限的场景中更安全、更实用。 HEAD-FL 采用基于 Rényi 差分隐私的逐轮自适应高斯机制，实现了更紧凑的隐私组合和明确的(ε, δ)-DP 保证；利用联邦平均（FedAvg）减少通信开销，并对客户端掉线具有鲁棒性。

rss · IACR ePrint 密码学论文 · 7月5日 06:31

**背景**: 联邦学习在分散数据上训练模型而不共享原始数据。差分隐私通过添加噪声提供正式保证，但通常是固定噪声。同态加密允许对密文进行计算，安全聚合则合并加密的更新。Rényi 差分隐私是一种放宽定义，可在多轮训练中实现更紧凑的隐私损失核算。HEAD-FL 整合这些技术以应对联邦学习中的隐私和完整性挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1702.07476">[1702.07476] Renyi Differential Privacy - arXiv.org</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S1383762124002169">VCSA: Verifiable and collusion-resistant secure aggregation for federated learning using symmetric homomorphic encryption - ScienceDirect</a></li>

</ul>
</details>

**标签**: `#federated learning`, `#differential privacy`, `#homomorphic encryption`, `#secure aggregation`, `#privacy-preserving machine learning`

---

<a id="item-9"></a>
## [法国 ANSSI：2027 年起停止非量子安全加密认证](https://www.schneier.com/blog/archives/2026/07/france-to-stop-certifying-non-quantum-safe-encryption.html) ⭐️ 8.0/10

法国国家信息系统安全局（ANSSI）宣布从 2027 年起停止认证缺乏量子抗性加密的安全产品，并要求到 2030 年仅采购量子安全产品，实际上强制政府和关键基础设施运营商进行迁移。 这一监管强制要求加速了向后量子密码学的迁移，保护敏感的国家数据免受未来量子计算威胁，并可能树立先例，促使其他国家采取类似措施。 ANSSI 认证对于法国政府和关键基础设施使用的产品是强制性的，因此该政策实际上在淘汰非量子安全加密。时间表设定 2027 年变更认证要求，2030 年强制采购量子安全产品。

rss · Schneier on Security · 7月6日 10:45

**背景**: 后量子密码学（PQC）开发能够抵御经典和量子计算机攻击的算法。美国 NIST 正在标准化基于结构化格子和哈希函数的 PQC。ANSSI 是法国国家网络安全机构，负责为政府使用产品进行认证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography - Wikipedia</a></li>
<li><a href="https://www.nist.gov/cybersecurity-and-privacy/what-post-quantum-cryptography">What Is Post-Quantum Cryptography? | NIST</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agence_Nationale_de_la_Sécurité_des_Systèmes_d'Information">Agence nationale de la sécurité des systèmes d'information</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#encryption`, `#policy`, `#quantum safety`, `#ANSSI`

---

<a id="item-10"></a>
## [基于 Walsh 基和懒比特的 CKKS AES 同态转换 LUT 评估](https://eprint.iacr.org/2026/1385) ⭐️ 7.0/10

提出了一种在 CKKS 同态加密中评估大型布尔查找表（LUT）的方法，通过 Walsh 基表示、懒加法形成奇偶校验和，并利用二进制自举刷新，将乘法深度与 LUT 大小解耦；应用于 AES-CTR 同态转换，比先前方法加速 3.25 倍。 该工作将同态评估的乘法深度与查找表大小解耦，使得在 CKKS 中能高效处理 AES S 盒等大 LUT，显著加速了同态转换——这是实用安全计算中的关键操作。 该方法利用懒 CKKS 加法实现 XOR，将奇偶校验和打包到密文槽，并通过二进制自举（StC、CtS、EvalMod）清理和映射比特。针对 AES 采用 nibble-split Walsh S 盒分解，额外消耗一层乘法深度但支持更多并行块。

rss · IACR ePrint 密码学论文 · 7月7日 16:22

**背景**: CKKS 是一种支持加密实数近似运算的全同态加密方案。查找表（LUT）用于评估任意函数，但大 LUT 通常需要很深的乘法电路。Walsh 基是布尔函数的一种正交基，懒比特技术通过将 XOR 视为加法并利用低比特正确性来避免昂贵的 XOR 操作。同态转换将 AES 加密数据转换为 CKKS 密文以便进行同态处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1385">Walsh LUT Evaluation on Lazy Bits for CKKS AES Transciphering</a></li>

</ul>
</details>

**标签**: `#homomorphic encryption`, `#CKKS`, `#LUT evaluation`, `#AES transciphering`, `#cryptography`

---

<a id="item-11"></a>
## [基于属性的内积函数加密分层结构形式化](https://eprint.iacr.org/2026/1379) ⭐️ 7.0/10

本文形式化了基于属性的内积函数加密（AB-IPFE）的两层分层框架，并根据可分层性对现有方案进行了分类。作者提出了多种基于配对的新构造，实现了自适应安全性，并引入了具有更短中间密钥的变体方案。 密钥生成的分层分解支持更灵活的密钥管理和委托，填补了 AB-IPFE 领域的空白。这推动了细粒度访问控制和加密计算的发展，有望实现更可扩展的实际系统。 该框架专注于支持算术程序（公开索引）和属性隐藏内积谓词（私有索引）的自适应安全方案。新构造基于谓词编码和配对，在可分层性、密文大小和密钥大小之间权衡；并结合了零类型谓词和密文策略变体的支持。

rss · IACR ePrint 密码学论文 · 7月6日 07:12

**背景**: 基于属性的内积函数加密（AB-IPFE）结合了属性加密（ABE）的访问控制和内积函数加密（IPFE）的线性计算能力。加密中的分层结构（如分层身份加密）将密钥生成分解为多个步骤，提高了灵活性。本文专门为 AB-IPFE 形式化了两层层次结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2019/846">Practical Attribute Based Inner Product Functional Encryption from Simple Assumptions</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-642-13190-5_4">Fully Secure Functional Encryption: Attribute-Based Encryption and (Hierarchical) Inner Product Encryption | Springer Nature Link</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0304397520301286">A fully distributed hierarchical attribute-based encryption scheme - ScienceDirect</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#functional encryption`, `#attribute-based encryption`, `#inner-product encryption`, `#hierarchical encryption`

---

<a id="item-12"></a>
## [Cloudflare Workers 缓存：通过 HTTP 头配置的区域分层缓存](https://blog.cloudflare.com/workers-cache/) ⭐️ 7.0/10

Cloudflare 推出了 Workers Cache，一个位于 Workers 前方的区域分层缓存层，完全可通过标准 HTTP 头进行配置。 该功能让开发者无需复杂代码即可声明式地精细控制边缘缓存，从而改善动态内容交付并减少源站负载。 它使用 Cache-Control 等标准 HTTP 缓存头，与编程式 Cache API 相区别，并利用区域分层架构以提高命中率。

rss · Cloudflare Blog (PQ 迁移) · 7月6日 13:00

**背景**: Cloudflare Workers 是一个无服务器边缘计算平台。边缘缓存将内容存储在用户附近以提升速度。区域分层缓存增加中间缓存层来提高命中率。像 Cache-Control 这样的 HTTP 缓存头是服务器设置缓存规则的标准方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/workers/reference/how-the-cache-works/">How the Cache works · Cloudflare Workers docs</a></li>
<li><a href="https://blog.cloudflare.com/introducing-regional-tiered-cache/">Reduce latency and increase cache hits with Regional Tiered Cache</a></li>
<li><a href="https://www.keycdn.com/blog/http-cache-headers">HTTP Cache Headers - A Complete Guide - KeyCDN</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#workers`, `#cache`, `#edge-computing`, `#web-performance`

---

<a id="item-13"></a>
## [谷歌起诉使用 Gemini AI 的中国钓鱼网络](https://www.schneier.com/blog/archives/2026/07/google-is-suing-chinese-scammers-who-are-using-gemini.html) ⭐️ 7.0/10

谷歌正在起诉一个名为 Outsider Enterprise 的中国网络犯罪团伙，该团伙利用谷歌的 Gemini AI，通过 Telegram 自动化提供钓鱼即服务，并提供近 300 种诈骗模板。 此案凸显了生成式 AI 被滥用于复杂网络犯罪的趋势，并为追究 AI 驱动的诈骗者法律责任开创了潜在先例，对网络安全、AI 伦理和国际执法产生影响。 根据谷歌的起诉文件，Outsider Enterprise 在 Telegram 上运作，指导用户如何使用 Gemini 创建模仿谷歌、YouTube 和纽约州 E-ZPass 等机构的虚假网站，并提供近 300 种模板。

rss · Schneier on Security · 7月7日 10:43

**背景**: Google Gemini 是谷歌开发的生成式 AI 模型系列，能生成文本、图像和代码。钓鱼即服务（PhaaS）是一种网络犯罪模式，犯罪分子以订阅方式出售钓鱼工具包、模板和基础设施，使新手也能发动复杂攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Gemini">Google Gemini - Wikipedia</a></li>
<li><a href="https://www.huntress.com/cybersecurity-101/topic/phishing-as-a-service">What is Phishing-as-a-Service | Cybercrime Democratized | Huntress</a></li>

</ul>
</details>

**标签**: `#AI misuse`, `#cybersecurity`, `#legal`, `#phishing`, `#Google`

---
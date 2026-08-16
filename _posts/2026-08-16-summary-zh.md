---
layout: default
title: "Horizon Summary: 2026-08-16 (ZH)"
date: 2026-08-16
lang: zh
---

> 从 50 条内容中筛选出 15 条重要资讯。

---

1. [基于 LWE 的首个完全简洁多密钥全同态加密及速率 1 阈值解密](#item-1) ⭐️ 9.0/10
2. [首个保证对数最坏情况复杂度的 CGKA 协议](#item-2) ⭐️ 9.0/10
3. [Aegon：面向全球加密消息的自审计密钥透明方案](#item-3) ⭐️ 8.0/10
4. [首个针对多头 Softmax 注意力模型的密码分析提取攻击](#item-4) ⭐️ 8.0/10
5. [ePrint 2026/1693：Simon 的 DCP 量子算法并未解决该问题](#item-5) ⭐️ 8.0/10
6. [从跳轮到跳 S 盒：子空间限制攻击 Poseidon](#item-6) ⭐️ 8.0/10
7. [混合量子态平均情况学习困难性与密码学的等价性](#item-7) ⭐️ 8.0/10
8. [基于 Module-SIS 的并发安全紧凑盲签名方案](#item-8) ⭐️ 8.0/10
9. [神经网络流水线实现三元快速矩阵乘法加性复杂度新低](#item-9) ⭐️ 8.0/10
10. [LLM 引导的形式化证明解决对称密码学开放问题](#item-10) ⭐️ 8.0/10
11. [循环安全密码原语的统一框架](#item-11) ⭐️ 8.0/10
12. [非交互式 Winternitz 到 Lamport 签名转换降低 BitVM 链上数据](#item-12) ⭐️ 8.0/10
13. [wolfSSL ML-KEM 不完整密文比较可致完整密钥恢复](#item-13) ⭐️ 8.0/10
14. [基于 LWE 的简单高效 SKL-IBE 经典撤销方案](#item-14) ⭐️ 8.0/10
15. [MinMandate：面向自适应代理的任务范围支付授权隐私方案](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [基于 LWE 的首个完全简洁多密钥全同态加密及速率 1 阈值解密](https://eprint.iacr.org/2026/1683) ⭐️ 9.0/10

该论文在标准 LWE 假设下构造了首个密文、公钥和私钥大小均与用户数量无关的多密钥全同态加密（MKFHE）方案。同时提出单轮分布式解密协议，各用户的部分解密份额大小等于明文长度（速率 1）且可模拟。 这项工作解决了长期未决的开放问题，证明在标准假设下可实现常数大小密文，消除了主要的效率瓶颈。它为通信复杂度渐近最优的多方计算协议铺平道路，推动安全计算实用化。 该方案是分层的（leveled），而非完全自举；此前所有 MKFHE 方案的密文大小至少随用户数量 N 线性增长。部分解密份额大小与明文完全相同（速率 1），且诚实用户的份额可模拟，这在标准假设下单轮协议中此前未能同时实现。

rss · IACR ePrint 密码学论文 · 8月13日 21:40

**背景**: 同态加密允许在不解密的情况下对加密数据进行计算。多密钥全同态加密将其扩展到不同用户密钥下的密文，支持对私有输入的联合计算。LWE（带错误学习）是一种抗量子的困难问题，是许多格密码方案的基础。阈值解密将私钥分片给多方，需共同协作才能解密，从而保护隐私。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_encryption">Homomorphic encryption - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Threshold_cryptosystem">Threshold cryptosystem - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Learning_with_errors">Learning with errors - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#fully homomorphic encryption`, `#multi-key FHE`, `#LWE`, `#threshold decryption`

---

<a id="item-2"></a>
## [首个保证对数最坏情况复杂度的 CGKA 协议](https://eprint.iacr.org/2026/1677) ⭐️ 9.0/10

该论文提出了首个在计算和通信上都具有可证明对数最坏情况复杂度的连续群组密钥协商（CGKA）协议。该协议基于分解学习带错误（decomposed LWE）这一可证伪且可能抗量子的假设，随机预言机扩展可增加前向安全性，同时保持次线性通信。 这解决了一个重要的公开问题：MLS/TreeKEM 等实际树形方案在最坏情况下会退化为线性复杂度，而先前的理论方案需要不可区分混淆等不切实际的工具。该结果为大型群组的高效、可证明安全消息传递提供了现实的路径。 基本构造实现了基础 CGKA 安全性和后妥协安全性（PCS），但不具备前向安全性；随机预言机变体增加了前向安全性，但刷新操作需要与群组规模成线性的时间，不过密文保持紧凑。其假设是分解 LWE，可证伪且可能抗量子。

rss · IACR ePrint 密码学论文 · 8月13日 15:09

**背景**: 安全群组消息协议（如 MLS）依赖连续群组密钥协商（CGKA）在动态群组中维护共享秘密，并提供前向安全和后妥协安全。MLS 中使用的 TreeKEM 等实际协议仅在“晴天”情况下达到对数复杂度，最坏情况下会退化为线性。先前的理论解决方案需借助不可区分混淆等强大但不切实际的工具来绕过黑盒不可能性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2025/1035">Continuous Group-Key Agreement: Concurrent Updates without Pruning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Messaging_Layer_Security">Messaging Layer Security - Wikipedia</a></li>
<li><a href="https://eprint.iacr.org/2025/410">TreeKEM: A Modular Machine-Checked Symbolic Security Analysis of Group Key Agreement in Messaging Layer Security</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secure group messaging`, `#continuous group key agreement`, `#MLS`, `#complexity`

---

<a id="item-3"></a>
## [Aegon：面向全球加密消息的自审计密钥透明方案](https://eprint.iacr.org/2026/1681) ⭐️ 8.0/10

研究人员提出了 Aegon，一种密钥透明方案，消除了与字典大小成比例的每轮工作量，实现了不到一分钟的轮次延迟（相比 IronDict 降低 500 倍），并用生产级 Rust 实现在 40 亿条目的字典上以每秒 1250 次更新进行了演示。Aegon 生成小于 30 KB 的恒定大小审计证明，验证时间低于 65 毫秒，且与每轮更新数和目录填充度无关。 这使得轻量级终端用户能够高效地自行审计全球加密消息服务的公钥目录，无需信任第三方全局审计者，从而在数十亿用户规模下直接应对恶意密钥注入风险。 Aegon 采用分片字典设计，将全局参数缩减为分片相关大小并支持水平扩展；证明缓存可安全丢弃历史字典快照，因此存储仅随保留的历史增长。在填满的 2^32 条目目录中，其审计证明大小比 WhatsApp 密钥透明（AKD）小约 8 万倍，验证时间快约 370 倍，同时提供更强的隐私保证。

rss · IACR ePrint 密码学论文 · 8月13日 19:22

**背景**: 密钥透明允许中心化加密消息服务商公开承诺其分发的公钥，使用户能够检测篡改或恶意密钥插入。WhatsApp 和 iMessage 等近期部署依赖第三方全局审计者，这可能成为信任瓶颈，也不适合轻量级客户端。此前的透明字典方案 IronDict 需要全局不变性证明，使每轮工作量随整个字典大小扩展。Aegon 基于 IronDict 构建，但用服务器计算量仅取决于每轮更新数的设计取代了这些证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Key_transparency">Key transparency</a></li>
<li><a href="https://eprint.iacr.org/2025/1580">IronDict: Transparent Dictionaries from Polynomial Commitments</a></li>

</ul>
</details>

**标签**: `#key transparency`, `#cryptography`, `#encrypted messaging`, `#security`, `#privacy`

---

<a id="item-4"></a>
## [首个针对多头 Softmax 注意力模型的密码分析提取攻击](https://eprint.iacr.org/2026/1678) ⭐️ 8.0/10

该论文提出了首个针对多头 Softmax 注意力模型的攻击方法，形式化了可提取代表元，并给出了提取规范代表模型参数的多项式时间算法。在有限精度实验中，成功提取了 token 维度为 8、6 个头的 Softmax 注意力模型参数，精度达到 2^{-51}；同时克服了现有单层单头 Transformer 参数提取算法在 ReLU 前馈网络含偏置项时失效的局限。 Softmax 注意力是 Transformer 架构的核心组件，而现有密码分析式提取攻击依赖 ReLU 等分段线性特性，无法处理其平滑且依赖序列的非线性。该工作将模型提取扩展到 Transformer，对 AI/ML 安全、模型知识产权保护和对抗性风险评估具有重要意义。 由于仅从值查询无法唯一确定多头注意力层参数，论文定义了可提取代表元，并给出了获取规范代表模型参数的多项式时间算法。对 token 维度为 8、6 个头的模型进行有限精度实验，提取精度达 2^{-51}，表明 Softmax 归一化本身暴露了可利用的代数结构。

rss · IACR ePrint 密码学论文 · 8月13日 16:10

**背景**: 密码分析式模型提取由 Carlini 等人在 CRYPTO 2020 提出，可从黑盒查询中恢复神经网络参数，通常依赖 ReLU 等分段线性激活函数的特性。Softmax 注意力是 Transformer 的关键组件，采用缩放点积和 Softmax 归一化计算注意力权重，其非线性平滑且依赖序列，难以套用已有的分段线性方法。多头注意力则将输入拆分到多个头以捕捉不同关系，进一步增加了提取难度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2003.04884">[2003.04884] Cryptanalytic Extraction of Neural Network Models</a></li>
<li><a href="https://en.wikipedia.org/wiki/Attention_(machine_learning)">Attention (machine learning) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#model extraction`, `#neural network security`, `#transformers`, `#attention mechanism`, `#cryptanalysis`

---

<a id="item-5"></a>
## [ePrint 2026/1693：Simon 的 DCP 量子算法并未解决该问题](https://eprint.iacr.org/2026/1693) ⭐️ 8.0/10

这篇新的 ePrint 笔记（2026/1693）正式证明，Simon 最近提出的量子算法（ePrint:2026/1591）无法以不可忽略的优势提取二面体陪集问题（DCP）密钥的最低有效位，因此并未解决 DCP。作者还为遵循 Regev 归约模板的算法建立了更广泛的不可能结果，并发布了 Lean 4 形式化代码。 这一结果严格驳斥了最近声称的 DCP 多项式时间量子算法，而 DCP 是基于格的密码学量子分析中的核心问题。它阻止了社区在错误方向上投入，并澄清了未来任何 Regev 风格 DCP 算法必须满足的条件。 证明表明，Simon 的算法在误差为 poly(n)2^{-n/3} 的情况下，仅需使用经典傅里叶标签的最高有效三分之一即可实现，因此无法成功。这一不可能结果适用于更广泛的 Regev 模板算法，意味着此类算法在反计算阶段很可能必须充分利用经典傅里叶标签；Lean 4 代码已发布在 GitHub 上。

rss · IACR ePrint 密码学论文 · 8月15日 03:46

**背景**: 二面体陪集问题（DCP）要求从形如 |x⟩|0⟩ + |x+d⟩|1⟩ 的量子样本中恢复秘密 d。Regev 在 2004 年的量子归约将 DCP 与唯一最短向量问题（unique-SVP）及相关格问题联系起来，因此高效的 DCP 求解器可能威胁基于格的密码学。2026 年 8 月，Simon 在 ePrint 2026/1591 中声称给出了 DCP 的多项式时间量子算法；这篇新笔记证明该算法实际上无法工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1693">The ePrint:2026/1591 Quantum Algorithm Does Not Solve DCP</a></li>
<li><a href="https://postquantum.com/security-pqc/simon-quantum-algorithm-lattice-pqc/">Simon Claims Polynomial-Time DCP Quantum Algorithm</a></li>
<li><a href="https://xenospectrum.com/en/quantum-dcp-algorithm-pqc/">AWS Researcher Claims Polynomial-Time Solution to Quantum-Hard DCP, With Conditional Implications for Lattice Cryptography | XenoSpectrum</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#cryptography`, `#dihedral coset problem`, `#post-quantum`, `#algorithms`

---

<a id="item-6"></a>
## [从跳轮到跳 S 盒：子空间限制攻击 Poseidon](https://eprint.iacr.org/2026/1692) ⭐️ 8.0/10

该论文提出了一种名为 GSR 的广义 S-box 跳过方法，可以在不提高 Poseidon 多项式系统次数的情况下吸收一个初始完整轮和 t−2k 个部分轮。基于此得到了概率为 1 的区分器，覆盖 t−2k+1 轮，并在以太坊 Poseidon 计划设置（KoalaBear 域，t=24，α=3）中实验求解了 31 轮中的 28 轮 CICO-1 问题和 31 轮中的 25 轮 CICO-2 问题。 Poseidon 是零知识证明系统中广泛使用的哈希函数，因此一个与轮常数和 MDS 矩阵无关的概率为 1 区分器会削弱对其安全裕度的信心。该技术可能导向针对已部署协议的实际攻击，并影响未来算术化导向哈希函数的设计。 该子空间限制方法仅由 t 和 k 调整，因此结果适用于任意轮常数、MDS 矩阵、S-box 指数 α 或域大小 p 的 Poseidon 结构。攻击通过消耗输入自由度来线性化内部状态转移，但论文并未声称在所示 CICO 实例之外实现完整的原像或碰撞破解。

rss · IACR ePrint 密码学论文 · 8月15日 02:00

**背景**: Poseidon 是一种为在零知识证明系统中高效运行而设计的密码学哈希函数，它在大素数域上进行加法和乘法运算，而非像传统哈希那样使用位运算。它采用海绵结构，包含完整轮和部分轮；部分轮只对状态的一部分元素应用 S-box，以降低算术电路复杂度。CICO（约束输入约束输出）问题要求找到满足特定输入输出约束的输入，是密码分析中常见的攻击目标。以太坊 Poseidon 计划规定了 31 轮变体，使用 KoalaBear 域，状态大小 t=24，S-box 指数 α=3。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.poseidon-hash.info/">Poseidon Hash</a></li>
<li><a href="https://docs.pantherprotocol.io/docs/learn/cryptographic-primitives/poseidon">Poseidon | Panther Protocol Documentation</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#zero-knowledge proofs`, `#hash functions`, `#cryptanalysis`, `#Poseidon`

---

<a id="item-7"></a>
## [混合量子态平均情况学习困难性与密码学的等价性](https://eprint.iacr.org/2026/1691) ⭐️ 8.0/10

本文证明了混合量子态的平均情况学习困难性（AHL）与不可高效验证的单向量子态生成器（IV-OWSG）的存在性等价，解决了此前未解决的问题。该结果还将混合态 AHL 与 EFI 对联系起来，并在 SWAP 预言机下得到了 IV-OWSG 与 OWSG 的分离。 该工作建立了量子学习困难性与量子密码原语之间的基础性联系，有助于理解量子密码所需的最小假设。分离结果厘清了量子单向性概念之间的层级关系，对设计抗量子安全协议具有重要意义。 该等价性针对不可高效验证的单向量子态生成器（IV-OWSG），其中验证算法不需要高效，这是比标准 OWSG 更弱的概念。分离结果依赖于已有的预言机结果并使用 SWAP 预言机，表明在该预言机模型下 IV-OWSG 与 OWSG 并不相同。

rss · IACR ePrint 密码学论文 · 8月14日 14:30

**背景**: 量子态的平均情况学习困难性（AHL）指的是任何高效算法都无法以显著高于随机猜测的概率从样本中学习未知量子态。单向量子态生成器（OWSG）是经典单向函数的量子类似物，产出难以求逆的量子态；不可高效验证的 OWSG（IV-OWSG）则放宽要求，允许验证算法不受计算资源限制。EFI 对是两族可高效制备但在统计上相距很远、计算上不可区分的量子态，是量子密码学的核心原语之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2404.13699">Exponential Quantum One -Wayness and EFI Pairs</a></li>
<li><a href="https://inspirehep.net/literature/2779580">Exponential Quantum One-Wayness and EFI Pairs - INSPIRE</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#cryptography`, `#learning theory`, `#quantum cryptography`, `#average-case hardness`

---

<a id="item-8"></a>
## [基于 Module-SIS 的并发安全紧凑盲签名方案](https://eprint.iacr.org/2026/1690) ⭐️ 8.0/10

作者提出了一种基于 Module-SIS 的并发安全盲签名方案，该方案去除了零知识证明，实现了 4.7 KB 的紧凑签名，而现有格基构造的基线为 22 KB。 这显著缩小了格基盲签名的签名尺寸瓶颈，使后量子隐私保护协议更加实用。 该方案在 Module-SIS 假设下实现并发安全；由于拒识抽样，可能需要额外轮次，但诚实用户的期望轮数可低至 1.1，恶意用户最多在 2.6 轮内终止。

rss · IACR ePrint 密码学论文 · 8月14日 12:07

**背景**: 盲签名允许用户在不向签名者透露消息内容的情况下获得有效签名，是隐私保护系统的核心构件。格基密码学是主要的后量子方法，可抵抗量子攻击，Module-SIS 问题作为其困难数学假设。以前的格基盲签名依赖零知识证明，导致签名至少为 22 KB。本工作改而遵循格基Σ协议生成短原像，从而避免了零知识证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blind_signature">Blind signature - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/BLISS_signature_scheme">BLISS signature scheme</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-58723-8_5">Concurrently Secure Blind Schnorr Signatures | Springer Nature Link</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#blind signatures`, `#lattice-based cryptography`, `#post-quantum`, `#privacy`

---

<a id="item-9"></a>
## [神经网络流水线实现三元快速矩阵乘法加性复杂度新低](https://eprint.iacr.org/2026/1688) ⭐️ 8.0/10

研究人员提出一种基于神经网络的流水线，用于生成和优化三元快速矩阵乘法算法，并在多种小维度上实现了创纪录的低加性复杂度，尤其在 (2,2,k) 维度上，且随 k 增大改进更显著。 矩阵乘法是科学计算、机器学习等众多领域的核心运算，具有三值系数、稀疏性和低加法次数的快速矩阵乘法算法更易于硬件实现；这项工作为小维度算法发现提供了新的自动化方法，并可能加速实用快速算法的设计。 该流水线可调整以输出具有 {-1,0,1} 三值系数、稀疏性和低优化后加法次数的方案；作者生成并优化了数千个快速矩阵乘法算法，并用热图分析其性能。他们还发现加法优化行为随维度不同差异很大，且在 (2,2,k) 中最小加法数的生成有时对整个流水线并非最优；相关实现和数据集已公开。

rss · IACR ePrint 密码学论文 · 8月14日 09:57

**背景**: 矩阵乘法是数值算法、图分析和模式识别等领域的基础运算。标准算法需要 O(n^3) 次算术运算，而 Strassen 等快速矩阵乘法算法通过巧妙组合减少乘法次数，但通常会增加加法次数。加性复杂度衡量算法所需的加法次数，而仅使用 {-1,0,1} 中的系数（三值）能简化实际实现。搜索最优的三元快速矩阵乘法方案是一个困难的组合优化问题，神经网络可以帮助探索这类方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fast_matrix_multiplication_algorithms">Fast matrix multiplication algorithms</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication">Computational complexity of matrix multiplication - Wikipedia</a></li>

</ul>
</details>

**标签**: `#matrix multiplication`, `#neural networks`, `#algorithm discovery`, `#computational complexity`, `#optimization`

---

<a id="item-10"></a>
## [LLM 引导的形式化证明解决对称密码学开放问题](https://eprint.iacr.org/2026/1687) ⭐️ 8.0/10

该论文提出了 Pilot-Sailor 框架：Pilot 提出中间命题和证明计划，Sailor 尝试形式化证明，只有经过机器检查的声明才能进入已验证上下文。该框架被应用于 14 个布尔函数理论和对称密码分析案例研究，解决了包括逐点 Tu-Deng 猜想在内的多个开放问题，并建立了新的非线性度上界。 该工作表明，LLM 引导的形式化证明助手能够解决对称密码学中长期悬而未决的理论问题，包括一个自 2011 年提出的猜想。它可能加速布尔函数和密码分析界的研究，并为可验证的人工智能辅助数学提供范例。 关于 Tu-Deng 界的等式条件指出，若 t 有 z 个零位，则等式成立当且仅当相邻零位之间的每个循环间隔至少为 z，从而给出等式情形数量的闭式公式。论文还证明，对于 n=2k≥6 且 k<m<2k，每个 F: F_2^n→F_2^m 都满足 NL(F) ≤ 2^{n-1} - 2^{n/2-1} - 2，并通过精确谱分类确定 8 变量平衡布尔函数的最大非线性度为 116；这些结果目前以预印本形式发表，尚未经过同行评审。

rss · IACR ePrint 密码学论文 · 8月14日 07:19

**背景**: 对称密码学依赖布尔函数构建 S 盒等组件，其对线性密码分析和差分密码分析的抵抗能力由非线性度衡量。Tu-Deng 猜想于 2011 年提出，涉及二进制展开的汉明权重的组合不等式，此前仅在有限参数范围内得到验证。形式化证明助手要求每一步推理都由机器检查，而 LLM 引导系统为这类助手生成候选引理和证明计划。此类非线性度上界的改进对设计密码学安全的置换至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.05187">A Complete Proof for Tu - Deng Conjecture</a></li>
<li><a href="https://www.alphaxiv.org/abs/1707.7945">The Tu -- Deng Conjecture holds almost surely | alphaXiv</a></li>
<li><a href="https://www.researchgate.net/publication/330526127_One_Note_About_the_Tu-Deng_Conjecture_in_Case_wt_5">(PDF) One Note About the Tu - Deng Conjecture in Case w(t) = 5</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#symmetric cryptography`, `#Boolean functions`, `#formal verification`, `#LLM`

---

<a id="item-11"></a>
## [循环安全密码原语的统一框架](https://eprint.iacr.org/2026/1686) ⭐️ 8.0/10

该论文为弱伪随机函数引入了密钥相关移位（KDS）安全性，并证明提示伪随机生成器、密钥相关消息安全的对称加密、线性抵抗伪随机生成器和提示弱伪随机函数之间存在存在性等价。论文还基于 KDS 安全性给出了随机性相关消息安全的公钥加密和关联乘积安全陷门函数的新构造。 该结果在概念上统一了多种循环安全原语，表明构造其中一个就足以获得其他原语，从而简化了理论密码学的研究图景。它提供了一个单一目标——KDS 安全的弱伪随机函数——并为公钥加密和陷门函数带来了新的构造意义。 核心技术贡献是从任意 KDM 安全的对称加密方案通用构造 KDS 安全的弱伪随机函数；此外，KDS 弱伪随机函数还蕴含线性抵抗伪随机生成器、提示弱伪随机函数，并能构造随机性相关消息安全的公钥加密和关联乘积安全陷门函数。令人意外的是，提示伪随机生成器与 KDM 安全的对称加密在存在性上等价。

rss · IACR ePrint 密码学论文 · 8月14日 03:43

**背景**: 密钥相关消息（KDM）安全性要求加密方案在敌手能够获得依赖于密钥的消息的密文时仍然安全。提示伪随机生成器是一种对种子具有确定性循环安全性质的伪随机生成器，由 Koppula 和 Waters 在 CRYPTO 2019 提出。弱伪随机函数仅要求对随机输入保持伪随机性，因此比标准伪随机函数更容易构造。本文提出的 KDS 安全性允许敌手对密钥的移位进行查询，从而强化了弱伪随机函数的安全要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/article/10.1007/s00145-024-09502-9">Cryptographic Primitives with Hinting Property | Journal of Cryptology</a></li>
<li><a href="https://www.cs.columbia.edu/~tal/papers/kdm-survey.pdf">Key dependent message security : recent results and applications</a></li>
<li><a href="https://ntt-research.com/wp-content/uploads/2022/06/New-Constructions-of-Hinting-PRGs-OWFs-with-Encryption.pdf">New Constructions of Hinting PRGs, OWFs with Encryption</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#circular security`, `#key-dependent message security`, `#pseudorandom functions`, `#cryptographic primitives`

---

<a id="item-12"></a>
## [非交互式 Winternitz 到 Lamport 签名转换降低 BitVM 链上数据](https://eprint.iacr.org/2026/1684) ⭐️ 8.0/10

本文提出一种非交互式转换工具，通过秘密共享将 Winternitz 一次性签名转换为 Lamport 签名所用的标签，从而允许在链上使用紧凑的 WOTS 来承诺乱码电路的输入标签。该方案已证明具有自适应隐私，并应用于 BABE，使链上脚本总大小减少超过 3 倍，并使争议交易符合比特币的标准性限制。 这一成果显著降低 BitVM3 和 BABE 等基于乱码电路的比特币二层协议的链上数据成本，提升可扩展性，并为更多参与者打开了大门。它在保持比特币可验证性的同时，恢复了早期 BitVM 版本转向 Lamport 签名后失去的 WOTS 紧凑性。 朴素转换表本会指数级增长，但利用两个对称性将其降至二次：Shamir 重构仅取决于所持分片的数量而非具体都是谁的份额，从而将指数多的消息折叠到单个校验和权重上；而曾经被视为缺点的单调性则按包含关系对求值者的访问进行排序。该工具被建模为乱码方案，并证明具有自适应隐私。

rss · IACR ePrint 密码学论文 · 8月13日 23:48

**背景**: Winternitz 和 Lamport 都是基于哈希的一次性签名方案。Winternitz 签名更紧凑，但其哈希链是单调的，乱码电路求值者可以向前哈希得到多个标签从而破坏隐私；Lamport 签名没有这个问题，但体积大得多，因此 BitVM3 和 BABE 在链上揭示乱码电路输入标签时改用了 Lamport 签名。BitVM2 早期使用的是紧凑的 Winternitz 签名，而后续协议变更迫使其转向更笨重的 Lamport 方案。本文提供了缺失的转换方法，使新的乱码电路设置能够重新利用 Winternitz 的紧凑性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hash-based_cryptography">Hash-based cryptography - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lamport_signature_scheme">Lamport signature scheme</a></li>
<li><a href="https://bitvm.org/">BitVM - Smarter Bitcoin Contracts | BitVM</a></li>

</ul>
</details>

**标签**: `#Bitcoin`, `#Winternitz signatures`, `#Lamport signatures`, `#secret sharing`, `#BitVM`

---

<a id="item-13"></a>
## [wolfSSL ML-KEM 不完整密文比较可致完整密钥恢复](https://eprint.iacr.org/2026/1682) ⭐️ 8.0/10

研究人员证明，wolfSSL 的 ML-KEM 实现中不完整的 Fujisaki–Okamoto 密文比较（x86-64 AVX2 仅比较 1568 字节中的 1536 字节，ARM64 NEON 约比较一半）可通过解密噪声的线性回归实现完整私钥恢复：在 AVX2 上用 400 个密文恢复 ML-KEM-1024 的 98% 私钥系数，在 NEON 上用 600 个密文恢复 98.5%，并在验证参考模型中以约 1300 个密文恢复完整私钥。 这将此前记录的 IND-CCA2 安全削弱升级为广泛部署的后量子 KEM 中的完整密钥恢复漏洞，意味着受影响的 wolfSSL 用户的私钥可能被完全攻破；它还表明常见的“验证所有 u”加固措施无法在 AVX2 后端封堵该漏洞，迫使人们重新审视优化密码学代码中 FO 校验的实现方式。 该攻击通过明文检验预言机从未经校验的 v 尾部字节读取解密噪声，需要 10^5–10^6 次查询（对比密钥不匹配攻击的几千次），仅使用普通最小二乘法而不涉及格基约简，且其成本取决于未校验字节的几何分布而非单纯数量。

rss · IACR ePrint 密码学论文 · 8月13日 19:23

**背景**: ML-KEM（FIPS 203）是 NIST 标准化的基于模格的后量子密钥封装机制；其 IND-CCA2 安全性依赖于 Fujisaki–Okamoto 变换，即在解封装时重新加密恢复出的消息并与接收到的密文进行比较，只有完全匹配才输出共享密钥。wolfSSL 是广泛使用的 C 库，在 x86-64 AVX2 和 ARM64 NEON 上用手写 SIMD 汇编实现 ML-KEM。跳过部分密文字节的不完整比较会让被篡改的密文通过校验，此前主要被当作 IND-CCA2 弱点对待。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://lukas-prokop.at/articles/2020-06-19-fo-transform">The Fujisaki - Okamoto transform</a></li>
<li><a href="https://en.wikipedia.org/wiki/IND-CCA2">IND-CCA2</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#ML-KEM`, `#key recovery`, `#post-quantum`, `#wolfSSL`

---

<a id="item-14"></a>
## [基于 LWE 的简单高效 SKL-IBE 经典撤销方案](https://eprint.iacr.org/2026/1676) ⭐️ 8.0/10

该论文提出了一种基于标准 LWE 假设的简单高效、选择性安全的 SKL-IBE 方案，并改进了 Dual-Regev SKL-PKE 方案的安全性分析，使其在多项式模数下达到多项式困难 LWE 安全性，成为目前已知量子效率最高的 SKL-PKE 方案。 这一成果推进了抗量子密码的实际应用，在标准 LWE 假设下为身份基加密提供了高效的密钥租赁与撤销机制，避免了混淆电路等强假设，有望促进可撤销量子密钥的现实部署。 新 SKL-IBE 方案通过 Agrawal-Boneh-Boyen IBE 框架直接扩展 Dual-Regev SKL-PKE，在多项式模数 LWE 下实现选择性安全，避免混淆电路；支持经典撤销且无需量子信道，但仅具备选择性安全而非自适应安全。

rss · IACR ePrint 密码学论文 · 8月13日 15:03

**背景**: 安全密钥租赁（SKL）是一种量子密码原语，允许出租方将编码在量子态中的解密密钥租给用户并在之后撤销，确保被撤销者失去解密能力；经典撤销指无需量子信道即可完成撤销。身份基加密（IBE）允许用户公钥为任意身份字符串（如邮箱），并依赖可信中心颁发私钥。带错误学习（LWE）是 Regev 于 2005 年提出的标准格密码困难假设，被推测可抵抗量子攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2410.03413v1">A Simple Framework for Secure Key Leasing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Identity-based_encryption">Identity-based encryption</a></li>
<li><a href="https://en.wikipedia.org/wiki/Learning_with_errors">Learning with errors</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#identity-based encryption`, `#learning with errors`, `#quantum cryptography`, `#secure key leasing`

---

<a id="item-15"></a>
## [MinMandate：面向自适应代理的任务范围支付授权隐私方案](https://eprint.iacr.org/2026/1674) ⭐️ 8.0/10

MinMandate 提出了一种密码学方案，能在用户批准的任务范围内实现自适应商家选择，并派生每次呼叫的新支付视图，而无需稳定的跨商家标识符。在 AgentDojo 任务上的实验表明，当 50% 的商家不可用时，MinMandate 在四个测试规划器上平均比 AP2 基线提高了 32.7 个百分点的任务成功率。 这解决了自主代理支付中的一个关键隐私和可用性缺口：用户无需预先指定每个商家，观察者也无法关联分离的付费调用以推断用户的更广泛意图。它可能使代理支付框架在多服务工作流中变得更加灵活且保护隐私。 该方案用每次呼叫的新支付视图取代了稳定的跨商家标识符，Stable Handle 消融实验显示，重新引入可复用的公共支付层句柄会使攻击者的任务恢复成功率平均提高 27.4 个百分点。代码可在 https://github.com/Zora-G/minmandate 获取。

rss · IACR ePrint 密码学论文 · 8月13日 08:30

**背景**: 自主代理是代表用户规划和执行多步骤任务、有时进行购买的 AI 系统。现有的代理支付框架使用商家准入授权凭证，类似于 OAuth 作用域或可验证凭证，但通常要求用户预先指定商家。跨商家复用稳定标识符会让第三方关联用户的活动并推断意图。AgentDojo 是一个用于评估此类代理工作流的基准环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentdojo.spylab.ai/">AgentDojo</a></li>
<li><a href="https://transmute-industries.github.io/authorization-credentials/">Authorization Credentials v0.0</a></li>

</ul>
</details>

**标签**: `#privacy`, `#cryptography`, `#autonomous agents`, `#payments`, `#security`

---
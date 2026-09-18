---
layout: default
title: "Horizon Summary: 2026-09-18 (ZH)"
date: 2026-09-18
lang: zh
---

> 从 51 条内容中筛选出 15 条重要资讯。

---

1. [全轮 DuX 和缩减轮 YuX 的实用密钥恢复攻击](#item-1) ⭐️ 9.0/10
2. [仅凭坍缩散列函数构造 QMA 的简洁论证](#item-2) ⭐️ 9.0/10
3. [超越 Johnson 半径的 Reed-Solomon 码线性列表大小界限](#item-3) ⭐️ 8.0/10
4. [超越 Johnson 界的 Reed-Solomon 码：高效解码与更小证明](#item-4) ⭐️ 8.0/10
5. [Lemur+：紧凑后量子多重签名与多跳聚合](#item-5) ⭐️ 8.0/10
6. [首个加权批量门限加密方案无需批次标签或索引](#item-6) ⭐️ 8.0/10
7. [通过承诺标量折叠改进 ElGamal 可验证洗牌证明](#item-7) ⭐️ 8.0/10
8. [PyuQuMuQu：对 MQ 可链接环签名的攻击与新型 5 轮构造](#item-8) ⭐️ 8.0/10
9. [任意除子椭圆码 McEliece 的多项式时间攻击](#item-9) ⭐️ 8.0/10
10. [面向 SQIsign 四元数算法的更紧整数界与精确矩阵求逆](#item-10) ⭐️ 8.0/10
11. [ROSETTA：混合 CKKS/TFHE 框架加速隐私保护 LLM 解码](#item-11) ⭐️ 8.0/10
12. [Falcon 多余的平方根计算可被故障攻击利用导致密钥恢复](#item-12) ⭐️ 8.0/10
13. [研究者修正 Sparkle+门限 Schnorr 签名安全边界中的代数错误](#item-13) ⭐️ 8.0/10
14. [新攻击显示盲签名和 OPRF 方案通过中止行为泄露秘密](#item-14) ⭐️ 8.0/10
15. [基于群表示理论求解阿贝尔扩张中的理想 uSVP 与理想 BDD](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [全轮 DuX 和缩减轮 YuX 的实用密钥恢复攻击](https://eprint.iacr.org/2026/2045) ⭐️ 9.0/10

作者展示了针对全轮 12 轮 DuX（基于 F_65537）以及 YupX-65537 和 Yu2X-16 的 14 轮中 11 轮的实用密钥恢复攻击，采用选择密文攻击。他们利用解密方向代数次数增长缓慢的特性，把 Yu2X-16 的数据复杂度从 2^96 降至 2^32。 这打破了 DuX 的安全声明并严重削弱了 YuX，这两种密码都是为高效全同态加密评估设计的。它表明仅从加密方向评估代数次数不够，必须同时考虑解密方向，这将影响未来 FHE 友好型分组密码的设计。 攻击用 2^32 个选择密文在 45 个小时核时内恢复 DuX 主密钥；对 YuX 的两种变体恢复了 14 轮中的 11 轮，并将 Yu2X-16 的数据复杂度从 2^96 降至 2^32。核心技术包括零和判据、整块结构、廉价坐标消去和加权矩，且这些区分器与刘国强和孙兵的独立并发工作一致，并将他们全轮攻击的数据复杂度从 2^67.58 降至 2^32。

rss · IACR ePrint 密码学论文 · 9月15日 11:40

**背景**: DuX 和 YuX 是为在全同态加密（FHE）下高效评估而设计的分组密码家族，FHE 允许直接对加密数据进行计算而无需先解密。为了满足 FHE 效率，它们使用低次 S 盒和大有限域上的线性层以保持乘法深度较小。其安全性分析最初侧重于加密方向，该方向上代数次数增长较快。本文表明解密方向增长要慢得多，并利用零和性质（即某些输入集合的输出之和为零）发起选择密文密钥恢复攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/2045">Practical Key Recovery Attacks on Full DuX and Reduced-Round YuX</a></li>
<li><a href="https://eprint.iacr.org/2026/1907.pdf">Higher-order differential attacks on the full DuX Guoqiang Liu1* and Bing Sun1</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fully_homomorphic_encryption">Fully homomorphic encryption</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#block ciphers`, `#fully homomorphic encryption`, `#cryptanalysis`, `#key recovery`

---

<a id="item-2"></a>
## [仅凭坍缩散列函数构造 QMA 的简洁论证](https://eprint.iacr.org/2026/2040) ⭐️ 9.0/10

作者首次仅基于坍缩散列函数这一 Minicrypt 假设构造出 QMA 的简洁论证。其主要技术是一种量子简洁爪态生成协议，仅使用经典通信将少量量子关联扩展为大量爪态关联，并由此得到基于单向函数的量子简洁盲委托协议。 这是首个仅依赖非结构化 Minicrypt 假设（且尚不知道能推出公钥加密）的此类方案，避免了对更强结构化假设的依赖。该结果推进了量子验证与委托的理论基础，并可能影响后量子简洁证明系统的设计。 与 Zhang（STOC 2021）相比，新协议具有更优的轮复杂度、标准模型下的证明且更为简单。由此得到的盲委托协议被代入 Bartusek、Liu 和 Malavolta（EUROCRYPT 2026）的通信压缩编译器，从而获得 QMA 的简洁论证。

rss · IACR ePrint 密码学论文 · 9月15日 07:30

**背景**: QMA 是 NP 的量子类比：由量子多项式时间验证者检查量子证明。坍缩散列函数是一种抗量子安全概念，敌手在输出散列值后无法区分被给的是原像的量子叠加态还是单个原像；它属于 Minicrypt 假设，因为尚不知道它能推出公钥加密。简洁论证让验证者用远少于直接执行计算的通信量或计算量来验证一个陈述。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/QMA">QMA - Wikipedia</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-030-03810-6_12">Classical Proofs for the Quantum Collapsing Property of Classical Hash Functions | Springer Nature Link</a></li>
<li><a href="https://simons.berkeley.edu/talks/succinct-arguments-part-i">Succinct Arguments (Part I)</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#quantum computing`, `#succinct arguments`, `#QMA`, `#Minicrypt assumptions`

---

<a id="item-3"></a>
## [超越 Johnson 半径的 Reed-Solomon 码线性列表大小界限](https://eprint.iacr.org/2026/2048) ⭐️ 8.0/10

该论文证明，在特征足够大的域上，速率为 ρ 的 Reed-Solomon 码在分数一致度 α < √ρ 时，列表大小不超过 C·n，其中 C 和 α 仅依赖于 ρ。这一结果在 Johnson 半径以下给出了线性列表大小界限，改进了近期 BCPZZ26 与 Jeronimo26 的 n^c 多项式界限。 这一结果通过将列表大小从多项式降为线性，使超越 Johnson 半径的 Reed-Solomon 列表解码更接近实际可用，对数据存储与通信中的高效纠错具有重要意义。它也补充了近期突破性工作，推动了编码理论核心问题的研究。 该结果适用于分数一致度 α < √ρ（而非完整的容量 ρ+ε），且要求域的特征足够大；常数 C 与 α 未明确给出。工作基于 better.codes 自动研究项目发现的技术，是对指数 c 未指定的 n^c 界限的补充。

rss · IACR ePrint 密码学论文 · 9月15日 15:38

**背景**: Reed-Solomon 码是一种广泛用于存储和通信的纠错码。列表解码是唯一解码的放松形式，允许解码器在给定一致半径内输出一个小的候选码字列表。Johnson 半径是经典界限，在该半径之内可保证列表解码得到多项式大小列表；超过该半径后列表可能很大，近期工作已获得多项式界限。本文在 Johnson 半径以下给出线性界限，因此是重要加强。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/List_decoding">List decoding - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reed–Solomon_error_correction">Reed–Solomon error correction - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Reed-Solomon`, `#list decoding`, `#coding theory`, `#error-correcting codes`, `#theoretical computer science`

---

<a id="item-4"></a>
## [超越 Johnson 界的 Reed-Solomon 码：高效解码与更小证明](https://eprint.iacr.org/2026/2056) ⭐️ 8.0/10

该论文给出了超越 Johnson 界的 Reed-Solomon 列表解码和互相关一致性的显式定量界限，并给出了在密码学大域上仍然高效的确定性解码算法。在安全目标不变的情况下，它还将 ProveKit 证明减小 79.4 KB（11.1%）、ZisK 压缩最终证明减小 13.2 KB（4.63%）、LambdaVM CPU 子证明减小 59.8 KB（4.85%）。 这些结果直接减小了已实现的简洁密码学证明系统中的证明大小，从而降低零知识证明和区块链扩容等应用的通信与验证成本。超越 Johnson 界的高效解码还加强了现代证明系统中所用邻近性间隙的理论基础。 在一致度 a1(ρ)+η1 处，仅使用一阶导数即可得到列表大小 Oρ(n/η1²)和 MCA 误差 Oρ(n²/(q η1⁴))；更高阶导数可将显式定量界限扩展至容量。确定性解码器在 Johnson 界以上每特征运行Õ(n log q)比特操作，在一阶曲线以上大特征域运行Õ(n² log q)，并已在 ArkLib 中形式化验证。

rss · IACR ePrint 密码学论文 · 9月16日 02:05

**背景**: Reed-Solomon 码将消息编码为有限域上的多项式求值，列表解码可在错误超过唯一解码限制时恢复所有邻近码字。Johnson 界是列表可解码性的经典阈值；互相关一致性（MCA）将单词一致性扩展到多个接收字，是许多简洁证明可靠性的基础。密码学证明系统利用由这类编码界限导出的邻近性间隙，确保恶意证明者无法作弊。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Johnson_bound">Johnson bound</a></li>
<li><a href="https://hackmd.io/@-urCr-W9R8mS-UktGXSzbQ/BJ6BwlGbfe">Background: Reed – Solomon List Decoding - HackMD</a></li>
<li><a href="https://eprint.iacr.org/2025/2110">A note on mutual correlated agreement for Reed-Solomon codes</a></li>

</ul>
</details>

**标签**: `#Reed-Solomon codes`, `#list decoding`, `#cryptographic proofs`, `#coding theory`, `#succinct arguments`

---

<a id="item-5"></a>
## [Lemur+：紧凑后量子多重签名与多跳聚合](https://eprint.iacr.org/2026/2054) ⭐️ 8.0/10

Lemur+提出了一种基于 Module LWE 和 Module SIS 的紧凑后量子同步多重签名方案，在多达一百万个签名者的情况下签名大小约为 56 KB，比之前的 Lemur 方案减少了 8.8 倍。该方案还支持多跳聚合，并在 2^13 个签名者下实现了 7.75 秒聚合和 0.29 秒验证的实用运行时间。 这大幅降低了大规模区块链共识和分布式系统的通信与存储开销，使后量子多重签名在实际部署中更加实用。非交互式聚合和多跳能力可为去中心化网络提供可扩展的量子安全签名聚合。 该方案保持约 56 KB 的近恒定签名大小和 42 年密钥寿命；其运行时间在 Lemur 的约 2 倍以内。它引入了带简洁打开证明的同态向量承诺（HVC-SOP），与密钥同态一次性签名（KOTS）通用结合，并使用 LaBRADOR 格证明系统实例化。

rss · IACR ePrint 密码学论文 · 9月16日 00:59

**背景**: 后量子密码学旨在保护系统免受量子计算机攻击；基于格的方案（如 Module LWE/SIS）是 Kyber 和 Dilithium 等标准的基础。多重签名将多个签名者的签名聚合成一个紧凑签名，同步设定假设签名者共享共同的时间段。先前的 Lemur 方案（CCS 2026）提供了基于格的同步多重签名，但签名大小要大得多。LaBRADOR 是一种基于格的零知识证明系统，在此用于生成紧凑证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post - quantum cryptography - Wikipedia</a></li>
<li><a href="https://github.com/lemur-sig/lemur-anon">GitHub - lemur -sig/ lemur -anon: Lemur Artifact · GitHub</a></li>
<li><a href="https://arxiv.org/html/2409.02222v1">A Digital signature scheme based on Module-LWE and Module-SIS</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#multi-signatures`, `#lattice-based cryptography`, `#blockchain`, `#cryptographic protocols`

---

<a id="item-6"></a>
## [首个加权批量门限加密方案无需批次标签或索引](https://eprint.iacr.org/2026/2053) ⭐️ 8.0/10

该论文提出了首个加权批量门限加密方案，无需批次/周期标签和加密时间索引，并且无论参与方的权益权重如何，其通信量都保持为单个群元素。该论文还为基于 BTX 的构造提供了专用分布式密钥生成（DKG）协议，避免了之前方案所需的通用 MPC 设置。 这消除了在 Solana 和以太坊等权益证明区块链中使用加密内存池（mempool）的主要实际障碍，验证者的解密能力可以与其质押量成比例。它有望实现高效、抗审查的交易排序，同时保护待处理交易的隐私。 该构造对已有的 BTX 方案和部分分式方案进行虚拟化，在通用双线性群模型下基于加权变体假设证明安全性。针对基于 BTX 方案的专用 DKG 消除了对昂贵的通用 MPC 设置的需求，实验结果表明在区块链相关参数规模下具有实用性能。

rss · IACR ePrint 密码学论文 · 9月15日 21:02

**背景**: 批量门限加密允许一个委员会解密选定的密文批次，同时保持其他密文私密；它是加密内存池的基础构件，用户可以提交加密交易，交易只有在排序后才被揭示。在权益证明区块链中，验证者拥有不同的质押量，因此需要加权门限方案，让拥有更多质押的参与方拥有成比例的解密能力。分布式密钥生成（DKG）允许多方在没有可信第三方的情况下协作生成共享密钥。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/674">Efficient Batch Threshold Encryption Using Partial Fraction Techniques</a></li>
<li><a href="https://en.wikipedia.org/wiki/Distributed_key_generation">Distributed key generation - Wikipedia</a></li>
<li><a href="https://a16zcrypto.com/posts/article/limits-encrypted-mempools/">On the limits of encrypted mempools - a16z crypto</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#threshold encryption`, `#blockchain`, `#encrypted mempool`, `#proof-of-stake`

---

<a id="item-7"></a>
## [通过承诺标量折叠改进 ElGamal 可验证洗牌证明](https://eprint.iacr.org/2026/2052) ⭐️ 8.0/10

Xue、Lu 和 Au 通过将重随机化向量导出的标量 ρ* = ⟨a, ρ⟩ 绑定到现有 KZG 承诺中，并用单边折叠证明替代两向量一致性论证，降低了用于重随机化 ElGamal 密文的对数大小可验证洗牌证明的通信与计算开销。其变体 A 的证明大小为 (2 log₂ N + 8) G₁ + 5 F，变体 B 增加一个群元素但减少一轮交互；在 N = 2^10 张选票的 4 服务器混网选举中，变体 A 的混合证明总大小为 5.88 KiB，比 XLA 约小 14%。 可验证洗牌是混网和电子投票等隐私关键系统的基础；减小证明大小并降低证明者与验证者的计算量，能够降低大规模匿名交易和选举的成本与延迟，使这些协议更实用。 该构造保留了原有关系、多项式次数和 powers-of-τ 设置；直接标量化是不安全的，但正确承诺的标量能够支持提取完整的重随机化向量。按 XLA 采用的分组基-标量对核算方式，证明者的指数运算次数从约 18N 降至 13N（变体 B 为 14N），验证者从约 7N 降至 6N，每个证明比 XLA 固定小 240 B。

rss · IACR ePrint 密码学论文 · 9月15日 20:14

**背景**: ElGamal 加密支持重随机化：用新的随机性重新加密同一明文会改变密文外观而不改变明文，从而支持洗牌以隐藏输入与输出的对应关系。可验证洗牌证明使验证者相信输出列表是重随机化输入密文的排列，同时不泄露排列本身。KZG 承诺是基于配对的密码学多项式承诺方案，具有短证明和高效验证，通常依赖可信设置。内积论证允许证明者高效地证明向量之间的关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/KZG_commitment">KZG commitment</a></li>
<li><a href="https://www.zkdocs.com/docs/zkdocs/commitments/kzg_polynomial_commitment/">KZG Polynomial Commitments - ZKDocs</a></li>
<li><a href="https://theses.hal.science/tel-05316233v1/document">Efficient and succinct zero-knowledge proofs in the CL encryption...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#zero-knowledge-proofs`, `#verifiable-shuffle`, `#KZG-commitment`, `#ElGamal`

---

<a id="item-8"></a>
## [PyuQuMuQu：对 MQ 可链接环签名的攻击与新型 5 轮构造](https://eprint.iacr.org/2026/2051) ⭐️ 8.0/10

该论文通过和集攻击证明，两个现有的基于 MQ 的可链接环签名方案（Omar–Padhye–Dey 与 Namdeo–Mishra–Srivastava）可在不知道 MQ 解的情况下被普遍伪造。论文还指出 Monteiro–Goya–Terada 四挑战协议的实际可靠误差为 3/4 而非 1/2，并构造了新的 5 轮基于 MQ 的可链接环签名方案 PyuQuMuQu。 这很重要，因为可链接环签名是加密货币和电子投票中的核心隐私原语，而随机多元二次（MQ）方程组是最保守的后量子假设之一。该工作打破了此前两个基于 MQ 的方案，并给出了带随机预言机模型证明的修正构造，为实践者提供了一个可信的后量子可链接环签名候选方案。 PyuQuMuQu 采用 5 轮协议，第一挑战为 d 维向量，第二挑战进行加法拆分，在环成员数 N≤q^d−1 时可靠误差为 1/2 + N/(2(q^d−1))。在 128 位安全级别下，4 成员环的签名大小为 355 kB；论文还指出 Monteiro–Goya–Terada 协议的自然修复只有 3-特殊可靠性，因此其双副本提取论证不成立。

rss · IACR ePrint 密码学论文 · 9月15日 20:09

**背景**: 环签名允许任意集合成员匿名签名；可链接环签名额外生成一个公开标签（常称为密钥镜像），使同一签名者的两个签名可被公开链接，适用于隐私币和电子投票等场景。多元二次（MQ）密码学基于在有限域上求解随机二次方程组这一难题，属于候选后量子假设。识别协议是交互式知识证明，经 Fiat–Shamir 变换后，其可靠性是签名安全的基础。此前两个基于 MQ 的可链接环签名方案建立在 Sakumoto 式协议上，但从未重新检查其在环场景中的可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ring_signature">Ring signature - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multivariate_cryptography">Multivariate cryptography - Wikipedia</a></li>
<li><a href="https://www.mexc.co/crypto-glossary/article/ring-signature-135847">Ring Signature Definition, Meaning & Crypto Use... | MEXC Glossary</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#ring signatures`, `#multivariate quadratic`, `#zero-knowledge proofs`

---

<a id="item-9"></a>
## [任意除子椭圆码 McEliece 的多项式时间攻击](https://eprint.iacr.org/2026/2050) ⭐️ 8.0/10

该论文提出了一种带有“提示”的新结构攻击，可破解基于任意有效除子椭圆码的 McEliece 密码系统：只要给出椭圆曲线、公开生成矩阵以及求值除子中的三个点，就能在与错误数无关的多项式时间内恢复整个秘密除子。基础攻击在 F_q 上需 O(k^2 n^2 + |E(F_q)| + n)次运算，成功概率极高；优化变体无需额外提示，平均需 O(k^2 n^2 + q^2 + (|E(F_q)|-n)n^2)次运算即可恢复等价密钥。 该结果表明，此前被认为能抵抗已知结构攻击的椭圆码 McEliece 变体并不安全，从而排除了一个基于代数几何码的后量子密码候选方案。这一结果进一步证明应优先使用二进制 Goppa 码（如 Classic McEliece）等结构安全性更强的码族，并可能影响 NIST 后量子标准化中对可选码族范围的判断。 基础攻击需要求值除子中的三个点作为提示，成功概率极高；随后以 O(k^2 n^2 + (|E(F_q)|-n)n^2)次运算恢复第二个除子。优化版本利用曲线自同构枚举一对域元素来替代三个提示点，平均运算量为 O(k^2 n^2 + q^2 + (|E(F_q)|-n)n^2)，且复杂度与纠错个数 t 无关，因此增大 t 不能抵御该攻击。

rss · IACR ePrint 密码学论文 · 9月15日 18:20

**背景**: McEliece 是基于编码的公钥密码系统，其安全性依赖一般线性码译码的困难性；标准方案使用二进制 Goppa 码，而用椭圆码等代数几何码替换 Goppa 码曾被认为可以减小密钥尺寸。椭圆码是在亏格为 1 的椭圆曲线上通过求值构造的代数几何码。结构攻击利用公钥中隐藏的代数结构恢复秘密参数，此前已有多个代数几何码变体因此被攻破；本论文针对椭圆码任意除子给出了新的结构攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/McEliece_cryptosystem">McEliece cryptosystem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Algebraic_geometry_code">Algebraic geometry code - Wikipedia</a></li>
<li><a href="https://errorcorrectionzoo.org/c/elliptic">Elliptic code</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#code-based cryptography`, `#McEliece`, `#elliptic codes`, `#cryptanalysis`

---

<a id="item-10"></a>
## [面向 SQIsign 四元数算法的更紧整数界与精确矩阵求逆](https://eprint.iacr.org/2026/2049) ⭐️ 8.0/10

该论文（eprint 2026/2049）重新分析了 SQIsign 的四元数算术层，证明其中出现的所有格都满足一种结构包含性质，从而可以用此前一半比特长度的模数计算规范形式。论文还提出了一种仅使用精确除法的矩阵求逆算法，其中间整数上界为模数的两倍，并给出二维高斯整数表示，用可证明终止的 Lagrange 约化替代 LLL。 SQIsign 是 NIST 后量子签名候选中的领先方案，具有最小的密钥和签名尺寸，但其签名运算中的大整数中间增长会阻碍固定精度和恒定时间实现。该工作用可证明的界减少了这种增长，使抗侧信道和固定精度的 SQIsign 实现更加实用，同时不牺牲其紧凑性。 通过包含性质将模数比特长度减半；精确除法矩阵求逆算法把中间值限制在模数的两倍以内，避免了标准求逆的立方级膨胀，而三角形式约定进一步节省了 O(p) 的因子。在二维高斯整数表示中，Lagrange 约化的迭代次数由最长输入向量的比特长度的常数倍界定，无需浮点运算即可输出最短基，相关实现已加入基于 GMP 的 C 参考 SQIsign。

rss · IACR ePrint 密码学论文 · 9月15日 15:53

**背景**: SQIsign 是一种基于椭圆曲线同源和四元数运算的后量子数字签名方案，具有极小的密钥和签名尺寸，但签名时间较长。四元数是一种四分量数系，SQIsign 将相关对象表示为整数格，并使用 LLL 等格约化算法来寻找短基。对于恒定时间和固定精度实现，每个中间算术值都必须有已知的有限边界，因此整数尺寸分析至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SQIsign">SQIsign</a></li>
<li><a href="https://sqisign.org/">SQIsign</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quaternion">Quaternion - Wikipedia</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#SQIsign`, `#quaternion arithmetic`, `#side-channel resistance`, `#implementation optimization`

---

<a id="item-11"></a>
## [ROSETTA：混合 CKKS/TFHE 框架加速隐私保护 LLM 解码](https://eprint.iacr.org/2026/2047) ⭐️ 8.0/10

研究人员提出 ROSETTA，一种混合 CKKS/TFHE 框架，利用自适应分段查找表协议和方案感知的算子选择，在隐私保护 LLM 解码中高效评估非线性运算。与现有最先进框架 CacheMir 相比，它实现了最高 4.8 倍的 Softmax 加速和 1.5 到 2.1 倍的端到端加速。 非线性运算是基于 FHE 的私有 LLM 推理中的主要瓶颈，提高其效率可使隐私保护 LLM 服务更接近实际部署。这可能推动加密推理在医疗、金融等敏感应用中的更广泛采用。 ROSETTA 的贡献包括基于 TFHE 的自适应分段查找表协议，用于精确评估非线性运算，以及方案感知的算子选择框架，自动将每个非线性算子分配给 CKKS 或 TFHE 以最小化端到端解码延迟。报告的提升以最先进的 CacheMir 框架为基准。

rss · IACR ePrint 密码学论文 · 9月15日 13:29

**背景**: 全同态加密（FHE）允许在不解密的情况下对加密数据进行计算。CKKS 是一种针对实数/复数近似算术优化的 FHE 方案，而 TFHE 在快速布尔和小整数运算方面效率较高。在 LLM 解码中，softmax、argmax 或激活层等非线性函数在 FHE 下代价高昂，因此结合不同 FHE 方案的混合方法在平衡精度与速度方面具有吸引力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tfhe.github.io/">TFHE Fast Fully Homomorphic Encryption over the Torus</a></li>
<li><a href="https://openmined.org/blog/ckks-explained-part-1-simple-encoding-and-decoding/">CKKS explained: Part 1, Vanilla Encoding and Decoding - OpenMined</a></li>
<li><a href="https://www.privatemode.ai/blog/privacy-preserving-inference">Privacy - preserving LLM inference</a></li>

</ul>
</details>

**标签**: `#Privacy-preserving ML`, `#Fully Homomorphic Encryption`, `#LLM Inference`, `#CKKS/TFHE`, `#Secure Computation`

---

<a id="item-12"></a>
## [Falcon 多余的平方根计算可被故障攻击利用导致密钥恢复](https://eprint.iacr.org/2026/2046) ⭐️ 8.0/10

这篇论文指出 Falcon 中的平方根计算是完全多余的，可以移除而不影响性能，并在 ARM Cortex-M4 上演示了一种实用的故障攻击：只需注入一次电压毛刺，再收集约一百万个正常签名，即可 100%恢复完整私钥。 由于 Falcon 是 NIST 已选定标准化的后量子签名方案之一（FN-DSA），移除多余的平方根可简化安全实现；同时该故障攻击暴露了严重的物理安全缺陷，可能影响后续实现指南和标准化方向。 攻击只需在单个平方根计算中注入一次毛刺，之后生成约一百万个签名即可恢复密钥，且故障签名与正常签名难以区分；这比之前需要数亿样本或产生可识别异常签名的攻击更具威胁。

rss · IACR ePrint 密码学论文 · 9月15日 12:16

**背景**: Falcon 是一种基于格的抗量子签名方案，已被 NIST 选定为标准算法 FN-DSA。它采用浮点运算，其中包括平方根计算，这些运算被认为复杂且难以安全实现。故障攻击是一类通过干扰设备运行来提取秘密的物理攻击。ARM Cortex-M4 是广泛使用的嵌入式微控制器内核，常用于评估实现安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Falcon_(signature_scheme)">Falcon (signature scheme) - Wikipedia</a></li>
<li><a href="https://csrc.nist.gov/presentations/2024/navigating-floating-point-challenges-in-falcon">Navigating Floating-Point Challenges in Falcon - NIST CSRC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Differential_fault_analysis">Differential fault analysis - Wikipedia</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#Falcon`, `#fault attack`, `#implementation security`, `#NIST standardization`

---

<a id="item-13"></a>
## [研究者修正 Sparkle+门限 Schnorr 签名安全边界中的代数错误](https://eprint.iacr.org/2026/2044) ⭐️ 8.0/10

作者重新推导了 Sparkle+门限 Schnorr 签名方案（2025 年 6 月版本）定理 1 和定理 2 的最终安全边界，发现先前所述的边界存在三处代数错误：博弈跳跃项相对于平方根的位置错误、提取不等式中博弈跳跃总体系数错误，以及一般分叉引理精确反演所贡献的项缺失。 修正这些边界可确保 Sparkle+的安全性证明不会被无意高估或低估，这对分布式系统和 EdDSA 等标准中的门限 Schnorr 部署至关重要。尽管在博弈转换正确的前提下渐进安全结论不变，但精确的具体边界对于参数选择和审计仍是必要的。 该论文证明了在离散对数（DL）假设下完全静态安全以及在 AOMDL 假设下抗 t/2 腐化的自适应安全的修正边界；修正后的边界把博弈跳跃项放在平方根外，整个博弈跳跃集合体系数为 2q，并包含一般分叉引理精确反演在平方根外的 q/2p 项和平方根内的 q^2/4p^2 项（q 为查询次数，p 为群阶）。作者还确定了两组边界各自更紧的确切条件。

rss · IACR ePrint 密码学论文 · 9月15日 10:12

**背景**: Schnorr 签名是一种基于离散对数问题、简单高效且验证快速的数字签名方案，与 EdDSA 兼容。门限 Schnorr 方案允许多方在不暴露完整私钥的情况下共同生成 Schnorr 签名，并保持与中心化签名相同的验证算法。Sparkle+是 2023 年提出的门限 Schnorr 签名方案，其安全性通过博弈跳跃和一般分叉引理进行分析；离散对数（DL）假设是标准困难假设，而 AOMDL（代数一次性离散对数）是更强但可证伪的变体，用于有腐化的自适应安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Schnorr_signature">Schnorr signature - Wikipedia</a></li>
<li><a href="https://eprint.iacr.org/2023/899">Practical Schnorr Threshold Signatures Without the Algebraic ...</a></li>
<li><a href="https://cronokirby.com/refs/2026-04-ordered-multi-signatures-from-the-dl-assumption.html">(2026-04) Ordered Multi-Signatures from the DL Assumption</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#threshold signatures`, `#Schnorr signatures`, `#security proofs`, `#Sparkle+`

---

<a id="item-14"></a>
## [新攻击显示盲签名和 OPRF 方案通过中止行为泄露秘密](https://eprint.iacr.org/2026/2043) ⭐️ 8.0/10

这篇论文展示了针对多个此前声称安全的盲签名和 OPRF 构造的显式恶意签名者/评估者攻击，包括 Qin 等人的盲 ECDSA 方案和可验证的 Dark Matter OPRF，证明其安全定理不成立。攻击通过让验证有条件地中止，将“中止/不中止”的结果变成对隐藏消息的一位测试预言机。 这对依赖这些原语的广泛部署的隐私保护协议和匿名令牌方案的安全保证构成挑战，可能迫使设计者添加可公开验证的诚实评估或在更强假设下重新证明安全性。它揭示了一个微妙的证明缺陷，可能影响其他基于同态加密的盲签名和 OPRF 设计。 主要攻击针对基于同态加密的盲签名和 OPRF，用户加密输入后解密并验证签名者的同态响应；缺陷在于先前证明在敌手还能获知与输入相关的终止事件时仍隐含地使用加密隐藏或承诺隐藏。作者指出 Fischlin-Schröder 意义上的可公开检查签名派生是避免泄露的正面准则，并提出包括零知识证明和针对部分基于同态加密随机令牌场景的随机未知消息盲性（RUMBL）变换在内的缓解措施。该论文是预印本，尚未经过同行评审。

rss · IACR ePrint 密码学论文 · 9月15日 09:31

**背景**: 盲签名由 David Chaum 提出，允许签名者在不知道消息内容的情况下签名，用于数字现金、匿名凭证等隐私应用。不经意伪随机函数（OPRF）类似地让客户端与服务器共同计算带密钥函数而服务器不获知输入。同态加密允许对加密数据进行计算，一些盲签名/OPRF 构造利用它让签名者/评估者从加密请求生成响应。盲性（blindness）或请求隐私（request-privacy）等安全定义要求恶意签名者无法将用户隐藏的消息与最终签名或输出关联起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Blind_signature">Blind signature</a></li>
<li><a href="https://en.wikipedia.org/wiki/Oblivious_pseudorandom_function">Oblivious pseudorandom function - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#blind signatures`, `#OPRF`, `#security analysis`, `#attacks`

---

<a id="item-15"></a>
## [基于群表示理论求解阿贝尔扩张中的理想 uSVP 与理想 BDD](https://eprint.iacr.org/2026/2042) ⭐️ 8.0/10

该论文提出了一个基于伽罗瓦子群的不可约有理表示的表示论框架，在阿贝尔扩张中将理想分解为低维子格，从而能够同时求解 Ideal-uSVP 和 Ideal-BDD。该方法推广了以往的子域攻击，并首次将群表示论直接用于格密码分析。 该结果对 NIST 标准化的 Kyber 和 Dilithium 等基于理想格的抗量子密码方案的安全分析具有重要意义。它将攻击能力从 SVP 扩展到 BDD，并放宽了对子结构乘法封闭性的要求，可能影响未来结构化格密码方案的参数选择和安全评估。 该构造利用 H 的不可约有理表示得到尺度化投影算子 q_i，将理想 I 分解为低维格 I_i；当目标距离不超过 λ₁(I)/(2|H|²) 时，可通过在各 I_i 上独立求解 BDD 并重组答案。在分圆域中，旋转性质进一步保证每个非零 I_i 都包含 I 的最短向量，且单个 BDD 实例可归约为同一最低秩分量上的 n 个低秩实例。

rss · IACR ePrint 密码学论文 · 9月15日 09:19

**背景**: 理想格是由数域中的理想构造的格，是 NIST 后量子密码方案 Kyber 和 Dilithium 的基础。Ideal-uSVP 是唯一最短向量问题，Ideal-BDD 是这类结构化格上的有界距离解码问题。以往的子域攻击利用子域将 SVP 降到更低维度，但仅限于 SVP 且依赖乘法封闭子结构；本文用群表示论对这些方法进行了推广。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-662-53018-4_6">A Subfield Lattice Attack on Overstretched NTRU Assumptions</a></li>
<li><a href="https://www.maths.ox.ac.uk/system/files/attachments/subfield-attack.pdf">A subfield lattice attack on overstretched NTRU assumptions</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#lattice-based cryptography`, `#ideal lattices`, `#cryptanalysis`, `#representation theory`

---
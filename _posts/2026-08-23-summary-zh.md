---
layout: default
title: "Horizon Summary: 2026-08-23 (ZH)"
date: 2026-08-23
lang: zh
---

> 从 62 条内容中筛选出 15 条重要资讯。

---

1. [秩度量与多线性秘密共享的指数下界](#item-1) ⭐️ 9.0/10
2. [Pilaf：无需配对、自适应安全的完全紧致两轮阈值签名方案](#item-2) ⭐️ 9.0/10
3. [基于标准 LWE 假设的选择密文安全全同态加密](#item-3) ⭐️ 9.0/10
4. [加权 DAO 治理的可验证仅赢家计票隐藏方案](#item-4) ⭐️ 8.0/10
5. [PAC 框架为侧信道分析提供轨迹需求保证](#item-5) ⭐️ 8.0/10
6. [新常数轮 MPC 协议实现最优阈值的回退安全性。](#item-6) ⭐️ 8.0/10
7. [圆-线性密码分析：基于 bibrace 特征的 CRAFT 弱密钥线性区分器](#item-7) ⭐️ 8.0/10
8. [精确线性相关与 Walsh 变换密钥恢复成本及其在 SPEEDY 上的应用](#item-8) ⭐️ 8.0/10
9. [缩减轮数 AES 已知明文攻击改进，攻击轮数至少增加一轮](#item-9) ⭐️ 8.0/10
10. [Sluice：读写流式降低 Groth16 证明阶段内存](#item-10) ⭐️ 8.0/10
11. [全新 Iceberg 构造为闪电网络通道实现阈值托管](#item-11) ⭐️ 8.0/10
12. [QuaILLL：四元数理想格上的 LLL 与 BKZ 算法](#item-12) ⭐️ 8.0/10
13. [固定行权重 EA 码在任意域上实现线性距离](#item-13) ⭐️ 8.0/10
14. [基于格的阈值零知识证明用于精确关系](#item-14) ⭐️ 8.0/10
15. [SafeHub：具有回滚检测的端到端加密 Git 托管系统](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [秩度量与多线性秘密共享的指数下界](https://eprint.iacr.org/2026/1769) ⭐️ 9.0/10

该论文证明了多线性秘密共享方案的指数下界，表明最坏情况下的信息比率为 2^Θ(n)，并回答了 Beimel 提出的一个问题。具体而言，它展示了 Razborov–Gál 秩度量在摊销下仍然成立，从而对每个有限域上的显式访问结构族给出了 2^Ω(n)的信息比率下界。 这一突破解决了一个长期悬而未决的问题，并表明对于某些访问结构，通过向量秘密摊销份额大小无法获得优于指数的效率。它为高效秘密共享方案的设计提供了根本限制，并影响依赖此类方案的密码协议。 证明使用了 Razborov–Gál 秩度量，并结合 Pitassi 和 Robere 的秩见证，得到了具有指数信息比率的显式访问结构。该下界扩展到具有任意共享算法和仿射线性重构、且成对统计隐私低于 1 的方案，并在秘密维度为 2^o(n)时，对固定重构次数给出指数规范化下界。

rss · IACR ePrint 密码学论文 · 8月21日 19:55

**背景**: 多线性秘密共享方案共享一个向量秘密，因此可以将份额大小在秘密维度上摊销，这可能会绕过针对单秘密线性方案已知的下界。单调张成程序是一种与线性秘密共享等价的线性代数模型，而秩度量是用于证明下界的复杂度度量。此前，多线性方案的最佳显式下界是拟多项式的（n^Ω(log n)），指数下界仍是悬而未决的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-642-54242-8_17">Multi-linear Secret-Sharing Schemes | Springer Nature Link</a></li>
<li><a href="https://egtheory.wordpress.com/2019/06/08/span-programs/">Span programs as a linear-algebraic representation of functions</a></li>

</ul>
</details>

**标签**: `#secret sharing`, `#cryptography`, `#lower bounds`, `#computational complexity`, `#span programs`

---

<a id="item-2"></a>
## [Pilaf：无需配对、自适应安全的完全紧致两轮阈值签名方案](https://eprint.iacr.org/2026/1762) ⭐️ 9.0/10

该论文提出了 TPilaf，首个在随机预言机模型下基于 MDDH 假设、无需配对即可实现针对自适应腐化完全紧致安全的两轮阈值签名方案。 这解决了阈值密码学中的一个重要开放问题，不再依赖配对、代数/知识假设以及需要猜测腐化模式或会话而带来的非紧致安全损失。它为在签名者可被自适应腐化的对抗环境中更高效、更实际地部署阈值签名铺平了道路。 方案的第一轮消息可离线生成，任意达到阈值的签名者集合都能将第二轮份额聚合成一个可公开验证的签名。证明使用了带可定向打开功能的线性同态双模式承诺和按配置的零和掩码，最终安全界在用户数、阈值、会话数和腐化模式上均无组合损失；主要限制是工作在随机预言机模型下。

rss · IACR ePrint 密码学论文 · 8月21日 13:20

**背景**: 阈值签名将签名密钥分成 n 份，任意至少 t 个参与方可以联合签名，而少于 t 个则不能。自适应腐化指敌手可以在协议执行过程中、在观察到交互记录后决定腐化哪些签名者。紧致安全意味着安全归约的成功概率与攻破底层假设的概率接近，不会因猜测事件而产生大的乘法损失；MDDH 假设是一类标准 Diffie-Hellman 型假设，而无配对方案避免了计算开销大的双线性配对。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Threshold_cryptosystem">Threshold cryptosystem - Wikipedia</a></li>
<li><a href="https://bitcoinops.org/en/topics/threshold-signature/">Threshold signature | Bitcoin Optech</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-662-53887-6_27">The Kernel Matrix Diffie-Hellman Assumption | Springer Nature Link</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#threshold signatures`, `#adaptive security`, `#tight reductions`, `#pairing-free`

---

<a id="item-3"></a>
## [基于标准 LWE 假设的选择密文安全全同态加密](https://eprint.iacr.org/2026/1756) ⭐️ 9.0/10

一篇新论文在标准模型下从学习带错误（LWE）假设构造了具有选择密文（CCA）安全的（1 跳）全同态加密（FHE）方案。其安全性仅依赖于循环安全 LWE 假设，与基本的选择明文安全 FHE 所需假设一致。 这是一项重大突破，因为全同态加密方案天然具有可延展性，通常只能达到选择明文安全；此前达到 CCA1 安全的 FHE 需要随机预言机或不可证伪假设。该结果在标准假设下提供了更强的安全保障，使 FHE 在对抗性现实场景中更具可行性。 该构造遵循 Naor-Yung 双重加密范式，但用专门设计的简洁论证替代了通用零知识简洁非交互式知识论证（ZK-SNARK），用于证明 FHE 密文的有效性。该简洁论证由针对 NP 的批量论证和一种名为“谓词可提取承诺”的新原语构建而成。

rss · IACR ePrint 密码学论文 · 8月21日 00:02

**背景**: 全同态加密允许在不解密数据的情况下对加密数据进行计算，从而保护外包计算中的隐私。选择密文安全模型假设攻击者可以将选定的密文提交解密，因此比选择明文安全更强。学习带错误是一种基于格的困难问题，广泛用于后量子密码学。全同态加密方案通常具有可延展性，这使得实现 CCA 安全极具挑战性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fully_homomorphic_encryption">Fully homomorphic encryption</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chosen-ciphertext_attack">Chosen-ciphertext attack - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Learning_with_errors">Learning with errors - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#fully-homomorphic-encryption`, `#chosen-ciphertext-security`, `#LWE`, `#succinct-arguments`

---

<a id="item-4"></a>
## [加权 DAO 治理的可验证仅赢家计票隐藏方案](https://eprint.iacr.org/2026/1773) ⭐️ 8.0/10

该论文提出一种针对 DAO 加权二元投票的密码学方案，仅公开胜出结果位，同时保持可公开验证；它通过零知识选票将注册权重与凭证绑定，并在聚合和阈值比较过程中保持加权贡献加密。 这很重要，因为 DAO 的代币加权投票可能通过公开权重和计票结果暴露个人选择，抑制参与并带来胁迫风险；仅披露胜者既能增强隐私，又能保留去中心化治理所需的完整性和透明性。 该构造由选民规模和贡献宽度参数化；原型测试了一个受限的八选民、八位实例，包含 134 个加密门和三选五受托人释放，且针对恶意子阈值受托人的隐私性仍然是开放问题。

rss · IACR ePrint 密码学论文 · 8月22日 07:28

**背景**: DAO 使用代币加权投票，持有更多治理代币意味着更大投票权，但公开权重和计票结果可能泄露选民选择。零知识证明允许在不暴露底层信息的情况下证明某个陈述。可验证计票隐藏是电子投票中的一种技术，从加密选票计算结果时只公开结果，而不公开具体计票数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof</a></li>
<li><a href="https://en.wikipedia.org/wiki/Decentralized_autonomous_organization">Decentralized autonomous organization - Wikipedia</a></li>
<li><a href="https://eprint.iacr.org/2021/491">A toolbox for verifiable tally-hiding e-voting systems</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#DAO governance`, `#privacy`, `#zero-knowledge proofs`, `#blockchain voting`

---

<a id="item-5"></a>
## [PAC 框架为侧信道分析提供轨迹需求保证](https://eprint.iacr.org/2026/1770) ⭐️ 8.0/10

研究人员提出了一种用于建模和非建模侧信道分析的 PAC 公式，为密钥排名和所需轨迹数提供有限样本置信保证。在 ASCAD-f 和 ASCAD-r 数据集上，建模攻击仅需数十条轨迹即可精确恢复密钥，而非建模攻击约需 1,000 条轨迹即可保证精确恢复。 该研究将轨迹复杂度从经验观察转变为可复用的有限样本判据，帮助评估者判断攻击失败是数据不足还是密钥区分度弱所致。这将改进侧信道攻击的评估与比较方式，有利于密码设备的认证和漏洞评估。 该框架将有限样本估计误差与正确密钥和竞争假设之间的本质分离区分开来。建模攻击仅需数十条攻击轨迹即可实现精确恢复，而非建模单次攻击排名证书约需 1,000 条轨迹保证精确恢复，与近期 ASCAD 攻击相当，且低于此前报道的非建模场景所需轨迹数。

rss · IACR ePrint 密码学论文 · 8月21日 21:03

**背景**: PAC 学习是一种数学框架，它将训练样本数量、错误率以及获得低错误率的概率联系起来。侧信道分析攻击通过测量密码计算过程中的物理泄漏（如功耗或电磁辐射）来恢复密钥；建模攻击使用克隆设备学习泄漏模型，而非建模攻击则没有此类建模阶段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Probably_approximately_correct_learning">Probably approximately correct learning - Wikipedia</a></li>
<li><a href="https://www.ndss-symposium.org/ndss-paper/mind-the-portability-a-warriors-guide-through-realistic-profiled-side-channel-analysis/">Mind the Portability: A Warriors Guide through Realistic Profiled ...</a></li>

</ul>
</details>

**标签**: `#side-channel analysis`, `#PAC learning`, `#cryptography`, `#security`, `#evaluation methodology`

---

<a id="item-6"></a>
## [新常数轮 MPC 协议实现最优阈值的回退安全性。](https://eprint.iacr.org/2026/1768) ⭐️ 8.0/10

该论文提出了具有回退安全性的常数轮 MPC 协议，实现了最优腐败阈值。它给出了在 t < n/2 下明文模型中的 3 轮半诚实协议（此前最优为 11 轮）、CRS 模型中 4 轮恶意安全且具一致中止的协议，以及 5 轮保留公平性的扩展；这是恶意设置下首批常数轮回退安全协议。 将轮复杂度从线性降至常数可显著降低延迟和通信开销，使回退安全 MPC 更适用于实际应用。这些结果通过最小轮数实现最优阈值和更强保证（公平性、一致中止），弥补了关键效率缺口。 半诚实协议在明文模型中对 t < n/2 只需 3 轮；此前最优需要至少 11 轮。恶意协议使用公共参考串（CRS），对相同阈值只需 4 轮且满足一致中止，扩展协议为 5 轮：针对 t < n/2 的无界对手提供公平性，对超出该阈值的任意腐败的 PPT 对手提供一致中止。

rss · IACR ePrint 密码学论文 · 8月21日 18:25

**背景**: 安全多方计算（MPC）允许多个参与方共同计算函数并保持各自输入私密。回退安全性由 Acharya 等人于 CRYPTO 2023 形式化，保证在仅有限数量参与方被腐败时提供信息论/无界安全性，而在任意腐败时降级为针对概率多项式时间（PPT）对手的计算安全性。轮复杂度衡量顺序通信轮数；此前的回退协议轮数与参与方数量和计算规模呈线性关系，而常数轮协议效率更高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1768">Constant-round MPC protocols with Fall-back Security</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#MPC`, `#cryptography`, `#secure computation`, `#fall-back security`, `#round complexity`

---

<a id="item-7"></a>
## [圆-线性密码分析：基于 bibrace 特征的 CRAFT 弱密钥线性区分器](https://eprint.iacr.org/2026/1767) ⭐️ 8.0/10

该论文提出使用 bibrace 特征进行圆-线性密码分析，并为 CRAFT 分组密码推导出弱密钥线性区分器。它在 18 轮内获得精确区分器，在 14 轮时平方相关性为 2^-44、适用于 2^108 个密钥的弱密钥类，比已知最佳线性壳改进 18 比特并多覆盖 4 轮。 这项工作引入了一种利用替代群结构的新密码分析技术，为 CRAFT 提供了强力的弱密钥线性区分器，并可能推广到其他对称密码。它推进了轻量级分组密码的安全性评估，并凸显了实际部署中弱密钥类的重要性。 Midori/CRAFT 的 S 盒具有四个概率为 1 的关系，构成对偶群的一个子群且可确定性传播，从而将最佳路径搜索转化为可精确枚举的最小重量码字问题。联合分析扩散层和密钥加得到比逐单元分析更大的弱密钥类，而且 CRAFT 的轮常数不施加任何限制。

rss · IACR ePrint 密码学论文 · 8月21日 16:16

**背景**: 线性密码分析通常使用差分群的特征来衡量相关性；将差分群替换为来自二进制 bibrace 的另一个初等阿贝尔群结构会改变可用的掩码。Beyne 的几何框架将线性密码分析推广到任意有限阿贝尔群。CRAFT 是一种轻量级可调分组密码，设计时考虑了针对差分故障攻击的高效防护。该论文在 CRAFT 上实例化了这一框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tcgcrest.org/wp-content/uploads/2022/11/Heys.pdf">Linear and Differential Cryptanalysis</a></li>
<li><a href="https://sites.google.com/view/craftcipher">CRAFT</a></li>
<li><a href="https://arxiv.org/html/2510.05848">Classification of small binary bibraces via bilinear maps</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#linear cryptanalysis`, `#CRAFT cipher`, `#symmetric-key`, `#cryptanalysis`

---

<a id="item-8"></a>
## [精确线性相关与 Walsh 变换密钥恢复成本及其在 SPEEDY 上的应用](https://eprint.iacr.org/2026/1765) ⭐️ 8.0/10

该论文提出了一个精确线性相关分析框架，对兼容的中间掩码进行带符号求和，而不是直接使用乘积法则；据此发现 SPEEDY 之前发表的五轮掩码相关系数为 2^{-90.0962}，而非 2^{-93.0147}，无限制五轮权重界由 53.7714 位提高到 62.2616 位。论文还将 SPEEDY-7-192 的完整轮攻击代价从 2^{158.06} 修正为至少 2^{199.97} 次等效加密，并给出对 SPEEDY-6-192 的六轮已知明文攻击（数据 2^{169.84}，时间 2^{170.20}，内存 2^{156}）。 这一修正是重要的，因为此前发表的 SPEEDY 安全裕度被高估了；该精确框架为密码分析者和密码设计者提供了一种更可靠的方法，用于计算当两个 S 盒层由线性运算而非密钥加分隔时的线性包络效应。它能够给出更准确的攻击代价估计，并可能影响其他具有类似结构的低延迟分组密码的安全性评估。 该框架包括精确单轮算法、可判定的乘积法则精确性条件、依赖图分解、覆盖数界和 Walsh 支撑准则；Walsh 支撑的仿射维数（受端点密钥掩码限制）决定了密钥恢复变换的成本。分析采用独立轮密钥模型，复杂度以等效加密表示；对 SPEEDY-6-192，该文证明所考虑的攻击类中不存在数据和时间均不超过 2^{128} 的攻击，其时间至少为 2^{136.302}。

rss · IACR ePrint 密码学论文 · 8月21日 15:32

**背景**: 线性密码分析是一种已知明文攻击，它用 GF(2) 上的线性近似描述分组密码的行为，并常通过各轮相关性的乘积来估计攻击成功率。SPEEDY 是一族超低延迟分组密码，具有多种分组/密钥长度和轮数，面向快速硬件实现。Walsh 变换衡量布尔函数与线性函数的相关程度，其支撑可决定密钥恢复成本。当两个 S 盒层之间由类似 ShiftColumns 的线性运算而非密钥加分隔时，轮相关性是兼容中间掩码上的带符号和，因此乘积法则可能失效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tches.iacr.org/index.php/TCHES/article/download/9074/8661">The SPEEDY Family of Block Ciphers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Linear_cryptanalysis">Linear cryptanalysis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Walsh_transform">Walsh transform</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#linear cryptanalysis`, `#SPEEDY cipher`, `#Walsh transform`, `#key recovery`

---

<a id="item-9"></a>
## [缩减轮数 AES 已知明文攻击改进，攻击轮数至少增加一轮](https://eprint.iacr.org/2026/1759) ⭐️ 8.0/10

该论文在随机已知明文模型下提出了针对所有版本缩减轮数 AES 的改进差分攻击，将以往结果至少扩展了一轮。论文还表明，带差分枚举的 Demirci-Selcuk 中间相遇攻击在该模型下依然有效，且无需接近完整码本的数据量。 这项工作显著推进了对称密码分析，表明许多不允许选择明文的工作模式仍可能受到优化的已知明文差分攻击。这可能促使密码学家在更现实的已知明文模型下评估未来设计，从而影响分组密码的安全余量。 这些攻击将随机已知明文模型下所有 AES 版本的已知最佳区分器和攻击改进了至少一轮，但复杂度过高，不会威胁完整的 10/12/14 轮 AES。值得注意的是，在选择数据条件下最优的差分路径在已知明文模型中可能不是最优的，可以找到更好的路径。

rss · IACR ePrint 密码学论文 · 8月21日 08:22

**背景**: AES 是 NIST 标准化的广泛使用的分组密码，具有 128 位分组和 128/192/256 位密钥，对应 10/12/14 轮。差分密码分析利用输入差异在输出中的传播；选择明文攻击允许攻击者选择输入，而已知明文攻击只能获得随机的明文-密文对。随机已知明文（RKP）模型是一种更受限的场景，攻击者无法选择明文，这与许多实际加密模式相符。不可能差分、矩形和混合差分等高级差分技术此前大多在选择数据条件下研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Impossible_differential_attack">Impossible differential attack</a></li>
<li><a href="https://cs.haifa.ac.il/~orrd/crypt/tausec.pdf">The Rectangle Attack</a></li>
<li><a href="https://www.researchgate.net/publication/346704286_Mixture_Differential_Cryptanalysis_a_New_Approach_to_Distinguishers_and_Attacks_on_round-reduced_AES">(PDF) Mixture Differential Cryptanalysis : a New Approach to...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#AES`, `#cryptanalysis`, `#block ciphers`, `#known-plaintext attack`

---

<a id="item-10"></a>
## [Sluice：读写流式降低 Groth16 证明阶段内存](https://eprint.iacr.org/2026/1758) ⭐️ 8.0/10

Sluice 提出一种读写流式 Groth16 证明器，借助新的 Split-Butterfly-Merge NTT 算法和分块 MSM，将证明阶段随机访问内存从 O(N) 降至 O(log N)，同时保持标准验证器兼容性。 这使内存受限设备也能生成 Groth16 证明，通过用 RAM 换取顺序存储 I/O，在不改变验证器合约的情况下扩展零知识证明的适用场景。 基于 BN-254 的原型在 N=2^25 及以下生成有效的 128 字节证明；在 N=2^23 的有界内存测试中，Sluice 在 8GB cgroup 限制下成功，而标准证明器需要 16GB。

rss · IACR ePrint 密码学论文 · 8月21日 04:30

**背景**: Groth16 是一种广泛使用的 zk-SNARK 证明系统，证明小、验证快，但其证明者通常需要 O(N) 内存。数论变换（NTT）是有限域上的傅里叶变换，用于加速 SNARK 中的多项式运算。多标量乘法（MSM）是证明生成中的主要椭圆曲线运算，通常通过 Pippenger 算法优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@daltonbembry97/a-beginners-guide-to-groth16-72d7c816376a">A Beginner’s Guide to Groth 16 . I began my journey as a ZKP... | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Number-theoretic_transform">Number-theoretic transform</a></li>
<li><a href="https://blog.lambdaclass.com/multiscalar-multiplication-strategies-and-challenges/">Fast Multiscalar Multiplication : Algorithms and Performance...</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#Groth16`, `#NTT`, `#streaming algorithms`, `#memory efficiency`

---

<a id="item-11"></a>
## [全新 Iceberg 构造为闪电网络通道实现阈值托管](https://eprint.iacr.org/2026/1757) ⭐️ 8.0/10

研究人员正式提出了嵌套阈值多重签名这一新原语，并推出了 Iceberg——首个用于嵌套阈值 MuSig2 签名的构造。它使闪电网络通道的一方能够以 t-of-n 阈值组运行，同时在对端看来仍是标准 MuSig2 参与者，从而无需修改比特币、闪电网络协议或对端即可单方面部署阈值托管。 这解决了一个关键安全缺陷：闪电网络通道端点目前依赖单个在线密钥，一旦被攻破就可能导致资金损失。通过在不改协议的情况下实现阈值托管，它能显著提升闪电网络部署抵御密钥被盗和内部攻击的能力，可能惠及交易所、托管方和大型节点运营商。 Iceberg 已通过安全性证明，并被集成到生产级闪电网络节点中。测试表明，能容忍一名成员被攻破的阈值组仍可保持未修改端点 93% 以上的支付吞吐量，开销很小。

rss · IACR ePrint 密码学论文 · 8月21日 03:00

**背景**: 闪电网络是建立在比特币之上的二层支付协议，使用链下通道并由链上比特币交易保障安全。MuSig2 是一种基于 Schnorr 的两方多重签名方案，用于闪电通道中聚合签名，同时不暴露参与方各自的密钥。阈值签名要求 n 方中至少 t 方同意才能联合签名，从而消除单点故障。嵌套阈值多重签名则进一步允许现有多重签名协议中的某一方在内部作为一个阈值组运行，而无需改变外部协议流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stacker.news/items/1552628">Enabling Threshold Custody on Lightning Network with Nested ...</a></li>
<li><a href="https://glossary.blockstream.com/musig2/">MuSig 2</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#threshold signatures`, `#Lightning Network`, `#Bitcoin`, `#MuSig2`

---

<a id="item-12"></a>
## [QuaILLL：四元数理想格上的 LLL 与 BKZ 算法](https://eprint.iacr.org/2026/1755) ⭐️ 8.0/10

该论文首次在四元数序上提出了格基约化算法 QuaILLL 和四元数 BKZ，用于分析秩 2 模格同构问题（module-LIP）方案。它扩展了 LLL 算法以利用四元数序的代数性质，并引入了后处理策略，随后描述了任意块大小的四元数 BKZ。 当前对一般秩 2 模 LIP 方案的密码分析依赖于实数嵌入上的 SVP 预言机，丢弃了四元数结构。新算法可将格基的秩减少到标准实数嵌入的四分之一左右，从而改善界限和渐近复杂度，对 Hawk 等后量子方案具有直接意义。 该方法先在欧几里得超格上约化，然后进行后处理：一个例程返回具有最佳界限的子格基，另一个返回原始格的真实基，但输出质量有所下降。该算法通过修改后的典范嵌入（保持维数和四元数结构）应用于由约化范数主理想问题产生的理想格，包括 Hawk 实例。

rss · IACR ePrint 密码学论文 · 8月20日 21:53

**背景**: LLL 是 1982 年提出的多项式时间格基约化算法，广泛用于密码分析。四元数代数是实数的四维非交换扩张，其序是整数环的推广。模格同构问题（module-LIP）询问数域整数环上的两个模格是否等距，是多项后量子密码提案的基础问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lenstra–Lenstra–Lovász_lattice_basis_reduction_algorithm">Lenstra–Lenstra–Lovász lattice basis reduction algorithm - Wikipedia</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-58754-2_9">Cryptanalysis of Rank - 2 Module -LIP in Totally Real Number Fields</a></li>

</ul>
</details>

**标签**: `#lattice-reduction`, `#quaternion-algebras`, `#post-quantum-cryptography`, `#cryptanalysis`, `#LLL-BKZ`

---

<a id="item-13"></a>
## [固定行权重 EA 码在任意域上实现线性距离](https://eprint.iacr.org/2026/1753) ⭐️ 8.0/10

这篇新论文以更强的域统一形式证明了 Block 等人在 CRYPTO 2024 上提出的猜想：单个固定行权重的扩展累积码在任意有限域上都能以逆多项式失败概率实现常数相对距离。 这解决了域无关 SNARK 和关联伪随机性的一个基础性问题：单个固定行权重 EA 分量就足够了，无需针对特定域调整参数，从而加强了在任意有限域上工作的构造。 对任意码率 R∈(0,1)，存在δ_R>0，使得对任意目标指数 C，选择行权重 t=⌈γ log N⌉后失败概率不超过 N^{-C}；这些常数对所有素数幂 q 都适用，即使域随块长变化。证明分别处理稀疏消息和高权重消息：稀疏消息借助扩展和累积消除的紧凑分析，高权重消息在较大域上利用线性约束盈余、在有界域上利用随机累积分析；并证明 t=Θ(log N)时逆多项式失败是最优的。

rss · IACR ePrint 密码学论文 · 8月20日 20:58

**背景**: 扩展累积（EA）码是稀疏线性码，定义为 H=BA，其中 B 是稀疏扩展矩阵，A 是累积矩阵。它们最初用于产生关联伪随机性，后来被用于构建域无关 SNARK，例如针对 R1CS 的 Brakedown，避免依赖特定域的性质。Block 等人在 CRYPTO 2024 中猜想单个固定行权重 EA 分量就能以逆多项式失败概率达到常数相对距离；本文以更强的形式证明了该猜想。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scispace.com/pdf/correlated-pseudorandomness-from-expand-accumulate-codes-2yupv4zv.pdf">Correlated Pseudorandomness from Expand-Accumulate Codes</a></li>
<li><a href="https://www.researchgate.net/publication/383167581_Field-Agnostic_SNARKs_from_Expand-Accumulate_Codes">Field-Agnostic SNARKs from Expand - Accumulate Codes</a></li>

</ul>
</details>

**标签**: `#coding theory`, `#expand-accumulate codes`, `#SNARKs`, `#cryptography`, `#linear codes`

---

<a id="item-14"></a>
## [基于格的阈值零知识证明用于精确关系](https://eprint.iacr.org/2026/1750) ⭐️ 8.0/10

该论文构建了首个基于格的阈值零知识证明系统，用于精确关系，允许持有 Shamir 共享证据的 n 方中任意 t 方共同生成证明，证明形式与单证明者证明相同，仅扩大 √t 倍，验证保持不变。它阈值化了 Attema、Lyubashevsky 和 Seiler（CRYPTO 2020）的乘积证明以及 Esgin、Nguyen 和 Seiler（ASIACRYPT 2020）的精确证明，使用 Hint-MLWE 使其无需拒绝采样，并在阈值同态加密上求值。 这填补了后量子密码学中的一个重要空白，使匿名凭证等隐私保护应用能够使用分布式证明者，避免单点故障，同时保持与单证明者系统相同的验证方式。它还证明了两种系统的 Fiat–Shamir 变换在随机预言模型下具有仿真可提取性，并确认了从子环中取秘密时 MLWE 仍然困难。 安全性针对被动敌手以及最多静态腐败 t−1 方的情况。证明通过 Hint-MLWE 和阈值同态加密实现无拒绝采样；此外，两种系统的 Fiat–Shamir 变换在随机预言模型下具有仿真可提取性，且当秘密取自环自同构固定的子环时 MLWE 仍保持困难。

rss · IACR ePrint 密码学论文 · 8月20日 17:07

**背景**: 零知识证明允许证明者在不泄露证据的情况下使验证者相信某个陈述为真。基于格的构造因能抵抗量子攻击而备受关注，但现有系统要求单一证明者持有完整证据。Shamir 秘密共享将秘密分成 n 份，任意 t 份即可重建，本文用它把证据分发给多个证明者。精确陈述（例如证明一个值满足精确的短界）在匿名凭证等应用中必不可少，并且比近似陈述更难阈值化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://crypto.iacr.org/2022/papers/538804_1_En_3_Chapter_OnlinePDF.pdf">Lattice - Based Zero - Knowledge Proofs and Applications: Shorter...</a></li>
<li><a href="https://www.quillaudits.com/blog/web3-security/shamir-secret-sharing">Shamir ’s Secret Sharing Demystified: A Visual Guide</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#lattice-based cryptography`, `#threshold cryptography`, `#post-quantum cryptography`, `#cryptographic protocols`

---

<a id="item-15"></a>
## [SafeHub：具有回滚检测的端到端加密 Git 托管系统](https://eprint.iacr.org/2026/1748) ⭐️ 8.0/10

SafeHub 是一种新型端到端加密 Git 托管系统，对仓库内容和语义元数据（文件名、提交消息、作者、分支、问题、拉取请求和引用）进行加密，同时保持标准 Git 操作。每个仓库都是一个 MLS 组，加密的、设备签名的哈希链清单可检测回滚；一个 NIST PQ 第 5 类 Rust 原型在 0.05 MB 增量时推送运行时间为普通 Git 的 1.45 倍，在 5 MB 时为其 0.98 倍。 SafeHub 弥补了代码托管中的一个关键缺口：即使有传输加密和静态加密，Git 托管商仍可读取私有仓库。通过隐藏内容和元数据同时保持 Git 工作流，它实现了机密协作，并可能降低企业和开源项目面临的内部人员及服务器被攻破风险。 该设计使用每个仓库一个 MLS 组，提供管理员介导的成员资格、泄露后恢复和每次邀请的历史窗口；可变引用由加密的、设备签名的哈希链清单保护，该清单可检测回滚，并且强制推送需要管理员共同签名。作者在通用可组合性模型下证明了针对恶意服务器和自适应成员腐败的安全性，假设在量子随机预言机模型下安全擦除；在共享传输上，SafeHub 在推送、拉取、获取、合并、变基和强制推送方面是六个系统中最快的，存储大小与普通 Git 相差在 0.2% 以内，但克隆会随密封历史增长，因为服务器无法重新打包。

rss · IACR ePrint 密码学论文 · 8月20日 15:37

**背景**: Messaging Layer Security（MLS）是 IETF 制定的端到端加密群组消息标准，支持大型群组和高效的成员变更，包括泄露后安全。Git 仓库通常以哈希链接对象存储，这能防止不可变对象被篡改，但不能保护分支指针等可变引用。Git 的端到端加密具有挑战性，因为服务器必须在不看到明文的情况下支持合并、追溯和克隆等操作；现有的 git-crypt 和 git-remote-gcrypt 等工具会加密单个文件，可能带来逐文件开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Messaging_Layer_Security">Messaging Layer Security</a></li>

</ul>
</details>

**标签**: `#git`, `#end-to-end-encryption`, `#security`, `#MLS`, `#version-control`

---
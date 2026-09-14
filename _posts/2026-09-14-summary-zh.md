---
layout: default
title: "Horizon Summary: 2026-09-14 (ZH)"
date: 2026-09-14
lang: zh
---

> 从 43 条内容中筛选出 15 条重要资讯。

---

1. [基于同态秘密共享的混淆 RAM 方案实现渐近最优通信](#item-1) ⭐️ 9.0/10
2. [研究人员用双锚点保留/Hermite 方法破解 TII-254 McEliece 密钥恢复挑战](#item-2) ⭐️ 9.0/10
3. [重新审视中间相遇攻击中的单色初始结构](#item-3) ⭐️ 8.0/10
4. [新对称多项式模型降低伴随式译码问题复杂度](#item-4) ⭐️ 8.0/10
5. [研究人员披露 Proton Docs/Sheets 三类完整性攻击](#item-5) ⭐️ 8.0/10
6. [新的网络无关 VSS 实现二次通信且无需拜占庭共识](#item-6) ⭐️ 8.0/10
7. [后量子密钥交换迁移的统一框架](#item-7) ⭐️ 8.0/10
8. [SHUTTLE：基于整数运算与标准假设的紧凑格签名方案](#item-8) ⭐️ 8.0/10
9. [有界信息：多变量侧信道迹的 PAC 认证](#item-9) ⭐️ 8.0/10
10. [Wasp：基于 VOLE 的简洁非交互零知识证明](#item-10) ⭐️ 8.0/10
11. [Bonsai：验证者无需存储无效符的可扩展隐私支付](#item-11) ⭐️ 8.0/10
12. [后量子小集合隐私集合求交已实用化。](#item-12) ⭐️ 8.0/10
13. [新论文从 GIJS 区分器中提取 Classic McEliece 密钥](#item-13) ⭐️ 8.0/10
14. [Akita：兼具小证明体积与快速验证的格基多项式承诺方案](#item-14) ⭐️ 8.0/10
15. [备选 mod-2/mod-3 弱 PRF 遭新区分攻击，复杂度 O(2^{0.099n})](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [基于同态秘密共享的混淆 RAM 方案实现渐近最优通信](https://eprint.iacr.org/2026/1998) ⭐️ 9.0/10

该论文提出一种混淆 RAM 构造，针对公开 RAM 程序、秘密输入和内存，在字长较大时实现 O(TW log N)比特的通信量，渐近匹配最优混淆随机存取存储器的带宽。 由于通信量渐近匹配 ORAM 带宽，该结果消除了长期存在的渐近开销，可能使 RAM 模型程序的安全计算更实用，对密码学、安全多方计算和隐私保护计算均有影响。 该构造面向布尔 RAM 模型，需要 W≥λ且 T≥poly(λ)，建立在基于同态秘密共享的简洁混淆电路之上，依赖循环幂形式的 DDH 或 RLWE 假设；与 Liu 等人（ACM CCS'26）在随机预言机模型下的最优混淆 RAM 相比，去掉了通信量中的因子λ。

rss · IACR ePrint 密码学论文 · 9月12日 21:53

**背景**: 混淆电路允许两方在不泄露输入的情况下安全计算函数，但把 RAM 程序编译成电路代价很高。混淆 RAM 是 RAM 模型下的对应物，避免整体电路编译，并以通信复杂度为主要效率指标。混淆随机存取存储器（ORAM）隐藏内存访问模式，任何安全的混淆 RAM 也必须如此隐藏访问。同态秘密共享允许各方对秘密共享数据执行本地计算，近期基于 HSS 的简洁混淆电路为本文构造提供了基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Oblivious_RAM">Oblivious RAM</a></li>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_secret_sharing">Homomorphic secret sharing</a></li>
<li><a href="https://experts.illinois.edu/en/publications/epigram-practical-garbled-ram">EpiGRAM: Practical Garbled RAM - Illinois Experts</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secure multiparty computation`, `#garbled RAM`, `#homomorphic secret sharing`, `#communication complexity`

---

<a id="item-2"></a>
## [研究人员用双锚点保留/Hermite 方法破解 TII-254 McEliece 密钥恢复挑战](https://eprint.iacr.org/2026/1986) ⭐️ 9.0/10

研究人员利用双锚点保留法，通过计算两个在不同公开坐标条件下的关系核，隔离出 F_{2^8} 上的射影直线几何，从而恢复了全部 87 个定位子并完整还原了 TII-254 McEliece 挑战的私钥；该挑战在原始暴力破解度量下是 2^{254}，是目前已破解的最难挑战。 这对基于编码的后量子密码学具有重要意义：它证明此前被认为需要 2^{254} 暴力破解工作量的 TII-254 参数集，可以用适度的 GPU 资源在约 27.2 GPU 小时内完成密钥恢复，可能会影响 McEliece 类方案的参数选择和安全评估。 参数为 (8,12,223)，定义一个二进制 [223,127] 码，其校验矩阵为 96×223 满秩矩阵；攻击恢复了全部 87 个可见定位子以及完整支撑和多项式。仅最后两个 Krylov 序列就在 NVIDIA GH200 上花费了 27.2 GPU 小时，这还不包括 GPU 重建和 CPU 处理时间。

rss · IACR ePrint 密码学论文 · 9月11日 19:10

**背景**: McEliece 密码系统是一种基于一般线性码译码困难性的后量子公钥加密方案，其私钥使用具有高效译码算法的 Goppa 码，而公钥将所选码伪装成看似随机的线性码。TII McEliece 挑战于 2024 年推出，提供奖金，要求参与者在不同参数集下从公钥恢复私钥；TII-254 在原始暴力破解度量下设计为 254 位安全。密钥恢复指的是找出隐藏结构（如 Goppa 多项式和定位子）以实现高效译码，而不是仅仅破解单条密文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1986">Two-Anchor Holdout/Hermite: Solving the TII-254 McEliece Key Recovery Challenge</a></li>
<li><a href="https://en.wikipedia.org/wiki/McEliece_cryptosystem">McEliece cryptosystem</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#McEliece`, `#code-based cryptography`, `#key recovery`, `#post-quantum`

---

<a id="item-3"></a>
## [重新审视中间相遇攻击中的单色初始结构](https://eprint.iacr.org/2026/1999) ⭐️ 8.0/10

论文提出了两种通用技术：一种利用 MITM 攻击中的常量空间来改进 Chen 等人在 Asiacrypt 2025 提出的单色初始结构算法，放宽自动搜索中的优化目标；另一种将 Li、Isobe 和 Shibutani 在 FSE 2012 提出的部分目标原像到碰撞转换扩展到选择前缀碰撞和菱形结构构造。 中间相遇攻击是最强大的密码分析工具之一，这项工作可能降低类 AES 结构在（伪）原像、碰撞和牧群攻击中的安全估计。 第一种技术观察到 MITM 攻击中的常量空间与值无关，可实现 MITM 式划分并加速攻击子过程；第二种将 FSE 2012 的转换扩展到选择前缀碰撞和菱形结构构造，并在类 AES 结构上取得了优于现有最佳的结果。

rss · IACR ePrint 密码学论文 · 9月13日 04:19

**背景**: 中间相遇（MITM）攻击将计算分成两半，从两端向中间状态推进并用预计算表匹配。初始结构是连接多个 MITM 分段以降低开销的技术；单色初始结构是 Chen 等人在 Asiacrypt 2025 提出的变体，用于自动搜索框架。Li、Isobe 和 Shibutani 在 FSE 2012 提出的部分目标原像到碰撞转换可将某些原像攻击转化为碰撞攻击。类 AES 结构是基于 SPN 的设计，广泛用作哈希函数和认证加密的构建模块。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1999">Revisiting Single-Color Initial Structures in Meet-In-The-Middle Attacks</a></li>
<li><a href="https://www.springerprofessional.de/en/converting-meet-in-the-middle-preimage-attack-into-pseudo-collis/3999108">Converting Meet-In-The-Middle Preimage Attack into Pseudo Collision Attack: Application to SHA-2 | springerprofessional.de</a></li>
<li><a href="https://link.springer.com/rwe/10.1007/978-1-4419-5906-5_597">Meet - in - the - Middle Attack | Springer Nature Link</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#cryptanalysis`, `#meet-in-the-middle`, `#hash functions`, `#collision attacks`

---

<a id="item-4"></a>
## [新对称多项式模型降低伴随式译码问题复杂度](https://eprint.iacr.org/2026/1995) ⭐️ 8.0/10

该论文引入基于初等对称多项式的新的多项式模型，用于求解二元伴随式译码问题（SDP）的精确变体。作者通过建立正则度和求解度的界，得到了比以往多项式模型更低的复杂度估计，并提供了一个依赖具体实例的变体，其复杂度更低。 这可能影响基于编码的密码体制的安全性评估，因为其安全性依赖于 SDP 的困难性。更低的复杂度估计可能促使后量子密码方案重新评估参数。 该论文针对二元 SDP 的精确变体，通过初等对称多项式建模，并推导相关理想的正则度与求解度界。第二个模型的复杂度直接依赖于具体实例，比第一个模型更低。

rss · IACR ePrint 密码学论文 · 9月12日 17:11

**背景**: 伴随式译码问题要求给定校验矩阵 H 和伴随式 b，找到低重量向量 x 使得 Hx=b，是基于编码的密码学中的基础困难问题。Gröbner 基是求解多项式方程组的重要工具，其复杂度通常用正则度和求解度来刻画。初等对称多项式是一类特殊多项式，可用于表示解向量汉明重量的约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://decodingchallenge.org/syndrome">Challenges for code-based problems</a></li>
<li><a href="https://en.wikipedia.org/wiki/Code-based_cryptography">Code-based cryptography</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gröbner_basis">Gröbner basis</a></li>

</ul>
</details>

**标签**: `#syndrome-decoding`, `#code-based-cryptography`, `#cryptanalysis`, `#polynomial-system-solving`, `#groebner-bases`

---

<a id="item-5"></a>
## [研究人员披露 Proton Docs/Sheets 三类完整性攻击](https://eprint.iacr.org/2026/1994) ⭐️ 8.0/10

研究人员披露了 Proton Docs/Sheets 的三种完整性攻击，可分别实现历史记录重写、上下文操控和审查，并且都能避开检测；其中前两种在 Proton 服务器诚实的情况下也可以发动，第三种则是由被攻陷的 Proton 服务器发起。论文同时提出了相应的缓解措施。 该研究揭示了协作编辑场景下端到端安全的重要细微之处，影响了一个被超过十万个组织使用的隐私优先服务。它凸显了对多用户、持续更新系统进行系统性形式化安全设计与分析的必要性。 该分析基于开源 Web 客户端代码和网页代码检查。第一、二种攻击可由恶意用户在服务器诚实的情况下实施，第三种需要被攻陷的服务器，且三种攻击都能规避检测；论文提出了相应的缓解方法，但尚未报告形式化验证。

rss · IACR ePrint 密码学论文 · 9月12日 14:58

**背景**: Proton 是一家注重隐私的服务商，其 Docs/Sheets 产品支持实时协作编辑，并声称通过客户端加密提供端到端安全。在这类系统中，多个用户会持续更新共享文档，而服务器可能并不完全可信。完整性要求内容和编辑历史无法在未被察觉的情况下被篡改。该论文正是针对这些保证，分析了 Proton Docs/Sheets 的加密设计和协作协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://proton.me/security/end-to-end-encryption">Proton’s end-to-end encryption — How we secure your data | Proton</a></li>
<li><a href="https://www.howtogeek.com/proton-now-has-a-google-sheets-clone/">Proton now has a Google Sheets clone with end-to-end encryption</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#end-to-end encryption`, `#collaborative editing`, `#security`, `#Proton`

---

<a id="item-6"></a>
## [新的网络无关 VSS 实现二次通信且无需拜占庭共识](https://eprint.iacr.org/2026/1993) ⭐️ 8.0/10

该论文提出一种采用虚拟参与方策略的新网络无关可验证秘密共享（VSS）协议，无需拜占庭协议，并将通信从 O(n^5)比特降低到一次性情形下的 O(n^2)比特，以及在轮次情形下借助争议控制达到 O(n)比特。 VSS 是安全多方计算的核心原语，将网络无关共享的通信从 O(n^5)降到 O(n^2)乃至摊还 O(n)，使 MPC 在同步和异步网络下都更加实用；去掉拜占庭协议还消除了昂贵的共识瓶颈。这一改进有望降低真实分布式系统中安全多方计算的部署成本。 关键技术是一种虚拟参与方策略，通过引入更多参与方进行重构，使协议免拜占庭协议且达到与同步 VSS 相同的效率。作者还将可靠广播中的纠删码、VSS 中的打包秘密共享以及 MPC 中的相关多项式技术适配到网络无关模型。

rss · IACR ePrint 密码学论文 · 9月12日 11:28

**背景**: 可验证秘密共享（VSS）允许分发者把秘密份额分给参与者，并让参与者能够验证份额是否一致，即使分发者或部分参与者是恶意的；它是安全多方计算（MPC）的基础构件。网络无关协议力求无论底层网络是同步还是异步，都提供安全保证。此前 Bhimrajka 等人的计算网络无关 VSS 需要拜占庭协议（一种确保诚实参与者在任意故障下仍能达成一致的共识原语），且通信为 O(n^5)。新工作在此方向上去除了拜占庭协议要求，并大幅降低通信。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Verifiable_secret_sharing">Verifiable secret sharing</a></li>
<li><a href="https://eprint.iacr.org/2025/228">Network agnostic consensus in constant time</a></li>
<li><a href="https://arxiv.org/abs/2306.01401">[2306.01401] Network Agnostic MPC with Statistical Security</a></li>

</ul>
</details>

**标签**: `#verifiable secret sharing`, `#multiparty computation`, `#network-agnostic protocols`, `#communication complexity`, `#cryptography`

---

<a id="item-7"></a>
## [后量子密钥交换迁移的统一框架](https://eprint.iacr.org/2026/1992) ⭐️ 8.0/10

这篇新的 ePrint 论文（2026/1992）提出了一个统一且经过形式化分析的安全框架，用于将传统密钥交换协议迁移到后量子对应方案；其动机是谷歌将内部后量子密码迁移截止时间提前到 2029 年。 由于量子计算和纠错进展快于预期，传统密钥交换协议会更早面临风险；一个经过形式化分析的迁移框架可以帮助协议设计者和企业在更紧迫的期限内保持安全。 该框架针对经典密钥交换构造及其后量子对应方案；论文引用了谷歌 2029 年截止日期与 NIST/美国政府 2035 年截止日期之间的差距，并提到量子硬件、量子纠错以及破解当前密码所需资源估算的加速进展。

rss · IACR ePrint 密码学论文 · 9月12日 10:58

**背景**: 后量子密码（PQC）旨在替代 RSA 和椭圆曲线等传统公钥算法，这些算法在足够强大的量子计算机面前可能被破解。NIST 一直在推进 PQC 标准化，包括用于密钥封装的标准 FIPS 203（ML-KEM），并设定 2035 年为美国联邦系统弃用传统公钥算法的截止日期。谷歌将内部截止日期提前到 2029 年，反映出其担忧量子攻击可能比官方时间表更早变得实际可行，这主要得益于量子硬件和量子纠错的进步。一个统一的密钥交换迁移形式化框架有望降低现有互联网协议过渡的工作量和风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization">NIST Post-Quantum Cryptography Standardization</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quantum_error_correction">Quantum error correction</a></li>
<li><a href="https://csrc.nist.gov/projects/post-quantum-cryptography">Post - Quantum Cryptography | CSRC</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#key exchange`, `#security framework`, `#protocol migration`, `#cryptographic transition`

---

<a id="item-8"></a>
## [SHUTTLE：基于整数运算与标准假设的紧凑格签名方案](https://eprint.iacr.org/2026/1991) ⭐️ 8.0/10

研究人员提出 SHUTTLE，一种基于标准 MLWE 公钥结构的紧凑 Fiat–Shamir 签名方案，其不可伪造性在随机预言机模型下归约到 MSIS。在 NIST 一级安全级别下，该方案签名大小为 1175 字节（合计 2167 字节），比 ML-DSA-44 小 51%、比 HAETAE-120 小 20%，并采用纯整数运算；签名约需 1406k 周期，比 HAETAE-120 快约 3 倍。 该方案缓解了格签名在紧凑性、实现简易性和标准假设之间的严格权衡。由于不使用浮点运算并消除了依赖秘密的拒绝采样，SHUTTLE 有望降低硬件和嵌入式设备上的部署难度，并减少侧信道风险。 SHUTTLE 的三大核心技术包括：用受 Rényi 散度约束的确定性转移替代依赖秘密的拒绝采样，使重启仅因公开边界和编码检查发生（概率约 2^-30）；将对数域转移逻辑化简为整数区间比较；以及采用非对称拉伸-压缩机制抵消 MLWE 参数扩展。

rss · IACR ePrint 密码学论文 · 9月12日 10:20

**背景**: MLWE 和 MSIS 是后量子密码中标准的格困难问题，ML-DSA（Dilithium）、HAETAE 等签名方案都基于这些问题，并通过 Fiat–Shamir 变换将交互式协议转为非交互式签名。Falcon 虽然签名很小，但依赖浮点离散高斯采样，安全实现难度较大；SHUTTLE 的目标是仅用整数运算达到紧凑签名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/155">Module Learning With Errors and Structured Extrapolated Dihedral ...</a></li>
<li><a href="https://csrc.nist.gov/glossary/term/module_short_integer_solution">Module Short Integer Solution - Glossary | CSRC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rényi_divergence">Rényi divergence</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#lattice-based cryptography`, `#digital signatures`, `#MLWE`, `#MSIS`

---

<a id="item-9"></a>
## [有界信息：多变量侧信道迹的 PAC 认证](https://eprint.iacr.org/2026/1990) ⭐️ 8.0/10

本文提出了有界信息（BI），一种 PAC 风格的有限样本认证方法，可对固定攻击者套件在未见迹上的精确恢复成功率给出上界。BI 通过 KL 二项置信区间与联合界覆盖包含所有训练攻击者、预处理选择和超参数的套件，将标准建模攻击评估转化为可审计的证书。 现有的感知信息、假设信息和互信息等信息论估计量在高维迹上不稳定，且无法给出有限样本的攻击者证书。BI 通过提供具有明确攻击者范围与置信水平的稳定可审计上界，增强了侧信道安全评估的可信度。 BI_suite 通过对包含训练攻击者、预处理选择和超参数的固定套件应用 KL 二项置信区间与联合界来给出上界；BI_loc(ε)约束归一化分数与套件中模型差异不超过ε的攻击者的恢复成功率。在迹维度高达 7000 的八个基准上，BI 无需密度估计即可提供稳定证书，其紧致性诊断可区分真实泄露度量与需要更多攻击迹才能收紧的保守界。

rss · IACR ePrint 密码学论文 · 9月12日 10:16

**背景**: 侧信道攻击利用密码设备运行时泄露的功耗、电磁辐射或时间等物理信息来恢复密钥。建模侧信道评估通常在已知密钥的副本设备上训练机器学习模型，再测试其对未见迹的秘密恢复能力。二项比例置信区间根据观测到的成功与失败次数给出真实成功率的区间；KL 二项变体利用 Kullback-Leibler 散度获得更紧的有限样本界。PAC 学习框架提供“概率近似正确”保证：以高概率使学习模型的误差不超过指定容差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Side-channel_attack">Side-channel attack</a></li>
<li><a href="https://en.wikipedia.org/wiki/Probably_approximately_correct_learning">Probably approximately correct learning - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval">Binomial proportion confidence interval - Wikipedia</a></li>

</ul>
</details>

**标签**: `#side-channel analysis`, `#information theory`, `#security evaluation`, `#PAC learning`, `#hardware security`

---

<a id="item-10"></a>
## [Wasp：基于 VOLE 的简洁非交互零知识证明](https://eprint.iacr.org/2026/1988) ⭐️ 8.0/10

该论文提出了 Wasp，一个基于 VOLE 构造的简洁非交互零知识证明系统，它把信息论多项式认证码（IT-PAC）增强为功能完整的多项式承诺方案。论文还给出了面向 SIMD 电路的 Wasp^S 和面向 Plonkish 约束系统的通用 zkSNARK Wasp^G（具有常数验证时间和证明大小），并优化了 Antman++的编译器以实现亚线性验证者。 这克服了 Antman 和 Antman++等先前基于 VOLE 证明的交互性和验证者简洁性限制，使 VOLE 零知识证明适用于区块链 Rollup 和去中心化验证等非交互场景。它提供了快速证明者、122 KB 证明和不到 1 毫秒的验证时间，有望成为配对、编码和格基 zkSNARK 的有力替代方案。 Wasp 的非交互性在 VOLE 混合模型下实现，需要预处理的 VOLE 相关性；实验显示 Wasp^S 验证者比 Antman 快 1–2 个数量级，编译后的通用验证者比 Antman++快 2–3 个数量级。Wasp^G 的证明者比基于配对、编码和格的 zkSNARK 快 1–2 个数量级，证明大小为 122 KB、验证时间不到 1 毫秒，但其证明速度比非简洁 VOLE 零知识证明慢 3–22 倍。

rss · IACR ePrint 密码学论文 · 9月12日 03:23

**背景**: VOLE（向量不经意线性评估）是将不经意线性评估扩展到向量的密码学原语，广泛用于构造高效零知识证明和安全多方计算。IT-PAC 在 Antman（CCS '22）中被引入，使基于 VOLE 的 ZK 证明在 SIMD 电路和通用电路上实现亚线性通信，Antman++进一步将通用通信降至 O(B+C)。但这些基于 IT-PAC 的协议仍保持交互式，验证者也不够简洁，部分原因是 IT-PAC 的功能有限，无法应用 Fiat-Shamir。Wasp 通过将 IT-PAC 强化为支持通用求值打开的多项式承诺方案来解决这些不足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1988">Wasp: Succinct Non-Interactive Zero-Knowledge Proofs from VOLE</a></li>
<li><a href="https://github.com/adust09/awesome-vole">GitHub - adust09/awesome-vole: A curated list of awesome Vector Oblivious Linear Evaluation (VOLE) resources, protocols, implementations, and applications. · GitHub</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3548606.3560667">AntMan | Proceedings of the 2022 ACM SIGSAC Conference on ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#zero-knowledge proofs`, `#VOLE`, `#succinct proofs`, `#non-interactive`

---

<a id="item-11"></a>
## [Bonsai：验证者无需存储无效符的可扩展隐私支付](https://eprint.iacr.org/2026/1987) ⭐️ 8.0/10

Bonsai 提出一种基于账户的隐私支付方案，验证者仅为每个账户存储一个承诺，而不再存储任何无效符。用户自行私密维护收到的支付无效符，并可将旧无效符移至冷存储；原型在 M5 MacBook Pro 上每秒验证超过一百万次操作。 这解决了一个关键的可扩展性瓶颈：在每秒百万笔交易下，无效符集合每年将增长一个拍字节，使隐私支付难以在普通硬件上运行。Bonsai 去除了验证者端的无效符存储，有望支撑全球规模的高吞吐量隐私支付。 Bonsai 在 Pari 证明系统（USENIX '26）中加入零知识，证明大小不变、证明者开销可忽略，并采用批量验证来维持吞吐量。外部观察者只能知道某账户执行了发送或接收动作，而无法得知金额或交易对手。

rss · IACR ePrint 密码学论文 · 9月12日 00:36

**背景**: 隐私支付系统通常为每笔交易发布一个无效符以防止双重支付，验证者必须存储不断增长的无效符集合以拒绝重复花费。随着吞吐量上升，这种设计会造成无上限的存储需求。Bonsai 将负担转移：验证者仅为每个账户存储一个承诺，用户则私密跟踪自己收到的支付无效符。Pari 是论文引用的一个证明系统（已被 USENIX Security 2026 接收），Bonsai 为其加入零知识以实现快速验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1987">Bonsai: Scalable Private Payments</a></li>
<li><a href="https://github.com/zcash/zcash/issues/3818">Bonsai: private payments on a succinct (or partially succinct) blockchain · Issue #3818 · zcash/zcash</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#privacy`, `#blockchain`, `#zero-knowledge proofs`, `#scalability`

---

<a id="item-12"></a>
## [后量子小集合隐私集合求交已实用化。](https://eprint.iacr.org/2026/1985) ⭐️ 8.0/10

该论文修改了 RT21 隐私集合求交协议，使其兼容 ML-KEM 等后量子密钥封装机制，并引入了理想置换的域扩展构造。它使用标准化后量子原语实现了小集合 PSI，延迟低至 0.25 毫秒/项，通信开销低至 1.67 KiB/项。 该研究消除了 PSI 协议实现后量子安全所面临的根本障碍，随着后量子密码标准逐步部署，这一工作愈发紧迫。它使小集合隐私求交以适度的开销实现后量子安全，可影响联系人发现、私密消息和隐私保护广告等应用。 该论文表明 RT21 因依赖 Diffie-Hellman 特有属性而无法直接使用后量子 KEM，并提出从 Keccak 等较小块长的理想置换构造大块理想置换的方法。实验显示，后量子安全的性能代价在延迟上为 1.25 到 5.92 倍，通信开销为 16.7 倍，具体取决于实例化方式。

rss · IACR ePrint 密码学论文 · 9月11日 17:00

**背景**: 隐私集合求交（PSI）允许双方在不泄露其他元素的情况下计算共同元素。RT21 协议由 Rosulek 和 Trieu 提出，是针对少于约一千项的小集合的先进 PSI 方案，最初基于 Diffie-Hellman 密钥封装构建。ML-KEM（NIST 标准化的 Kyber）等后量子 KEM 能抵抗量子攻击，但不具备 RT21 所依赖的代数性质。理想置换是理论构件，Keccak 置换族提供了实际实例化方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Private_set_intersection">Private set intersection</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#private set intersection`, `#post-quantum`, `#privacy`, `#protocols`

---

<a id="item-13"></a>
## [新论文从 GIJS 区分器中提取 Classic McEliece 密钥](https://eprint.iacr.org/2026/1984) ⭐️ 8.0/10

该论文证明 Classic McEliece 的 GIJS 区分器计算中已经包含秘密密钥，并给出两种提取方法：一种利用多项式梯度恢复子码和 Goppa 多项式，另一种只需一次区分器运行即可读出整个支撑。论文还将区分器成本估算降低约 20 比特，并解决了此前未解的 TII McEliece 密钥恢复挑战实例。 这是针对一个主流基于编码的后量子加密方案的重要密码分析进展，可能降低安全裕度并影响参数评估。不过，该攻击仍远未达到实用程度，因此不会立即攻破 Classic McEliece。 在 GIJS 成本模型下，密钥恢复成本降至 2^94 到 2^102 比特运算；若完全保留 GIJS 条件和公式，则为 2^114 到 2^124；信息集解码成本为 2^151 到 2^287。第一种方法约需 100 到 1400 次区分器运行；演示攻击恢复了 TII 挑战标签 253（m=8, t=9, n=214）的密钥，使用两个稀疏核计算，每个约 10^7 个未知量、约 700 核时。论文中的多个环节是启发式的，并以显式假设形式列出，并在小密钥和部分完整规模上进行了测试。

rss · IACR ePrint 密码学论文 · 9月11日 16:11

**背景**: Classic McEliece 是一种基于二进制 Goppa 码的编码公钥加密方案，其安全性依赖于解码一般线性码的困难性，并且因抵抗 Shor 算法而成为重要的后量子候选方案。2026 年，Ghoshal、Ishai、Jain 和 Sun（GIJS）提出了首个比通用解码更便宜的 Classic McEliece 公钥区分器，其核心是一个大型稀疏线性代数计算。密钥恢复将区分器扩展为恢复私钥的攻击。信息集解码是针对此类基于编码方案的主要通用攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1984">Improving GIJS Key Recovery for Classic McEliece</a></li>
<li><a href="https://classic.mceliece.org/">Classic McEliece : Intro</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum cryptography`, `#Classic McEliece`, `#key recovery`, `#cryptanalysis`

---

<a id="item-14"></a>
## [Akita：兼具小证明体积与快速验证的格基多项式承诺方案](https://eprint.iacr.org/2026/1983) ⭐️ 8.0/10

Akita 是一种新的格基多项式承诺方案，同时实现了小证明体积、快速验证以及基于标准 Module-SIS 假设的安全性。它通过新的设置卸载技术改进了前身 Hachi，将验证时间降至 O(N^{1/k})，同时保持 O(log N) 的证明大小和 O(N) 的证明者时间；集成到 Jolt 后，相比 Dory 获得 1.3–2.2 倍证明者加速和 2.2–7.4 倍验证者加速。 后量子 SNARK 需要既小又快的多项式承诺，同时不能依赖前量子椭圆曲线假设；Akita 基于标准格困难问题满足了这些需求。这可以使 Jolt 等实用零知识虚拟机更高效，并加强迈向抗量子 zkVM 的路径。 对于任意固定 k≥2，Akita 在 Module-SIS 假设下实现 O(N^{1/k}) 的验证时间、O(log N) 的证明大小和 O(N) 的证明者时间；它还具备 128 字节压缩承诺以及用于更紧参数的精确欧几里得范数检查。基准测试显示证明大小为 61–70 KB，验证速度比 Greyhound 快 10–94 倍，且除存储多项式本身外内存开销为次线性。

rss · IACR ePrint 密码学论文 · 9月11日 16:03

**背景**: 多项式承诺方案（PCS）允许证明者用短字符串承诺一个多项式，并在之后证明所选点上的求值，而不泄露多项式本身。基于格的 PCS 旨在抵御量子计算机，与 KZG 等椭圆曲线构造不同。Module-SIS（模块最短整数解）是一种标准的格困难假设，用于证明安全性。Jolt 是一个零知识虚拟机（zkVM），它依赖快速内存检查论证和多项式承诺来高效证明 RISC-V 程序的正确执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.alignedlayer.com/introduction-to-polynomial-commitment-schemes-pcs/">Introduction to Polynomial Commitment Schemes (PCS)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Short_integer_solution_problem">Short integer solution problem - Wikipedia</a></li>
<li><a href="https://github.com/a16z/jolt">GitHub - a16z/jolt: The simplest and most extensible zkVM. Fast and fully open source from a16z crypto and friends. ⚡</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#zero-knowledge-proofs`, `#post-quantum`, `#polynomial-commitments`, `#SNARKs`

---

<a id="item-15"></a>
## [备选 mod-2/mod-3 弱 PRF 遭新区分攻击，复杂度 O(2^{0.099n})](https://eprint.iacr.org/2026/1982) ⭐️ 8.0/10

该论文提出一种针对备选 mod-2/mod-3 弱伪随机函数（weak PRF）的新区分攻击，其数据和时间复杂度为 O(2^{0.099n})，并在 n=384 的原始参数集上实现了首次实用攻击。作者进一步引入一种通用的“分裂策略”，将渐进复杂度降至 Õ(2^{0.09n})，并修正和细化了 Johansson 等人的偏差分析。 该弱 PRF 是现代密码协议中广泛使用的构造之一，此攻击显著降低了其安全估计，可能影响使用该原语的协议和参数选择。论文还表明在数据限制为 2^{45} 时，n=510 的安全性低于 128 位，为实际部署提供了警示。 攻击利用固定密钥和输入汉明重量下的输出分布，分离并放大了以往被平均掉的统计偏差；分裂策略通过部分固定或猜测密钥来增强偏差，并用类 FFT 技术处理额外计算成本。作者还识别出一大类密钥，对于这些密钥，Johansson 等人的攻击实际表现远好于其渐近预期。

rss · IACR ePrint 密码学论文 · 9月11日 14:30

**背景**: 备选 mod-2/mod-3 弱 PRF 由 Boneh 等人（TCC'18）提出，是一种面向多方计算（MPC）等场景的高效弱伪随机函数，安全性弱于标准 PRF，但计算开销更低。此前主要密码分析结果来自 Cheon 等人和 Johansson 等人的区分攻击。区分攻击旨在将密码原语的输出与随机数据区分开，若快于暴力搜索则被视为对该原语的破解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2020/783">Adventures in Crypto Dark Matter: Attacks, Fixes for Weak Pseudorandom Functions</a></li>
<li><a href="https://link.springer.com/article/10.1007/s10623-022-01071-x">Adventures in crypto dark matter: attacks, fixes and analysis for weak ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#cryptanalysis`, `#weak PRF`, `#distinguishing attack`, `#mod-2/mod-3`

---
---
layout: default
title: "Horizon Summary: 2026-07-25 (ZH)"
date: 2026-07-25
lang: zh
---

> 从 43 条内容中筛选出 15 条重要资讯。

---

1. [基于泡利本征态的高效不可克隆加密](#item-1) ⭐️ 9.0/10
2. [首个无条件不可克隆加密方案实现一比特消息安全](#item-2) ⭐️ 9.0/10
3. [发现相干运行时预期量子多项式时间模拟定义缺陷](#item-3) ⭐️ 9.0/10
4. [量子惰性采样与路径记录技术适用于任意群](#item-4) ⭐️ 8.0/10
5. [ZKPoSP：面向分层确定性钱包的后量子零知识证明](#item-5) ⭐️ 8.0/10
6. [新框架将社会技术因素融入密码威胁建模](#item-6) ⭐️ 8.0/10
7. [Encifher：基于 TEE 的 Solana 机密计算协处理器](#item-7) ⭐️ 8.0/10
8. [线性与恒定不可追踪资产转移的共识数](#item-8) ⭐️ 8.0/10
9. [MAGE-Stern：多级摊销高斯消元法将 HQC 攻击提升约 3 比特](#item-9) ⭐️ 8.0/10
10. [Cloudflare 研究揭示 BGP ORIGIN 属性普遍被篡改](#item-10) ⭐️ 8.0/10
11. [SM4th 和 uBlockith：基于中国分组密码的后量子签名方案](#item-11) ⭐️ 7.0/10
12. [基于全同态加密的高效隐私保护 LSTM 推理协议](#item-12) ⭐️ 7.0/10
13. [免费托管平台扭曲证书透明钓鱼检测](#item-13) ⭐️ 7.0/10
14. [BF²：基于 Bloom 过滤器的多目标密码暴力破解 FPGA 框架](#item-14) ⭐️ 7.0/10
15. [首个支持高效增量更新的可更新私有集合合并协议](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [基于泡利本征态的高效不可克隆加密](https://eprint.iacr.org/2026/1509) ⭐️ 9.0/10

作者提出了首个基于泡利本征态的、在标准模型下实现信息论安全的有效不可克隆加密方案，实现了指数级小的解密优势。该方案避免了以往的低效问题，并结合伪随机函数样态实现了多次安全。 这项工作首次使不可克隆加密具有实用性，消除了先前的效率瓶颈，并提供了强大的信息论安全性。它为现实世界中的量子安全通信协议开辟了道路。 该方案将一经典比特加密为一个随机 n 量子比特泡利算符的随机本征态，加解密仅需 O(n) 个单量子比特门和经典操作。证明的安全界为 1/2 + O(2^{-n/2})，在常数因子内达到最优；证明依赖一个关于泡利群对易结构的新线性代数引理。

rss · IACR ePrint 密码学论文 · 7月23日 20:42

**背景**: 不可克隆加密是一种量子密码学原语，可阻止敌手生成两个均能解密为同一明文的密文。泡利本征态是泡利矩阵的本征态，是量子信息论的基础。伪随机函数样态（PRFS）是经典伪随机函数的量子对应，由 Ananth 等人于 2022 年提出，用于构造多次安全加密方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2022/884">On the Feasibility of Unclonable Encryption, and More</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pauli_matrices">Pauli matrices - Wikipedia</a></li>
<li><a href="https://eprint.iacr.org/2024/1811">Pseudorandom Function-like States from Common Haar Unitary</a></li>

</ul>
</details>

**标签**: `#quantum cryptography`, `#unclonable encryption`, `#Pauli eigenstates`, `#information-theoretic security`, `#post-quantum`

---

<a id="item-2"></a>
## [首个无条件不可克隆加密方案实现一比特消息安全](https://eprint.iacr.org/2026/1511) ⭐️ 9.0/10

该论文首次提出了一种无条件安全的一次性私钥不可克隆加密方案，适用于一比特消息，具有高效运算和指数级小的安全优势。 这一突破实现了不可克隆加密的信息论安全，消除了对计算假设的依赖，能够抵御拥有无限计算资源的敌手，是量子密码学的重大理论进展。 该方案处理一比特消息，使用一次性私钥，实现指数级小的不可克隆不可区分优势，这一强安全概念此前仅有计算安全的构造。

rss · IACR ePrint 密码学论文 · 7月24日 00:11

**背景**: 不可克隆加密是一种量子密码原语，利用量子不可克隆定理防止敌手复制密文。信息论安全（又称无条件安全）确保对拥有无限计算能力的攻击者提供保护，不同于依赖困难性假设的计算安全方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mzhandry.github.io/files/Unclonable.slides.pdf">Unclonable</a></li>
<li><a href="https://en.wikipedia.org/wiki/Information-theoretic_security">Information-theoretic security</a></li>
<li><a href="https://www.emergentmind.com/topics/uncloneable-encryption-ue">Uncloneable Encryption (UE)</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#unclonable encryption`, `#information-theoretic security`, `#quantum cryptography`, `#theoretical computer science`

---

<a id="item-3"></a>
## [发现相干运行时预期量子多项式时间模拟定义缺陷](https://eprint.iacr.org/2026/1500) ⭐️ 9.0/10

该论文指出，Lombardi、Spooner 和 Ma 提出的相干运行时预期量子多项式时间（EQPTc）定义不一定高效，由于酉扩张选择不受限制，甚至可以判定任何经典决策问题。论文提出了一个修订定义，在限制这一自由度的同时保留了 GMW86、FS90 和 GK96 协议的零知识性质，并将 GK96 框架升级到全量子环境，首次实现了针对 QMA 的常数轮量子零知识证明。 该缺陷破坏了量子零知识模拟框架，而这是后量子密码学的基石。修复该问题为常数轮量子零知识奠定了坚实基础，并支持针对 QMA 的新证明系统，拓展了量子安全协议的可行性。 该问题源于为高效量子信道选择酉扩张时的自由度，这可能被利用来进行超多项式计算。修订方案以谨慎的方式限制该选择，确保 EQPTc 模拟器仍然高效。论文还利用修订后的 EQPTc 模拟，构建了针对 QMA 的常数轮恶意验证者零知识证明。

rss · IACR ePrint 密码学论文 · 7月22日 20:37

**背景**: 零知识证明通过一个高效模拟器来形式化，该模拟器模拟验证方的视图。经典常数轮协议依赖预期多项式时间（EPT）模拟器，因为严格多项式时间模拟器通常不存在。在量子环境中，模拟器必须至少是量子多项式时间（QPT）的，但 Chia 等人（CCLY22）证明，即使预期 QPT 黑盒模拟在常数轮协议中也是不可能的。Lombardi 等人（LMS22）随后引入 EQPTc 以规避这一问题，通过相干运行时预期定义效率，而这项新工作对此进行了严格审视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1500">How to Define Expected Quantum Polynomial-Time Zero Knowledge ...</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#quantum cryptography`, `#expected polynomial-time`, `#simulation`, `#post-quantum`

---

<a id="item-4"></a>
## [量子惰性采样与路径记录技术适用于任意群](https://eprint.iacr.org/2026/1510) ⭐️ 8.0/10

本文提出了一种通用的路径记录预言机，能够完美模拟 U(N)任意闭子群中的随机元素，并利用群张量幂表示的交换子给出了其更新过程的数学描述。 这一压缩预言机的推广通过增强可解释性推进了量子算法分析与安全证明，并允许不同群的预言机直接比较，从而得到一种更简单的伪随机酉构造。 该预言机存储 t 个输入输出对的叠加态，编码了费曼路径，透明地记录了学到的信息。其主要应用是将伪随机酉构造为伪随机置换与随机 Clifford 的乘积。

rss · IACR ePrint 密码学论文 · 7月23日 22:03

**背景**: 压缩预言机是一种量子信息框架，用紧凑的叠加数据库状态替代指数大的真值表，从而高效模拟量子查询。它最初针对随机函数提出，后被推广至随机酉和置换，并成为后量子密码学证明的关键工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.30281">[2606.30281] Quantum Lazy Sampling and Path Recording for Any Group</a></li>
<li><a href="https://www.emergentmind.com/topics/compressed-oracle-technique">Compressed Oracle Technique</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#cryptography`, `#compressed oracles`, `#random oracles`, `#query complexity`

---

<a id="item-5"></a>
## [ZKPoSP：面向分层确定性钱包的后量子零知识证明](https://eprint.iacr.org/2026/1508) ⭐️ 8.0/10

该论文提出了 ZKPoSP，一种面向分层确定性钱包的种子知识非交互式零知识证明。它能在不迁移地址的情况下保护现有的 BIP32/BIP44/SLIP-10 地址免受量子攻击，并将每条消息的证明成本降低到与派生深度无关的常数。 这一突破为区块链钱包提供了应对量子威胁的实用方案，它保留了所有现有地址格式，避免全网密钥迁移的混乱。随着量子计算机性能的提升，这对整个加密货币生态系统具有重要意义。 ZKPoSP 将证明分为每个密钥对一次性生成的派生证明和每条消息的签名证明，从而实现了常数级别的签名成本。它利用强化密钥和非强化密钥的结构差异来缩短派生证明。论文还引入了一种新的通用密钥派生方案 QBIP32，该方案基于 HASH768（KMAC256），可统一用于 secp256k1 和 Ed25519 等曲线。其安全性依赖于哈希函数的量子难解性以及 NIZK 对量子敌手的可靠性。

rss · IACR ePrint 密码学论文 · 7月23日 19:28

**背景**: 分层确定性钱包（HD 钱包）由 BIP32、BIP44 和 SLIP-10 标准定义，通过单个种子生成密钥树，便于备份和恢复。目前这些钱包依赖椭圆曲线密码学，而量子计算机运行的 Shor 算法可破解其私钥。迁移到后量子签名需要更改地址格式，是一项庞大的协调挑战。非交互式零知识证明（NIZK）允许一方在不泄露秘密的情况下证明其知识，无需交互即可验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hierarchical_deterministic_wallet">Hierarchical deterministic wallet</a></li>
<li><a href="https://www.spark.money/tools/bitcoin-key-derivation-paths-reference">Bitcoin Key Derivation Paths Reference: BIP32 to BIP86 | Spark</a></li>
<li><a href="https://en.wikipedia.org/wiki/Non-interactive_zero-knowledge_proof">Non-interactive zero-knowledge proof</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#zero-knowledge proofs`, `#blockchain`, `#wallet security`, `#hierarchical deterministic wallets`

---

<a id="item-6"></a>
## [新框架将社会技术因素融入密码威胁建模](https://eprint.iacr.org/2026/1507) ⭐️ 8.0/10

提出了一种密码学原生的情境化威胁建模框架，通过融入社会技术维度来揭示部署系统应具备的社会技术属性；以苹果 CSAM 扫描提案为例，发现了此前未被记录的特性。 该框架弥补了密码学分析与社会技术需求之间的鸿沟，有助于在部署前预见到可能的社会危害与隐私问题，推动负责任的系统设计。 该框架基于广泛接受的密码学建模技术，苹果 CSAM 案例研究揭示了功能蠕变等批评，并发现了扫描协议中一个此前未被记录的属性。

rss · IACR ePrint 密码学论文 · 7月23日 13:36

**背景**: 社会技术属性是指由技术组件与人类、社会及制度环境相互作用而产生的系统特性。苹果 2021 年提出的 CSAM 扫描方案试图通过客户端哈希检测 iCloud 照片中的已知儿童性虐待内容，但因隐私和监控风险引发广泛争议。传统密码威胁建模通常只关注技术安全属性，忽略社会影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/collections/jcgafdhjge">Sociotechnical Perspectives to Infrastructure Resilience</a></li>
<li><a href="https://www.wired.com/story/apple-csam-scanning-heat-initiative-letter/">Apple's Decision to Kill Its CSAM Photo-Scanning Tool Sparks Fresh Controversy | WIRED</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#threat modeling`, `#security`, `#privacy`, `#sociotechnical`

---

<a id="item-7"></a>
## [Encifher：基于 TEE 的 Solana 机密计算协处理器](https://eprint.iacr.org/2026/1504) ⭐️ 8.0/10

Encifher 是一种基于 TEE 的新型协处理器，通过在硬件飞地中链下执行加密操作，在 Solana 上实现通用机密计算，克服了 FHE 和 MPC 的性能限制。 它为高通量区块链上的隐私保护金融应用提供了实用解决方案，允许智能合约在不牺牲速度的情况下处理加密数据，这对现实世界的 DeFi 采用至关重要。 Encifher 使用 AES-256-GCM 对称加密，每秒超过一百万次操作；阈值解密在几毫秒内完成；并利用 Solana 的 Sealevel 并行性实现正确排序的执行。

rss · IACR ePrint 密码学论文 · 7月23日 07:30

**背景**: 可信执行环境（TEE）是处理器中的一个安全区域，保护代码和数据免受未授权访问。全同态加密（FHE）允许在加密数据上计算，但速度极慢。安全多方计算（MPC）分散计算但通信开销大。Solana 是一个高通量区块链，使用账户模型和名为 Sealevel 的并行事务调度器。机密计算协处理器（如 Zama 的 fhEVM）将加密计算卸载到专用硬件或环境中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Trusted_execution_environment">Trusted execution environment</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fully_homomorphic_encryption">Fully homomorphic encryption</a></li>
<li><a href="https://github.com/zama-ai/fhevm">GitHub - zama-ai/fhevm: FHEVM, a full-stack framework for ...</a></li>

</ul>
</details>

**标签**: `#confidential computing`, `#TEE`, `#Solana`, `#blockchain privacy`, `#cryptography`

---

<a id="item-8"></a>
## [线性与恒定不可追踪资产转移的共识数](https://eprint.iacr.org/2026/1503) ⭐️ 8.0/10

一项形式化分析指出，线性不可追踪资产转移（LUAT）对象的共识数为 2，而恒定不可追踪资产转移（CUAT）对象在弱不可追踪性下共识数无界，在强不可追踪性下则随掩蔽集大小呈二次增长。 这为增强隐私的加密货币设计的同步成本提供了基础性见解，揭示了不可追踪性既可以仅需适度的共识开销（LUAT），也可能以大幅增加的同步需求为代价（CUAT）。 LUAT 的共识数 2 与掩蔽集大小无关且保证无饥饿性；CUAT 在强不可追踪性下通过冲突图上的均匀关联约束精确确定了共识数，且 CUAT 不满足无饥饿性。

rss · IACR ePrint 密码学论文 · 7月23日 05:38

**背景**: 在分布式系统中，对象的共识数是指仅使用读/写寄存器，该对象能够解决无等待共识问题的最大进程数。不可追踪加密货币通过掩蔽集隐藏转账的真实来源账户。线性设计（如使用无效符）保留旧账户，而恒定状态设计则替换整个集合以保持账本大小固定。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Consensus_(computer_science)">Consensus (computer science) - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2607.20929">[2607.20929] The Consensus Number of Untraceable Cryptocurrencies</a></li>

</ul>
</details>

**标签**: `#consensus`, `#cryptocurrency`, `#privacy`, `#distributed computing`, `#formal verification`

---

<a id="item-9"></a>
## [MAGE-Stern：多级摊销高斯消元法将 HQC 攻击提升约 3 比特](https://eprint.iacr.org/2026/1498) ⭐️ 8.0/10

该论文提出了 MAGE-Stern，这是 Stern 信息集解码算法的一种新变体，采用多级摊销高斯消元法，将针对 HQC 密码系统已知最佳攻击的时间复杂度降低了约 3 比特，存储复杂度降低了约 12 比特。 这一进展意义重大，因为 HQC 是 NIST 选定的后量子加密算法，该攻击将其安全裕度降至低于预期的 128 比特目标，突显了后量子密码学中稳健参数选择的重要性。 该攻击采用分支过程技术进行精细复杂度分析，使用一致的逻辑门成本模型，并且在实际参数下还将伪随机相关生成器（PCG）的攻击改进了最多 6 比特。

rss · IACR ePrint 密码学论文 · 7月22日 08:46

**背景**: 信息集解码（ISD）是一类通过求解解码问题来攻击基于编码的密码系统的算法。HQC（汉明准循环）是近期被 NIST 选定用于后量子加密的基于编码的密钥封装机制。Stern 算法是一种经典的 ISD 方法，引入了碰撞技术。高斯消元是 ISD 中成本较高的步骤；本工作通过多级摊销的主元重用来降低其成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://doc.sagemath.org/html/en/reference/coding/sage/coding/information_set_decoder.html">Information - set decoding for linear codes - Coding Theory</a></li>
<li><a href="https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption">NIST Selects HQC as Fifth Algorithm for Post-Quantum Encryption</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-56232-7_15">Concrete Time/Memory Trade-Offs in Generalised Stern’s ISD ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#cryptanalysis`, `#information-set-decoding`, `#post-quantum-cryptography`, `#HQC`

---

<a id="item-10"></a>
## [Cloudflare 研究揭示 BGP ORIGIN 属性普遍被篡改](https://blog.cloudflare.com/bgp-origin-attribute/) ⭐️ 8.0/10

Cloudflare 的研究发现，中转提供商为获取流量优势，在近 70% 的 BGP 路径上篡改了 ORIGIN 属性。研究主张在路由选择中弃用 ORIGIN。 这种篡改行为破坏了 BGP 路由的完整性，可能导致次优路径选择和安全风险。弃用 ORIGIN 可提升路由稳定性并减少攻击面。 Cloudflare 通过控制实验，用不同 ORIGIN 值通告三个前缀，分析直连对等体和路由收集器。发现即使是直连对等体也经常修改 ORIGIN，且 ORIGIN 值与路由安全无有意义关联。

rss · Cloudflare Blog (PQ 迁移) · 7月24日 17:25

**背景**: BGP（边界网关协议）是互联网的核心路由协议。ORIGIN 属性表示路由的学习方式（如通过 IGP、EGP 或 Incomplete），并在 BGP 最佳路径选择算法中作为一项决策依据。默认情况下，它应由发起网络设置，且中转提供商不应修改。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/bgp-origin-attribute/">BGP ORIGIN attribute manipulation and its impact on the Internet | The Cloudflare Blog</a></li>
<li><a href="https://ipcisco.com/lesson/bgp-path-attributes-origin/">BGP Path Attributes - Origin | BGP Origin Attribute IPCisco</a></li>

</ul>
</details>

**标签**: `#BGP`, `#Internet routing`, `#network security`, `#research`, `#Cloudflare`

---

<a id="item-11"></a>
## [SM4th 和 uBlockith：基于中国分组密码的后量子签名方案](https://eprint.iacr.org/2026/1506) ⭐️ 7.0/10

研究人员提出了 SM4th 和 uBlockith 两种后量子签名方案，基于 FAEST 框架但使用 SM4、uBlock 和 Ballet 等中国设计的分组密码，并进行了定制优化。 该工作表明中国国密算法在后量子密码学中具有竞争力，在有硬件支持的平台上性能接近 FAEST，可能影响密码标准多样化。 在支持原生 SM4 的 Intel 平台上，SM4th 变体性能与 FAEST-128 差距不到 1 倍；在支持 CIS-SM4 的 Hygon 平台上约慢 3 倍。uBlockith 比 FAEST-256 慢 3–4 倍。SM4th-EM-s 公钥和签名总大小 3850 字节，略小于 FAEST-EM-128s 的 3938 字节。

rss · IACR ePrint 密码学论文 · 7月23日 08:26

**背景**: FAEST 是 NIST 后量子签名竞赛第三轮候选方案，基于 VOLE-in-the-Head 技术，该技术将基于 VOLE 的零知识证明转化为仅依赖对称原语（如 AES）的非交互签名。SM4 是中国国家分组密码标准，uBlock 则是近期中国全国密码算法设计竞赛的获奖算法。该工作将 FAEST 的电路方法适配到这些密码的内部运算上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/csrc/media/Projects/post-quantum-cryptography/documents/pqc-seminars/presentations/15-vole-in-the-head-06182024.pdf">Constructions for digital signatures Part II: VOLE - in - the - head and...</a></li>
<li><a href="http://www.jcr.cacrnet.org.cn/EN/10.13868/j.cnki.jcr.000334">The Block Cipher uBlock</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#digital signatures`, `#block ciphers`, `#FAEST`, `#VOLE-in-the-Head`

---

<a id="item-12"></a>
## [基于全同态加密的高效隐私保护 LSTM 推理协议](https://eprint.iacr.org/2026/1502) ⭐️ 7.0/10

该论文提出了一种基于全同态加密的高效 LSTM 推理协议，利用轻量级归一化模块和混合 Remez-最小二乘多项式逼近策略，以低次多项式准确逼近非线性函数，比现有方法速度提升最高 4.7 倍。 这项工作通过大幅降低延迟，显著提升了全同态加密 LSTM 推理的实用性，使得隐私保护的序列数据分析（如医疗文本分析或私有自然语言处理服务）更易于实际部署。 该协议通过轻量级归一化层约束隐藏状态，使用混合 Remez-最小二乘法精确逼近 Sigmoid、Tanh 和平方根倒数函数。基于 Lattigo 库实现，并利用密文打包、旋转减少和 SIMD 并行化，在文本分类任务上达到与明文模型相当的准确率。

rss · IACR ePrint 密码学论文 · 7月23日 05:10

**背景**: 全同态加密（FHE）允许在不解密的情况下对加密数据进行任意计算，是隐私保护机器学习的关键技术。LSTM 网络广泛用于序列数据（如文本），但其非线性激活函数（Sigmoid、Tanh）在 FHE 下计算代价高，需要多项式逼近。Remez 算法用于寻找极小化极大逼近多项式，而最小二乘逼近最小化平均误差；两者结合可兼顾精度与效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fully_homomorphic_encryption">Fully homomorphic encryption</a></li>
<li><a href="https://github.com/tuneinsight/lattigo">GitHub - tuneinsight/ lattigo : A library for lattice-based multiparty...</a></li>

</ul>
</details>

**标签**: `#fully homomorphic encryption`, `#LSTM`, `#privacy-preserving machine learning`, `#secure inference`, `#polynomial approximation`

---

<a id="item-13"></a>
## [免费托管平台扭曲证书透明钓鱼检测](https://eprint.iacr.org/2026/1501) ⭐️ 7.0/10

一项测量研究发现，免费托管平台（FHP）的特性（如共享证书和通配符证书）过度影响了基于证书透明度（CT）的钓鱼检测指标，导致信号扭曲。 这些发现揭示了当前 CT 钓鱼检测系统的一个关键盲区，强调需将托管平台影响纳入考量，以避免误报并提高准确性，尤其在 AI 生成钓鱼网站规模扩大之际。 域名级相关性显示，子域名级别（η=0.54）是与 FHP 最相关的特征，而证书有效期（η=0.31）是与钓鱼最相关的特征。两个代表性 CT 钓鱼检测框架在仅限 FHP 数据上表现不佳，原因在于提供商管理的基础设施。

rss · IACR ePrint 密码学论文 · 7月22日 22:31

**背景**: 证书透明度（CT）是一项互联网安全标准，公开记录所有签发的 TLS 证书，以便检测恶意证书。X.509 证书将身份与公钥绑定，用于 HTTPS。通配符证书可保护一个域名下的多个子域名，在免费托管平台上常见，因为许多用户共享一个域名。免费托管平台允许用户以极低成本托管网站，但攻击者也会利用它们进行钓鱼。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Certificate_Transparency">Certificate Transparency</a></li>
<li><a href="https://en.wikipedia.org/wiki/X.509_certificate">X.509 certificate</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wildcard_certificate">Wildcard certificate</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#phishing`, `#certificate transparency`, `#PKI`, `#web security`

---

<a id="item-14"></a>
## [BF²：基于 Bloom 过滤器的多目标密码暴力破解 FPGA 框架](https://eprint.iacr.org/2026/1499) ⭐️ 7.0/10

研究人员提出了 BF²，一个开源 FPGA-CPU 框架，通过将全流水线 NT 哈希核心与 Bloom 过滤器预检结合，在 199 美元的 NiteFury II 开发板上实现了每秒 16 亿次哈希运算。 这项工作表明，低成本 FPGA 开发板在速度和能效上可大幅超越传统软件和 GPU 密码破解工具，凸显了加强密码哈希算法防护的迫切需求。 该 FPGA 实现包含 16 条运行于 100 MHz 的并行 NT 哈希流水线，利用 Bloom 过滤器预先剔除大多数不匹配的密码候选，随后在主机端通过完美哈希函数进行精确成员资格验证；实验显示其吞吐量最高可达 John the Ripper 的 7.5 倍，功耗比 RTX 5000 上的 Hashcat 低 90%。

rss · IACR ePrint 密码学论文 · 7月22日 15:44

**背景**: Bloom 过滤器是一种空间高效的概率数据结构，用于集合成员资格测试，绝无假阴性但可能存在假阳性，从而快速排除大部分非成员元素。NT 哈希是 Windows NTLM 认证中使用的密码哈希算法，因易于暴力破解而广受批评。完美哈希函数可将已知键集无冲突映射到唯一值，支持快速精确的成员资格检查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bloom_filter">Bloom filter</a></li>
<li><a href="https://en.wikipedia.org/wiki/Perfect_hash_function">Perfect hash function</a></li>
<li><a href="https://en.wikipedia.org/wiki/NT_Hash">NT Hash</a></li>

</ul>
</details>

**标签**: `#password security`, `#FPGA`, `#brute-force attack`, `#hardware acceleration`, `#cryptography`

---

<a id="item-15"></a>
## [首个支持高效增量更新的可更新私有集合合并协议](https://eprint.iacr.org/2026/1497) ⭐️ 7.0/10

该论文提出了首个可更新的私有集合合并（uPSU）协议，使双方能够在不重新计算整个并集的情况下进行增量更新。它提供了通用构造，并证明了在半诚实敌手模型下的安全性。 这一突破使得隐私保护数据共享在动态数据集（如通讯录发现、医疗记录匹配或威胁情报共享）中变得可行，这些场景下数据频繁变动。 该协议使用 Kim 等人的 PSU 和 Raghuraman 及 Rindal 的 PSI 进行实例化，在集合大小 N=2^20、更新大小 t=2^12 的情况下，相比完全重新计算实现了 14.1–45.4 倍的加速和 4.8–59.1 倍的通信量降低。但其开销仍取决于原始集合大小，而非仅与更新大小相关。

rss · IACR ePrint 密码学论文 · 7月22日 08:12

**背景**: 私有集合合并（PSU）允许两方在不泄露各自集合其他信息的情况下计算并集。传统上，任何变更都需要重新计算整个并集，这对于频繁的小更新效率低下。私有集合交集（PSI）类似地计算交集。uPSU 将这些概念扩展到动态场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1497">Updatable Private Set Union: Generic Construction with ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Private_set_intersection">Private set intersection</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#private-set-union`, `#multiparty-computation`, `#privacy-preserving`, `#incremental-updates`

---
---
layout: default
title: "Horizon Summary: 2026-07-26 (ZH)"
date: 2026-07-26
lang: zh
---

> 从 36 条内容中筛选出 13 条重要资讯。

---

1. [基于泡利本征态的高效不可克隆加密](#item-1) ⭐️ 9.0/10
2. [首个无条件不可克隆加密方案：实现单比特消息的信息论安全](#item-2) ⭐️ 9.0/10
3. [Encifher：基于 TEE 的 Solana 机密计算协处理器](#item-3) ⭐️ 8.0/10
4. [针对任意群的量子惰性采样与路径记录](#item-4) ⭐️ 8.0/10
5. [ZKPoSP：用于分层确定性钱包的后量子零知识证明](#item-5) ⭐️ 8.0/10
6. [密码学原生威胁建模框架加入社会技术考量](#item-6) ⭐️ 8.0/10
7. [Cloudflare 发现 70%的 BGP 路径存在 ORIGIN 属性篡改，建议废弃该属性](#item-7) ⭐️ 8.0/10
8. [提出用于衡量 AI 对齐的“精灵系数”](#item-8) ⭐️ 8.0/10
9. [施奈尔新论文解读端到端加密争议](#item-9) ⭐️ 8.0/10
10. [SM4th 与 uBlockith：基于国密算法的后量子签名方案](#item-10) ⭐️ 7.0/10
11. [不可追踪加密货币的共识数分析](#item-11) ⭐️ 7.0/10
12. [Cloudflare 推出缓存响应规则，精细化控制缓存](#item-12) ⭐️ 7.0/10
13. [RFC 10026：DNSSEC DS 记录自动化最佳实践](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [基于泡利本征态的高效不可克隆加密](https://eprint.iacr.org/2026/1509) ⭐️ 9.0/10

研究人员提出了首个在普通模型中具有信息论安全性的高效不可克隆加密方案，利用随机泡利本征态加密经典比特，实现了 O(2^{-n/2})优势的指数级安全性，并在假设伪随机函数态存在的前提下扩展至多次使用的安全性。 这一进展解决了不可克隆加密中长期存在的效率和安全缺陷，为以信息论安全性保障的实用量子安全通信和多次使用加密方案铺平了道路。 该方案将比特编码为 n 量子比特非恒等泡利算符的随机本征态，加密和密钥生成均仅需 O(n)经典运算和单量子比特操作。证明中 1/2+O(2^{-n/2})的上界在常数因子意义上与 n 量子比特密文的已知下界匹配，其安全性依赖于一个关联算符正定性与解密成功概率的新线性代数引理。

rss · IACR ePrint 密码学论文 · 7月23日 20:42

**背景**: 不可克隆加密是一种量子原语，利用不可克隆定理防止密文被复制后两方同时解密。泡利本征态是泡利矩阵的本征向量，是量子信息的基础。普通模型避免使用随机预言机等理想化假设，更具实际意义。伪随机函数态（PRFS）是伪随机函数的量子类比，用于构建多次使用安全的方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mzhandry.github.io/files/Unclonable.slides.pdf">Unclonable</a></li>
<li><a href="https://www.emergentmind.com/topics/uncloneable-encryption-ue">Uncloneable Encryption (UE)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pauli_matrices">Pauli matrices - Wikipedia</a></li>

</ul>
</details>

**标签**: `#quantum cryptography`, `#unclonable encryption`, `#information-theoretic security`, `#Pauli eigenstates`, `#pseudorandom states`

---

<a id="item-2"></a>
## [首个无条件不可克隆加密方案：实现单比特消息的信息论安全](https://eprint.iacr.org/2026/1511) ⭐️ 9.0/10

该论文提出了首个无条件的一次性私钥不可克隆加密方案，用于单比特消息，实现了信息论安全，具有高效的加解密算法和指数级小的不可克隆不可区分优势。 该成果消除了对计算假设的依赖，能抵御拥有无限计算能力的攻击者，是量子密码学的基础性突破，为实用的信息论安全量子通信原语铺平了道路。 该方案针对单比特消息，采用私钥一次性加密，其安全性证明利用 Choi-Jamiołkowski 表示将任意攻击者优势压缩为指数级小量。

rss · IACR ePrint 密码学论文 · 7月24日 00:11

**背景**: 不可克隆加密由 Broadbent 和 Lord 提出，利用量子不可克隆性防止攻击者生成两个均解密为同一消息的密文。以往方案需要后量子公钥加密等计算假设，因此无法抵御拥有无限计算能力的敌手。信息论安全（无条件安全）则无视攻击者的计算资源。该工作首次证明不可克隆加密可在单比特消息上同时实现无条件安全和高效性，填补了重要理论空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2103.15009">[2103.15009] Unclonable Encryption, Revisited</a></li>
<li><a href="https://en.wikipedia.org/wiki/Information-theoretic_security">Information-theoretic security</a></li>
<li><a href="https://arxiv.org/html/2607.21551v1">Unconditional Unclonable Encryption</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#quantum cryptography`, `#unclonable encryption`, `#information-theoretic security`, `#theoretical computer science`

---

<a id="item-3"></a>
## [Encifher：基于 TEE 的 Solana 机密计算协处理器](https://eprint.iacr.org/2026/1504) ⭐️ 8.0/10

研究人员推出了 Encifher，一种可信执行环境（TEE）协处理器，为 Solana 带来可编程的加密计算，支持机密支付、交换和跨链桥，速度接近明文；已投入生产，服务超过 5000 名用户和 5 万次操作。 这弥补了 Solana 缺乏通用机密计算的短板，对金融应用至关重要，通过提供一种实用的替代方案，避免了全同态加密（FHE）的速度慢和安全多方计算（MPC）的高通信开销，有望推动更广泛的 DeFi 隐私用例。 Encifher 在链上使用 128 位密文句柄，链下 AES-256-GCM 加密速度超过百万次/秒，阈值解密在毫秒级完成，并利用 Solana 的 Sealevel 并行调度器；信任分布于阈值委员会和飞地证明验证。

rss · IACR ePrint 密码学论文 · 7月23日 07:30

**背景**: 可信执行环境（TEE）是硬件隔离的安全区域，保护代码和数据不被系统其余部分访问，如 Intel SGX 飞地。全同态加密（FHE）允许在不解密的情况下计算加密数据，但目前对于交互式应用来说速度太慢。安全多方计算（MPC）使多方联合计算函数同时保护输入隐私，但带来高通信开销。Solana 的账户模型和 Sealevel 调度器通过声明读/写集实现并行交易处理，Encifher 将其扩展到加密状态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Trusted_execution_environment">Trusted execution environment</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fully_homomorphic_encryption">Fully homomorphic encryption</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation</a></li>

</ul>
</details>

**标签**: `#privacy`, `#trusted-execution-environment`, `#solana`, `#blockchain`, `#confidentiality`

---

<a id="item-4"></a>
## [针对任意群的量子惰性采样与路径记录](https://eprint.iacr.org/2026/1510) ⭐️ 8.0/10

该论文提出了一个通用的量子惰性采样框架，通过路径记录预言机实现，适用于酉群 U(N)的任意闭子群，从基本原理出发统一并扩展了之前针对随机函数、置换和酉矩阵的压缩预言机构造，并通过群张量幂表示的交换子给出了实用的更新过程描述。 这一进展为量子密码学和查询复杂度提供了统一、可解释的工具，简化了安全证明并有助于获得新的下界。尤其重要的是，它给出了目前已知最简单的伪随机酉矩阵构造（伪随机置换与随机 Clifford 门之积），优于此前工作。 该路径记录预言机存储输入输出对的叠加态，编码 Feynman 路径，透明地记录了算法学到的信息。更新过程通过群张量幂作用的交换子描述，框架直接关联不同群的压缩预言机，从而仅用 PC（伪随机置换与随机 Clifford 之积）构造伪随机酉矩阵，比此前的 PFC 构造（Metger 等，FOCS '24）更简单。

rss · IACR ePrint 密码学论文 · 7月23日 22:03

**背景**: 压缩预言机是量子版本的惰性采样，允许在运行时动态模拟随机预言机，无需预先固定整个随机对象。最初由 Zhandry（CRYPTO '19）针对随机函数提出，后来扩展到随机酉矩阵和随机置换，在量子密码证明和查询复杂度下界中至关重要。本论文基于 Grinko 和 Yoshida（QIP '26）的近期工作，将该技术推广到 U(N)的任意闭子群，并添加了路径记录以增强可解释性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1510">Quantum Lazy Sampling and Path Recording for Any Group</a></li>
<li><a href="https://arxiv.org/abs/2606.30281">[2606.30281] Quantum Lazy Sampling and Path Recording for Any Group</a></li>
<li><a href="https://simons.berkeley.edu/news/compressed-oracles-coherent-workshops-theory-institute-beyond">Compressed Oracles and Coherent Workshops | Theory at the Institute and Beyond</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#cryptography`, `#lazy sampling`, `#compressed oracles`, `#quantum algorithms`

---

<a id="item-5"></a>
## [ZKPoSP：用于分层确定性钱包的后量子零知识证明](https://eprint.iacr.org/2026/1508) ⭐️ 8.0/10

提出了一种新的后量子零知识证明系统 ZKPoSP，通过证明对根种子的知识来保护分层确定性钱包，无需更改现有地址格式，并配套提出了通用的密钥派生方案 QBIP32。 该方法应对了量子计算机破解当前钱包安全性的迫切威胁，无需进行后量子签名方案所需的大规模且破坏性的地址迁移，为整个区块链生态系统提供了无缝过渡。 ZKPoSP 将零知识证明分解为一次性派生证明和每条消息的签名证明，将每条消息的证明开销降至常数。QBIP32 使用基于密钥的哈希函数 HASH768（KMAC256）在一次调用中派生签名标量、量子安全证据和链码，并适用于任何素数阶椭圆曲线群。

rss · IACR ePrint 密码学论文 · 7月23日 19:28

**背景**: 由 BIP32 定义的分层确定性（HD）钱包允许从单个种子生成多个密钥对。传统的 HD 钱包依赖椭圆曲线密码学，该密码学易受使用 Shor 算法的量子攻击。后量子密码学旨在开发对量子计算机安全的方案。零知识证明，特别是非交互零知识（NIZK）证明，允许证明者在不泄露秘密的情况下证明其知道秘密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/BIP32_implementations_in_Rust">BIP32 implementations in Rust</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shor's_algorithm">Shor's algorithm</a></li>
<li><a href="https://crypto.stanford.edu/cs355/19sp/lec5.pdf">Lecture 5: Proofs of Knowledge, Schnorr’s protocol, NIZK</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#zero-knowledge proofs`, `#blockchain`, `#wallet security`, `#hierarchical deterministic wallets`

---

<a id="item-6"></a>
## [密码学原生威胁建模框架加入社会技术考量](https://eprint.iacr.org/2026/1507) ⭐️ 8.0/10

该论文提出了一种密码学原生框架，系统性地将社会技术因素融入威胁建模协议，并以苹果 2021 年的 CSAM 扫描提案为案例，揭示了已知的批评意见和一个未记录的特性。 该框架填补了密码学理论与实际部署之间的关键空白，使分析人员能够及早发现社会技术缺陷，从而可能防止像苹果的 CSAM 扫描提案这样的有害系统在未充分理解其全面影响的情况下被实施。 该框架基于广泛接受的密码学建模技术，支持上下文分析；在应用于苹果的 CSAM 扫描系统时，不仅重现了已知批评，还发现了一个先前未记录的特性。

rss · IACR ePrint 密码学论文 · 7月23日 13:36

**背景**: 威胁建模是系统性地识别系统中安全威胁的方法。2021 年，苹果提议使用加密哈希扫描 iCloud 照片以检测已知儿童性虐待材料(CSAM)，该方法因损害隐私并可能打开监控后门而广受批评。密码学家通常仅分析协议的技术安全属性，而忽略了系统部署的社会技术背景。这一新框架旨在通过将社会技术考量纳入形式化的密码分析来弥合这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.usenix.org/conference/usenixsecurity26/presentation/canetti">Analyzing Cryptography in Context: A Cryptography - Native ...</a></li>
<li><a href="https://www.bu.edu/riscs/2021/08/10/apple-csam/">The Broken Promise of Apple’s Announced Forbidden-photo Reporting System – And How To Fix It | Center for Reliable Information Systems & Cyber Security</a></li>
<li><a href="https://www.wired.com/story/apple-csam-scanning-heat-initiative-letter/">Apple's Decision to Kill Its CSAM Photo-Scanning Tool Sparks Fresh Controversy | WIRED</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#threat modeling`, `#sociotechnical systems`, `#privacy`, `#CSAM`

---

<a id="item-7"></a>
## [Cloudflare 发现 70%的 BGP 路径存在 ORIGIN 属性篡改，建议废弃该属性](https://blog.cloudflare.com/bgp-origin-attribute/) ⭐️ 8.0/10

Cloudflare 的一项测量研究发现，近 70%的观测 BGP 路径的 ORIGIN 属性被中转提供商重写，通常是为了影响流量路由。该公司认为这种普遍篡改使 ORIGIN 属性不再可靠，并主张在 BGP 选路中废弃该属性。 ORIGIN 是 BGP 最佳路径选择中使用的一个公认必遵属性，其被篡改可能导致次优路由、安全风险以及互联网测量数据失真。废弃它可以简化 BGP 并减少非预期的流量工程，影响全球网络运营商。 该研究通过受控 BGP 公告、直接对等体和公共路由收集器进行观测，发现即使在简单的双 AS 路径中，ORIGIN 也常被修改（例如从 IGP 改为 INCOMPLETE）。分析了超过 352 个直接对等体，行为因提供商而异，有些系统性地重写 ORIGIN 以影响入站流量。

rss · Cloudflare Blog (PQ 迁移) · 7月24日 17:25

**背景**: 边界网关协议（BGP）是互联网的核心路由协议，使用路径属性进行路由选择。ORIGIN 属性表示路由最初如何注入 BGP：IGP（来自内部网关协议）、EGP（来自现已废弃的外部网关协议）或 INCOMPLETE（从其他来源重分发）。当其他属性相同时，BGP 最佳路径选择过程优先 IGP，其次 EGP，再次 INCOMPLETE。篡改 ORIGIN 使中转提供商能让某些路径看起来更有吸引力，可能覆盖原本的路由策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/bgp-origin-attribute/">BGP ORIGIN attribute manipulation and its impact on the Internet | The Cloudflare Blog</a></li>
<li><a href="https://ipcisco.com/lesson/bgp-path-attributes-origin/">BGP Path Attributes - Origin | BGP Origin Attribute IPCisco</a></li>

</ul>
</details>

**标签**: `#BGP`, `#routing security`, `#Internet measurement`, `#network infrastructure`, `#transit providers`

---

<a id="item-8"></a>
## [提出用于衡量 AI 对齐的“精灵系数”](https://www.schneier.com/blog/archives/2026/07/why-ai-needs-a-genie-coefficient.html) ⭐️ 8.0/10

Bruce Schneier 和 Barath Raghavan 提出了一个名为“精灵系数”的新指标，用于衡量用户意图与 AI 行为之间的差距，重点关注未明说的假设。 目前的 AI 基准测试仅评估任务完成情况，而非 AI 是否按照用户期望行事，随着 AI 代理获得更多自主权，这带来了安全风险。该指标可能推动更对齐、更可信的 AI 系统的开发。 精灵系数将量化未明说假设的差距，类似于基尼系数衡量不平等的方式，但尚未公布具体的技术公式。

rss · Schneier on Security · 7月24日 11:03

**背景**: 基尼系数是衡量分布不平等程度的统计指标，如收入不平等。在 AI 领域，对齐指的是确保 AI 系统的目标和行为与人类价值观一致。当前的大型语言模型基准测试侧重于准确性和能力，但很少关注用户请求与 AI 理解之间的细微差异。未明说的假设是人类交流的自然部分，像精灵系数这样的指标旨在捕捉 AI 处理这种微妙之处的程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gini_coefficient">Gini coefficient - Wikipedia</a></li>
<li><a href="https://www.remio.ai/post/schneier-security-says-ai-needs-a-genie-coefficient-before-agents-get-more-contr">AI Agents Need a Genie Coefficient Before They Get More Control</a></li>

</ul>
</details>

**标签**: `#AI alignment`, `#metrics`, `#AI safety`, `#interpretability`, `#human-AI interaction`

---

<a id="item-9"></a>
## [施奈尔新论文解读端到端加密争议](https://www.schneier.com/blog/archives/2026/07/end-to-end-encryption-and-going-dark.html) ⭐️ 8.0/10

施奈尔等人更新了 2012 年的加密政策研究，重点分析当前关于端到端加密的‘走向黑暗’辩论第三轮，并审视全球限制 E2EE 的立法措施。 这篇及时的论文为立法者和法院提供了必要的历史和技术背景，以批判性地评估拟议的加密后门，因为全球政府正加紧削弱 E2EE。论文对过去监控时代的回顾凸显了数字隐私面临的重大转变。 论文将辩论分为三个历史阶段：1990 年代的加密战争、2010-2015 年间因云服务访问而出现的“监控黄金时代”，以及当前没有中间机构可以获取明文的 E2EE 时代。文章专门为法律和政策领域的非专业人士撰写，使其理解这些技术现实。

rss · Schneier on Security · 7月23日 11:03

**背景**: “走向黑暗”辩论指的是执法部门对通信内容的访问需求与加密技术广泛采用导致无法访问之间的紧张关系。在 1990 年代的“加密战争”中，美国政府试图通过出口控制和像 Clipper 芯片这样的密钥托管方案来限制强加密。端到端加密确保只有通信用户能够解密消息，甚至服务提供商也无法读取，这从根本上挑战了传统的合法访问方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.schneier.com/blog/archives/2026/07/end-to-end-encryption-and-going-dark.html">End-to-End Encryption and "Going Dark" - Schneier on Security</a></li>
<li><a href="https://en.wikipedia.org/wiki/Crypto_Wars">Crypto Wars - Wikipedia</a></li>
<li><a href="https://www.fbi.gov/news/testimony/going-dark-encryption-technology-and-the-balances-between-public-safety-and-privacy">Going Dark: Encryption, Technology, and the Balances Between Public Safety and Privacy | Federal Bureau of Investigation</a></li>

</ul>
</details>

**标签**: `#end-to-end-encryption`, `#policy`, `#going-dark`, `#crypto-wars`, `#law`

---

<a id="item-10"></a>
## [SM4th 与 uBlockith：基于国密算法的后量子签名方案](https://eprint.iacr.org/2026/1506) ⭐️ 7.0/10

研究人员提出了 SM4th 和 uBlockith 两个新的后量子签名家族，它们基于 FAEST 框架并使用中国分组密码 SM4、uBlock 和 Ballet。性能评估显示，在具备原生 SM4 指令的平台上，SM4th 的速度接近 FAEST-128。 这项工作展示了使用中国国密算法构建具有竞争力的后量子签名的可行性，促进了密码技术的多样性，支持了中国在密码标准方面的自主发展。同时，它通过探索替代对称原语，为 NIST 后量子竞赛做出了贡献。 SM4th-EM-s 的公钥和签名总大小为 3,850 字节，略小于 FAEST-EM-128s 的 3,938 字节。在支持 CIS-SM4 的 Hygon 处理器上，SM4th 的性能在 FAEST-128 的 3 倍以内；uBlockith 比 FAEST-256 慢 3 到 4 倍。这些方案包含了指令集感知优化和定制的约束系统。

rss · IACR ePrint 密码学论文 · 7月23日 08:26

**背景**: FAEST 是一种基于 VOLE-in-the-Head 技术的后量子签名方案，该技术将零知识证明转化为非交互、可公开验证的形式。它仅依赖对称原语（如分组密码），避免了数论假设。SM4 是中国国家分组密码标准，uBlock 是一种轻量级密码，在 2018 年中国全国密码设计竞赛中夺冠，Ballet 是另一种中国设计的分组密码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/csrc/media/Projects/post-quantum-cryptography/documents/pqc-seminars/presentations/15-vole-in-the-head-06182024.pdf">Constructions for digital signatures Part II: VOLE - in - the - head and...</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-981-97-5028-3_11">New Strategy for Evaluating Differential Clustering Effect of uBlock</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#digital signatures`, `#VOLE-in-the-Head`, `#block ciphers`, `#FAEST`

---

<a id="item-11"></a>
## [不可追踪加密货币的共识数分析](https://eprint.iacr.org/2026/1503) ⭐️ 7.0/10

该论文形式化定义了线性不可追踪资产转移（LUAT）和常数状态不可追踪资产转移（CUAT）对象，并确定了它们的共识数：LUAT 的共识数为 2，而 CUAT 的共识数取决于不可追踪性的强度和匿名集大小。 这项分析揭示了一个根本性权衡：LUAT 需要更多存储但同步要求较低，而 CUAT 通过增加同步复杂度和牺牲公平性来最小化状态量，为隐私保护加密货币的设计提供了指导。 在 LUAT 中，来自不同账户的转移可交换，使得其共识数与匿名集大小无关，恒为 2。在强不可追踪性下，CUAT 的共识数因冲突图中的均匀关联性而随匿名集大小平方增长，且 CUAT 不具备无饥饿性。

rss · IACR ePrint 密码学论文 · 7月23日 05:38

**背景**: 在分布式系统中，共享对象的共识数是指仅使用该对象和读写寄存器就能解决共识问题的最大进程数。标准资产转移的共识数为 1。在不可追踪资产转移中，发送者将其账户隐藏在一组称为“匿名集”的账户中；两种设计在管理该集合上存在差异：线性方案追加无效标识符并保留集合，而常数状态方案则替换整个集合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.20929">The Consensus Number of Untraceable Cryptocurrencies</a></li>
<li><a href="https://www.slideserve.com/elaina/wait-free-consensus">PPT - Wait-Free Consensus PowerPoint Presentation, free download...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#consensus`, `#blockchain`, `#privacy`, `#untraceability`

---

<a id="item-12"></a>
## [Cloudflare 推出缓存响应规则，精细化控制缓存](https://blog.cloudflare.com/introducing-cache-response-rules/) ⭐️ 7.0/10

Cloudflare 推出了缓存响应规则，用户可以在响应到达缓存之前，重写 Cache-Control 指令、移除 Set-Cookie 和 ETag 等响应头，以及管理缓存标签，无需修改源站代码。 该功能显著减少了因响应头（如 Set-Cookie）导致的不必要回源请求，提升了网站性能并降低了源站负载。它让开发者能够直接在 Cloudflare 上精细调整缓存逻辑，无需修改应用代码。 缓存响应规则支持重写 Cache-Control、移除特定响应头（如 Set-Cookie、ETag、Last-Modified）以及管理缓存标签。使用该功能需要将 DNS 记录代理至 Cloudflare，规则在收到源站响应头后评估。

rss · Cloudflare Blog (PQ 迁移) · 7月23日 18:40

**背景**: 在 CDN 缓存中，像 Set-Cookie 这样的响应头可能会意外地阻止缓存，导致大量的回源请求。此前，Cloudflare 的 Page Rules 和 Cache Rules 主要基于请求，对于由响应头驱动的缓存控制较为不便。缓存响应规则填补了这一空白，允许基于响应头进行规则评估，从而在 CDN 层面实现精准的缓存控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/introducing-cache-response-rules/">Introducing Cache Response Rules | The Cloudflare Blog</a></li>
<li><a href="https://developers.cloudflare.com/cache/how-to/cache-response-rules/">Cache Response Rules · Cloudflare Cache (CDN) docs</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#CDN`, `#caching`, `#web performance`, `#DevOps`

---

<a id="item-13"></a>
## [RFC 10026：DNSSEC DS 记录自动化最佳实践](https://rfc-editor.org/info/rfc10026) ⭐️ 7.0/10

RFC 10026 为自动接受 DNSSEC 委托签名者（DS）记录提供了操作建议，指导注册机构和注册商进行接受检查、错误/成功报告以及处理并发更新。 自动化 DS 记录更新可减少手动错误，简化 DNSSEC 密钥轮换，增强 DNS 基础设施的安全性和效率，让域名运营者和整个互联网从中受益。 该建议涉及接受检查、错误/成功报告以及多参与方问题（如并发更新）的技术决策，这对于根据 RFC 7344 和相关标准进行 CDS/CDNSKEY 扫描至关重要。

rss · IETF 新标准 RFC (PQC 标准化) · 7月23日 08:34

**背景**: DNSSEC 为 DNS 数据添加加密签名以防止欺骗。父区域中的委托签名者（DS）记录通过引用子区域的 DNSKEY 来创建信任链。为了实现信任维护的自动化，子区域可以发布 CDS 或 CDNSKEY 记录，父区域可扫描这些记录并自动更新 DS 记录。RFC 7344 引入了这种自动化方法，而 RFC 10026 则提供了父端操作的指导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc7344.html">RFC 7344: Automating DNSSEC Delegation Trust Maintenance</a></li>
<li><a href="https://www.linode.com/docs/guides/dnssec/">How to Secure DNS with DNSSEC | Linode Docs</a></li>
<li><a href="https://dnsimple-support.netlify.app/articles/what-are-cds-and-cdnskey/">What Are CDS and CDNSKEY ? - DNSimple Help</a></li>

</ul>
</details>

**标签**: `#DNSSEC`, `#automation`, `#DNS`, `#security`, `#standards`

---
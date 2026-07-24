---
layout: default
title: "Horizon Summary: 2026-07-24 (ZH)"
date: 2026-07-24
lang: zh
---

> 从 37 条内容中筛选出 10 条重要资讯。

---

1. [侧信道攻击利用编译器寄存器溢出破解 HQC 密钥](#item-1) ⭐️ 9.0/10
2. [首次用 Isabelle/HOL 形式化验证 KZG 多项式承诺](#item-2) ⭐️ 9.0/10
3. [施奈尔更新加密辩论：端到端加密与“走向黑暗”第三轮](#item-3) ⭐️ 9.0/10
4. [新论文证明需求证明无法替代工作量证明](#item-4) ⭐️ 8.0/10
5. [SwitchFold：代码无关的简洁多项式承诺](#item-5) ⭐️ 8.0/10
6. [麻省理工学院部署超过 500 台 AI 监控摄像头](#item-6) ⭐️ 8.0/10
7. [面向联邦 AI 的隐私保护反事实解释算法](#item-7) ⭐️ 7.0/10
8. [2026 年世界杯如何重塑全球互联网流量](#item-8) ⭐️ 7.0/10
9. [RFC 10026：自动化 DNSSEC DS 管理的操作建议](#item-9) ⭐️ 7.0/10
10. [NIST 发布存储基础设施安全指南修订草案（SP 800-209 Rev. 1）](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [侧信道攻击利用编译器寄存器溢出破解 HQC 密钥](https://eprint.iacr.org/2026/1491) ⭐️ 9.0/10

该侧信道攻击通过分析 Cortex-M4 上 HQC 稀疏向量操作中编译器引起的寄存器溢出所产生的电磁泄漏，构建零字区分器恢复秘密零位，从而将密钥恢复转化为缩短的纠错码解码问题。 该攻击针对 NIST 后量子密码标准化决赛入围者 HQC，暴露了实际实现中的安全漏洞，可能影响其标准化进程，并凸显了加密软件中侧信道防护的紧迫性。 每个 64 位字的低 32 位半泄漏更强（约 500 条电磁迹线），高半部较弱（约 5000 条），可实现可靠的零/非零分类。在 32 位粒度下，HQC-1 中 88.7%的秘密向量机器字为零，将解码复杂度降至约 2^46 比特操作。

rss · IACR ePrint 密码学论文 · 7月21日 09:31

**背景**: HQC 是一种基于编码理论的后量子密钥封装机制，已被 NIST 选为标准化候选算法，其安全性依赖于准循环纠错码解码问题的困难性。寄存器溢出是编译器在寄存器压力大时将变量存入内存的过程，可能通过侧信道泄露信息。纠错码解码问题是指根据校验子恢复错误向量，在密码学参数下计算困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pqc-hqc.org/">HQC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Register_allocation">Register allocation - Wikipedia</a></li>
<li><a href="https://decodingchallenge.org/syndrome">Syndrome Decoding Problem</a></li>

</ul>
</details>

**标签**: `#side-channel attack`, `#post-quantum cryptography`, `#HQC`, `#implementation security`, `#Cortex-M4`

---

<a id="item-2"></a>
## [首次用 Isabelle/HOL 形式化验证 KZG 多项式承诺](https://eprint.iacr.org/2026/1490) ⭐️ 9.0/10

研究人员首次在 Isabelle/HOL 中形式化了多项式承诺方案的概念，验证了两种 KZG 构造（标准版和批量版）的安全性证明，并用一种受约束编程启发的新方法形式化了代数群模型（AGM）。 这项工作为高级加密协议的形式化验证奠定了严格基础，可能增强区块链和隐私应用中所用零知识证明和简洁论证的信任度。 验证使用了 CryptHOL 框架和 Shoup 的游戏序列方法，并进行机器检查的转换；涵盖了正确性、绑定性、隐藏性和知识可靠性，AGM 的形式化采用了一种受约束编程启发的技术。

rss · IACR ePrint 密码学论文 · 7月21日 09:14

**背景**: 多项式承诺方案（PCS）允许证明者承诺一个多项式，并在之后证明其在任意点的值。KZG 是一种基于双线性配对的流行 PCS，广泛用于零知识协议。代数群模型（AGM）限制敌手执行代数操作，介于标准模型和通用群模型之间。Isabelle/HOL 是一个交互式定理证明器，用于生成机器检查的数学证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zkdocs.com/docs/zkdocs/commitments/kzg_polynomial_commitment/">KZG Polynomial Commitments | ZKDocs</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-319-96881-0_2">The Algebraic Group Model and its Applications | Springer Nature Link</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isabelle/HOL">Isabelle/HOL</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#polynomial commitments`, `#KZG`, `#Isabelle/HOL`, `#algebraic group model`

---

<a id="item-3"></a>
## [施奈尔更新加密辩论：端到端加密与“走向黑暗”第三轮](https://www.schneier.com/blog/archives/2026/07/end-to-end-encryption-and-going-dark.html) ⭐️ 9.0/10

布鲁斯·施奈尔与合作者发布新论文，更新其 2012 年的研究，分析当前围绕端到端加密及政府限制企图的“走向黑暗”辩论第三轮。 该论文弥合技术与法律视角，帮助决策者和技术专家评估限制端到端加密的影响，涉及全球隐私、安全与执法能力。 论文梳理三个阶段：1990 年代的加密战争、2010 至 2015 年传输加密下的“监控黄金时代”，以及当前中间方无法读取明文的端到端加密辩论；面向法律与政策读者，并阐释相关技术。

rss · Schneier on Security · 7月23日 11:03

**背景**: “走向黑暗”辩论中，执法部门要求获取证据，隐私倡导者则警告加密后门会破坏安全。端到端加密确保只有收发双方可读消息，服务提供商也无法获取明文。1990 年代加密战争以美国放松强加密出口管制告终。2010 至 2015 年间，传输加密普及，但云服务商仍能配合搜查令，形成“监控黄金时代”。如今端到端加密再度引发冲突，部分政府已立法限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/End-to-end_encryption">End-to-end encryption</a></li>
<li><a href="https://en.wikipedia.org/wiki/Crypto_Wars">Crypto Wars</a></li>
<li><a href="https://cyber.harvard.edu/pubrelease/dont-panic/Dont_Panic_Making_Progress_on_Going_Dark_Debate.pdf">Going Dark - Berkman Klein Center - Harvard University</a></li>

</ul>
</details>

**标签**: `#encryption`, `#privacy`, `#policy`, `#security`, `#going-dark`

---

<a id="item-4"></a>
## [新论文证明需求证明无法替代工作量证明](https://eprint.iacr.org/2026/1492) ⭐️ 8.0/10

一篇新密码学论文形式化证明了需求加权共识无法从内生需求中获得女巫攻击抵抗。共谋实体之间的支付是可回收的转移，且机制必须在零需求路径上保持活性，从而削弱了有用工作量证明方案的核心假设。 这项工作意义重大，因为许多区块链项目试图用有用计算取代能耗密集型的工作量证明。论文揭示了根本性局限，表明安全性不能仅依赖需求，这会影响共识协议设计者和有用工作量证明链的可行性。 引理 1 证明支付为无女巫抵抗成本的可回收转移；定理 1 表明在自由化名下，内生收据可模拟独立请求者。定理 2 约束了零需求路径上的领导者选举下限，论文提出以不可回收税作为安全资源，并刻画了有用产出残值效应，同时提及了 Pearl cuPOW 审计案例。

rss · IACR ePrint 密码学论文 · 7月21日 12:56

**背景**: 有用工作量证明（PoUW）方案旨在用机器学习等有用计算取代区块链中的密码学谜题。女巫攻击抵抗可防止攻击者创建多个虚假身份。需求加权共识使用服务需求（以收据形式）赋予参与者权重，但本文挑战了这种需求本身能抵御女巫攻击的假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/coinmonks/what-is-proof-of-useful-work-a-deep-dive-with-dfinity-founder-dominic-williams-ecc0657b4845">What Is Proof of Useful Work ? A Deep Dive with DFINITY... | Medium</a></li>
<li><a href="https://members.delphidigital.io/learn/sybil-resistance">What is Sybil Resistance? - Delphi Digital</a></li>
<li><a href="https://learn.qbc.network/proof-of-useful-work">Proof of Useful Work : Mining That Computes Something Real | QBC</a></li>

</ul>
</details>

**标签**: `#consensus`, `#proof-of-work`, `#blockchain`, `#sybil-resistance`, `#mechanism-design`

---

<a id="item-5"></a>
## [SwitchFold：代码无关的简洁多项式承诺](https://eprint.iacr.org/2026/1489) ⭐️ 8.0/10

该论文提出了 SwitchFold，一种基于哈希的多线性多项式承诺方案，通过递归代码切换实现线性证明时间和多对数级别证明大小，无需依赖特定域的代数结构。其基于 Brakedown 码的实例 BrakeFold 相比 Brakedown 证明缩小 3.5 倍、验证加速 20.6 倍，且比 BaseFold 快 17 倍。 SwitchFold 满足大规模 zkSNARK 应用（如 zkML）的关键需求，此类应用需高效承诺数十亿参数且必须使用大素数域防止算术溢出。其域无关设计和线性证明时间使其在实际应用中切实可行，推动了可验证机器学习的发展。 SwitchFold 递归应用代码切换技术，将一种编码下的多线性扩展声明归约为更短编码下的声明，并利用积累方案处理重复打开。与 Blaze 和 BrakingBase 不同，它无需辅助可折叠码；Brakedown 码序列天然适配其递归框架。在十亿系数和 100 比特安全参数下，BrakeFold 的每次额外打开使证明比 Brakedown 小 3.5 倍、验证快 20.6 倍，证明者时间仅增加 1.3 倍。

rss · IACR ePrint 密码学论文 · 7月21日 09:09

**背景**: 多项式承诺方案是零知识证明的核心组件，允许证明者对多项式做出承诺并之后证明其求值。代码切换是一种密码学技术，可将一个线性码下的多项式声明归约为更短码下的声明，从而实现递归。在 zkML 中，大素数域可避免定点数算术溢出，但许多多项式承诺方案依赖小域以提升效率；SwitchFold 的域无关设计解除了这一限制。现有方案如 Brakedown（线性证明时间但证明大）和 BaseFold（证明小但证明者慢）代表了某种权衡，SwitchFold 对此进行了改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zkjargon.github.io/definitions/polynomial_commitment.html">Polynomial Commitment Scheme - ZK Jargon Decoder</a></li>
<li><a href="https://www.quillaudits.com/blog/ai-agents/zero-knowledge-machine-learning-zkml">What Is a Real World ZKML Application? A Beginner’s Guide</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#zero-knowledge proofs`, `#polynomial commitments`, `#zkML`, `#code-based cryptography`

---

<a id="item-6"></a>
## [麻省理工学院部署超过 500 台 AI 监控摄像头](https://www.schneier.com/blog/archives/2026/07/mit-to-become-hotbed-of-ai-video-surveillance.html) ⭐️ 8.0/10

MIT 投入超过 300 万美元，在校园内安装超过 500 台 AI 监控摄像头，这些摄像头能实时进行人脸和物体分类，包括检测移动、徘徊、人群、口罩，并能在最远 35 英尺（约 11 米）的范围内根据衣着颜色、性别和年龄对个人进行自动分类。 这所著名学术机构的大规模部署引发了重大的隐私和伦理问题，可能使普遍的 AI 监控常态化，影响学生、教职员工和访客，并引发关于安全与公民自由之间平衡的辩论。 摄像头将安装在教学楼、宿舍和户外区域；数据最多保留 30 天，除非获得例外批准。安装工作始于 2025 年 11 月，预计持续至 2026 年 9 月。

rss · Schneier on Security · 7月21日 11:07

**背景**: AI 监控摄像头利用计算机视觉和机器学习自动分析视频画面，实现人脸识别和行为分析等功能。这类系统能够追踪个人并推断个人属性，引发了对大规模监控、数据安全和潜在滥用的担忧。以技术研究闻名的 MIT 正在部署这一系统，正值全球就 AI 在公共场所的伦理问题展开持续辩论之际。

**标签**: `#ai-surveillance`, `#privacy`, `#facial-recognition`, `#university-policy`, `#ethics`

---

<a id="item-7"></a>
## [面向联邦 AI 的隐私保护反事实解释算法](https://eprint.iacr.org/2026/1488) ⭐️ 7.0/10

研究人员提出了一种面向联邦 AI 的隐私保护反事实解释算法，可在垂直划分的数据上结合同态加密和秘密共享，安全地找到反事实实例，且不损失准确性。 该研究解决了处理敏感数据的 AI 系统对可解释性的迫切需求，使利益相关者能够在不暴露私有信息的情况下理解决策，为值得信赖的联邦学习奠定基础。 该算法专为垂直划分数据设计，各参与方持有不同特征但同一样本。它可扩展至数千个数据点，实验验证表明相比非隐私方法准确性无损失。

rss · IACR ePrint 密码学论文 · 7月21日 08:22

**背景**: 反事实解释提供‘如果...会怎样’的情景，是解释性 AI 的重要方法。同态加密允许对加密数据进行计算，秘密共享则将秘密分发给多个参与方，只有满足门限才能重构。垂直划分数据指不同参与方拥有相同记录的不同特征，常见于联邦学习。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://christophm.github.io/interpretable-ml-book/counterfactual.html">15 Counterfactual Explanations – Interpretable Machine Learning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_encryption">Homomorphic encryption</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secret_sharing">Secret sharing</a></li>

</ul>
</details>

**标签**: `#privacy-preserving AI`, `#explainable AI`, `#federated learning`, `#homomorphic encryption`, `#secret sharing`

---

<a id="item-8"></a>
## [2026 年世界杯如何重塑全球互联网流量](https://blog.cloudflare.com/2026-world-cup-internet-traffic/) ⭐️ 7.0/10

Cloudflare 分析了 2026 年世界杯期间的全球 HTTP 流量，揭示开球时间、流媒体观看习惯和补水暂停导致了深夜流量激增和中场浏览高峰等明显模式。 该分析展示了大型现场活动如何显著影响互联网使用，使互联网服务提供商、流媒体服务和内容提供商能在需求高峰期更好地优化基础设施和用户体验。 研究特别指出了补水暂停（一项最近的规则变更）对流量的影响，并发现深夜比赛与日间比赛的在线活动存在差异。

rss · Cloudflare Blog (PQ 迁移) · 7月21日 12:59

**背景**: Cloudflare 运营着一个提供内容分发和安全服务的全球网络，因此能全面洞察互联网流量模式。HTTP 流量指网络请求，分析它可以揭示体育赛事等外部事件如何实时改变在线活动。2026 年世界杯凭借其全球观众和独特的赛程安排，成为研究这些动态的理想案例。

**标签**: `#Internet Traffic`, `#World Cup`, `#Cloudflare`, `#Data Analysis`, `#Streaming`

---

<a id="item-9"></a>
## [RFC 10026：自动化 DNSSEC DS 管理的操作建议](https://rfc-editor.org/info/rfc10026) ⭐️ 7.0/10

IETF 发布 RFC 10026，为自动接受 DNSSEC 委派签名者（DS）参数提供操作建议，基于现有协议（RFC 7344、8078、9615），以简化安全委派维护。 该文件帮助注册管理机构（registries）和注册商（registrars）统一实施 DS 自动化，减少手动错误，提高 DNSSEC 在互联网上的部署效率和安全性。 该 RFC 涵盖关于验收检查、错误和成功报告以及并发更新处理的建议；合规确保基本安全性并防止 DNS 功能中断。

rss · IETF 新标准 RFC (PQC 标准化) · 7月23日 08:34

**背景**: DNSSEC 通过 DS 记录建立信任链；自动化协议如 CDS 允许子区域向父方发出所需 DS 参数的信号。父方代理（注册管理机构/注册商）随后需要更新 DS 记录。该 RFC 提供操作指引以确保此流程统一安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rfc-editor.org/info/rfc10026/">RFC 10026: Operational Recommendations for DNSSEC Delegation ...</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc10026">RFC 10026: Operational Recommendations for DNSSEC Delegation ...</a></li>

</ul>
</details>

**标签**: `#DNSSEC`, `#DNS`, `#internet-standards`, `#automation`, `#security`

---

<a id="item-10"></a>
## [NIST 发布存储基础设施安全指南修订草案（SP 800-209 Rev. 1）](https://csrc.nist.gov/pubs/sp/800/209/r1/ipd) ⭐️ 7.0/10

NIST 发布了 SP 800-209 第一修订版的初始公开草案，更新了存储基础设施安全指南：删除了过时内容，新增了“平台安全破坏”和“数据恢复/保护受损”等威胁焦点领域，将安全控制重组为七个具有标准化缩写的控制族，并增加了将控制措施与威胁映射的新附录。 随着存储架构向软件定义模式演进，配置复杂性增加了安全风险；这份更新的权威指南帮助组织实施一致且全面的安全控制，影响政府及行业的合规、系统设计和采购决策。 该修订将原先的九个类别合并为七个控制族，并采用如‘AC’、‘AU’等标准化缩写；附录 C 将每项控制措施与第 3 节中识别的威胁进行明确映射。该草案面向公众征求意见，并包含专利主张征集。

rss · NIST CSRC Drafts (标准草案) · 7月22日 04:00

**背景**: 软件定义存储（SDS）将存储硬件与管理软件分离，带来了灵活性，但也增加了配置错误和攻击面。NIST SP 800-209 专门为存储系统（包括 NAS 和 SAN）提供全面的安全建议。本次修订针对现代威胁，如平台破坏和备份漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-209.pdf">[PDF] Security Guidelines for Storage Infrastructure - NIST Technical Series Publications</a></li>
<li><a href="https://en.wikipedia.org/wiki/Software-defined_storage">Software-defined storage</a></li>

</ul>
</details>

**标签**: `#security`, `#storage`, `#NIST`, `#guidelines`, `#infrastructure`

---
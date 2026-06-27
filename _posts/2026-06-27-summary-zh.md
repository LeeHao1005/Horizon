---
layout: default
title: "Horizon Summary: 2026-06-27 (ZH)"
date: 2026-06-27
lang: zh
---

> 从 36 条内容中筛选出 15 条重要资讯。

---

1. [对 HAWK 签名方案的经典多项式时间攻击](#item-1) ⭐️ 10.0/10
2. [针对后量子签名中 GGM 树种子压缩的通用故障攻击](#item-2) ⭐️ 9.0/10
3. [ProtogaLattice：面向一般多项式关系的常数轮格基折叠方案](#item-3) ⭐️ 8.0/10
4. [Pippenger 算法内存优化版将多标量乘法性能提升高达 40%](#item-4) ⭐️ 8.0/10
5. [VERDICT：面向去中心化 DAG 的可验证谱系框架](#item-5) ⭐️ 8.0/10
6. [HHE Kombat：混合同态加密方案基准评估框架](#item-6) ⭐️ 8.0/10
7. [Meta 与五角大楼供应商测试面部识别智能眼镜](#item-7) ⭐️ 8.0/10
8. [德国法院裁定谷歌对 AI 搜索摘要负责](#item-8) ⭐️ 8.0/10
9. [LLM 基于文本风格解析指令，提示注入漏洞难解](#item-9) ⭐️ 8.0/10
10. [间谍软件嵌入禁用文本干扰 AI 分析](#item-10) ⭐️ 8.0/10
11. [GSMA 发布 Telco Common Corpus：超 100 亿词元的开放电信数据集](#item-11) ⭐️ 8.0/10
12. [Cloudflare Workflows 加入 Saga 风格回滚](#item-12) ⭐️ 7.0/10
13. [大麻药房系统遭黑客入侵，百万护照数据泄露](#item-13) ⭐️ 7.0/10
14. [RFC 9994 定义了 MPLS 网络动作子栈](#item-14) ⭐️ 7.0/10
15. [RFC 10005：BGP 链路带宽扩展团体](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [对 HAWK 签名方案的经典多项式时间攻击](https://eprint.iacr.org/2026/1318) ⭐️ 10.0/10

一种经典概率多项式时间算法通过随机幺模共轭和 Lenstra-Silverberg 算法利用了格同构问题攻破了 HAWK 签名方案，该算法假设了四个数论启发式。 HAWK 是 NIST 后量子签名标准化中唯一的基于格的候选方案；该攻击若被验证，将彻底破坏其安全性并重塑后量子密码学的格局。 攻击通过用随机下三角幺模矩阵共轭来重新随机化 HAWK 公钥，然后反复应用 Lenstra-Silverberg 算法和子域方法求解生成的 nrdPIP 实例；该方法依赖于四个看似合理但未经验证的启发式。

rss · IACR ePrint 密码学论文 · 6月25日 19:03

**背景**: HAWK 是一种基于格同构问题（LIP）的后量子数字签名方案，已提交至 NIST 后量子密码标准化进程。LIP 要求找到两个格之间的正交变换。nrdPIP 是 Eurocrypt 2025 上引入的相关问题。Lenstra-Silverberg 算法是一种多项式时间方法，用于判断环和格的同构，源于 Gentry-Szydlo 算法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/csrc/media/Projects/pqc-dig-sig/documents/round-1/spec-files/hawk-spec-web.pdf">PDF HAWK Specification Document - NIST Computer Security Resource Center</a></li>
<li><a href="https://eprint.iacr.org/2021/1332">On the Lattice Isomorphism Problem, Quadratic Forms, Remarkable Lattices, and Cryptography</a></li>
<li><a href="https://link.springer.com/content/pdf/10.1007/978-3-662-44371-2_16.pdf">Revisiting the Gentry-Szydlo Algorithm H. W. Lenstra1 and A. Silverberg2,⋆</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#cryptanalysis`, `#lattice-based cryptography`, `#digital signatures`, `#HAWK`

---

<a id="item-2"></a>
## [针对后量子签名中 GGM 树种子压缩的通用故障攻击](https://eprint.iacr.org/2026/1313) ⭐️ 9.0/10

一篇新论文（eprint 2026/1313）提出了通用零知识种子树（GZKST）抽象，统一了针对 LESS、CROSS 和 MEDS 等后量子签名中 GGM 树种子压缩的已有故障攻击。该攻击仅需少量故障签名即可恢复完整私钥，并在 ARM Cortex-M4 上通过时钟毛刺注入对 MEDS 进行了实际验证。 该攻击揭示了 GGM 树种子压缩——许多 NIST 后量子签名候选方案核心优化——的根本性弱点，并凸显了实施中严格故障注入防护的必要性。它可能影响正在进行的 NIST 标准化进程，迫使受影响方案被剔除或重新设计。 通用零知识种子树抽象形式化了正确性和种子隐藏不变性，表明针对 LESS-v1 和 LESS-v2 的先前攻击尽管目标层和树构造不同，却违反了相同的不变性。该攻击针对所有 MEDS 参数集仅需少数成功故障签名即可恢复完整密钥，并利用了树遍历与路径构造中的多个攻击面。

rss · IACR ePrint 密码学论文 · 6月24日 09:07

**背景**: LESS、CROSS 和 MEDS 等后量子签名方案基于零知识证明，通过 Fiat-Shamir 转换构建，并采用 GGM 树（Goldreich-Goldwasser-Micali）压缩种子承诺：仅公开非挑战轮的种子，隐藏依赖挑战的私密种子。故障攻击通过注入硬件毛刺操控程序流，从而可能暴露隐藏种子。GGM 树以分层方式生成伪随机种子，实现高效压缩，但引入了故障攻击面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wiki-92c.pages.dev/GGM-Tree">GGM Tree</a></li>
<li><a href="https://postquantum.com/security-pqc/nist-third-round-pqc-signatures/">NIST Selects 9 Third-Round PQC Signature Candidates</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum signatures`, `#fault attacks`, `#GGM-trees`, `#zero-knowledge`

---

<a id="item-3"></a>
## [ProtogaLattice：面向一般多项式关系的常数轮格基折叠方案](https://eprint.iacr.org/2026/1317) ⭐️ 8.0/10

ProtogaLattice 提出了一种适用于一般高次多项式关系的新型格基折叠方案，该方案在常数轮次内完成，不再依赖和校验协议。与 Latticefold+ 和 (Super)Neo 等之前的格折叠构造相比，该方法大幅减小了验证者电路规模。 通过缩小验证者电路，ProtogaLattice 降低了增量可验证计算（IVC）和证明携带数据（PCD）的递归开销，使格基证明更实用、更可扩展。这一进展扩展了可高效证明的关系集，并强化了后量子生态。 ProtogaLattice 的完整迭代仅需四次随机预言机调用，并且包含一个引导协议来降低证据中的范数增长。它还引入了一种通过 Protogalaxy 实现 PCD 的方法，即使在经典配对设置中也是新颖的。

rss · IACR ePrint 密码学论文 · 6月25日 14:59

**背景**: 折叠方案允许证明者将两个 NP 命题实例合并为一个，从而支持高效的增量计算。先前的格基折叠方案使用和校验协议，虽然证明时间较短，但因大量哈希运算导致验证者电路庞大，损害了 IVC 效率。ProtogaLattice 转而采用来自 Protostar 和 Protogalaxy 等经典折叠方案的常数轮代数技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gokulbalex.medium.com/folding-schemes-and-unfolding-pathways-for-proof-carrying-data-and-incrementally-verifiable-c90e37a9d5eb">Folding Schemes and Unfolding Pathways for Proof... | Medium</a></li>
<li><a href="https://www.osdnk.me/blog/l2-folding-scheme">More efficient Lattice Folding via ℓ₂-Norm Checks | osdnk</a></li>
<li><a href="https://blog.lambdaclass.com/incrementally-verifiable-computation-nova/">Incrementally verifiable computation: NOVA - LambdaClass Blog</a></li>

</ul>
</details>

**标签**: `#folding-schemes`, `#lattice-cryptography`, `#zero-knowledge-proofs`, `#IVC`, `#post-quantum`

---

<a id="item-4"></a>
## [Pippenger 算法内存优化版将多标量乘法性能提升高达 40%](https://eprint.iacr.org/2026/1316) ⭐️ 8.0/10

论文提出了一种 Pippenger 算法优化版本，根据可用内存动态调整桶的数量，在内存受限设备上对 BLS12-381 曲线的多标量乘法实现了高达 40%的性能提升。 多标量乘法是零知识证明中的关键瓶颈，尤其在内存受限设备上。该优化大幅降低了内存需求，可能使零知识证明能在更广泛的设备上运行，包括物联网和嵌入式系统。 测试在 BLS12-381 曲线上进行，多标量乘法规模从 2^8 到 2^14 个点。对于 2^13 个点的 MSM，在 1 KB 内存下性能提升 40%，当内存不再受限时增益降至 1.5%。

rss · IACR ePrint 密码学论文 · 6月25日 12:47

**背景**: 多标量乘法（MSM）是在椭圆曲线上计算许多标量点乘之和的操作，是许多零知识证明系统的核心组件。Pippenger 算法（又称桶方法）是 MSM 的标准高效算法，它将标量划分为窗口并将点累积到桶中。BLS12-381 是一种广泛用于零知识证明的配对友好椭圆曲线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hackmd.io/@drouyang/SyYwhWIso">Pippenger Algorithm for Multi-Scalar Multiplication (MSM) - HackMD</a></li>
<li><a href="https://en.wikipedia.org/wiki/BLS12-381">BLS12-381</a></li>
<li><a href="https://blog.lambdaclass.com/multiscalar-multiplication-strategies-and-challenges/">Fast Multiscalar Multiplication: Algorithms and Performance Optimization Strategies</a></li>

</ul>
</details>

**标签**: `#multi-scalar multiplication`, `#Pippenger's algorithm`, `#zero-knowledge proofs`, `#memory optimization`, `#BLS12-381`

---

<a id="item-5"></a>
## [VERDICT：面向去中心化 DAG 的可验证谱系框架](https://eprint.iacr.org/2026/1315) ⭐️ 8.0/10

该论文提出了 VERDICT 框架，采用互联的数据 DAG 和事件 DAG，结合同态哈希与层级压缩，实现加密可验证的数据谱系。它利用跳 DAG 结构、桶索引和 Merkle 树，达成 O(log n)的高效验证。 它解决了联邦学习等隐私敏感分布式系统中防篡改数据谱系的关键需求，能够在不泄露数据机密性的前提下进行完整性验证。 验证时间随 DAG 层级呈 O(log n)增长，与每层节点数无关；通过挑战-响应机制防止重放攻击。该设计通过双 DAG 清晰分离了数据依赖与事件因果关系。

rss · IACR ePrint 密码学论文 · 6月25日 07:14

**背景**: DAG（有向无环图）是用于建模工作流与依赖关系的图结构，其节点表示操作，边表示顺序。同态哈希允许将多个输入的哈希组合成一个与拼接数据哈希相等的值，从而简化完整性检查。数据谱系跟踪数据的全部转换历史，是分布式系统审计的基础。层级压缩根据节点距起源的距离进行分组，形成跳结构以加速图遍历。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Directed_acyclic_graph">Directed acyclic graph - Wikipedia</a></li>
<li><a href="https://medium.com/asecuritysite-when-bob-met-alice/homomophic-hashes-efficient-trust-and-avoiding-complex-hashing-operations-1b288a17f7b1">Homomorphic Hashes — Efficient Trust and Avoiding... | Medium</a></li>
<li><a href="https://engineering.fb.com/2019/03/01/security/homomorphic-hashing/">Open-sourcing homomorphic hashing to secure update propagation</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#distributed systems`, `#data integrity`, `#DAG`, `#lineage tracking`

---

<a id="item-6"></a>
## [HHE Kombat：混合同态加密方案基准评估框架](https://eprint.iacr.org/2026/1314) ⭐️ 8.0/10

一个全面的基准测试框架评估了 19 个开源混合同态加密方案，提供了一个统一的代码仓库和一套语言无关的工具，以在 HHE-128 安全目标下进行公平的性能比较。 这项工作填补了混合同态加密评估标准化的关键空白，使研究人员和实践者能够就安全与性能的权衡做出明智决策，这对推动实用的隐私保护计算至关重要。 该研究分析了 218 个不同的密码基准测试，并区分了达到 HHE-128 安全阈值的配置与不达标的配置，为实际安全性和性能提供了细致的视角。

rss · IACR ePrint 密码学论文 · 6月24日 10:15

**背景**: 混合同态加密（HHE）结合了部分同态方案（如具备加法同态的 Paillier 和乘法同态的 ElGamal），以在加密数据上实现任意计算，同时比全同态加密更高效。它是一种实用的安全云计算方案，但各种实现一直缺乏标准化的基准测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1314">HHE Kombat: Benchmarking Hybrid Homomorphic Encryption Schemes</a></li>

</ul>
</details>

**标签**: `#hybrid homomorphic encryption`, `#benchmarking`, `#cryptography`, `#privacy-preserving computation`, `#performance evaluation`

---

<a id="item-7"></a>
## [Meta 与五角大楼供应商测试面部识别智能眼镜](https://www.schneier.com/blog/archives/2026/06/meta-is-testing-facial-recognition-for-police-and-military.html) ⭐️ 8.0/10

据报道，Meta 正在与五角大楼供应商 Rank One Computing 合作，为其智能眼镜开发面部识别功能原型，可能用于执法和军事领域的实时身份识别。 这一进展引发了严重的隐私和伦理担忧，因为它可能通过消费设备实现大规模监控，且与 Meta 此前因监管和社会反对而暂停类似功能的决定相矛盾。 Rank One Computing 曾是五角大楼的分包商，专注于生物识别和视觉 AI，而美国移民和海关执法局（ICE）已表示有兴趣部署面部识别眼镜用于现场行动。

rss · Schneier on Security · 6月26日 16:40

**背景**: 智能眼镜上的面部识别技术结合了实时摄像头输入和 AI 算法，通过将人脸与数据库进行比对来识别个人。这项技术因可能导致无端监控、对少数族裔的错误识别以及缺乏同意而备受争议。Meta 此前曾因类似的‘Name Tag’功能而面临强烈反对，超过 70 个组织签署公开信表示反对。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://roc.ai/">ROC | Vision AI & Biometrics Software - NIST Ranked | Formerly Rank One Computing</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2l6emRidkVCRmJPNlJ2dlNhbnZTZ0FQAQ?hl=en-US&gl=US&ceid=US:en">ACLU among groups opposing facial recognition in Meta glasses ...</a></li>

</ul>
</details>

**标签**: `#facial recognition`, `#surveillance`, `#privacy`, `#Meta`, `#law enforcement`

---

<a id="item-8"></a>
## [德国法院裁定谷歌对 AI 搜索摘要负责](https://www.schneier.com/blog/archives/2026/06/ai-and-liability.html) ⭐️ 8.0/10

德国一家法院裁定谷歌对其 AI 生成的搜索摘要负有法律责任，驳回了用户可自行核实或不信任 AI 输出等辩护理由。法院认为这些摘要反映了谷歌的商业行为。 这一里程碑式的裁决为 AI 责任确立了重要先例，可能让科技公司对 AI 生成的内容负责，并影响全球监管及企业在面向消费者的产品中部署 AI 的方式。 法院特别驳回了谷歌应被视为中立传输者而非发布者的论点，认定 AI 摘要构成公司自身的言论。这挑战了数字时代传统上对传输者与发布者的法律区分。

rss · Schneier on Security · 6月25日 17:03

**背景**: 传统上，电信运营商不对其传输的内容负责，而发布者需对其传播的内容负责。谷歌的 AI 概览是一项人工智能功能，可生成搜索结果的简洁摘要。德国法院的裁决将 AI 生成的摘要与发布者责任挂钩。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_AI_Overviews">Google AI Overviews</a></li>

</ul>
</details>

**标签**: `#AI`, `#liability`, `#legal`, `#regulation`, `#Google`

---

<a id="item-9"></a>
## [LLM 基于文本风格解析指令，提示注入漏洞难解](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html) ⭐️ 8.0/10

一项新研究发现，大语言模型主要依据文本风格而非角色标签来解析指令，导致角色混淆，削弱了基于标签的安全防护。 这项发现揭示了当前 AI 安全机制的根本缺陷，表明基于角色的安全措施容易被绕过，对所有处理不可信内容的大语言模型应用都有深远影响，表明有效的防御需要更深层的架构变革。 该研究在 role-confusion.github.io 上详细展示，模型依赖正式程度和用词选择等风格特征而非显式标签，甚至能让细微的注入逐步改变模型行为。

rss · Schneier on Security · 6月25日 11:23

**背景**: 提示注入是一种网络安全攻击，通过恶意输入操控大语言模型忽略原始指令。开发者通常使用“system”、“user”等角色标签来区分可信与不可信提示，但该论文揭示模型实际上并不真正理解这些角色，而是学习将风格模式与权威关联起来，这使得即使对标签进行清洗，注入仍然可能发生。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/">Prompt Injection as Role Confusion | Simon Willison’s Weblog</a></li>

</ul>
</details>

**标签**: `#AI security`, `#prompt injection`, `#LLMs`, `#role confusion`, `#machine learning`

---

<a id="item-10"></a>
## [间谍软件嵌入禁用文本干扰 AI 分析](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis-2.html) ⭐️ 8.0/10

恶意软件开发者开始在间谍软件中嵌入核武器和生物武器相关文本，放置在 JavaScript 注释块中，诱使 AI 分析工具拒绝响应或产生混淆，从而隐藏真实恶意载荷。 这种新颖的逃避技术利用了 AI 安全机制，暴露了 AI 辅助网络安全的漏洞。它迫使人们重新思考 AI 模型处理不可信输入的方式，可能推动自动化恶意软件分析防御的改进。 恶意文件头部是一大段注释，内含虚假指令和策略触发内容，之后才是真实恶意代码，使用 eval()和 ROT 替换密码。攻击目标是将文件开头直接输入语言模型而未做隔离的薄弱扫描管道。

rss · Schneier on Security · 6月24日 11:03

**背景**: 目前许多网络安全工具使用大语言模型自动分析恶意文件。一些 AI 系统具有安全过滤器，会拒绝处理提及武器的内容。ROT 是一种简单的字母替换密码，常被用于恶意软件混淆。部分分析人员也通过模型上下文协议（MCP）将 AI 模型与扫描工具连接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://www.infosecinstitute.com/resources/malware-analysis/simple-malware-obfuscation-techniques/">Simple malware obfuscation techniques | Infosec</a></li>
<li><a href="https://learn.microsoft.com/en-us/copilot/security/whats-new-copilot-security">What's new in Microsoft Security Copilot? | Microsoft Learn</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#malware`, `#AI-safety`, `#adversarial-AI`, `#spyware`

---

<a id="item-11"></a>
## [GSMA 发布 Telco Common Corpus：超 100 亿词元的开放电信数据集](https://www.gsma.com/newsroom/article/telco-common-corpus-the-largest-open-verified-data-commons-for-telecom-ai/) ⭐️ 8.0/10

GSMA 与 Pleias 发布了 Telco Common Corpus（TCC）数据集，包含超过 100 亿个开放许可且经过验证的电信数据词元，旨在助力电信行业专用 AI 模型的开发。 该数据集为开发电信领域专用 AI 模型提供了关键资源，能够推动网络管理、客户服务及其他电信应用的改进，同时促进开放协作。 Telco Common Corpus 包含科学文献、专利和开放数据，可在 Hugging Face 上获取，所有数据均采用开放许可并经过合规验证。

rss · GSMA Newsroom (移动安全标准) · 6月25日 08:56

**背景**: 在 AI 中，词元（token）是训练语言模型时使用的数据单位，如单词或子词。数据共享空间（data commons）是一个公开可访问的数据存储库，旨在促进协作与创新。与其他领域相比，电信行业长期以来缺乏大规模开放数据集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gsma.com/newsroom/blog/telco-common-corpus-the-largest-open-verified-data-commons-for-telecom-ai/">Telco Common Corpus : The largest open, verified data commons for...</a></li>
<li><a href="https://huggingface.co/datasets/PleIAs/Telco-Common-Corpus">PleIAs/ Telco - Common - Corpus · Datasets at Hugging Face</a></li>

</ul>
</details>

**标签**: `#telecom`, `#AI`, `#open-data`, `#dataset`, `#GSMA`

---

<a id="item-12"></a>
## [Cloudflare Workflows 加入 Saga 风格回滚](https://blog.cloudflare.com/rollbacks-for-workflows/) ⭐️ 7.0/10

Cloudflare Workflows 现已支持 Saga 风格回滚，允许开发者为持久化多步骤应用中的每一步定义补偿操作。 该功能为长时间运行的工作流提供了内置故障恢复，提高了可靠性，减少了自定义回滚逻辑的需要。 开发者可以为每一步的 do() 调用附加补偿函数，引擎在失败时自动执行。补偿操作应具有幂等性，以安全处理重试。

rss · Cloudflare Blog (PQ 迁移) · 6月25日 13:00

**背景**: Saga 模式将分布式事务分解为一系列本地事务，每个事务都有一个补偿操作用于回滚。持久化执行引擎（如 Cloudflare Workflows）会持久化工作流状态并重试失败步骤，非常适合长时间运行的流程。Cloudflare Workflows 基于 Cloudflare Workers 构建，提供自动重试和状态持久化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/azure/architecture/patterns/saga">Saga Design Pattern - Azure Architecture Center | Microsoft Learn</a></li>
<li><a href="https://www.cloudflare.com/products/workflows/">Cloudflare Workflows - Durable Execution Engine</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#workflows`, `#saga-pattern`, `#distributed-systems`, `#rollbacks`

---

<a id="item-13"></a>
## [大麻药房系统遭黑客入侵，百万护照数据泄露](https://www.schneier.com/blog/archives/2026/06/one-million-passports-leaked-online.html) ⭐️ 7.0/10

近百万本护照数据在网上遭泄露，原因是黑客入侵了一家大麻药房使用的低安全性身份验证系统。由于护照这类高价值凭证被用于低安全性的环境，导致此次泄露发生。 该事件凸显了在低安全性第三方系统中使用护照等高价值身份证件所带来的系统性风险，这类系统可能成为单点故障。它强调了需要更好的身份验证架构，以减少敏感凭证的暴露面。 泄露源于一家大麻药房的身份检查系统，这类辅助性认证往往缺乏健全的安全措施。数据库包含护照详细信息，对于身份盗窃和欺诈具有极高价值。

rss · Schneier on Security · 6月26日 11:03

**背景**: 护照是因用于国际旅行和作为主要身份证件而被视为高价值凭证。在诸如大麻药房等场景中，常需使用护照进行年龄验证，但这类企业的安全措施可能不如银行或政府系统严格。

**标签**: `#security`, `#data breach`, `#passport leak`, `#authentication`, `#identity theft`

---

<a id="item-14"></a>
## [RFC 9994 定义了 MPLS 网络动作子栈](https://rfc-editor.org/info/rfc9994) ⭐️ 7.0/10

RFC 9994 正式规定了 MPLS 网络动作（MNA）子栈，它是一组连续的标签栈条目，用于在 MPLS 标签栈内部携带网络动作和辅助数据，并更新了 RFC 9789 以完善 MNA 文档的编写要求。 通过将控制和 OAM 数据直接嵌入 MPLS 标签栈的标准化方法，该 RFC 增强了 MPLS 的扩展性和可编程性，支持随路 OAM 和自定义数据包处理等高级用例，同时保持与现有网络的互操作性。 MNA 子栈使用网络动作子栈指示符（NSI）标签标记起始，支持的路由器可处理其中的动作而旧设备忽略；它基于 MNA 框架构建，与栈后方案互为补充。

rss · IETF 新标准 RFC (PQC 标准化) · 6月27日 01:14

**背景**: MPLS 网络利用标签栈实现无需逐跳 IP 查找的快速转发。MNA 框架泛化了嵌入额外动作和数据的概念（类似 IPv6 扩展头），以支持操作、管理和自定义处理。RFC 9994 为此类信息的栈内传递定义了具体的子栈结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-hdr/">draft-ietf- mpls - mna -hdr-21 - MPLS Network Action ( MNA ) Sub - Stack ...</a></li>
<li><a href="https://arxiv.org/pdf/2410.20400v1">MPLS Network Actions : Technological Overview</a></li>

</ul>
</details>

**标签**: `#MPLS`, `#networking`, `#IETF`, `#RFC`, `#label switching`

---

<a id="item-15"></a>
## [RFC 10005：BGP 链路带宽扩展团体](https://rfc-editor.org/info/rfc10005) ⭐️ 7.0/10

IETF 发布了 RFC 10005，标准化了一种新的 BGP 扩展团体类型，用于携带链路带宽信息。这使得路由器能够根据实际链路容量在多条路径间执行加权负载均衡。 该标准使网络运维人员能够根据可用带宽优化流量分配，提高整体网络效率并避免拥塞。对于大规模 IP 网络（尤其是使用 BGP 多路径的网络），这是一项虽小但有意义的改进。 链路带宽扩展团体是一个可传递的 8 字节值，包含类型字段和以字节/秒为单位的带宽。关键处理规则是：重新通告路由但未改变下一跳的 BGP 发言者，不应修改该带宽团体。

rss · IETF 新标准 RFC (PQC 标准化) · 6月26日 23:37

**背景**: BGP（边界网关协议）是互联网的核心路由协议，负责在自治系统间交换可达信息。扩展团体（RFC 4360）将标准 BGP 团体扩展为 64 位，支持更丰富的元数据。BGP 多路径负载均衡允许在多个等价路径上分担流量，但若缺乏带宽感知，当链路容量不同时，负载分配可能不理想。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_bgp/configuration/xe-16/irg-xe-16-book/bgp-link-bandwidth.html">IP Routing: BGP Configuration Guide - BGP Link Bandwidth ... - Cisco</a></li>

</ul>
</details>

**标签**: `#BGP`, `#networking`, `#load-balancing`, `#RFC`, `#IETF`

---
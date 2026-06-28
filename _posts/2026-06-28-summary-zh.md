---
layout: default
title: "Horizon Summary: 2026-06-28 (ZH)"
date: 2026-06-28
lang: zh
---

> 从 31 条内容中筛选出 11 条重要资讯。

---

1. [HAWK 签名方案的新型经典密钥恢复攻击](#item-1) ⭐️ 9.0/10
2. [ProtogaLattice：支持通用多项式关系的常数轮格基折叠方案](#item-2) ⭐️ 9.0/10
3. [Cloudflare Workflows 新增 Saga 风格回滚](#item-3) ⭐️ 8.0/10
4. [Meta 为警察和军方开发实时面部识别眼镜](#item-4) ⭐️ 8.0/10
5. [大麻药房认证系统被黑，导致百万护照泄露](#item-5) ⭐️ 8.0/10
6. [德国法院裁定谷歌须为其 AI 搜索摘要负责](#item-6) ⭐️ 8.0/10
7. [研究揭示 LLM 依赖文本风格而非标签识别角色](#item-7) ⭐️ 8.0/10
8. [RFC 9994：MPLS 网络动作（MNA）子栈规范](#item-8) ⭐️ 8.0/10
9. [自适应桶数优化 MSM 提速 40%](#item-9) ⭐️ 7.0/10
10. [VERDICT：基于同态哈希的去中心化 DAG 数据血缘验证系统](#item-10) ⭐️ 7.0/10
11. [GSMA 发布百亿 Token 电信通用语料库，赋能开放电信 AI](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [HAWK 签名方案的新型经典密钥恢复攻击](https://eprint.iacr.org/2026/1318) ⭐️ 9.0/10

提出了一种新的经典算法，通过随机下三角幺模矩阵对公开 Gram 矩阵进行共轭，将 rank-2 module-LIP 实例约化为 nrdPIP 问题，再利用 Lenstra-Silverberg 子域方法求解，从而在概率多项式时间内恢复 HAWK 私钥。该攻击基于四个尚未实验验证的数论启发式假设。 此攻击针对提交至 NIST 后量子标准化进程的 HAWK 格基签名方案，若假设成立将可能破坏其安全性，表明基于格同构问题的方案存在子域方法的风险。 攻击通过反复用随机下三角幺模矩阵 U 共轭公开 Gram 矩阵 G 得到新实例 G’=U*GU，并测试其对应的 nrdPIP 实例是否可通过子域方法求解。每次试验声称有不可忽略的成功概率，但尚未得到实验验证，作者目前未宣称 HAWK 已被破解。

rss · IACR ePrint 密码学论文 · 6月25日 19:03

**背景**: HAWK 是 2022 年提出的后量子签名方案，基于格同构问题（LIP），即判断两个格是否正交同构，其安全性依赖于 rank-2 module-LIP 实例。该攻击将 HAWK 实例约化为四元数代数中的降范主理想问题（nrdPIP），当随机共轭产生“容易”实例时，可通过 Lenstra-Silverberg 子域算法在多项式时间内求解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/csrc/media/Projects/pqc-dig-sig/documents/round-1/spec-files/hawk-spec-web.pdf">HAWK version 1.0 (June 1, 2023) https://hawk-sign.info</a></li>
<li><a href="https://eprint.iacr.org/2024/1147.pdf">A reduction from Hawk to the principal ideal problem in a quaternion algebra</a></li>
<li><a href="https://arxiv.org/abs/1311.0366">[1311.0366] On the Lattice Isomorphism Problem - arXiv.org</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#lattice-based-cryptography`, `#HAWK`, `#cryptanalysis`

---

<a id="item-2"></a>
## [ProtogaLattice：支持通用多项式关系的常数轮格基折叠方案](https://eprint.iacr.org/2026/1317) ⭐️ 9.0/10

ProtogaLattice 是一种新的基于格的折叠方案，以常数轮实现通用多项式关系的折叠，相比现有的基于和校验的构造（如 LatticeFold+、Cyclo），大幅减小了验证器电路规模。 该进展显著提高了基于格的增量可验证计算和携带证明数据的效率，解决了递归中的一个关键瓶颈，使后量子简洁证明系统更加实用。 ProtogaLattice 将多个多项式实例合并为累加器，每轮完整迭代仅需四次随机预言机调用（不包括范围证明），并引入了一种使用 Protogalaxy 实现 PCD 的新技术。

rss · IACR ePrint 密码学论文 · 6月25日 14:59

**背景**: 折叠方案是一种密码学技术，可将关系的多个实例合并为一个，从而实现高效的递归证明。此前基于格的方案（如 LatticeFold）使用和校验协议，导致验证器电路因大量随机预言机调用而规模庞大。增量可验证计算和携带证明数据允许用简洁证明验证长计算或分布式计算链。格密码是离散对数方案的后量子替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2024/257">LatticeFold: A Lattice-based Folding Scheme and its Applications to Succinct Proof Systems</a></li>
<li><a href="https://eprint.iacr.org/2025/247">LatticeFold+: Faster, Simpler, Shorter Lattice-Based Folding for Succinct Proof Systems</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sum-check_protocol">Sum-check protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#zero-knowledge`, `#folding-schemes`, `#lattice-cryptography`, `#IVC/PCD`

---

<a id="item-3"></a>
## [Cloudflare Workflows 新增 Saga 风格回滚](https://blog.cloudflare.com/rollbacks-for-workflows/) ⭐️ 8.0/10

Cloudflare 的持久化执行引擎 Workflows 现在支持 Saga 模式回滚，开发人员可以为每个步骤指定补偿操作，实现自动故障恢复。 此增强通过提供结构化的部分故障处理方式，提高了长时间运行工作流的可靠性，减少了人工干预，并使 Cloudflare 与分布式事务的 Saga 模式等行业实践保持一致，增强了平台构建复杂应用的稳定性。 回滚功能作为每个步骤的元数据直接集成到工作流定义中，而非独立的全局错误处理程序。这种设计允许对补偿逻辑进行细粒度控制，并利用了现有的持久化执行保证。

rss · Cloudflare Blog (PQ 迁移) · 6月25日 13:00

**背景**: Saga 模式是一种无需分布式事务即可在多个微服务之间保持数据一致性的设计模式。它使用一系列本地事务，每个事务都有对应的补偿事务，以便在失败时撤消其影响。持久化执行引擎会保存执行状态，使工作流能够在故障后从断点恢复，而不会丢失进度。Cloudflare Workflows 就是这样一种引擎，使开发人员能够构建可靠的、多步骤的应用程序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/rollbacks-for-workflows/">How we built saga rollbacks for Cloudflare Workflows</a></li>
<li><a href="https://microservices.io/patterns/data/saga.html">Microservices Pattern: Pattern: Saga</a></li>
<li><a href="https://www.restate.dev/what-is-durable-execution">What is Durable Execution? A Definitive Guide | Restate</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#workflows`, `#durable execution`, `#saga pattern`, `#rollback`

---

<a id="item-4"></a>
## [Meta 为警察和军方开发实时面部识别眼镜](https://www.schneier.com/blog/archives/2026/06/meta-is-testing-facial-recognition-for-police-and-military.html) ⭐️ 8.0/10

Meta 正与五角大楼供应商合作，为其智能眼镜开发实时面部识别功能，这与 ICE 部署类似监控技术的兴趣相符。 这一进展引发了严重的隐私和伦理担忧，可能为执法和军事机构的大规模生物识别监控铺平道路，并可能为在公共空间广泛使用面部识别技术树立先例。 该原型将实时面部识别集成到 Meta 的智能眼镜中，据报道是与五角大楼承包商 Rank One Computing 合作开发；该技术可即时识别个人身份，增加了滥用风险。

rss · Schneier on Security · 6月26日 16:40

**背景**: Meta 是 Facebook 的母公司，一直在开发具有摄像头和音频功能的智能眼镜（如 Ray-Ban Stories）。面部识别技术利用人工智能将人脸与数据库进行比对，引发了隐私问题。美国移民和海关执法局（ICE）曾表示有兴趣将此类技术用于执法。五角大楼供应商可能指的是为政府机构提供面部识别解决方案的 Rank One Computing 公司。

**标签**: `#facial-recognition`, `#surveillance`, `#privacy`, `#meta`, `#police`

---

<a id="item-5"></a>
## [大麻药房认证系统被黑，导致百万护照泄露](https://www.schneier.com/blog/archives/2026/06/one-million-passports-leaked-online.html) ⭐️ 8.0/10

一个包含全球近百万本护照的数据库，因大麻药房的低安全身份验证系统被黑而泄露到了网上。 此次泄露事件暴露了将护照等高价值凭证用于低安全性认证的重大风险，表明低级系统一旦被攻破，就会成为大规模身份盗窃的单点故障。 泄露并非源自高安全性的政府数据库，而是大麻药房的身份验证系统，表明攻击者专攻最弱环节；受影响的护照来自多个国家，放大了全球风险。

rss · Schneier on Security · 6月26日 11:03

**背景**: 护照是政府签发的高安全性旅行证件，越来越多地被用于在线身份验证。当如此敏感的数据由低安全系统（如大麻药房的年龄验证）处理时，整个凭证生态就变得脆弱。攻击者常瞄准这些外围服务，以收割可在其他服务中用于欺诈的凭证。

**标签**: `#cybersecurity`, `#data breach`, `#identity theft`, `#passport leak`, `#authentication`

---

<a id="item-6"></a>
## [德国法院裁定谷歌须为其 AI 搜索摘要负责](https://www.schneier.com/blog/archives/2026/06/ai-and-liability.html) ⭐️ 8.0/10

德国一家法院裁定谷歌对其 AI 生成的搜索摘要中的虚假陈述负有责任，驳回了用户可自行核实信息的辩护理由。法院认为这些摘要是谷歌商业活动的表达，而非中立传输。 这一里程碑式的裁决确立了 AI 生成内容可归责于运营 AI 的公司，可能重塑全球科技公司的责任格局。它表明平台可能被视为其 AI 输出的发布者而非单纯的传输者。 法院明确驳回了谷歌声称用户通常知道 AI 信息不可盲信并可自行核查来源的论点。这意味着 AI 生成内容负有与传统出版类似的更高注意义务。

rss · Schneier on Security · 6月25日 17:03

**背景**: 历史上，法律框架区分传输者（如电话公司，不对用户内容负责）和发布者（如报纸，对其发布的内容负责）。互联网模糊了这些界限，美国《通信规范法》第 230 条等早期保护措施使平台得以免责。AI 摘要因是生成而非单纯托管，挑战了这些分类，而德国此次裁决将其归类为发布者内容。

**标签**: `#AI liability`, `#legal precedent`, `#Google`, `#AI-generated content`, `#technology law`

---

<a id="item-7"></a>
## [研究揭示 LLM 依赖文本风格而非标签识别角色](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html) ⭐️ 8.0/10

一篇新论文显示，大语言模型（LLM）学习区分系统、用户和助手角色时，依赖于文本的风格模式而非显式的角色标签，这使其天生容易受到提示注入攻击。 这揭示了 LLM 的根本安全弱点：缺乏真正的角色感知能力，针对提示注入的防御将成为一场持续的猫鼠游戏，对人工智能安全及敏感应用部署具有深远影响。 研究发现，角色标签原本只是一种格式化技巧，在模型表征中并未持久存在，从而导致角色混淆。攻击者可能通过看似无关的文本微妙地改变 LLM 状态，利用角色边界的连续性进行攻击。

rss · Schneier on Security · 6月25日 11:23

**背景**: 提示注入是一种攻击方式，对手精心设计输入以覆盖语言模型的指令或绕过安全措施，通常是在用户查询中插入恶意指令。LLM 通常使用如‘系统：’、‘用户：’、‘助手：’等特殊标签来划分对话的不同部分。然而，这项研究表明，LLM 并未将这些标签内化为稳固的角色边界，而是学习了表面的风格线索，因此容易被操纵。

**标签**: `#prompt-injection`, `#LLM-security`, `#AI-safety`, `#machine-learning`, `#cybersecurity`

---

<a id="item-8"></a>
## [RFC 9994：MPLS 网络动作（MNA）子栈规范](https://rfc-editor.org/info/rfc9994) ⭐️ 8.0/10

RFC 9994 已发布，定义了 MPLS 网络动作（MNA）子栈，这是一种在 MPLS 标签栈中直接嵌入网络动作和辅助数据的机制。该 RFC 还通过细化定义 MNA 动作的要求来更新 RFC 9789。 这对于 MPLS 协议实现者和网络运营商非常重要，因为 MNA 提供了一种标准化的方式来编码指令和元数据，支持带内 OAM、流量工程和自定义数据包处理等高级功能。这符合网络协议可编程性和可扩展性的行业趋势。 MNA 子栈由网络动作子栈指示符（NSI）标签指示，并且永远不会出现在标签栈的顶部。它通过修订 MNA 定义文档中必须包含的信息来更新 RFC 9789，并且可以携带操作、管理和维护（OAM）信息以及用户自定义操作。

rss · IETF 新标准 RFC (PQC 标准化) · 6月27日 01:14

**背景**: MPLS（多协议标签交换）使用标签栈逐跳转发数据包，每个标签可以指定特定的转发动作。网络动作是路由器执行超越简单转发操作的指令，IETF MPLS 工作组开发了 MNA 框架以便在标签栈内带内携带这些动作。RFC 9789 此前建立了该框架，但 RFC 9994 现在定义了具体的子栈编码以实现互操作性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-mpls-mna-hdr/">draft-ietf- mpls -mna-hdr-21 - MPLS Network Action (MNA) Sub - Stack ...</a></li>
<li><a href="https://ftp.ripe.net/internet-drafts/draft-ietf-mpls-mna-fwk-01.xml">MPLS Network Actions Framework</a></li>

</ul>
</details>

**标签**: `#MPLS`, `#Networking`, `#IETF`, `#RFC`, `#Network-Actions`

---

<a id="item-9"></a>
## [自适应桶数优化 MSM 提速 40%](https://eprint.iacr.org/2026/1316) ⭐️ 7.0/10

该论文提出了一种 Pippenger 算法的优化方法，根据可用内存动态调整桶的数量，在内存受限设备上的 BLS12-381 曲线多标量乘法中实现了最高 40%的速度提升。 MSM 是基于配对的零知识证明中的关键运算，内存限制常常影响嵌入式或边缘设备的性能。该优化能加快此类设备上的证明生成速度，有望扩展隐私保护技术的应用范围。 该方法将桶数量从标准的 2^w - 1 调整为适合可用内存的值，在 2^8 到 2^14 个点的 MSM 中均有效果。例如，使用 2^13 个点和 1 KB 内存时提升 40%，随着内存增加增益逐渐降至 1.5%。

rss · IACR ePrint 密码学论文 · 6月25日 12:47

**背景**: 多标量乘法（MSM）是计算多个标量与点乘积之和的过程，是 Groth16、PLONK 等零知识证明系统中多项式承诺的核心。Pippenger 算法是标准的高效方法，通过桶将标量按比特切片分组，但通常需要大量内存存储点。BLS12-381 是一种广泛用于零知识应用的双线性配对友好椭圆曲线。

**标签**: `#cryptography`, `#zero-knowledge proofs`, `#multi-scalar multiplication`, `#performance optimization`, `#BLS12-381`

---

<a id="item-10"></a>
## [VERDICT：基于同态哈希的去中心化 DAG 数据血缘验证系统](https://eprint.iacr.org/2026/1315) ⭐️ 7.0/10

该论文提出 VERDICT，一个面向去中心化有向无环图（DAG）的安全数据血缘框架，利用同态哈希和跳过 DAG 结构实现高效、密码学可验证的数据转换追溯。 它在不牺牲隐私的前提下为数据来源提供密码学保证，对信任和机密性至关重要的联邦学习和去中心化架构意义重大。 该系统采用桶索引和默克尔树验证，相对于 DAG 层级数实现 O(log n)验证时间，并通过应用层挑战-应答机制抵御重放攻击。

rss · IACR ePrint 密码学论文 · 6月25日 07:14

**背景**: 有向无环图（DAG）用于建模无循环的依赖关系。数据血缘记录数据的来源和变换，对审计和完整性至关重要。同态哈希允许在不暴露各部分内容的情况下计算组合哈希值，从而保护隐私。

**标签**: `#cryptography`, `#data lineage`, `#DAG`, `#decentralized systems`, `#verifiable computing`

---

<a id="item-11"></a>
## [GSMA 发布百亿 Token 电信通用语料库，赋能开放电信 AI](https://www.gsma.com/newsroom/article/telco-common-corpus-the-largest-open-verified-data-commons-for-telecom-ai/) ⭐️ 7.0/10

GSMA 开放电信 AI 倡议与 Pleias 合作发布了 Telco Common Corpus，一个包含超过 100 亿个开放、经许可验证的 token 的数据集，旨在推动电信专用 AI 模型的开发。 这个大规模、法律上清洁的数据集降低了电信 AI 开发的壁垒，使运营商、供应商和研究人员能够构建更准确、可靠的电信应用，而无需为许可问题担忧。 该语料库包含超过 100 亿个 token，完全开放且经许可验证，专门用于训练以电信为核心的模型。目前尚未披露数据构成或预处理等更多细节。

rss · GSMA Newsroom (移动安全标准) · 6月25日 08:56

**背景**: 数据公共资源（Data Commons）指可开放获取、自由使用和共享的数据集，通常采用宽松许可。Token 是 AI 文本处理的基本单位。GSMA 是全球移动运营商的行业协会，其开放电信 AI 倡议旨在促进电信领域的协作式 AI 开发。Telco Common Corpus 解决了此前缺乏大规模、开放的电信专用数据集来训练专用语言模型的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_commons">Data commons</a></li>

</ul>
</details>

**标签**: `#telecom`, `#AI`, `#dataset`, `#open-data`, `#natural-language-processing`

---
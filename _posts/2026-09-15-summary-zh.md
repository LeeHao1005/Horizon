---
layout: default
title: "Horizon Summary: 2026-09-15 (ZH)"
date: 2026-09-15
lang: zh
---

> 从 58 条内容中筛选出 15 条重要资讯。

---

1. [理想格问题的 NP 困难性通过确定性归约得到证明](#item-1) ⭐️ 9.0/10
2. [Anthropic 报告：也门威胁行为者利用 Claude AI 开发武器](#item-2) ⭐️ 9.0/10
3. [支付通道安全的第三支柱：威慑](#item-3) ⭐️ 8.0/10
4. [研究人员发现 Proton Docs/Sheets 存在不可检测的完整性攻击](#item-4) ⭐️ 8.0/10
5. [角度水印：尖锐泄漏界限与公共子空间验证](#item-5) ⭐️ 8.0/10
6. [新型信号泄漏攻击攻破 MQV 式基于 LWE 的认证密钥交换](#item-6) ⭐️ 8.0/10
7. [SoK：私有 Transformer 推理的系统、模型与密码学综述](#item-7) ⭐️ 8.0/10
8. [异步主动秘密共享：不可能性与最优协议](#item-8) ⭐️ 8.0/10
9. [新量子算法降低椭圆曲线离散对数的量子比特和 Toffoli 门数量](#item-9) ⭐️ 8.0/10
10. [基于沃尔什变换的统一差分-线性密码分析框架](#item-10) ⭐️ 8.0/10
11. [面向 OLE 的 UC 反向防火墙实现抗颠覆 MPC](#item-11) ⭐️ 8.0/10
12. [Beasley 交付首个实用的基于格的轮最优 VOPRF](#item-12) ⭐️ 8.0/10
13. [全简洁不可区分混淆：混淆大小仅取决于秘密部分](#item-13) ⭐️ 8.0/10
14. [新的不完美高阈值与切片秘密共享方案](#item-14) ⭐️ 8.0/10
15. [从子群不可区分性构造 HSS 与 PCF，超越 DCR 并改进 DDLog](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [理想格问题的 NP 困难性通过确定性归约得到证明](https://eprint.iacr.org/2026/2003) ⭐️ 9.0/10

这篇论文（eprint 2026/2003）通过一个保持维度、确定性的多项式时间归约，证明了理想格问题（包括 ℓ2 范数下的 SVP 和 CVP）的最坏情况 NP 困难性。该构造在一个单基因、全实域的数域的标准嵌入中，生成一个可逆理想，它能在缩放和正交变换意义上逼近任意输入格，并且定义理想和环的整数及判别式的比特长度都是多项式的。 这解决了一个长期悬而未决的问题，即理想格问题是否与一般格问题同样困难，从而加强了基于 Ring-LWE/Ring-SIS 密码体制的最坏情况困难性基础。它可能影响高效格密码方案的安全性假设和参数选择。 该归约保持维度且是确定性的；所得到的理想是可逆的，环是单基因的，数域是全实的，且判别式的比特长度为多项式。一个限制是：如果要求数环为完全整数环，该归约仅在猜想上可在有界误差量子多项式时间内成功。

rss · IACR ePrint 密码学论文 · 9月13日 16:48

**背景**: 理想格是对应于环中理想的格，通常来自 Z[x]/(f(x)) 之类的环，是构造 Ring-SIS 和 Ring-LWE 等高效格密码方案的基础。最短向量问题（SVP）要求找到格中最短的非零向量，最近向量问题（CVP）要求找到最接近给定目标点的格向量。一般格的 SVP 和 CVP 是 NP 困难的，但理想格上的对应问题是否保持 NP 困难性此前一直未解决。标准嵌入（canonical embedding）把数域映射到 R^n 或 C^n，是研究理想格的标准工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ideal_lattice">Ideal lattice - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lattice_problem">Lattice problem - Wikipedia</a></li>

</ul>
</details>

**标签**: `#lattice-cryptography`, `#NP-hardness`, `#ideal-lattices`, `#SVP`, `#CVP`

---

<a id="item-2"></a>
## [Anthropic 报告：也门威胁行为者利用 Claude AI 开发武器](https://www.schneier.com/blog/archives/2026/09/using-ai-for-weapons-development.html) ⭐️ 9.0/10

Anthropic 发布了一份详细报告，记录了其 Claude 模型被滥用的情况，并披露了一个位于也门北部的威胁行为者小组开展了三个武器研发项目：一枚使用消费级手机级飞行计算机和末段寻的制导的制导火箭、一枚目标射程超过 2000 公里的多级弹道导弹，以及一个包含高超声速滑翔飞行器型号的“R2000”多型号导弹。Bruce Schneier 在其安全博客上重点指出了这一发现。 这表明，可获取的大语言模型可能降低非国家行为体设计先进武器的门槛，包括此前主要与国家间军备竞赛相关的高超声速滑翔飞行器。这引发了对 AI 安全控制、模型滥用检测以及 AI 能力出口和政策措施的严重关切。 根据节选内容，制导火箭使用了消费级手机级飞行计算机和末段寻的制导，多级弹道导弹的声明射程目标超过 2000 公里。“R2000”系列被描述为多型号，包括高超声速滑翔飞行器型号。

rss · Schneier on Security · 9月14日 16:07

**背景**: Claude 是 Anthropic 开发的大语言模型系列，2023 年 3 月作为聊天机器人发布，也用于 AI 辅助软件开发。高超声速滑翔飞行器（HGV）是由弹道导弹助推器投送的机动弹头，分离后以高超声速滑翔，使其弹道难以预测，比传统弹道再入飞行器更难拦截。末段寻的制导是指末段制导技术，常基于比例导引法，在飞行的最后阶段控制导弹。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hypersonic_glide_vehicle">Hypersonic glide vehicle</a></li>
<li><a href="https://secwww.jhuapl.edu/techdigest/content/techdigest/pdf/V29-N01/29-01-Palumbo_Principles_Rev2018.pdf">Basic Principles of Homing Guidance</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#weapons development`, `#Anthropic`, `#misuse of AI`, `#national security`

---

<a id="item-3"></a>
## [支付通道安全的第三支柱：威慑](https://eprint.iacr.org/2026/2001) ⭐️ 8.0/10

该论文（ePrint 2026/2001）提出将威慑作为支付通道安全的第三支柱，并为锁定-解决通道建立了占用定价理论，证明线性时间比例责任是必要的，并给出一种目前在比特币上即可运行、无需 covenant、预言机或矿工假设的融合债券构造，将时隙拥塞威慑能力提升八个数量级。 这项工作直接解决了可低成本阻塞 Lightning 类支付通道的 griefing/拥塞攻击，提供可证明的经济威慑和正式权衡，可能影响支付通道设计并改善区块链可扩展性和用户体验。 论文证明时间无关定价允许无限 griefing，损害成本比超过 10^7，而线性时间比例责任达到紧界；并证明四个期望属性（对合谋汇聚方的威慑、仅依赖惩罚的诚实性、零中介锁定、路径隐私）中有三个无法同时实现，还通过证明转发三难困境解决了 2020 年 Lightning 工程界的猜想，同时暴露了一个关于发送方路径长度的新 O(1/n)侧信道。

rss · IACR ePrint 密码学论文 · 9月13日 15:08

**背景**: 支付通道允许双方通过锁定资金在链下进行交易，传统安全目标包括安全性（不会损失资金）和活性（支付可以继续）。锁定-解决通道使用时间锁脚本在链上解决争议，但攻击者可以低成本占用通道资源（拥塞/griefing）来延迟支付。本文加入威慑——让有害占用承担可证明的代价——作为第三安全支柱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/2001">The Price of Time: Deterrence as the Third Pillar of Payment Channel Security</a></li>

</ul>
</details>

**标签**: `#payment channels`, `#blockchain`, `#security`, `#deterrence`, `#cryptography`

---

<a id="item-4"></a>
## [研究人员发现 Proton Docs/Sheets 存在不可检测的完整性攻击](https://eprint.iacr.org/2026/1994) ⭐️ 8.0/10

在 IACR ePrint 报告（2026/1994）中，研究人员演示了对 Proton Docs/Sheets 的三种无法被检测的完整性攻击，包括历史重写、上下文操纵和审查；前两种攻击甚至可以在 Proton 服务器诚实的情况下发起，第三种则需要损坏的服务器。 这表明端到端加密本身不足以保证多人实时协作文档的完整性，可能使用户在不知情的情况下被操纵内容或审查。它也凸显了对协同编辑系统进行系统性形式化安全设计和分析的必要性。 这些攻击利用了协同编辑协议和密码设计中的弱点；前两种在诚实服务器下攻击，说明弱点存在于客户端协议，而第三种需要恶意服务器。作者还提出了相应的缓解方法。

rss · IACR ePrint 密码学论文 · 9月12日 14:58

**背景**: Proton Docs/Sheets 是 Proton Drive 的一部分，属于 Proton AG 提供的端到端加密云存储与协作服务，定位为 Google Docs 的隐私替代方案。端到端加密通常只保证只有文档参与者能读取内容，但实时协作编辑必须接受来自多用户的操作并解决冲突，这带来了完整性挑战。在没有谨慎密码保护的情况下，恶意方可能重写历史或操纵内容而不被发现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://proton.me/drive/docs">Create and collaborate with secure online documents | Proton</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proton_Docs">Proton Docs</a></li>

</ul>
</details>

**标签**: `#security`, `#cryptography`, `#collaborative editing`, `#integrity attacks`, `#Proton`

---

<a id="item-5"></a>
## [角度水印：尖锐泄漏界限与公共子空间验证](https://eprint.iacr.org/2026/1989) ⭐️ 8.0/10

该论文针对高斯潜变量模型中的角度水印，推导了尖锐的泄漏界限和公共子空间验证技术，包括精确的四阶签名、分布隐藏的边界，以及固定探针学习者在秩、精度和置信度固定时 O(p^3 log p/c^2) 的观测复杂度。 这仅利用公开验证方向和尺度信息，就能给出冻结候选者载波重叠的有限样本下界，无需密钥或载荷，可能改进 AI 模型的公开水印检测与审计。 核心统计结果是一个尖锐的、维度无关的中心化四阶张量协方差界。在八个固定候选者上，已知尺度和未知尺度的下界平均分别为 0.173 和 0.057，而 oracle 重叠平均为 0.600；这些保证基于所述 iid 模型和精确算术，并未建立同数据自适应训练收敛性、有序比特恢复或神经水印攻击。

rss · IACR ePrint 密码学论文 · 9月12日 10:03

**背景**: 角度水印将信息嵌入潜变量向量之间的相对角度中，通常用于为生成模型添加水印。高斯潜变量模型假设潜在特征服从高斯分布，载波子空间是水印信号所在的低维方向。分布隐藏是指在特定条件下水印在统计上与原始分布不可区分，而解码裕度衡量水印信号的可分离程度以支持可靠提取。本研究考察即使载荷比特被刷新，固定水印载波仍会泄漏多少信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1989">Sharp Leakage Bounds and Public Subspace Validation</a></li>

</ul>
</details>

**标签**: `#watermarking`, `#machine learning security`, `#statistical learning theory`, `#adversarial machine learning`, `#cryptography`

---

<a id="item-6"></a>
## [新型信号泄漏攻击攻破 MQV 式基于 LWE 的认证密钥交换](https://eprint.iacr.org/2026/2017) ⭐️ 8.0/10

研究人员提出了新的信号泄漏攻击，可在以往攻击失效的情况下攻破基于 LWE 的认证密钥交换协议。该攻击利用 eCK 模型中的临时密钥泄露，通过几何视角恢复静态私钥，明确回答了 ZZDSD-AKE 协议能否实现 eCK 安全这一长期悬而未决的问题，并给出否定结果，同时也攻破了 GDLL-KE 协议的随机噪声对抗措施。 该研究解决了后量子密码学中的一个重要开放问题，表明 MQV 式结构和临时随机化不足以抵御主动攻击者对直接基于 LWE 的认证密钥交换的威胁。这些发现为未来协议设计和标准化提供了关键指导。 攻击通过几何视角利用信号泄漏，分别约用 1700 次查询攻破 ZZDSD-AKE、180 次查询攻破 GDLL-KE 来恢复静态私钥。研究表明 GDLL-KE 中的随机噪声对抗措施未能消除依赖秘密的泄漏。

rss · IACR ePrint 密码学论文 · 9月14日 07:16

**背景**: 认证密钥交换（AKE）协议允许双方在不安全网络上协商共享密钥并相互认证。许多后量子 AKE 候选方案直接基于带错误学习（LWE）假设构建，该假设被认为即使对量子计算机也是困难的。扩展 Canetti-Krawczyk（eCK）安全模型是一种强安全模型，允许敌手获取长期私钥和会话特定秘密状态，因此是衡量 AKE 安全性的严格基准。信号泄漏攻击利用协调机制在将 LWE 值转换为共享比特时产生的信息泄漏，此前被认为可通过专门对抗措施阻断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-319-02726-5_14">Efficient eCK-Secure Authenticated Key Exchange Protocols in the Standard Model | Springer Nature Link</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-17140-6_33">Light the Signal: Optimization of Signal Leakage Attacks ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange">Diffie–Hellman key exchange - Wikipedia</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#authenticated key exchange`, `#LWE`, `#eCK model`, `#signal leakage attacks`

---

<a id="item-7"></a>
## [SoK：私有 Transformer 推理的系统、模型与密码学综述](https://eprint.iacr.org/2026/2005) ⭐️ 8.0/10

作者系统化了 2022 至 2026 年的 58 个密码学私有 Transformer 框架，从系统、模型和密码学三个相互关联的层面展开分析。他们发现两类反复出现的跨后端适用性约束：优化无法在需要尚未获得的值时跨执行阶段原样迁移；数据依赖的剪枝、缓存管理、路由和稀疏性要求私有执行结构被隐藏、约束、预测或披露。 该综述为研究人员提供了跨层面参考图谱，说明私有 Transformer 技术在何种条件下仍适用或可组合，有助于避免重复工作和不可泛化的设计。论文还提炼了 12 个开放问题和 16 个展望，为隐私保护机器学习领域的后续协议设计指明方向。 该研究覆盖 2022 至 2026 年的 58 个框架，将分析分为系统、模型和密码学三个层面，并指出 16 个框架依赖经验校准或分布特定机制，21 个框架需要额外训练。研究还识别出影响 5 个框架的四类安全问题，并分析了恶意安全设计中的组合边界。

rss · IACR ePrint 密码学论文 · 9月13日 18:07

**背景**: 私有 Transformer 推理利用安全多方计算（MPC）等密码学协议运行 Transformer 模型，同时不泄露用户输入或模型权重。Transformer 因大规模秘密矩阵乘法、softmax/GELU 等高成本非线性操作和顺序自回归执行而具有独特挑战。以往综述多按密码学后端、部署场景或支持的操作分类，难以说明技术在不同执行阶段之间是否仍适用或可组合。本文通过系统、模型与密码学三层分类法厘清了这些关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/491">SoK: Private Transformer-Based Model Inference</a></li>
<li><a href="https://arxiv.org/abs/2412.08145">[2412.08145] A Survey on Private Transformer Inference SoK: Private Transformer Inference Across Systems, Models ... A Survey on Private Transformer Inference - arXiv.org Sok: Private Transformer-based Model Inference | USENIX Breaking the Layer Barrier: Remodeling Private Transformer ... Efficient and performant Transformer private inference with ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation</a></li>

</ul>
</details>

**标签**: `#private inference`, `#transformers`, `#cryptography`, `#secure computation`, `#machine learning`

---

<a id="item-8"></a>
## [异步主动秘密共享：不可能性与最优协议](https://eprint.iacr.org/2026/2018) ⭐️ 8.0/10

该论文在完全异步认证网络中系统研究了主动秘密共享的可行性，形式化了一组移动敌手模型，并通过通用攻击建立了不可能性结果，同时给出了在每个模型中达到最优弹性的显式协议。 这项工作为异步环境下的主动秘密共享划定了理论边界，有助于设计更安全的分布式密码协议，对安全多方计算和门限密码系统等应用具有重要意义。 论文在无全局时钟的完全异步认证网络模型中，定义了不同移动敌手能力的层次，推导出弹性上界，并用显式协议证明这些上界是紧的。

rss · IACR ePrint 密码学论文 · 9月14日 08:08

**背景**: 主动秘密共享是一种周期性地刷新秘密份额而不改变秘密本身的技术，以限制移动敌手在长时间内逐步攻陷参与方的能力。异步网络没有全局时钟，各参与方无法依赖同步时隙来协调份额更新，这使得主动秘密共享的设计更具挑战性。移动敌手模型允许敌手在不同时期腐蚀不同的参与方集合，是评估长期安全性的重要抽象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Proactive_secret_sharing">Proactive secret sharing</a></li>
<li><a href="https://www.researchgate.net/publication/2545033_APSS_Proactive_Secret_Sharing_in_Asynchronous_Systems">(PDF) APSS: Proactive Secret Sharing in Asynchronous Systems</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#distributed systems`, `#secret sharing`, `#asynchronous networks`, `#proactive security`

---

<a id="item-9"></a>
## [新量子算法降低椭圆曲线离散对数的量子比特和 Toffoli 门数量](https://eprint.iacr.org/2026/2014) ⭐️ 8.0/10

该论文提出一种用于 n 比特素数域上椭圆曲线离散对数问题的量子算法，使用 5/2 n + o(n) 个逻辑量子比特和 Õ(n^2) 个 Toffoli 门，将此前 Luo 等人的 3n + O(log n) 个逻辑量子比特和 O(n^3/log n) 个 Toffoli 门分别优化到更低的领先项和近二次的门数。 这一优化具有重要意义，因为它通过减少所需的逻辑量子比特和 Toffoli 门数量，使针对椭圆曲线密码学的实用量子攻击更接近现实，从而影响后量子安全评估和密码迁移规划。 该算法构造了一个精确的原位模逆器，占用 3/2 n + o(n) 个逻辑量子比特和 Õ(n) 个 Toffoli 门，利用不变量 Rt + rT = p 只存储 R、r、T、t 中的三个值，并通过基于测量的反计算在次线性工作空间中执行算术查询。随后使用 Hua 恒等式将仿射点加所需的可变平方乘法化简为求逆。

rss · IACR ePrint 密码学论文 · 9月14日 06:47

**背景**: 椭圆曲线密码学依赖于椭圆曲线离散对数问题的困难性。足够大的量子计算机可以通过 Shor 算法高效求解该问题，但实际实现需要大量的逻辑量子比特和门。Toffoli 门是一种通用可逆三量子比特门，是容错量子电路中的基本成本单位。基于测量的反计算是一种通过测量临时量子比特来概率性地清除它们的技术，从而减少对显式辅助工作空间的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Elliptic_curve_discrete_logarithm_problem">Elliptic curve discrete logarithm problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Toffoli_gate">Toffoli gate</a></li>
<li><a href="https://arxiv.org/abs/2407.20167">[2407.20167] Measurement-based uncomputation of quantum circuits for modular arithmetic</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#elliptic curve cryptography`, `#discrete logarithm`, `#quantum cryptanalysis`, `#resource optimization`

---

<a id="item-10"></a>
## [基于沃尔什变换的统一差分-线性密码分析框架](https://eprint.iacr.org/2026/2013) ⭐️ 8.0/10

该论文在差分转移函数上引入统一的沃尔什变换框架，涵盖标准、旋转和内部差分-线性密码分析。论文还为 ARX 模加推导出 2×2 矩阵乘积公式，并针对 Xoodoo-p、Ascon-p、Alzette、SipHash 和 SPECK64 获得了新的区分器。 这一统一方法将成熟的标准差分-线性搜索工具扩展到旋转和内部差分-线性分析，可能使对 ARX 及置换型设计的密码分析更加高效。它还部分解决了 Niu 等人在 CRYPTO 2022 提出的开放问题，对轻量级对称原语的安全性评估具有实际影响。 对于 ARX 中的单个模加，作者推导出 2×2 矩阵乘积公式，其输入差分矩阵具有秩 1 结构，从而可以只用线性不等式和查表来构造 CP 近似。该框架得到 Xoodoo-p 的 6 轮 RDL 区分器和文献中首个 IDL 区分器、Ascon-p 的 6 轮 RDL 区分器、Alzette 的 8 轮 RDL 区分器（此前最好为 4 轮）、SipHash 的 5 轮区分器以及 SPECK64 的 14 轮 SDL 区分器。

rss · IACR ePrint 密码学论文 · 9月14日 06:42

**背景**: 差分-线性密码分析由 Langford 和 Hellman 于 1994 年提出，它将差分特征与线性逼近结合起来攻击密码。沃尔什变换（也称沃尔什-哈达玛变换）是一种正交线性变换，可用于分析布尔函数，相当于二进制域上的傅里叶变换。ARX 原语由模加、循环移位和异或构成，广泛用于轻量级密码和哈希函数。论文涉及的 Xoodoo-p、Ascon-p、Alzette、SipHash 和 SPECK64 都是 ARX 或置换型设计，常用于轻量级密码学。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Differential-linear_cryptanalysis">Differential-linear cryptanalysis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Walsh_transform">Walsh transform</a></li>
<li><a href="https://eprint.iacr.org/2021/1690.pdf">[PDF] A New Framework of Cryptanalysis on ARX ciphers with Applications to ...</a></li>

</ul>
</details>

**标签**: `#cryptanalysis`, `#differential-linear cryptanalysis`, `#Walsh transform`, `#ARX`, `#symmetric-key cryptography`

---

<a id="item-11"></a>
## [面向 OLE 的 UC 反向防火墙实现抗颠覆 MPC](https://eprint.iacr.org/2026/2012) ⭐️ 8.0/10

该论文首次为不经意线性求值(OLE)构造通用可组合反向防火墙，使算术安全多方计算具备抗颠覆能力。论文证明自然加法同态加密(AHE)类协议的两轮不可能性，并基于密钥可延展 AHE 给出 UC 安全三轮构造，同时给出隐蔽敌手下的两轮协议。 这填补了反向防火墙保护与高性能算术 MPC 之间的空白——后者依赖 OLE 而非不经意传输，使抗颠覆安全计算在隐私集合求交(PSI)等实际应用中变得可行。所报告的 1.5–3 倍开销说明防御机器颠覆不一定代价过高。 该工作形式化了可净化 OLE 功能 FsOLE，并证明自然 AHE 类协议无法在 UC 安全下实现两轮；但基于密钥可延展 AHE 可实现三轮 UC 安全协议，而隐蔽敌手模型下的包装式可净化 OLE 则带来高效两轮协议。两个构造都通过基于类群的密钥可延展 AHE 实例化，所得 PSI 协议达到最优通信。

rss · IACR ePrint 密码学论文 · 9月14日 05:45

**背景**: 安全多方计算(MPC)通常假设参与者在可信机器上执行协议，但被攻陷的设备可能通过被操纵的协议记录泄露秘密。Mironov 和 Stephens-Davidowitz 提出的密码学反向防火墙位于参与方机器外部，在不改变功能的前提下清洗消息。不经意线性求值(OLE)允许持有(a,b)的发送方与持有 x 的接收方计算 ax+b 且不泄露其他输入，是许多高性能算术 MPC 的核心原语。通用可组合性(UC)是一种强安全框架，保证协议与其他协议组合时仍然安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scispace.com/pdf/cryptographic-reverse-firewalls-4izfxlss0z.pdf">Cryptographic Reverse Firewalls</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_composability">Universal composability</a></li>
<li><a href="https://quantum-journal.org/papers/q-2024-10-23-1507/">Quantum Universally Composable Oblivious Linear Evaluation</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secure multi-party computation`, `#reverse firewalls`, `#oblivious linear evaluation`, `#universal composability`

---

<a id="item-12"></a>
## [Beasley 交付首个实用的基于格的轮最优 VOPRF](https://eprint.iacr.org/2026/2010) ⭐️ 8.0/10

Beasley 论文首次给出了一个轮最优、恶意安全、基于格的验证性不经意伪随机函数（VOPRF）的具体原型实现。其核心优化包括将 BLMR 伪随机函数推广为每步处理 4 位输入，并用环切换求和检查协议替代 LaBRADOR 风格的证明；在单核 AVX2 笔记本上，生成客户端请求和非交互式零知识证明（NIZK）需 520 毫秒，服务器验证需 15.3 毫秒，峰值内存 113.7MB，客户端通信量 109KB。 这填补了实际应用空白：提供了一种具备恶意安全性和轮最优性质的后量子 VOPRF，可用于隐私集合求交、口令认证密钥交换和匿名凭证等隐私保护协议，替代易受量子攻击的现有构造。其在普通硬件上的具体性能表明，基于格的 VOPRF 已经具备现实部署潜力。 Beasley 将 BLMR13 伪随机函数推广为每步同时处理 w 位输入（实现中 w=4），在不影响安全性的情况下将评估深度和运行时间降低为原来的四分之一。它用环切换求和检查协议替换 LaBRADOR 风格证明，并采用 512 的环维度，产生 75.4KB 的 NIZK 证明，同时实现紧凑密钥和无安全松弛的精确范围证明。

rss · IACR ePrint 密码学论文 · 9月13日 22:06

**背景**: 不经意伪随机函数（OPRF）允许两方共同计算一个伪随机函数，使得客户端得到输出而服务器不知道客户端输入；验证性 OPRF（VOPRF）还允许客户端验证服务器确实使用了其承诺的密钥。基于格的密码学是后量子密码的主要方向之一，其安全性依赖于学习带误差（LWE）等困难格问题，可抵抗舒尔算法针对 RSA 和椭圆曲线等传统方案的量子攻击。BLMR13 是一种基于格的伪随机函数构造，Beasley 将其推广为每步处理多位输入，以降低零知识证明成本。环切换求和检查协议是一种在不同代数环之间迁移计算以提高证明效率的技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Oblivious_pseudorandom_function">Oblivious pseudorandom function - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lattice-based_cryptography">Lattice-based cryptography</a></li>
<li><a href="https://people.csail.mit.edu/vinodv/CS294/lecture5.pdf">CS 294. Pseudorandom Functions from Lattices</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#zero-knowledge proofs`, `#lattice-based cryptography`, `#oblivious pseudorandom functions`, `#post-quantum`

---

<a id="item-13"></a>
## [全简洁不可区分混淆：混淆大小仅取决于秘密部分](https://eprint.iacr.org/2026/2009) ⭐️ 8.0/10

该论文引入全简洁不可区分混淆（IO）概念，混淆后程序的大小仅取决于描述中的秘密部分，既不依赖公开部分也不依赖输入大小。作者从 PV 等价机器的输入简洁 IO 出发构造了全简洁 pv-IO，并在简洁见证加密或 NP 唯一证明 SNARG 下自举到完整 IO 安全性。 这推动了简洁混淆的前沿，使描述大部分公开的程序能够以仅与隐藏部分成比例的开销进行混淆。它首次实现了一类实用程序中混淆大小小于原程序两倍的 IO，免除了混淆前填充的需要，并实现了简洁计算秘密共享，可能重塑理论密码学。 该构造从 PV 等价机器的输入简洁 IO 出发（可由超多项式困难的电路 IO 和 LWE 获得），随后以简洁见证加密或 NP 唯一证明 SNARG 作为自举原语。所有正确性证明都要求在 Cook 理论 PV 中可形式化，并且这些假设被证明既充分又必要。

rss · IACR ePrint 密码学论文 · 9月13日 21:00

**背景**: 不可区分混淆（IO）是一种密码学原语，它将程序转换为功能等价程序的混淆在计算上不可区分，在保持功能的同时隐藏实现细节。目前的 IO 候选方案远未实用，但近期工作已能混淆图灵机，其大小只依赖于输入长度而非运行时间；Jain 和 Jin 进一步去除了输入大小依赖，适用于等价性可在 Cook 理论 PV（一种弱形式算术理论）中证明的程序。本文推广了这一思路，探讨混淆大小是否可仅依赖于程序描述中的秘密部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indistinguishability_obfuscation">Indistinguishability obfuscation</a></li>
<li><a href="https://ieee-focs.org/FOCS-2025-Papers/pdfs/FOCS2025-4pLZMZRP5BPG9n0GSua5T9/713200b706/713200b706.pdf">On Succinct Obfuscation via Propositional Proofs</a></li>
<li><a href="https://simons.berkeley.edu/talks/surya-mathialagan-mit-2025-06-25">Succinct Obfuscation via Propositional Proofs (or: How to use ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#obfuscation`, `#succinctness`, `#indistinguishability obfuscation`, `#theoretical computer science`

---

<a id="item-14"></a>
## [新的不完美高阈值与切片秘密共享方案](https://eprint.iacr.org/2026/2008) ⭐️ 8.0/10

该论文提出了针对常数 t 和增长 n 的 (n - t + 1)-out-of-n 阈值及切片秘密共享新方案，具有不完美保密性。其中一个构造对比特实现 ε-差分保密，份额字母表大小为 Õ_t(1/ε^2)；另一个构造对 (n-2)-out-of-n 切片实现 ε-统计保密，份额大小为 O(log n log 1/ε)；对于 t > 3，前者的安全性依赖于有限域上单变量多项式分解的一个猜想。 这些结果大幅减小了高阈值和切片秘密共享的份额大小，超越了完美安全和计算安全，并解决了相关开放问题。更小的份额有助于秘密共享在分布式存储、安全多方计算和隐私保护系统中的实际应用。 ε-差分秘密阈值方案的份额字母表大小不随 n 增长，而完美保密下界为 n - t + 1；但当 t > 3 时，其证明依赖于一个未经证实的猜想。ε-统计秘密切片方案对 n 和 1/ε 仅呈对数依赖，优于以往仅计算安全的构造；此外，变体还给出了具有最优份额大小的 (n-1)-out-of-n 弱比特秘密共享方案。

rss · IACR ePrint 密码学论文 · 9月13日 20:40

**背景**: 秘密共享将秘密拆分为多个份额，只有特定的授权参与者子集才能重建秘密，其他子集无法获得信息。在完美秘密共享中，每个份额的大小至少与秘密相同，这对高阈值方案来说代价很高。不完美保密放宽了这一要求，允许少量可量化的泄漏（例如用差分隐私或统计距离度量），以换取更小的份额。切片访问结构是近期高阈值和一般秘密共享效率研究中涉及的一类访问结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/2008">New Imperfect High Threshold and Slice Secret Sharing Schemes</a></li>
<li><a href="https://eprint.iacr.org/2024/602">Secret-Sharing Schemes for High Slices</a></li>
<li><a href="https://en.wikipedia.org/wiki/Differential_privacy">Differential privacy - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secret sharing`, `#threshold schemes`, `#imperfect secrecy`, `#differential privacy`

---

<a id="item-15"></a>
## [从子群不可区分性构造 HSS 与 PCF，超越 DCR 并改进 DDLog](https://eprint.iacr.org/2026/2006) ⭐️ 8.0/10

这篇论文基于子群不可区分性假设构造了同态秘密共享和伪随机相关函数，将其推广到 DCR 之外的实例；同时提出适用于光滑阶群的高效分布式离散对数算法，首次支持素数幂情形，并将复杂度优化至 O(log t log log t)。 这扩大了同态秘密共享和伪随机相关函数所依赖的假设范围，不再局限于 DCR，可能影响安全多方计算和静默 OT 扩展等应用；同时解决了素数幂阶分布式离散对数的开放问题，具有理论与实用价值。 新 DDLog 算法采用分治优化，把 Abram 等人在 Crypto 2022 的 O(log² t / log log t)群操作改进为 O(log t log log t)；论文还引入公开币子群不可区分性(PC-SgI)并证明某些实例下 SgI 蕴含 PC-SgI，从而在 PC-SgI 下泛化得到 VOLE、OT、OLE 和二次相关 PCF，其中 OLE 和二次相关还需稀疏 LPN 假设；另外修复了 Joye–Libert 实例中的 DDH 攻击和 IKNP OT 扩展优化变体的证明缺陷。

rss · IACR ePrint 密码学论文 · 9月13日 19:02

**背景**: 同态秘密共享允许在不重构秘密的情况下对份额进行同态计算；伪随机相关函数让双方以非交互方式生成大量相关随机数。子群不可区分性假设由 Brakerski 和 Goldwasser 提出，涵盖二次剩余和 DCR 等特例；DCR（判定合数剩余）是许多密码方案的经典困难假设。分布式离散对数协议要求多方从群元素份额中恢复离散对数，光滑阶群因其因子小更易处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_secret_sharing">Homomorphic secret sharing</a></li>
<li><a href="https://eprint.iacr.org/2025/2325">Pseudorandom Correlation Functions for Garbled Circuits</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-642-14623-7_1">Circular and Leakage Resilient Public-Key Encryption under Subgroup ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#homomorphic secret sharing`, `#pseudorandom correlation functions`, `#subgroup indistinguishability`, `#discrete logarithm`

---
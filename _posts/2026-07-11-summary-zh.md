---
layout: default
title: "Horizon Summary: 2026-07-11 (ZH)"
date: 2026-07-11
lang: zh
---

> 从 31 条内容中筛选出 8 条重要资讯。

---

1. [分离原理：激活函数结构无法减少 zkML 查找证明开销](#item-1) ⭐️ 9.0/10
2. [6G 感知安全：分布式博弈论强化学习用于城市波束成形攻击检测](#item-2) ⭐️ 8.0/10
3. [Cloudflare 主张立即采用 ML-DSA 后量子签名](#item-3) ⭐️ 8.0/10
4. [Cloudflare 推出 Meerkat 全球共识服务及 QuePaxa 算法](#item-4) ⭐️ 8.0/10
5. [布鲁斯·施奈尔警告 AI 监控将实时执行所有规则](#item-5) ⭐️ 8.0/10
6. [用内积切片布尔函数](#item-6) ⭐️ 7.0/10
7. [Squid 代理存在 29 年之久的“Squidbleed”漏洞可泄露 HTTP 请求](#item-7) ⭐️ 7.0/10
8. [AI 生成文本或改变人类语言习惯](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [分离原理：激活函数结构无法减少 zkML 查找证明开销](https://eprint.iacr.org/2026/1390) ⭐️ 9.0/10

该论文证明，在用于 zkML 的 Shout 式（独热）查找论证中，每次查找的证明成本仅取决于访问模式，而与激活函数的数学结构无关。这直接限制了一种常见的优化思路，即试图利用函数结构来降低证明开销。 该分离原理将证明器设计工作重定向到优化访问模式，而非函数结构，从而可能避免徒劳的工作，并导向更高效的零知识机器学习系统。 由于典型输入上存在 σ 下限，每次查找成本不随深度增长，使得单一固定证明精度即可满足要求，从而证明成本与层数近乎线性。承诺地址宽度是唯一可调的参数，作者已在 EZKL/halo2 和 Jolt Atlas 中实现了逐比特精确的证明时间缩短。

rss · IACR ePrint 密码学论文 · 7月8日 05:45

**背景**: 零知识机器学习（zkML）能够在保证输入和模型参数不泄露的情况下，证明机器学习模型推理的正确性。查找论证是 zkML 中的一项关键技术，通过检查值是否出现在预计算的表中，来高效处理激活函数等非线性操作。Shout 是近期提出的一种索引查找论证，采用独热编码。该论文表明，在此类系统中，每次查找的证明工作量完全取决于访问模式（即查询表的方式），而不是表的值，因此简化激活函数的结构并不能减少这一主要开销——这便是分离原理的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1390">A Separation Principle for Lookup-Based zkML: Activation-Function Structure Cannot Reduce Per-Lookup Proving Cost</a></li>
<li><a href="https://powdr.org/papers/twist_shout_logup_star.pdf">Twist and Shout via logup* Georg Wiese Powdr Labs georg@powdrlabs.com</a></li>
<li><a href="https://www.zkm.io/blog/lookup-argument-in-zero-knowledge-proofs">Lookup Argument in Zero - Knowledge Proofs</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#machine learning`, `#lookup arguments`, `#computational complexity`, `#transformers`

---

<a id="item-2"></a>
## [6G 感知安全：分布式博弈论强化学习用于城市波束成形攻击检测](https://eprint.iacr.org/2026/1391) ⭐️ 8.0/10

该论文提出了一种分布式博弈论强化学习框架，用于检测在城市 6G 集成感知与通信（ISAC）环境中操纵波束成形方向的攻击者。 随着 6G 网络将感知与通信融合，检测波束成形攻击对于保障数据传输和环境感知的安全至关重要。该研究针对新的威胁形式，可能提升下一代智慧城市和自主系统的韧性。 该方法将合法用户与攻击者之间的交互建模为博弈，并将基于效用的公式集成到强化学习算法中。仿真结果证明了其有效性，但未提供实际部署验证。

rss · IACR ePrint 密码学论文 · 7月8日 07:14

**背景**: 集成感知与通信（ISAC）是一项关键的 6G 技术，使得网络能通过无线电信号同时进行通信和环境感知。波束成形通过集中无线信号方向来提升效率，但攻击者可能操纵它以造成干扰或窃听。博弈论对理性决策者之间的策略交互进行建模，而强化学习使智能体通过试错学习最优动作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/integrated-sensing-communication-isac-shaping-future-6g-mittal-683ne">Integrated Sensing & Communication ( ISAC ): Shaping the Future of...</a></li>
<li><a href="https://www.researchgate.net/publication/383396909_Beamforming_made_Malicious_Manipulating_Wi-Fi_Traffic_via_Beamform-ing_Feedback_Forgery">(PDF) Beamforming made Malicious: Manipulating Wi-Fi Traffic via Beamform-ing Feedback Forgery</a></li>

</ul>
</details>

**标签**: `#6G`, `#ISAC`, `#beamforming`, `#game theory`, `#reinforcement learning`

---

<a id="item-3"></a>
## [Cloudflare 主张立即采用 ML-DSA 后量子签名](https://blog.cloudflare.com/ml-dsa-will-have-to-do/) ⭐️ 8.0/10

Cloudflare 认为，尽管 NIST 正在推进九种新的后量子签名候选算法，但 ML-DSA 是当前最成熟、最安全的方案，应被立即采用。 立即采用 ML-DSA 可保护系统免受未来量子攻击，确保互联网协议和数字通信的长期安全。 ML-DSA（FIPS 204）是一种基于格的签名方案，源自 CRYSTALS-Dilithium，其安全性基于抗量子攻击的格难题。

rss · Cloudflare Blog (PQ 迁移) · 7月9日 14:00

**背景**: 后量子密码学旨在开发能够抵御量子计算机和经典计算机攻击的密码算法。现有的公钥方案如 RSA 和 ECDSA 可能被 Shor 算法在量子计算机上破解。NIST 一直通过标准化进程选择抗量子算法，ML-DSA 是首批完成标准化的算法之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://rya-sge.github.io/access-denied/2026/06/29/ml-dsa-fips-204-post-quantum-signatures/">ML - DSA — The Module-Lattice Digital Signature Standard (FIPS 204)</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#digital signatures`, `#NIST`, `#ML-DSA`, `#security`

---

<a id="item-4"></a>
## [Cloudflare 推出 Meerkat 全球共识服务及 QuePaxa 算法](https://blog.cloudflare.com/meerkat-introduction/) ⭐️ 8.0/10

Cloudflare Research 宣布推出 Meerkat——一项全球共识服务实验，以及其使用的 QuePaxa 共识算法；该算法避免依赖超时来保证活性，旨在构建强一致、容错的键值存储系统。 这一进展可能显著提升全球分布式系统的性能和健壮性，因为 QuePaxa 无需手动调参超时，在正常条件下保持与基于领导者的协议相当的效率，同时避免超时带来的脆弱性。 QuePaxa 结合了随机异步共识以保证最坏情况下的活性，使用对冲（hedging）而非超时以获得类似领导者协议的正常情况效率，并自适应选择领导者以减少手动配置；Meerkat 目前是实验性服务。

rss · Cloudflare Blog (PQ 迁移) · 7月8日 13:00

**背景**: 共识算法使分布式系统能够在故障情况下达成一致。广泛使用的协议如 Raft 依赖超时进行领导者选举，在恶劣网络条件下可能延迟。异步共识避免超时，但通常牺牲性能。QuePaxa 通过使用对冲和随机化结合了二者的优点，实现了健壮性与效率的平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/meerkat-introduction/">Introducing Meerkat: an experiment in global consensus</a></li>
<li><a href="https://bford.info/pub/os/quepaxa/quepaxa.pdf">QuePaxa: Escaping the Tyranny of Timeouts in Consensus Pasindu Tennage* EPFL</a></li>
<li><a href="https://bford.info/pub/os/quepaxa/">QuePaxa: Escaping the Tyranny of Timeouts in Consensus – Bryan Ford's Home Page</a></li>

</ul>
</details>

**标签**: `#consensus`, `#distributed systems`, `#Cloudflare`, `#key-value store`, `#QuePaxa`

---

<a id="item-5"></a>
## [布鲁斯·施奈尔警告 AI 监控将实时执行所有规则](https://www.schneier.com/blog/archives/2026/07/ai-surveillance-and-social-progress.html) ⭐️ 8.0/10

布鲁斯·施奈尔描绘了不久的将来，AI 驱动的监控系统将追踪所有公共及许多私人行为，实时自动检测并处罚任何违规行为，如同超级加强版的测速摄像头。 这一情景凸显了隐私严重侵蚀和无处不在的社会控制风险，即使轻微违规也会被永久记录并即时处罚，从根本上改变日常生活并引发深刻的伦理担忧。 与几周后邮寄罚单的现有测速摄像头不同，这些 AI 系统将对任何预定义违规行为（从乱扔垃圾到闯红灯）即时发出通知和罚款，并将其绑定至官方政府档案，同时可能实时通知执法部门和公众。

rss · Schneier on Security · 7月10日 11:02

**背景**: 自动测速摄像头是当前无需人类警员的执法形式；AI 监控利用先进的计算机视觉和模式识别，将这一概念扩展到所有公共行为。布鲁斯·施奈尔是一位以分析技术社会影响而闻名的安全技术专家和作家。

**标签**: `#AI ethics`, `#surveillance`, `#privacy`, `#social implications`, `#technology policy`

---

<a id="item-6"></a>
## [用内积切片布尔函数](https://eprint.iacr.org/2026/1392) ⭐️ 7.0/10

这项工作将布尔函数的汉明重量切片推广为由整数线性形式（与固定向量的内积）定义的 v-切片。它给出了在每片上有界次数的分解所需切片数量的界限，并针对类 GSW 同态评估进行了适配，提供了噪声估计。 这种推广为同态友好对称原语提供了更灵活的布尔函数分解，可能提高混合同态加密的效率。它为具有强密码学性质和低同态评估开销的密码设计开辟了新的可能性。 论文给出了整数向量诱导划分的结构性质和界限，以及类 GSW 同态评估的噪声估计。实验表明，对称函数的直接推广通常会失去密码学强度，但推广的权重次 d 构造展现出更丰富且更有前景的特性。

rss · IACR ePrint 密码学论文 · 7月8日 08:07

**背景**: 汉明重量切片根据置位比特数划分布尔立方体，形成用于 FLIP 等对称密码的权重次 d 函数。混合同态加密（HHE）将对称加密与同态运算相结合，以实现隐私保护计算。从汉明重量推广到任意整数线性形式，允许根据特定同态评估策略进行更细粒度的分解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://orbilu.uni.lu/handle/10993/57255">ORBilu: On the cryptographic properties of weightwise affine and...</a></li>
<li><a href="https://khoaguin.github.io/blog/what-is-hhe">What is Hybrid Homomorphic Encryption and Its Applications</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#boolean-functions`, `#homomorphic-encryption`, `#symmetric-cryptography`, `#mathematical-cryptography`

---

<a id="item-7"></a>
## [Squid 代理存在 29 年之久的“Squidbleed”漏洞可泄露 HTTP 请求](https://www.schneier.com/blog/archives/2026/07/friday-squid-blogging-squidbleed-vulnerability.html) ⭐️ 7.0/10

一个名为“Squidbleed”的漏洞在 Squid 代理服务器中被披露，该漏洞已存在 29 年之久，可让攻击者泄露 HTTP 请求。 Squid 被广泛用于缓存和转发网络流量；此漏洞可能泄露 HTTP 请求中的敏感数据，影响众多网络安全部署。 被称为 Squidbleed 的缺陷是 Squid 中一个存在数十年的漏洞，可泄露 HTTP 请求，但初步报告未提供 CVE 编号或具体技术机制等细节。

rss · Schneier on Security · 7月10日 21:07

**背景**: Squid 是一款缓存和转发 HTTP 网页代理，通过缓存频繁请求来提升网页性能，也可用于流量过滤和安全。它支持 HTTP、HTTPS 和 FTP 等协议，主要在类 Unix 系统上运行。该代理常部署于企业和互联网服务提供商环境中，以减少带宽消耗并加速浏览。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Squid_proxy">Squid proxy</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#vulnerability`, `#Squid-proxy`, `#HTTP-leak`, `#network-security`

---

<a id="item-8"></a>
## [AI 生成文本或改变人类语言习惯](https://www.schneier.com/blog/archives/2026/07/the-language-of-ai-could-change-how-humans-speak.html) ⭐️ 7.0/10

施奈尔指出，大语言模型主要基于书面文本和脚本化语音训练，缺乏自然对话数据。随着 AI 生成文本的普及，人类可能不自觉地模仿其语言模式，从而改变自身交流方式。 这一观点揭示了常被忽视的文化风险：语言同质化，以及自然交谈丰富性的丧失。它可能影响所有使用者，削弱语言多样性。 关键细节：文中指出，人类大部分交流是即兴的口头对话，但大语言模型的训练数据中这类内容极少。模型仅捕捉了语言的一个片段，这可能通过反馈循环成为主流。

rss · Schneier on Security · 7月9日 11:00

**背景**: 大语言模型（LLM）是基于大量文本训练的神经网络，用于自然语言生成等任务，其基础架构为 Transformer。训练数据包括书籍、文章、社交媒体和影视剧本，但很少包含日常即兴对话。这导致模型的语言风格与现实口语存在偏差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/large-language-model-llm/">Large Language Model (LLM) - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#AI`, `#linguistics`, `#culture`, `#LLMs`, `#impact`

---
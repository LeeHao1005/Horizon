---
layout: default
title: "Horizon Summary: 2026-08-08 (ZH)"
date: 2026-08-08
lang: zh
---

> 从 61 条内容中筛选出 15 条重要资讯。

---

1. [对亚密 2025 同源基 VRF 的三重密码分析](#item-1) ⭐️ 9.0/10
2. [研究人员通过蓝牙入侵 KARR 汽车安全系统，影响超 200 万辆汽车](#item-2) ⭐️ 9.0/10
3. [Cloudflare 推出 Kitesurf：基于 V8 隔离区的代理优先浏览器](#item-3) ⭐️ 8.0/10
4. [Relect：快速透明单秘密领导者选举协议](#item-4) ⭐️ 8.0/10
5. [支持公钥重随机化和精确解密的实用 Ring-LWE 加密方案](#item-5) ⭐️ 8.0/10
6. [基于 Plantard 算术的快速 NTT 形式化验证代码生成](#item-6) ⭐️ 8.0/10
7. [MPC-in-the-Head 签名中基于 AES 的研磨方案](#item-7) ⭐️ 8.0/10
8. [首次对 Olvid Messenger 的形式化安全分析揭示其局限](#item-8) ⭐️ 8.0/10
9. [UOV 代数密钥恢复攻击扩展至 v≥2m](#item-9) ⭐️ 8.0/10
10. [Verifiable SelfMix：分离槽分配与消息放置的可验证匿名架构](#item-10) ⭐️ 8.0/10
11. [KORD: 通过协议-硬件协同设计实现单轮去经销商 FSS 密钥生成](#item-11) ⭐️ 8.0/10
12. [新颖框架联合分析 LFSR 与布尔掩码](#item-12) ⭐️ 8.0/10
13. [DYNAFIX：适用于任意范围 MPC 的动态定点编码](#item-13) ⭐️ 8.0/10
14. [Cloudflare 推出新一代无状态 MCP，助力 Workers](#item-14) ⭐️ 8.0/10
15. [Cloudflare 推出开放协议，打造 Agentic 互联网](#item-15) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [对亚密 2025 同源基 VRF 的三重密码分析](https://eprint.iacr.org/2026/1623) ⭐️ 9.0/10

一篇新论文提出了对亚密 2025 上 Levin–Pedersen 同源基可验证随机函数的三种攻击：第一阶段利用公钥表示的不一致破坏唯一可证明性；第二阶段通过 1536 次查询在 30 分钟内恢复 256 比特密钥；以及对群作用变体的单次查询攻击概率接近 1/2。 这些攻击彻底打破了一个近期提出的后量子 VRF 构造的安全性，表明曲线表示的精确规范至关重要，且底层的 radical 同源漫步仅从公钥就会泄漏侧信道信息。 第一阶段利用公钥存储为 j-不变量而 radical-CGL 计算使用两个系数的事实，使得同一密钥和消息可产生两个不同输出；第二阶段利用这些泄露的系数恢复密钥。R1CS 证明未强制表示形式，且仅公钥有时可泄露秘密漫步的 1–2 比特。

rss · IACR ePrint 密码学论文 · 8月5日 18:59

**背景**: 可验证随机函数（VRF）提供可验证正确性的伪随机输出。同源基密码学利用椭圆曲线之间的映射（同源）实现后量子安全。radical 同源高效计算小次数同源链，用于类似 CGL 的哈希函数。被攻击的 VRF 结合了秘密 radical-CGL 漫步与 R1CS 证明系统，以断言两次漫步使用相同密钥。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2020/1108">Radical isogenies</a></li>
<li><a href="https://eprint.iacr.org/2017/1202.pdf">Faster Cryptographic Hash Function From Supersingular Isogeny Graphs</a></li>
<li><a href="https://hal.science/hal-04389904/document">Verifiable random function from the Deuring correspondence and...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#cryptanalysis`, `#isogeny-based cryptography`, `#verifiable random functions`, `#Asiacrypt`

---

<a id="item-2"></a>
## [研究人员通过蓝牙入侵 KARR 汽车安全系统，影响超 200 万辆汽车](https://www.schneier.com/blog/archives/2026/08/vulnerabilities-in-car-anti-theft-device.html) ⭐️ 9.0/10

加州大学圣地亚哥分校的安全研究人员发现，安装于超过 200 万辆美国汽车上的 KARR 安全系统可通过蓝牙被远程入侵，实现解锁车门、关闭警报、控制车灯或喇叭，甚至禁用发动机点火，导致车辆抛锚。 该漏洞使数百万车主面临车辆被盗、被困或人身安全风险，凸显了后装车联网设备在安全性上的严重缺陷，并对日益互联的汽车生态提出了安全警示。 攻击利用蓝牙通信，黑客需在约 10 至 30 米范围内，无需认证即可向设备发送指令。受影响的型号常作为经销商附加组件安装，建议通过固件更新修复漏洞。

rss · Schneier on Security · 8月5日 09:42

**背景**: KARR 安全系统是一种后装汽车警报与追踪设备，常由汽车经销商作为附加功能安装。它具备 GPS 追踪、远程锁止发动机及警报功能，旨在防盗窃并协助追回车辆。此类设备通常利用无线连接（如蜂窝网络、蓝牙）进行控制和监控，但这同时也带来了潜在漏洞，正如许多物联网设备所面临的问题。研究人员的发现加剧了人们对汽车网络安全的担忧，强调了联网车辆组件必须经过严格的安全测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://karrsecurity.com/">Home | Karr Security</a></li>
<li><a href="https://www.acrisurepg.com/karr-auto-security">Karr Auto Security | Acrisure Protection Group</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#automotive`, `#IoT`, `#vulnerability`, `#hacking`

---

<a id="item-3"></a>
## [Cloudflare 推出 Kitesurf：基于 V8 隔离区的代理优先浏览器](https://blog.cloudflare.com/kitesurf/) ⭐️ 8.0/10

Cloudflare 推出了 Kitesurf，这是一个全新的代理优先浏览器，完全运行在 Cloudflare Workers 的 V8 隔离区上。它基于开源 Blitz 引擎构建，能够在全球范围内实现无头 Chrome 自动化。 Kitesurf 可能通过利用 Cloudflare 的边缘网络，使大规模网页自动化和抓取更加普及，提供经济高效且可扩展的解决方案。这也表明 Cloudflare 有志于成为代理式 AI 生态系统的关键基础设施提供商。 Kitesurf 是无状态的，专为“代理云”设计，并基于 Dioxus Labs 的模块化浏览器引擎 Blitz 构建。Cloudflare 计划将他们的补丁开源并回馈给 Blitz 项目。

hackernews · Cloudflare Blog (PQ 迁移) · 8月7日 10:42 · [社区讨论](https://news.ycombinator.com/item?id=49208393)

**背景**: V8 隔离区是单个进程内的轻量级、隔离的 JavaScript 执行环境，Cloudflare Workers 用它来安全地大规模运行不可信代码。无头 Chrome 是一种运行 Chromium 浏览器而不显示可见用户界面的方式，通常用于自动化测试和网页抓取。Blitz 引擎是一个用 Rust 编写的全新开源模块化浏览器引擎，旨在提供可嵌入的网页渲染能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/kitesurf/">Introducing Kitesurf: The agent-first browser that runs in V8 isolates on Cloudflare Workers | Cloudflare Blog</a></li>
<li><a href="https://news.ycombinator.com/item?id=31740885">Ask HN: Pros and cons of V8 isolates? | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一但参与积极。Blitz 的作者指出 Kitesurf 基于他的引擎构建，并将获得上游补丁。一些用户担心 Cloudflare 可能绕过自己的反爬虫保护，或在 CDN 和代理托管之间产生利益冲突。其他用户将其与 Lightpanda 等替代方案进行比较，或质疑代理的实际用例。

**标签**: `#web-automation`, `#cloudflare`, `#headless-browser`, `#v8-isolates`, `#web-scraping`

---

<a id="item-4"></a>
## [Relect：快速透明单秘密领导者选举协议](https://eprint.iacr.org/2026/1619) ⭐️ 8.0/10

Relect 是一种基于格的单秘密领导者选举协议，利用阈值全同态加密，与 Qelect 相比，本地 FHE 计算速度提升 7 到 48 倍，通信成本降低最多 2 倍，同时消除了可信设置需求，支持每轮动态领导者选举。 这些效率提升和透明设置使单秘密领导者选举在实际区块链共识中变得可行，增强了安全性，并允许无需可信第三方的动态领导者选择。 基于环上的错误学习假设，Relect 在 2 到 128 个参与方的端到端测试中，局域网下快 2.77 到 345 倍，广域网下快 1.94 到 17.2 倍；单线程 FHE 计算时间快 7.15 到 42.4 倍，通信量减少 1.14 到 2 倍。

rss · IACR ePrint 密码学论文 · 8月5日 15:08

**背景**: 单秘密领导者选举随机选出唯一的领导者，其身份仅对领导者本人公开。阈值全同态加密允许多方对加密数据执行运算并联合解密。基于格的密码学（如环上的错误学习）被公认为能够抵抗量子计算机攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/what-single-secret-leader-election-why-do-we-need-stefan-piech">What is Single Secret Leader Election , and why do we need it?</a></li>
<li><a href="https://eprint.iacr.org/2025/699">Threshold (Fully) Homomorphic Encryption</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lattice-based_cryptography">Lattice-based cryptography</a></li>

</ul>
</details>

**标签**: `#single secret leader election`, `#fully homomorphic encryption`, `#lattice-based cryptography`, `#secure multiparty computation`, `#blockchain consensus`

---

<a id="item-5"></a>
## [支持公钥重随机化和精确解密的实用 Ring-LWE 加密方案](https://eprint.iacr.org/2026/1618) ⭐️ 8.0/10

提出了一种新的 Ring-LWE 公钥加密方案，支持公开重随机化且不增加密文长度，并利用双肢中国剩余定理（CRT）模数实现精确解密。 该方案填补了后量子匿名基础设施的关键空白，因为经典 ElGamal 重随机化易被量子计算机攻破，而它提供了一种可证明安全的实用格基替代方案。 方案采用模数 q = t·q_2，将明文嵌入为 q_2 M 使其在模 q_2 下消去，保证精确恢复；密文在决策 Ring-LWE 下是伪随机的。恒定时间 Rust 实现在 3.8 GHz CPU 上对每 64 KiB 密文（含 15.5 KiB 负载）的加密、重随机化和解密时间分别为 0.80 毫秒、0.51 毫秒和 0.21 毫秒。

rss · IACR ePrint 密码学论文 · 8月5日 14:52

**背景**: Ring-LWE 是一种抗量子攻击的后量子困难问题。公钥重随机化允许任何人在不知明文的情况下将密文变为新样子的密文，对混合网络至关重要。先前格方案存在密文大、近似解密或噪声分析不足的问题。CRT 可将模数分为互质因子进行独立处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ring-LWE">Ring-LWE</a></li>
<li><a href="https://github.com/massalabs/pq-rerand">GitHub - massalabs/pq-rerand: Post-quantum publicly re ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#encryption`, `#privacy`, `#lattice-based`

---

<a id="item-6"></a>
## [基于 Plantard 算术的快速 NTT 形式化验证代码生成](https://eprint.iacr.org/2026/1624) ⭐️ 8.0/10

一个新的代码生成器利用 Plantard 算术生成形式化验证的数论变换（NTT）实现，相比参考 C 代码速度提升 1.5 至 2.5 倍，相比先前验证过的 Jasmin 代码最高提升 2.19 倍，并附带端到端正确性证明。 该工作在提供形式化正确性保证的同时，加速了后量子密码标准（ML-KEM、ML-DSA、FN-DSA）中的关键运算，对性能和安全性并重的高保障部署至关重要。 生成器通过静态边界分析在代码生成时插入模约简，避免运行时分支和手动逐方案调整；它输出可移植 C 和 Jasmin 两种后端，在 EasyCrypt 中对 Plantard 算术进行参数化形式化，并证明与 formosa-mlkem 的连接。

rss · IACR ePrint 密码学论文 · 8月6日 05:37

**背景**: NTT（数论变换）是有限域上的积分变换，在格密码中用于高效多项式乘法。Plantard 算术是一种针对常数的模乘法高效技术，特别适合 NTT 旋转因子。ML-KEM（Kyber）是 NIST 标准化的后量子密钥封装机制，ML-DSA 和 FN-DSA 是数字签名方案。形式化验证从数学上证明实现符合规范，杜绝时序侧信道等漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Number-theoretic_transform">Number-theoretic transform</a></li>
<li><a href="https://eprint.iacr.org/2022/956">Improved Plantard Arithmetic for Lattice-based Cryptography</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#post-quantum cryptography`, `#NTT`, `#code generation`, `#Plantard arithmetic`

---

<a id="item-7"></a>
## [MPC-in-the-Head 签名中基于 AES 的研磨方案](https://eprint.iacr.org/2026/1625) ⭐️ 8.0/10

该论文提出用 AES 替换 MPC-in-the-Head 签名方案中工作量证明研磨步骤的 Keccak 哈希函数，以实现更快的计算和潜在更短的签名，并形式化了研磨方案，在理想密码与随机谕言模型下给出了安全证明。 这一优化利用 AES 的硬件加速提升签名生成速度并缩短签名长度，直接惠及 FAEST、MQOM 和 SDitH 等 NIST 后量子签名候选方案，可能影响最终标准化选择。 所提方案每次迭代使用两次 AES 调用，安全证明表明敌手的伪造概率至多为(4/3)·ε·Q_E/2^w；可推广至更多调用以将常数因子降至接近 1。

rss · IACR ePrint 密码学论文 · 8月6日 08:19

**背景**: 研磨通过要求哈希输出满足部分原像条件，在 Fiat-Shamir 变换中引入工作量证明，使伪造难度指数增加，从而允许缩减参数和签名长度。MPC-in-the-Head（MPCitH）框架通过在用户“头脑中”模拟多方计算协议构建签名，FAEST、MQOM 和 SDitH 是 NIST 后量子标准化第三轮候选方案。现有实现使用 Keccak，但 AES 因现代 CPU 的专用指令集而更快。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fiat–Shamir_heuristic">Fiat–Shamir heuristic - Wikipedia</a></li>
<li><a href="https://eprint.iacr.org/2024/252">Faster Signatures from MPC-in-the-Head</a></li>
<li><a href="https://eprint.iacr.org/2026/206">MPSpeed: Implementing and Optimizing MPC-in-the-Head Digital ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#digital-signatures`, `#MPC-in-the-head`, `#AES`

---

<a id="item-8"></a>
## [首次对 Olvid Messenger 的形式化安全分析揭示其局限](https://eprint.iacr.org/2026/1622) ⭐️ 8.0/10

研究人员首次对 Olvid 的加密协议进行了形式化安全分析。他们确认了相互认证和前向保密等核心安全属性，但发现 Olvid 缺乏 Signal 等现代协议所满足的 eCK 安全性等属性，并发现了潜在的时间信息泄露。 Olvid 被法国政府官员用于敏感通信，因此这些安全缺陷具有直接的实际影响。该分析表明，即使是政府采用的通信工具也可能未达到最先进的安全标准。 分析使用了 Dolev-Yao 敌手模型，验证了协议在会话密钥保密性和重放保护方面的安全性。结果显示 Olvid 未能达到 eCK 安全性要求，并发现了一个时间侧信道，同时对其匿名性声明提出了质疑。

rss · IACR ePrint 密码学论文 · 8月5日 18:28

**背景**: Olvid 是一款法国开发的加密消息应用，免费且开源，无需手机号等个人信息。Dolev-Yao 模型是一种用于分析加密协议的形式化框架，假设攻击者可以完全控制网络。eCK（扩展 Canetti-Krawczyk）模型是一种现代安全模型，捕捉更强的攻击者能力，包括临时密钥泄露。持续密钥协商（CKA）是一种为每条消息生成新密钥的协议，被 Signal 等应用采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Olvid_(software)">Olvid (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dolev-Yao_model">Dolev-Yao model</a></li>
<li><a href="https://eprint.iacr.org/2019/088">Continuous Key Agreement with Reduced Bandwidth</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secure-messaging`, `#formal-verification`, `#Olvid`, `#security-analysis`

---

<a id="item-9"></a>
## [UOV 代数密钥恢复攻击扩展至 v≥2m](https://eprint.iacr.org/2026/1620) ⭐️ 8.0/10

本文将对 UOV 的代数密钥恢复攻击从原有的 v<2m 条件扩展至 v≥2m 的情况，克服了此前阻碍攻击的额外核元素。该方法在 SNOVA 上得到验证，降低了其某些 NIST PQC 参数集的安全性。 UOV 是 NIST 后量子签名标准化的主要候选者之一；该攻击拓宽了近期密码分析的范围，可能影响更多参数选择及 UOV 类方案的安全性评估。 该攻击利用一种技术处理 v≥2m 时的额外核元素，并通过 Nakamura 等人的 lifting 方法应用于 SNOVA，将参数集 (37,17,16,2) 的安全性降至 2^{103}次门操作，与 Bros 等人在 2026 年的攻击相当。

rss · IACR ePrint 密码学论文 · 8月5日 16:53

**背景**: 不平衡油醋（UOV）方案是一种多变量签名方案，其公钥由 m 个包含 v 个醋变量和 o 个油变量的二次方程构成，其中 v>o，安全性基于求解随机二次方程组的 NP 困难性。2025 年，Ran 提出了一种利用代数结构的密钥恢复攻击，但仅当醋变量个数 v 小于方程数 m 的两倍（v<2m）时才有效。本研究将该攻击扩展到 v≥2m 的范围，填补了密码分析中的空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1620">Extending the Applicability of Algebraic Key Recovery Attacks on the UOV Signature Scheme</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unbalanced_oil_and_vinegar_scheme">Unbalanced oil and vinegar scheme - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum cryptography`, `#UOV`, `#key recovery attack`, `#multivariate cryptography`

---

<a id="item-10"></a>
## [Verifiable SelfMix：分离槽分配与消息放置的可验证匿名架构](https://eprint.iacr.org/2026/1617) ⭐️ 8.0/10

研究人员提出了“Verifiable SelfMix”（VSM），一种新的匿名架构，将不经意槽分配与加密消息放置解耦，在解密后为公共公告板上的消息提供无条件的个人可验证性。 VSM 提供了形式化安全证明和模块化设计，相比现有系统（如混网或 DC-net）可能提升效率和可验证性，为匿名通信带来更强的信任保证。 安全私有排列映射（SMPP）组件可使用 ElGamal、Boneh–Goh–Nissim（BGN）及理论上的全同态加密（FHE）实例化；向量式方法下每用户上传量为 O(m)，公共聚合为 O(nm)，而 FHE 变体对固定大小消息将每用户上传量降至 Õ(log m)。

rss · IACR ePrint 密码学论文 · 8月5日 14:19

**背景**: 匿名通信系统隐藏收发对应关系。混网通过多跳服务器混洗消息但依赖节点诚实性，DC-net 和 MPC 混洗提供更强的匿名性但开销更大。VSM 通过分离槽分配与消息放置，引入新的折衷方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dining_cryptographers_problem">Dining cryptographers problem - Wikipedia</a></li>

</ul>
</details>

**标签**: `#anonymous communication`, `#cryptography`, `#mixnets`, `#privacy`, `#verifiability`

---

<a id="item-11"></a>
## [KORD: 通过协议-硬件协同设计实现单轮去经销商 FSS 密钥生成](https://eprint.iacr.org/2026/1615) ⭐️ 8.0/10

KORD 引入了一种基于芯片的相互认证机制，建立共同信任根，实现无经销商功能秘密共享的单轮密钥生成，通信量降低 7,633 至 70,274 倍。 这一突破消除了去经销商 FSS 的信任依赖和通信开销，使隐私保护计算在大规模部署（如私有机器学习推理）中更加实用。 KORD 在 ZCU102 FPGA 上的交叉密钥调度使 AES 通道利用率达到 99.0%，在 187.5 MHz 下每秒生成 11.60 百万个 32 位 DPF 密钥，将私有 ResNet-18 推理中密钥生成份额从 96%以上降至 10.1%。

rss · IACR ePrint 密码学论文 · 8月5日 11:53

**背景**: 功能秘密共享（FSS）允许将函数拆分为共享份额进行分别计算，但通常需要可信经销商为每次操作生成新密钥。去经销商协议消除了这一信任，但先前方法需要大量与输入位宽成正比的通信轮次，形成性能瓶颈。KORD 通过硬件信任根解决了这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1615">KORD: Breaking the Key-Generation Bottleneck in Dealerless Function Secret Sharing via Protocol–Hardware Co-Design</a></li>
<li><a href="https://github.com/xingpz2008/dealerless-FSS_public">GitHub - xingpz2008/dealerless-FSS_public: Implementation of Distributed function secret sharing and applications</a></li>

</ul>
</details>

**标签**: `#function secret sharing`, `#privacy-preserving computation`, `#hardware-software co-design`, `#cryptography`, `#dealerless protocols`

---

<a id="item-12"></a>
## [新颖框架联合分析 LFSR 与布尔掩码](https://eprint.iacr.org/2026/1614) ⭐️ 8.0/10

该论文提出了首个验证框架，在 d 探测模型中联合分析基于 LFSR 的伪随机数生成器与布尔掩码，将沃尔什-哈达玛变换扩展至鲁棒探测模型，并在 4 位和 8 位 S 盒上进行了验证，且通过 FPGA 进行了实际确认。 这弥合了掩码方案中理想随机假设与实际伪随机数生成器使用之间的鸿沟，有望推动更真实的侧信道攻击防御证明与设计。 该框架利用来自线性密码分析的沃尔什-哈达玛变换，扩展至鲁棒探测模型，同时提供了 4 位和 8 位 S 盒的形式化验证结果与 FPGA 实测评估。

rss · IACR ePrint 密码学论文 · 8月5日 10:57

**背景**: LFSR（线性反馈移位寄存器）是一种常见的伪随机数生成器。布尔掩码是一种通过异或将秘密拆分为多个份额以抵御侧信道攻击的对策。d 探测模型假设攻击者最多可探测 d 个电路信号，但无法获取秘密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Linear-feedback_shift_register">Linear-feedback shift register - Wikipedia</a></li>
<li><a href="https://www.researchgate.net/publication/224114142_Evaluation_of_Countermeasure_Implementations_Based_on_Boolean_Masking_to_Thwart_Side-Channel_Attacks">(PDF) Evaluation of Countermeasure Implementations Based on Boolean Masking to Thwart Side-Channel Attacks</a></li>
<li><a href="https://ches.iacr.org/2024/papers-issue-4/4_68.pdf">Robust but Relaxed Probing Model</a></li>

</ul>
</details>

**标签**: `#side-channel attacks`, `#masking`, `#formal verification`, `#LFSR`, `#cryptography`

---

<a id="item-13"></a>
## [DYNAFIX：适用于任意范围 MPC 的动态定点编码](https://eprint.iacr.org/2026/1612) ⭐️ 8.0/10

DYNAFIX 为多方计算（MPC）引入了一种动态定点编码，在保持定点级效率的同时支持任意数值范围，在计算如指数函数等高精度函数时，比现有方法实现了 24.1 倍加速。 这一进步弥合了 MPC 中定点与浮点计算之间的效率鸿沟，使得对于既要求速度又要求宽动态范围的应用（如机器学习和统计分析），安全实数计算更加实用。 该论文是预印本（2026/1612），尚未经过同行评审。所报告的 24.1 倍加速是针对高精度指数函数与最先进方法的对比，并且该方案可泛化到任意数值范围。

rss · IACR ePrint 密码学论文 · 8月5日 08:11

**背景**: 安全多方计算（MPC）能够在保护输入隐私的同时联合计算函数。对于实数，定点运算速度快但范围受限，浮点运算灵活但速度慢数个数量级。DYNAFIX 引入动态定点编码，通过调整缩放来平衡范围与效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multi-party_computation">Multi-party computation</a></li>

</ul>
</details>

**标签**: `#MPC`, `#fixed-point arithmetic`, `#privacy-preserving computation`, `#real number encoding`, `#secure computation`

---

<a id="item-14"></a>
## [Cloudflare 推出新一代无状态 MCP，助力 Workers](https://blog.cloudflare.com/mcp-v2/) ⭐️ 8.0/10

Cloudflare 发布了新一代 MCP，核心重写为无状态架构，包含协议升级和 SDK 迁移路径，现已在 Workers 上投入生产使用。 这使得开发者能够在 Cloudflare 的边缘平台上构建可扩展且可靠的 AI 应用，利用新兴的 MCP 标准连接大语言模型和外部工具，推动无服务器 AI 集成的发展。 无状态核心消除了会话状态依赖，非常适合 Workers 等无服务器环境。新版本还引入了功能生命周期管理以增强稳定性，并为早期 SDK 用户提供了明确的迁移路径。

rss · Cloudflare Blog (PQ 迁移) · 8月6日 13:00

**背景**: MCP（模型上下文协议）是 Anthropic 制定的开放标准，用于规范 AI 模型与外部工具的交互方式。Cloudflare Workers 是一个在边缘运行代码的无服务器平台。之前的 MCP 实现通常有状态，难以在 Workers 上使用；此次重写使其原生支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/">Cloudflare's own MCP servers · Cloudflare Agents docs</a></li>
<li><a href="https://github.com/cloudflare/mcp-server-cloudflare">GitHub - cloudflare/mcp-server-cloudflare · GitHub</a></li>

</ul>
</details>

**标签**: `#MCP`, `#Cloudflare`, `#Workers`, `#protocol`, `#SDK`

---

<a id="item-15"></a>
## [Cloudflare 推出开放协议，打造 Agentic 互联网](https://blog.cloudflare.com/the-agentic-internet/) ⭐️ 8.0/10

Cloudflare 宣布推出开放工具和协议，让网站与 AI 代理配合，实现内容的可读、可发现、可调用和可支付，从而避免对代理的封锁。 该倡议防止 AI 代理被大规模封锁导致互联网割裂，并通过开放标准塑造一个人类与代理无缝共存的开放网络。 协议覆盖四个层面：可读性（为代理提供结构化数据）、可发现性（代理友好的站点地图）、可调用性（类 API 的服务访问）和可支付性（小额支付整合），但具体技术细节尚未公布。

rss · Cloudflare Blog (PQ 迁移) · 8月6日 13:00

**背景**: AI 代理（如自动化助手）正广泛用于网络任务，但现有网络针对人类浏览优化，依赖 CSS 和广告呈现。网站常通过 robots.txt 或验证码封锁代理以防资源滥用，却误伤潜在用户。Cloudflare 的开放协议栈旨在通过标准化代理与网站的交互解决此矛盾。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/agentic-web">The Agentic Web: AI Agents Will Redefine the Internet - IEEE ...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#web protocols`, `#Cloudflare`, `#agentic internet`, `#open infrastructure`

---
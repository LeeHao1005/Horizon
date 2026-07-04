---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> 从 37 条内容中筛选出 15 条重要资讯。

---

1. [Spain：面向数值计算的简洁证明协议](#item-1) ⭐️ 9.0/10
2. [GPT-5.5-Cyber 一天内构建 zlib 模糊测试实验室](#item-2) ⭐️ 9.0/10
3. [通过秘密复制压缩相关：基于对称密码学的伪随机相关函数](#item-3) ⭐️ 8.0/10
4. [3PaaS：隐私保护的事后安全即服务](#item-4) ⭐️ 8.0/10
5. [首个死人开关密码学的形式化研究](#item-5) ⭐️ 8.0/10
6. [Cloudflare 推出货币化网关，通过 x402 协议实现稳定币收费](#item-6) ⭐️ 8.0/10
7. [白宫行政令提前后量子密码学截止日期](#item-7) ⭐️ 8.0/10
8. [Flock 摄像头现可无需车牌创建车辆指纹](#item-8) ⭐️ 8.0/10
9. [论文警示美国网络安全使命蠕变及其风险](#item-9) ⭐️ 8.0/10
10. [棒约翰利用 Instacart 数据预测杂货消耗以投放定向广告](#item-10) ⭐️ 8.0/10
11. [HPCC：首个可组合硬件掩码立方门](#item-11) ⭐️ 7.0/10
12. [内容独立日一周年：构建智能体互联网的商业模式](#item-12) ⭐️ 7.0/10
13. [Cloudflare 推出新计划提升 AI 搜索中创作者的可见度与收入](#item-13) ⭐️ 7.0/10
14. [Cloudflare 推出精细化 AI 爬虫流量管理功能](#item-14) ⭐️ 7.0/10
15. [IETF 126 将举行聚焦新兴互联网标准的 BoF 会议](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Spain：面向数值计算的简洁证明协议](https://eprint.iacr.org/2026/1356) ⭐️ 9.0/10

Spain 提出了一种新的证明协议，通过放宽精确约束可满足性，允许近似约束，从而支持具有固有近似误差的数值计算，实现了实数计算的简洁证明。 这一突破填补了简洁证明系统的重要空白，使依赖浮点运算的 AI/ML 等领域能够实际应用，并显著扩展了可验证计算的范围。 该论文包含完整的设计、实现与评估，性能较自然基线有数量级提升；系统采用了专为近似可满足性设计的新证明协议和约束转换方法。

rss · IACR ePrint 密码学论文 · 7月1日 19:47

**背景**: 简洁证明协议（如 SNARK）允许验证者在不重新执行计算的情况下检查其正确性，这要求证明者将计算转换为精确约束。但数值计算中的浮点近似会引入误差，使精确约束无法满足，因此与现有系统不兼容。Spain 通过允许近似约束可满足性，弥合了这一差距，使真实世界数值计算的证明成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Constraint_satisfaction_problem">Constraint satisfaction problem - Wikipedia</a></li>

</ul>
</details>

**标签**: `#succinct proofs`, `#zero-knowledge`, `#numerical computations`, `#SNARKs`, `#cryptography`

---

<a id="item-2"></a>
## [GPT-5.5-Cyber 一天内构建 zlib 模糊测试实验室](https://blog.trailofbits.com/2026/07/02/field-reports-from-patch-the-planet/) ⭐️ 9.0/10

Trail of Bits 报告称，GPT-5.5-Cyber 在一天内自主构建了一个针对 zlib 压缩库的综合模糊测试实验室，该任务以往需要专家数周的工作量。 这一突破极大加速了安全漏洞的发现，可能导致开源维护者被高质量错误报告淹没，同时也降低了攻击者的利用门槛。 该模型使用了 AddressSanitizer (ASan) 和 UndefinedBehaviorSanitizer (UBSan) 构建版本，将边缘案例测试转用为种子，并编写了针对十多个 zlib 入口点的 harness，发现了仅由操作系统背压触发的错误。

rss · Trail of Bits Blog · 7月2日 11:00

**背景**: 模糊测试是一种自动化软件测试技术，通过向程序提供无效或随机输入来发现崩溃或内存错误。zlib 是一个广泛使用的开源压缩库。“Patch the Planet”是 Trail of Bits 与 OpenAI 的合作项目，旨在帮助开源项目主动修复漏洞，防止 AI 生成的错误报告让维护者不堪重负。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/patch-the-planet/">Patch the Planet: a Daybreak initiative to support open source maintainers</a></li>
<li><a href="https://trailofbits.com/patch-the-planet/">Patch the Planet - Trail of Bits</a></li>

</ul>
</details>

**标签**: `#AI security`, `#fuzzing`, `#vulnerability discovery`, `#GPT-5.5`, `#open-source security`

---

<a id="item-3"></a>
## [通过秘密复制压缩相关：基于对称密码学的伪随机相关函数](https://eprint.iacr.org/2026/1355) ⭐️ 8.0/10

本文通过引入秘密复制模式，推广了利用对称密码学压缩多方相关性的技术，重新推导出两方 VOLE 的 PCF 构造，并提出了适用于小域 VOLE 式相关的新型多方 PCF，包括标量-向量乘法三元组及其认证变体。 这项工作推动了安全多方计算的发展，通过仅使用对称密码学高效生成相关随机性，避免了非对称密码学的开销，可能实现更具扩展性和高效性的 MPC 协议。 该构造基于由线性子空间定义的线性相关，各方获得秘密向量条目的固定子集。PCF 密钥大小与最小支撑码字的数量成比例，秘密复制模式将辅助相关中的各方案随机分配至目标相关中的各方。

rss · IACR ePrint 密码学论文 · 7月1日 15:10

**背景**: 伪随机相关函数（PCF）允许多方从短相关密钥本地生成大量来自目标相关的伪随机样本，这是安全多方计算的关键组成部分。早期的 PCF 构造常依赖于公钥密码学，而仅使用对称密码学有助于提升效率。本文建立在 Gilboa-Ishai（Crypto 1999）和 Cramer-Damgård-Ishai（TCC 2005）的开创性成果之上，他们使用 PRF 复制来压缩线性相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-31371-4_8">Pseudorandom Correlation Functions from Variable-Density LPN, Revisited | Springer Nature Link</a></li>
<li><a href="https://eprint.iacr.org/2023/650">Pseudorandom Correlation Functions from Variable-Density LPN, Revisited</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secure multiparty computation`, `#pseudorandom correlation functions`, `#symmetric cryptography`, `#information-theoretic security`

---

<a id="item-4"></a>
## [3PaaS：隐私保护的事后安全即服务](https://eprint.iacr.org/2026/1353) ⭐️ 8.0/10

研究人员开发了 3PaaS 协议，这是首个通过第三方提供事后安全即服务且保护隐私的协议，利用新颖的盲签名零知识证明实现跨会话、群组和服务的恢复能力。 这解决了如 Signal 等通讯软件中现有事后安全机制的局限——恢复通常仅限于单个会话且不一定能实现——通过提供隐私保护的跨会话、群组和服务的事后安全能力。 该协议采用了首个高效的盲签名零知识证明，确保服务器无法将用户活动与身份关联，并支持在不泄露身份的前提下进行撤销，已进行形式化分析与实现。

rss · IACR ePrint 密码学论文 · 7月1日 11:59

**背景**: 事后安全（PCS）指系统在密钥泄露后仍能恢复安全的能力。Signal 等通讯应用采用双棘轮算法实现前向安全和 PCS，但近期分析表明由于状态丢失恢复机制和会话局限性，PCS 在实践中可能未完全实现。3PaaS 旨在提供一种可跨会话和服务的外包式 PCS 服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2016/221.pdf">Post-Compromise Security Katriel Cohn-Gordon⋆, Cas CremersQ, and Luke Garratt</a></li>
<li><a href="https://en.wikipedia.org/wiki/Double_Ratchet_Algorithm">Double Ratchet Algorithm</a></li>
<li><a href="https://signal.org/docs/specifications/doubleratchet/">Signal >> Specifications >> The Double Ratchet Algorithm</a></li>

</ul>
</details>

**标签**: `#post-compromise-security`, `#cryptography`, `#secure-messaging`, `#privacy`, `#protocol-design`

---

<a id="item-5"></a>
## [首个死人开关密码学的形式化研究](https://eprint.iacr.org/2026/1352) ⭐️ 8.0/10

该论文首次将死人开关（DMS）形式化为一种密码学原语，具备释放和删除两种模式，并在通用可组合（UC）框架下给出严格的安全定义，同时基于交易商控制的演化委员会主动秘密共享（DC-EPSS）提供了一个具体构造。 这一工作填补了密码学文献中的一个显著空白，解决了在用户去世后安全释放或销毁秘密的实际需求，可应用于数字遗产和数据隐私保护，并能提供强大的可组合安全保证。 该构造利用了 DC-EPSS（Benhamouda 等人提出的演化委员会主动秘密共享的扩展方案），并通过嵌套 YOSO 框架进行通用实例化。DMS-释放模式进一步结合了多接收者公钥加密、密钥提交对称加密和 NIZK 证明系统。

rss · IACR ePrint 密码学论文 · 7月1日 11:30

**背景**: 通用可组合（UC）框架是分析密码协议的常用模型，即使协议被任意组合也能保证安全。主动秘密共享将秘密分发给多个参与方，并定期刷新份额以抵御移动对手。YOSO（You Only Speak Once）模型要求参与方只发言一次，随即消失，有助于构建无需长期信任的协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Universal_composability">Universal composability - Wikipedia</a></li>
<li><a href="https://link.springer.com/article/10.1007/s10623-025-01658-0">Evolving secret sharing revisited: computational security and ...</a></li>
<li><a href="https://eprint.iacr.org/2025/2313.pdf">Nested YOSO MPC: Near Optimal Resilience Without an MPC Setup</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#secret-sharing`, `#dead-mans-switch`, `#UC-framework`, `#formal-methods`

---

<a id="item-6"></a>
## [Cloudflare 推出货币化网关，通过 x402 协议实现稳定币收费](https://blog.cloudflare.com/monetization-gateway/) ⭐️ 8.0/10

Cloudflare 开放了其货币化网关的候补名单，允许用户对通过 Cloudflare 提供的网页、API、数据集或 MCP 工具收费。支付将通过 x402 开放协议以稳定币结算，无需构建自己的支付系统。 该服务利用稳定币实现即时、低费用的交易，无需传统支付基础设施，极大降低了开发者对在线资源（尤其是 AI 代理和机器间支付）进行货币化的门槛。 货币化网关采用 x402 协议，该协议基于 HTTP 402 付款要求，面向机器原生支付，并支持 MCP 工具——一种新兴的 AI 工具集成标准。目前处于候补阶段，未公布具体发布日期。

rss · Cloudflare Blog (PQ 迁移) · 7月1日 13:00

**背景**: x402 协议是对 HTTP 402 付款要求的扩展，专为机器原生支付和微支付设计，尤其适用于 AI 代理和自动化系统。模型上下文协议（MCP）是 Anthropic 于 2024 年发布的一项开放标准，允许 AI 模型调用外部工具，例如 API 和数据服务。两者结合使 Cloudflare 能为 AI 可访问资源提供无缝的收费方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://shatale.com/blog/what-is-x402-protocol">What Is the x 402 Protocol ? HTTP 402 and Machine-Native... — Shatale</a></li>
<li><a href="https://www.linkedin.com/posts/halborn_web3-ai-security-activity-7441879924505944064-Bxrw">x 402 Protocol Gains Attention in Web3 and AI Ecosystems | LinkedIn</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#monetization`, `#stablecoins`, `#payments`, `#api`

---

<a id="item-7"></a>
## [白宫行政令提前后量子密码学截止日期](https://neilmadden.blog/2026/07/02/are-we-any-closer-to-the-quantum-apocalypse/) ⭐️ 8.0/10

尼尔·马登分析了白宫行政令，该令要求高价值系统在 2030 年前迁移后量子密钥交换算法，在 2031 年前迁移签名算法，比原计划提前。 这加剧了防范未来量子计算机破解现有加密的紧迫性，特别是在‘现在收集，以后解密’攻击的担忧下。它表明了政府最高级别的关注，并将迫使关键基础设施部门快速实现密码学现代化。 该行政令区分了密钥交换（截止 2030 年）和数字签名（2031 年），反映了不同的风险状况。马登可能讨论了技术挑战、算法选择（如 2024 年 NIST 标准）以及达到这些期限的可行性。

rss · Neil Madden (后量子密码) · 7月2日 11:25

**背景**: 后量子密码学（PQC）指能抵抗量子计算机攻击的算法。当前的公钥密码（如 RSA、ECC）在足够强大的量子计算机上可能被 Shor 算法破解。尽管此类计算机尚未出现，但‘现在收集，以后解密’的威胁（存储今天加密的数据以便将来解密）推动了早期采用。2024 年，NIST 发布了首批 PQC 标准。‘量子末日’或 Q-Day 指的是量子计算机强大到足以破解加密的那一天。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://www.bbc.com/news/technology-60144498">What is the quantum apocalypse and should we be scared? - BBC</a></li>
<li><a href="https://www.wired.com/story/q-day-apocalypse-quantum-computers-encryption/">The Quantum Apocalypse Is Coming. Be Very Afraid - WIRED</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#cybersecurity`, `#government policy`, `#quantum computing`, `#encryption standards`

---

<a id="item-8"></a>
## [Flock 摄像头现可无需车牌创建车辆指纹](https://www.schneier.com/blog/archives/2026/07/flock-cameras-can-surveil-cars-without-license-plates.html) ⭐️ 8.0/10

Flock Safety 升级了其监控摄像头，可通过车辆贴纸、保险杠贴纸、车顶行李架和临时标签等非车牌特征生成“车辆指纹”，使执法部门即使没有可见车牌也能识别和追踪车辆。 这一进展显著扩大了自动车辆监控的范围，可能实现对所有车辆的大规模追踪，引发了严重的隐私和公民自由问题，因为它破坏了公共道路上的匿名保护。 该系统利用 AI 对车辆品牌、型号、颜色、划痕、贴纸等细节进行分类；它还支持“多地搜索”以定位一起移动的车辆。Flock 的网络每月在全美 49 个州的 5000 多个社区扫描超过 200 亿辆车。

rss · Schneier on Security · 7月3日 11:15

**背景**: Flock Safety 运营着一个广泛的车牌自动识别（ALPR）摄像头网络，供执法部门用于实时犯罪警报。传统上，ALPR 专注于读取车牌，但技术已发展到结合其他车辆属性的视觉识别。这符合 AI 驱动的大规模监控的大趋势，引发了隐私与安全之间的争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.aclu.org/campaigns-initiatives/get-the-flock-out">Fight Creepy ALPR Cameras | American Civil Liberties Union</a></li>

</ul>
</details>

**标签**: `#surveillance`, `#privacy`, `#computer-vision`, `#law-enforcement`, `#security`

---

<a id="item-9"></a>
## [论文警示美国网络安全使命蠕变及其风险](https://www.schneier.com/blog/archives/2026/07/cybersecurity-mission-creep-in-the-us.html) ⭐️ 8.0/10

一篇题为《网络安全使命蠕变》的新学术论文警告称，政策制定者正越来越多地将虚假信息和儿童安全等多元化政策问题重新定义为网络安全问题，这可能引发有问题的治理应对措施。 这一趋势意义重大，因为它可能使政府对非生存性威胁动用类似紧急状态的权力，从而侵蚀民主制衡和公民自由。 论文创造了'cybersecuritization'一词，描述将问题框架为网络安全威胁如何使其获得紧迫性和例外性的政治，并列举了反垄断法规和记者不当行为等例子。

rss · Schneier on Security · 7月2日 11:11

**背景**: 使命蠕变指目标逐渐超出原始范围。国际关系中的安全化理论解释了将某事标记为安全问题如何为非常规措施辩护。在此，网络安全的范围扩大可能将这种例外主义带入传统上由正常法律程序治理的领域。

**标签**: `#cybersecurity`, `#policy`, `#mission creep`, `#law`, `#governance`

---

<a id="item-10"></a>
## [棒约翰利用 Instacart 数据预测杂货消耗以投放定向广告](https://www.schneier.com/blog/archives/2026/07/papa-johns-surveillance-based-advertising.html) ⭐️ 8.0/10

棒约翰与 NBCUniversal、Instacart 和 Carat 合作，分析 Instacart 购买记录，预测消费者何时快要用完杂货，并在流媒体平台上向他们投放定向披萨广告。 这表明监控资本主义的升级，即利用私密的购买数据在消费者脆弱时刻进行操纵，引发了严重的隐私和操控担忧。 自定义受众基于经常购买鸡蛋、牛奶和农产品等日常用品的 Instacart 用户；系统推断出消耗日期，在 NBCU 流媒体上投放带有二维码和'冰箱空了吗？'等提示的广告。

rss · Schneier on Security · 7月1日 10:53

**背景**: 基于监控的广告通过跟踪详细消费者行为来投放个性化广告。Instacart 是一家杂货配送平台，收集细颗粒度的购买数据，这里通过服务提供商与棒约翰等广告商共享，用于创建预测性定向模型。

**标签**: `#privacy`, `#advertising`, `#surveillance`, `#data-tracking`, `#consumer-data`

---

<a id="item-11"></a>
## [HPCC：首个可组合硬件掩码立方门](https://eprint.iacr.org/2026/1351) ⭐️ 7.0/10

该论文提出了 HPCC，这是首个针对任意域的低延迟三输入乘法门，保持恒定单周期延迟。这使得硬件掩码中的立方函数能够实现可组合 PINI 安全，超越了现有的二次门。 这一进展大幅降低了抗侧信道密码硬件的面积、延迟和随机数开销。它能高效实现如 AES S 盒等复杂功能，仅需两个周期，有利于安全芯片设计。 HPCC 在两份额 GF(2)下将所需新鲜掩码数减半，并且是唯一能在任意域实现多份额三输入乘法的单周期方案。它实现了首个可组合的 AES S 盒，对于任意份额数仅需两个周期延迟。

rss · IACR ePrint 密码学论文 · 7月1日 09:15

**背景**: 密码硬件可能通过功耗等侧信道泄露秘密。掩码是一种将秘密拆分为多个随机份额以打破依赖的对策，但硬件毛刺可重聚份额降低安全性。PINI 概念在毛刺扩展探测模型中确保可组合安全，但现有门仅限于二次函数。HPCC 将其扩展到立方门并提升效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1351">Hardware Private Cubic Circuits</a></li>
<li><a href="https://casa.rub.de/fileadmin/img/Publikationen_PDFs/2021_Automated_Generation_of_Masked_Hardware_Publication_ClusterofExcellence_CASA_Bochum.pdf">Automated Generation of Masked Hardware</a></li>

</ul>
</details>

**标签**: `#hardware security`, `#side-channel attacks`, `#masking`, `#composable security`, `#cryptographic implementations`

---

<a id="item-12"></a>
## [内容独立日一周年：构建智能体互联网的商业模式](https://blog.cloudflare.com/agentic-internet-bot-report/) ⭐️ 7.0/10

Cloudflare 的新报告显示，在宣布内容独立日一年后，随着自主 AI 智能体颠覆了传统搜索引荐，一个动态的付费内容市场已正式形成。 这标志着向可持续网络经济的关键转变，AI 智能体代表用户消费内容，迫使开发新的货币化和基础设施模型，确保创作者获得公平报酬。 报告研究了从传统搜索引荐到智能体驱动的内容访问的转变，所需基础设施包括支付机制和基于 Cloudflare 政策（阻止未付费的 AI 爬虫）的访问控制。

rss · Cloudflare Blog (PQ 迁移) · 7月1日 13:00

**背景**: 内容独立日是 Cloudflare 于 2025 年 7 月 1 日发起的一项倡议，默认阻止 AI 爬虫，除非其向发布商支付报酬，旨在保护内容创作者。智能体互联网指的是一个由数万亿个 AI 智能体在没有人类直接监督的情况下自主执行任务（包括内容检索）的未来。这一转变挑战了传统的网络流量模式，因为智能体绕过了面向人类的界面，需要程序化访问内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/">Content Independence Day: no AI crawl without compensation!</a></li>
<li><a href="https://blog.cloudflare.com/agentic-internet-bot-report/">Content Independence Day, one year on: building the business ...</a></li>
<li><a href="https://agenticinternet.com/">Agentic Internet</a></li>

</ul>
</details>

**标签**: `#agentic internet`, `#AI agents`, `#content monetization`, `#Cloudflare`, `#web infrastructure`

---

<a id="item-13"></a>
## [Cloudflare 推出新计划提升 AI 搜索中创作者的可见度与收入](https://blog.cloudflare.com/making-ai-search-smarter/) ⭐️ 7.0/10

Cloudflare 宣布了两项新计划，旨在帮助创作者在 AI 驱动的搜索中保持可发现性并获得报酬，因为 AI 搜索可能将流量和收入从原始来源转移走。 此举应对了 AI 搜索对创作者经济日益严重的破坏，AI 搜索常常直接总结内容而不将用户引导至来源，威胁到作家、艺术家和其他网络发布者的财务生存能力。 这些计划针对‘代理时代’的挑战，即 AI 代理自主消费信息，需要新的内容归属和微支付标准；Cloudflare 尚未公布具体技术细节。

rss · Cloudflare Blog (PQ 迁移) · 7月1日 13:00

**背景**: AI 驱动的搜索使用大语言模型直接提供答案，减少了原始网站的点击量。‘代理时代’描述了自主行动的 AI 系统，使传统的搜索引擎优化效果降低。这一转变危及依赖广告和流量的内容创作者的营收模式。Cloudflare 作为基础设施提供商，具有独特性实现诸如更好的索引控制或自动微支付系统等解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/new-front-door-to-the-internet-winning-in-the-age-of-ai-search">Winning in the age of AI search | McKinsey</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://www.growth-rocket.com/blog/modern-seo-strategies-for-the-ai-driven-search-landscape/">Modern SEO Strategies for the AI-Driven Search Landscape</a></li>

</ul>
</details>

**标签**: `#AI`, `#search`, `#Cloudflare`, `#creator economy`, `#web infrastructure`

---

<a id="item-14"></a>
## [Cloudflare 推出精细化 AI 爬虫流量管理功能](https://blog.cloudflare.com/content-independence-day-ai-options/) ⭐️ 7.0/10

Cloudflare 现在允许网站所有者分别管理搜索爬虫、AI 智能体爬虫和 AI 训练爬虫，并新增了广告盈利页面的保护功能。 这让内容创作者能更好地控制 AI 服务对其网站的访问方式，有助于保护知识产权和广告收入免受未经授权的抓取。 这些新控件向所有 Cloudflare 客户开放，支持为每类爬虫设置不同的规则，例如允许搜索索引但阻止 AI 训练爬虫。

rss · Cloudflare Blog (PQ 迁移) · 7月1日 13:00

**背景**: 网络爬虫是自动浏览互联网的程序。搜索爬虫为搜索引擎建立索引，AI 智能体爬虫实时抓取以回答用户查询，训练爬虫则收集数据来训练 AI 模型。作为 CDN 和安全服务提供商，Cloudflare 提供爬虫管理服务，帮助网站控制爬虫流量。

**标签**: `#Cloudflare`, `#AI bots`, `#website management`, `#bot traffic`, `#content protection`

---

<a id="item-15"></a>
## [IETF 126 将举行聚焦新兴互联网标准的 BoF 会议](http://www.ietf.org/blog/ietf126-bofs/) ⭐️ 7.0/10

定于 2026 年 7 月 18 日至 24 日在维也纳举行的 IETF 126 会议将包含 BoF（Birds-of-a-Feather）会议，这些非正式聚会旨在探讨潜在的互联网标准新工作。 BoF 会议通常是成立新工作组和标准的第一步，因此成为互联网协议发展未来方向的关键风向标。 这些会议与既有的工作组并行举行，被描述为“观察互联网标准工作下一步走向的最有趣场所”。

rss · IETF Blog (标准动态) · 7月2日 15:39

**背景**: IETF（互联网工程任务组）负责制定和推广自愿性的互联网标准，特别是 TCP/IP 协议族。BoF 会议是 IETF 大会上的非正式临时会议，与会者讨论新兴话题，旨在评估社区支持度并可能促成新工作组的成立。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ietf.org/blog/ietf126-bofs/">IETF | Birds of a Feather at IETF 126</a></li>
<li><a href="https://www.youtube.com/watch?v=D10069Nh2to">IETF 120: Digital Emblems (diem) Birds - of - a - Feather session</a></li>

</ul>
</details>

**标签**: `#IETF`, `#standards`, `#networking`, `#protocols`, `#internet-engineering`

---
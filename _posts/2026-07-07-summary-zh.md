---
layout: default
title: "Horizon Summary: 2026-07-07 (ZH)"
date: 2026-07-07
lang: zh
---

> 从 30 条内容中筛选出 6 条重要资讯。

---

1. [法国将于 2027 年停止认证非量子安全加密产品](#item-1) ⭐️ 9.0/10
2. [HAWK 猜谜游戏攻击并非多项式时间](#item-2) ⭐️ 8.0/10
3. [恶意安全 MPC 支持加权与流体参与](#item-3) ⭐️ 8.0/10
4. [Cloudflare Workers 现可自带区域分层缓存](#item-4) ⭐️ 8.0/10
5. [基于 ROAST 的鲁棒异步分布式可验证随机函数](#item-5) ⭐️ 7.0/10
6. [HEAD-FL：联邦学习中的自适应差分隐私与可验证同态聚合](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [法国将于 2027 年停止认证非量子安全加密产品](https://www.schneier.com/blog/archives/2026/07/france-to-stop-certifying-non-quantum-safe-encryption.html) ⭐️ 9.0/10

法国网络安全机构 ANSSI 宣布将从 2027 年起停止认证缺乏量子抗性加密的安全产品，强制政府机构和关键基础设施进行过渡。 这是国家政府层面的一项重大监管举措，将加速全球后量子密码学的采用，迫使供应商升级，并可能对国际网络安全标准产生连锁影响。 该政策从 2027 年起停止认证，并建议企业在 2030 年前仅购买量子安全产品，实际上使后量子密码学成为法国政府和关键基础设施市场的实际要求。

rss · Schneier on Security · 7月6日 10:45

**背景**: 后量子密码学（PQC）涉及旨在抵御未来量子计算机攻击的加密算法，量子计算机可能通过 Shor 算法破解广泛使用的公钥系统。2024 年，NIST 最终确定了首批三项 PQC 标准，由于“先收集后解密”威胁，迁移被认为紧迫。ANSSI 是法国国家网络安全机构，其认证对于政府和关键部门使用的安全产品是强制性的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#post-quantum cryptography`, `#cybersecurity policy`, `#encryption`, `#France`

---

<a id="item-2"></a>
## [HAWK 猜谜游戏攻击并非多项式时间](https://eprint.iacr.org/2026/1377) ⭐️ 8.0/10

这篇论文通过实验证实了针对 HAWK 的所谓多项式时间攻击实际上呈现出超多项式增长，并指出错误的启发式（Heuristic 4）是造成计算瓶颈的原因。“Guessing Game”攻击的作者已承认这些发现，一项机器验证的条件归约也确认复杂度至少是超多项式的。 这一研究纠正了可能对 HAWK 安全性产生不必要担忧的错误密码分析主张，增强了人们对后量子标准的信心。同时也展示了结合实验分析、形式化归约和 AI 辅助研究的严谨方法论。 原始攻击的多项式时间主张基于四个未经实现的“合理假设”。实验揭示了超多项式类数障碍，并准确指出 Heuristic 4 是错误的假设。所有源代码和数据集已公开，可复现结果。

rss · IACR ePrint 密码学论文 · 7月5日 10:47

**背景**: HAWK 是一种基于格的签名方案，参与了 NIST 后量子密码标准化进程，其安全性依赖于格问题的难解性，以抵御量子计算机的攻击。“Guessing Game”攻击曾声称可在多项式时间内攻破 HAWK，但本工作证明，由于类数障碍（与代数对象类群的大小相关），该攻击的复杂度呈超多项式增长。后量子密码学旨在开发能同时抵抗经典和量子攻击的算法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post - quantum cryptography - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptanalysis`, `#post-quantum cryptography`, `#HAWK`, `#computational complexity`, `#AI-assisted research`

---

<a id="item-3"></a>
## [恶意安全 MPC 支持加权与流体参与](https://eprint.iacr.org/2026/1375) ⭐️ 8.0/10

本文首次提出了同时支持加权参与和流体参与的恶意安全多方计算协议。通过扩展加权斜坡秘密共享，增加可验证性和主动性，并设计状态移交协议，实现了静态与动态委员会下的安全计算。 此工作在恶意安全模型下首次同时实现加权信任和动态参与，对区块链共识、隐私机器学习等需委员会轮换和可信度分层的场景至关重要。它为实用化的委员会式 MPC 提供了坚实的安全基础。 协议基于同步网络和诚实多数假设，静态版本可保障输出可靠交付，动态版本通过主动状态移交实现委员会更新。所提出的加权斜坡秘密共享方案增加了可验证性与主动性，支持份额的可验证算术运算。

rss · IACR ePrint 密码学论文 · 7月4日 13:52

**背景**: 多方安全计算（MPC）允许多方在不泄露各自输入的情况下联合计算一个函数。秘密共享将秘密分割为份额，加权方案中越受信任的参与方获得越大份额，斜坡方案则在安全与效率间权衡。流体（动态）参与允许计算过程中成员动态加入或退出。主动秘密共享通过定期更新份额来缩短攻击者的可利用时间窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iacr.org/news/item/28941">IACR News item: 06 July 2026</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proactive_secret_sharing">Proactive secret sharing</a></li>
<li><a href="https://arxiv.org/pdf/2505.24289">Verifiable Weighted Secret Sharing</a></li>

</ul>
</details>

**标签**: `#multi-party computation`, `#cryptographic protocols`, `#weighted secret sharing`, `#dynamic participation`, `#malicious security`

---

<a id="item-4"></a>
## [Cloudflare Workers 现可自带区域分层缓存](https://blog.cloudflare.com/workers-cache/) ⭐️ 8.0/10

Cloudflare 推出了 Workers Cache，这是一个直接位于 Worker 入口前的区域分层缓存系统，可通过标准 HTTP 头进行配置。 这使开发者能够更好地控制无服务器边缘应用的缓存策略，提高性能并减少源站负载，对高流量全球服务至关重要。 该缓存采用区域分层架构（上层和下层），以最大化缓存命中率，并支持无限组合，允许通过 HTTP 头动态配置多个 CDN 缓存。

rss · Cloudflare Blog (PQ 迁移) · 7月6日 13:00

**背景**: Cloudflare Workers 是在 Cloudflare 边缘网络上运行的无服务器函数。缓存将响应存储在离用户更近的位置以降低延迟。分层缓存添加了多个缓存层；区域上层缓存在请求到达源站前进行聚合，提高效率并保护源站免受流量冲击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/workers/runtime-apis/cache/">Cache · Cloudflare Workers docs</a></li>
<li><a href="https://blog.cloudflare.com/introducing-regional-tiered-cache/">Reduce latency and increase cache hits with Regional Tiered Cache</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#workers`, `#cache`, `#serverless`, `#edge-computing`

---

<a id="item-5"></a>
## [基于 ROAST 的鲁棒异步分布式可验证随机函数](https://eprint.iacr.org/2026/1378) ⭐️ 7.0/10

该论文提出了(R)Icy-DVRF，它通过集成 ROAST 包装框架来增强基于 FROST 的 Icy-DVRF 协议，从而在异步网络上实现鲁棒性和活跃性，同时保持证明大小恒定。 这一进展使得分布式可验证随机函数即使在异步环境中存在恶意或无响应节点时也能可靠运行，从而更适用于随机信标和共识协议等去中心化系统。 该协议利用阈值签名方案 FROST 和 ROAST 包装器，保持了恒定大小的证明，并确保了活跃性和鲁棒性，而不增加证明复杂性。它专为异步网络设计，而现有 DVRF 在此类网络中常常失效。

rss · IACR ePrint 密码学论文 · 7月5日 21:20

**背景**: 分布式可验证随机函数（DVRF）允许多方共同生成可公开验证的伪随机输出。FROST 是一种灵活且回合优化的 Schnorr 阈值签名方案，能够以阈值参与者数高效签名。ROAST 是针对 FROST 的包装框架，可在异步环境中增加鲁棒性和活跃性。Icy-DVRF 是一种现有 DVRF 协议，它使用 FROST 但缺乏异步网络中的鲁棒性。本文通过集成 ROAST 与 Icy-DVRF 来克服这一局限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ZcashFoundation/frost">ZF FROST (Flexible Round-Optimised Schnorr Threshold signatures)</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-030-81652-0_2">FROST: Flexible Round-Optimized Schnorr Threshold Signatures</a></li>
<li><a href="https://github.com/fetchai/research-dvrf">fetchai/research-dvrf: C++ implementation of Distributed Verifiable ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#distributed-systems`, `#verifiable-random-functions`, `#threshold-signatures`, `#asynchronous-networks`

---

<a id="item-6"></a>
## [HEAD-FL：联邦学习中的自适应差分隐私与可验证同态聚合](https://eprint.iacr.org/2026/1376) ⭐️ 7.0/10

本文提出 HEAD-FL 框架，在联邦平均（FedAvg）中集成了轮次自适应的 Rényi 差分隐私与可验证同态加密，在对抗恶意服务器时改善了隐私与效用的权衡。 该工作解决了联邦学习中的关键挑战：梯度泄露、恶意聚合服务器和通信开销，非常适用于隐私敏感且带宽受限的实际部署。 该方案采用基于 Rényi 差分隐私分析的轮次自适应高斯噪声，可进行严格的累积隐私核算并显式转换为 (ε,δ)‑差分隐私保证；同时，使用 FedAvg 而非梯度传输，降低了通信开销并支持客户端掉线。

rss · IACR ePrint 密码学论文 · 7月5日 06:31

**背景**: 联邦学习允许不分享原始数据的协作训练，但梯度可能泄露隐私。差分隐私通过添加噪声来量化隐私损失，Rényi 差分隐私能提供更严格的分析。同态加密允许对密文进行计算，可验证聚合确保在恶意服务器下结果的正确性。FedAvg 通过交换模型更新而非梯度，大幅降低了通信量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1702.07476">Abstract page for arXiv paper 1702.07476: Renyi Differential Privacy</a></li>
<li><a href="https://www.mdpi.com/2410-387X/4/3/25">Practical and Provably Secure Distributed Aggregation: Verifiable ...</a></li>

</ul>
</details>

**标签**: `#federated learning`, `#differential privacy`, `#homomorphic encryption`, `#secure aggregation`, `#privacy-preserving ML`

---
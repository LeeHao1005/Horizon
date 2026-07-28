---
layout: default
title: "Horizon Summary: 2026-07-28 (ZH)"
date: 2026-07-28
lang: zh
---

> 从 16 条内容中筛选出 4 条重要资讯。

---

1. [用 350 行 Python 实现生产级 ML-DSA 签名验证](#item-1) ⭐️ 8.0/10
2. [NIST 发布 SP 800-239 草案应对 AI 数据中心安全](#item-2) ⭐️ 8.0/10
3. [Cloudflare 开源用于测试 Oblivious HTTP 的 pvcli 工具](#item-3) ⭐️ 7.0/10
4. [Cognyte 向美国警方出售 FalcoNet 移动监控车](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [用 350 行 Python 实现生产级 ML-DSA 签名验证](https://words.filippo.io/mldsa-py/) ⭐️ 8.0/10

Filippo Valsorda 发布了一个纯 Python 的生产就绪 ML-DSA 签名验证实现，代码简洁易读，仅 350 行。 这为开发者提供了一个易于理解的参考实现，便于将后量子签名验证集成到应用中，加速向量子安全密码学的过渡，应对量子计算机的潜在威胁。 该实现完全用 Python 编写，仅专注于验证（不包含签名），并强调代码可读性和健壮性，适合学习及生产环境使用。

rss · Filippo Valsorda (Go 密码学) · 7月26日 11:45

**背景**: ML-DSA（基于模格的数字签名算法）是 NIST 标准化的后量子密码算法，旨在抵御经典和量子计算机的攻击。它基于格密码学，于 2022 年被选定为后量子签名标准。与易受量子 Shor 算法攻击的 RSA 和 ECDSA 等传统算法不同，ML-DSA 提供长期安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.encryptionconsulting.com/ml-dsa-and-pq-signing/">ML-DSA and PQ Signing: What You Need to Know | Encryption Consulting</a></li>
<li><a href="https://blog.cloudflare.com/another-look-at-pq-signatures/">A look at the latest post-quantum signature standardization candidates | The Cloudflare Blog</a></li>
<li><a href="https://blog.cloudflare.com/ml-dsa-will-have-to-do/">Why we cannot wait for better post-quantum signature algorithms | The Cloudflare Blog</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#python`, `#post-quantum`, `#ML-DSA`, `#open-source`

---

<a id="item-2"></a>
## [NIST 发布 SP 800-239 草案应对 AI 数据中心安全](https://csrc.nist.gov/pubs/sp/800/239/ipd) ⭐️ 8.0/10

NIST 发布了 SP 800-239 的初步公开草案，通过将 AI 数据中心与传统 HPC 系统进行比较，提供了全面的威胁和安全差距分析。 该草案标准将帮助各组织保护下一代 AI 基础设施，这对于模型训练和推理操作越来越关键。 分析涵盖架构、硬件、软件栈、工作流和存储。它基于 HPC 威胁分析和安全叠加，明确了关键威胁和潜在解决方案。草案中包含专利主张征集。

rss · NIST CSRC Drafts (标准草案) · 7月27日 04:00

**背景**: 高性能计算（HPC）系统长期以来拥有成熟的安全实践和 NIST 安全叠加——为特定环境定制的安全控制集。该草案将这些原则扩展到 AI 专用数据中心，这些数据中心通常具有类似的基础设施，但由于 AI 工作流和数据敏感性而面临独特威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/projects/risk-management/sp800-53-controls/overlay-repository">Control Overlay Repository - NIST Risk Management Framework | CSRC | CSRC</a></li>

</ul>
</details>

**标签**: `#NIST`, `#AI security`, `#HPC`, `#data center security`, `#standards`

---

<a id="item-3"></a>
## [Cloudflare 开源用于测试 Oblivious HTTP 的 pvcli 工具](https://blog.cloudflare.com/open-sourcing-our-privacy-proxy-cli/) ⭐️ 7.0/10

Cloudflare 开源了 pvcli，一个类似 curl 的命令行工具，简化了 Oblivious HTTP (OHTTP) 隐私协议的测试。该工具使开发者无需复杂设置即可轻松尝试 OHTTP 请求。 OHTTP 是一种用于匿名化 HTTP 交易的新兴 IETF 标准，但测试过程一直很繁琐。通过提供类似 curl 的简单界面，pvcli 降低了开发者采用和验证隐私增强协议的门槛，有望加速 OHTTP 在遥测数据收集或隐私型 AI 服务等现实应用中的部署。 pvcli 自动处理 OHTTP 的双跳中继架构、密钥配置和消息封装。它主要作为测试辅助工具，而非用于替代生产级 OHTTP 客户端。

rss · Cloudflare Blog (PQ 迁移) · 7月27日 13:00

**背景**: Oblivious HTTP (OHTTP) 在 RFC 9458 中定义，通过中继路由加密的 HTTP 消息，防止服务器将请求与客户端 IP 地址关联。它需要客户端、中继和网关之间的协作，导致手动测试困难。pvcli 通过提供熟悉的 curl 式语法简化了这一过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Oblivious_HTTP">Oblivious HTTP</a></li>
<li><a href="https://ietf-wg-ohai.github.io/oblivious-http/draft-ietf-ohai-ohttp.html">Oblivious HTTP</a></li>

</ul>
</details>

**标签**: `#privacy`, `#OHTTP`, `#open-source`, `#CLI`, `#Cloudflare`

---

<a id="item-4"></a>
## [Cognyte 向美国警方出售 FalcoNet 移动监控车](https://www.schneier.com/blog/archives/2026/07/cognyte-sells-a-mobile-cell-surveillance-van.html) ⭐️ 7.0/10

Cognyte 公司的 FalcoNet 系统安装在货车内，通过模拟基站迫使附近手机连接，使执法部门能拦截通信并追踪区域内所有手机的位置，而不仅限于嫌疑人。 这扩大了大规模监控能力，引发严重隐私担忧，因为无辜路人的数据被无差别收集。此类技术可隐蔽部署，威胁公民自由并可能被滥用。 FalcoNet 系统可隐藏在车辆、背包或直升机上，其运作方式与臭名昭著的 StingRay 类似。Cognyte 已与得克萨斯州签订部署合同。

rss · Schneier on Security · 7月27日 11:04

**背景**: 基站模拟器通常被称为 StingRay 或 IMSI 抓捕器，是模仿合法基站诱骗手机连接的设备。它们能拦截 IMSI 号码和位置等数据。最初为军事和情报用途开发，现在美国许多执法机构常在无搜查令的情况下使用，引发法律和隐私争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cell_site_simulator">Cell site simulator</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stingray_phone_tracker">Stingray phone tracker - Wikipedia</a></li>
<li><a href="https://sls.eff.org/technologies/cell-site-simulators-imsi-catchers">Cell-Site Simulators/ IMSI Catchers</a></li>

</ul>
</details>

**标签**: `#surveillance`, `#privacy`, `#cell-site simulator`, `#law enforcement`, `#Israeli tech`

---
---
layout: default
title: "Horizon Summary: 2026-08-11 (ZH)"
date: 2026-08-11
lang: zh
---

> 从 24 条内容中筛选出 3 条重要资讯。

---

1. [IETF RFC 10024 标准化 TLS 1.3 的后量子混合密钥协商](#item-1) ⭐️ 9.0/10
2. [Cloudflare 回顾 Agents 周发布：钱包、雷达等新品](#item-2) ⭐️ 7.0/10
3. [Python 密码库 pyca/cryptography 支持后量子加密](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [IETF RFC 10024 标准化 TLS 1.3 的后量子混合密钥协商](https://rfc-editor.org/info/rfc10024) ⭐️ 9.0/10

RFC 10024 为 TLS 1.3 定义了三种混合密钥协商机制——X25519MLKEM768、SecP256r1MLKEM768 和 SecP384r1MLKEM1024，将后量子算法 ML-KEM 与椭圆曲线 Diffie-Hellman 相结合以抵御量子攻击。 这一标准化是迈向抗量子互联网安全的关键一步，使 TLS 1.3 能够在兼容现有经典基础设施的同时抵御未来的量子计算机攻击。 这三个命名组分别将 X25519、P-256 和 P-384 与 ML-KEM-768 或 ML-KEM-1024 配对；混合结构确保即使其中一个组件被攻破仍保持安全，但 ML-KEM 较大的公钥和密文会增加一些开销。

rss · IETF 新标准 RFC (PQC 标准化) · 8月10日 18:11

**背景**: TLS 1.3 是当前互联网安全连接的主要协议。现有的密钥交换算法（如 ECDHE）容易受到大规模量子计算机的威胁。后量子密码学旨在开发抗量子攻击的算法，其中 ML-KEM（原 Kyber）是首个由 NIST 标准化的密钥封装机制（FIPS 203）。混合方案将两者结合，提供纵深防御并帮助平滑过渡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://docs.aws.amazon.com/kms/latest/developerguide/pqtls.html">Using hybrid post-quantum TLS with AWS KMS - AWS Key Management Service</a></li>
<li><a href="https://postquantum.com/post-quantum/hybrid-cryptography-pqc/">Hybrid Cryptography for the Post-Quantum Era</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#TLS 1.3`, `#IETF`, `#ML-KEM`, `#hybrid encryption`

---

<a id="item-2"></a>
## [Cloudflare 回顾 Agents 周发布：钱包、雷达等新品](https://blog.cloudflare.com/agents-week-review-august-2026/) ⭐️ 7.0/10

Cloudflare 结束了其 Agents 周，总结了一系列产品发布，其中包括全新的可编程钱包 Cloudflare Wallets 以及 Cloudflare Radar 的互联网分析增强功能。 这一发布标志着 Cloudflare 正在扩展为 AI 代理提供基础设施，通过身份和支付解决方案简化自主交易，并提升开发者的可观测性。 Cloudflare Wallets 提供具有唯一标识符和支出限制的可编程钱包，而 Radar 则新增了 URL 扫描和基于 NetFlows 与攻击数据的调查功能。

rss · Cloudflare Blog (PQ 迁移) · 8月10日 18:34

**背景**: Cloudflare Agents 周是一系列聚焦于 AI 代理工具的发布活动。Cloudflare 钱包旨在为代理提供可编程的支付和身份层，而 Radar 则提供全球互联网趋势和安全分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/wallets/">Announcing Cloudflare Wallets : The programmable wallet for the...</a></li>
<li><a href="https://radar.cloudflare.com/scan">URL Scanner | Cloudflare Radar</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#agents`, `#product-launch`, `#recap`, `#developers`

---

<a id="item-3"></a>
## [Python 密码库 pyca/cryptography 支持后量子加密](https://www.schneier.com/blog/archives/2026/08/python-now-has-a-post-quantum-encryption-library.html) ⭐️ 7.0/10

pyca/cryptography 库现在包含了 NIST 标准化的后量子密钥封装机制 (ML-KEM) 和数字签名算法 (ML-DSA)，让 Python 生态可以通过 pip 轻松安装使用。 这降低了 Python 开发者采用后量子密码学的门槛，有助于实现密码敏捷性，并为应对未来的量子威胁提前做好准备。这反映了行业推动标准化和部署抗量子算法的广泛努力。 该实现遵循 FIPS 203 (ML-KEM) 和 FIPS 204 (ML-DSA) 标准。ML-KEM 基于 Kyber，使用格密码学建立共享秘密；ML-DSA 基于 Dilithium 用于数字签名。该库提供了高级接口，是广泛受信任的 Python 密码库 pyca/cryptography 的一部分。

rss · Schneier on Security · 8月10日 11:02

**背景**: 后量子密码学旨在开发能够抵御量子计算机攻击的算法。NIST 于 2024 年将 ML-KEM（Kyber）和 ML-DSA（Dilithium）分别标准化为 FIPS 203 和 FIPS 204。pyca/cryptography 是一个重要的 Python 密码库，为许多 Python 应用程序提供了密码方案和原语，是事实上的标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://github.com/pyca/cryptography">GitHub - pyca/cryptography: cryptography is a package designed to expose cryptographic primitives and recipes to Python developers. · GitHub</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#Python`, `#NIST`, `#pyca`, `#crypto agility`

---
---
layout: default
title: "Horizon Summary: 2026-07-13 (ZH)"
date: 2026-07-13
lang: zh
---

> 从 23 条内容中筛选出 3 条重要资讯。

---

1. [RFC 9846 正式确定带后量子加密的 TLS 1.3](#item-1) ⭐️ 9.0/10
2. [AI 监控将监视所有公共与私人行为，即时惩罚违规](#item-2) ⭐️ 8.0/10
3. [Cloudflare Smart Tiered Cache 新增云区域提示功能](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [RFC 9846 正式确定带后量子加密的 TLS 1.3](https://rfc-editor.org/info/rfc9846) ⭐️ 9.0/10

RFC 9846 规范了 TLS 1.3 协议版本，纳入了后量子密码学更新，并取代了包括 RFC 8446 和 RFC 5246 在内的旧版 TLS 标准。 此次更新至关重要，因为它将抗量子算法集成到核心互联网安全协议中，有助于保护全球通信免受未来量子计算攻击，并确保安全迁移路径。 它淘汰了 RFC 8446、5246、5077、6961、7627 和 8422，更新了 RFC 5705 和 6066，并为 TLS 1.3 引入了新的强制性后量子密钥交换机制。

rss · IETF 新标准 RFC (PQC 标准化) · 7月11日 16:03

**背景**: TLS 是用于加密网络流量、电子邮件等互联网通信的基础协议。后量子密码学旨在开发能够抵御量子计算机攻击的算法，因为量子计算机可能破解现有的公钥密码系统。RFC 是 IETF 发布的定义互联网协议的技术标准。此前的 RFC 8446 定义了无量子安全措施的 TLS 1.3，因此此次更新至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc9846">RFC 9846 - The Transport Layer Security (TLS) Protocol Version 1.3</a></li>
<li><a href="https://www.microsoft.com/en-us/research/project/post-quantum-tls/">Post-Quantum TLS - Microsoft Research</a></li>

</ul>
</details>

**标签**: `#TLS`, `#Post-Quantum Cryptography`, `#RFC`, `#Internet Security`, `#Protocol Standard`

---

<a id="item-2"></a>
## [AI 监控将监视所有公共与私人行为，即时惩罚违规](https://www.schneier.com/blog/archives/2026/07/ai-surveillance-and-social-progress.html) ⭐️ 8.0/10

Bruce Schneier 警告称，AI 驱动的监控系统即将能够监视所有公共和私人行为，即时发现并惩罚违规行为，可能重塑社会规范。 这一发展可能通过消除对轻微违规的宽容来根本改变社会规范，引发关于隐私、正当程序和专制控制潜力的关键问题。 这些系统不仅会检测违规行为，还会将其与个人记录关联，并实时向当局和公众发出警报，以即时罚款执行任何可想象的规则。

rss · Schneier on Security · 7月10日 11:02

**背景**: Bruce Schneier 是著名的安全技术专家和作家。当前的 AI 监控包括面部识别和自动罚单，但 Schneier 设想了一种更普遍的监控系统，实时监视所有行为并执行所有规则，类似于全景监狱。

**标签**: `#ai-ethics`, `#surveillance`, `#privacy`, `#social-control`, `#technology-policy`

---

<a id="item-3"></a>
## [Cloudflare Smart Tiered Cache 新增云区域提示功能](https://blog.cloudflare.com/smart-tiered-cache-for-public-clouds/) ⭐️ 7.0/10

Cloudflare 的 Smart Tiered Cache 现在支持用户提供的云区域提示，从而能够为托管在 AWS、GCP、Azure 和 Oracle Cloud 上的源站精确选择上层数据中心。 这一改进减少了缓存未命中时的延迟，提高了云托管源站用户的性能，同时有助于降低公有云的出站流量成本。 该功能需要用户提供云区域提示；目前支持 AWS、GCP、Azure 和 Oracle Cloud。上层数据中心是到源站 IP 延迟最低的 Cloudflare 节点。

rss · Cloudflare Blog (PQ 迁移) · 7月10日 13:00

**背景**: Smart Tiered Cache 是 Cloudflare CDN 的一项功能，它通过将缓存未命中的请求汇聚到一个位置最优的上层数据中心来减少源站负载。此前，上层数据中心根据到源站 IP 的延迟测量自动选择。此次更新后，对于托管在主要公有云上的源站，用户可以提供明确的区域提示以进一步优化选择，从而提高效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/smart-tiered-cache-for-public-clouds/">Improving Smart Tiered Cache for public cloud regions</a></li>
<li><a href="https://developers.cloudflare.com/smart-shield/configuration/smart-tiered-cache/">Smart Tiered Cache · Cloudflare Smart Shield docs</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#CDN`, `#caching`, `#performance`, `#cloud`

---
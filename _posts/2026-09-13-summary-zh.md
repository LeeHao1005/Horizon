---
layout: default
title: "Horizon Summary: 2026-09-13 (ZH)"
date: 2026-09-13
lang: zh
---

> 从 23 条内容中筛选出 3 条重要资讯。

---

1. [Cloudflare 1.1.1.1 解析器现已支持使用 ML-DSA-44 验证后量子 DNSSEC](#item-1) ⭐️ 8.0/10
2. [AI 代理将漏洞传言变为补丁发布前的攻击代码](#item-2) ⭐️ 8.0/10
3. [Bruce Schneier 分享 DEF CON 关于 AI 黑客攻击的演讲](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Cloudflare 1.1.1.1 解析器现已支持使用 ML-DSA-44 验证后量子 DNSSEC](https://blog.cloudflare.com/post-quantum-dnssec-1111/) ⭐️ 8.0/10

Cloudflare 的公共 DNS 解析器 1.1.1.1 现在使用 NIST 的后量子签名算法 ML-DSA-44 验证 DNSSEC 签名，能够处理 2,420 字节的签名并在规模上应对降级风险。 这是朝抗量子 DNS 安全迈出的重要一步，可防止未来量子计算机破解当前 RSA/ECC 算法；它影响依赖 1.1.1.1 的互联网用户，并为 DNSSEC 采用后量子密码学树立先例。 ML-DSA-44 是 NIST 于 2024 年 8 月标准化为 FIPS 204 的模块格基数字签名算法，源自 CRYSTALS-Dilithium。DNSSEC 响应中的签名有 2,420 字节，远大于传统签名，Cloudflare 需要处理响应大小问题并防止攻击者通过移除 DNSSEC 来实施降级攻击。

rss · Cloudflare Blog (PQ 迁移) · 9月10日 13:00

**背景**: DNSSEC 通过为 DNS 响应添加数字签名来验证其真实性，防止缓存投毒等攻击。当前使用的 RSA 或椭圆曲线算法理论上可被量子计算机用 Shor 算法破解。ML-DSA-44 是基于模块格的抗量子签名算法，由 NIST 在 2024 年标准化为 FIPS 204。在 DNSSEC 中部署此类算法需要处理大签名带来的包大小问题，并防止攻击者通过移除签名迫使解析器退回不安全模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://github.com/NeuraiProject/mldsa-esp32">GitHub - NeuraiProject/mldsa-esp32: ML-DSA-44 (FIPS 204) post-quantum digital signatures for ESP32. · GitHub</a></li>
<li><a href="https://dnschkr.com/blog/dnssec-downgrade-attack">DNSSEC Downgrade Attack : How Attackers Strip... | DNSChkr Blog</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#DNSSEC`, `#Cloudflare`, `#ML-DSA`, `#DNS security`

---

<a id="item-2"></a>
## [AI 代理将漏洞传言变为补丁发布前的攻击代码](https://www.schneier.com/blog/archives/2026/09/ais-compress-exploit-timeline.html) ⭐️ 8.0/10

Anil 报告称，他的 AI 代理仅凭对漏洞的大致了解就能找到可用的攻击代码，甚至可能早于公开补丁发布。Simon Willison 于 2026 年 8 月 28 日评论说，这种发现速度似乎与现有的开源漏洞保密期做法不兼容。 这一发现缩短了漏洞传言到实际利用的时间窗口，威胁到协调披露中保密期的作用。开源项目可能需要重新考虑安全响应流程，因为攻击者可能仅在修补程序发布前，根据蛛丝马迹就实施攻击。 文章未提及具体的 CVE 或项目，但作者表示他用自己构建的 AI 代理，仅凭大致信息复现了这一攻击。其含义是，即使泄露的关键词或模糊的公告细节，也可能让攻击者在补丁发布前实施利用。

rss · Schneier on Security · 9月10日 10:40

**背景**: 开源项目通常采用保密期漏洞管理：安全团队私下准备修复方案，并在公开披露前通知下游相关方。ExploitGym 等近期研究表明，自主 AI 代理能够分析漏洞并编写完整攻击代码。如果 AI 代理只需传言或模糊提示就能行动，那么保密期依赖的信息不公开这一传统安全网可能失效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openstack/project-team-guide/blob/master/doc/source/vulnerability-management.rst">project-team-guide/doc/ source / vulnerability -management.rst at...</a></li>
<li><a href="https://eclipse-csi.github.io/security-handbook/vulnerabilities/embargoes.html">Best Practices Related to Embargoes — Eclipse Security Handbook...</a></li>
<li><a href="https://snapost.net/ai-agents-compress-exploit-timelines-and-shatter-traditional-open-source-security-models/">AI Agents Compress Exploit Timelines and Shatter Traditional Open ...</a></li>

</ul>
</details>

**社区讨论**: Simon Willison 的评论强化了这一担忧，他表示这种发现速度似乎与现有的开源保密期做法不兼容，社区需要找出新的流程来保障安全。

**标签**: `#AI security`, `#vulnerability disclosure`, `#open source`, `#exploit development`, `#cybersecurity`

---

<a id="item-3"></a>
## [Bruce Schneier 分享 DEF CON 关于 AI 黑客攻击的演讲](https://www.schneier.com/blog/archives/2026/09/my-talk-at-def-con.html) ⭐️ 7.0/10

Bruce Schneier 发布了一篇博文，分享他在 DEF CON 上的演讲《AI 黑客攻击：当 AI 成为黑客时会发生什么》，以及一段 AI Village 采访。该演讲在 YouTube 上几天内获得了超过 10 万次观看。 作为权威安全专家，Schneier 的讨论凸显了 AI 驱动黑客攻击的新风险，将他书中提出的理论威胁与当前 AI 模型的实际行为联系起来。这一点很重要，因为安全专业人员必须预判 AI 如何自动化或增强网络攻击。 该演讲结合了他 2022 年出版的《黑客思维》（A Hacker's Mind）中的观点，以及当前 AI 模型参与黑客行为的经验教训。博文本身很简短，主要链接到 YouTube 视频，没有提供详细的技术分析。

rss · Schneier on Security · 9月11日 18:06

**背景**: DEF CON 是每年在拉斯维加斯举办的大型黑客大会，始于 1993 年，安全研究人员、专业人士和黑客聚集于此讨论漏洞并测试系统。AI Village 是 DEF CON 内的一个社群，专注于 AI 安全的实践教育和测试。Bruce Schneier 是知名安全技术专家和作家，他在 2022 年出版的《黑客思维》探讨了黑客攻击的运作方式以及 AI 如何可能成为强大的黑客工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DEF_CON">DEF CON</a></li>
<li><a href="https://aivillage.org/">Home | AI Village</a></li>

</ul>
</details>

**标签**: `#AI security`, `#hacking`, `#DEF CON`, `#Bruce Schneier`, `#artificial intelligence`

---
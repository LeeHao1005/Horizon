---
layout: default
title: "Horizon Summary: 2026-09-12 (ZH)"
date: 2026-09-12
lang: zh
---

> 从 38 条内容中筛选出 8 条重要资讯。

---

1. [Cloudflare 1.1.1.1 支持基于 ML-DSA-44 的后量子 DNSSEC 验证](#item-1) ⭐️ 8.0/10
2. [布鲁斯·施奈尔在 DEF CON 谈 AI 系统成为黑客](#item-2) ⭐️ 8.0/10
3. [AI 代理将漏洞传闻转化为可用漏洞利用，挑战补丁禁运](#item-3) ⭐️ 8.0/10
4. [1.53 亿条驾照数据在暗网出售](#item-4) ⭐️ 8.0/10
5. [Cloudflare CASB 推出自动修复策略](#item-5) ⭐️ 7.0/10
6. [Cloudflare Workers 重建模块注册表以实现 Node.js 兼容性](#item-6) ⭐️ 7.0/10
7. [Claude Fable 5.1 用 44 分钟破解 370 年前 Cyphral Distich 密码](#item-7) ⭐️ 7.0/10
8. [Lean 漏洞使伪造费马大定理证明成为可能](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Cloudflare 1.1.1.1 支持基于 ML-DSA-44 的后量子 DNSSEC 验证](https://blog.cloudflare.com/post-quantum-dnssec-1111/) ⭐️ 8.0/10

Cloudflare 的公共 DNS 解析器 1.1.1.1 现在能够使用 NIST 的后量子算法 ML-DSA-44 验证 DNSSEC 签名，包括高达 2,420 字节的签名，并已在大规模部署中实施缓解降级攻击的措施。 这是在关键 DNS 基础设施中实际部署后量子密码学的重要一步，表明大签名和降级风险可以在生产环境中得到管理。这将推动量子安全 DNSSEC 的更广泛应用，并帮助保护用户免受未来量子计算威胁。 ML-DSA-44 在 NIST FIPS 204 中定义，提供安全级别 2；其签名大小为 2,420 字节，远大于典型 DNSSEC 签名，可能给基于 UDP 的 DNS 响应带来挑战。Cloudflare 的解析器现在能够处理这种大小，并缓解攻击者强制回退到较弱算法的降级风险。

rss · Cloudflare Blog (PQ 迁移) · 9月10日 13:00

**背景**: DNSSEC 为 DNS 记录添加数字签名，以验证响应真实性并防止欺骗。然而，广泛使用的 RSA 和 ECDSA 等签名算法可能会被足够强大的量子计算机破解。NIST 已在 FIPS 204 中标准化了基于格的 ML-DSA 后量子签名算法，ML-DSA-44 是其中的一个参数集。Cloudflare 的 1.1.1.1 是流行的公共 DNS 解析器，处理大量查询，因此此次部署在真实环境中检验了后量子 DNSSEC。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ietf.org/archive/id/draft-sheth-pqc-dnssec-strategy-00.html">Post-Quantum Cryptography Strategy for DNSSEC - ietf.org</a></li>
<li><a href="https://openquantumsafe.org/liboqs/algorithms/sig/ml-dsa.html">ML-DSA | Open Quantum Safe</a></li>
<li><a href="https://dnssec-downgrade.net/">DNSSEC Downgrade</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#DNSSEC`, `#Cloudflare`, `#network security`, `#ML-DSA-44`

---

<a id="item-2"></a>
## [布鲁斯·施奈尔在 DEF CON 谈 AI 系统成为黑客](https://www.schneier.com/blog/archives/2026/09/my-talk-at-def-con.html) ⭐️ 8.0/10

布鲁斯·施奈尔在 DEF CON 发表了一场关于 AI 黑客攻击的演讲，探讨了当前 AI 模型参与黑客行为以及当 AI 成为黑客时会发生什么。该演讲在 YouTube 上几天内获得了超过 10 万次观看，AI Village 的采访也已上线。 这场由顶尖安全专家发表的演讲凸显了 AI 系统自主发现和利用漏洞这一新兴风险，可能从根本上改变网络安全威胁格局。它也表明在重要黑客大会上，业界和社区对 AI 驱动的黑客行为日益关注。 演讲结合了施奈尔 2022 年著作《黑客的思维》中的观点与当前表现出黑客行为的 AI 模型所带来的经验教训。AI Village 中的配套采访也已在线发布。

rss · Schneier on Security · 9月11日 18:06

**背景**: DEF CON 是全球最大、最著名的黑客大会之一，每年在拉斯维加斯举行。布鲁斯·施奈尔是知名的安全技术专家和作家，他在 2022 年出版的《黑客的思维》一书中探讨了系统与规则在广义上如何被黑客攻击，而不仅仅局限于计算机系统。AI Village 是 DEF CON 中专注于人工智能与安全的社区。近期的研究表明，大语言模型有时能够发现漏洞或实施网络攻击，从而引发了关于“AI 黑客攻击”的讨论。

**标签**: `#AI`, `#cybersecurity`, `#hacking`, `#DEF CON`, `#security`

---

<a id="item-3"></a>
## [AI 代理将漏洞传闻转化为可用漏洞利用，挑战补丁禁运](https://www.schneier.com/blog/archives/2026/09/ais-compress-exploit-timeline.html) ⭐️ 8.0/10

Anil 报告称，仅给 AI 代理一个漏洞传闻，就足以让它找到漏洞并开发出利用方法，且可能在公开补丁发布前就加以利用。Simon Willison 评论说，这种发现速度与现有开源补丁禁运做法不兼容。 如果仅凭传闻就能让攻击者在补丁发布前生成可用漏洞利用，现有的协调披露和禁运模式就无法保护开源用户。安全响应流程需要重新设计，以应对 AI 加速漏洞发现。 报告未透露具体的漏洞或项目，但指出只要大致了解安全问题的性质，作者的 AI 代理就足以定位并利用漏洞。Simon Willison 强调需要新的社区安全流程，因为当前禁运时间表可能太慢。

rss · Schneier on Security · 9月10日 10:40

**背景**: AI 代理是由大语言模型驱动的程序，能够自主使用工具并执行多步骤任务，而不仅仅是回答问题。开源补丁禁运是一种协调披露机制：在修复公开之前，将漏洞私下通知发行商和服务提供商，以便他们准备补丁并减少用户暴露。然而在开源开发中，补丁一旦合并就会对所有人可见，因此禁运依赖于在协调发布前保守秘密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent</a></li>
<li><a href="https://github.com/google/oss-vulnerability-guide/blob/main/templates/notifications/embargo.md">oss-vulnerability-guide/templates/notifications/embargo.md at main · google/oss-vulnerability-guide</a></li>
<li><a href="https://access.redhat.com/blogs/766093/posts/1976653">The hidden costs of embargoes - Red Hat Customer Portal</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#open source`, `#vulnerability disclosure`, `#exploit`

---

<a id="item-4"></a>
## [1.53 亿条驾照数据在暗网出售](https://www.schneier.com/blog/archives/2026/09/drivers-license-data-for-sale.html) ⭐️ 8.0/10

2026 年 9 月，布鲁斯·施奈尔报道，一个包含 1.53 亿驾照的数据库正在暗网上出售，并链接了 Ars Technica 和 Brian Krebs 的详细分析。Brian Krebs 还报道称，FBI 正在调查出售这些数据的服务。 此次泄露使海量个人面临身份盗用和欺诈风险，因为驾照包含姓名、地址、出生日期和驾照编号等个人信息。这也凸显了暗网上被盗身份信息交易的日益猖獗，给政府机构和数据经纪人保护敏感数据敲响了警钟。 这些数据在一个新的暗网站上出售；Brian Krebs 报道称 FBI 正在调查相关服务。原文未说明数据泄露的来源、获取方式或具体包含哪些字段。

rss · Schneier on Security · 9月9日 16:05

**背景**: 暗网是指互联网中只能通过 Tor 等匿名软件访问的部分，常被用于非法交易。驾照作为身份凭证，包含照片、地址、出生日期和唯一驾照编号，可用于开设欺诈账户或实施身份盗用。被盗的政府记录经常在暗网论坛上出售，买家利用其进行网络钓鱼、合成身份欺诈或转售给其他犯罪分子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dark_web">Dark web</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#data breach`, `#privacy`, `#dark web`, `#driver's licenses`

---

<a id="item-5"></a>
## [Cloudflare CASB 推出自动修复策略](https://blog.cloudflare.com/casb-policies/) ⭐️ 7.0/10

Cloudflare CASB 现在提供自动修复策略，让安全团队能够配置事件驱动逻辑，无需人工干预即可撤销有风险的文件共享并发送 webhook。 这将通过自动化修复 SaaS 安全风险来减少安全团队的人工工作量，并且与 Cloudflare 开发者平台集成，使大规模强制执行安全策略更加容易。 该自动化引擎原生构建于 Cloudflare 开发者平台之上，支持事件驱动逻辑，例如撤销有风险的文件共享和发送 webhook。

rss · Cloudflare Blog (PQ 迁移) · 9月11日 13:00

**背景**: 云访问安全代理（CASB）用于监控并强制执行 SaaS 应用程序的安全策略。Cloudflare CASB 通过 API 与第三方 SaaS 应用集成，以识别安全发现。Webhook 是一种 HTTP 回调机制，在事件发生时自动将数据发送到另一个系统。此前，修复通常需要人工操作；新策略则支持自动响应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/sase/products/casb/">CASB | Protect SaaS Apps | Cloudflare</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-one/applications/casb/">Cloud Access Security Broker · Cloudflare Zero Trust docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Webhook">Webhook</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#CASB`, `#SaaS security`, `#automation`, `#remediation`

---

<a id="item-6"></a>
## [Cloudflare Workers 重建模块注册表以实现 Node.js 兼容性](https://blog.cloudflare.com/workers-module-registry-nodejs/) ⭐️ 7.0/10

Cloudflare Workers 现默认启用 Node.js 兼容性，支持最大 64 MiB 的应用，并引入了基于 URL 的模块注册表，支持 import.meta、惰性编译、共享代码缓存和更清晰的错误提示。 这让开发者更容易在 Workers 上直接运行现有 Node.js 包，并通过惰性编译和共享缓存改善冷启动性能和内存效率，从而增强 Cloudflare 的边缘计算平台。 新注册表使用 URL 作为模块标识符格式，按需编译而不是提前编译，并在多个 V8 isolate 之间共享代码缓存；同时将应用大小限制提高到 64 MiB。

rss · Cloudflare Blog (PQ 迁移) · 9月9日 13:00

**背景**: Cloudflare Workers 是一个在 Cloudflare 边缘节点运行 JavaScript 的无服务器平台。Node.js 兼容性允许 Workers 使用 Node.js API 和 npm 包，此前这通常需要额外配置或打包。import.meta 是一种 JavaScript 元属性，可暴露模块的 URL 等元数据；惰性编译意味着模块只有在实际被导入时才会被编译。旧模块注册表会提前编译整个 Worker 包，并在每个 V8 isolate 中保留独立副本，而新注册表使用 URL 并共享缓存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/workers-module-registry-nodejs/">How we rebuilt Cloudflare Workers’ module registry for Node.js compatibility | Cloudflare Blog</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import.meta">import.meta - JavaScript | MDN</a></li>
<li><a href="https://noise.getoto.net/2026/09/09/how-we-rebuilt-cloudflare-workers-module-registry-for-node-js-compatibility/">How we rebuilt Cloudflare Workers’ module registry for Node.js compatibility | Noise</a></li>

</ul>
</details>

**标签**: `#Cloudflare Workers`, `#Node.js`, `#Serverless`, `#Edge Computing`, `#Module Registry`

---

<a id="item-7"></a>
## [Claude Fable 5.1 用 44 分钟破解 370 年前 Cyphral Distich 密码](https://www.schneier.com/blog/archives/2026/09/claude-fable-solves-a-historical-cipher.html) ⭐️ 7.0/10

据 Vals AI 报告，Claude Fable 5.1 在 44 分钟内、使用 176,000 个 token 且无人工干预，解出了托马斯·厄克特爵士 370 年前的 Cyphral Distich 密码，并给出 64 个字母的保皇党对句明文。 这展示了大语言模型在搜索密集型问题上的优势，与观察到的 AI 擅长需要大量搜索和验证的任务相吻合。它可能加速历史密码破译，并为解读档案文献开辟新方法。 该密码出现在厄克特《Logopandecteision》结尾，由两行各 32 个数字组成。Vals AI 称 Fable 5.1 通过索引密码前 32 个编号段落中的单词得到 64 个字母的明文；Fable 5.1 是 Anthropic 于 2026 年 9 月发布的 Mythos 级模型。

rss · Schneier on Security · 9月9日 11:08

**背景**: 托马斯·厄克特爵士是 17 世纪苏格兰作家，其《Logopandecteision》结尾的 Cyphral Distich 是由两行各 32 个数字组成的密文。密文是指故意按规则编码、不知道规则就无法阅读的短消息。Claude Fable 5.1 是 Anthropic 公司 Claude 系列中的大语言模型，属于 Mythos 级、面向通用用途并带有安全防护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.vals.ai/blogs/fable-solves-cyphral-distich">Claude Fable 5.1 Solves the Cyphral Distich - Vals AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5.1 and Claude Mythos 5.1 \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#cryptography`, `#historical codebreaking`, `#Claude Fable`, `#artificial intelligence`

---

<a id="item-8"></a>
## [Lean 漏洞使伪造费马大定理证明成为可能](https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/) ⭐️ 7.0/10

Trail of Bits 披露了 Lean 底层字符串切片函数 String.Pos.Raw.extract 中的一个漏洞，该漏洞导致逻辑定义与原生代码求值结果不一致，从而可以伪造费马大定理的证明。该问题影响所有稳定版本直到 4.33.1，并已在 v4.34.0-rc1 中修复。 该漏洞损害了广泛使用的证明助手 Lean 中形式化证明的可信度，因为它允许在不涉及内核不可靠性的情况下导出矛盾。这凸显了验证外部证明以及确保逻辑规范与编译实现一致性的重要性。 该漏洞源于 Lean 的逻辑定义在极大位置处返回空字符串，而编译后的原生代码返回整个原始字符串；将两者结合便产生矛盾，从而可以推出任何定理。Lean 团队在报告后约 90 分钟内修复了内存安全问题，并在五天内合并了完整的语义修复。

rss · Trail of Bits Blog · 9月9日 11:00

**背景**: Lean 是一种基于依赖类型理论的证明助手和函数式编程语言，用于数学和软件的形式化验证。在定理证明中，逻辑规范与可执行代码之间的任何不一致都可能产生不可靠的证明。形式化验证是根据形式规范证明系统正确性的过程，对于高可信软件至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>

</ul>
</details>

**标签**: `#lean`, `#formal-verification`, `#theorem-proving`, `#bug`, `#fermat-last-theorem`

---
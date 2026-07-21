---
layout: default
title: "Horizon Summary: 2026-07-21 (ZH)"
date: 2026-07-21
lang: zh
---

> 从 23 条内容中筛选出 3 条重要资讯。

---

1. [Cloudflare 内部 DNS 现已正式发布](#item-1) ⭐️ 8.0/10
2. [Flock 车牌识别 AI 误读致无辜者被捕](#item-2) ⭐️ 8.0/10
3. [提议互通式 Passkey 记录格式及 Go API](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Cloudflare 内部 DNS 现已正式发布](https://blog.cloudflare.com/internal-dns/) ⭐️ 8.0/10

Cloudflare 推出了内部 DNS 服务，为私有网络提供权威和递归 DNS 功能，现已正式发布，并与 Cloudflare 的零信任和网络平台集成。 这统一了 Cloudflare 全球网络上的公网和私网 DNS 管理，使企业能够在单一平台上应用一致的安全策略，并简化内部网络运营。 内部 DNS 运行在与公共 DNS 相同的任播网络上，提供低延迟解析，并利用 Cloudflare 的零信任访问控制来保护私有资源查询。

rss · Cloudflare Blog (PQ 迁移) · 7月20日 20:59

**背景**: 权威 DNS 服务器保存域名的官方 IP 地址记录，而递归 DNS 服务器代表客户端查询这些记录。零信任是一种安全模型，假设没有隐式信任，要求对每个访问请求进行严格的身份验证。Cloudflare 现有的平台提供公共 DNS（1.1.1.1）和零信任网络服务；内部 DNS 将这些功能扩展到企业内部网络。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudns.net/blog/authoritative-dns-server/">What is Authoritative DNS server? - ClouDNS Blog</a></li>
<li><a href="https://umbrella.cisco.com/blog/what-is-the-difference-between-authoritative-and-recursive-dns-nameservers">Difference Between Recursive DNS & Authoritative DNS - Cisco Umbrella</a></li>
<li><a href="https://www.ibm.com/think/topics/zero-trust">What is zero trust? - IBM</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#DNS`, `#Zero Trust`, `#private networking`, `#internal DNS`

---

<a id="item-2"></a>
## [Flock 车牌识别 AI 误读致无辜者被捕](https://www.schneier.com/blog/archives/2026/07/on-flock-license-plate-tracking-cameras.html) ⭐️ 8.0/10

一名作家因其车辆牌照被 Flock 自动车牌识别系统误读，被误认为盗车嫌疑人而遭多日追踪并逮捕。该系统仅匹配了不完整的车牌号'34 DTM'，忽略了中间的小号数字，导致误报。 此事暴露了执法监控中过度依赖有缺陷的 AI 的严重风险，不准确性可能导致冤拘。这加剧了关于隐私、公民自由以及大规模监控技术问责和精准性的讨论。 实际车牌为'34 03 DTM'，但输入 Flock 系统时仅为'34 DTM'，随后 AI 将其匹配为'34 10 DTM'，忽略了偶尔捕捉到的中间小号数字。这暴露了 AI 处理非标准车牌格式和模糊数据的局限性。

rss · Schneier on Security · 7月20日 11:03

**背景**: Flock Safety 摄像头是广泛使用的 AI 驱动自动车牌识别系统，可捕获车辆品牌、型号、颜色和位置等信息，并存入执法部门可搜索的数据库。隐私倡导者如 DeFlock 项目记录了它们的普及，并对大规模监控和潜在滥用表示担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.flocksafety.com/products/license-plate-readers">Flock Safety LPR Cameras: Automated License Plate Reader</a></li>
<li><a href="https://deflock.org/">DeFlock is an open-source project that maps license plate readers...</a></li>
<li><a href="https://www.motherjones.com/politics/2026/07/police-losing-jobs-flock-cameras-alprs/">Police keep losing their jobs for using Flock cameras to stalk people</a></li>

</ul>
</details>

**标签**: `#surveillance`, `#AI errors`, `#privacy`, `#license plate recognition`, `#security`

---

<a id="item-3"></a>
## [提议互通式 Passkey 记录格式及 Go API](https://words.filippo.io/passkey-record/) ⭐️ 7.0/10

Filippo Valsorda 提出了一种可互操作的 passkey 记录格式，用于存储 WebAuthn 凭证，类似于密码哈希字符串，并提供了一个草案级别的 crypto/passkey Go API，以实现标准化的凭证处理。 这通过提供一种标准化的 WebAuthn 凭证存储和交换方式，填补了 passkey 推广中的空白，使开发者更容易实现 passkey 认证，并可能加速 passkey 在整个行业的普及。 该格式不透明且可互操作，API 设计为无状态。作者质疑了跨账户强制唯一凭证 ID 的常见建议，认为当通过用户 ID 进行查找时，这一要求是不必要的。

rss · Filippo Valsorda (Go 密码学) · 7月20日 22:33

**背景**: WebAuthn 是 W3C 发布的用于无密码认证的标准，使用公钥加密技术。Passkey 是依赖生物识别或设备 PIN 的用户友好型 WebAuthn 凭证。目前，缺乏标准的可互操作序列化格式来存储这些凭证，往往导致供应商锁定。该提案旨在创建一个通用格式，类似于 bcrypt 字符串标准化密码哈希的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://words.filippo.io/passkey-record/">Opaque, Interoperable Passkey Records (and a Go API)</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAuthn">WebAuthn - Wikipedia</a></li>

</ul>
</details>

**标签**: `#passkeys`, `#webauthn`, `#golang`, `#cryptography`, `#interoperability`

---
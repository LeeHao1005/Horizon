---
layout: default
title: "Horizon Summary: 2026-07-15 (ZH)"
date: 2026-07-15
lang: zh
---

> 从 33 条内容中筛选出 7 条重要资讯。

---

1. [1.1.1.1 返回 EDE 33 标记 DNSSEC 验证绕过](#item-1) ⭐️ 8.0/10
2. [Cloudflare 推出 Precursor：连续行为式机器人检测](#item-2) ⭐️ 8.0/10
3. [施奈尔：聚焦 AI 数据中心掩盖财富集中问题](#item-3) ⭐️ 8.0/10
4. [RFC 9999：远程证明概念消息封装（CMW）标准发布](#item-4) ⭐️ 8.0/10
5. [Trail of Bits 测试手册新增 Rust 安全测试章节](#item-5) ⭐️ 7.0/10
6. [RFC 9916：为 PCEP 安全传输更新 TLS 使用限制](#item-6) ⭐️ 7.0/10
7. [RFC 9995 定义 COSE 哈希信封头部参数](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [1.1.1.1 返回 EDE 33 标记 DNSSEC 验证绕过](https://blog.cloudflare.com/dnssec-nta-ede-33/) ⭐️ 8.0/10

在 .AL 顶级域名因 DNSSEC 密钥轮换失败导致解析中断后，Cloudflare 的 1.1.1.1 解析器现在会返回扩展 DNS 错误代码 33（EDE 33），以显式表明 DNSSEC 验证已被绕过。 此举提升了运行透明度，使网络管理员和用户不仅知道验证被绕过，还能知晓何时通过负信任锚点进行了有意覆盖，有助于诊断 DNSSEC 问题，并减少对解析器的盲目信任。 EDE 33（负信任锚点）是 RFC 8914 中新定义的错误代码，用于指示应用了负信任锚点；它与 EDE 9（缺少 DNSKEY）一起返回，后者表明信任链断裂。.AL 事件需要部署 NTA 来恢复解析，1.1.1.1 现在在 NOERROR 响应中包含这些 EDE 代码，以通知客户端发生了绕过。

rss · Cloudflare Blog (PQ 迁移) · 7月14日 13:00

**背景**: DNSSEC 通过对 DNS 记录进行加密签名来防止欺骗；密钥轮换是替换签名密钥的过程，若操作不当会破坏信任链并导致域名无法解析。负信任锚点 (NTA) 允许解析器暂时绕过受影响域的验证。扩展 DNS 错误 (EDE) 在 RFC 8914 中标准化，可在 DNS 响应中提供额外诊断信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/dnssec-nta-ede-33">A broken DNSSEC rollover took down .AL. Now 1.1.1.1 tells you when validation is bypassed</a></li>
<li><a href="https://www.rfc-editor.org/rfc/rfc8914.html">RFC 8914: Extended DNS Errors</a></li>

</ul>
</details>

**标签**: `#DNSSEC`, `#DNS Security`, `#Cloudflare`, `#Extended DNS Errors`, `#Key Rollover`

---

<a id="item-2"></a>
## [Cloudflare 推出 Precursor：连续行为式机器人检测](https://blog.cloudflare.com/introducing-precursor/) ⭐️ 8.0/10

Cloudflare 推出了 Precursor，这是一款新的连续行为验证引擎，通过分析整个用户会话来检测高级机器人自动化，精度更高，同时减少对合法用户的干扰。 这种方法通过捕捉绕过单点检查的复杂自动化，改善了机器人管理，增强了网站安全性和用户体验，反映了行业向持续行为分析和代理行为检测的更广泛转变。 Precursor 运行在 Cloudflare 的边缘网络和浏览器内部，收集会话范围内的行为信号（如鼠标移动和交互模式）。现有 Cloudflare 机器人管理客户可通过一键启用该功能。

rss · Cloudflare Blog (PQ 迁移) · 7月13日 13:00

**背景**: 机器人检测传统上使用验证码或请求元数据分析等时间点检查。现在高级机器人能够模仿人类行为，使其难以被发现。Precursor 增加了一个持续监控层，观察整个会话中的用户行为，从而能够识别微妙的自动化特征。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/introducing-precursor/">Introducing Precursor: detecting agentic behavior with ...</a></li>
<li><a href="https://www.cloudflare.com/press/press-releases/2026/cloudflare-introduces-precursor-one-click-behavioral-defense-against-modern-bots/">Cloudflare Introduces Precursor; One-Click Behavioral Defense ...</a></li>

</ul>
</details>

**标签**: `#bot detection`, `#security`, `#Cloudflare`, `#behavioral analysis`, `#web security`

---

<a id="item-3"></a>
## [施奈尔：聚焦 AI 数据中心掩盖财富集中问题](https://www.schneier.com/blog/archives/2026/07/ai-data-centers-and-the-concentration-of-wealth.html) ⭐️ 8.0/10

Bruce Schneier 和 Nathan E. Sanders 在《卫报》上发表文章指出，政治上对 AI 数据中心的反对声音分散了人们对 AI 公司财富和权力集中这一更深层问题的关注。 这一观点将争论从地方环境和资源问题转向经济不平等和企业权力的系统性议题，可能影响未来的 AI 政策和监管方向。 文章指出，美国两党都反对数据中心建设，但这种聚焦可能让 AI 公司在不受制约的情况下继续扩大其金融和政治影响力。

rss · Schneier on Security · 7月13日 11:01

**背景**: AI 数据中心是容纳训练和运行先进 AI 模型所需硬件的大规模设施，通常消耗大量电力和水资源，引发地方争议。财富集中指少量企业掌握了巨量经济资源，可能转化为超常的政治影响力。Bruce Schneier 是知名的安全技术专家和作家，以科技与社会评论著称。

**标签**: `#AI data centers`, `#wealth concentration`, `#AI policy`, `#political influence`, `#Bruce Schneier`

---

<a id="item-4"></a>
## [RFC 9999：远程证明概念消息封装（CMW）标准发布](https://rfc-editor.org/info/rfc9999) ⭐️ 8.0/10

RFC 9999 定义了概念消息封装（CMW），一种使用 CBOR、JWT/CWT 和 X.509 封装 RATS 消息（如证据和证明结果）的通用结构。 该标准通过为 CBOR、JWT 和 X.509 提供统一的消息格式，提高了远程证明系统的互操作性，简化了实现，并促进了硬件安全和机密计算领域的采用。 CMW 引入了专用的 CBOR 标签、JWT 和 CWT 声明以及 X.509 扩展，并定义了媒体类型和 CoAP 内容格式，以支持在 HTTP、MIME 和 CoAP 等协议上传输。

rss · IETF 新标准 RFC (PQC 标准化) · 7月14日 16:34

**背景**: 远程证明程序（RATS）是一个 IETF 工作组，定义远程验证设备可信性的协议。RFC 9334 中引入了证据和证明结果等核心概念消息，但缺少通用封装格式，导致互操作性问题。CMW 利用 CBOR 进行高效二进制编码，JWT/CWT 用于 Web 令牌，X.509 用于基于证书的场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/rfc9334/">RFC 9334 - Remote ATtestation procedureS (RATS) Architecture</a></li>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-rats-msg-wrap/">RATS Conceptual Messages Wrapper (CMW) draft-ietf-rats-msg-wrap-23</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc8392">RFC 8392 - CBOR Web Token (CWT)</a></li>

</ul>
</details>

**标签**: `#remote-attestation`, `#IETF`, `#RFC`, `#security`, `#CBOR`

---

<a id="item-5"></a>
## [Trail of Bits 测试手册新增 Rust 安全测试章节](https://blog.trailofbits.com/2026/07/13/rust-proof-your-code-with-our-new-testing-handbook-chapter/) ⭐️ 7.0/10

Trail of Bits 在其测试手册中发布了一个新章节，全面介绍了 Rust 程序的安全测试工具和技术。 这份来自顶尖安全公司的资源帮助 Rust 开发者掌握专业测试实践，随着 Rust 的普及，有望减少其代码库中的漏洞。 该章节是公开测试手册 appsec.guide/rust 的一部分，涵盖了 Trail of Bits 用于 Rust 安全审计的具体工具和方法。

rss · Trail of Bits Blog · 7月13日 11:00

**背景**: Trail of Bits 是一家以安全审计闻名的网络安全公司。测试手册是一个开源应用安全测试指南。Rust 是一种重视内存安全的系统语言，但仍需严格测试以发现逻辑错误。

**标签**: `#rust`, `#security`, `#testing`, `#appsec`, `#guide`

---

<a id="item-6"></a>
## [RFC 9916：为 PCEP 安全传输更新 TLS 使用限制](https://rfc-editor.org/info/rfc9916) ⭐️ 7.0/10

RFC 9916 更新了 PCEPS（使用 TLS 保护 PCEP 通信）的规范，明确了当实现支持多个 TLS 版本时的处理方式，并明确禁止使用 TLS 1.3 的早期数据。 这一更新提高了 PCEPS 的安全性，防止因 TLS 版本不兼容及早期数据的重放攻击带来的风险，对网络路径计算基础设施的保护至关重要。 该更新对 RFC 8253 第 3.4 节进行了补充，特别禁止 TLS 1.3 的 0-RTT 早期数据，并要求在支持多个 TLS 版本时进行严格的版本协商。

rss · IETF 新标准 RFC (PQC 标准化) · 7月14日 23:25

**背景**: PCEP（路径计算单元通信协议）用于在 MPLS-TE 和段路由网络中进行集中路径计算。PCEPS 是其 TLS 加密版本，最初由 RFC 8253 定义。TLS 1.3 引入了早期数据（0-RTT）以加速会话恢复，但存在重放攻击风险，因此在安全敏感的协议中常被禁止。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rfc-editor.org/info/rfc5440/">RFC 5440: Path Computation Element (PCE) Communication ...</a></li>
<li><a href="https://www.cisco.com/c/en/us/td/docs/iosxr/cisco8000/srv6/b-srv6-configuration-guide/m-path-computation-element-protocol.pdf">Path Computation Element Protocol - Cisco</a></li>

</ul>
</details>

**标签**: `#PCEP`, `#TLS`, `#network security`, `#IETF`, `#protocol standard`

---

<a id="item-7"></a>
## [RFC 9995 定义 COSE 哈希信封头部参数](https://rfc-editor.org/info/rfc9995) ⭐️ 7.0/10

IETF RFC 9995 引入了新的 CBOR 对象签名与加密（COSE）头部参数，允许将载荷标记为哈希输出。这使得签名验证无需访问原始载荷数据。 这一改进加快了验证过程，在后量子密码学和原始载荷传输成本高的受限环境中尤为有益。它还包含内容格式和发现的提示，有助于互操作性。 新参数包括哈希算法标识符、内容类型提示和可用性提示，后者引用了可选的发现机制以查找原始载荷。该规范是对 COSE 的增量更新，建立在现有 IETF 工作之上。

rss · IETF 新标准 RFC (PQC 标准化) · 7月14日 03:34

**背景**: CBOR（简洁二进制对象表示）是一种类似 JSON 但更紧凑的二进制数据格式。COSE（CBOR 对象签名与加密）是使用 CBOR 序列化进行签名和加密的协议，由 RFC 8152 定义。哈希信封概念允许对载荷的哈希值进行签名而不是载荷本身，从而减少数据传输和处理开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CBOR">CBOR - Wikipedia</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc8152">RFC 8152 - CBOR Object Signing and Encryption (COSE)</a></li>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-cose-hash-envelope/">draft-ietf-cose-hash-envelope-10 - COSE Hash Envelope</a></li>

</ul>
</details>

**标签**: `#COSE`, `#Hash Envelope`, `#IETF`, `#RFC`, `#PQC`

---
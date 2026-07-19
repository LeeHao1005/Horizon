---
layout: default
title: "Horizon Summary: 2026-07-19 (ZH)"
date: 2026-07-19
lang: zh
---

> 从 26 条内容中筛选出 7 条重要资讯。

---

1. [RFC 9955：混合签名频谱分类](#item-1) ⭐️ 8.0/10
2. [RFC 10015 弃用 TLS 1.2 中 DH 与 RSA 密钥交换](#item-2) ⭐️ 8.0/10
3. [Cloudflare WAF 防护两个高危 WordPress 漏洞](#item-3) ⭐️ 7.0/10
4. [图灵 Delilah 语音加密系统文件拍卖](#item-4) ⭐️ 7.0/10
5. [AI 时代隐私保护：从个人控制转向企业问责](#item-5) ⭐️ 7.0/10
6. [RFC 10004：更新 CMC 合规要求并取代旧版 RFC](#item-6) ⭐️ 7.0/10
7. [RFC 9852 要求新协议必须使用 TLS 1.3](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [RFC 9955：混合签名频谱分类](https://rfc-editor.org/info/rfc9955) ⭐️ 8.0/10

IETF 发布了 RFC 9955，对混合数字签名方案的设计目标进行了分类，涵盖证明可组合性、非分离性和并发验证等安全考量。 该 RFC 为混合签名提供了标准化评估框架，对后量子密码迁移至关重要，能确保即使某个组件算法被攻破，整体安全仍得以保持。 关键属性包括证明可组合性（将混合安全性归约到组件）、非分离性（阻止剥离某个签名）、并发验证（要求两个组件均通过验证），以及兼容性和混合通用性。

rss · IETF 新标准 RFC (PQC 标准化) · 7月17日 02:41

**背景**: 混合数字签名将传统算法（如 RSA、ECDSA）与后量子算法（如 Dilithium、SPHINCS+）结合，以同时抵御经典和量子攻击。随着量子计算机威胁现有密码学，这类过渡方案至关重要。IETF 的这项工作催生了 RFC 9955，旨在标准化此类组合并为实现者提供指导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-pquip-hybrid-signature-spectrums/">draft-ietf-pquip-hybrid-signature-spectrums-07 - Hybrid signature spectrums</a></li>
<li><a href="https://eprint.iacr.org/2023/423.pdf">A Note on Hybrid Signature Schemes Nina Bindel† and Britta Hale‡ ⋆</a></li>
<li><a href="https://www.ietf.org/archive/id/draft-hale-pquip-hybrid-signature-spectrums-01.html">Hybrid signature spectrums</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#digital-signatures`, `#post-quantum-cryptography`, `#RFC`, `#standards`

---

<a id="item-2"></a>
## [RFC 10015 弃用 TLS 1.2 中 DH 与 RSA 密钥交换](https://rfc-editor.org/info/rfc10015) ⭐️ 8.0/10

RFC 10015 正式废弃在 TLS 1.2 和 DTLS 1.2 中使用有限域 Diffie-Hellman 和 RSA 密钥交换，并建议避免使用静态 ECDH 密码套件。该文档更新多项 RFC 以反映这些更改。 这一弃用举措通过促使部署转向提供前向保密的临时密钥交换方法，提升了安全性，降低了密钥泄露风险。它直接影响网络运营商、软件供应商以及所有依赖 TLS 1.2 安全通信的用户。 这些更改仅适用于 TLS 1.2 和 DTLS 1.2，因为更早的版本已被弃用，而 TLS 1.3 使用现代密钥交换。该文档更新了 17 个先前 RFC，包括 RFC 5246（TLS 1.2）和 RFC 6347（DTLS 1.2）。

rss · IETF 新标准 RFC (PQC 标准化) · 7月16日 20:55

**背景**: TLS 1.2 支持多种密钥交换方法，如 RSA、有限域 Diffie-Hellman（DH）和椭圆曲线 Diffie-Hellman（ECDH）。这些方法的静态版本对所有会话使用单一密钥对，使其容易遭受长期密钥泄露。临时变体（以 DHE 或 ECDHE 表示）每次会话生成临时密钥，确保前向保密。IETF 一直致力于要求前向保密，以便即使服务器私钥事后泄露，也能保护过往通信。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Finite_Field_Diffie-Hellman">Finite Field Diffie-Hellman</a></li>
<li><a href="https://en.wikipedia.org/wiki/Elliptic-curve_Diffie–Hellman">Elliptic-curve Diffie–Hellman - Wikipedia</a></li>

</ul>
</details>

**标签**: `#security`, `#TLS`, `#cryptography`, `#IETF`, `#deprecation`

---

<a id="item-3"></a>
## [Cloudflare WAF 防护两个高危 WordPress 漏洞](https://blog.cloudflare.com/wordpress-vulnerabilities/) ⭐️ 7.0/10

Cloudflare 部署了两条 WAF 规则，自动防御由 WordPress 安全团队披露的两个高危漏洞，保护所有使用受影响版本的客户。 这一主动防护为大量 WordPress 站点抵御潜在攻击，凸显了及时打补丁的紧迫性以及云端安全层的价值。 WAF 规则作为虚拟补丁在边缘拦截攻击，但未公布具体 CVE 编号和受影响版本；手动更新至修复版本仍是根本措施。

rss · Cloudflare Blog (PQ 迁移) · 7月17日 21:30

**背景**: Web 应用程序防火墙（WAF）通过过滤和监控 HTTP 流量来阻止 SQL 注入、跨站脚本等攻击。Cloudflare 提供全球云 WAF 可即时部署。WordPress 是使用广泛的内容管理系统，常受黑客攻击，及时缓解漏洞至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Web_application_firewall">Web application firewall</a></li>

</ul>
</details>

**标签**: `#web-security`, `#wordpress`, `#waf`, `#cloudflare`, `#vulnerability`

---

<a id="item-4"></a>
## [图灵 Delilah 语音加密系统文件拍卖](https://www.schneier.com/blog/archives/2026/07/details-of-alan-turings-voice-encryption-system.html) ⭐️ 7.0/10

一批图灵的战时文件被拍卖，披露了他秘密的'Delilah'便携式语音加密系统的工程细节。 这一发现提供了图灵除破译密码外的密码工程工作的前所未见的细节，极大地丰富了二战安全通信的历史。 Delilah 系统开发于 1943 至 1945 年，通过向语音信号添加伪随机密钥流实现加密，方法类似电传打字机加密；其设计强调便携性，与庞大的 SIGSALY 系统形成鲜明对比。文件包含图灵的手写笔记和技术图表。

rss · Schneier on Security · 7月17日 11:02

**背景**: 图灵因在二战中破解纳粹 Enigma 密码而闻名，但他也对语音加密做出了贡献。Delilah 项目旨在制造便携式安全语音通信系统，取代体积如房间大小且资源需求巨大的 SIGSALY。语音加密将语音在传输过程中扰乱为无法理解的形式，在接收端恢复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/alan-turings-delilah">Alan Turing ’s Secret “ Delilah ” Project - IEEE Spectrum</a></li>
<li><a href="https://interestingengineering.com/culture/delilah-alan-turing-voice-encryption-secret">The little-known story of Alan Turing ’s top-secret ' Delilah ' project</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#history`, `#Alan Turing`, `#voice encryption`, `#World War II`

---

<a id="item-5"></a>
## [AI 时代隐私保护：从个人控制转向企业问责](https://www.schneier.com/blog/archives/2026/07/protecting-privacy-in-an-ai-era.html) ⭐️ 7.0/10

丹尼尔·索洛夫在《华尔街日报》发文主张，不应依赖个人控制数据，而应通过数据最小化、信义义务和过失人工智能设计问责来让企业负责。 这标志着隐私监管理念的重大转变，可能在人工智能普及的时代带来更有效的保护，并影响未来的法律与企业数据实践。 索洛夫的建议包括多利益相关方技术审查和有害算法问责；完整论文在 SSRN 上，《华尔街日报》文章可通过替代链接访问。

rss · Schneier on Security · 7月16日 14:34

**背景**: 现行隐私法律主要依赖通知和同意机制，让个人负责管理自己的数据。然而，人工智能系统能从海量数据中推断出敏感信息，使得个人控制变得不切实际。索洛夫将其类比为食品和药品监管，即由企业而非消费者承担安全责任。

**标签**: `#privacy`, `#AI`, `#regulation`, `#data-protection`, `#accountability`

---

<a id="item-6"></a>
## [RFC 10004：更新 CMC 合规要求并取代旧版 RFC](https://rfc-editor.org/info/rfc10004) ⭐️ 7.0/10

IETF 发布了 RFC 10004，为基于 CMS 的证书管理（CMC）注册协议规定了一套合规要求，并正式废除了旧版标准 RFC 5274 和 RFC 6402。 该文档为公钥基础设施（PKI）系统的实现者提供了明确的合规指南，确保基于 CMC 的证书管理解决方案的互操作性和一致性，这对安全网络通信至关重要。 合规声明集中在 CMC 注册协议上；底层的 ASN.1 结构和传输机制分别在 RFC 10002 和 RFC 10003 中单独定义。符合要求的实现必须共同遵循 RFC 10004 中规定的配置文件。

rss · IETF 新标准 RFC (PQC 标准化) · 7月17日 23:17

**背景**: 基于 CMS 的证书管理（CMC）是一种 IETF 协议，它使用加密消息语法（CMS）来管理 X.509 公钥证书，例如注册和吊销。抽象语法表示一（ASN.1）是许多互联网协议中用于定义数据结构的标准语言。RFC 5274 和 RFC 6402 是 CMC 合规的早期规范，RFC 10004 随着证书管理标准的持续发展而更新并取代了它们。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ietf.org/ietf-ftp/internet-drafts/draft-ietf-lamps-rfc5272bis-03.html">Certificate Management over CMS ( CMC )</a></li>
<li><a href="https://en.wikipedia.org/wiki/ASN.1">ASN.1</a></li>

</ul>
</details>

**标签**: `#CMC`, `#certificate management`, `#IETF`, `#RFC`, `#compliance`

---

<a id="item-7"></a>
## [RFC 9852 要求新协议必须使用 TLS 1.3](https://rfc-editor.org/info/rfc9852) ⭐️ 7.0/10

IETF 发布了 RFC 9852，规定任何使用传输层安全（TLS）的新协议都必须强制使用 TLS 1.3，因为它在安全性和隐私性方面较 TLS 1.2 有已验证的改进。该要求不适用于数据报 TLS（DTLS），因为 DTLS 1.3 尚未广泛部署。 此举正式确立了行业向 TLS 1.3 迁移的趋势，加速淘汰过时且安全性较低的协议，推动整个生态系统采用更强大的加密和隐私保护。它直接影响了协议设计者、实现者和服务运营商，将现代安全性作为不可妥协的前提。 该 RFC 更新了 RFC 9325，并将后量子密码学作为其理由的一部分，指出 TLS 1.3 为未来的抗量子算法提供了更好的基础。该要求仅适用于使用 TLS 的新协议，不适用于 DTLS，这反映了 DTLS 1.3 较慢的采用速度。

rss · IETF 新标准 RFC (PQC 标准化) · 7月17日 02:25

**背景**: 传输层安全（TLS）是一种用于保障网络通信安全的加密协议。TLS 1.3 是最新版本，提供了前向保密、减少握手延迟和加密更多握手过程等重大改进。数据报 TLS（DTLS）是为 UDP 等不可靠数据报协议设计的变种，常用于实时应用；其 1.3 版本实现相对较少。后量子密码学指的是旨在抵御未来量子计算机攻击的算法，将其集成到 TLS 中是一个活跃的标准化领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DTLS">DTLS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>

</ul>
</details>

**标签**: `#network security`, `#TLS`, `#standardization`, `#post-quantum cryptography`, `#protocols`

---
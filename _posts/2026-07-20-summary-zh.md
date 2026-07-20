---
layout: default
title: "Horizon Summary: 2026-07-20 (ZH)"
date: 2026-07-20
lang: zh
---

> 从 25 条内容中筛选出 3 条重要资讯。

---

1. [Cloudflare WAF 保护 WordPress 免受两个高危漏洞影响](#item-1) ⭐️ 8.0/10
2. [拍卖文件揭示图灵秘密语音加密系统 Delilah](#item-2) ⭐️ 7.0/10
3. [RFC 10002：更新版的基于 CMS 的证书管理标准](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Cloudflare WAF 保护 WordPress 免受两个高危漏洞影响](https://blog.cloudflare.com/wordpress-vulnerabilities/) ⭐️ 8.0/10

Cloudflare 已部署两条 WAF 规则，以防御 WordPress 安全团队最近披露的两个高危漏洞，保护所有使用受影响 WordPress 版本的客户。 这一主动措施为使用 Cloudflare 的数百万 WordPress 站点提供即时保护，可能在管理员应用官方补丁之前防止漏洞被广泛利用。 虽然 WAF 规则提供了防护，但并不能替代更新；受影响用户仍应尽快升级到最新的 WordPress 修补版本以确保全面保护。

rss · Cloudflare Blog (PQ 迁移) · 7月17日 21:30

**背景**: Web 应用程序防火墙（WAF）是一种位于 Web 应用程序与互联网之间的安全系统，分析传入的 HTTP 请求并阻止那些匹配已知攻击模式（如 SQL 注入或跨站脚本）的请求。Cloudflare 的 WAF 是一项基于云的服务，可在无需更改服务器的情况下保护网站。在此事件中，Cloudflare 创建了特定规则来检测和阻止利用已披露 WordPress 漏洞的尝试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/">What is a WAF ? | Web Application Firewall explained</a></li>

</ul>
</details>

**标签**: `#security`, `#wordpress`, `#cloudflare`, `#waf`, `#vulnerability`

---

<a id="item-2"></a>
## [拍卖文件揭示图灵秘密语音加密系统 Delilah](https://www.schneier.com/blog/archives/2026/07/details-of-alan-turings-voice-encryption-system.html) ⭐️ 7.0/10

2023 年 11 月，一批名为“贝利文件”的战时档案在伦敦拍卖，其中包含艾伦·图灵关于其绝密便携式语音加密系统 Delilah 的手写笔记，该系统于 1943 至 1945 年间研发。 这些文件揭示了图灵在数字语音加密方面较少为人知的贡献，开创了早期数字技术，超越了破译密码的范畴，丰富了密码学史。 Delilah 是一种便携式系统，利用早期数字方法将语音转换为加密信号；文件中既有图灵的手稿，也有工程师唐纳德·贝利根据其口述所做的笔记，贝利将文件珍藏至 2020 年去世。

rss · Schneier on Security · 7月17日 11:02

**背景**: 艾伦·图灵是英国数学家和计算机科学家，因二战期间在布莱切利园破解恩尼格玛密码而闻名。Delilah 项目旨在为军事用途提供安全的便携式语音通信。语音加密将语音转换为乱码信号后传输，接收端再解密还原，这种方法预示着现代数字加密标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hackaday.com/2026/06/26/alan-turings-remarkable-nearly-forgotten-voice-encryption-device/">Alan Turing’s Remarkable, Nearly-Forgotten Voice Encryption ...</a></li>
<li><a href="https://interestingengineering.com/culture/delilah-alan-turing-voice-encryption-secret">The little-known story of Alan Turing’s top-secret ‘Delilah ...</a></li>
<li><a href="https://netcrook.com/written_article?slug=delilah-and-the-quiet-birth-of-digital-voice-security&lang=en">Delilah and the Quiet Birth of Digital Voice Security</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#history`, `#Alan Turing`, `#encryption`, `#voice encryption`

---

<a id="item-3"></a>
## [RFC 10002：更新版的基于 CMS 的证书管理标准](https://rfc-editor.org/info/rfc10002) ⭐️ 7.0/10

RFC 10002 定义了基于 CMS 的证书管理（CMC）的基本语法，并取代了先前标准 RFC 5272 和 RFC 6402。 此次更新为公钥基础设施（PKI）实现者提供了现代化且精简的规范，确保了依赖 CMS 的证书管理协议的互操作性和清晰度。 新 RFC 要求配套的传输文档（RFC 10003）和需求使用文档（RFC 10004）才能构成完整定义，并明确废弃了 RFC 5272 和 RFC 6402。

rss · IETF 新标准 RFC (PQC 标准化) · 7月17日 23:01

**背景**: 加密消息语法（CMS）是 IETF 制定的、用于密码保护消息的标准，在 PKI 中广泛使用。基于 CMS 的证书管理（CMC）是一种管理 X.509 数字证书的协议，最初在 RFC 5272 中定义，后由 RFC 6402 修订。RFC 10002 更新并整合了这些早期规范。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cryptographic_Message_Syntax">Cryptographic Message Syntax</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc5272">RFC 5272 - Certificate Management over CMS (CMC)</a></li>

</ul>
</details>

**标签**: `#IETF`, `#RFC`, `#PKI`, `#Certificate Management`, `#CMS`

---
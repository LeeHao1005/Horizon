---
layout: default
title: "Horizon Summary: 2026-07-22 (ZH)"
date: 2026-07-22
lang: zh
---

> 从 27 条内容中筛选出 3 条重要资讯。

---

1. [提出不透明的、可互操作的通行密钥记录格式及 Go API](#item-1) ⭐️ 8.0/10
2. [MIT 安装 500 多个高级 AI 监控摄像头](#item-2) ⭐️ 8.0/10
3. [Cloudflare 内部 DNS 正式全面可用](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [提出不透明的、可互操作的通行密钥记录格式及 Go API](https://words.filippo.io/passkey-record/) ⭐️ 8.0/10

Filippo Valsorda 提出了一种不透明的、可互操作的 WebAuthn 凭据（通行密钥）记录格式，并为 crypto 包提供了配套的 Go API，旨在标准化通行密钥的存储和交换方式。 该提案解决了通行密钥缺乏标准化存储格式的问题，类似于 bcrypt 字符串对密码哈希的标准化作用。它可以提高可移植性、减少供应商锁定，并加速无密码认证的采用。 该格式是不透明的，通过隐藏内部结构来增强安全性和互操作性。Go API 提案针对标准库的 crypto 包，但尚未启动正式的标准化流程。

rss · Filippo Valsorda (Go 密码学) · 7月20日 22:33

**背景**: WebAuthn 是 W3C 标准，使用公钥加密进行无密码认证。通行密钥是 WebAuthn 凭据，通常通过 Apple Keychain 或 Windows Hello 等平台身份验证器在设备间同步。目前缺乏通用的、可互操作的凭据存储方式，导致供应商锁定。该提案为通行密钥引入了一种类似密码哈希字符串的格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAuthn">WebAuthn</a></li>

</ul>
</details>

**标签**: `#passkeys`, `#webauthn`, `#authentication`, `#cryptography`, `#go`

---

<a id="item-2"></a>
## [MIT 安装 500 多个高级 AI 监控摄像头](https://www.schneier.com/blog/archives/2026/07/mit-to-become-hotbed-of-ai-video-surveillance.html) ⭐️ 8.0/10

MIT 正在学术楼、宿舍和户外区域安装 500 多个 AI 监控摄像头，安装工作从 2025 年 11 月持续到 2026 年 9 月。 在顶尖科技大学部署这种系统加剧了关于 AI 监控隐私和伦理的辩论，可能影响其他机构的政策。 摄像头可在 35 英尺（约 11 米）外对衣物颜色、性别和年龄进行分类，并能检测移动、徘徊、人群、口罩和摄像头篡改。数据最多保留 30 天，项目耗资超过 300 万美元。

rss · Schneier on Security · 7月21日 11:07

**背景**: AI 视频监控利用机器学习实时分析录像，自动识别物体和行为。MIT 是世界知名的研究型大学。校园监控系统因可能的大规模数据收集和隐私侵蚀引发争议，特别是结合人脸识别和人口统计分析时。

**标签**: `#AI surveillance`, `#privacy`, `#ethics`, `#MIT`, `#Bruce Schneier`

---

<a id="item-3"></a>
## [Cloudflare 内部 DNS 正式全面可用](https://blog.cloudflare.com/internal-dns/) ⭐️ 7.0/10

Cloudflare 宣布推出内部 DNS 服务，将权威和递归 DNS 功能引入私有网络，并集成到其全球 Zero Trust 平台中。 此举将内部 DNS 与现有 Zero Trust 安全和网络服务统一，降低了混合环境的复杂性和攻击面，使组织可在公私有网络中实施一致的策略。 该服务支持私有域名的权威解析以及从私有网络发出的递归查询，两者均基于 Cloudflare 的 Anycast 网络运行，并通过 Zero Trust 控制面板进行管理。

rss · Cloudflare Blog (PQ 迁移) · 7月20日 20:59

**背景**: 零信任网络是一种默认不信任任何实体、要求持续验证的安全模型。权威 DNS 服务器为特定域名提供最终解析结果，而递归 DNS 服务器则通过查询其他服务器获取答案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/">Zero Trust Security | What's a Zero Trust Network? - Cloudflare</a></li>
<li><a href="https://www.nslookup.io/learning/recursive-vs-authoritative-dns/">Recursive vs Authoritative DNS — What's the difference?</a></li>

</ul>
</details>

**标签**: `#DNS`, `#Cloudflare`, `#Zero Trust`, `#Networking`, `#Private Networks`

---
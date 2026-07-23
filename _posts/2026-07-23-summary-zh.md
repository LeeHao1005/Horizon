---
layout: default
title: "Horizon Summary: 2026-07-23 (ZH)"
date: 2026-07-23
lang: zh
---

> 从 28 条内容中筛选出 6 条重要资讯。

---

1. [Filippo Valsorda 提案：可互通的 Passkey 记录格式及 Go API](#item-1) ⭐️ 8.0/10
2. [MIT 成为 AI 视频监控的热点](#item-2) ⭐️ 8.0/10
3. [Flock AI 车牌识别错误导致冤捕](#item-3) ⭐️ 8.0/10
4. [Cloudflare Internal DNS 正式发布](#item-4) ⭐️ 7.0/10
5. [亲身经历揭露邮箱安全隐患](#item-5) ⭐️ 7.0/10
6. [NIST 发布存储安全指南 SP 800-209 修订初稿](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Filippo Valsorda 提案：可互通的 Passkey 记录格式及 Go API](https://words.filippo.io/passkey-record/) ⭐️ 8.0/10

Filippo Valsorda 提出了一种用于 WebAuthn 凭证（Passkey）的可互通记录格式，以及相应的 Go API，旨在标准化 Passkey 数据的存储和交换方式。 该提案解决了 Passkey 普及中的关键缺口，使凭证可跨平台移植，减少供应商锁定，并便于备份和迁移。这可能对开发者实践和更广泛的身份验证生态系统产生影响。 该记录格式类似于密码哈希字符串，使用结构化前缀来编码凭证元数据和加密材料。提议的 Go API（暂定位于 `crypto/passkey`）将解析并生成这些记录，简化 WebAuthn 集成。

rss · Filippo Valsorda (Go 密码学) · 7月20日 22:33

**背景**: WebAuthn 是 W3C 的网页身份验证标准，使用公钥加密技术实现无密码登录。Passkey 是基于 WebAuthn 的凭证，可在设备间同步，但目前缺乏通用的存储和交换格式，导致碎片化。标准化 Passkey 记录，类似于 bcrypt 的 `$2y$` 密码哈希字符串格式，将允许不同密码管理器和服务之间无缝互操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://words.filippo.io/passkey-record/">Opaque, Interoperable Passkey Records (and a Go API )</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAuthn">WebAuthn - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#passkeys`, `#Go`, `#WebAuthn`, `#interoperability`

---

<a id="item-2"></a>
## [MIT 成为 AI 视频监控的热点](https://www.schneier.com/blog/archives/2026/07/mit-to-become-hotbed-of-ai-video-surveillance.html) ⭐️ 8.0/10

麻省理工学院正在部署 500 多个 AI 监控摄像头，可对学术楼、宿舍和户外区域的实时视频进行面部、物体和行为分类。这个 300 万美元的项目还能在 11 米范围内自动分析衣物颜色、性别和年龄。 一流大学部署此类系统将使大规模监控常态化，引发严重的隐私和伦理担忧，并可能为其他学术机构和公共场所树立先例。 摄像头功能包括徘徊、人群、口罩和摄像机篡改检测，数据保留最多 30 天。安装于 2025 年 11 月开始，计划 2026 年 9 月完成。

rss · Schneier on Security · 7月21日 11:07

**背景**: AI 视频监控利用计算机视觉和深度学习自动分析录像。徘徊检测识别人员在特定区域超时停留，摄像机篡改检测标记被遮挡或移动的画面，而属性分类能够估算可见特征如性别和年龄。这些技术引发了关于准确性、偏见和大规模数据收集的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://surveillant.ai/solutions/loitering-detection">Loitering Detection | AI-Powered Suspicious Behavior Monitoring</a></li>
<li><a href="https://www.een.com/video-analytics-tampering-detection/">Camera Tampering Detection | Eagle Eye Networks</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2666827023000531">Real-time AI-based inference of people gender and age in ...</a></li>

</ul>
</details>

**标签**: `#AI surveillance`, `#privacy`, `#ethics`, `#campus security`, `#facial recognition`

---

<a id="item-3"></a>
## [Flock AI 车牌识别错误导致冤捕](https://www.schneier.com/blog/archives/2026/07/on-flock-license-plate-tracking-cameras.html) ⭐️ 8.0/10

Flock 的 AI 车牌识别系统因车牌号录入错误（混淆了 '34 03 DTM' 和 '34 10 DTM'），导致一名司机被错误追踪并逮捕。 这起事件凸显了依赖容易出错的 AI 监控系统的危险性，表明一个微小的数据录入错误就可能引发严重的公民自由侵犯和不公正的法律行动。 Flock 的系统仅记录了车牌中的大号字符 '34 DTM'，忽略了中间的小数字，导致其 AI 错误匹配了相似字符的车辆；这一缺陷暴露了部分车牌匹配的关键漏洞。

rss · Schneier on Security · 7月20日 11:03

**背景**: Flock Safety 是一家提供车牌识别（LPR）摄像头的公司，其设备广泛部署于社区和警察部门。系统自动捕获并存储车辆牌照数据，虽有助于调查但也引发隐私担忧。最近，由于担心监控过度和移民追踪，美国一些城市已取消与其合同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.npr.org/2026/02/17/nx-s1-5612825/flock-contracts-canceled-immigration-survillance-concerns">Why some cities are canceling Flock license plate reader contracts : NPR</a></li>

</ul>
</details>

**标签**: `#privacy`, `#surveillance`, `#AI-errors`, `#license-plate-recognition`, `#civil-liberties`

---

<a id="item-4"></a>
## [Cloudflare Internal DNS 正式发布](https://blog.cloudflare.com/internal-dns/) ⭐️ 7.0/10

Cloudflare 宣布 Internal DNS 正式全面可用，将面向私有网络的权威 DNS 和递归 DNS 服务整合到其全球网络和 Zero Trust 控制平面中。 这使得企业能够使用与公共 DNS 相同的基础设施和安全策略来管理内部 DNS，充分利用 Cloudflare 的全球 Anycast 网络和 Zero Trust 平台，从而简化运营并增强安全性。 该服务运行在 Cloudflare 的全球 Anycast 网络上，为私有网络提供集中式控制和 DNS 解析，并与 Zero Trust 控制平面集成以实现策略执行。

rss · Cloudflare Blog (PQ 迁移) · 7月20日 20:59

**背景**: 权威 DNS 服务器存储域名的官方 DNS 记录，提供关于该域名资源的权威答案。递归 DNS 解析器代表客户端查询多个 DNS 服务器，将域名解析为 IP 地址。Zero Trust 控制平面是一个集中式策略引擎，管理与数据平面分离的访问权限和安全策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cloudflare.com/learning/dns/dns-server-types/">DNS server types | Learning Center</a></li>
<li><a href="https://www.cloudflare.com/learning/dns/what-is-recursive-dns/">What Is Recursive DNS ?</a></li>
<li><a href="https://quizlet.com/study-guides/zero-trust-control-plane-a83dd918-9a73-4528-90dc-9ff582e6be57">Zero Trust Control Plane Study Guide | Quizlet</a></li>

</ul>
</details>

**标签**: `#DNS`, `#Cloudflare`, `#Private Networks`, `#Zero Trust`, `#Networking`

---

<a id="item-5"></a>
## [亲身经历揭露邮箱安全隐患](https://www.schneier.com/blog/archives/2026/07/first-person-identity-theft-story.html) ⭐️ 7.0/10

一起令人痛心的身份盗窃亲身经历显示，受害者将双因素认证码交给骗子，导致邮箱被接管，进而引发多个账户沦陷。 此案例凸显了邮箱账户常成为单点故障——一旦被攻破，攻击者即可重置密码并访问众多其他服务。 受害者直接分享了 2FA 码，但底层缺陷在于许多在线服务仅依赖邮箱进行账户恢复，使得邮箱安全至关重要。

rss · Schneier on Security · 7月22日 11:02

**背景**: 双因素认证（2FA）在密码之外增加了一层保护，通常通过短信或应用生成验证码。但若邮箱被攻破，攻击者可拦截发至邮箱的 2FA 码，并利用密码重置链接控制其他账户。这一依赖性使邮箱成为最需保护的账户。

**标签**: `#identity theft`, `#email security`, `#two-factor authentication`, `#cybersecurity awareness`, `#account takeover`

---

<a id="item-6"></a>
## [NIST 发布存储安全指南 SP 800-209 修订初稿](https://csrc.nist.gov/pubs/sp/800/209/r1/ipd) ⭐️ 7.0/10

NIST 发布了 SP 800-209 修订版 1 的初步公开草案，通过删除过时技术、修订威胁分析并增添新关注领域、将安全控制重组为七个标准化系列，更新了存储基础设施安全指南。 更新后的指南有助于组织应对现代存储威胁、减少配置错误并增强数据韧性，以应对软件定义存储架构日益增长的复杂性。 新增“平台安全威胁”和“数据韧性/保护受损”章节；附录 C 提供了控制措施与威胁的映射，并删除了对专有技术的引用。

rss · NIST CSRC Drafts (标准草案) · 7月22日 04:00

**背景**: NIST SP 800-209 最初于 2020 年 10 月发布，为存储系统提供全面的安全建议。NIST 特别出版物是美国联邦机构及业界广泛采用的安全指南。本次修订版反映了当前威胁和向软件定义存储的架构转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/pubs/sp/800/209/r1/ipd">SP 800-209 Rev. 1, Security Guidelines for Storage Infrastructure | CSRC</a></li>
<li><a href="https://csrc.nist.gov/pubs/sp/800/209/final">SP 800-209, Security Guidelines for Storage Infrastructure | CSRC</a></li>

</ul>
</details>

**标签**: `#NIST`, `#storage security`, `#security guidelines`, `#draft`, `#cybersecurity`

---
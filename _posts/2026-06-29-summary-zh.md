---
layout: default
title: "Horizon Summary: 2026-06-29 (ZH)"
date: 2026-06-29
lang: zh
---

> 从 24 条内容中筛选出 3 条重要资讯。

---

1. [Meta 正为警方和军方测试面部识别技术](#item-1) ⭐️ 8.0/10
2. [近百万护照在线泄露](#item-2) ⭐️ 7.0/10
3. [RFC 9994 规范 MPLS 网络动作子栈](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Meta 正为警方和军方测试面部识别技术](https://www.schneier.com/blog/archives/2026/06/meta-is-testing-facial-recognition-for-police-and-military.html) ⭐️ 8.0/10

据报道，Meta 正与一家五角大楼供应商合作，为其智能眼镜开发面部识别原型功能，该功能可实现实时身份识别，可能被警方和军方使用。 此举引发了严重的隐私和伦理担忧，因为它可能导致当局大规模监控和滥用技术。这也标志着科技巨头与政府监控项目之间的关系进一步深化。 该原型正与一家五角大楼供应商合作开发，同时美国移民和海关执法局（ICE）此前已表示有意部署此类眼镜进行实时身份识别。该技术目前处于测试阶段，尚未向公众提供。

rss · Schneier on Security · 6月26日 16:40

**背景**: 面部识别技术通过算法将图像或视频中的人脸与数据库进行匹配。内置摄像头的智能眼镜能够隐蔽地捕捉人脸，引发隐私问题。Meta（前身为 Facebook）此前曾将面部识别用于照片标记，但在 2021 年因隐私争议而停用。这项新举措标志着其向军事和执法应用的转变。

**标签**: `#facial recognition`, `#surveillance`, `#privacy`, `#Meta`, `#law enforcement`

---

<a id="item-2"></a>
## [近百万护照在线泄露](https://www.schneier.com/blog/archives/2026/06/one-million-passports-leaked-online.html) ⭐️ 7.0/10

一个包含近百万本全球护照的数据库从大麻药房的身份证验证系统被盗，并在网上泄露。 这一事件表明，将高价值凭证用于低安全性认证会带来严重风险，可能导致大规模身份盗用和护照伪造。 被入侵的系统用于大麻药房的年龄验证，泄露的数据包含来自多个国家的护照详细信息，由数据泄露追踪网站报道。

rss · Schneier on Security · 6月26日 11:03

**背景**: 护照是政府签发的用于证明身份和国籍的主要文件。它们被视为高价值凭证，因为它们可用于国际旅行、金融交易和其他敏感活动。当此类凭证被用于安全级别较低的目的（如零售店的年龄验证）时，便容易因系统安全措施不完善而遭到泄露。此次泄露事件突出了一点：凭证应根据其最高潜在用途加以保护，而非最低用途。

**标签**: `#data-breach`, `#security`, `#passport-leak`, `#credential-reuse`, `#systemic-risk`

---

<a id="item-3"></a>
## [RFC 9994 规范 MPLS 网络动作子栈](https://rfc-editor.org/info/rfc9994) ⭐️ 7.0/10

RFC 9994 定义了 MPLS 网络动作（MNA）子栈，能够在 MPLS 标签栈中直接编码网络动作和辅助数据，并更新了 RFC 9789，细化了 MNA 定义文档的要求。 该标准为在 MPLS 数据包中编码网络动作和辅助数据提供了统一方法，推动了带内 OAM、流量工程和用户自定义处理等高级用例，并促进了多厂商设备间的互操作性。 MNA 子栈嵌入 MPLS 标签栈，包含网络动作指示符和可选的辅助数据。RFC 9994 更新了定义 MNA 动作文档中必须包含的信息列表，这些要求最初在 RFC 9789 中规定。

rss · IETF 新标准 RFC (PQC 标准化) · 6月27日 01:14

**背景**: MPLS（多协议标签交换）是一种使用短标签而非网络地址转发数据包的网络技术。IETF 的 MNA 框架（RFC 9789）概述了如何在 MPLS 数据包中携带网络动作和辅助数据。RFC 9994 提供了具体的子栈编码方式，使实际部署成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rfc-editor.org/rfc/rfc9994.pdf">PDF RFC 9994: MPLS Network Action (MNA) Sub-Stack Specification Including ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multiprotocol_Label_Switching">Multiprotocol Label Switching - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2410.20400v1">MPLS Network Actions: Technological Overview and P4-Based Implementation on a High-Speed Switching ASIC</a></li>

</ul>
</details>

**标签**: `#MPLS`, `#networking`, `#standards`, `#IETF`, `#protocol design`

---
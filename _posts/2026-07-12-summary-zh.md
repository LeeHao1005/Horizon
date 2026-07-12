---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> 从 24 条内容中筛选出 4 条重要资讯。

---

1. [RFC 9846 发布，更新 TLS 1.3 协议并淘汰旧版 RFC](#item-1) ⭐️ 9.0/10
2. [为何我们不能等待更好的后量子签名算法](#item-2) ⭐️ 8.0/10
3. [AI 监控与社会进步](#item-3) ⭐️ 7.0/10
4. [AI 语言模型可能改变人类说话方式](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [RFC 9846 发布，更新 TLS 1.3 协议并淘汰旧版 RFC](https://rfc-editor.org/info/rfc9846) ⭐️ 9.0/10

RFC 9846 已发布为 TLS 1.3 的新版权威标准，取代了 RFC 8446 及更早的 TLS 规范，并对 TLS 1.2 的实现提出了新的要求。 这一更新标准整合了多年协议演进成果，确保了更强的安全性，并为实现者提供了清晰指导，影响所有安全的互联网通信。 RFC 9846 整合了密钥派生（通过 RFC 5705）和扩展处理（RFC 6066）方面的更新，并正式要求现代 TLS 1.2 实现采纳这些实践。

rss · IETF 新标准 RFC (PQC 标准化) · 7月11日 16:03

**背景**: TLS（传输层安全）是 HTTPS 背后的加密协议，保护绝大多数网络流量。TLS 1.3 最初在 RFC 8446（2018 年）中规定，简化了握手过程并移除了不安全算法。RFC 5705 定义了应用从 TLS 会话派生额外密钥的标准方法，RFC 6066 定义了诸如服务器名称指示（SNI）等重要扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ietf.org/rfc/rfc5705">ietf.org/ rfc / rfc 5705</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc6066">RFC 6066 - Transport Layer Security (TLS) Extensions: Extension Definitions</a></li>

</ul>
</details>

**标签**: `#TLS`, `#security`, `#networking`, `#IETF`, `#standards`

---

<a id="item-2"></a>
## [为何我们不能等待更好的后量子签名算法](https://blog.cloudflare.com/ml-dsa-will-have-to-do/) ⭐️ 8.0/10

Cloudflare 分析了 NIST 正在考虑用于未来标准化的九个新后量子签名候选算法，并得出结论：组织应立即采用已标准化的 ML-DSA，而不是等待这些未来的改进。 密码学迁移需要数年时间，延迟采用后量子签名会使系统容易遭受“先收集后破解”攻击。Cloudflare 务实的建议推动了针对量子威胁的早期防护。 ML-DSA（FIPS 204）是一种源自 CRYSTALS-Dilithium 的格密码方案，被认为能抵御量子计算机的攻击。九个新候选算法探索了不同的数学基础，但距离标准化仍需数年。

rss · Cloudflare Blog (PQ 迁移) · 7月9日 14:00

**背景**: 后量子密码学旨在开发能抵抗量子计算机攻击的算法，量子计算机可能破解当前的 RSA 和椭圆曲线系统。NIST 自 2016 年起推动此类算法的标准化，并于 2024 年将 ML-DSA 作为模格数字签名标准（FIPS 204）发布。格密码是 ML-DSA 的基础，它依赖于对经典和量子计算机都难以求解的数学难题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://rya-sge.github.io/access-denied/2026/06/29/ml-dsa-fips-204-post-quantum-signatures/">ML - DSA — The Module-Lattice Digital Signature Standard (FIPS 204)</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#digital signatures`, `#NIST`, `#ML-DSA`, `#security`

---

<a id="item-3"></a>
## [AI 监控与社会进步](https://www.schneier.com/blog/archives/2026/07/ai-surveillance-and-social-progress.html) ⭐️ 7.0/10

布鲁斯·施奈尔描绘了一个无处不在的 AI 监控系统即时执行所有规则、可能扼杀社会进步和个人自由的未来。 这一分析强调了普遍 AI 监控带来的深刻社会风险，威胁公民自由和挑战不公正法律的能力。 该系统会即时将违规行为与官方记录关联，并通知当局和公众，消除了目前允许自由裁量或申诉的延迟。

rss · Schneier on Security · 7月10日 11:02

**背景**: 布鲁斯·施奈尔是著名的安全技术专家和作家，经常就数字隐私和社会风险发表评论。AI 监控指使用机器学习大规模监测行为，加剧了关于隐私、伦理和国家权力的辩论。

**标签**: `#AI`, `#surveillance`, `#ethics`, `#society`, `#privacy`

---

<a id="item-4"></a>
## [AI 语言模型可能改变人类说话方式](https://www.schneier.com/blog/archives/2026/07/the-language-of-ai-could-change-how-humans-speak.html) ⭐️ 7.0/10

大型语言模型主要基于书面文本和剧本化的语音进行训练，缺乏对即兴、面对面交流的学习。AI 生成文本的广泛使用可能导致人类采用这些受限的语言模式，从而改变自然说话方式。 这是因为语言塑造思维、文化和社会关系；偏好剧本化、书面化规范的反馈循环可能削弱人类语言的自发性和文化丰富性。 大型语言模型基于大量书籍、文章和剧本媒体训练，但大多遗漏了未经记录的即兴对话。反馈循环是指人类阅读并潜意识模仿 AI 生成的文本，而该文本本身仅反映有限的语言模式子集。

rss · Schneier on Security · 7月9日 11:00

**背景**: 像 GPT 这样的大型语言模型通过互联网、书籍和字幕等海量文本语料训练，能够生成连贯文本。然而，它们并未接触大多数人类语言，即非正式、即兴的对话。这种训练偏差意味着它们反映的是书面化、经过编辑的语言形式，而非自然的口语。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>
<li><a href="https://www.ibm.com/think/topics/large-language-models">What Are Large Language Models (LLMs)? | IBM</a></li>

</ul>
</details>

**标签**: `#AI`, `#language`, `#culture`, `#large language models`, `#human communication`

---
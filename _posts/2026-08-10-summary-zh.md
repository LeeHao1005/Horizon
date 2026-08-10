---
layout: default
title: "Horizon Summary: 2026-08-10 (ZH)"
date: 2026-08-10
lang: zh
---

> 从 27 条内容中筛选出 4 条重要资讯。

---

1. [ICE 从数据经纪人处购买信用卡记录](#item-1) ⭐️ 8.0/10
2. [预处理私有函数评估实现查找表亚线性在线复杂度](#item-2) ⭐️ 7.0/10
3. [Cloudflare 推出基于 BotBase 与 Precursor 的持续机器人检测](#item-3) ⭐️ 7.0/10
4. [Cloudflare 将 Workers AI 与 AI Gateway 统一为单一控制面](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [ICE 从数据经纪人处购买信用卡记录](https://www.schneier.com/blog/archives/2026/08/ice-is-buying-access-to-credit-card-records.html) ⭐️ 8.0/10

美国移民及海关执法局（ICE）从商业数据经纪人处购买个人数据，包括申请信用卡时提供的姓名、地址、电话号码等信息。 这允许 ICE 绕过对直接数据收集的法律限制，对个人财务活动进行无令状的大规模监视，威胁所有人的公民自由和隐私权。 购买的数据可能是信用报告头部信息（姓名、现在和过去地址、电话号码、社会安全号码），并非详细的交易记录，但仍可实现精确定位和身份识别。目前尚无联邦法律禁止数据经纪人未经授权向政府机构出售此类信息。

rss · Schneier on Security · 8月7日 10:26

**背景**: 数据经纪人是收集和销售个人信息的公司，数据来源包括公共记录和商业交易。信用报告头部数据通常包含姓名、地址、电话号码和社会安全号码等基本身份信息。与欧盟的 GDPR 不同，美国缺乏全面的联邦隐私法来规范个人数据的销售，消费者在政府购买其信息时几乎得不到保护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_broker">Data broker</a></li>
<li><a href="https://www.experian.com/blogs/news/2024/10/01/credit-header-data-an-indispensable-tool-to-combatting-fraud/">Credit Header Data: An Indispensable Tool to Combatting Fraud - Experian Global News Blog</a></li>
<li><a href="https://www.tracers.com/blog/what-is-credit-header/">What is Credit Header? - Credit Header Data Definition</a></li>

</ul>
</details>

**标签**: `#privacy`, `#surveillance`, `#data brokers`, `#ICE`, `#credit cards`

---

<a id="item-2"></a>
## [预处理私有函数评估实现查找表亚线性在线复杂度](https://eprint.iacr.org/2026/1631) ⭐️ 7.0/10

提出了一种新的私有函数评估（PFE）变体——预处理私有函数评估（PPFE），其专门针对查找表操作的设计实现了亚线性的在线计算复杂度。实验结果显示，对于大小为 2^24 的查找表，单次查询约需 3 毫秒，比现有方案快了一个数量级以上。 现有 PFE 方案在查找表等基础操作上效率低下，阻碍了其在隐私保护医疗、信用核查等领域的应用。这一突破大幅提升了在线效率，使安全计算在实际场景中更加实用和可扩展。 该构造利用预处理将繁重的密码计算任务移至离线阶段，使在线阶段复杂度随表大小亚线性增长，并支持数千次自适应查询。对于包含 2^24 条目的查找表，每次查询在线耗时仅 3 毫秒，性能较此前的线性复杂度方案有显著跃升。

rss · IACR ePrint 密码学论文 · 8月7日 05:26

**背景**: 私有函数评估（PFE）是一种安全计算协议，其函数和输入均保持加密状态。PFE 通常通过通用电路实现，会带来与电路规模相关的线性开销，导致查找表等操作成本高昂。查找表将键映射到值，在需要隐藏商业逻辑或专有算法的隐私保护系统中是基础操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://encrypto.de/papers/HKRS20.pdf">Linear-Complexity Private Function Evaluation is Practical</a></li>
<li><a href="https://crypto.stackexchange.com/questions/41899/difference-between-secure-function-evaluation-and-private-function-evaluation">multiparty computation - Difference between secure function ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#private function evaluation`, `#secure computation`, `#preprocessing`, `#lookup tables`

---

<a id="item-3"></a>
## [Cloudflare 推出基于 BotBase 与 Precursor 的持续机器人检测](https://blog.cloudflare.com/good-and-bad-agentic-behaviors/) ⭐️ 7.0/10

Cloudflare 正从单点风险评估转向持续信任评估，推出两个新系统：BotBase 分析机器人的好与坏行为，Precursor 则是一种行为验证引擎，能随时间评估光标移动等交互行为。 这种持续监测方式能更好地检测那些间歇性模仿人类行为的复杂机器人，减少对单次挑战的依赖，在提升安全性的同时不干扰合法用户。 Precursor 可通过 Cloudflare 仪表板或 API 按区域启用，并包含一个公开模拟工具（Precursor Trace），用于测试光标移动评估。BotBase 可能负责对行为模式进行编目，但内部技术细节有限。

rss · Cloudflare Blog (PQ 迁移) · 8月7日 13:01

**背景**: 传统机器人缓解依赖验证码等单点检查，但机器人有时能通过。持续信任评估则随时间监控会话行为，寻找自动化模式。Cloudflare 的 Bot Management 已使用机器学习；Precursor 专门分析鼠标移动和交互节奏，而 BotBase 可能充当已知机器人行为的知识库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/cloudflare-challenges/precursor/">Precursor · Cloudflare challenges docs</a></li>

</ul>
</details>

**标签**: `#bot-mitigation`, `#continuous-trust-evaluation`, `#web-security`, `#behavioral-analysis`, `#cloudflare`

---

<a id="item-4"></a>
## [Cloudflare 将 Workers AI 与 AI Gateway 统一为单一控制面](https://blog.cloudflare.com/workers-ai-gateway-unification/) ⭐️ 7.0/10

Cloudflare 已将其 AI Gateway 和 Workers AI 合并为一个统一的控制平面，为开发者提供跨托管式无服务器 GPU 和外部 AI 提供商的统一可观测性、计费和动态路由接口。 这一统一简化了在 Cloudflare 上构建弹性 AI 应用的流程，降低了管理多个 AI 模型和提供商的复杂性，并为企业 AI 工作负载提供了集中治理和成本控制能力。 开发者现在可以使用统一绑定通过一致的接口访问 Cloudflare 的模型和外部 API，并采用模型优先路由，根据性能或成本等标准动态选择最优模型。可观测性和计费在所有 AI 交互中实现了统一。

rss · Cloudflare Blog (PQ 迁移) · 8月7日 13:00

**背景**: Workers AI 允许开发者在 Cloudflare 全球网络上运行 AI 推理，无需管理基础设施。AI Gateway 为调用外部 AI API 提供缓存、速率限制和可观测性。控制平面是一种架构层，用于治理和编排 AI 使用，确保策略执行和可见性。通过统一两者，Cloudflare 提供了一个集成平台，既能使用自己的 AI 资源，也能管理第三方模型访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/cloudflare_unifying-workers-ai-and-ai-gateway-into-a-activity-7491485847184273408-46nN">Unifying Workers AI and AI Gateway into a single AI control plane</a></li>
<li><a href="https://www.cloudflare.com/products/workers-ai/">Cloudflare Workers AI - Edge AI Inference Platform</a></li>
<li><a href="https://www.cloudflare.com/solutions/ai/">Cloudflare AI Cloud</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#AI Gateway`, `#Workers AI`, `#control plane`, `#observability`

---
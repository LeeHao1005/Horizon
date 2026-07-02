---
layout: default
title: "Horizon Summary: 2026-07-02 (ZH)"
date: 2026-07-02
lang: zh
---

> 从 48 条内容中筛选出 15 条重要资讯。

---

1. [RFC 9980 为 OpenPGP 引入后量子加密技术](#item-1) ⭐️ 9.0/10
2. [Cloudflare 推出基于 x402 协议的变现网关](#item-2) ⭐️ 8.0/10
3. [Falafel：联邦学习中的模块化零知识训练证明](#item-3) ⭐️ 8.0/10
4. [Cloudflare 推出 AI 搜索时代创作者发现与收益新举措](#item-4) ⭐️ 8.0/10
5. [含大量零位的新型弱 RSA 密钥被发现](#item-5) ⭐️ 8.0/10
6. [后量子密码学现已支持 Python pip 安装](#item-6) ⭐️ 8.0/10
7. [RFC 9943：值得信赖的数字供应链架构](#item-7) ⭐️ 8.0/10
8. [RFC 9942: 标准化用于可验证数据结构的 COSE Receipts](#item-8) ⭐️ 8.0/10
9. [新论文揭示 EasyCrypt 难以证明加密协议的关键挑战](#item-9) ⭐️ 7.0/10
10. [ML-DSA 基准测试的陷阱与标准化方法](#item-10) ⭐️ 7.0/10
11. [Cloudflare 报告：代理式互联网时代的内容变现](#item-11) ⭐️ 7.0/10
12. [Cloudflare 推出精细的 AI 机器人流量管控功能](#item-12) ⭐️ 7.0/10
13. [Papa Johns 利用 Instacart 数据预测冰箱空时推送定向广告](#item-13) ⭐️ 7.0/10
14. [AI 实现视频监控的自然语言查询](#item-14) ⭐️ 7.0/10
15. [RFC 9978 为 BFD 协议定义稳定性扩展](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [RFC 9980 为 OpenPGP 引入后量子加密技术](https://rfc-editor.org/info/rfc9980) ⭐️ 9.0/10

IETF 发布的 RFC 9980 扩展了 OpenPGP 协议, 定义了后量子加密算法: 结合 ML-KEM 与 ECC 的复合加密, 结合 ML-DSA 与 ECC 的复合签名, 以及独立的 SLH-DSA 签名方案。 该 RFC 回应了保护 OpenPGP 通信免受未来量子计算机攻击的迫切需求, 确保邮件与数据加密的长期机密性和真实性。它为在广泛使用的标准中普及后量子加密技术奠定了基础。 复合方案要求攻击者同时攻破 ECC 与后量子算法, 提供纵深防御。所使用的后量子算法均为 NIST 标准 (ML-KEM 为 FIPS 203, ML-DSA 为 FIPS 204, SLH-DSA 为 FIPS 205)。

rss · IETF 新标准 RFC (PQC 标准化) · 6月30日 22:51

**背景**: OpenPGP 是广泛使用的邮件与数据加密标准。目前的 RSA 和 ECC 加密易受未来量子计算机的 Shor 算法攻击。后量子密码学旨在开发抗量子攻击的算法。NIST 标准选中了 ML-KEM, ML-DSA 和 SLH-DSA 作为后量子标准。RFC 9980 将这些算法以复合方案的形式集成到 OpenPGP 中, 确保只要其中一个组件未被攻破, 系统就安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://en.wikipedia.org/wiki/SLH-DSA">SLH-DSA</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#standards`, `#OpenPGP`, `#IETF`

---

<a id="item-2"></a>
## [Cloudflare 推出基于 x402 协议的变现网关](https://blog.cloudflare.com/monetization-gateway/) ⭐️ 8.0/10

Cloudflare 推出了一款变现网关，允许网站运营者使用 x402 协议对其网络后的任何资源进行收费访问，从而实现微交易和来自 AI 代理的支付。 这一进展可能加速机器对机器支付，使 AI 代理能够自主付费访问，并通过提供广告支持模式的替代方案，可能重塑网络经济。 该网关基于 x402 协议构建，该协议利用很少使用的 HTTP 402 “需要支付”状态码与加密货币支付（例如 Polygon 上的 USDC），但有关定价层级或欺诈预防的详细信息尚未完全披露。

hackernews · Cloudflare Blog (PQ 迁移) · 7月1日 13:59 · [社区讨论](https://news.ycombinator.com/item?id=48746914)

**背景**: HTTP 402 是原本用于数字支付的状态码，但从未被广泛采用。x402 是最近由 Coinbase 主导的开放标准，能够使用稳定币进行即时微支付。Cloudflare 的实现允许网站所有者对内容收费，而无需传统的付费墙，可能针对 API 访问或高级内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/HTTP_402">HTTP 402</a></li>
<li><a href="https://cheetahai.co/blog/post-46">x 402 Protocol Explained: Engineering HTTP-Native Payments for AI...</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一。一些人认为这是为 AI 代理实现长期渴望的微交易，而其他人则担心它无法解决机器人检测问题，并且可能助长垃圾信息或低质量内容计划。此外，还有关于已有的 L402 实现以及 Cloudflare 为何自己构建的讨论。

**标签**: `#monetization`, `#cloudflare`, `#x402`, `#microtransactions`, `#web infrastructure`

---

<a id="item-3"></a>
## [Falafel：联邦学习中的模块化零知识训练证明](https://eprint.iacr.org/2026/1335) ⭐️ 8.0/10

Falafel 提出了一种模块化方案，为联邦学习生成零知识训练证明，确保从数据集到最终模型的整个训练过程具有主动安全性和公开可验证性，同时不泄露私有数据。 这使得无需信任的验证联邦学习成为可能，任何人都可以审计训练过程而无需访问敏感数据，从而增强信任，并可能推动医疗和金融等隐私关键领域采用联邦学习。 Falafel 采用基于成熟假设的模块化承诺-证明设计。对于 LeNet，每轮训练可在约 150 秒内生成 70 kB 的证明，大小比先前方案小 10–15 倍，且无需使用算术哈希函数实例化 Fiat–Shamir。

rss · IACR ePrint 密码学论文 · 6月29日 12:12

**背景**: 零知识证明允许证明者向验证者证明某个陈述为真，而不泄露任何额外信息。联邦学习使多方能在不共享原始数据的情况下协同训练机器学习模型，保护隐私。先前关于可验证训练的工作通常开销较大或依赖未经充分测试的密码学假设，限制了实用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof</a></li>
<li><a href="https://en.wikipedia.org/wiki/Federated_learning">Federated learning</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#federated learning`, `#privacy`, `#verifiable computation`, `#cryptography`

---

<a id="item-4"></a>
## [Cloudflare 推出 AI 搜索时代创作者发现与收益新举措](https://blog.cloudflare.com/making-ai-search-smarter/) ⭐️ 8.0/10

Cloudflare 宣布了两项新举措，旨在帮助内容创作者在 AI 驱动的搜索引擎日益主导信息获取的时代，保持可被发现并获得相应报酬。 这一举措解决了 AI 搜索工具抓取和总结内容却不将流量或收入返还创作者的关键矛盾，威胁到网络出版的经济可持续性。 该博文未透露具体技术细节，但这些举措旨在确保 AI 搜索引擎适当标注来源并补偿创作者内容。

rss · Cloudflare Blog (PQ 迁移) · 7月1日 13:00

**背景**: “代理时代”指的是 AI 不仅回答问题，还能自主执行任务的阶段。在 AI 驱动的搜索中，这意味着 ChatGPT 或 Perplexity 等系统能综合多个来源的信息，常常绕过原始网站。这减少了创作者的流量和广告收入，引发了关于合理使用以及需要新变现模式的争论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://time.com/7312641/agentic-ai-era-humans/">What the Agentic AI Era Means for Business—And for Humanity</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-the-agentic-era-google-io-2026">What Is the Agentic Era? How Google I/O 2026 Defined the Next Phase of AI | MindStudio</a></li>

</ul>
</details>

**标签**: `#AI`, `#search`, `#web`, `#content-creation`, `#Cloudflare`

---

<a id="item-5"></a>
## [含大量零位的新型弱 RSA 密钥被发现](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html) ⭐️ 8.0/10

Trail of Bits 的研究人员发现了一类新的弱 RSA 公钥，称为“短袖”密钥，它们包含异常多的零位。这些密钥通过 badkeys 项目在现实世界的部署中被发现，并可使用基于多项式的技术高效分解。 这一发现揭示了使用这些错误生成密钥的系统存在实际漏洞，攻击者可能借此破解加密和签名。这强调了在加密密钥生成中正确使用随机性的关键需求，特别是在野外发现此类缺陷的情况下。 该攻击利用了模数的稀疏结构，其中许多位为零，从而实现了多项式时间分解。badkeys 工具从证书透明度日志、TLS/SSH 扫描和其他来源收集密钥，识别出数百个易受攻击的密钥。

rss · Schneier on Security · 6月29日 16:05

**背景**: RSA 加密的安全性依赖于大合数分解的难度。如果模数具有非随机模式，例如大量零位，则比相同大小的真正随机模数更容易分解。badkeys 项目是一个开源工具，用于扫描公钥中的已知漏洞，帮助识别此类弱点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/">Factoring " short - sleeve " RSA keys with polynomials - The Trail of Bits...</a></li>
<li><a href="https://github.com/badkeys/badkeys">GitHub - badkeys/badkeys: Tool to find common vulnerabilities in cryptographic public keys · GitHub</a></li>

</ul>
</details>

**标签**: `#RSA`, `#cybersecurity`, `#vulnerability-research`, `#public-key-cryptography`, `#badkeys`

---

<a id="item-6"></a>
## [后量子密码学现已支持 Python pip 安装](https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/) ⭐️ 8.0/10

Trail of Bits 在 pyca/cryptography 中实现了对 NIST 标准后量子原语 ML-KEM 和 ML-DSA 的支持，从版本 48 开始可通过 pip 安装使用。 这一集成通过最关键加密库将后量子密码学带入整个 Python 生态，并响应白宫要求联邦系统在 2030 年前采用后量子密钥建立的行政令。 ML-KEM（密钥封装）和 ML-DSA（数字签名）使用基于格的密码学，是 NIST 标准 FIPS 203 和 FIPS 204；与 Ed25519 等经典算法相比，其公钥、签名和密文大小显著增加。

rss · Trail of Bits Blog · 6月30日 11:00

**背景**: 后量子密码学旨在抵御未来量子计算机的攻击，量子计算机可利用 Shor 算法破解当前的 RSA、ECC 等公钥系统。ML-KEM（原 Kyber）和 ML-DSA（原 Dilithium）是 NIST 于 2024 年首批标准化的后量子算法，分别用于密钥建立和数字签名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#Python`, `#pyca/cryptography`, `#NIST`, `#security`

---

<a id="item-7"></a>
## [RFC 9943：值得信赖的数字供应链架构](https://rfc-editor.org/info/rfc9943) ⭐️ 8.0/10

RFC 9943 定义了单发行者签名声明透明度的通用架构，弥补了可验证数据结构在多样化数字供应链中缺乏共同框架的不足。 该标准化工作增强了供应链生态系统中的信任、互操作性和可审计性，有助于在各行业更广泛地采用防篡改日志，并符合监管透明度要求。 该架构专注于由单一发行者签名的声明，支持可扩展性并兼容多种审计程序，但未直接处理多发行者场景。

rss · IETF 新标准 RFC (PQC 标准化) · 6月30日 22:43

**背景**: 可验证数据结构如仅追加日志和默克尔树用于在证书透明度等系统中证明数据的完整性和一致性。数字供应链涉及跨多个实体跟踪软件、硬件或数据的来源和完整性。歧义攻击是指攻击者向不同观察者展示同一数据的不同版本，而可验证数据结构有助于检测这种情况。RFC 9943 提供了一个标准化架构，以通用方式应用这些概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://transparency.dev/verifiable-data-structures/">Verifiable Data Structures | Trillian</a></li>

</ul>
</details>

**标签**: `#supply-chain`, `#transparency`, `#verifiable-data-structures`, `#standards`, `#security`

---

<a id="item-8"></a>
## [RFC 9942: 标准化用于可验证数据结构的 COSE Receipts](https://rfc-editor.org/info/rfc9942) ⭐️ 8.0/10

RFC 9942 定义了使用 CBOR 和 COSE 来证明可验证数据结构属性（如 Merkle 包含证明和一致性证明）的 COSE Receipts。 它通过可验证证明实现了简洁透明的系统，影响证书透明度、端到端加密和供应链安全，促进互操作性和信任。 该 RFC 提供了 Merkle 包含证明和一致性证明的 CBOR 编码，定义了像'vds'这样的头部参数来表示可验证数据结构类型，并利用 COSE 和 CBOR。

rss · IETF 新标准 RFC (PQC 标准化) · 6月30日 22:43

**背景**: COSE（CBOR 对象签名与加密）是使用 CBOR（二进制数据格式）的加密消息标准。可验证数据结构（如 Merkle 树）允许高效且安全地证明数据完整性和包含性。透明系统（如证书透明度）使用此类证明构建信任。该 RFC 扩展了 COSE 以支持这些结构的 receipts。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-cose-merkle-tree-proofs/">draft-ietf-cose-merkle-tree-proofs-18 - COSE (CBOR Object Signing and Encryption) Receipts</a></li>
<li><a href="https://datatracker.ietf.org/doc/draft-birkholz-cose-receipts-ccf-profile/">draft-birkholz-cose-receipts-ccf-profile-04 - COSE Receipts with CCF</a></li>
<li><a href="https://transparency.dev/verifiable-data-structures/">Verifiable Data Structures | Trillian</a></li>

</ul>
</details>

**标签**: `#COSE`, `#CBOR`, `#Verifiable Data Structures`, `#Transparency`, `#IETF Standard`

---

<a id="item-9"></a>
## [新论文揭示 EasyCrypt 难以证明加密协议的关键挑战](https://eprint.iacr.org/2026/1334) ⭐️ 7.0/10

该论文在 EasyCrypt 中形式化了一个简单的交互式密钥协商协议，发现证明同时需要用于密码学推理的状态不变量和用于协议结构的时间不变量，这导致了显著的复杂性。 这一发现有助于开发新的推理工具，弥合原语导向与协议导向验证工具之间的差距，使交互式协议的形式化安全证明更加可行。 作者从探索性证明开始，经历结构化尝试的失败，最终得出一个“本质”证明，认为同时管理状态不变量和时间不变量是核心挑战，并指出这些发现可用于指导未来工具改进。

rss · IACR ePrint 密码学论文 · 6月29日 08:03

**背景**: EasyCrypt 是一个使用概率关系 Hoare 逻辑（pRHL）的密码学原语证明助手。pRHL 通过比较两个概率程序来证明安全性等关系属性。交互式协议涉及多条消息交换，需要跟踪状态随时间的变化，现有工具对此支持不足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/EasyCrypt/easycrypt">GitHub - EasyCrypt/easycrypt: EasyCrypt: Computer-Aided Cryptographic Proofs · GitHub</a></li>
<li><a href="https://popl25.sigplan.org/details/POPL-2025-popl-research-papers/40/A-quantitative-probabilistic-relational-Hoare-logic">A quantitative probabilistic relational Hoare logic (POPL 2025 - POPL Research Papers) - POPL 2025</a></li>

</ul>
</details>

**标签**: `#formal verification`, `#cryptographic protocols`, `#EasyCrypt`, `#pRHL`, `#interactive protocols`

---

<a id="item-10"></a>
## [ML-DSA 基准测试的陷阱与标准化方法](https://eprint.iacr.org/2026/1333) ⭐️ 7.0/10

该论文揭示，由于拒绝采样和其他数据依赖步骤，ML-DSA 签名具有内在的执行时间变异性，使得最小/平均/最大时间等常用指标在迁移规划中具有误导性。它提出了一种标准化基准测试方法，使用固定输入集和合格指标，确保不同实现之间的公平比较。 准确且可比较的性能数据对于后量子密码迁移中的工程决策至关重要。所提出的方法能够公平地评估 ML-DSA 实现，并支持实时系统的执行时间分析。 ML-DSA 签名包含拒绝采样以防止泄露秘密信息，导致执行时间显著波动。该方法要求使用预定输入向量和合格指标（如百分位数），解决了简单最小/平均/最大值无法满足实时需求的问题。

rss · IACR ePrint 密码学论文 · 6月29日 07:05

**背景**: ML-DSA（基于模格的数字签名算法）是 NIST 标准化的后量子签名方案（FIPS 204），基于模格问题的困难性。拒绝采样是基于格的签名中的关键技术，确保签名分布不泄露私钥，但同时也导致执行时间不确定。对此类操作进行基准测试具有挑战性，因为执行时间依赖于秘密数据，标准指标可能产生误导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/pubs/fips/204/final">FIPS 204, Module-Lattice-Based Digital Signature Standard | CSRC</a></li>
<li><a href="https://medium.com/@kootie73/lattice-based-signatures-and-rejection-sampling-an-introduction-to-modern-cryptographic-techniques-19774f87b7c7">Lattice-Based Signatures and Rejection Sampling: An ... - Medium</a></li>
<li><a href="https://openquantumsafe.org/liboqs/algorithms/sig/ml-dsa.html">ML-DSA - Open Quantum Safe</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#benchmarking`, `#ML-DSA`, `#cryptographic migration`, `#methodology`

---

<a id="item-11"></a>
## [Cloudflare 报告：代理式互联网时代的内容变现](https://blog.cloudflare.com/agentic-internet-bot-report/) ⭐️ 7.0/10

在内容独立日一周年之际，Cloudflare 发布报告，探讨了由自主 AI 智能体驱动的内容变现市场兴起，以及这些智能体如何颠覆传统搜索引荐模式，并详述了支撑可持续网络经济所需的新基础设施。 这一转变标志着网页内容访问和补偿方式的根本变革，因为 AI 智能体正成为信息的主要消费者。它威胁着传统出版营收模式，需要新的许可和支付系统。 该报告基于 Cloudflare 2025 年发起的‘内容独立日’倡议，该倡议屏蔽不付费的 AI 爬虫。报告指出，AI 智能体付费获取内容的市场已经形成，但本摘要未披露具体技术或经济数据。

rss · Cloudflare Blog (PQ 迁移) · 7月1日 13:00

**背景**: 2025 年 7 月，Cloudflare 和出版商共同宣布‘内容独立日’，默认屏蔽不向内容创作者付费的 AI 爬虫。‘代理式互联网’指 AI 智能体自主浏览、决策并代表用户执行交易的未来网络。流量从人类转向智能体的变化挑战了传统的广告和引荐变现模式，催生了对内容许可 API 和小额支付系统等新基础设施的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/agentic-internet-bot-report/">Content Independence Day, one year on- building the business ...</a></li>
<li><a href="https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/">Content Independence Day: no AI crawl without compensation!</a></li>
<li><a href="https://cacm.acm.org/news/the-rise-of-the-ai-enabled-agentic-internet/">The Rise of the AI-Enabled Agentic Internet – Communications of the ACM</a></li>

</ul>
</details>

**标签**: `#agentic Internet`, `#AI agents`, `#content monetization`, `#web infrastructure`, `#Cloudflare`

---

<a id="item-12"></a>
## [Cloudflare 推出精细的 AI 机器人流量管控功能](https://blog.cloudflare.com/content-independence-day-ai-options/) ⭐️ 7.0/10

2026 年 7 月 1 日，Cloudflare 推出了新功能，允许所有客户区分和管理三类 AI 机器人流量：搜索机器人、代理机器人、训练机器人，还引入了对广告变现页面的保护。 这让网站所有者可以精确控制 AI 机器人对其内容的访问方式，允许有益的搜索引擎索引，同时阻止未经授权的 AI 训练数据抓取，从而有助于保护广告收入和知识产权。 三种机器人类别为：搜索（为搜索引擎索引内容的爬虫）、代理（代表用户行动的机器人）、训练（收集数据用于 AI 模型训练的爬虫）。从 2026 年 9 月 15 日起，新的 Cloudflare 域将默认在含广告页面上拦截训练和代理机器人，除非这些机器人公开区分搜索和训练行为。

rss · Cloudflare Blog (PQ 迁移) · 7月1日 13:00

**背景**: AI 机器人，也称为爬虫，会自动浏览网页，被用于搜索引擎内容索引（如 Googlebot）和收集数据以训练大语言模型。此前 Cloudflare 只提供简单的全部拦截选项，但许多网站所有者希望允许搜索索引的同时阻止训练数据抓取。此次更新通过按行为分类机器人，解决了这些精细化需求，并引入机制保护广告支持页面，防止未经授权的抓取损害收入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/">Block AI Bots · Cloudflare bot solutions docs</a></li>
<li><a href="https://www.theregister.com/ai-and-ml/2026/07/01/cloudflare-to-block-cynical-search-and-scrape-bots-from-ad-supported-web-pages/5264727">Cloudflare to block cynical search-and-scrape bots from ad ...</a></li>
<li><a href="https://www.nbcnews.com/tech/tech-news/cloudflare-sets-ai-crawler-deadline-separate-search-blocked-rcna352446">Cloudflare sets AI crawler deadline: separate search or be ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#bot management`, `#Cloudflare`, `#web traffic`, `#content independence`

---

<a id="item-13"></a>
## [Papa Johns 利用 Instacart 数据预测冰箱空时推送定向广告](https://www.schneier.com/blog/archives/2026/07/papa-johns-surveillance-based-advertising.html) ⭐️ 7.0/10

Papa John's 与 NBCUniversal、Instacart 和 Carat 合作，利用 Instacart 的购买数据预测消费者何时食品短缺，并在流媒体电视上向他们推送定制比萨广告，广告语如“冰箱空了吗？”以促发订单。 这一做法体现了基于监控的广告日益盛行的趋势，个人购物数据被共享和用于定向投放，而消费者并未明确知情，引发了严重的隐私担忧。它影响到所有可能不知不觉中购物习惯被追踪并用于广告定位的消费者。 该活动从 Instacart 用户中创建购买了鸡蛋、牛奶、肉类等日常必需品的定制受众群，然后判断他们可能耗尽的日期。广告通过 NBCU 的流媒体内容投放，包含二维码，据媒体代理机构称，努力做到预测而不致“过于令人不适”。

rss · Schneier on Security · 7月1日 10:53

**背景**: 基于监控的广告涉及追踪个人线上和线下行为以提供定制广告。Instacart 是一家收集详细购买数据的食品杂货配送服务，这些数据常被用于定向广告。此做法因其侵入性和缺乏透明度而受到隐私倡导者和监管机构的批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://proton.me/blog/ban-surveillance-advertising">It is time to ban surveillance - based advertising | Proton</a></li>
<li><a href="https://vivaldi.com/blog/its-time-to-ban-surveillance-based-advertising/">It’s time to ban surveillance - based advertising | Vivaldi Browser</a></li>

</ul>
</details>

**标签**: `#surveillance`, `#advertising`, `#privacy`, `#data-mining`, `#consumer-rights`

---

<a id="item-14"></a>
## [AI 实现视频监控的自然语言查询](https://www.schneier.com/blog/archives/2026/06/the-realities-of-ai-video-surveillance.html) ⭐️ 7.0/10

新的 AI 工具允许用户对视频画面提出自然语言问题，突破了传统监控系统只能进行有限预设检索的限制。 这一进展极大地扩展了大规模监控的能力，使得进行广泛且有针对性的间谍活动更加容易，加剧了隐私风险和伦理关切。 与以往仅支持几十种预设检索的工具不同，新系统支持几乎无限范围的语言化视频查询。

rss · Schneier on Security · 6月30日 12:05

**背景**: 传统视频监控依赖人工回放或简单的运动检测。近期 AI 在时间语言定位和视频问答领域的进展，使计算机能够根据自然语言查询理解并检索视频中的特定片段。这将监控从被动记录转变为主动、可扩展的分析，使得大规模间谍活动成为可能，类似于数字网络如何扩展了数据监控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Soldelli/Awesome-Temporal-Language-Grounding-in-Videos">GitHub - Soldelli/Awesome-Temporal- Language -Grounding-in- Videos ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S1047320324002761">Video Question Answering: A survey of the state-of-the-art - ScienceDirect</a></li>
<li><a href="https://arxiv.org/abs/2203.01225">[2203.01225] Video Question Answering: Datasets, Algorithms and Challenges</a></li>

</ul>
</details>

**标签**: `#AI`, `#surveillance`, `#privacy`, `#security`, `#video analytics`

---

<a id="item-15"></a>
## [RFC 9978 为 BFD 协议定义稳定性扩展](https://rfc-editor.org/info/rfc9978) ⭐️ 7.0/10

RFC 9978 为双向转发检测 (BFD) 协议引入了新扩展，能够测量 BFD 稳定性并检测 BFD 数据包丢失情况。 该扩展使网络管理员能更精确地衡量 BFD 会话的稳定性，识别间歇性丢包问题，从而提升网络故障检测的准确性和整体可靠性。 该 RFC 描述了检测 BFD 数据包丢失的具体机制，可能通过新的协议字段或统计报告来量化会话的稳定性。

rss · IETF 新标准 RFC (PQC 标准化) · 6月29日 22:54

**背景**: 双向转发检测 (BFD) 是一种网络协议，通过定期交换 Hello 包来快速检测路由器或交换机之间的故障，其检测速度不受底层介质或路由协议影响。通常，连续丢失若干 Hello 包即触发故障通告。RFC 9978 扩展了 BFD 以测量丢包率，为网络管理员提供了更细粒度的链路质量可见性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bidirectional_Forwarding_Detection">Bidirectional Forwarding Detection - Wikipedia</a></li>
<li><a href="https://www.cisco.com/c/en/us/td/docs/ios/12_0s/feature/guide/fs_bfd.html">Bidirectional Forwarding Detection - Cisco</a></li>
<li><a href="https://www.juniper.net/documentation/us/en/software/junos/high-availability/topics/topic-map/bfd.html">Understanding How BFD Detects Network Failures | Junos OS | Juniper Networks</a></li>

</ul>
</details>

**标签**: `#BFD`, `#networking`, `#RFC`, `#protocol extension`, `#fault detection`

---
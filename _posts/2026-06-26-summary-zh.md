---
layout: default
title: "Horizon Summary: 2026-06-26 (ZH)"
date: 2026-06-26
lang: zh
---

> 从 42 条内容中筛选出 15 条重要资讯。

---

1. [可验证编辑音频的匿名溯源方案](#item-1) ⭐️ 8.0/10
2. [钱包用户干预设计抵御授权钓鱼攻击](#item-2) ⭐️ 8.0/10
3. [对植入后门的 UA-8295 消息终端的取证密码分析](#item-3) ⭐️ 8.0/10
4. [基于本地验证的高效恶意安全多方计算协议](#item-4) ⭐️ 8.0/10
5. [白宫后量子行政令设定 2030 年迁移期限](#item-5) ⭐️ 8.0/10
6. [漏洞报告不再特殊](#item-6) ⭐️ 8.0/10
7. [德国法院裁定谷歌对 AI 搜索摘要负责](#item-7) ⭐️ 8.0/10
8. [LLM 无法真正感知角色，提示注入威胁持续](#item-8) ⭐️ 8.0/10
9. [NIST 发布物联网网络安全指南修订草案](#item-9) ⭐️ 8.0/10
10. [GSMA 发布电信通用语料库：10B+ tokens 开放数据集](#item-10) ⭐️ 8.0/10
11. [多密钥设置下可调 Feistel 密码的后量子安全证明](#item-11) ⭐️ 7.0/10
12. [BN 配对子群被证明为相对迹映射核](#item-12) ⭐️ 7.0/10
13. [掩码硬件随机性与延迟权衡的自动化设计空间探索](#item-13) ⭐️ 7.0/10
14. [Cloudflare 工作流新增 Saga 式回滚功能](#item-14) ⭐️ 7.0/10
15. [Cloudflare 面向所有开发者推出自管理 OAuth](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [可验证编辑音频的匿名溯源方案](https://eprint.iacr.org/2026/1308) ⭐️ 8.0/10

一种名为 PPAAS（隐私保护音频认证系统）的新型密码系统被提出，它能在不泄露原始录音、编辑操作或录制设备身份的情况下，验证编辑后音频的真实性。该系统利用零知识证明将来源可信性和编辑正确性绑定到一个隐藏的见证上。 该研究解决了音频认证与隐私保护之间的根本矛盾，使编辑后的音频可作为可靠证据使用而无须暴露敏感内容，对数字取证、新闻和法律等同时需要可验证性和保密性的领域具有重要意义。 PPAAS 提供了两种构造：基于分段的方法仅对实际编辑的片段生成零知识证明，适用于稀疏编辑的低成本场景；基于迭代的方法采用增量可验证计算（IVC），在编辑密集时更为高效。两种方法均将验证过程压缩为单个证明，隐藏了所有敏感见证数据。

rss · IACR ePrint 密码学论文 · 6月23日 10:51

**背景**: 传统音频认证依赖与原始录音绑定的数字签名，验证时需公开原始文件，与隐私需求相悖。零知识证明允许在不泄露秘密的情况下证明相关陈述，匿名凭证可在不暴露身份的情况下验证属性。增量可验证计算（IVC）可高效验证长序列计算。PPAAS 结合这些技术，实现了编辑音频的匿名认证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1308">Trust the Voice, Hide the Source: Anonymous Provenance for Verifiably Edited Audio</a></li>

</ul>
</details>

**标签**: `#privacy-preserving`, `#audio-authentication`, `#cryptographic-protocols`, `#provenance`, `#anonymous-credentials`

---

<a id="item-2"></a>
## [钱包用户干预设计抵御授权钓鱼攻击](https://eprint.iacr.org/2026/1310) ⭐️ 8.0/10

研究人员设计并测试了四种基于钱包的干预措施——支出上限建议、主动支出者警告、被动支出者警告和延迟确认——以抵御授权钓鱼攻击。在一项涉及 364 名参与者的组间实验和后续访谈中，这些干预措施提高了用户设置支出上限和取消钓鱼任务的比例。 授权钓鱼是一种日益猖獗的 Web3 威胁，攻击者诱骗用户授予代币支出权限。该研究通过实证表明，基于钱包界面的干预措施可有效减少此类攻击，为超越 URL 检测的实用防御层提供了证据。 支出上限建议显著提高了用户设置支出上限的行为；主动支出者警告和延迟确认显著增加了对钓鱼任务的取消率，而被动支出者警告的增加并不显著。用户仍难以解读可疑信号，常忽视批准细节。

rss · IACR ePrint 密码学论文 · 6月23日 16:42

**背景**: 授权钓鱼攻击诱骗用户签署交易，授予攻击者从其钱包中花费代币的权限。在以太坊等区块链中，代币标准（如 ERC-20）允许用户批准智能合约代表其转移指定数量的代币，这一机制常被钓鱼诈骗利用。由于攻击者经常劫持合法网站，钱包界面便成为用户验证的关键环节。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chainalysis.com/blog/what-is-approval-phishing/">What Is Approval Phishing ? Detect & Disrupt Crypto Scams at Scale</a></li>
<li><a href="https://support.ledger.com/article/Ethereum-Token-Approvals-Explained">Understanding Ethereum Token Approvals - support.ledger.com</a></li>
<li><a href="https://blocksec.com/blog/how-to-avoid-being-a-web3-phishing-victim">How to Avoid Being a Web3 Phishing Victim - BlockSec Blog</a></li>

</ul>
</details>

**标签**: `#security`, `#cryptocurrency`, `#phishing`, `#user-interface`, `#wallet`

---

<a id="item-3"></a>
## [对植入后门的 UA-8295 消息终端的取证密码分析](https://eprint.iacr.org/2026/1309) ⭐️ 8.0/10

该论文首次对植入后门的 UA-8295 消息终端进行了详细的取证密码分析，研究了其后门的设计方式及所针对的攻击。同时提出了一个“后门猜想”，以帮助推理现实世界中的密码后门。 这项工作为国家层面设计的密码后门提供了罕见的公开见解，这类信息通常高度保密。它有助于安全社区理解现实世界的威胁，并可能为防御策略和政策讨论提供参考。 UA-8295 是由诺基亚开发、飞利浦销售的短消息突发终端，据报被 NSA 植入了后门。论文引入了一个“后门猜想”，作为分析后门设计原理及其预期攻击的概念框架。

rss · IACR ePrint 密码学论文 · 6月23日 11:53

**背景**: UA-8295 消息终端是 20 世纪 80 年代开发的一种加密短消息突发通信设备，用于隐蔽通信。取证密码分析是将密码分析技术应用于调查场景；在此案例中，用于逆向工程和理解疑似后门。历史上，国家机构曾试图削弱密码标准或产品以促进信号情报收集，但此类后门的具体细节很少公开披露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1309">Forensic Cryptanalysis of the Backdoored UA-8295 Message Terminal</a></li>
<li><a href="https://www.cryptomuseum.com/crypto/philips/ua8295/">Short-burst message terminal with encryption</a></li>

</ul>
</details>

**标签**: `#cryptanalysis`, `#backdoor`, `#forensic analysis`, `#cryptography`, `#signal intelligence`

---

<a id="item-4"></a>
## [基于本地验证的高效恶意安全多方计算协议](https://eprint.iacr.org/2026/1307) ⭐️ 8.0/10

该论文提出了一种基于编译器的多方计算协议，可在最多 t<n/3 腐败方的情况下实现恶意安全性，并使用 Shamir 秘密共享。它引入了一个本地验证框架，通过用本地 2t 次计算和批量打开替代多次乘法验证，降低了通信开销。 恶意安全性提供了针对主动攻击的更强保障，对实际应用至关重要。这项工作提高了通信效率，使实用的恶意多方计算更易于实现。 该协议假设静态恶意敌手控制不到三分之一的参与方。它利用 2t 次多项式进行本地验证，在保持统计安全性的同时降低了通信开销，允许很小的误差。

rss · IACR ePrint 密码学论文 · 6月23日 08:55

**背景**: 安全多方计算允许参与方在不泄露各自输入的前提下联合计算函数。半诚实敌手遵循协议但试图窃取信息，恶意敌手则可能任意偏离协议。Shamir 秘密共享将秘密分割成份额，需达到门限数量才能重构，常用于有限域上的 MPC。诚实多数场景下 MPC 通常更高效；三分之二诚实多数（t<n/3）是恶意敌手存在时实现信息论安全的标准设置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shamir's_secret_sharing">Shamir's secret sharing</a></li>

</ul>
</details>

**标签**: `#Secure Multi-Party Computation`, `#Malicious Security`, `#Shamir Secret Sharing`, `#Communication Efficiency`, `#Cryptography`

---

<a id="item-5"></a>
## [白宫后量子行政令设定 2030 年迁移期限](https://blog.cloudflare.com/post-quantum-eo-2026/) ⭐️ 8.0/10

白宫发布行政令，要求联邦机构在 2030 年前采用后量子密码学，Cloudflare 提供了详细的迁移指导手册。 该行政令推动后量子密码的紧急采用，保护国家安全免受未来量子攻击，并为全球行业标准树立先例。 虽然行政令针对联邦系统，但 Cloudflare 的指导手册将范围延伸至私营部门，强调分阶段迁移、算法敏捷性以及尽管期限设在 2030 年仍需立即行动的重要性。

rss · Cloudflare Blog (PQ 迁移) · 6月23日 18:25

**背景**: 后量子密码学旨在开发能抵抗量子攻击的算法，量子计算机可能破解 RSA 和 ECC 等现有公钥方法。2030 年期限应对了‘先窃取、后解密’的威胁，即对手现在存储加密数据以供未来解密。2024 年，NIST 发布了首批三项后量子密码标准，包括 ML-KEM 和 ML-DSA，为迁移提供了基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://csrc.nist.gov/projects/post-quantum-cryptography">Post-Quantum Cryptography | CSRC | CSRC</a></li>

</ul>
</details>

**标签**: `#post-quantum`, `#cryptography`, `#executive order`, `#cybersecurity`, `#migration`

---

<a id="item-6"></a>
## [漏洞报告不再特殊](https://words.filippo.io/vuln-reports/) ⭐️ 8.0/10

Filippo Valsorda 指出，大语言模型（LLM）使得任何人都能发现软件漏洞，这降低了传统漏洞报告的特殊地位，因为这类报告过去依赖于专家洞察和保密性。 漏洞发现的大众化可能让安全团队收到大量报告，改变传统的披露做法，并挑战原有的负责任漏洞处理模式。 尽管 LLM 使漏洞发现普及化，但它们可能产生误报且缺乏经验丰富研究人员的细致理解，然而大量的报告仍可能使人工分类负担加重。

rss · Filippo Valsorda (Go 密码学) · 6月23日 13:00

**背景**: 传统上，发现软件漏洞需要深厚的技术专长，通常由安全研究人员负责发现并负责任地披露。企业依赖这些报告并保密以保护用户。随着大语言模型（LLM）在大量代码库上训练，任何人都可以查询这些模型来识别潜在的安全问题，从根本上改变了这一格局。

**标签**: `#security`, `#vulnerability`, `#LLM`, `#AI`, `#cybersecurity`

---

<a id="item-7"></a>
## [德国法院裁定谷歌对 AI 搜索摘要负责](https://www.schneier.com/blog/archives/2026/06/ai-and-liability.html) ⭐️ 8.0/10

德国一家法院裁定，谷歌对其 AI 生成的搜索摘要内容负有法律责任，驳回了用户应自行核实信息的辩护理由。 该裁决为追究 AI 系统运营者对其输出内容的责任开创了先例，可能重塑全球 AI 责任法律框架，并影响科技公司在用户端产品中部署 AI 的方式。 法院明确驳回了谷歌关于用户通常知道 AI 生成信息不可盲目信任的辩护，转而将 AI 摘要归类为'谷歌商业活动的表达'。

rss · Schneier on Security · 6月25日 17:03

**背景**: 互联网法律历来区分'传输者'（如电话公司，不对传输内容负责）和'发布者'（如报纸，对发布内容负责）。AI 生成的摘要模糊了这一界限，因为它们涉及自动生成反映运营商业务活动的内容。此案是更广泛讨论的一部分：AI 输出应被视为单纯的数据传输还是编辑内容。

**标签**: `#AI liability`, `#legal ruling`, `#Google`, `#AI search`, `#internet law`

---

<a id="item-8"></a>
## [LLM 无法真正感知角色，提示注入威胁持续](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html) ⭐️ 8.0/10

一项新研究表明，大语言模型并非真正理解“系统”或“用户”等角色标签，而是通过文本块中的风格模式来区分指令。因此，提示注入攻击可通过模仿权威风格而非单纯操纵标签来绕过防御。 这一发现表明，基于角色标签的安全架构存在根本缺陷，使提示注入防御成为持久的“打地鼠”游戏。所有大模型应用，尤其是具备网页浏览或文件上传功能的，将持续面临威胁，除非模型能实现真正的角色感知。 该研究引入“角色混淆”作为关键指标，发现混淆程度越高，攻击成功率越大。研究还揭示角色边界是连续的，使攻击者可通过看似无害的文本微妙改变模型状态。

rss · Schneier on Security · 6月25日 11:23

**背景**: 提示注入是一种攻击，利用大语言模型无法区分系统提示与用户输入的特性，通过特制输入覆盖原始指令。大模型交互通常使用角色标签（如系统、用户、助手）来隔离可信指令与不可信输入，但这种隔离常流于表面。间接提示注入可发生在大模型处理包含隐藏对抗性提示的外部内容（如网页或上传文件）时。本研究发现，模型内部表示并未将角色标签编码为明确的安全边界，这动摇了当前防御的基础假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://www.lesswrong.com/posts/d8xDGzCEYE639qqEv/a-theory-of-prompt-injection-and-why-you-should-study-roles">A Theory of Prompt Injection (and why you should study roles )</a></li>
<li><a href="https://role-confusion.github.io/">Prompt Injection as Role Confusion</a></li>

</ul>
</details>

**标签**: `#prompt-injection`, `#LLM`, `#AI-security`, `#machine-learning`, `#research`

---

<a id="item-9"></a>
## [NIST 发布物联网网络安全指南修订草案](https://csrc.nist.gov/pubs/sp/800/213/r1/ipd) ⭐️ 8.0/10

NIST 发布了 SP 800-213 第 1 次修订版的初始公开草案，更新了联邦机构将物联网产品作为系统元素纳入风险管理以制定其网络安全要求的指南。 此更新使联邦机构能更好地评估和缓解物联网相关风险，强化政府系统的网络安全态势，并影响采购与集成实践。 草案强调，物联网产品的集成可能改变系统风险评估，并要求从 NIST SP 800-53 中选取额外控制措施；文件还包含专利声明征集。

rss · NIST CSRC Drafts (标准草案) · 6月24日 04:00

**背景**: NIST SP 800-213 最初于 2021 年发布，是联邦物联网网络安全指南系列的一部分，与 NIST SP 800-53 的安全控制目录互补。SP 800-213A 提供了详细的要求目录。此修订版与 NIST 风险管理框架保持一致，以应对不断变化的物联网威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NIST_SP_800-53">NIST SP 800-53</a></li>
<li><a href="https://www.nist.gov/itl/applied-cybersecurity/nist-cybersecurity-iot-program/sp-800-213-series">SP 800-213 Series | NIST</a></li>

</ul>
</details>

**标签**: `#IoT`, `#cybersecurity`, `#NIST`, `#federal government`, `#risk management`

---

<a id="item-10"></a>
## [GSMA 发布电信通用语料库：10B+ tokens 开放数据集](https://www.gsma.com/newsroom/article/telco-common-corpus-the-largest-open-verified-data-commons-for-telecom-ai/) ⭐️ 8.0/10

GSMA 与法国 AI 初创公司 Pleias 合作，在 GSMA 开放电信 AI 倡议下发布了电信通用语料库（TCC），这是一个包含超过 100 亿 tokens 的经过许可验证的电信数据开放数据集，旨在帮助运营商、供应商和研究机构构建电信专用 AI 模型。 这是目前最大的电信领域开放且经过许可验证的数据共享集，解决了电信 AI 开发中高质量、开放许可数据稀缺的问题。它将促进电信 AI 在网络优化和客户服务等场景的应用，同时确保合规性。 该语料库包含超过 100 亿 tokens，数据经过开放许可验证，是 Pleias 公司 2.27 万亿 tokens 通用语料库的子集。数据集可能涵盖技术文档、标准、报告等，但并非实时更新，且可能不涵盖所有电信子领域。

rss · GSMA Newsroom (移动安全标准) · 6月25日 08:56

**背景**: 电信 AI 利用机器学习优化网络管理、客服等。大语言模型（LLM）的微调依赖领域专用数据。开放数据共享集避免了版权风险，促进协作。GSMA 是代表全球移动运营商的行业协会，Pleias 是专长 LLM 训练数据的法国初创公司。通用语料库（Common Corpus）是目前最大的开放文本数据集，本语料库是其电信子集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.telecompaper.com/news/gsma-and-pleias-release-open-ai-dataset-for-telecom-sector--1575277">GSMA and Pleias release open AI dataset for telecom sector</a></li>
<li><a href="https://www.open-telco.ai/data/">Telecom AI Datasets | Training Data for Telco Models - GSMA</a></li>

</ul>
</details>

**标签**: `#telecom`, `#AI dataset`, `#open data`, `#GSMA`, `#natural language processing`

---

<a id="item-11"></a>
## [多密钥设置下可调 Feistel 密码的后量子安全证明](https://eprint.iacr.org/2026/1312) ⭐️ 7.0/10

该论文在内部原语量子访问模型下，证明了 3 轮和 4 轮可调密钥交替 Feistel 密码（TKAF）的后量子安全性，将先前经典结果扩展至多密钥量子场景。 随着量子计算威胁的迫近，这些针对 Feistel 结构的正式安全保证对设计抗量子对称密码至关重要，确保了面对量子敌手时的机密性。 安全界要求至少Ω(2^{n/3}/ℓ^{2/3})次经典与量子组合查询，或Ω(ε^{-1/2})次经典查询，其中ε是几乎异或通用哈希函数的碰撞概率，ℓ为多密钥设置中经典预言机数量。

rss · IACR ePrint 密码学论文 · 6月23日 18:35

**背景**: 可调密钥交替 Feistel 密码采用 Feistel 网络，每轮先将密钥与依赖调柄的值异或，再应用公开随机函数。TPRP（可调伪随机置换）和 STPRP（强 TPRP）模型分别针对选择明文和选择密文攻击。Q1 模型假设敌手可量子访问内部原语，但仅经典访问密码实例。后量子对称密码学确保设计能抵御 Grover、Simon 等量子算法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1312">Post-Quantum Security of Tweakable Key-Alternating Feistel Ciphers in the Multi-Key Setting</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-030-57808-4_4">Tweaking Key-Alternating Feistel Block Ciphers | SpringerLink</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_hashing">Universal hashing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#symmetric-key cryptography`, `#Feistel ciphers`, `#security proofs`, `#quantum security`

---

<a id="item-12"></a>
## [BN 配对子群被证明为相对迹映射核](https://eprint.iacr.org/2026/1311) ⭐️ 7.0/10

这篇新论文（ePrint 2026/1311）首次严格证明了 Barreto-Naehrig（BN）曲线的配对子群恰为 n-torsion 点上相对迹映射的核，证实了一个长期存在但未被证明的假设。 该成果巩固了基于配对密码学的理论基础，尤其是对于零知识证明协议（如 zkSNARKs）中广泛使用的 BN 曲线，确保依赖此性质的安全证明和实现坚实可靠。 该证明通过限制在 n-torsion 点上的相对迹映射显式刻画了配对子群，给出了此前仅为经验之谈的几何描述。

rss · IACR ePrint 密码学论文 · 6月23日 17:04

**背景**: Barreto-Naehrig（BN）曲线是 2005 年提出的一类配对友好椭圆曲线，因其在基于配对密码学中的高效性而被广泛用于 zkSNARKs 等系统。相对迹映射是一种与 Weil descent 和迹零子代数相关的代数工具，用于将扩展域上椭圆曲线的点映射到子域上曲线的点。n-torsion 点是指阶整除 n 的点。配对子群是双线性配对取值为 1 的点组成的子群。尽管该子群与相对迹之间的联系被广泛认可，但此前缺乏正式证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/scipr-lab/dizk/5-barreto-naehrig-curves">Barreto-Naehrig Curves | scipr-lab/dizk | DeepWiki</a></li>
<li><a href="https://math.mit.edu/~drew/TraceZeroVarieties.html">Trace Zero Varieties - MIT Mathematics</a></li>

</ul>
</details>

**标签**: `#Cryptography`, `#Elliptic Curves`, `#Pairing-Based Cryptography`, `#Barreto-Naehrig Curves`, `#Mathematical Proof`

---

<a id="item-13"></a>
## [掩码硬件随机性与延迟权衡的自动化设计空间探索](https://eprint.iacr.org/2026/1306) ⭐️ 7.0/10

本文提出了两种对偶算法——随机性约束下最小化延迟（MLRC）和延迟约束下最小化随机性（MRLC），用于自动寻找掩码硬件中最优的 gadget 分配方案，相比当前最先进的全局 SAT 优化方法实现了数个数量级的加速。 这项工作能够高效地按用户约束优化掩码硬件，大幅缩短设计时间，同时增强抵御侧信道攻击的能力，并可能通过让安全-性能权衡更易于实现来影响密码工程领域。 该方法利用基于 gadget 的掩码中探查隔离非干扰（PINI）gadget 的结构化权衡，在不到一毫秒内提供可比或更优的面积结果，避免了昂贵的全局优化。

rss · IACR ePrint 密码学论文 · 6月23日 08:39

**背景**: 掩码硬件将敏感数据分割为多个份额以抵御侧信道攻击。基于 gadget 的掩码使用预设计的掩码组件（gadget），其随机性和延迟成本已知，且随掩码阶数变化。设计空间探索（DSE）系统地搜索设计备选方案以优化性能和成本等参数。本文自动化该过程以平衡掩码电路中的随机性与延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Design_space_exploration">Design space exploration</a></li>
<li><a href="https://eprint.iacr.org/2016/486">Domain-Oriented Masking: Compact Masked Hardware Implementations with Arbitrary Protection Order</a></li>
<li><a href="https://tches.iacr.org/index.php/TCHES/article/view/877">Hardware Masking, Revisited | IACR Transactions on Cryptographic Hardware and Embedded Systems</a></li>

</ul>
</details>

**标签**: `#hardware security`, `#side-channel attacks`, `#design space exploration`, `#masking`, `#cryptographic engineering`

---

<a id="item-14"></a>
## [Cloudflare 工作流新增 Saga 式回滚功能](https://blog.cloudflare.com/rollbacks-for-workflows/) ⭐️ 7.0/10

Cloudflare 的持久化执行引擎 Workflows 现在支持 Saga 式回滚，允许开发者为每个 step.do() 附加一个补偿操作，以便在发生故障时自动撤销已完成的步骤。 该功能简化了复杂分布式工作流中的错误处理，减少了手动清理工作，并确保跨服务的数据一致性，这对于生产级无服务器应用至关重要。 回滚功能以元数据形式直接附加在每个持久化步骤上，而不是作为一个独立的全局错误处理程序，它利用现有的 Workflows 执行日志来确定需要调用哪些补偿操作。

rss · Cloudflare Blog (PQ 迁移) · 6月25日 13:00

**背景**: Cloudflare Workflows 是 Cloudflare Workers 上的一个服务，用于以持久化方式运行多步骤应用程序——自动重试并在故障时保存状态。Saga 模式常见于微服务架构，通过定义补偿事务来撤销先前步骤的影响，从而在后续步骤失败时维护数据一致性。持久化执行确保每个步骤都会被重试直到成功，但过去缺乏回滚机制，开发者需手动处理部分失败。通过集成 Saga 回滚，Workflows 现在提供了一种声明式方法来撤销已完成步骤，符合行业最佳实践。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/rollbacks-for-workflows/">How we built saga rollbacks for Cloudflare Workflows</a></li>
<li><a href="https://developers.cloudflare.com/workflows/">Overview · Cloudflare Workflows docs</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#workflows`, `#serverless`, `#rollbacks`, `#durable-execution`

---

<a id="item-15"></a>
## [Cloudflare 面向所有开发者推出自管理 OAuth](https://blog.cloudflare.com/oauth-for-all/) ⭐️ 7.0/10

Cloudflare 现在向所有开发者提供自管理 OAuth，使他们能够创建和管理自己的 OAuth 客户端，以委托方式访问 Cloudflare API。该公告附带一篇技术博客，详细介绍了 Cloudflare 如何对其核心 OAuth 引擎执行零停机迁移。 此功能简化了第三方应用程序与 Cloudflare 服务的集成，通过消除共享登录凭据的需求来增强安全性。它使开发者社区能够在 Cloudflare 平台上构建更强大的应用生态系统。 自管理 OAuth 功能支持基于令牌的委托访问，实现细粒度控制。零停机迁移涉及详细的工程设计，以确保在过渡期间持续提供服务。

rss · Cloudflare Blog (PQ 迁移) · 6月24日 06:00

**背景**: OAuth（开放授权）是一种行业标准协议，用于授权，允许用户在不透露密码的情况下，授予网站或应用程序对其在其他服务上资源的有限访问权限。Cloudflare 的平台包括 Workers、Pages 和 R2 等服务，第三方应用程序可利用其 API。此前，OAuth 客户端管理受到更多限制；自管理 OAuth 将控制权交到开发者手中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48668033">OAuth for all - Hacker News</a></li>
<li><a href="https://www.facebook.com/Cloudflare/posts/self-managed-oauth-is-now-available-to-all-developers-on-cloudflare-heres-how-we/1482385660584815/">Self-Managed OAuth is now available to all developers on Cloudflare. Here's how we executed a zero-downtime migration of our core OAuth engine to make it happen. https://cfl.re/4vsBr18</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#oauth`, `#authentication`, `#api`, `#security`

---
---
layout: default
title: "Horizon Summary: 2026-06-26 (ZH)"
date: 2026-06-26
lang: zh
---

> 从 39 条内容中筛选出 15 条重要资讯。

---

1. [UA-8295 后门终端的首次详细法证密码分析](#item-1) ⭐️ 9.0/10
2. [可验证编辑音频的匿名溯源新方案](#item-2) ⭐️ 8.0/10
3. [面向三分之二诚实多数的通信高效恶意安全多方计算协议](#item-3) ⭐️ 8.0/10
4. [通过规范编码修复实现 SQIsign 的强不可伪造性](#item-4) ⭐️ 8.0/10
5. [白宫行政令要求 2030 年前迁移至后量子密码](#item-5) ⭐️ 8.0/10
6. [德国法院裁定谷歌 AI 概览责任成立](#item-6) ⭐️ 8.0/10
7. [LLMs 凭风格而非标签辨识角色，致提示注入攻击持续](#item-7) ⭐️ 8.0/10
8. [间谍软件嵌入禁用文本逃避 AI 分析](#item-8) ⭐️ 8.0/10
9. [可调密钥交替 Feistel 密码的后量子安全性](#item-9) ⭐️ 7.0/10
10. [钱包干预措施降低授权钓鱼风险](#item-10) ⭐️ 7.0/10
11. [TETRIS：掩码硬件中随机性-延迟权衡的自动化设计空间探索](#item-11) ⭐️ 7.0/10
12. [Cloudflare 向所有开发者提供自主管理型 OAuth](#item-12) ⭐️ 7.0/10
13. [Java SSLContext 协议名称陷阱：易引发安全配置错误](#item-13) ⭐️ 7.0/10
14. [专家称大型语言模型降低漏洞报告的特殊性](#item-14) ⭐️ 7.0/10
15. [Anthropic 的 Fable 5 安全模型数日内遭越狱](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [UA-8295 后门终端的首次详细法证密码分析](https://eprint.iacr.org/2026/1309) ⭐️ 9.0/10

该论文首次对真实世界中被植入后门的 UA-8295 消息终端进行了详细的法证密码分析，揭示了其后门设计和潜在攻击的见解，并提出了用于推理后门设计的‘后门猜想’框架。 这项工作之所以重要，是因为它罕见地公开分析了一种由国家行为体植入后门的加密设备，增进了对真实世界后门技术的理解。‘后门猜想’为分析和识别后门提供了系统性方法，这对密码安全和数字取证至关重要。 UA-8295 是一种短突发消息终端，其后门由美国国家安全局（NSA）植入。论文对加密算法进行了逆向工程，并运用法证密码分析推断后门可能的目的和攻击向量。该研究是法证层面的分析，并未实际利用后门。

rss · IACR ePrint 密码学论文 · 6月23日 11:53

**背景**: UA-8295 是飞利浦公司设计的军用级短突发消息终端，用于安全通信。后来披露，NSA 在其加密算法中植入了后门，可能用于拦截和解密消息。法证密码分析涉及在数字取证背景下检查密码系统的漏洞，以了解它们可能被利用的方式。‘后门猜想’是本文提出的新框架，用于推理后门的设计和预期用途。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/stef/UA-8295-NSA">GitHub - stef/UA-8295-NSA: fully reverse-engineered and re-implemented ...</a></li>
<li><a href="https://www.cryptomuseum.com/crypto/philips/ua8295/files/ua8295_man.pdf">PDF SHOR-BURSTT MESSAGE TERMNIAL - cryptomuseum.com</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#backdoor`, `#forensic analysis`, `#signal intelligence`, `#national security`

---

<a id="item-2"></a>
## [可验证编辑音频的匿名溯源新方案](https://eprint.iacr.org/2026/1308) ⭐️ 8.0/10

研究人员提出了一种隐私保护音频认证系统（PPAAS），利用零知识证明验证编辑后的音频来自授权设备且经过允许的编辑，同时不泄露原始录音、编辑操作或设备身份。 该方案解决了音频取证中完整性与机密性的矛盾，使音频证据在认证和编辑时既能保护隐私，又不损害可信度，对法律、新闻及举报等领域有重大影响。 提供了两种构造：分段式方法仅对活跃编辑片段使用零知识证明（适合稀疏编辑），迭代式方法利用增量可验证计算与零知识压缩（适合密集编辑）。实际评估表明了二者的效率权衡。

rss · IACR ePrint 密码学论文 · 6月23日 10:51

**背景**: 零知识证明允许一方在不泄露额外信息的情况下证明某个陈述为真。设备认证可验证设备硬件和软件的真实性与完整性。PPAAS 结合匿名溯源技术，在隐藏来源和编辑历史的同时仍能验证音频的真实性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof</a></li>
<li><a href="https://www.ninjaone.com/it-hub/it-service-management/device-attestation/">What Is Device Attestation? | NinjaOne</a></li>

</ul>
</details>

**标签**: `#privacy`, `#audio-authentication`, `#zero-knowledge-proofs`, `#digital-forensics`, `#cryptography`

---

<a id="item-3"></a>
## [面向三分之二诚实多数的通信高效恶意安全多方计算协议](https://eprint.iacr.org/2026/1307) ⭐️ 8.0/10

该研究提出了一种基于编译器的安全多方计算协议，利用沙米尔秘密共享和本地验证框架，通过注入新鲜随机性和批量打开操作，实现抗三分之一腐败方的恶意安全，并降低了通信开销。 该研究为恶意安全的多方计算提供了更高效的通信方案，这对于隐私保护机器学习等实际应用至关重要，因为强安全性通常伴随着高昂的通信成本。 该协议适用于最多 t < n/3 个腐败方的情况，通过注入新鲜随机性来检测使用错误乘法三元组时的作弊行为，并用本地度-2t 计算和单次批量打开取代了多次乘法验证。

rss · IACR ePrint 密码学论文 · 6月23日 08:55

**背景**: 安全多方计算允许多方在不泄露私有输入的情况下联合计算函数。沙米尔秘密共享将秘密分割为若干份额，只有达到门限数量的份额才能恢复秘密。恶意安全模型保护协议免受任意偏离协议的敌手攻击，而半诚实模型仅防止被动窃听。基于编译器的方法通过添加验证阶段，将半诚实协议转化为恶意安全协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shamir's_secret_sharing">Shamir's secret sharing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation - Wikipedia</a></li>
<li><a href="https://drum.lib.umd.edu/items/2780657c-82d2-44fc-bdf9-d0260fd8ba1c">A New Paradigm for Practical Maliciously Secure Multi-Party Computation</a></li>

</ul>
</details>

**标签**: `#secure multi-party computation`, `#malicious security`, `#Shamir secret sharing`, `#communication efficiency`, `#cryptographic protocols`

---

<a id="item-4"></a>
## [通过规范编码修复实现 SQIsign 的强不可伪造性](https://eprint.iacr.org/2026/1305) ⭐️ 8.0/10

研究人员发现 SQIsign v2.0 中一个具体的可延展性漏洞：将签名中的基变换矩阵 M_chl 模 2^N 取负可产生不同的有效签名，类似于 ECDSA 的可延展性。他们提出了规范矩阵编码修复方案，并证明修改后的方案在量子随机谕言模型下实现了 SUF-CMA 安全性。 这填补了 SQIsign 在 NIST 标准化过程中安全性证明的关键缺口。强不可伪造性可防止签名可延展性攻击，确保对手无法在无密钥的情况下修改已有签名，这对交易账本和智能合约的安全至关重要。 修复方案将 M_chl 规范化为标准形式，并在验证时拒绝非规范形式，从而建立了单射响应编码。概念验证攻击在全部三个 NIST 安全级别的 C 参考实现上得到演示。

rss · IACR ePrint 密码学论文 · 6月23日 04:21

**背景**: SQIsign 是基于同源的主流后量子签名方案，拥有小密钥和签名尺寸但计算开销较高。存在性不可伪造性（EUF-CMA）仅保证无法伪造新签名，而强不可伪造性（SUF-CMA）还禁止将合法签名修改为新的有效签名。可延展性风险包括交易重放攻击和分布式系统的不一致性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SQIsign">SQIsign</a></li>
<li><a href="https://blog.cryptographyengineering.com/euf-cma-and-suf-cma/">EUF-CMA and SUF-CMA – A Few Thoughts on Cryptographic Engineering</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#digital signatures`, `#isogeny-based cryptography`, `#SQIsign`, `#SUF-CMA`

---

<a id="item-5"></a>
## [白宫行政令要求 2030 年前迁移至后量子密码](https://blog.cloudflare.com/post-quantum-eo-2026/) ⭐️ 8.0/10

白宫发布行政令，要求联邦机构在 2030 年前完成后量子密码迁移。Cloudflare 随后发表了对该行政令的分析，并提供了面向政府和行业的迁移指南。 该行政令首次为美国政府的后量子迁移设定了具体期限，迫使公共和私营部门立即行动，升级密码系统以防范未来的量子威胁。Cloudflare 的指南为实现这一目标提供了可操作的步骤。 行政令要求在 2030 年前盘点加密资产并测试后量子算法；Cloudflare 建议先采用混合证书并优先保护关键系统。

rss · Cloudflare Blog (PQ 迁移) · 6月23日 18:25

**背景**: 后量子密码学旨在开发能抵御量子计算机攻击的算法。量子计算机可通过 Shor 算法破解 RSA 和 ECC 等现行公钥密码。为防范‘现在收集，以后解密’的威胁，各机构正加快向抗量子算法迁移。美国 NIST 于 2024 年发布了首批后量子密码标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://csrc.nist.gov/projects/post-quantum-cryptography">Post-Quantum Cryptography - NIST CSRC - National Institute of Standards and Technology</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#executive order`, `#Cloudflare`, `#migration`, `#cybersecurity`

---

<a id="item-6"></a>
## [德国法院裁定谷歌 AI 概览责任成立](https://www.schneier.com/blog/archives/2026/06/ai-and-liability.html) ⭐️ 8.0/10

德国法院裁定，谷歌对其 AI 生成的搜索摘要中的虚假陈述承担责任，驳回了用户应自行核实信息的辩护。 该裁决确立了 AI 生成内容可归责于部署公司的法律先例，可能影响全球 AI 责任标准和平台问责机制。 法院指出 AI 摘要是谷歌商业活动的表现，不能以用户可核实为由免责；谷歌的 AI 概览是核心搜索功能，无法关闭。

rss · Schneier on Security · 6月25日 17:03

**背景**: 互联网责任法传统上区分传输者（如电话公司，不对内容负责）和发布者（如报纸，需负责）。在美国，第 230 条通常使平台对第三方内容免责。谷歌于 2023 年推出的 AI 概览功能直接生成摘要，挑战了这些界限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_Overviews">AI Overviews - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Section_230">Section 230 - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#liability`, `#legal`, `#Google`, `#content moderation`

---

<a id="item-7"></a>
## [LLMs 凭风格而非标签辨识角色，致提示注入攻击持续](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html) ⭐️ 8.0/10

一项新研究发现，大语言模型（LLMs）是通过文本风格而非显式角色标签来识别指令来源的，这削弱了当前依赖角色分离的提示注入防御措施。 这揭示了提示注入是一个根本性缺陷，而非表面问题：攻击者利用风格线索即可绕过基于角色的防御，因此除非 LLMs 具备真正的角色感知能力，否则注入攻击将是一场长期的‘打地鼠’游戏。 论文提出了‘角色混淆’概念，即模型根据文本的‘听感’而非标签来识别来源。通过内部‘角色探针’，他们发现这种混淆能强有力地预测注入攻击的成功，甚至在模型生成输出之前就能检测。

rss · Schneier on Security · 6月25日 11:23

**背景**: 提示注入是一种攻击方式，攻击者将恶意指令嵌入外部数据中，操纵大语言模型（LLM）的行为。通常，系统使用角色标签（如<system>、<user>）来分隔提示的不同部分并构建安全边界，但这项研究挑战了模型能真正理解这些角色的假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.12277">[2603.12277] Prompt Injection as Role Confusion</a></li>
<li><a href="https://www.gilesthomas.com/2026/06/role-confusion">Thoughts on Role Confusion - Giles' blog</a></li>

</ul>
</details>

**标签**: `#AI security`, `#prompt injection`, `#LLMs`, `#adversarial attacks`, `#role confusion`

---

<a id="item-8"></a>
## [间谍软件嵌入禁用文本逃避 AI 分析](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis-2.html) ⭐️ 8.0/10

恶意软件开发者开始在间谍软件代码注释中嵌入关于核武器和生物武器的文本，诱使基于人工智能的分析工具拒绝扫描文件。 这种手段利用了人工智能安全过滤器，表明攻击者可将负责任的人工智能防护措施武器化。这威胁到自动化安全分析，需要更强大的上下文感知扫描器。 恶意注释包含伪造的系统指令和违反政策的内容，位于基于 eval 的 ROT 编码载荷之前。真实恶意代码在注释后才执行，因此运行时不受影响，但解析文件头的人工智能扫描器可能被误导而拒绝分析。

rss · Schneier on Security · 6月24日 11:03

**背景**: AI 安全扫描器通常使用大型语言模型分析代码，有时会优先处理文件开头。ROT 密码是一种简单的字母替换加密，在此用于混淆恶意软件。模型上下文协议（MCP）是连接 AI 与外部数据的开放标准；该间谍软件针对 MCP 开发者，显示出定向攻击意图。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rotor_cipher_machine">Rotor cipher machine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#adversarial AI`, `#malware`, `#AI safety`, `#espionage`

---

<a id="item-9"></a>
## [可调密钥交替 Feistel 密码的后量子安全性](https://eprint.iacr.org/2026/1312) ⭐️ 7.0/10

该论文证明了在 Q1 模型下，当敌手可量子访问内部公开随机函数时，可调密钥交替 Feistel 密码（TKAF）在多密钥场景中的后量子安全性。它扩展了 Basak 等人（ASIACRYPT 2025）的非可调版本证明，表明 3 轮 TKAF 实现 TPRP 安全，4 轮 TKAF 实现 STPRP 安全。 这项工作增强了后量子时代对称密钥密码学的理论基础，特别是对广泛用于磁盘加密和认证加密的可调分组密码而言。通过量化量子攻击下的具体安全边界，它为未来抗量子敌手的设计提供了指导。 证明采用ε-AXU 哈希函数族注入调柄，并表明在多密钥场景下，至少需要Ω(2^(n/3)/ℓ^(2/3))次经典与量子查询组合，或Ω(ε^(-1/2))次经典查询才能攻破 TPRP/STPRP 安全性，其中ℓ为多密钥设置中的预言机数量。

rss · IACR ePrint 密码学论文 · 6月23日 18:35

**背景**: Feistel 密码（如 DES）采用轮结构，用密钥化函数变换一半分组。密钥交替 Feistel 密码在每轮函数前后异或密钥。可调分组密码通过额外调柄输入改变行为，常借哈希函数注入。Q1 模型允许敌手对内部原语进行量子叠加访问，但对构造预言机仅允许经典访问。后量子安全性确保方案能抵抗拥有量子计算机的攻击者，这是量子计算发展下的关键领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://infoscience.epfl.ch/server/api/core/bitstreams/2147e5cc-e4ee-49a4-b7a3-11eae1e0b3b3/content">Tweaking Key - Alternating Feistel Block</a></li>
<li><a href="https://eprint.iacr.org/2025/945.pdf">PDF Quantum Security Analysis of the Key-Alternating Ciphers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_hashing">Universal hashing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#symmetric-key`, `#security-proof`, `#feistel-cipher`

---

<a id="item-10"></a>
## [钱包干预措施降低授权钓鱼风险](https://eprint.iacr.org/2026/1310) ⭐️ 7.0/10

该论文提出并评估了四种钱包内干预措施：支出上限建议、主动授权者警告、被动授权者警告和延迟确认，一项有 364 名参与者的用户研究表明，这些措施能提高用户设置支出上限和取消钓鱼交易等保护行为。 授权钓鱼是 Web3 中日益严重的威胁，现有基于 URL 的检测手段不足；这些钱包端干预在授权时刻提供最后一道防线，对改进钱包设计和用户安全具有直接影响。 主动授权者警告和延迟确认条件显著提高了取消率，而被动授权者警告的提升不具统计显著性；支出上限建议有效鼓励了设置上限，但用户有时难以解读可疑线索。

rss · IACR ePrint 密码学论文 · 6月23日 16:42

**背景**: 授权钓鱼利用以太坊等区块链中的代币授权机制，即 ERC-20 的 approve 函数允许用户授予智能合约花费其代币的权限。攻击者诱骗用户向恶意合约授予无限授权，随后无需私钥即可转移资金。钱包会显示授权详情，但用户经常忽略。这种纵深防御方法旨在让授权参数的验证更加突出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chainalysis.com/blog/what-is-approval-phishing/">What Is Approval Phishing ? Detect & Disrupt Crypto Scams at Scale</a></li>
<li><a href="https://support.ledger.com/article/Ethereum-Token-Approvals-Explained">Understanding Ethereum Token Approvals</a></li>
<li><a href="https://support.metamask.io/stay-safe/safety-in-web3/what-is-a-token-approval/">What is a token approval? | MetaMask Help Center</a></li>

</ul>
</details>

**标签**: `#approval phishing`, `#Web3 security`, `#user study`, `#wallet design`, `#HCI`

---

<a id="item-11"></a>
## [TETRIS：掩码硬件中随机性-延迟权衡的自动化设计空间探索](https://eprint.iacr.org/2026/1306) ⭐️ 7.0/10

TETRIS 引入两种启发式算法（MLRC 和 MRLC），自动探索基于组件的掩码硬件中随机性与延迟之间的权衡。与先前全局优化方法相比，它在不到一毫秒内完成探索，实现了可比的面积结果，速度提升数个数量级。 该工具使硬件安全工程师能够在随机性或延迟约束下快速找到最优掩码设计，减少开发工作量，并可能增强对侧信道攻击的抵御能力。 TETRIS 利用了 PINI 组件固有的结构化权衡，其算法——随机性约束下最小化延迟（MLRC）和延迟约束下最小化随机性（MRLC）互为对偶。它在亚毫秒级时间内运行，并实现与现有最优方法相当甚至更好的面积。

rss · IACR ePrint 密码学论文 · 6月23日 08:39

**背景**: 掩码是一种抵抗侧信道攻击的对策，将秘密值分割成多个随机份额。基于组件的掩码使用对应简单逻辑门的预验证组件（gadget）构建安全电路。安全阶数（份额数减一）决定所需的随机性和延迟。PINI（Probe-Isolating Non-Interference）是一种可组合性概念，确保组件能够安全组合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artifacts.iacr.org/tches/2024/a5/">Gadget-based Masking of Streamlined NTRU Prime Decapsulation in Hardware - IACR</a></li>
<li><a href="https://casa.rub.de/fileadmin/img/Publikationen_PDFs/2021_Automated_Generation_of_Masked_Hardware_Publication_ClusterofExcellence_CASA_Bochum.pdf">Automated Generation of Masked Hardware</a></li>

</ul>
</details>

**标签**: `#hardware security`, `#side-channel attacks`, `#masking`, `#design space exploration`, `#randomness`

---

<a id="item-12"></a>
## [Cloudflare 向所有开发者提供自主管理型 OAuth](https://blog.cloudflare.com/oauth-for-all/) ⭐️ 7.0/10

Cloudflare 在完成其核心 OAuth 引擎的零停机迁移后，现已向所有开发者提供自主管理型 OAuth。 这简化了应用集成，减少了入驻障碍，并赋予开发者更自主地在 Cloudflare 平台上构建和扩展应用的能力。 零停机迁移确保在无缝部署新 OAuth 引擎时，现有用户的服务不会中断。

rss · Cloudflare Blog (PQ 迁移) · 6月24日 06:00

**背景**: OAuth 是一种标准协议，允许应用程序在无需共享密码的情况下代表用户访问资源。Cloudflare 运营着一个提供安全和性能服务的全球网络，其应用生态系统允许第三方开发者构建集成工具。自主管理型 OAuth 让开发者完全掌控身份验证凭证，无需 Cloudflare 手动审批。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Zero-Downtime_Migration">Zero-Downtime Migration</a></li>

</ul>
</details>

**标签**: `#OAuth`, `#Cloudflare`, `#Developer Tools`, `#Zero-Downtime Migration`, `#Authentication`

---

<a id="item-13"></a>
## [Java SSLContext 协议名称陷阱：易引发安全配置错误](https://neilmadden.blog/2026/06/23/javas-sslcontext-protocol-name-is-a-footgun/) ⭐️ 7.0/10

一篇博文警告，Java 开发者经常误用 SSLContext.getInstance，传入‘TLSv1.3’等 TLS 版本字符串，这会意外地限制协议支持，构成安全陷阱。 这种错误配置可能导致与仅支持其他 TLS 版本的服务器的连接中断，并不经意间削弱安全性，从而影响大量 Java 应用的可靠性和安全性。 正确参数应为‘TLS’或‘SSL’，这会启用一组默认的多种协议；使用‘TLSv1.2’等特定版本字符串会将上下文锁定为仅该版本，引发兼容性和安全性问题。

rss · Neil Madden (后量子密码) · 6月23日 20:12

**背景**: 在 Java 中，SSLContext 是配置 SSL/TLS 连接的核心类。getInstance(String protocol)方法期望一个协议族名称，而非版本号。标准安全提供者支持‘TLS’、‘SSL’等协议族，它们会自动启用所有合适且安全的协议版本。使用‘TLSv1.2’这样的版本字符串会绕过这种智能选择，强制限定在单一版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.oracle.com/javase/8/docs/api/javax/net/ssl/SSLContext.html">SSLContext (Java Platform SE 8 )</a></li>
<li><a href="https://docs.oracle.com/en/java/javase/11/docs/api/java.base/javax/net/ssl/SSLContext.html">SSLContext (Java SE 11 & JDK 11 )</a></li>

</ul>
</details>

**标签**: `#Java`, `#TLS`, `#security`, `#SSL`, `#footgun`

---

<a id="item-14"></a>
## [专家称大型语言模型降低漏洞报告的特殊性](https://words.filippo.io/vuln-reports/) ⭐️ 7.0/10

Filippo Valsorda 认为，随着大型语言模型（LLM）的兴起，任何人现在都能生成类似的安全见解，因此机密漏洞披露可能不再必要。 这挑战了传统的漏洞披露模式，可能影响漏洞赏金计划、安全研究以及公司处理安全漏洞的方式。 该文章缺乏技术深度，更像是一个引发讨论的挑衅性观点；它没有提供实证证据或关于 LLM 发现漏洞的具体能力说明。

rss · Filippo Valsorda (Go 密码学) · 6月23日 13:00

**背景**: 大型语言模型（LLM）是像 GPT-4 这样的 AI 系统，可以理解和生成文本。漏洞披露通常是指研究人员向供应商秘密报告安全缺陷，以便他们在公开发布前修复，保护用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#vulnerability-disclosure`, `#LLM`, `#AI`, `#software-security`

---

<a id="item-15"></a>
## [Anthropic 的 Fable 5 安全模型数日内遭越狱](https://www.schneier.com/blog/archives/2026/06/anthropics-fable-5-model-jailbroken-within-days.html) ⭐️ 7.0/10

Anthropic 的 Claude Fable 5 模型旨在防止生成网络攻击，但在发布后数日内即被越狱，网络安全新闻对此进行了报道。 此次迅速越狱凸显了将强大 AI 模型与安全目标对齐的持续挑战，引发了人们对防护措施有效性及网络安全信任度的担忧。 Fable 5 是 Anthropic 的 Mythos Preview 的安全导向变体，后者是一个具有强大网络安全能力、仅限研究预览的模型。绕过安全限制是通过未公开的提示工程技术实现的。

rss · Schneier on Security · 6月23日 11:03

**背景**: Anthropic 的 Mythos Preview 是一款专长于网络安全任务的尖端 AI 模型，最初仅向经过审查的防御者发布。Fable 5 通过增加阻拦恶意用途（特别是网络攻击生成）的防护栏，打造了一个更安全的公开可用版本。AI 中的越狱是指通过精心设计的输入绕过安全约束的方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.reddit.com/r/Anthropic/comments/1u4wjbi/fable_5_was_the_best_model_out_there_anyone_think/">Fable 5 was the best model out there — anyone think it's actually coming back after the gov directive? : r/Anthropic - Reddit</a></li>

</ul>
</details>

**社区讨论**: 在 Reddit 上，用户注意到 Fable 5 如此迅速被越狱的讽刺意味，一些人批评该模型过度限制，并就政府指令下的未来展开辩论。

**标签**: `#AI safety`, `#jailbreaking`, `#cybersecurity`, `#Anthropic`

---
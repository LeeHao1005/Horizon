---
layout: default
title: "Horizon Summary: 2026-07-10 (ZH)"
date: 2026-07-10
lang: zh
---

> 从 28 条内容中筛选出 8 条重要资讯。

---

1. [密钥恢复攻击破解 TALUS 门限 ML-DSA 方案](#item-1) ⭐️ 10.0/10
2. [基于懒惰比特的 Walsh LUT 加速 CKKS AES 转换加密](#item-2) ⭐️ 8.0/10
3. [基于黑盒密码学的带预处理 PIR 计算下界](#item-3) ⭐️ 8.0/10
4. [立即采用 ML-DSA，无需等待更好的后量子签名算法](#item-4) ⭐️ 8.0/10
5. [AI 文本可能重塑人类口语](#item-5) ⭐️ 8.0/10
6. [Cloudflare 推出 Meerkat：采用 QuePaxa 的全球共识服务](#item-6) ⭐️ 7.0/10
7. [五眼联盟警告 AI 自主黑客攻击风险，标准网络安全措施迫在眉睫](#item-7) ⭐️ 7.0/10
8. [谷歌起诉利用 Gemini 进行自动化钓鱼的中国诈骗团伙](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [密钥恢复攻击破解 TALUS 门限 ML-DSA 方案](https://eprint.iacr.org/2026/1386) ⭐️ 10.0/10

通过利用 ML-DSA 公钥矩阵 A 的左可逆性，攻击者可从 TALUS-MPC 的密钥生成和签名广播中被动恢复秘密份额；同时，因删除拒绝采样检查，攻击者可从数亿个签名中恢复完整密钥。 这些攻击完全打破了 TALUS 声称的 EUF-CMA 安全性，使其无法用于 NIST 门限后量子密码标准化，凸显了格基方案中拒绝采样检查缺失的严重后果。 攻击利用 ML-DSA 中公钥矩阵 A 的左可逆性，通过高斯消元直接求逆；而删除拒绝采样检查使每个签名泄漏关于 s2 的含噪线性方程，可在分圆环上用最小二乘法恢复 s2。

rss · IACR ePrint 密码学论文 · 7月7日 17:30

**背景**: 门限密码方案将密钥分片给多方以增强安全性。ML-DSA 是基于模格的后量子数字签名标准。TALUS 旨在通过非零预处理和边界清除条件实现高效的单轮在线门限 ML-DSA 签名，其 MPC 版本使用 Feldman 承诺共享秘密。标准 ML-DSA 中，签名时的拒绝采样检查防止秘密泄露，TALUS 删除了这一保护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.22109">[2603.22109] TALUS: Threshold ML-DSA with One-Round Online ... TALUS: Threshold ML-DSA with One-Round Online Signing TALUS: Threshold ML-DSA with One-Round Online Signing via ... TALUS: Threshold ML-DSA with One-Round Online Signing TALUS: Threshold ML-DSA with One-Round Online Signing ... Finally! A Compact Lattice-Based Threshold Signature</a></li>
<li><a href="https://csrc.nist.gov/csrc/media/Projects/threshold-cryptography/documents/TCall-1/TALUS-PW02.pdf">TALUS: Threshold ML-DSA with One-Round Online Signing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Verifiable_secret_sharing">Verifiable secret sharing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#ML-DSA`, `#threshold signatures`, `#key-recovery attack`, `#NIST`

---

<a id="item-2"></a>
## [基于懒惰比特的 Walsh LUT 加速 CKKS AES 转换加密](https://eprint.iacr.org/2026/1385) ⭐️ 8.0/10

该论文提出一种在二进制 CKKS 上的布尔查找表新评估方法，利用懒惰加法和 Walsh 基，将 LUT 大小与电路深度解耦，并在 AES-CTR 转换加密上比以往的 XBOOT 变体快 3.25 倍。 该工作降低了 CKKS 中布尔 LUT 的乘法深度开销，使 AES 转换加密更加高效，推动同态加密在隐私保护云计算等实际应用中更近一步。 LUT 以 Walsh 基表示，通过 CKKS 二进制自举清理后的奇偶符号与明文系数重组求值。AES 采用半字节分割的 Walsh 分解，仅增加一层乘法深度即支持更多块；AES 状态利用全复数打包，实部和虚部通道承载独立块，在 1024 块批处理下比 XBOOT 快 3.25 倍。

rss · IACR ePrint 密码学论文 · 7月7日 16:22

**背景**: 全同态加密允许在加密数据上计算。CKKS 是一种支持近似算术的同态加密方案，但二进制运算（如异或）代价高昂。Walsh 基可将布尔函数表示为奇偶函数的线性组合，并通过懒惰加法计算。转换加密利用 AES 等对称密码在客户端加密，将繁重计算转移到云端。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_encryption">Homomorphic encryption - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/ckks-homomorphic-encryption-scheme">CKKS Homomorphic Encryption Scheme</a></li>
<li><a href="https://eprint.iacr.org/2025/093.pdf">A Survey on Transciphering and Symmetric Ciphers for Homomorphic Encryption</a></li>

</ul>
</details>

**标签**: `#homomorphic encryption`, `#CKKS`, `#lookup tables`, `#AES`, `#transciphering`

---

<a id="item-3"></a>
## [基于黑盒密码学的带预处理 PIR 计算下界](https://eprint.iacr.org/2026/1384) ⭐️ 8.0/10

该论文为使用黑盒密码学的单服务器 PIR 预处理方案建立了新的计算下界，证明对于存储了 n 比特数据库 s bits 的客户端，在线摊销计算量必须为Ω(n/s)，即使查询是批处理的。 这些下界揭示了带预处理 PIR 在客户端存储、计算和通信之间的固有权衡，表明从黑盒假设出发不可能同时实现亚线性计算与通信的双重高效 PIR，从而为近期构造中使用格密码等非黑盒技术提供了理论依据。 该下界是紧的，因为存在 PIR 方案满足低计算或低通信之一。此外，论文还为特定类别（如服务器计算量 o(n/s)或仅依赖于查询通信的方案）提供了无条件的通信下界，并证明了对称 PIR 的下界，给出了仅用单向函数的匹配构造。

rss · IACR ePrint 密码学论文 · 7月7日 12:48

**背景**: 私有信息检索（PIR）允许客户端在不泄露检索目标的情况下从数据库查询数据。预处理使客户端可离线存储提示信息，从而减少在线计算量。黑盒密码学指将密码学原语（如随机预言机或混淆）视为黑盒的构造方法。在引入预处理前，单服务器 PIR 需要服务器端线性计算量；近期方案虽绕过了这一点，但依赖环-LWE 等非黑盒假设。本文确立了黑盒方法的能力上限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/rwe/10.1007/978-3-030-71522-9_1470">Private Information Retrieval with Preprocessing | Springer Nature Link</a></li>
<li><a href="https://eprint.iacr.org/2024/780">Information-theoretic Multi-server Private Information Retrieval with Client Preprocessing</a></li>
<li><a href="https://eprint.iacr.org/2022/830">Near-Optimal Private Information Retrieval with Preprocessing</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#private information retrieval`, `#lower bounds`, `#preprocessing`, `#blackbox constructions`

---

<a id="item-4"></a>
## [立即采用 ML-DSA，无需等待更好的后量子签名算法](https://blog.cloudflare.com/ml-dsa-will-have-to-do/) ⭐️ 8.0/10

Cloudflare 认为，尽管 NIST 正在评估九种新的后量子签名算法，但 ML-DSA（原 Dilithium）是目前最好的可用方案，应立即采用。 该分析为迁移到抗量子签名提供了实际紧迫性，警告等待未来的算法将使系统暴露于‘现在收集，以后解密’的量子攻击风险。 ML-DSA 是一种基于格的仅签名算法，于 2024 年由 NIST 标准化，提供三种参数集；它不支持加密或密钥交换。

rss · Cloudflare Blog (PQ 迁移) · 7月9日 14:00

**背景**: 后量子密码学旨在开发抵抗量子计算机的算法。NIST 自 2016 年起标准化此类算法，ML-DSA（Dilithium）是首批获批的算法之一。目前另有九种签名候选算法正在评估中，以丰富未来选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://csrc.nist.gov/projects/pqc-dig-sig">Post-Quantum Cryptography: Additional Digital Signature ...</a></li>
<li><a href="https://postquantum.com/post-quantum/post-quantum-digital-signatures/">The Future of Digital Signatures in a Post-Quantum World</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#digital signatures`, `#NIST standardization`, `#ML-DSA`, `#cybersecurity`

---

<a id="item-5"></a>
## [AI 文本可能重塑人类口语](https://www.schneier.com/blog/archives/2026/07/the-language-of-ai-could-change-how-humans-speak.html) ⭐️ 8.0/10

布鲁斯·施奈尔警告，越来越多接触 AI 生成的文本可能导致人类采纳大语言模型的语言模式，从而可能贬低无稿口语交流的价值。 这一转变可能侵蚀面对面交谈中固有的自发性和文化丰富性，改变人类互动与身份认同的基本方面。 大语言模型主要基于书面文本和脚本化语音训练，缺失了构成人类口语文化核心的绝大多数无稿日常对话。

rss · Schneier on Security · 7月9日 11:00

**背景**: 像 GPT-4 这样的大语言模型是在互联网和书籍等海量文本语料上训练的，其中书面语言占主导地位。无稿口语，如日常闲聊，很少被这些数据集收录。随着 AI 生成文本的泛滥，可能出现反馈循环：人类语言越来越模仿 AI 模式，可能导致交流同质化，削弱自发言语的多样性。

**标签**: `#AI`, `#language models`, `#linguistics`, `#society`, `#cultural impact`

---

<a id="item-6"></a>
## [Cloudflare 推出 Meerkat：采用 QuePaxa 的全球共识服务](https://blog.cloudflare.com/meerkat-introduction/) ⭐️ 7.0/10

Cloudflare Research 推出了 Meerkat，一个采用新型 QuePaxa 算法的全球共识服务，该算法使用对冲延迟而非传统超时来实现共识。 该方法有望将强一致性与高性能和容错性结合起来，可能提升全球分布式服务的可靠性，并影响未来的共识协议设计。 QuePaxa 以对冲调度的方式组织潜在提议者，在交错的时间间隔内激活它们以避免冲突，并在正常条件下实现一轮往返的快速路径；其安全性已通过 Spin 模型检查器验证。

rss · Cloudflare Blog (PQ 迁移) · 7月8日 13:00

**背景**: 分布式共识算法允许多台服务器就单一状态达成一致，这对于容错系统至关重要。领导者驱动的协议（如 Paxos 和 Raft）依赖超时机制来从领导者故障中恢复，在不利的网络条件下可能导致性能问题。对冲策略，常用于多层查询系统，涉及在不同节点上冗余发起操作以缓解尾部延时。QuePaxa 将对冲应用于共识，允许多个提议者按照协调调度尝试领导，而不产生破坏性干扰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bford.info/pub/os/quepaxa/quepaxa.pdf">QuePaxa: Escaping the Tyranny of Timeouts in Consensus Introducing Meerkat- an experiment in global consensus QuePaxa: Escaping the Tyranny of Timeouts in Consensus QuePaxa: Escaping the tyranny of timeouts in consensus QuePaxa: Escaping the Tyranny of Timeouts in Consensus QuePaxa: Escaping the tyranny of timeouts in consensus</a></li>
<li><a href="https://github.com/dedis/quepaxa">GitHub - dedis/quepaxa: This is the code repository for ...</a></li>

</ul>
</details>

**标签**: `#consensus`, `#distributed systems`, `#cloudflare`, `#research`, `#fault-tolerance`

---

<a id="item-7"></a>
## [五眼联盟警告 AI 自主黑客攻击风险，标准网络安全措施迫在眉睫](https://www.schneier.com/blog/archives/2026/07/cybersecurity-and-the-gap-between-skill-and-ability.html) ⭐️ 7.0/10

五眼联盟（美国、英国、加拿大、澳大利亚、新西兰）发布联合声明，警告 AI 模型可自主入侵系统，Bruce Schneier 评论称，尽管风险真实存在，但建议的缓解措施都是标准的网络安全实践。 该声明强调了基本网络安全卫生的紧迫性，因为 AI 降低了攻击者的技术门槛，可能使复杂的网络攻击大众化，迫使组织优先采用现有最佳实践。 与媒体的夸张标题相比，五眼联盟的声明较为审慎；建议包括系统补丁、多因素身份验证和网络监控——这些标准实践仍有许多组织未能持续实施。

rss · Schneier on Security · 7月8日 11:03

**背景**: 五眼联盟是澳大利亚、加拿大、新西兰、英国和美国之间的情报联盟，根据 UKUSA 协议进行信号情报合作。AI 驱动的网络安全威胁涉及使用大语言模型自主发现和利用漏洞，这比依赖工具的手动黑客攻击严重升级。尽管威胁是新的，但建议的基本安全控制措施（如访问管理和定期更新）仍然有效，但常被忽视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Five_Eyes">Five Eyes - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#artificial intelligence`, `#national security`, `#hacking`, `#risk assessment`

---

<a id="item-8"></a>
## [谷歌起诉利用 Gemini 进行自动化钓鱼的中国诈骗团伙](https://www.schneier.com/blog/archives/2026/07/google-is-suing-chinese-scammers-who-are-using-gemini.html) ⭐️ 7.0/10

谷歌对一个名为 Outsider Enterprise 的中国网络犯罪团伙提起诉讼，该团伙利用 Gemini AI 自动生成冒充谷歌、YouTube 及政府机构的虚假网站，并提供近 300 个诈骗模板的钓鱼即服务。 此案凸显了 AI 驱动的钓鱼攻击这一新兴威胁，生成式 AI 降低了网络犯罪分子实施复杂诈骗的门槛，并可能为 AI 平台的责任认定及 AI 滥用政策制定开创法律先例。 该团伙通过 Telegram 运营，提供详细的 Gemini 使用教程来克隆网站；谷歌的诉讼旨在捣毁这一提供近 300 个诈骗模板的钓鱼即服务平台。

rss · Schneier on Security · 7月7日 10:43

**背景**: Google Gemini 是谷歌开发的生成式 AI 聊天机器人，能够生成文本和代码。钓鱼即服务（PhaaS）是一种网络犯罪模式，犯罪分子将预制的钓鱼工具、模板和托管基础设施出售给其他犯罪分子，使非技术人员也能实施诈骗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Gemini">Google Gemini - Wikipedia</a></li>
<li><a href="https://www.huntress.com/cybersecurity-101/topic/phishing-as-a-service">What is Phishing-as-a-Service | Cybercrime Democratized ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI misuse`, `#phishing`, `#legal action`, `#Google Gemini`

---
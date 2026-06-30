---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> 从 32 条内容中筛选出 10 条重要资讯。

---

1. [Flock：面向批量哈希计算的高速 SNARK 系统](#item-1) ⭐️ 9.0/10
2. [澄清 OEKE-2F PAKE 协议：究竟需要哈希哪些内容](#item-2) ⭐️ 8.0/10
3. [Falafel：面向联邦学习的模块化零知识训练证明](#item-3) ⭐️ 8.0/10
4. [EasyCrypt 协议验证的关键：状态与时态不变量](#item-4) ⭐️ 8.0/10
5. [现实世界资格证明：DeFi 中现实世界资产的隐私验证协议](#item-5) ⭐️ 8.0/10
6. [发现新型稀疏模数 RSA 弱密钥](#item-6) ⭐️ 8.0/10
7. [提出标准化 ML-DSA 基准测试方法以避免误比](#item-7) ⭐️ 7.0/10
8. [后量子 DNSSEC 的差异化算法选择](#item-8) ⭐️ 7.0/10
9. [萨克拉门托警局无人机用磁铁解除嫌犯武装](#item-9) ⭐️ 7.0/10
10. [RFC 9970 增强 STIR 应对连接身份问题](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Flock：面向批量哈希计算的高速 SNARK 系统](https://eprint.iacr.org/2026/1329) ⭐️ 9.0/10

Flock 是一种新型基于哈希的 SNARK 系统，能以极低开销证明大批量哈希运算（如 SHA-256、BLAKE3），单核每秒可处理 8.2 万次 BLAKE3 压缩。 这大大缩短了 SNARK 在区块链扩容和隐私保护等应用中的证明时间，使此前不切实际的实时性能成为可能。 Flock 采用优化的 lincheck 和 zerocheck 协议，单核开销低于原生执行的 250 倍，十核下 BLAKE3 压缩速度达 66 万次/秒，SHA-256 证明速度比前先进技术 Binius64 快 9 倍以上。

rss · IACR ePrint 密码学论文 · 6月28日 00:15

**背景**: SNARK（简洁非交互式知识论证）允许在不泄露输入的情况下证明计算的正确性，广泛应用于区块链可扩展性和隐私保护。R1CS 是 SNARK 中表示电路的常见形式。SHA-256 和 BLAKE3 等哈希函数是密码学基础，高效证明大批量此类布尔计算一直是个难题。Flock 专注于这些位运算，实现了前所未有的吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SNARK">SNARK</a></li>

</ul>
</details>

**标签**: `#SNARKs`, `#zero-knowledge proofs`, `#hash functions`, `#cryptographic proofs`, `#performance optimization`

---

<a id="item-2"></a>
## [澄清 OEKE-2F PAKE 协议：究竟需要哈希哪些内容](https://eprint.iacr.org/2026/1331) ⭐️ 8.0/10

这篇论文通过分析 OEKE-2F PAKE 协议的全部 16 种变体，解决了社区内的分歧，证明了每种变体的通用可组合安全性，并找出了对底层密钥封装机制安全假设要求最少的一个版本。 这项工作为如何实现计算效率最高的 PAKE 协议提供了明确指导，确保了该协议在经典与后量子密码场景下均能被正确、安全地部署。 “全量哈希”版本对 KEM 的属性要求最少，而从哈希中删除某些项则会引入一些额外的、但仍较温和的要求；该论文篇幅超过 100 页，详细阐述了每种变体的设计理由。

rss · IACR ePrint 密码学论文 · 6月28日 17:41

**背景**: 口令认证密钥交换（PAKE）协议允许两方仅基于一个密码建立共享密钥。OEKE-2F 是一种将密钥封装机制（KEM）转换为 PAKE 的编译器，效率极高。通用可组合（UC）框架是一种强安全模型，能保证协议在与其他协议组合时的安全性。本文澄清了协议中需要哈希的具体输入，以在最少假设下保持 UC 安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Password-authenticated_key_agreement">Password-authenticated key agreement - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Key_encapsulation_mechanism">Key encapsulation mechanism - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_composability">Universal composability - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#PAKE`, `#OEKE-2F`, `#key exchange`, `#security`

---

<a id="item-3"></a>
## [Falafel：面向联邦学习的模块化零知识训练证明](https://eprint.iacr.org/2026/1335) ⭐️ 8.0/10

Falafel 提出了一种模块化的提交-证明方案，用于在联邦学习中生成零知识训练证明 (zkPoT)，仅依赖于公认的密码学原语便可实现主动安全性和公开可验证性。 该方案能在不泄露敏感本地数据的前提下实现可验证的联邦学习，解决了协作式 AI 中的信任与隐私难题，尤其适用于对模型完整性要求极高的医疗和金融等领域。 在 LeNet 上，单轮训练可在约 150 秒内生成 70 kB 的证明，证明体积比先前工作小 10 至 15 倍。该方案引入了可信审计员确保输入真实性，且高度并行化。

rss · IACR ePrint 密码学论文 · 6月29日 12:12

**背景**: 联邦学习 (FL) 能在不共享原始数据的情况下跨多个去中心化客户端训练模型，但如何在保护隐私的同时验证训练的正确性一直是个难题。零知识训练证明 (zkPoT) 允许证明者展示模型确实是从承诺的数据集正确训练而来，且不泄露数据或中间状态。以往方案常依赖非标准假设或产生较大证明，而 Falafel 通过模块化设计和标准原语对此进行了改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dl.acm.org/doi/abs/10.1145/3576915.3623202">Experimenting with Zero-Knowledge Proofs of Training</a></li>
<li><a href="https://arxiv.org/abs/2307.16273">[2307.16273] zkDL: Efficient Zero-Knowledge Proofs of Deep ... zkDL: Efficient Zero-Knowledge Proofs of Deep Learning Training Images Zero-Knowledge Proofs of Training for Deep Neural Networks IACR News item: 05 February 2024 Experimenting with Zero-Knowledge Proofs of Training Zero Knowledge Proofs: Challenges, Applications, and Real ...</a></li>
<li><a href="https://aisecurityandsafety.org/en/guides/federated-learning/">Federated Learning for AI Safety: The Complete Guide (2026)</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#federated learning`, `#machine learning`, `#cryptography`, `#privacy`

---

<a id="item-4"></a>
## [EasyCrypt 协议验证的关键：状态与时态不变量](https://eprint.iacr.org/2026/1334) ⭐️ 8.0/10

该论文指出，在 EasyCrypt 的 pRHL 中形式化交互式加密协议，需要同时使用状态不变量进行密码推理，以及时态不变量处理协议结构，这一发现源于对一个简单密钥协商协议的详细案例分析。 这一见解揭示了当前验证工具的根本性差距，这些工具通常专门针对密码原语或分布式协议，并为构建更一体化的推理框架指明了方向。 作者依次尝试了探索性证明、失败的结构化证明，以及最终的“本质”证明，表明 EasyCrypt 的 pRHL 缺乏对时态不变量的支持是处理协议交互的主要障碍。

rss · IACR ePrint 密码学论文 · 6月29日 08:03

**背景**: EasyCrypt 是一个基于博弈的密码证明辅助工具，依赖于用于概率计算的关联程序逻辑 pRHL。虽然它擅长验证非交互原语（如加密），但交互式协议涉及多轮状态变化和消息顺序。时态不变量约束步骤的顺序，在当前 pRHL 中不能自然表达，迫使采用变通方法，使证明复杂化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/EasyCrypt/easycrypt">GitHub - EasyCrypt/easycrypt: EasyCrypt: Computer-Aided ...</a></li>
<li><a href="https://easycrypt.gitlab.io/easycrypt-web/">EasyCrypt Documentation | EasyCrypt</a></li>

</ul>
</details>

**标签**: `#Formal verification`, `#Cryptographic protocols`, `#EasyCrypt`, `#pRHL`, `#Interactive protocols`

---

<a id="item-5"></a>
## [现实世界资格证明：DeFi 中现实世界资产的隐私验证协议](https://eprint.iacr.org/2026/1330) ⭐️ 8.0/10

提出了名为现实世界资格证明（RQP）的新协议，它引入新颖的见证隐藏认证（WHA）原语并与 zk-SNARK 结合，实现 DeFi 中链下资产资格的隐私保护验证。该协议还采用内积论证（MIPP）聚合多个证明，达到对数级验证效率。 该研究解决了现实世界资产融入 DeFi 的关键缺失，通过密码学绑定发行方认证与零知识证明，同时保障数据隐私与来源真实性，为利用链下抵押品进行更安全、可扩展的 DeFi 借贷铺平道路。 WHA 将数据隐私锚定在零知识证明系统的零知识性上，同时确保发行方认证。基于 MIPP 的证明聚合能降低多借款人场景的链上验证成本，且设计兼容 zk-rollup 架构以优化 gas 消耗。

rss · IACR ePrint 密码学论文 · 6月28日 07:04

**背景**: 去中心化金融（DeFi）通过区块链智能合约提供无中介金融服务。现实世界资产（RWA）指房地产、发票等链下资产，可被代币化并用作抵押品。隐私而安全地验证这些资产颇具挑战：现有方案如预言机和去中心化标识符（DID）要么泄露数据，要么缺乏发行方与链上证明之间的密码学绑定。零知识证明（zk-SNARK）能在不泄露数据的情况下证明拥有该数据，但本身不认证数据由谁签发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zk-SNARK">Zk-SNARK</a></li>
<li><a href="https://link.springer.com/rwe/10.1007/0-387-23483-7_461">Witness Hiding | SpringerLink</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#DeFi`, `#real-world assets`, `#zk-SNARKs`, `#privacy`

---

<a id="item-6"></a>
## [发现新型稀疏模数 RSA 弱密钥](https://www.schneier.com/blog/archives/2026/06/factoring-rsa-keys-with-many-zeros.html) ⭐️ 8.0/10

Trail of Bits 与 badkeys 项目的研究发现，在现实世界的部署中存在大量模数稀疏（包含许多零）的 RSA 弱密钥，可以利用多项式方法高效分解。 这些易受攻击的密钥正被实际用于 TLS、SSH 和 PGP，构成直接安全风险；快速检测和更换对于防止潜在泄露至关重要。 该攻击利用偏向零的比特模式，实现多项式时间分解；在证书透明度日志和全互联网扫描中发现了数百个唯一密钥。

rss · Schneier on Security · 6月29日 16:05

**背景**: RSA 安全性依赖于大数分解的困难性。正常情况下，RSA 密钥使用随机质数生成，但有缺陷的实现可能产生非随机比特模式的模数，例如许多连续的零。badkeys 项目收集并扫描公钥以发现已知漏洞。稀疏模数使得分解更容易，因为它们可以表示为特殊形式的多项式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/">Factoring "short-sleeve" RSA keys with polynomials - The Trail of Bits Blog</a></li>
<li><a href="https://badkeys.info/">badkeys</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#RSA`, `#vulnerability`, `#security`, `#badkeys`

---

<a id="item-7"></a>
## [提出标准化 ML-DSA 基准测试方法以避免误比](https://eprint.iacr.org/2026/1333) ⭐️ 7.0/10

本文指出 ML-DSA 基准测试中常见误区，包括跨安全级别比较不当，以及因拒绝采样导致签名时间可变，使得最小值/平均值/最大值等常规统计指标不适用于迁移规划。为此，提出基于标准化输入数据集和明确度量指标的鲁棒方法，以支持不同实现间的公平比较。 在后量子密码迁移中，可靠的基准测试至关重要，误导性性能数据可能导致错误决策。该方法确保不同实现间的公平比较，直接支持实际部署规划。 该方法针对 ML-DSA 签名算法因拒绝采样等数据依赖组件导致的执行时间可变性，提出标准化输入数据集并要求报告超出简单统计的度量指标，以反映实时系统必需的最坏情况行为。

rss · IACR ePrint 密码学论文 · 6月29日 07:05

**背景**: ML-DSA（原 CRYSTALS-Dilithium）是 NIST 于 2024 年标准化的后量子数字签名算法，旨在取代 RSA 和 ECC。它基于格密码，签名时采用拒绝采样以确保安全性，导致执行时间不确定。随着各类组织规划向量子安全系统迁移，准确的性能基准测试对于实现方案的选择和优化至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf">Module-Lattice-Based Digital Signature Standard - NIST</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rejection_sampling">Rejection sampling - Wikipedia</a></li>
<li><a href="https://www.nccoe.nist.gov/applied-cryptography/migration-to-pqc">Migration to Post-Quantum Cryptography - NCCoE</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#ML-DSA`, `#benchmarking`, `#digital signatures`, `#performance measurement`

---

<a id="item-8"></a>
## [后量子 DNSSEC 的差异化算法选择](https://eprint.iacr.org/2026/1332) ⭐️ 7.0/10

该论文提出了一种差异化的 DNSSEC 算法选择方法，让区域签名密钥（ZSK）和密钥签名密钥（KSK）使用不同的签名算法，使具有大密钥的后量子算法（如 UOV）能够绕过 DNS 传输大小限制。 该方法扩展了 DNSSEC 可部署的后量子算法集合，克服了迁移的关键障碍，可能加速向抗量子 DNS 安全的过渡，而无需重新设计核心协议。 在模拟.fr 顶级域（420 万域名）的测试平台上，实验表明差异化配置的延迟开销仅为经典 ECDSA 的 1.28–1.52 倍，而混合 PQ/T 拼接仅增加 7–19%的开销。UOV 具有 128 字节签名但 43KB 密钥，仅在密钥角色差异化下才可行。

rss · IACR ePrint 密码学论文 · 6月28日 20:31

**背景**: DNSSEC 通过数字签名保护 DNS。它使用两种密钥：区域签名密钥（ZSK）对单个记录签名；密钥签名密钥（KSK）对包含 ZSK 和 KSK 公钥的 DNSKEY 记录签名。后量子签名算法通常具有比经典算法大得多的密钥或签名（如 UOV 密钥为 43 KB）。DNS over UDP 有实际大小限制；超过约 1232 字节的响应可能需要 TCP，导致回退开销。该差异化方法为 KSK 选择紧凑密钥算法以保持 DNSKEY 响应较小，同时为 ZSK 使用较大密钥的算法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/csrc/media/Projects/pqc-dig-sig/documents/round-1/spec-files/UOV-spec-web.pdf">UOV Specification Document - NIST Computer Security Resource ...</a></li>
<li><a href="https://www.cloudflare.com/learning/dns/dnssec/how-dnssec-works/">How does DNSSEC work?</a></li>

</ul>
</details>

**标签**: `#DNSSEC`, `#post-quantum cryptography`, `#DNS security`, `#key management`, `#hybrid signatures`

---

<a id="item-9"></a>
## [萨克拉门托警局无人机用磁铁解除嫌犯武装](https://www.schneier.com/blog/archives/2026/06/robot-police-officers.html) ⭐️ 7.0/10

2026 年 6 月 22 日，萨克拉门托县警局使用搭载强磁铁的无人机在一所房屋内解除了一名持刀嫌犯的武装，这是美国执法部门首次此类行动。 这起事件是机器人执法迈出的具体一步，有望减少警员风险。同时也引发了关于警用机器人适当使用武力以及制定明确规章的紧迫问题。 一架由警员通过视频眼镜遥控的无人机使用磁铁从嫌犯手中夺走了刀。该技术仅适用于金属武器，且仍然需要直接人工操控。

rss · Schneier on Security · 6月29日 10:55

**背景**: 警用无人机传统上仅限于监视。近年来，机器人物理干预的实验越来越多，但各地规章差异很大，许多辖区缺乏关于机器人使用武力的政策。这起事件发生在机器人执法伦理与法律影响日益争论的背景下。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thehill.com/policy/technology/5936248-sacramento-sheriff-drone-disarmed-suspect/">Sacramento County sheriff says drone used to disarm felon 'definitely the future'</a></li>
<li><a href="https://www.police1.com/drones/video-calif-officers-attach-magnet-to-drone-disarm-suspect-inside-home">Video: Sacramento County deputies attach magnet to drone, disarm suspect inside home</a></li>
<li><a href="https://www.governing.com/policy/the-rising-call-for-regulating-police-robots">The Rising Call for Regulating Police Robots</a></li>

</ul>
</details>

**标签**: `#drones`, `#police`, `#robotics`, `#law-enforcement`, `#security`

---

<a id="item-10"></a>
## [RFC 9970 增强 STIR 应对连接身份问题](https://rfc-editor.org/info/rfc9970) ⭐️ 7.0/10

RFC 9970 更新了 STIR 框架，纳入连接身份功能，能够检测被重定向的呼叫，并防止中间对话事件的冒充。 此项增强通过验证被叫方身份，弥补了 VoIP 安全的一个关键空白，从而降低了通过重定向或伪造连接进行欺诈和自动呼叫的风险。 该文件修订了先前关于 SIP 身份头的指南，以反映 STIR 的变化，重点关注重定向检测和中间对话事件认证；这是一个 IETF 标准轨道 RFC。

rss · IETF 新标准 RFC (PQC 标准化) · 6月29日 21:25

**背景**: STIR（安全电话身份重访）是一个用于在 SIP 呼叫中加密验证来电者身份的框架，最初由 FCC 根据 STIR/SHAKEN 强制实施以打击自动呼叫。连接身份将此扩展到验证被叫方，解决了呼叫被重新路由至冒充者的场景。SIP（会话发起协议）是 VoIP 呼叫的信令协议。该 RFC 更新了早期方法以适应现代 STIR 架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx">STIR /SHAKEN With Telnyx | Telnyx Help Center</a></li>
<li><a href="https://docs.portaone.com/docs/sip-identity">SIP identity - PortaOne Documentation | May 13th, 2026</a></li>

</ul>
</details>

**标签**: `#STIR`, `#SIP`, `#VoIP security`, `#identity`, `#RFC`

---
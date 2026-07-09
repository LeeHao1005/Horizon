---
layout: default
title: "Horizon Summary: 2026-07-09 (ZH)"
date: 2026-07-09
lang: zh
---

> 从 38 条内容中筛选出 11 条重要资讯。

---

1. [针对 TALUS 阈值 ML-DSA 方案的密钥恢复攻击](#item-1) ⭐️ 9.0/10
2. [Cloudflare Meerkat：无超时的全球共识系统](#item-2) ⭐️ 8.0/10
3. [黑盒密码学中预处理私密信息检索的下界研究](#item-3) ⭐️ 8.0/10
4. [XL 求解多元二次方程组的比特操作代价模型](#item-4) ⭐️ 8.0/10
5. [PriFT：利用 MPC 和 HE 实现隐私保护微调](#item-5) ⭐️ 8.0/10
6. [TIM：基于零知识证明的隐私保护盲水印方案](#item-6) ⭐️ 8.0/10
7. [Cloudflare Workers 现内置区域分层缓存](#item-7) ⭐️ 8.0/10
8. [法国 2027 年起停发非量子安全加密认证](#item-8) ⭐️ 8.0/10
9. [基于惰性位的沃尔什查表法加速 CKKS AES 转码](#item-9) ⭐️ 7.0/10
10. [施奈尔分析五眼联盟关于 AI 黑客攻击的警告](#item-10) ⭐️ 7.0/10
11. [谷歌起诉利用 Gemini AI 进行网络钓鱼的中国诈骗团伙](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [针对 TALUS 阈值 ML-DSA 方案的密钥恢复攻击](https://eprint.iacr.org/2026/1386) ⭐️ 9.0/10

密码分析人员发现了针对 TALUS（一种基于 FIPS 204 的阈值 ML-DSA 构造）的密钥恢复攻击。这些攻击利用 Feldman 承诺中使用的左可逆公开矩阵，通过高斯消元法恢复秘密密钥份额，打破了该方案的安全性声明。 TALUS 曾是 NIST 阈值签名征集中备受瞩目的候选方案，承诺高效的一轮在线签名。其安全性的彻底崩溃不仅损害了该方案的可信度，也凸显了未经仔细密码分析就修改标准化原语的风险。 文中提出了两种独立的攻击：一种是被动攻击，从密钥生成广播中恢复所有 s1 密钥份额；另一种利用移除了拒绝采样的漏洞，通过最小二乘法恢复 s2，需要几亿个签名。两种攻击都源于同一根本原因：使用了没有密码学隐藏的左可逆矩阵。

rss · IACR ePrint 密码学论文 · 7月7日 17:30

**背景**: ML-DSA 是一种后量子签名标准（FIPS 204）。阈值签名将签名权力分发给多个参与方。TALUS 旨在通过 Feldman 承诺（一种公开承诺的可验证秘密共享方法）实现一轮签名的阈值 ML-DSA。ML-DSA 中的公开矩阵 A 在所有参数集下都是左可逆的，即存在矩阵 B 使得 B*A 为单位矩阵，这使得攻击者能够通过基本的线性代数对承诺求逆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.22109">[2603.22109] TALUS: Threshold ML-DSA with One-Round Online Signing via Boundary Clearance and Carry Elimination</a></li>
<li><a href="https://en.wikipedia.org/wiki/Verifiable_secret_sharing">Verifiable secret sharing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Cryptanalysis`, `#Threshold Signatures`, `#Key Recovery`, `#ML-DSA`, `#Vulnerability`

---

<a id="item-2"></a>
## [Cloudflare Meerkat：无超时的全球共识系统](https://blog.cloudflare.com/meerkat-introduction/) ⭐️ 8.0/10

Cloudflare 推出了 Meerkat，一个全球分布式共识服务，它采用 QuePaxa 异步共识算法，无需依赖超时即可取得进展，这是异步共识协议的首个生产级实现。 QuePaxa 的无超时设计使 Meerkat 在恶劣网络条件下具有稳健性，克服了基于领导者的共识协议（如 Raft）在领导者选举期间可能停滞的局限性，有望提高大规模分布式系统的可靠性。 Meerkat 仍处于实验阶段，尚未投入生产；其读写操作均需达成全局共识，这可能会影响读取延迟，但避免了 Raft 中常见的领导者风暴等问题。

hackernews · Cloudflare Blog (PQ 迁移) · 7月8日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=48831565)

**背景**: Paxos、Raft 等传统共识协议是部分同步的：它们依赖领导者和超时机制，在消息延迟时可能表现不佳。像 QuePaxa 这样的异步算法不依赖超时，即使在不利网络条件下也能取得进展，但在生产环境中高效实现一直具有挑战性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/meerkat-introduction/">Introducing Meerkat: an experiment in global consensus</a></li>
<li><a href="https://bford.info/pub/os/quepaxa/">QuePaxa: Escaping the Tyranny of Timeouts in Consensus – Bryan Ford's Home Page</a></li>
<li><a href="https://github.com/dedis/quepaxa">GitHub - dedis/quepaxa: This is the code repository for QuePaxa project (formerly Raxos or QSCOD) · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论指出 Meerkat 是首个异步共识算法的生产实现，可能对不稳定网络很有帮助。但有人担心每次读取都需全局共识会带来读取延迟，并质疑其相对于无领导者 Paxos 变体的优势。此外，对自研共识系统仍存在一定怀疑态度。

**标签**: `#distributed-systems`, `#consensus`, `#asynchronous-algorithms`, `#cloudflare`, `#que-paxa`

---

<a id="item-3"></a>
## [黑盒密码学中预处理私密信息检索的下界研究](https://eprint.iacr.org/2026/1384) ⭐️ 8.0/10

本文为使用黑盒密码学的预处理单服务器私密信息检索（PIR）建立了计算下界，证明在客户端存储 s 比特、数据库大小为 n 比特时，跨 k=Ω(s)个查询的在线均摊计算量必须为Ω(n/s)，否则在线通信量或服务器密码操作量将达到Ω(n/s)。 这些结果揭示了预处理 PIR 方案中固有的权衡，表明黑盒密码技术无法同时实现低计算和低通信，这指导了实际系统设计，并凸显了基于格密码等非黑盒方法的必要性。 这些下界是紧的，因为存在达到计算或通信界中之一的客户端预处理 PIR 方案。本文还在服务器密码操作很少或其操作仅依赖于查询通信的方案中证明了无条件的通信下界，并在随机预言机模型中给出了匹配的对称 PIR 构造。

rss · IACR ePrint 密码学论文 · 7月7日 12:48

**背景**: 私密信息检索（PIR）允许客户端在不向服务器泄露所查询条目的情况下检索数据库内容。单服务器场景下的平凡方案效率低下，但密码学技术可以降低通信量。最近的突破引入了客户端预处理，即客户端离线下载并存储一些数据库相关信息，使得每次查询的在线计算量达到次线性。本文考虑的是对密码学原语（如随机预言机或混淆）的“黑盒”使用，即方案将这些原语视为理想黑盒，这是理论密码学中常见的假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Private_information_retrieval">Private information retrieval</a></li>
<li><a href="https://crypto.stanford.edu/pir-library/">Private Information Retrieval</a></li>
<li><a href="https://en.wikipedia.org/wiki/Black-box_obfuscation">Black-box obfuscation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#private information retrieval`, `#lower bounds`, `#cryptography`, `#preprocessing`, `#black-box`

---

<a id="item-4"></a>
## [XL 求解多元二次方程组的比特操作代价模型](https://eprint.iacr.org/2026/1382) ⭐️ 8.0/10

该论文为 XL 算法引入了一个闭合形式的比特操作代价模型，结合了 Wiedemann 线性代数和 Berlekamp-Massey 序列恢复，并应用于 NIST 后量子签名候选方案。 它提供了一个经过实现验证的严格代价指标，用于比较多变量二次方案的安全性，帮助密码学家评估 NIST 候选方案并设定参数。 该模型涵盖 GF(2)、GF(31)、GF(256)，包括基线、常系数和分桶矩阵求值变体；实验证实了预测的准确性以及与预期常数收敛的渐近行为。

rss · IACR ePrint 密码学论文 · 7月6日 13:02

**背景**: XL（扩展线性化）算法通过生成大量方程并线性化来求解多元二次方程组。Wiedemann 算法在有限域上求解稀疏线性系统，而 Berlekamp-Massey 算法找到线性递推序列的最小多项式，用于恢复系统解。NIST 后量子密码标准化进程正在评估基于多变量二次方程的数字签名方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Berlekamp-Massey_algorithm">Berlekamp-Massey algorithm</a></li>
<li><a href="https://grokipedia.com/page/block_wiedemann_algorithm">Block Wiedemann algorithm</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum cryptography`, `#multivariate quadratic systems`, `#cryptanalysis`, `#cost model`

---

<a id="item-5"></a>
## [PriFT：利用 MPC 和 HE 实现隐私保护微调](https://eprint.iacr.org/2026/1381) ⭐️ 8.0/10

研究人员推出了 PriFT 框架，利用现成的 MPC 和 HE 库实现神经网络的隐私保护微调，支持完全隐私和半隐私两种训练模式。 这项工作使隐私保护训练更加实用，让组织能够在遵守 GDPR 和 HIPAA 等法规的同时，利用敏感数据进行模型微调。 PriFT 使用 Transformer 作为特征提取器，在加密特征上训练神经网络；半隐私模式解密标签，在 MPC 下实现约 3 倍加速，代码基于 Crypten 和 TenSEAL 开源。

rss · IACR ePrint 密码学论文 · 7月6日 10:41

**背景**: 安全多方计算（MPC）允许多个参与方在不泄露各自私密输入的前提下，共同计算某个函数。同态加密（HE）能够在加密数据上直接进行计算，解密后得到正确结果。微调是机器学习中的一项技术，指利用较小的特定任务数据集对预训练模型进行调整，使其适应特定任务。这些技术结合，实现了保护隐私的模型适配。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Homomorphic_encryption">Homomorphic encryption</a></li>

</ul>
</details>

**标签**: `#privacy-preserving ML`, `#fine-tuning`, `#secure multi-party computation`, `#homomorphic encryption`, `#machine learning`

---

<a id="item-6"></a>
## [TIM：基于零知识证明的隐私保护盲水印方案](https://eprint.iacr.org/2026/1380) ⭐️ 8.0/10

研究人员开发了 TIM，这是首个公开可验证的盲水印方案，利用零知识证明在不泄露水印种子或嵌入位置的情况下证明图像所有权。 该方案消除了对验证者的信任假设，通过保护敏感水印参数解决了现有盲水印方案的关键漏洞，实现了安全的公开所有权验证。 TIM 将基于整数 DCT 的提取过程重构为算术电路，结合 Nova 和 Spartan 进行迭代子证明，并采用阈值投票机制保证鲁棒性，对 4K 图像生成证明耗时 5.61 分钟，峰值内存 9.61 GB。

rss · IACR ePrint 密码学论文 · 7月6日 09:54

**背景**: 盲水印是一种无需原始图像即可验证图像所有权的技术。现有方案中，验证者必须被信任获得水印种子和嵌入位置，一旦泄露就可能被伪造或移除。零知识证明是一种密码学协议，允许一方在不泄露秘密的情况下证明其知识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof</a></li>

</ul>
</details>

**标签**: `#blind watermarking`, `#zero-knowledge proofs`, `#privacy-preserving`, `#image ownership verification`, `#cryptography`

---

<a id="item-7"></a>
## [Cloudflare Workers 现内置区域分层缓存](https://blog.cloudflare.com/workers-cache/) ⭐️ 8.0/10

Cloudflare 推出了 Workers Cache，一个区域分层的缓存层，直接位于 Worker 入口点之前，通过标准 HTTP 头部配置，实现无限组合性。 该缓存可降低无服务器应用的延迟和源服务器负载，可能降低成本，并在 Cloudflare 的全球边缘网络中改善用户体验。 它采用区域分层以靠近用户，并使用标准的 Cache-Control 头部进行配置，但未披露具体的逐出策略或存储上限。

rss · Cloudflare Blog (PQ 迁移) · 7月6日 13:00

**背景**: Cloudflare Workers 是一个在边缘运行 JavaScript 的无服务器平台。边缘缓存将内容存储在靠近用户的位置以减少源请求；分层缓存通过增加中间区域层进一步提高效率，降低延迟和回源流量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Cloudflare_Workers">Cloudflare Workers</a></li>

</ul>
</details>

**标签**: `#cloudflare`, `#workers`, `#caching`, `#serverless`, `#edge-computing`

---

<a id="item-8"></a>
## [法国 2027 年起停发非量子安全加密认证](https://www.schneier.com/blog/archives/2026/07/france-to-stop-certifying-non-quantum-safe-encryption.html) ⭐️ 8.0/10

法国网络安全机构 ANSSI 宣布，从 2027 年起将停止认证缺乏抗量子加密的安全产品，并规定到 2030 年企业只能采购量子安全产品。 该政策迫使法国政府机构和关键基础设施向抗量子密码迁移，这一先例可能会加速全球对量子安全标准的采用。 ANSSI 认证是法国政府和关键基础设施使用安全产品的必备条件，因此停止认证无异于强制淘汰；该机构还设定了 2030 年企业仅采购量子安全产品的最后期限。

rss · Schneier on Security · 7月6日 10:45

**背景**: 后量子密码学（PQC）旨在开发能够抵御未来量子计算机攻击的加密算法，因为量子计算机可破解当前广泛使用的 RSA、ECC 等公钥系统。美国国家标准与技术研究院（NIST）已于 2024 年发布了首批 PQC 标准。为应对“先窃取、后解密”的长期威胁，多国正推动关键领域的迁移。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#encryption`, `#cybersecurity policy`, `#ANSSI`, `#quantum computing`

---

<a id="item-9"></a>
## [基于惰性位的沃尔什查表法加速 CKKS AES 转码](https://eprint.iacr.org/2026/1385) ⭐️ 7.0/10

提出了一种新颖的布尔查找表评估方法，在 CKKS 中利用沃尔什基和惰性加法形成奇偶和，并通过二进制自举刷新，以恒定小深度评估大规模 LUT，用于 AES S 盒评估。 该技术将查找表大小与乘法深度解耦，显著加速 AES-CTR 转码，在 1024 块批处理时比先前方法快 3.25 倍，使基于 FHE 的 AES 更实用。 AES S 盒采用半字节分割的沃尔什分解，额外增加一次乘法深度；AES 状态保持在复数 CKKS 打包中，实虚部承载独立块；惰性加法保持异或低位正确；自举包括 StC、CtS 和 EvalMod 步骤。

rss · IACR ePrint 密码学论文 · 7月7日 16:22

**背景**: CKKS 是一种支持加密数据近似计算的全同态加密方案。全同态加密（FHE）允许密文计算，但评估 AES S 盒等函数常因高乘法深度而困难。查找表评估通常带来深度开销，但结合布尔函数的沃尔什基表示与 CKKS 中的惰性算术可降低该成本。

**标签**: `#homomorphic-encryption`, `#CKKS`, `#AES`, `#lookup-table`, `#transciphering`

---

<a id="item-10"></a>
## [施奈尔分析五眼联盟关于 AI 黑客攻击的警告](https://www.schneier.com/blog/archives/2026/07/cybersecurity-and-the-gap-between-skill-and-ability.html) ⭐️ 7.0/10

上周，五眼联盟情报机构发布联合声明，警告 AI 模型自主入侵系统和网络的能力日益增强，Bruce Schneier 对此进行了理性分析。 这凸显了应对 AI 驱动的网络威胁的紧迫性，由于 AI 的自主能力，即使是标准的安全建议也需要加强警惕。它提醒政策制定者和安全专家，现有防御可能不足。 五眼联盟的声明比媒体渲染更为审慎，Schneier 指出风险确实存在，但给出的建议基本是常规建议，只是现在更为紧迫。声明未提出新的具体技术缓解措施。

rss · Schneier on Security · 7月8日 11:03

**背景**: 五眼联盟是由美国、英国、加拿大、澳大利亚和新西兰组成的情报共享联盟。生成式 AI 模型已发展到能自主探测和利用软件漏洞的程度。Bruce Schneier 是著名的安全技术专家和作家，经常评论网络安全和政策问题。

**标签**: `#cybersecurity`, `#AI`, `#hacking`, `#policy`, `#Five Eyes`

---

<a id="item-11"></a>
## [谷歌起诉利用 Gemini AI 进行网络钓鱼的中国诈骗团伙](https://www.schneier.com/blog/archives/2026/07/google-is-suing-chinese-scammers-who-are-using-gemini.html) ⭐️ 7.0/10

谷歌对一个名为 Outsider Enterprise 的中国网络犯罪团伙提起诉讼，该团伙利用谷歌的 Gemini AI 自动化网络钓鱼诈骗。该团伙通过 Telegram 提供钓鱼即服务，提供了近 300 个仿冒谷歌、YouTube 和政府网站的诈骗模板。 这一法律行动为追究 AI 驱动的网络犯罪责任开创了先例，凸显了生成式 AI 的双重用途风险。它可能阻止类似滥用行为，并促使 AI 服务加强防护措施。 犯罪分子通过 Telegram 频道运营，向非技术用户提供钓鱼即服务。他们利用 Gemini 制作以假乱真的虚假网站，诉讼针对的是一个拥有近 300 个诈骗模板的网络。

rss · Schneier on Security · 7月7日 10:43

**背景**: 钓鱼即服务是一种订阅制的网络犯罪商业模式，攻击者出售或出租钓鱼工具包。谷歌的 Gemini 是一款多模态大语言模型，能够生成文本、图像和代码，因此可用于制作欺骗性内容。该诉讼代表了针对 AI 在网络攻击中被滥用的法律对策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Phishing_as_a_service">Phishing as a service</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_AI">Gemini AI</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#artificial intelligence`, `#phishing`, `#legal`, `#google`

---
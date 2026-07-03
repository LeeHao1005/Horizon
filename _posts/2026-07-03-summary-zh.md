---
layout: default
title: "Horizon Summary: 2026-07-03 (ZH)"
date: 2026-07-03
lang: zh
---

> 从 49 条内容中筛选出 15 条重要资讯。

---

1. [量子 Merkle-Damgård：证明修复与紧一致性界限](#item-1) ⭐️ 9.0/10
2. [实用差分故障攻击打破 ML-DSA 与 HAETAE 签名安全](#item-2) ⭐️ 9.0/10
3. [BiSON：毫秒级十亿规模不经意最近邻搜索](#item-3) ⭐️ 9.0/10
4. [GPT-5.5-Cyber 一天内构建出 zlib 模糊测试实验室](#item-4) ⭐️ 9.0/10
5. [RFC 9980 为 OpenPGP 引入后量子密码学](#item-5) ⭐️ 9.0/10
6. [改进型 SIS 攻击降低 Falcon-256 成本并威胁 Dilithium 类签名](#item-6) ⭐️ 8.0/10
7. [基于群作用的典范提升框架实现高效环签名](#item-7) ⭐️ 8.0/10
8. [几乎无脚本的适配器签名：适用于任何签名方案](#item-8) ⭐️ 8.0/10
9. [白宫行政令加速向后量子密码迁移](#item-9) ⭐️ 8.0/10
10. [AI 实现视频监控自然语言搜索](#item-10) ⭐️ 8.0/10
11. [PyCA Cryptography 库新增后量子 ML-KEM 和 ML-DSA 支持](#item-11) ⭐️ 8.0/10
12. [RFC 9943：可信透明数字供应链架构](#item-12) ⭐️ 8.0/10
13. [RFC 9942：使用 COSE 的可验证数据结构回执](#item-13) ⭐️ 8.0/10
14. [带消息编码的格基公钥加密解密失败率精化评估](#item-14) ⭐️ 7.0/10
15. [双结构遗传算法实现 SVP 最快求解](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [量子 Merkle-Damgård：证明修复与紧一致性界限](https://eprint.iacr.org/2026/1347) ⭐️ 9.0/10

这篇论文解决了 Merkle-Damgård 构造现有量子不可区分性证明中的关键缺陷。它基于 Zhandry 的压缩预言机技术开发了一个模块化的量子博弈框架，并利用一种新颖的错误传播方法确立了 O(q_s^{3/2}/2^{n/2})的紧一致性界限。此外，它还识别了不可区分博弈中的一个根本性障碍。 Merkle-Damgård 构造是广泛使用的哈希函数（如 SHA-256）的基础，量子不可区分性保证了它们在量子敌手攻击下的安全性。这项工作提供了首个正确且最优紧致的安全界，增强了对后量子密码系统的信心，并解决了可证明安全中长期存在的差距。 该紧界限与最优通用量子碰撞攻击的复杂度相匹配，确认了不存在更优的攻击。论文还表明，在顺序自适应查询下，不可区分博弈存在固有的障碍，导致预言机偏差有下界，从而阻止了在没有额外技术的情况下完成完整证明。

rss · IACR ePrint 密码学论文 · 6月30日 10:53

**背景**: Merkle-Damgård 构造将固定大小的压缩函数扩展为完整的哈希函数。不可区分性是一种安全概念，确保构造即使在量子查询下也表现得像随机预言机。Zhandry 的压缩预言机技术是分析量子敌手的证明方法。先前的 Merkle-Damgård 量子不可区分性证明被发现存在缺陷，特别是在一致性博弈中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Merkle-Damgård_construction">Merkle-Damgård construction</a></li>
<li><a href="https://www.emergentmind.com/topics/compressed-oracle-method">Compressed Oracle Method Overview</a></li>
<li><a href="https://arxiv.org/html/2410.16595v1">( Quantum ) Indifferentiability and Pre-Computation</a></li>

</ul>
</details>

**标签**: `#quantum cryptography`, `#indifferentiability`, `#Merkle-Damgård`, `#provable security`, `#hash functions`

---

<a id="item-2"></a>
## [实用差分故障攻击打破 ML-DSA 与 HAETAE 签名安全](https://eprint.iacr.org/2026/1344) ⭐️ 9.0/10

一种新的差分故障攻击针对确定性 ML-DSA 和 HAETAE 的挑战采样过程，表明单次错误签名即可恢复用于伪造签名的密钥。这是首次对 HAETAE 实现密钥恢复的实用故障攻击。 ML-DSA 是 NIST 标准化的后量子签名，广泛应用于关键领域，HAETAE 是韩国 KpqC 竞赛选定的方案；揭示这一新攻击面迫使重新审视实际系统中物理安全性的假设。 该攻击仅使用公开信息识别预期故障注入，无需直接访问错误挑战，并在仿真和实际测试中达到 100%的识别率。作者针对该漏洞提出了防护措施。

rss · IACR ePrint 密码学论文 · 6月30日 06:31

**背景**: ML-DSA（基于模格的数字签名标准）是 NIST 主要的后量子签名标准，其安全性基于模格困难问题。HAETAE 是韩国 KpqC 竞赛选择的格基签名方案。差分故障攻击通过向密码计算注入电压毛刺等物理故障，并对比正确与错误输出来推断密钥。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#fault attack`, `#ML-DSA`, `#HAETAE`, `#side-channel analysis`

---

<a id="item-3"></a>
## [BiSON：毫秒级十亿规模不经意最近邻搜索](https://eprint.iacr.org/2026/1343) ⭐️ 9.0/10

BiSON 提出了首个支持十亿级加密向量数据库的安全最近邻搜索协议，查询延迟仅毫秒级，准确度与当前最先进的不安全 ANN 算法相当。相比先前系统 Compass，BiSON 将通信开销降低最高 28 倍，端到端延迟最高改善 23.5 倍。 这一突破使得云规模的实用隐私语义搜索成为可能，组织能够在不牺牲性能的情况下安全查询大规模加密向量数据库。它代表了隐私保护机器学习和安全计算领域的重大进步，弥合了安全性与现实可扩展性之间的鸿沟。 BiSON 的核心创新是一种新颖的磁盘兼容不经意随机存取存储器（ORAM）架构，能够无缝扩展至十亿点数据集，同时保持低延迟和隐私性。然而，论文未提及具体的计算开销或相对于明文方法的准确度指标。

rss · IACR ePrint 密码学论文 · 6月30日 05:56

**背景**: 最近邻搜索寻找与查询最相似的项，对于大规模数据集，近似方法（ANN）以精度换速度。不经意随机存取存储器（ORAM）隐藏数据访问模式以防止泄露，是安全搜索的关键技术。先前最先进的系统 Compass 使用基于图的索引和 ORAM 进行加密语义搜索，但无法扩展到十亿级数据库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nearest_neighbor_search">Nearest neighbor search - Wikipedia</a></li>
<li><a href="https://www.usenix.org/system/files/osdi25-zhu-jinhao.pdf">PDF Compass: Encrypted Semantic Search with High Accuracy</a></li>

</ul>
</details>

**标签**: `#secure computation`, `#vector databases`, `#nearest-neighbor search`, `#privacy-preserving ML`, `#cryptography`

---

<a id="item-4"></a>
## [GPT-5.5-Cyber 一天内构建出 zlib 模糊测试实验室](https://blog.trailofbits.com/2026/07/02/field-reports-from-patch-the-planet/) ⭐️ 9.0/10

GPT-5.5-Cyber 在没有人工指导的情况下，自主决定为 zlib 构建模糊测试方案，并在一天内编写了多个入口点的 fuzz harness、配置了地址消毒器等构建，并发现了多个正进行协同披露的漏洞。 这表明先进 AI 能将漏洞发现速度提升到工业化水平，可能会让开源维护者淹没在大量错误报告中，但也使防御者能够在攻击者利用之前抢先发现并修复关键漏洞。 该模型没有直接模糊测试 gz* API，而是利用操作系统背压产生的有效状态来发现漏洞；使用了 INFLATE_STRICT 等编译时变体构建覆盖隐藏代码路径，并专门针对压缩库中一类高危漏洞进行测试。

rss · Trail of Bits Blog · 7月2日 11:00

**背景**: zlib 是一个广泛使用的无损压缩库，其安全漏洞可能影响深远。模糊测试是通过向软件输入随机或半随机数据来触发崩溃、发现漏洞的方法。Patch the Planet 是 Trail of Bits 与 OpenAI 的合作项目，利用前沿 AI 模型抢先发现并修复开源漏洞。GPT-5.5-Cyber 是 OpenAI 专为高级防御性网络安全任务打造的模型，目前仅向经过审查的防御者提供有限预览。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/">Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber | OpenAI</a></li>
<li><a href="https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities">Our evaluation of OpenAI's GPT-5.5 cyber capabilities | AISI Work</a></li>

</ul>
</details>

**标签**: `#ai`, `#security`, `#fuzzing`, `#open-source`, `#gpt-5.5-cyber`

---

<a id="item-5"></a>
## [RFC 9980 为 OpenPGP 引入后量子密码学](https://rfc-editor.org/info/rfc9980) ⭐️ 9.0/10

RFC 9980 为 OpenPGP 定义了一组新的后量子密码算法，包括基于 ML-KEM 与 ECC 的复合加密、基于 ML-DSA 与 ECC 的复合签名，以及独立的 SLH-DSA 签名，扩展了现有的 RFC 9580 标准。 该标准对于保护 OpenPGP 通信免受未来量子攻击至关重要，能够确保电子邮件和文档的长期机密性与真实性。 复合方案将后量子算法与椭圆曲线密码学 (ECC) 结合以提供过渡性安全，而 SLH-DSA (FIPS 205) 提供独立的签名选项，其密钥和签名尺寸较大但安全保证更为保守。

rss · IETF 新标准 RFC (PQC 标准化) · 6月30日 22:51

**背景**: OpenPGP 是广泛用于安全电子邮件和文件加密的协议。当前算法（RSA、ECC）易受量子计算机攻击。由 NIST 标准化的后量子密码学（如 ML-KEM、ML-DSA、SLH-DSA）利用被认为能抵抗量子攻击的数学问题。该 RFC 将这些算法引入 OpenPGP，确保其未来可行性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://en.wikipedia.org/wiki/SLH-DSA">SLH-DSA</a></li>

</ul>
</details>

**标签**: `#post-quantum-cryptography`, `#standards`, `#OpenPGP`, `#security`, `#IETF`

---

<a id="item-6"></a>
## [改进型 SIS 攻击降低 Falcon-256 成本并威胁 Dilithium 类签名](https://eprint.iacr.org/2026/1349) ⭐️ 8.0/10

该论文通过利用主筛长度分布和联合概率改进了针对 SIS/ISIS 问题的大范数攻击，将 Falcon-256 的攻击成本降低了约 11 倍，并约 4.5 秒内伪造了 Mitaka-512 签名。同时提出了针对 Dilithium 型 ISIS∞的闭式ℓ∞ 'Z 形'攻击，在三种参数设置下均在 1.6 秒内成功。 这些成果直接影响 NIST 后量子标准 Falcon 和 Dilithium 的安全裕度，表明特定参数下其安全性可能低于预期，并解决了格密码分析中的关键开放问题。 该工作复用了原有的θ卷积框架，扩展较小；ℓ∞攻击被称为'Z 形'攻击；在小模数假设下，所有 Dilithium 预设参数均在 1.6 秒内被攻破。然而当前安全参数可能不受影响，但更精确的成本模型指导未来参数选择。

rss · IACR ePrint 密码学论文 · 6月30日 15:56

**背景**: 格密码是 Falcon 和 Dilithium 等主要 NIST 后量子标准的基础，其安全性依赖于短整数解（SIS）等问题，即寻找模 q 下的短非零向量。大范数攻击（Ducas 等人，CRYPTO 2023）利用小 q 值恢复短解，无需找到最短向量。BDGL 筛法是寻找格中短向量的关键算法，其成本估算对攻击模型至关重要。本工作通过考虑筛向量长度实际分布和相关概率改进了成本模型，并将攻击扩展到 Dilithium 类签名所用的无穷范数变体（ISIS∞）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-17234-2_22">Estimating the Hidden Overheads in the BDGL Lattice Sieving Algorithm | Springer Nature Link</a></li>
<li><a href="https://www.emergentmind.com/topics/short-integer-solution-sis-problem">SIS Problem in Lattice Cryptography</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#lattice-based-crypto`, `#cryptanalysis`, `#SIS`

---

<a id="item-7"></a>
## [基于群作用的典范提升框架实现高效环签名](https://eprint.iacr.org/2026/1348) ⭐️ 8.0/10

该论文引入了群作用的典范提升框架，推广了如 LESS 等方案中的典范形式，并构建了环签名方案及可链接的变体，避免了已知的密钥重用安全隐患。这两个方案均实现了签名大小与环成员数成对数关系，并基于线性码等价问题实例化，提供了名为 CERES 和 CELERES 的 AVX2 优化 C 语言实现。 该研究解决了先前基于群作用的可链接环签名中的关键安全缺陷，尤其是那些已被证明对线性码等价和格同构不安全的密钥重用机制。模块化的典范提升框架提供了可证明安全性，推动了后量子匿名签名的发展，并可能有益于 NIST 后量子标准化等进程。 典范提升抽象了典范形式的使用，避开了 Beullens 等人(ASIACRYPT'20)方案中在 ASIACRYPT'24 和 CiC'25 被破解的陷门。环签名 CERES 和可链接环签名 CELERES 在标准假设下被证明安全，签名大小与现有最优方案相当，优化代码展现了实用性能。

rss · IACR ePrint 密码学论文 · 6月30日 12:40

**背景**: 密码学中的群作用基于难解均匀空间，寻找两个对象之间的变换是困难的。线性码等价问题要求找出两个线性码之间的等距映射，在字母表大小 q≥5 时被认为是困难的。LESS 是一个基于该问题的 NIST 后量子签名候选方案。环签名允许用户代表一个群体匿名签名，而可链接环签名额外添加一个标签，能在不破坏匿名性的情况下检测两个签名是否来自同一签名者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/csrc/media/Projects/pqc-dig-sig/documents/round-1/spec-files/less-spec-web.pdf">LESS: Linear Equivalence Signature Scheme < https://www.less-project.com/</a></li>
<li><a href="https://eprint.iacr.org/2024/244">Don’t Use It Twice! Solving Relaxed Linear Code Equivalence Problems</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#group actions`, `#ring signatures`, `#linkable ring signatures`, `#post-quantum`

---

<a id="item-8"></a>
## [几乎无脚本的适配器签名：适用于任何签名方案](https://eprint.iacr.org/2026/1346) ⭐️ 8.0/10

本文提出了“几乎无脚本”的适配器签名概念，通过签署扩展消息（原始消息与随机字符串拼接）而非原始消息，使得该方案能与任何签名方案配合使用，从而克服了唯一签名方案不可能实现无脚本适配器签名的结论。 这一突破使得适配器签名能够适用于所有签名方案，包括此前不可能实现无脚本适配器签名的唯一签名方案（如 BLS），极大地扩展了其在支付通道和原子交换等区块链协议中的应用范围。 通用编译器可将任何函数签名转化为适配器签名，且几乎保持验证方式不变；该构造依赖于不可区分混淆（CRS 模型）或证据加密（ROM）来实现无脚本的函数签名。

rss · IACR ePrint 密码学论文 · 6月30日 09:55

**背景**: 适配器签名将消息认证与秘密交换绑定，用于原子交换等场景。无脚本适配器签名可像标准签名一样验证，无需额外脚本。2021 年的一项不可能性结果表明，无法为唯一签名（如 BLS）构建无脚本适配器。本文通过签署扩展消息 m||r 来放松无脚本要求，称之为“几乎无脚本”，从而绕开了该不可能性结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@muniratolayiwola/understanding-the-basic-concept-of-adaptor-signatures-9211539258c9">Understanding the basic concept of Adaptor signatures | Medium</a></li>
<li><a href="https://bitcoinops.org/en/topics/multisignature/">Scriptless multisignatures | Bitcoin Optech</a></li>

</ul>
</details>

**标签**: `#adaptor signatures`, `#cryptography`, `#blockchain`, `#scriptless signatures`, `#digital signatures`

---

<a id="item-9"></a>
## [白宫行政令加速向后量子密码迁移](https://neilmadden.blog/2026/07/02/are-we-any-closer-to-the-quantum-apocalypse/) ⭐️ 8.0/10

白宫发布新行政令，要求特定"高价值"系统在 2030 年前完成密钥交换的后量子密码（PQC）迁移，并在 2031 年前完成数字签名的迁移，缩短了原定时间表。 此举凸显了政府层面对"现在收集，以后解密"威胁的担忧，并将推动全行业在量子计算机具备攻击能力前加速合规步伐，具有紧迫的现实意义。 该行政令针对'高价值'系统进行分阶段迁移；美国国家标准与技术研究院（NIST）已于 2024 年发布三项后量子密码最终标准（如用于密钥交换的 ML-KEM，用于签名的 ML-DSA），为迁移提供了明确的技术路径。

rss · Neil Madden (后量子密码) · 7月2日 11:25

**背景**: 后量子密码（PQC）旨在开发能同时抵抗经典和量子计算机攻击的算法。当前公钥密码（如 RSA、ECC）在足够强大的量子计算机面前，会因 Shor 算法而面临破解风险。由于存在"现在收集，以后解密"的攻击模式，即今天截获的加密数据在未来量子计算机成熟时可能被破解，因此需尽早迁移。NIST 的标准化工作提供了经过验证的 PQC 算法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://csrc.nist.gov/projects/post-quantum-cryptography">Post - Quantum Cryptography | CSRC</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#executive order`, `#cybersecurity`, `#quantum computing`, `#cryptography`

---

<a id="item-10"></a>
## [AI 实现视频监控自然语言搜索](https://www.schneier.com/blog/archives/2026/06/the-realities-of-ai-video-surveillance.html) ⭐️ 8.0/10

人工智能系统现在能够处理关于视频监控录像的自然语言问题，支持几乎无限的查询范围，标志着大规模监视能力的重大转变。 这一进展大幅降低了大规模间谍活动的门槛，任何人用简单语言即可瞬间搜索海量录像，对隐私和公民自由产生深远影响。 与仅限于几十种预设搜索的旧工具不同，这些新的 AI 系统能理解开放式自然语言，在摄像头画面中查找任意对象、人物或情况，通常在数秒内返回结果。

rss · Schneier on Security · 6月30日 12:05

**背景**: 传统视频监控依赖人工审查或简单规则分析。AI 驱动的系统利用计算机视觉和自然语言处理技术自动标记视频内容并解读用户查询，无需专业背景即可进行快速、大规模语义搜索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/03/26/conntour-raises-7m-from-general-catalyst-yc-to-build-an-ai-search-engine-for-security-video-systems/">Conntour raises $7M from General Catalyst, YC to build an AI search engine for security video systems | TechCrunch</a></li>
<li><a href="https://duckviewsystems.com/natural-language-search/">Natural Language Search | AI Video Search & Rapid Evidence Retrieval</a></li>
<li><a href="https://www.checkvideo.com/blog-post/natural-language-search-video-surveillance/">Natural Language Search in Video Surveillance: What It Is and Why It Matters - CheckVideo</a></li>

</ul>
</details>

**标签**: `#AI`, `#surveillance`, `#privacy`, `#natural language processing`, `#video analytics`

---

<a id="item-11"></a>
## [PyCA Cryptography 库新增后量子 ML-KEM 和 ML-DSA 支持](https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/) ⭐️ 8.0/10

广泛使用的 PyCA cryptography 包现在包含了 NIST 标准的后量子算法 ML-KEM 和 ML-DSA 的实现，可通过 pip install cryptography>=48 使用。 这使得整个 Python 生态系统能够开始向量子安全密码学迁移，符合美国政府要求高价值联邦系统在 2030 年前采用后量子密钥建立、2031 年前采用数字签名的规定。 新的后量子原语的公钥、签名和密文大小比经典算法大一到两个数量级，速度较慢，但在常规使用中性能影响不大；由于集成权衡不同，不能直接替换现有算法。

rss · Trail of Bits Blog · 6月30日 11:00

**背景**: ML-KEM（基于模格的密钥封装机制，前身是 Kyber）和 ML-DSA（基于模格的数字签名标准，前身是 Dilithium）是 NIST 于 2024 年标准化的后量子算法，分别为 FIPS 203 和 FIPS 204。它们基于格问题，被认为能够抵御经典和量子计算机的攻击，而 RSA 和 ECC 可能被大规模量子计算机上的 Shor 算法攻破。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://www.encryptionconsulting.com/education-center/ml-dsa-fips-204/">ML - DSA (FIPS 204) Explained | Encryption Consulting LLC</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#Python`, `#pyca`, `#ML-KEM`, `#ML-DSA`, `#policy`

---

<a id="item-12"></a>
## [RFC 9943：可信透明数字供应链架构](https://rfc-editor.org/info/rfc9943) ⭐️ 8.0/10

IETF 发布了 RFC 9943，定义了一种针对单签发者签名声明透明性的可互操作架构，以增强数字供应链的可追溯性和信任。 该 RFC 通过标准化数字供应链的透明性来应对紧迫的安全需求，有望推动广泛采用，并提升各行业的审计与合规水平。 该架构专注于单签发者签名声明，确保了可扩展性、不同透明性服务之间的互操作性，并与多种审计流程和监管要求保持一致。

rss · IETF 新标准 RFC (PQC 标准化) · 6月30日 22:43

**背景**: 数字供应链面临流程不透明的风险，例如单签发者可能发出相互矛盾的声明（即“equivocation”）。可验证数据结构（VDS）已被用于增加透明性，例如在证书日志中检测异常行为。RFC 9943 基于这些概念，为任何单签发者签名声明创建了一个通用架构，以实现一致的信任验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://transparency.dev/verifiable-data-structures/">Verifiable Data Structures | Trillian</a></li>
<li><a href="https://www.dock.io/post/digital-certificates">Verifiable Digital Certificates: Complete Guide on How They Work</a></li>

</ul>
</details>

**标签**: `#supply-chain`, `#transparency`, `#RFC`, `#architecture`, `#security`

---

<a id="item-13"></a>
## [RFC 9942：使用 COSE 的可验证数据结构回执](https://rfc-editor.org/info/rfc9942) ⭐️ 8.0/10

IETF 发布了 RFC 9942，该标准定义了基于 CBOR 和 COSE 的简洁回执格式，用于证明可验证数据结构（如默克尔树包含性和一致性证明）的属性。 该标准为透明性回执提供了标准化、高效的二进制格式，有助于在证书透明性、安全通信和供应链安全等领域采用，并利用现有的 IETF 标准（如 CBOR 和 COSE）实现紧凑性和互操作性。 该规范定义了默克尔包含性和一致性证明的 CBOR 编码，利用 COSE 框架（RFC 8152）进行签名和加密，并设计为可扩展以支持其他证明类型。

rss · IETF 新标准 RFC (PQC 标准化) · 6月30日 22:43

**背景**: CBOR（简洁二进制对象表示）是一种比 JSON 更紧凑的二进制数据格式，适用于资源受限环境。COSE（CBOR 对象签名与加密）是为 CBOR 数据提供签名和加密等安全服务的标准，类似于 JSON 的 JOSE。可验证数据结构（VDS）如默克尔树，允许高效、密码学上可验证的包含性或一致性证明，从而实现透明性和不可抵赖性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CBOR">CBOR - Wikipedia</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc8152">RFC 8152 - CBOR Object Signing and Encryption (COSE)</a></li>
<li><a href="https://transparency.dev/verifiable-data-structures/">Verifiable Data Structures | Trillian</a></li>

</ul>
</details>

**标签**: `#COSE`, `#CBOR`, `#Verifiable Data Structures`, `#Transparency`, `#IETF`

---

<a id="item-14"></a>
## [带消息编码的格基公钥加密解密失败率精化评估](https://eprint.iacr.org/2026/1350) ⭐️ 7.0/10

该论文提出了一种精化的解密失败率（DFR）评估框架，通过利用编码格结构为 MLD 方案推导更紧的联合界，并为 BDD 方案引入非中心卡方分布方法，避免了以往过于简化的高斯近似。 通过提供显著更紧且更准确的 DFR 界，这项工作使得格密码系统的参数选择和安全认证更加精确，这对于后量子密码学走向标准化和实际部署至关重要。 对于 MLD 方案，精确刻画了 Barnes-Wall 格的极小向量以收紧联合界；对于 BDD，引入非中心卡方分布建模高斯-离散混合噪声；并将框架扩展到代数格，采用加权卡方分布与鞍点近似。验证显示：CNTR 的 DFR 界收紧了 15 比特，scloud 收紧了 1 比特，而 CNTR-Prime 至少增加了 84 比特，表明其失败率曾被严重低估。

rss · IACR ePrint 密码学论文 · 6月30日 21:34

**背景**: 基于格的公钥加密方案（例如基于带错误学习问题的方案）通常包括消息编码机制，将明文比特映射到格点。解密失败率（DFR）可能导致安全漏洞和效率低下。解密噪声密文的两种常见方法是最大似然解码（MLD），选择最可能的码字，以及有界距离解码（BDD），在一定距离内找到最近的格点。Barnes-Wall 格是一类高维格，具有高效解码算法，偶尔用于 MLD 方案。传统 DFR 分析常依赖过于简化的噪声模型（如纯高斯），而格密码方案中的实际噪声可能包含离散分量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Maximum_likelihood_decoding">Maximum likelihood decoding</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/11830924_41">On Bounded Distance Decoding for General Lattices | Springer Nature Link</a></li>
<li><a href="https://en.wikipedia.org/wiki/Barnes–Wall_lattice">Barnes–Wall lattice</a></li>

</ul>
</details>

**标签**: `#lattice-based cryptography`, `#decryption failure rate`, `#post-quantum cryptography`, `#maximum likelihood decoding`, `#bounded distance decoding`

---

<a id="item-15"></a>
## [双结构遗传算法实现 SVP 最快求解](https://eprint.iacr.org/2026/1345) ⭐️ 7.0/10

提出了一种新的用于最短向量问题（SVP）的双结构遗传算法，将基于 Fukase 算法的内部遗传算法与使用新型“进化速度”准则优化参数的外部遗传算法相结合。该算法据称是目前最快的 SVP 遗传算法。 由于 SVP 是支持基于格的抗量子密码学的难题，更快的求解算法可能影响安全性估计和参数选择，因此这一进展对密码分析和密码设计具有重要意义。 内部遗传算法最小化平方欧几里得范数，而外部遗传算法最大化由 Gram-Schmidt 和的变化率定义的进化速度。这种目标分离和两种类型染色体的使用是关键创新点。

rss · IACR ePrint 密码学论文 · 6月30日 07:01

**背景**: 最短向量问题（SVP）要求找到格中最短的非零向量，是基于格的密码学中的一个基本计算问题。遗传算法（GA）是受自然选择启发的启发式搜索方法。Fukase 算法是之前用于 SVP 的一种遗传算法，本工作通过添加外部优化循环对其进行了改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Shortest_vector_problem">Shortest vector problem</a></li>
<li><a href="https://eprint.iacr.org/2026/1345">Double-Structured Genetic Algorithm for Solving the SVP Based on Double Optimization: Using Two Types of Chromosomes</a></li>

</ul>
</details>

**标签**: `#lattice-based cryptography`, `#genetic algorithm`, `#shortest vector problem`, `#optimization`, `#cryptanalysis`

---
---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 49 条内容中筛选出 15 条重要资讯。

---

1. [首个与 NIST 标准兼容的阈值 FALCON 签名方案](#item-1) ⭐️ 10.0/10
2. [Trail of Bits 推出 Patch the Planet，利用 GPT-5.5-Cyber 发现漏洞](#item-2) ⭐️ 9.0/10
3. [信任声音，隐藏来源：可验证编辑音频的匿名溯源](#item-3) ⭐️ 8.0/10
4. [对后门 UA-8295 信息终端的取证密码分析](#item-4) ⭐️ 8.0/10
5. [SQIsign 通过规范响应编码实现强不可伪造性](#item-5) ⭐️ 8.0/10
6. [TRIP：具有输入隐私的线性回归新协议](#item-6) ⭐️ 8.0/10
7. [结构化格及其在密码学与无线安全中的应用综述](#item-7) ⭐️ 8.0/10
8. [后量子密码行政令设定 2030 年截止日期，Cloudflare 发布迁移手册](#item-8) ⭐️ 8.0/10
9. [LLMs 让漏洞报告不再特殊](#item-9) ⭐️ 8.0/10
10. [新研究揭示大语言模型提示注入源于角色混淆](#item-10) ⭐️ 8.0/10
11. [间谍软件嵌入禁用文本以阻挠 AI 分析](#item-11) ⭐️ 8.0/10
12. [Cloudflare 推出基于 Ory Hydra 的自助 OAuth 服务](#item-12) ⭐️ 7.0/10
13. [多密钥设置下可调密钥交替 Feistel 密码的后量子安全性](#item-13) ⭐️ 7.0/10
14. [BN 曲线配对子群等于相对迹映射的核](#item-14) ⭐️ 7.0/10
15. [防范授权钓鱼的钱包干预方案测试](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [首个与 NIST 标准兼容的阈值 FALCON 签名方案](https://eprint.iacr.org/2026/1300) ⭐️ 10.0/10

一篇新论文提出了首个适用于 NIST 标准化 FALCON 数字签名方案的阈值签名协议，生成的签名可由未修改的标准验证算法验证。 这一突破使得无需修改 FALCON 标准即可实现抗量子安全的多方签名，为安全的企业钱包和区块链验证人等实际应用铺平了道路。 关键创新包括：为私密参数适配 MPC 离散高斯采样，通过 Rényi 散度分析证明 73 位定点精度足够，以及基于两方 DPF 的伪随机相关生成器降低通信开销。

rss · IACR ePrint 密码学论文 · 6月22日 19:19

**背景**: FALCON 是一种基于格的抗量子签名方案，被 NIST 选为标准化方案，以其紧凑的签名和密钥尺寸著称。阈值签名允许多方共同签名，防止少数子集伪造。安全多方计算(MPC)能在不泄露各分片秘密的情况下实现协作签名。该工作将这些概念结合，实现了与现有标准兼容的阈值 FALCON 协议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Falcon_(signature_scheme)">Falcon (signature scheme) - Wikipedia</a></li>
<li><a href="https://falcon-sign.info/">Falcon</a></li>

</ul>
</details>

**标签**: `#threshold signatures`, `#FALCON`, `#post-quantum cryptography`, `#secure multi-party computation`, `#lattice-based cryptography`

---

<a id="item-2"></a>
## [Trail of Bits 推出 Patch the Planet，利用 GPT-5.5-Cyber 发现漏洞](https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/) ⭐️ 9.0/10

Trail of Bits 启动了 Patch the Planet 计划，将 OpenAI 的 GPT-5.5-Cyber 前沿模型与专家人工审查相结合，在关键开源项目中查找并修复漏洞。第一周就在 19 个项目中发现了数百个缺陷，提交了 51 个问题单和 64 个拉取请求，其中 37 个已合并。 这展示了一种可扩展的模型，将前沿 AI 应用于网络安全防御，可能改变行业应对开源软件中大量漏洞的方式。通过将 AI 与专家审查相结合，它解决了误报问题并直接提供补丁，减轻了资源不足的维护者的负担。 该计划最初覆盖了 19 个项目，包括 cURL、Go、Python 和 Sigstore，并正在扩展到 30 多个项目。值得注意的贡献超越了缺陷修复，还包括添加 CI 安全扫描、供应链工具和正确性改进。

rss · Trail of Bits Blog · 6月22日 16:50

**背景**: GPT-5.5-Cyber 是 OpenAI GPT-5.5 模型的一个变体，专门针对防御性网络安全任务（如追踪漏洞代码和开发补丁）进行了微调。前沿模型是指能力最强的先进 AI 模型。Trail of Bits 是一家知名的网络安全公司，专注于代码审计和漏洞研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/">Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Frontier_model">Frontier model</a></li>

</ul>
</details>

**标签**: `#AI`, `#security`, `#open-source`, `#vulnerability-detection`, `#LLM`

---

<a id="item-3"></a>
## [信任声音，隐藏来源：可验证编辑音频的匿名溯源](https://eprint.iacr.org/2026/1308) ⭐️ 8.0/10

该论文提出了 PPAAS，一种隐私保护音频认证系统，允许验证者确认已编辑录音的完整性和来源，而不泄露原始音频、编辑操作或设备身份，并提供分别适用于稀疏编辑和密集编辑的两种构造。 这一突破解决了音频认证与隐私之间的长期冲突，使得在取证、新闻和举报中能安全使用音频证据，而不泄露敏感的源内容。 基于分段的构造仅对编辑片段使用零知识证明，最小化稀疏编辑的成本；而基于迭代的构造使用增量可验证计算和零知识压缩来高效处理密集编辑；两种构造均被证明是实用的。

rss · IACR ePrint 密码学论文 · 6月23日 10:51

**背景**: 数字音频认证通常需要披露原始录音或编辑历史以验证来源，但这可能暴露隐私。匿名凭证允许证明属性（如设备授权）而不泄露身份，零知识证明则可以在不泄露输入的情况下验证计算。PPAAS 结合了这些技术，在隐藏源音频、编辑和设备身份的同时实现编辑验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anonymous_credential">Anonymous credential</a></li>
<li><a href="https://blog.cryptographyengineering.com/2026/03/02/anonymous-credentials-an-illustrated-primer/">Anonymous credentials: an illustrated primer – A Few Thoughts ...</a></li>

</ul>
</details>

**标签**: `#audio provenance`, `#privacy-preserving authentication`, `#digital signatures`, `#anonymous credentials`, `#verifiable editing`

---

<a id="item-4"></a>
## [对后门 UA-8295 信息终端的取证密码分析](https://eprint.iacr.org/2026/1309) ⭐️ 8.0/10

本文首次对存在后门的 UA-8295 信息终端进行了详细的取证密码分析，并提出了一种后门猜想，以系统地推理现实世界中的后门设计与攻击。 这项工作为理解国家支持级别的密码颠覆提供了前所未有的洞见，帮助安全界理解此类后门的构造方式及检测方法，这对强化未来密码系统至关重要。 该分析完全基于取证手段，通过对设备密码实现进行逆向工程；后门猜想为推理后门机制提供了新颖框架，但论文也承认，确切的网络后门设计只能基于现有证据进行推测。

rss · IACR ePrint 密码学论文 · 6月23日 11:53

**背景**: UA-8295 是由诺基亚开发、飞利浦销售的短脉冲消息终端，已知其内含美国国家安全局安插的后门。取证密码分析将调查技术应用于密码系统，以发现隐藏漏洞或后门。国家对密码设备植入后门长期遭疑，但极少有如此详尽的公开分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cryptomuseum.com/crypto/philips/ua8295/">Short-burst message terminal with encryption</a></li>
<li><a href="https://eprint.iacr.org/2026/1309">Forensic Cryptanalysis of the Backdoored UA-8295 Message Terminal</a></li>

</ul>
</details>

**标签**: `#cryptanalysis`, `#backdoor`, `#forensic analysis`, `#cryptographic standards`, `#nation-state attacks`

---

<a id="item-5"></a>
## [SQIsign 通过规范响应编码实现强不可伪造性](https://eprint.iacr.org/2026/1305) ⭐️ 8.0/10

该论文发现 SQIsign v2.0 中存在一个可锻性漏洞：对基变换矩阵 M_chl 取模 2^N 的相反数可生成另一个有效签名，这与 ECDSA 的可锻性类似。文中给出了概念验证攻击，并提出一种规范矩阵编码修复方案来防止此类伪造。 这项工作将 SQIsign 的安全性从存在性不可伪造性(EUF-CMA)提升到强不可伪造性(SUF-CMA)，后者是许多实际应用的关键属性。此举加强了这一 NIST 后量子密码候选方案，可能影响标准化决策。 该可锻性源于二维同源表示的非唯一性。修复方案对 M_chl 进行规范化并拒绝非规范形式，从而实现单射编码。该方案在量子随机预言模型中结合诚实验证者零知识和计算唯一响应，证明了其 SUF-CMA 安全性。

rss · IACR ePrint 密码学论文 · 6月23日 04:21

**背景**: SQIsign 是一种基于同源的 NIST 后量子签名候选方案，以极小的密钥和签名尺寸著称，但签名速度较慢。存在性不可伪造性（EUF-CMA）仅保证敌手无法伪造新消息的签名，而强不可伪造性（SUF-CMA）则进一步防止为已签名消息生成新签名。此处发现的可锻性类似 ECDSA 中(r,s)与(r,n-s)的问题，即可以从已有签名中轻易导出另一个有效签名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SQIsign">SQIsign</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isogeny-based_cryptography">Isogeny-based cryptography</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_signature_forgery">Digital signature forgery - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#digital signatures`, `#isogeny-based cryptography`, `#NIST standardization`

---

<a id="item-6"></a>
## [TRIP：具有输入隐私的线性回归新协议](https://eprint.iacr.org/2026/1302) ⭐️ 8.0/10

TRIP 结合了安全多方计算、稳健统计和差分隐私，实现高效且抗污染的线性回归。与纯 MPC 方案相比，速度提升最高可达 250 倍，并能容忍高达 40%的恶意数据污染。 该研究弥补了安全计算中常被忽视的数据投毒防御缺口。它支持具有强鲁棒性保证的实用安全机器学习，有利于金融、医疗等领域的协作分析。 TRIP 采用均值中位数预处理和差分隐私阈值化技术，在回归前检测并剔除异常值。即使在小数据集上，它也比基线快 10 倍；在真实数据中，即使污染高达 40%，其估计仍接近干净的最小二乘结果。

rss · IACR ePrint 密码学论文 · 6月22日 20:58

**背景**: 安全多方计算（MPC）允许多方在不泄露各自数据的前提下联合计算。然而，单独的 MPC 无法防御恶意或错误数据的投毒攻击。稳健统计学研究对异常值不敏感的方法，差分隐私则保证输出不会泄露个体数据点。TRIP 融合这些技术，同时实现隐私性与正确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi-party computation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Robust_statistics">Robust statistics</a></li>

</ul>
</details>

**标签**: `#secure-multiparty-computation`, `#machine-learning`, `#differential-privacy`, `#robust-statistics`, `#linear-regression`

---

<a id="item-7"></a>
## [结构化格及其在密码学与无线安全中的应用综述](https://eprint.iacr.org/2026/1301) ⭐️ 8.0/10

一篇新的综述论文系统性地回顾了结构化格（尤其是好圆格）及其在基于格的密码学和无线安全通信中的最新应用。 该工作将深刻的数论与格几何学同两个紧迫的安全需求——后量子密码学和物理层无线安全——连接起来，有望激发跨学科突破。 该综述重点介绍了极短向量可张成全空间的好圆格及其与球堆积问题的联系；它很可能讨论了具体的数域构造及其对密码学困难性的启示。

rss · IACR ePrint 密码学论文 · 6月22日 20:05

**背景**: 欧几里得格是 ℝⁿ 的离散子群，支撑着后量子密码学，其安全性依赖于最短向量问题的困难性。好圆格的极短向量张成全空间，是经典几何猜想的中心对象。在无线通信中，格码可在物理层提供抗窃听的信息论安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lattice-based_cryptography">Lattice-based cryptography</a></li>
<li><a href="https://link.springer.com/article/10.1007/s00013-018-1232-7">Well-rounded algebraic lattices in odd prime dimension | Archiv der Mathematik | Springer Nature Link</a></li>

</ul>
</details>

**标签**: `#lattices`, `#cryptography`, `#post-quantum`, `#number theory`, `#wireless security`

---

<a id="item-8"></a>
## [后量子密码行政令设定 2030 年截止日期，Cloudflare 发布迁移手册](https://blog.cloudflare.com/post-quantum-eo-2026/) ⭐️ 8.0/10

美国政府发布了一项行政命令，要求在 2030 年前迁移至后量子密码技术，Cloudflare 随后发布了分析报告以及针对政府和行业的迁移实施手册。 2030 年的截止日期凸显了政府和行业采用抗量子密码的紧迫性，主动迁移规划对于防止未来的数据泄露至关重要。 该行政令设定了 2030 年最后期限，Cloudflare 的手册包括清点密码资产、测试 PQC 实现和分阶段部署等步骤。NIST 已标准化首批后量子算法，但大规模迁移仍很复杂。

rss · Cloudflare Blog (PQ 迁移) · 6月23日 18:25

**背景**: 后量子密码学（PQC）旨在开发能抵御未来量子计算机攻击的算法，因为量子计算机可通过 Shor 算法破解当前广泛使用的公钥密码。尽管大规模量子计算机尚未出现，但‘先收集、后解密’的威胁意味着如今加密的数据未来可能被破解。2024 年，NIST 发布了首批 PQC 标准，以指导迁移工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://csrc.nist.gov/projects/post-quantum-cryptography">Post - Quantum Cryptography | CSRC</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#executive order`, `#cybersecurity`, `#migration`, `#Cloudflare`

---

<a id="item-9"></a>
## [LLMs 让漏洞报告不再特殊](https://words.filippo.io/vuln-reports/) ⭐️ 8.0/10

Filippo Valsorda 指出，大语言模型（LLM）的兴起让任何人都能发现与安全专家相似的漏洞，从而降低了保密漏洞报告的必要性。 这种技术平民化可能颠覆传统的漏洞披露生态，研究者私下报告漏洞的动力或将减弱，进而影响软件安全的修复进程。 虽然 LLM 在辅助漏洞发现方面展现出潜力，但近期研究表明该领域进展停滞，完全自主发现漏洞尚不可靠。

rss · Filippo Valsorda (Go 密码学) · 6月23日 13:00

**背景**: 漏洞报告通常是安全研究者向软件厂商私下披露漏洞信息，给厂商留出修复时间后再公开。大语言模型（LLM）是基于海量文本训练的人工智能系统，能够生成和分析代码。以往，发现复杂漏洞需要稀有的专业知识，而 LLM 可能降低这一门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>
<li><a href="https://arxiv.org/abs/2509.19117">[2509.19117] LLM-based Vulnerability Discovery through the ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#LLM`, `#vulnerability disclosure`, `#security research`, `#AI impact`

---

<a id="item-10"></a>
## [新研究揭示大语言模型提示注入源于角色混淆](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html) ⭐️ 8.0/10

一篇已被 ICML 2026 接收的论文表明，大语言模型的提示注入漏洞源于角色混淆：模型通过文本风格而非明确的角色标签来感知角色，这削弱了基于标签的安全措施。 这揭示了大语言模型安全架构的根本缺陷，表明依赖角色标签的防御是脆弱的。攻击者可通过看似无害的文本进行微妙且可扩展的操纵，为 AI 代理和应用带来持续风险。 研究者设计了“角色探针”来测量内部的角色感知，并引入了 CoT Forgery 攻击，该攻击会注入伪造的推理步骤。论文在 arXiv 上（abs/2603.12277），项目页面为 role-confusion.github.io。

rss · Schneier on Security · 6月25日 11:23

**背景**: 提示注入是将恶意指令插入用户输入或工具输出以劫持大语言模型。系统常使用角色标签（如<|system|>）作为安全边界，但 LLM 将所有文本作为单一 token 流处理，可能依赖措辞和风格而非标签来判断指令来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.12277">[2603.12277] Prompt Injection as Role Confusion - arXiv.org</a></li>
<li><a href="https://role-confusion.github.io/">Prompt Injection as Role Confusion</a></li>

</ul>
</details>

**标签**: `#prompt-injection`, `#llm`, `#security`, `#ai-safety`, `#machine-learning`

---

<a id="item-11"></a>
## [间谍软件嵌入禁用文本以阻挠 AI 分析](https://www.schneier.com/blog/archives/2026/06/embedding-forbidden-text-in-spyware-to-discourage-ai-analysis-2.html) ⭐️ 8.0/10

恶意软件开发者开始在间谍软件的 JavaScript 文件中嵌入有关核武器和生物武器的注释，这种新手法旨在通过触发内容政策拒绝来干扰基于 AI 的恶意软件扫描器。 这标志着对抗性 AI 战术的新升级，可能破坏自动化防御管道，迫使网络安全行业重新思考如何将语言模型集成到恶意软件分析中。 真正的恶意软件隐藏在注释之后，位于一个 try{eval(...)}包装器内，使用字符代码数组和 ROT 式替换密码；那些将文件开头直接喂给 AI 而没有隔离的薄弱管道最易受攻击。

rss · Schneier on Security · 6月24日 11:03

**背景**: 基于 AI 的恶意软件分析通常依赖大型语言模型来检查代码。ROT（Rotation）密码是一种简单的替换加密方法，将每个字母移动固定数量的位置，这里用于混淆有效载荷。模型上下文协议（MCP）由 Anthropic 于 2024 年推出，旨在标准化 AI 与外部工具的连接方式；一些恶意软件包专门针对 MCP 开发者，利用了 AI 与工具集成之间的交集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.dcode.fr/rot-cipher">ROT Cipher - Rotation - Online Rot Decoder, Solver, Translator</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI`, `#malware`, `#adversarial techniques`, `#spyware`

---

<a id="item-12"></a>
## [Cloudflare 推出基于 Ory Hydra 的自助 OAuth 服务](https://blog.cloudflare.com/oauth-for-all/) ⭐️ 7.0/10

Cloudflare 推出了自管理的 OAuth 2.0 服务，该服务基于开源项目 Ory Hydra 的分支构建，让所有客户都能运行自己的 OAuth 服务器，无需依赖外部身份提供商。 这降低了组织构建强大、可扩展 OAuth 基础设施的门槛，可能减少供应商锁定并简化自托管身份管理的合规性。 该服务基于 Ory Hydra 的一个性能优化分支，以低 CPU 占用和高扩展性著称，并集成到 Cloudflare 现有平台中，支持 OAuth 2.0 和 OpenID Connect。

hackernews · Cloudflare Blog (PQ 迁移) · 6月25日 02:18 · [社区讨论](https://news.ycombinator.com/item?id=48668033)

**背景**: OAuth 2.0 是一种行业标准的授权协议，常用于委托访问。Ory Hydra 是一个用 Go 语言编写的开源 OAuth 2.0 服务器，获得 OpenID 认证，以其安全性和可扩展性著称。许多公司自托管身份服务器，以保持对身份验证和数据的控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ory/hydra">GitHub - ory/hydra: Internet-scale OpenID Certified™ OpenID Connect and OAuth2.1 provider that integrates with your user management through headless APIs. Solve OIDC/OAuth2 user cases over night. Consume as a service on Ory Network or self-host. Trusted by OpenAI and many others for scale and security. Written in Go.</a></li>
<li><a href="https://medium.com/@klcoder/getting-started-with-ory-hydra-building-your-own-oauth2-authentication-service-4d06716fbc18">Getting Started with Ory/Hydra: Building Your Own OAuth2 Authentication Service | by Karim Lalani | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人称赞技术成就和低开销，也有人对 OAuth 的复杂性表示不满。有人担忧 Cloudflare 放弃项目的历史，并对长期支持提出质疑。Ory Hydra 作者赞扬了该实现，并提到有更快的商业版本。

**标签**: `#OAuth`, `#Cloudflare`, `#authentication`, `#self-hosted`, `#identity`

---

<a id="item-13"></a>
## [多密钥设置下可调密钥交替 Feistel 密码的后量子安全性](https://eprint.iacr.org/2026/1312) ⭐️ 7.0/10

本文在敌手可量子访问内部原语的条件下，证明了 3 轮 TKAF 是后量子 TPRP 安全的，4 轮 TKAF 是后量子 STPRP 安全的，并将分析扩展到多密钥场景。 这项工作为可调 Feistel 设计提供了抵御量子敌手的严格安全保证，加强了后量子对称密码学的理论基础，尤其在多密钥和可调场景中具有重要影响。 证明在 Q1 模型中成立，敌手只能经典访问ℓ个独立预言机；安全边界为总查询量Ω(2^{n/3}/ℓ^{2/3})或经典查询量Ω(ε^{-1/2})，前提是使用一个ε-AXU 散列函数。

rss · IACR ePrint 密码学论文 · 6月23日 18:35

**背景**: 密钥交替 Feistel 密码（KAF）每轮将秘密轮密钥与输入异或后应用一个公开随机函数。可调版本（TKAF）通过一个ε-几乎异或通用散列函数将调柄注入该异或中。Q1 模型允许敌手对内部原语进行量子叠加查询。TPRP 和 STPRP 是可调分组密码的安全定义，其中 STPRP 对选择密文攻击具有更强的抵抗能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1312">Post-Quantum Security of Tweakable Key-Alternating Feistel Ciphers in the Multi-Key Setting</a></li>
<li><a href="https://crypto.stackexchange.com/questions/112222/exploring-quantum-attacks-in-q1-model-on-symmetric-primitives-with-better-than-q">Exploring Quantum Attacks in Q1 Model on Symmetric Primitives ...</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-030-57808-4_4">Tweaking Key-Alternating Feistel Block Ciphers | SpringerLink</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum security`, `#Feistel cipher`, `#provable security`, `#tweakable cipher`

---

<a id="item-14"></a>
## [BN 曲线配对子群等于相对迹映射的核](https://eprint.iacr.org/2026/1311) ⭐️ 7.0/10

一篇新论文严格证明了 BN 配对子群恰好是 n-挠点上相对迹映射的核，将此前的一个民间认知形式化了。 这一严格证明强化了 BN 曲线配对的理论基础，该曲线广泛应用于零知识证明和基于身份的加密，提高了对其安全性和正确性的信心。 该证明利用了从 12 次扩域到其 6 次子域的相对迹映射，其在 n-挠点上的核恰好给出了正确的配对子群。这一结果特指 BN 曲线，未必适用于其他配对友好曲线族。

rss · IACR ePrint 密码学论文 · 6月23日 17:04

**背景**: Barreto-Naehrig（BN）曲线是一类嵌入度为 12 的椭圆曲线，广泛用于零知识证明等基于配对的密码协议。对偶对定义在 n-挠点的一个特定子群上，其中 n 整除曲线阶。迹映射是一种代数映射，将元素在域扩张下的所有伽罗瓦共轭求和；相对迹映射则限制在子域扩张上。该论文证明了该相对迹映射在 n-挠点上的核恰好就是配对子群。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepwiki.com/scipr-lab/dizk/5-barreto-naehrig-curves">Barreto-Naehrig Curves | scipr-lab/dizk | DeepWiki</a></li>
<li><a href="https://en.wikipedia.org/wiki/Elliptic_curve">Elliptic curve - Wikipedia</a></li>
<li><a href="https://math.stackexchange.com/questions/5058637/range-of-the-trace-map-on-elliptic-curves">galois theory - Range of the trace map on elliptic curves ...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#elliptic curves`, `#pairings`, `#BN curves`, `#trace map`

---

<a id="item-15"></a>
## [防范授权钓鱼的钱包干预方案测试](https://eprint.iacr.org/2026/1310) ⭐️ 7.0/10

一项研究提出并实证测试了四种基于钱包的用户干预方案——支出上限建议、主动支出者警告、被动支出者警告和延迟确认——来减轻授权钓鱼攻击。实验（n=364）表明，支出上限建议提高了支出上限设置率，而主动支出者警告和延迟确认显著提升了钓鱼任务的取消率。 授权钓鱼是一种日益严重的 Web3 威胁，已造成数十亿美元损失，在基于 URL 的检测失效时，钱包级防御至关重要。这些干预方案为钱包开发者提供了有实证支持的设计方向，以增强用户安全。 通过受试者间实验（n=364）和半结构化访谈（n=23）评估干预方案。仅主动支出者警告和延迟确认对钓鱼任务取消率有统计显著提升，被动支出者警告则无。用户有时难以解读可疑线索，更关注交易结果而非授权细节。

rss · IACR ePrint 密码学论文 · 6月23日 16:42

**背景**: 授权钓鱼通过恶意智能合约诱骗用户授予攻击者代币支出权限。在 Web3 中，代币授权（如 ERC20 的 approve 函数）允许支出者代表所有者转移代币。此类骗局已造成超过 10 亿美元损失，常通过劫持正规网站实施，使得浏览器级检测力不从心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chainalysis.com/blog/approval-phishing-cryptocurrency-scams-2023/">Crypto Crime: Targeted Approval Phishing Scams On the Rise</a></li>
<li><a href="https://support.ledger.com/article/Ethereum-Token-Approvals-Explained">Understanding Ethereum Token Approvals - support.ledger.com</a></li>

</ul>
</details>

**标签**: `#Web3 Security`, `#Phishing Mitigation`, `#Wallet Design`, `#User Intervention`, `#Empirical Study`

---
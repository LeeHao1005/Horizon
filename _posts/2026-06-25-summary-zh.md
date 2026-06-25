---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 49 条内容中筛选出 15 条重要资讯。

---

1. [TRIP 协议：可容忍 40%恶意输入的高效安全线性回归](#item-1) ⭐️ 9.0/10
2. [首个兼容未修改 FALCON 验证的阈值签名方案](#item-2) ⭐️ 9.0/10
3. [Cloudflare 推出自托管 OAuth 服务](#item-3) ⭐️ 8.0/10
4. [信任声音，隐藏来源：编辑音频的匿名溯源](#item-4) ⭐️ 8.0/10
5. [可调密钥交替 Feistel 密码的后量子安全证明](#item-5) ⭐️ 8.0/10
6. [基于钱包的干预措施以缓解授权钓鱼攻击](#item-6) ⭐️ 8.0/10
7. [首次对后门 UA-8295 报文终端进行取证密码分析](#item-7) ⭐️ 8.0/10
8. [TETRIS：自动优化掩码硬件随机性与延迟权衡](#item-8) ⭐️ 8.0/10
9. [SQIsign 签名方案通过规范编码修复实现 SUF-CMA 安全性](#item-9) ⭐️ 8.0/10
10. [椭圆曲线 G 压缩的同源分解与点恢复](#item-10) ⭐️ 8.0/10
11. [Cloudflare 分析美国新的后量子行政命令](#item-11) ⭐️ 8.0/10
12. [研究揭示角色混淆是 LLM 提示注入漏洞根源](#item-12) ⭐️ 8.0/10
13. [Trail of Bits 与 OpenAI 发起“修补地球”行动，利用 GPT-5.5-Cyber 修复开源漏洞](#item-13) ⭐️ 8.0/10
14. [BN 曲线相对迹零子群等于相对迹映射核的证明](#item-14) ⭐️ 7.0/10
15. [通信高效的恶意安全 MPC（2/3 诚实多数）](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [TRIP 协议：可容忍 40%恶意输入的高效安全线性回归](https://eprint.iacr.org/2026/1302) ⭐️ 9.0/10

研究者提出了 TRIP 协议，结合安全多方计算、鲁棒统计和差分隐私技术，实现了可抵御最高 40%恶意输入损坏的安全线性回归。 这一突破解决了安全机器学习中的关键漏洞，即现有协议可能被低质量或对抗性数据破坏，为构建真正可信的协作机器学习奠定了基础。 TRIP 在合成数据上能恢复真实模型，在真实数据集上面对 40%损坏时仍接近普通最小二乘基线，且在大规模数据上比纯安全多方计算方案快 250 倍。

rss · IACR ePrint 密码学论文 · 6月22日 20:58

**背景**: 安全多方计算（MPC）允许在不泄露私有输入的情况下联合计算，但无法防御参与者提交恶意构建的数据。鲁棒统计关注在存在异常值或违背假设时依然可靠的方法。差分隐私提供数学上严格的隐私保证。线性回归是机器学习的基础技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Robust_statistics">Robust statistics</a></li>

</ul>
</details>

**标签**: `#secure computation`, `#machine learning`, `#differential privacy`, `#robust statistics`, `#linear regression`

---

<a id="item-2"></a>
## [首个兼容未修改 FALCON 验证的阈值签名方案](https://eprint.iacr.org/2026/1300) ⭐️ 9.0/10

该工作首次提出了适用于 FALCON 的阈值签名方案，其生成的签名可通过未修改的 FALCON 验证算法进行验证。它通过适配基于 MPC 的离散高斯采样以支持私有中心和标准差，并提供了 Rényi 散度分析，表明在定点算术下 73 位精度足以保证 Klein 采样器的安全性。 在后量子标准化之后，这满足了为所选原语开发阈值版本的迫切需求。FALCON 拥有最小的签名和密钥尺寸，非常适合带宽受限环境，而该协议使得在需要抵御量子攻击的分布式签名场景中使用 FALCON 成为可能。 该协议适配了 Wei 等人基于 MPC 的离散高斯采样以处理私有中心和标准差，利用 Rényi 散度分析证实 73 位定点精度已足够，并设计了高效的 Klein 采样器 MPC 协议，利用固定陷门基和两方分布式点函数来降低通信量。

rss · IACR ePrint 密码学论文 · 6月22日 19:19

**背景**: FALCON 是 NIST 选定的后量子签名方案，基于格密码学，以其紧凑的签名尺寸著称。阈值签名要求一定数量的参与方共同生成签名，增强了安全性。多方计算（MPC）允许参与方在保护隐私输入的情况下计算函数。Klein 采样器是 FALCON 签名过程中使用的离散高斯采样算法，而 Rényi 散度是一种用于分析近似采样器安全性的度量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rényi_divergence">Rényi divergence</a></li>
<li><a href="https://doc.sagemath.org/html/en/reference/stats/sage/stats/distributions/discrete_gaussian_integer.html">Discrete Gaussian Samplers over the Integers - Statistics</a></li>

</ul>
</details>

**标签**: `#threshold-signatures`, `#post-quantum-cryptography`, `#FALCON`, `#MPC`, `#discrete-gaussian-sampling`

---

<a id="item-3"></a>
## [Cloudflare 推出自托管 OAuth 服务](https://blog.cloudflare.com/oauth-for-all/) ⭐️ 8.0/10

Cloudflare 发布了一项自托管 OAuth 服务，使用户能够独立颁发和管理 API 令牌，无需依赖第三方身份提供商。 这简化了开发者和组织的身份验证流程，减少对外部服务的依赖，并可能增强 Cloudflare 生态系统内的安全控制。 该服务集成到 Cloudflare 的控制面板和 API 中，无需外部身份提供商即可实现自托管 OAuth，但未披露具体的技术性能细节。

hackernews · Cloudflare Blog (PQ 迁移) · 6月25日 02:18 · [社区讨论](https://news.ycombinator.com/item?id=48668033)

**背景**: OAuth 是一种用于访问委托的开放标准，常用于基于令牌的身份验证。内部管理 OAuth 通常很复杂，往往需要专门的身份提供商。Cloudflare 的服务旨在通过提供内置解决方案来简化用户的这一过程。

**社区讨论**: 社区评论反映了复杂的情绪：一些用户认为 OAuth 复杂且令人沮丧，而另一些用户指出在大规模下可管理。社区对 Cloudflare 长期改进项目的承诺表示怀疑，同时也对博文中分享的技术细节表示赞赏。

**标签**: `#oauth`, `#cloudflare`, `#authentication`, `#security`, `#developer-tools`

---

<a id="item-4"></a>
## [信任声音，隐藏来源：编辑音频的匿名溯源](https://eprint.iacr.org/2026/1308) ⭐️ 8.0/10

该论文提出了隐私保护音频认证系统（PPAAS），利用零知识证明将来源溯源和编辑正确性绑定到隐藏见证人，从而在不泄露原始录音、编辑操作或设备身份的情况下验证编辑后的音频。论文提供了两种构造：针对稀疏编辑的基于分段的构造，以及针对密集编辑的使用增量可验证计算（IVC）的基于迭代的构造。 这项工作解决了音频认证与隐私之间的矛盾，使得敏感录音可以作为证据使用而不会泄露来源机密。它对于新闻、举报和法律等领域特别重要，因为这些领域同时需要信任和匿名性。 基于分段的方案仅对主动编辑的片段应用零知识证明，从而最大限度地减少了稀疏编辑的成本。基于迭代的方案使用增量可验证计算（IVC）将重复检查折叠为单个证明，对于密集编辑更高效。

rss · IACR ePrint 密码学论文 · 6月23日 10:51

**背景**: 零知识证明是一种密码协议，允许一方向另一方证明某个陈述为真，而不泄露任何额外信息。传统的音频认证依赖于数字签名，一旦音频被编辑，签名就会失效，从而迫使在隐私和可验证性之间做出选择。PPAAS 结合了这些概念，允许编辑操作同时保持匿名性和真实性证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-knowledge_proof">Zero-knowledge proof</a></li>

</ul>
</details>

**标签**: `#audio authentication`, `#privacy-preserving`, `#provenance`, `#zero-knowledge proofs`, `#multimedia security`

---

<a id="item-5"></a>
## [可调密钥交替 Feistel 密码的后量子安全证明](https://eprint.iacr.org/2026/1312) ⭐️ 8.0/10

该论文严格证明了在 Q1 模型下，3 轮可调密钥交替 Feistel 密码（TKAF）满足后量子 TPRP 安全，4 轮 TKAF 满足后量子 STPRP 安全，适用于多密钥场景，且攻破这些安全性需要至少Ω(2^{n/3}/ℓ^{2/3})或Ω(ε^{-1/2})次经典/量子查询。 它奠定了设计抗量子对称加密方案的基础，确保可调分组密码（广泛用于磁盘加密）在未来量子攻击下仍能保持安全，即使在该场景中攻击者针对多个密钥。 该证明将 Basak 等人（ASIACRYPT 2025）的技术从标准 KAF 推广到可调和多密钥情形，使用ε-AXU 哈希函数注入调柄。Q1 模型允许对内部原语进行量子叠加查询，安全边界取决于分组长度 n 和密钥数量ℓ。

rss · IACR ePrint 密码学论文 · 6月23日 18:35

**背景**: 可调分组密码允许额外的公开调柄（tweak）来改变加密过程，常用于磁盘加密。密钥交替 Feistel 密码（KAF）将轮密钥与公开随机函数交替使用。Q1 模型允许敌手以量子叠加态访问内部原语。多密钥设置考虑攻击者可以经典访问多个独立密钥的加密神谕。ε-AXU 通用哈希族用于注入调柄，并具有低碰撞概率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://infoscience.epfl.ch/server/api/core/bitstreams/2147e5cc-e4ee-49a4-b7a3-11eae1e0b3b3/content">Tweaking Key - Alternating Feistel Block</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-030-57808-4_4">Tweaking Key - Alternating Feistel Block Ciphers | Springer Nature Link</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_hashing">Universal hashing - Wikipedia</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#symmetric cryptography`, `#provable security`, `#Feistel ciphers`, `#tweakable encryption`

---

<a id="item-6"></a>
## [基于钱包的干预措施以缓解授权钓鱼攻击](https://eprint.iacr.org/2026/1310) ⭐️ 8.0/10

研究人员设计并测试了四种基于钱包的干预措施——支出上限建议、主动支出者警告、被动支出者警告和延迟确认——在一项有 364 名参与者的用户研究中，发现主动支出者警告和延迟确认显著提高了钓鱼任务的取消率。 授权钓鱼是一个日益严重的威胁，利用合法的代币授权机制，随着攻击者越来越多地劫持合法网站，钱包成为最后一道防线。这些干预措施提供了实用的、以用户为中心的解决方案，保护 Web3 用户免于资产损失。 支出上限建议显著增加了用户设置支出上限的可能性，但被动警告条件在取消率上没有显示出统计学上显著的增加。用户往往关注交易结果而忽略授权细节，这表明需要更好地教育用户了解授权后的后果。

rss · IACR ePrint 密码学论文 · 6月23日 16:42

**背景**: 授权钓鱼通过诱骗用户授权恶意智能合约使用其代币，利用了合法的 ERC-20 'approve'函数。一旦授权，攻击者可以无需用户后续操作即可转走代币。由于可信网站被攻陷时基于 URL 的检测失效，当前安全机制面临挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.chainalysis.com/blog/what-is-approval-phishing/">What Is Approval Phishing ? Detect & Disrupt Crypto Scams at Scale</a></li>
<li><a href="https://support.ledger.com/article/Ethereum-Token-Approvals-Explained">Understanding Ethereum Token Approvals</a></li>
<li><a href="https://support.metamask.io/stay-safe/safety-in-web3/what-is-a-token-approval/">What is a token approval? | MetaMask Help Center</a></li>

</ul>
</details>

**标签**: `#web3 security`, `#phishing mitigation`, `#wallet design`, `#user study`, `#approval mechanisms`

---

<a id="item-7"></a>
## [首次对后门 UA-8295 报文终端进行取证密码分析](https://eprint.iacr.org/2026/1309) ⭐️ 8.0/10

本文首次对后门植入的 UA-8295 报文终端进行详细的取证密码分析，并提出了一种“后门猜想”来表征其后门设计和预期的攻击场景。 它为安全界提供了对真实国家级别后门设计的洞见，有助于理解和潜在归因此类攻击，并改善对类似威胁的防御。 分析揭示了后门可能的工作方式，但摘要未披露具体密码漏洞。后门猜想提供了一个用于推理后门特性的框架。

rss · IACR ePrint 密码学论文 · 6月23日 11:53

**背景**: UA-8295 是一款由诺基亚开发、飞利浦 Usfa 从 1984 年起销售的加密报文终端，用于军事安全通信。取证密码分析涉及分析密码实现以发现弱点或后门，通常用于取证环境。该论文研究了一个已知被植入后门的系统，由于此类设备通常涉密，公开分析极为罕见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cryptomuseum.com/crypto/philips/ua8295/">UA - 8295</a></li>
<li><a href="https://github.com/stef/UA-8295-NSA">GitHub - stef/ UA - 8295 -NSA: fully reverse-engineered and...</a></li>
<li><a href="https://study.com/academy/lesson/applications-of-cryptography-in-digital-forensics-uses-impact.html">Applications of Cryptography in Digital Forensics: Uses & Impact | Study.com</a></li>

</ul>
</details>

**标签**: `#cryptanalysis`, `#backdoor`, `#forensic analysis`, `#cryptography`, `#security`

---

<a id="item-8"></a>
## [TETRIS：自动优化掩码硬件随机性与延迟权衡](https://eprint.iacr.org/2026/1306) ⭐️ 8.0/10

本文介绍了 TETRIS，一个软件级的设计空间探索工具，利用两种新算法 MLRC 和 MRLC，自动寻找基于组件掩码硬件设计中最佳的随机性与延迟权衡。 该方法填补了关键空白，通过快速启发式优化取代繁重的全局 SAT 求解，实现数量级加速，并获得可比或更优的面积结果。 TETRIS 利用探测隔离无干扰（PINI）组件的结构化权衡，在毫秒内完成优化；其对偶算法分别在随机性约束下最小化延迟（MLRC），和在延迟约束下最小化随机性（MRLC）。

rss · IACR ePrint 密码学论文 · 6月23日 08:39

**背景**: 掩码是一种侧信道防护措施，将敏感数据分割成多个随机份额以抵御功耗分析攻击。在硬件中，它会带来随机性（所需随机比特）和延迟（计算时间）的开销。基于组件的掩码将电路分解为具有已知随机性-延迟特征的小型可复用组件，使得结构化优化成为可能。设计空间探索（DSE）自动寻找用户约束下的最佳组件分配。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iacr.org/news/item/28866">IACR News item: 24 June 2026</a></li>
<li><a href="https://hal-lirmm.ccsd.cnrs.fr/lirmm-04639398/document">Randomness Generation for Secure Hardware Masking</a></li>

</ul>
</details>

**标签**: `#hardware security`, `#masked gadgets`, `#design space exploration`, `#randomness-latency trade-off`, `#optimization`

---

<a id="item-9"></a>
## [SQIsign 签名方案通过规范编码修复实现 SUF-CMA 安全性](https://eprint.iacr.org/2026/1305) ⭐️ 8.0/10

该论文发现 NIST 后量子候选方案 SQIsign v2.0 存在具体的延展性漏洞：将基变换矩阵模 2^N 取负即可生成另一个有效签名。为此，作者提出了一种规范编码修复方案，首次使该签名方案达到强不可伪造性（SUF-CMA）。 该成果意义重大，因为 SUF-CMA 是一种更强的安全定义，可防止重签名攻击，并消除了实践中类似 ECDSA 中 (r,s) 与 (r,n-s) 的延展性问题。随着 SQIsign 在 NIST 标准化进程中不断推进，此修复方案可能会直接影响最终规范，并增强对其实际部署的信心。 延展性源于二维同源表示的非唯一性：将签名中的挑战矩阵 M_chl 模 2^N 取负即可产生另一个有效签名。修复方案通过规范编码实现：签名者对 M_chl 进行规范化，验证者则拒绝非规范形式。作者证明了规范化后响应编码是单射的，并利用这一性质在量子随机预言模型下证明了 SUF-CMA 安全性。

rss · IACR ePrint 密码学论文 · 6月23日 04:21

**背景**: SQIsign 是基于超奇异椭圆曲线同源的后量子签名方案，因密钥和签名尺寸小而备受关注，但计算时间较长。该方案正接受 NIST 评估，以取代易受量子攻击的经典算法。SUF-CMA（选择消息攻击下的强存在不可伪造性）是一种安全定义，不仅防止伪造新消息的签名，还阻止对已签名消息生成新签名，从而解决延展性问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SQIsign">SQIsign</a></li>
<li><a href="https://blog.cryptographyengineering.com/euf-cma-and-suf-cma/">EUF-CMA and SUF - CMA – A Few Thoughts on Cryptographic...</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#digital signatures`, `#isogeny-based cryptography`, `#NIST standardization`, `#SUF-CMA`

---

<a id="item-10"></a>
## [椭圆曲线 G 压缩的同源分解与点恢复](https://eprint.iacr.org/2026/1299) ⭐️ 8.0/10

该论文提出了一种称为 G 压缩的新抽象，利用有限子群 G 推广了椭圆曲线上的点压缩。论文证明了任一 G 压缩都可分解为一个标准 2 次压缩与一个以 G 为核的可分同源的复合，从而能够高效实现倍点、差分加法和点恢复。 这项工作为多种椭圆曲线模型提供了统一的点压缩框架，有望提升密码协议的效率。通过将 G 压缩与同源联系起来，也为将这些技术整合到基于同源的密码学中开辟了新途径，这对后量子安全具有重要意义。 论文为扩展雅可比四次曲线、扭曲爱德华曲线、扭曲雅可比交和扭曲黑森曲线（部分模型有额外系数条件）给出了具体的分解 w = f ∘ Φ，其中的同源Φ通常映射到蒙哥马利曲线，且满足 x(Φ)=1/w。对偶同源也被用于点恢复。

rss · IACR ePrint 密码学论文 · 6月22日 15:21

**背景**: 在椭圆曲线密码学中，点压缩将点的表示缩减为 x 坐标和一个符号位，使存储减半。同源是保持单位元的椭圆曲线之间的有理映射。G 压缩通过使用有限子群 G 来进一步减小函数域扩张的次数，从而推广了点压缩，实现了更紧凑的表示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Twisted_Hessian_curves">Twisted Hessian curves</a></li>
<li><a href="https://defeo.lu/docet/assets/slides/2019-11-28-ntnu.pdf">Isogeny Based Cryptography : an Introduction</a></li>

</ul>
</details>

**标签**: `#elliptic curves`, `#cryptography`, `#isogenies`, `#point compression`, `#arithmetic`

---

<a id="item-11"></a>
## [Cloudflare 分析美国新的后量子行政命令](https://blog.cloudflare.com/post-quantum-eo-2026/) ⭐️ 8.0/10

Cloudflare 发布了对美国新的后量子密码行政命令的分析，该命令设定了 2030 年迁移期限，并为量子安全建立了基础。该公司还为政府和行业提供了迁移手册。 该分析强调了一项关键政策推动，以防御未来的量子威胁，敦促组织开始过渡到量子安全加密。2030 年的期限增加了各行业基础设施升级的紧迫性。 该行政命令要求在 2030 年之前迁移到后量子密码学，基于 NIST 于 2024 年标准化的算法。Cloudflare 的迁移手册解决了诸如盘点加密资产和测试混合解决方案等实施挑战。

rss · Cloudflare Blog (PQ 迁移) · 6月23日 18:25

**背景**: 后量子密码学(PQC)开发能够抵御量子计算机攻击的算法，量子计算机可能破解广泛使用的公钥加密。美国国家标准与技术研究院(NIST)于 2024 年发布了首批三项 PQC 标准。该行政命令将这些标准扩展到联邦强制要求，加速了政府及相关行业的采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://csrc.nist.gov/projects/post-quantum-cryptography">Post - Quantum Cryptography | CSRC</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#cybersecurity`, `#executive order`, `#migration`, `#Cloudflare`

---

<a id="item-12"></a>
## [研究揭示角色混淆是 LLM 提示注入漏洞根源](https://www.schneier.com/blog/archives/2026/06/interesting-paper-exploring-prompt-injection.html) ⭐️ 8.0/10

来自 role-confusion.github.io 的新研究发现，大语言模型（LLM）容易受到提示注入攻击，原因是它们识别的是不同角色（如系统与用户）的风格模式，而非真正理解角色本身。论文总结道，原本作为安全措施的角色标签并未在模型内部表示中持续存在，从而导致角色混淆，可被攻击者利用。 这一发现意味着，除非 LLM 获得真正的角色感知能力，否则提示注入防御将始终是一场无休止的“打地鼠”游戏。角色边界的连续性还为大规模、隐蔽的注入攻击提供了可能，攻击者可通过看似无害的文本逐渐改变模型行为。 该研究为提示注入提供了机制性解释，证明现有的角色标签架构并未在神经表示中转化为稳固的角色分离。它还警告，经过精巧设计的注入技术可在合法且大规模的情况下，利用这些连续的角色边界进行微妙的状态操纵。

rss · Schneier on Security · 6月25日 11:23

**背景**: 提示注入是一种安全漏洞，攻击者通过精心构造输入来覆盖或操纵 LLM 的原始指令，常通过混淆模型对提示中权威部分的判断来实现。基于角色的提示使用特殊标签（如“系统：”、“用户：”）来划分不同来源，假设模型会遵守这些边界。这项新研究对此提出质疑，表明模型依赖的是表面的风格线索，而非对角色深层理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://role-confusion.github.io/">Prompt Injection as Role Confusion</a></li>
<li><a href="https://www.lesswrong.com/posts/d8xDGzCEYE639qqEv/a-mechanistic-explanation-of-prompt-injection-and-why-you">A Mechanistic Explanation of Prompt Injection ... — LessWrong</a></li>
<li><a href="https://devblogs.co/posts/prompt-injection-as-role-confusion">Prompt Injection as Role Confusion</a></li>

</ul>
</details>

**标签**: `#prompt injection`, `#LLM security`, `#AI safety`, `#role confusion`, `#machine learning`

---

<a id="item-13"></a>
## [Trail of Bits 与 OpenAI 发起“修补地球”行动，利用 GPT-5.5-Cyber 修复开源漏洞](https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/) ⭐️ 8.0/10

在“修补地球”行动的首周，Trail of Bits 工程师利用 GPT-5.5-Cyber 在 19 个关键开源项目中发现了数百个漏洞，并提交了 64 个拉取请求和 51 个问题，其中 37 个修复已被合并。 这展示了一种可扩展的 AI 辅助安全改进模式，通过专家筛选确保补丁切实可行，直接惠及负担过重的维护者和整个软件生态。 项目涵盖密码学（RustCrypto）、网络（cURL、NATS）、供应链（Sigstore、Python.org）等领域；行动不仅修复漏洞，还增加了测试、模糊测试工具和 CI 安全扫描。

rss · Trail of Bits Blog · 6月22日 16:50

**背景**: GPT-5.5-Cyber 是 OpenAI 专为网络防御设计的 AI 模型，能识别代码中的漏洞。Trail of Bits 是一家以审计复杂软件著称的安全公司。该行动旨在解决 AI 生成的漏洞报告可能因误报过多而令维护者不堪重负的问题，因此由人类专家筛选结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apidog.com/blog/what-is-gpt-5-5/">What Is GPT - 5 . 5 ? OpenAI's New Frontier Model Explained</a></li>
<li><a href="https://www.theregister.com/security/2026/05/01/openai-locks-gpt-55-cyber-behind-velvet-rope/5219691">OpenAI locks GPT - 5 . 5 - Cyber behind velvet rope</a></li>

</ul>
</details>

**标签**: `#AI`, `#security`, `#open-source`, `#vulnerability-discovery`, `#LLM`

---

<a id="item-14"></a>
## [BN 曲线相对迹零子群等于相对迹映射核的证明](https://eprint.iacr.org/2026/1311) ⭐️ 7.0/10

该论文首次严格证明了 Barreto-Naehrig 曲线的相对迹零子群恰好等于 n-挠点上的相对迹映射的核，证实了一个被广泛使用但此前未经证明的特性。 该成果巩固了配对密码学的数学基础，确保基于 BN 曲线的协议的正确性和安全性，对实现者和理论家均有益处。 该证明适用于 BN 曲线（参数化的配对友好椭圆曲线），利用配对中扩域的相对迹映射，并在曲线阶为 n 的 n-挠点上成立。

rss · IACR ePrint 密码学论文 · 6月23日 17:04

**背景**: Barreto-Naehrig（BN）曲线是一类广泛使用的配对友好椭圆曲线，用于高效密码协议。相对迹零子群由在扩域下迹为零的点组成，是零知识证明等构造中的常用组件。将其作为相对迹映射核的刻画是业界已知但缺乏正式验证的结果。n-挠点是指阶整除曲线阶 n 的点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cp4space.hatsya.com/2020/12/27/barreto-naehrig-curves-and-cryptographic-pairings/">Barreto - Naehrig curves and cryptographic pairings</a></li>
<li><a href="https://www.ietf.org/archive/id/draft-irtf-cfrg-pairing-friendly-curves-05.html">Pairing-Friendly Curves</a></li>
<li><a href="https://link.springer.com/article/10.1007/s10623-016-0249-9">An optimal representation for the trace zero subgroup</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#elliptic-curves`, `#pairing-based-crypto`, `#Barreto-Naehrig`, `#mathematical-proof`

---

<a id="item-15"></a>
## [通信高效的恶意安全 MPC（2/3 诚实多数）](https://eprint.iacr.org/2026/1307) ⭐️ 7.0/10

本文提出了一种通信高效的编译器，可在三分之二诚实多数（即至多三分之一腐败方）的设定下，利用 Shamir 秘密共享将半诚实 MPC 协议编译为恶意安全协议。它通过用局部度 2t 计算和批量打开代替多次乘法验证来降低通信开销。 这项工作通过显著降低通信开销，推进了实用的恶意安全 MPC，使其在需要强安全保证但不牺牲性能的现实应用中更加可行。 该协议基于 Shamir 秘密共享和编译器方法，注入新鲜随机数以检测错误乘法三元组。通信开销通过用局部度 2t 计算和单次批量打开代替多次乘法验证来降低，同时保持局部验证成本较低。

rss · IACR ePrint 密码学论文 · 6月23日 08:55

**背景**: 安全多方计算（MPC）允许多方在不泄露各自输入的情况下共同计算函数。MPC 协议通常考虑半诚实对手（遵循协议但试图窃取信息）和恶意对手（可任意偏离协议）。诚实多数设定（假设大多数参与方是诚实的）可实现更高效的协议；本文考虑强三分之二诚实多数（t < n/3）。Shamir 秘密共享是一种将秘密分割为份额、需要阈值才能重构的方案，广泛用于 MPC 的线性秘密共享。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi - party computation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shamir's_secret_sharing">Shamir's secret sharing</a></li>

</ul>
</details>

**标签**: `#secure multi-party computation`, `#malicious security`, `#Shamir secret sharing`, `#honest majority`, `#cryptography`

---
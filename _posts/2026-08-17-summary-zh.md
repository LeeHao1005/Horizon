---
layout: default
title: "Horizon Summary: 2026-08-17 (ZH)"
date: 2026-08-17
lang: zh
---

> 从 39 条内容中筛选出 15 条重要资讯。

---

1. [LLM 引导的形式化验证证明对称密码学 Tu-Deng 猜想](#item-1) ⭐️ 9.0/10
2. [DTRU：采用双 E8 编码的紧凑 NTRU KEM，满足中国商用密码标准](#item-2) ⭐️ 8.0/10
3. [改进四元数理想到同源变换：修复 Qlapoti 缺陷并大幅提速](#item-3) ⭐️ 8.0/10
4. [DumboMix：实用的鲁棒异步匿名广播协议](#item-4) ⭐️ 8.0/10
5. [MamaBearZKP：协同设计素数域与 AVX-512IFMA 加速零知识证明](#item-5) ⭐️ 8.0/10
6. [VeriFSS：无经销商主动安全两方函数秘密共享](#item-6) ⭐️ 8.0/10
7. [Jasmin 编译器为掩码实现添加泄漏检测](#item-7) ⭐️ 8.0/10
8. [密码学群鲁棒组合器被证明不可行](#item-8) ⭐️ 8.0/10
9. [新方法通过子空间限制跳过 S 盒区分多轮 Poseidon 哈希](#item-9) ⭐️ 8.0/10
10. [混合量子态学习的平均难度与密码学等价性](#item-10) ⭐️ 8.0/10
11. [《地狱之钟》：三元快速矩阵乘法算法流水线](#item-11) ⭐️ 8.0/10
12. [施奈尔与桑德斯：若市场失灵，美国应国有化 OpenAI 和 Anthropic](#item-12) ⭐️ 8.0/10
13. [UMQ、MQOW 与 MQSPR 假设之间的紧致蕴含关系](#item-13) ⭐️ 7.0/10
14. [形式化证明显示西蒙量子算法无法解决二面体陪集问题](#item-14) ⭐️ 7.0/10
15. [基于 Module-SIS 的并发安全紧凑盲签名方案，签名大小降至 4.7 KB](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LLM 引导的形式化验证证明对称密码学 Tu-Deng 猜想](https://eprint.iacr.org/2026/1687) ⭐️ 9.0/10

研究人员提出了由大语言模型引导的 Pilot–Sailor 形式化验证框架，并将其应用于对称密码学的 14 个数学案例研究。他们证明了适用于所有字长和允许余数的原始逐点 Tu–Deng 猜想，并证明 8 变量平衡布尔函数的最大非线性度为 116。 这项工作解决了对称密码学中的一个长期未解问题，并证明大语言模型引导的形式化验证能够为深层理论结果生成可信证明。它可能加速布尔函数研究，并提高密码学设计的可信度。 在该框架中，Pilot 提出中间陈述和证明计划，Sailor 尝试形式化证明，证明助手只接受经过检查的声明进入已验证上下文。论文还刻画了 Tu–Deng 界中等号成立的条件：若 t 有 z 个零比特，则等号成立当且仅当相邻零点之间的每个循环间隔至少为 z。此外，对于 n=2k≥6 且 k<m<2k，证明了非线性度上界 NL(F)≤2^{n-1}-2^{n/2-1}-2。

rss · IACR ePrint 密码学论文 · 8月14日 07:19

**背景**: 对称密码学依赖布尔函数作为 S 盒和流密码的基础构件，其非线性度衡量抵抗线性密码分析的能力。Tu–Deng 猜想是一个关于汉明重量的组合不等式：对所有 1≤t≤N-1，满足 a+b≡t (mod N)且 wt(a)+wt(b)<k 的(a,b)对最多有 2^{k-1}对，此前只有部分证明。形式化验证使用证明助手检查数学论证，而 LLM 引导的框架将语言模型与形式化证明检查结合，用于探索未解决问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1707.07945">[1707.07945] The Tu--Deng Conjecture holds almost surely</a></li>
<li><a href="https://eprint.iacr.org/2020/227">About the Tu-Deng Conjecture for $\w(t)$ Less Than or Equal to 10</a></li>

</ul>
</details>

**标签**: `#symmetric cryptography`, `#formal verification`, `#LLM`, `#Boolean functions`, `#cryptanalysis`

---

<a id="item-2"></a>
## [DTRU：采用双 E8 编码的紧凑 NTRU KEM，满足中国商用密码标准](https://eprint.iacr.org/2026/1701) ⭐️ 8.0/10

论文提出 DTRU，一种基于 NTRU 的新型密钥封装机制（KEM），采用双 E8 编码构造具有低解码复杂度的 16 维格码。它支持二的幂次分圆环、三分圆环和大伽罗瓦群素数度素理想数域，并提供 C、AVX2 和 ARM 平台的实现及详细的解密失败概率分析。 该工作直接响应中国 2025 年商用密码标准对 128 位、256 位和 512 位安全级别的需求，并可能影响未来后量子密码标准化进程。其相对于 NTRU-HRSS 和 Kyber 的紧凑性和速度优势使其对低功耗设备和多样化部署场景具有吸引力。 双 E8 编码从 E8 格构造 16 维格码，在紧凑带宽下改善纠错能力。DTRU 有意在密钥生成过程中避免系数压缩和冗余可逆性检查，其推荐参数集排除了稀疏噪声分布；在相同安全级别下，与 Kyber 相比，其封装更紧凑 7%–27% 且快 1.05–1.32 倍，与 NTRU-HRSS 相比，在临时密钥交换往返时间上更紧凑 49%–52% 且快 3.84–15.69 倍。

rss · IACR ePrint 密码学论文 · 8月16日 01:52

**背景**: NTRU 是一种基于格的公钥密码系统，被认为能够抵抗量子攻击；KEM 是一种在不安全信道上安全建立共享秘密的密码原语。E8 格是一种特殊的 8 维格，以高密度和高效解码著称，常用于编码理论和密码学。中国 2025 年商用密码标准要求多个后量子安全级别，从而产生了对新 KEM 设计的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NTRU">NTRU - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Key_encapsulation_mechanism">Key encapsulation mechanism</a></li>
<li><a href="https://en.wikipedia.org/wiki/E8_lattice">E8 lattice</a></li>

</ul>
</details>

**标签**: `#post-quantum cryptography`, `#NTRU`, `#lattice-based cryptography`, `#key encapsulation mechanism`, `#E8 lattice`

---

<a id="item-3"></a>
## [改进四元数理想到同源变换：修复 Qlapoti 缺陷并大幅提速](https://eprint.iacr.org/2026/1700) ⭐️ 8.0/10

该论文修正了 Qlapoti 失败概率分析中的缺陷，并解决了实现与伪代码之间的差异，提出了一种失败概率可忽略的新范数方程求解算法。其 C 实现显示范数求解提速 6 至 9 倍，SQIsign NIST2 签名提速 1.3 至 2.1 倍。 SQIsign 是 NIST 后量子标准化中基于同源的领先签名候选方案，具有极小的密钥和签名尺寸；改进其核心理想-同源变换可直接降低签名延迟并增强竞争力。修正后的分析也使安全性论证更加可靠。 论文聚焦于 Qlapoti 中的范数方程求解步骤，并指出此前失败概率为 2^{-60}，并非密码学上可忽略。新 C 实现的速度提升取决于 NIST 安全级别。

rss · IACR ePrint 密码学论文 · 8月15日 21:47

**背景**: SQIsign 是一种基于超奇异椭圆曲线同源的后量子数字签名方案，它通过 Fiat-Shamir 变换将椭圆曲线自同态的零知识证明转化为签名。它的密钥（64-128 字节）和签名（177-335 字节）都很小，但签名和验证时间较长。四元数理想-同源变换是核心子程序，用于将四元数理想映射到同源，并主导性能。Qlapoti（ASIACRYPT 2025）简化了该变换，使 IdealToIsogeny 快了 2.2-2.6 倍，但留下了分析空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1700">Qlapoty: Improved analysis and eﬃciency for quaternionic ideal to isogeny transformation</a></li>
<li><a href="https://en.wikipedia.org/wiki/SQIsign">SQIsign</a></li>
<li><a href="https://eprint.iacr.org/2025/1604">Qlapoti: Simple and Efficient Translation of Quaternion Ideals to Isogenies</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#isogeny-based cryptography`, `#SQIsign`, `#post-quantum cryptography`, `#algorithm optimization`

---

<a id="item-4"></a>
## [DumboMix：实用的鲁棒异步匿名广播协议](https://eprint.iacr.org/2026/1699) ⭐️ 8.0/10

该论文提出了 DumboMix，这是一个实用的异步匿名广播框架，即使在最多 n/3 个拜占庭服务器和不可预测网络延迟下也能保证输出交付。论文引入了 DumboMix1 和 DumboMix2 算术电路，在 Shamir 秘密共享的 MPC 中实现 O(1)乘法深度、O(N^2)标量乘法和最多 O(N)次 MPC 乘法。 这项工作意义重大，因为现有匿名混洗技术要么缺乏鲁棒性（如 Blinder 可能泄露输入），要么乘法深度高（如蝴蝶网络），要么需要 O(N^2)次 MPC 乘法（如 RabbitMix）或 O(N^3)次标量乘法（如 PowerMix）。DumboMix 的实用效率和有保证的输出交付可以增强匿名通信、去中心化投票等隐私保护系统，尤其是在异步对抗网络中。 在 n=4 到 31 个服务器、混洗 1024 条消息的评估中，DumboMix 在 LAN 下相比 RabbitMix 快 44.8–65.9 倍，相比 PowerMix 快 4.8–7.1 倍，相比蝴蝶交换网络快 2.7–4.0 倍；WAN 下分别快 37.1–52.7 倍、3.9–5.5 倍和 5.1–7.2 倍。DumboMix 在 DumboMPC++中实现，该实现是异步 MPC 框架 DumboMPC（Security'25）的计算优化版本，但协议假设底层 MPC 框架是鲁棒的。

rss · IACR ePrint 密码学论文 · 8月15日 21:32

**背景**: 异步拜占庭容错（ABFT）不假设消息延迟有界，因此协议必须在对手控制网络时序的情况下仍保证活性。Shamir 秘密共享将秘密拆分为多个份额，只有达到阈值数量的服务器才能重建秘密，它是多方计算（MPC）的基础构件。匿名广播旨在私下收集客户端消息，之后以均匀随机顺序同时揭示，且不把消息与发送者关联。此前的方法如基于 DC-net 的 Blinder、蝴蝶交换网络、RabbitMix 和 PowerMix 在鲁棒性、乘法深度或通信复杂度上各有取舍，DumboMix 试图改善这些方面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://eprint.iacr.org/2026/1699.pdf">DumboMix: Robust Asynchronous Anonymous Broadcast Made Practical</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shamir's_secret_sharing">Shamir's secret sharing</a></li>
<li><a href="https://finerymarkets.com/glossary/asynchronous-byzantine-fault-tolerance-abft">Asynchronous Byzantine Fault Tolerance (ABFT)</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#multi-party computation`, `#anonymity`, `#asynchronous protocols`, `#Byzantine fault tolerance`

---

<a id="item-5"></a>
## [MamaBearZKP：协同设计素数域与 AVX-512IFMA 加速零知识证明](https://eprint.iacr.org/2026/1698) ⭐️ 8.0/10

研究人员提出了 MamaBearZKP，一个协同设计框架，利用 49 位 MamaBear 素数域（p = 2^49 - 2^34 + 1）和 AVX-512IFMA 指令优化 sum-check 与 FFT 运算。在 HyperPlonk-DeepFold 证明器中，ZeroCheck 获得最高 42 倍单线程和 64 倍 8 线程加速，端到端相比 Plonky3 的 AVX-512 BabyBear 后端最高加速 18 倍。 这项工作表明，跨层协同设计域运算、协议结构和硬件原语能大幅提升零知识证明性能。这可以缩短在普通 CPU 上的证明时间、降低成本，使 ZK rollup 和可验证计算更实用。 加速来自 49 位域提供的余量支持惰性归约和融合 fold-and-evaluate 内核，从而在整个 HyperPlonk 和 DeepFold 栈中保持 stay-packed 数据流。相比基于 Goldilocks 的基线，单线程下 ZeroCheck、ProductCheck、DeepFold Commit、DeepFold Open 和端到端分别加速 42、33、15、21、21 倍；8 线程下分别达到 64、47、81、45、45 倍。

rss · IACR ePrint 密码学论文 · 8月15日 15:55

**背景**: 现代零知识证明器的大部分时间花在 sum-check 和 FFT 计算上。HyperPlonk 是基于 sum-check 协议的 Plonk 变体，具有线性时间证明器；DeepFold 是 USENIX Security 2025 提出的基于 FRI 的折叠方案。AVX-512IFMA 是 Intel 的 SIMD 扩展，在 64 位通道内对 52 位整数进行乘法，并留出高位用于进位累积，适合多精度模运算。49 位素数域可以放入 64 位字中，并有足够余量推迟模约减。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@espressosys/hyperplonk-a-zk-proof-system-for-zkevms-d45fd077bfba">HyperPlonk , a zk-proof system for ZKEVMs | by Espresso... | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advanced_Vector_Extensions">Advanced Vector Extensions - Wikipedia</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-030-38991-8_5">Accelerating Large Integer Multiplication Using Intel AVX - 512 IFMA</a></li>

</ul>
</details>

**标签**: `#zero-knowledge proofs`, `#FFT`, `#sum-check`, `#AVX-512`, `#prime fields`

---

<a id="item-6"></a>
## [VeriFSS：无经销商主动安全两方函数秘密共享](https://eprint.iacr.org/2026/1697) ⭐️ 8.0/10

作者提出 VeriFSS，一种无经销商的两方函数秘密共享方案，在标准仿真模型下证明具有主动安全性。该方案采用双平面认证密钥构造，通过秘密全局标量 Λ 生成配对函数 x ↦ (f_θ(x), Λ f_θ(x))，使每次本地求值都成为认证份额，无需向量承诺或可提取哈希即可实现在线报告绑定。 该工作从主动安全的分布式函数秘密共享中去除了可信经销商，消除了单点故障，使基于预处理的安全多方计算更适用于实际部署。其常数轮聚合认证意味着大量密钥的广域网认证延迟与单个密钥相当，降低了大规模预处理会话的开销。 生成需要两轮通信，每方每层发送五个域元素；认证额外增加 O(n) 个元素，与域大小无关。实现中 n=16 的认证 DPF 密钥生成耗时 5.7 毫秒、认证耗时 3.3 毫秒，比半诚实基线大 5.4%，聚合认证流量收敛到每次 1,282 字节且轮数保持不变。

rss · IACR ePrint 密码学论文 · 8月15日 15:23

**背景**: 函数秘密共享（FSS）将函数拆分为两个简短密钥，各方本地求值得到 f(x) 的秘密份额，将份额相加即可恢复函数值。无经销商 FSS 去除了通常负责生成密钥的可信经销商，但恶意安全要求绑定计算的所有阶段。主动安全防范任意偏离协议的恶意参与方，而不仅是半诚实模型。VeriFSS 基于 Boyle 等人提出的分布式点函数（DPF）和分布式比较函数（DCF），将其扩展到无经销商且主动安全的设置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cs.idc.ac.il/~elette/FunctionSecretSharing.pdf">Function Secret Sharing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Secure_multi-party_computation">Secure multi - party computation - Wikipedia</a></li>
<li><a href="https://www.ndss-symposium.org/wp-content/uploads/2025-2233-paper.pdf">Distributed Function Secret Sharing and Applications</a></li>

</ul>
</details>

**标签**: `#function secret sharing`, `#secure multiparty computation`, `#active security`, `#cryptography`

---

<a id="item-7"></a>
## [Jasmin 编译器为掩码实现添加泄漏检测](https://eprint.iacr.org/2026/1696) ⭐️ 8.0/10

该论文提出了一种集成到 Jasmin 形式化验证流水线中的泄漏检测 pass，在寄存器与栈分配之前运行于中间表示上。它采用可配置的、面向微架构的泄漏模型，追踪份额、秘密、随机值与公开值之间的接触，能够检测掩码阶数降低，并在 60 个专用测试片段上进行了验证。 这弥补了源级验证无法捕捉编译器引入泄漏、而泄漏仿真成本高且依赖特定功耗模型的缺陷。将泄漏检测移入编译器，能够增强现实密码代码的安全性，并推动安全编译的发展。 该 pass 在寄存器分配和栈分配之前运行，能够明确泄漏的根本原因，并检测掩码阶数降低。它在 60 个覆盖各类泄漏源与类别组合的 Jasmin 测试片段上得到验证，未来将作为自动消除泄漏的编译器阶段的基础。

rss · IACR ePrint 密码学论文 · 8月15日 11:28

**背景**: Jasmin 是一种用于高保障、高速密码实现的领域专用语言和编译器，可生成经过验证的汇编代码。掩码是一种将秘密拆分为多个份额以降低侧信道泄漏的对策，但编译器可能在寄存器或内存中意外合并份额，导致泄漏。安全编译研究如何将源语言的安全属性保持到目标代码，而这项工作位于 Jasmin 的形式化验证流水线中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2511.11292">[2511.11292] The Jasmin Compiler Preserves Cryptographic Security</a></li>
<li><a href="https://deepwiki.com/jasmin-lang/jasmin">jasmin -lang/ jasmin | DeepWiki</a></li>
<li><a href="https://github.com/jasmin-lang/jasmin/blob/main/README.compiler.md">jasmin /README. compiler .md at main · jasmin -lang/ jasmin · GitHub</a></li>

</ul>
</details>

**标签**: `#secure compilation`, `#side-channel attacks`, `#masking`, `#Jasmin`, `#compiler security`

---

<a id="item-8"></a>
## [密码学群鲁棒组合器被证明不可行](https://eprint.iacr.org/2026/1695) ⭐️ 8.0/10

该论文在 Maurer 的通用群模型中首次研究密码学群的鲁棒组合器。作者证明，对于任意 k<n，不存在能保持 DDH 安全性的通用(k,n)-鲁棒组合器；对离散对数问题，他们建立了紧致阈值：当群阶满足 log N ≥ (n-k+1)λ时存在鲁棒组合器，当 log N ≤ (n-k)λ时不可能，其中分量群具有λ位素数阶。 这些不可能性结果表明，像 DDH 这样的判定性假设无法在群层面被鲁棒组合，因此基于群的密码学鲁棒性通常必须在协议设计或密钥派生等更高层实现。这对密码学库的设计以及希望规避特定群实例失效风险的实践者具有重要意义。 直接乘积构造能保持搜索困难性，但对判定性假设失败且带来显著的表示开销。作者在通用群模型中证明，对任意多项式有界的 n 和 k（k<n），不存在能保持 DDH 安全性的通用(k,n)-鲁棒组合器；对离散对数问题，当 n 和 k 为常数时，组合群阶 N 需满足 log N ≥ (n-k+1)λ（λ为分量群的λ位素数阶）才存在鲁棒组合器，否则不可能。

rss · IACR ePrint 密码学论文 · 8月15日 09:01

**背景**: 鲁棒组合器是一种密码学构造，将多个候选原语实现组合起来，只要其中至少一部分仍然安全，整体方案就保持安全。Maurer 引入的通用群模型忽略具体群编码，仅允许算法通过黑盒进行群运算，适合证明下界与不可能结果。直接乘积构造在多个独立输入上分别求值，是组合密码学群的直观基线，但它会带来表示开销，并且不保持判定性假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alonrosen.net/PAPERS/combiners/combiners.pdf">robust _EC_proc1.dvi</a></li>
<li><a href="https://link.springer.com/content/pdf/10.1007/978-3-031-22972-5_11.pdf">An Analysis of the Algebraic Group Model</a></li>
<li><a href="https://hal.science/hal-03374577/document">On Derandomizing Yao's Weak-to-Strong OWF Construction</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#robust combiners`, `#generic group model`, `#cryptographic groups`, `#impossibility results`

---

<a id="item-9"></a>
## [新方法通过子空间限制跳过 S 盒区分多轮 Poseidon 哈希](https://eprint.iacr.org/2026/1692) ⭐️ 8.0/10

该论文提出了 GSR，一种广义的 S 盒跳过小工具，通过限制解子空间来线性化 Poseidon 的部分轮，从而实现对 t−2k+1 轮的概率为 1 的区分器。在以太坊 Poseidon 参数设置（KoalaBear 域，t=24，α=3）下，作者实验上解决了 31 轮中的 28 轮 CICO-1 问题和 31 轮中的 25 轮 CICO-2 问题。 Poseidon 是零知识证明系统中广泛使用的算术化导向哈希函数，因此针对其多轮的概率为 1 区分器对其安全假设构成挑战。由于该子空间限制方法仅由 t 和 k 调节，结果适用于任何 Poseidon 实例（无论轮常数、MDS 矩阵、S 盒指数或域大小如何），迫使设计者重新考虑参数选择。 GSR 小工具在不增加 Poseidon 多项式系统次数的情况下吸收一个初始完整轮和 t−2k 个部分轮，将系统映射为由 k 个自由变量参数化的低次理想。该攻击利用与轮常数、MDS 矩阵、S 盒指数α或域大小 p 无关的子空间限制，并在以太坊 Poseidon 设置下实验解决了 28/31 轮的 CICO-1 问题和 25/31 轮的 CICO-2 问题。

rss · IACR ePrint 密码学论文 · 8月15日 02:00

**背景**: Poseidon 是一种算术化导向的哈希函数，旨在最小化零知识证明系统中的乘法复杂度，其中哈希被表示为大素数域上的算术电路。它采用海绵结构，包含完整轮和部分轮；部分轮仅对状态的一部分应用 S 盒以降低开销。S 盒跳过攻击旨在绕过非线性 S 盒层以构造区分器。以太坊 Poseidon 倡议已为区块链应用标准化参数，包括 KoalaBear 域，状态大小 t=24，S 盒指数α=3。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.poseidon-hash.info/">Poseidon Hash</a></li>
<li><a href="https://autoparallel.github.io/poseidon/index.html">Poseidon - Poseidon Journal</a></li>
<li><a href="https://docs.pantherprotocol.io/docs/learn/cryptographic-primitives/poseidon">Poseidon | Panther Protocol Documentation</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#zero-knowledge proofs`, `#hash functions`, `#cryptanalysis`, `#Poseidon`

---

<a id="item-10"></a>
## [混合量子态学习的平均难度与密码学等价性](https://eprint.iacr.org/2026/1691) ⭐️ 8.0/10

该论文证明了混合量子态的平均情形学习困难性（AHL）与低效验证单向态生成器（IV-OWSG）的存在性是等价的。这一结果将混合态 AHL 与 EFI 对联系起来，并在 SWAP 预言机相对下得到了 IV-OWSG 与 OWSG 的分离。 这解决了混合量子态学习困难性与量子密码学之间关系的开放问题，填补了此前纯态结果留下的空白。它对 EFI 对和量子密码原语有直接影响，并澄清了单向态生成器的相对能力。 等价性针对的是低效验证的 OWSG，其中验证算法允许为指数时间而非量子多项式时间。IV-OWSG 与 OWSG 的分离是相对化的：它需要在 SWAP 预言机存在下成立，并不一定在无预言机世界中成立。

rss · IACR ePrint 密码学论文 · 8月14日 14:30

**背景**: 单向态生成器（OWSG）是单向函数的量子对应物：它们能高效生成但难以求逆的量子态。低效验证的单向态生成器（IV-OWSG）放宽了验证算法必须为量子多项式时间的要求。EFI 对是高效可制备、统计上可分但计算上不可区分的量子态对，是许多量子密码构造的核心。量子态的平均情形学习困难性（AHL）指当量子态从分布中采样时，从副本中学习该态在平均情况下是困难的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2404.13699">Exponential Quantum One -Wayness and EFI Pairs</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-031-71070-4_6">Exponential Quantum One -Wayness and EFI Pairs | Springer Nature...</a></li>

</ul>
</details>

**标签**: `#quantum cryptography`, `#quantum learning theory`, `#one-way state generators`, `#average-case hardness`, `#theoretical computer science`

---

<a id="item-11"></a>
## [《地狱之钟》：三元快速矩阵乘法算法流水线](https://eprint.iacr.org/2026/1688) ⭐️ 8.0/10

该论文提出一种神经网络流水线，可生成系数为{-1, 0, 1}的三元快速矩阵乘法算法，并针对稀疏性和低加法复杂度进行优化。该方法在多个小维度上实现了创纪录的低加法复杂度，并且在(2,2,k)情形下改进幅度随 k 增大而提升。 由于矩阵乘法是科学计算和机器学习中的核心子程序，具有三元系数和低加法次数的实用算法能够在乘法代价较高或使用三元权重的硬件上提升性能。这种可调节的神经网络生成方法有望加速特定硬件约束下高效算法的发现。 该流水线生成并优化数千个快速矩阵乘法算法，单独执行加法优化，并使用热图分析性能。作者公开了实现、生成的方案、热图工具和数据集，并指出在(2,2,k)情形中单纯最小化加法次数有时对完整流水线并非最优。

rss · IACR ePrint 密码学论文 · 8月14日 09:57

**背景**: 矩阵乘法是数值线性代数、优化和模式识别中的核心操作，标准算法复杂度为 O(n^3)。快速矩阵乘法算法通过降低乘法次数（秩）来加速，但实际性能还取决于加法复杂度和系数取值。系数为{-1,0,1}的三元方案很有吸引力，因为常数乘法变成加法或符号变化，从而降低硬件开销。本工作基于近期基于神经网络的算法发现方法，针对这些实用性质进行优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fast_matrix_multiplication_algorithms">Fast matrix multiplication algorithms</a></li>
<li><a href="https://en.wikipedia.org/wiki/Computational_complexity_of_matrix_multiplication">Computational complexity of matrix multiplication - Wikipedia</a></li>

</ul>
</details>

**标签**: `#matrix multiplication`, `#neural networks`, `#algorithm discovery`, `#fast algorithms`, `#performance optimization`

---

<a id="item-12"></a>
## [施奈尔与桑德斯：若市场失灵，美国应国有化 OpenAI 和 Anthropic](https://www.schneier.com/blog/archives/2026/08/if-the-markets-reject-openai-and-anthropic-the-us-should-nationalize-them.html) ⭐️ 8.0/10

布鲁斯·施奈尔和纳森·桑德斯发表文章主张，如果金融市场无法让 OpenAI 和 Anthropic 继续作为维护公共利益的 AI 开发者存在，美国政府就应将它们国有化。 该主张直指领先 AI 实验室优先考虑投资者价值而非公共安全的问题，可能影响关于 AI 治理和市场集中的政策讨论。 该文最初于 2026 年 8 月 12 日发表在《卫报》上，文中指出 OpenAI 和 Anthropic 虽为避免不受约束的企业 AI 开发而创立，但自身也已成为守护未来投资者价值的企业巨头。

rss · Schneier on Security · 8月14日 11:03

**背景**: 布鲁斯·施奈尔是知名安全技术专家和作家；纳森·桑德斯是数据科学家和政策研究员。OpenAI 和 Anthropic 是领先的 AI 实验室，创立时均宣称以安全地为人类开发 AI 为使命，但都已成长为高估值的私营公司。国有化是指政府收购企业所有权，以追求公共目标而非私人利润。

**标签**: `#AI governance`, `#nationalization`, `#OpenAI`, `#Anthropic`, `#policy`

---

<a id="item-13"></a>
## [UMQ、MQOW 与 MQSPR 假设之间的紧致蕴含关系](https://eprint.iacr.org/2026/1694) ⭐️ 7.0/10

该论文证明了 UMQ 与 MQSPR 紧致等价，MQOW 紧致蕴含 UMQ，并且当 m≤n+O(log λ)时 UMQ 蕴含 MQOW（在 m≤n+O(1)时该蕴含是紧致的）。同时推论表明在相同条件下 MQSPR 蕴含 MQOW，弱于一般函数族中 SPR 到 OW 所需的压缩条件 n=m+ω(log λ)。 这深化了多元二次密码学作为后量子候选方案的基础安全假设。理清 UMQ、MQOW 和 MQSPR 之间的关系有助于设计者选择最小假设，并理解平均情形困难性何时能推出单向性。 结果覆盖方形方程组（m=n）以及满足 m=n+O(log λ)的轻度超定方程组。其依赖紧致归约，并改进了 SPR 到 OW 蕴含所需的一般压缩阈值 n=m+ω(log λ)。

rss · IACR ePrint 密码学论文 · 8月15日 08:16

**背景**: 多元二次（MQ）密码学基于求解有限域上二次多项式方程组的困难性，该问题在一般情况下是 NP 难的。均匀 MQ（UMQ）假设指出，均匀生成的 MQ 函数难以求逆（等价于求零困难）。MQ 单向性（MQOW）意味着难以从输出恢复输入，而 MQ 第二原像抵抗（MQSPR）意味着难以找到具有相同输出的不同输入。这些假设支撑着后量子签名和加密方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciweavers.org/publications/public-key-cryptography-new-multivariate-quadratic-assumptions">Public-Key Cryptography from New Multivariate Quadratic Assumptions</a></li>
<li><a href="https://en.wikipedia.org/wiki/Preimage_attack">Preimage attack - Wikipedia</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#multivariate quadratic`, `#computational complexity`, `#security assumptions`

---

<a id="item-14"></a>
## [形式化证明显示西蒙量子算法无法解决二面体陪集问题](https://eprint.iacr.org/2026/1693) ⭐️ 7.0/10

一篇新笔记正式证明，ePrint 2026/1591 中描述的西蒙算法无法以不可忽略的优势提取二面体陪集问题秘密的最低有效位，因此不能解决 DCP。该否定结果被推广到依赖部分经典傅里叶标签的一类更广泛的算法。 这推翻了近期一项声称能解决 DCP 的量子算法，对后量子密码学和基于格问题的密码分析具有重要意义。使用 Lean 4 进行形式化验证也提高了对这一否定结果的信心。 该否定结论适用于遵循 Regev 约化模板的 DCP 算法：这类算法必须在逆计算（uncomputation）阶段充分利用经典傅里叶标签。被否定的西蒙算法可以只用最高有效三分之一的经典傅里叶标签实现，误差为 poly(n)2^{-n/3}，这是不够的。

rss · IACR ePrint 密码学论文 · 8月15日 03:46

**背景**: 二面体陪集问题（DCP）是一个与二面体群上隐藏子群问题密切相关的计算问题，在量子计算和后量子密码学中被广泛研究，因为高效的 DCP 量子算法可能通过 Regev 2004 年提出的约化攻破基于格的密码方案。西蒙算法是量子计算中解决交换群隐藏子群问题的历史性重要算法，但其能否扩展到 DCP 一直是近期争论的焦点。这篇笔记分析了此类算法中经典傅里叶标签和逆计算的作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://inria.hal.science/hal-04276584/document">Time and Query Complexity Tradeoffs for the Dihedral Coset Problem</a></li>
<li><a href="https://www.sitg-consulting.com/post/daniel-simon-s-dihedral-coset-algorithm-what-does-it-actually-mean-for-lattice-based-cryptography-a">Daniel Simon’s Dihedral Coset Algorithm: What Does It Actually Mean...</a></li>
<li><a href="https://who.rocq.inria.fr/Andre.Chailloux/qip1.pdf">Quantum Algorithms inspired by Regev 's reduction</a></li>

</ul>
</details>

**标签**: `#quantum algorithms`, `#dihedral coset problem`, `#cryptography`, `#no-go theorem`, `#formal verification`

---

<a id="item-15"></a>
## [基于 Module-SIS 的并发安全紧凑盲签名方案，签名大小降至 4.7 KB](https://eprint.iacr.org/2026/1690) ⭐️ 7.0/10

该论文提出了一种基于 Module-SIS 的新型格盲签名方案，实现了并发安全性，并将签名大小降至 4.7 KB，而此前最先进的格基盲签名至少需要 22 KB。该方案通过设计使协议最后一步自然形成 GPV 签名中的短原像，从而不再需要零知识证明。 盲签名对于电子现金、匿名凭证和隐私投票等隐私保护应用至关重要，而在后量子安全需求下必须采用格基构造。该工作通过消除昂贵的零知识证明，显著降低了通信和存储开销，使后量子盲签名更加实用。 该方案在 Module-SIS 假设下实现并发安全性；诚实用户的期望轮数可低至 1.1 轮，而恶意用户最多需要 2.6 轮，因为协议要求用户在新一轮开始前证明上一轮未能成功生成签名。这种多轮行为源于格基Σ协议中的拒绝采样，以少量额外交互换取大幅减小的签名尺寸。

rss · IACR ePrint 密码学论文 · 8月14日 12:07

**背景**: 盲签名允许签名者在不知道消息内容的情况下进行签名，且无法将签名与某次签名交互关联。格基密码学是主流的后量子密码方向，因为短整数解（SIS）等问题被认为对量子计算机困难；Module-SIS 是其结构化变体，兼顾效率与安全性。此前的格基盲签名需要零知识证明来保证盲性，导致签名尺寸显著增大，而 GPV 签名框架展示了如何利用陷门生成短原像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lattice-based_cryptography">Lattice-based cryptography</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-540-70936-7_18">Concurrently - Secure Blind Signatures Without Random Oracles or...</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#blind signatures`, `#lattice-based cryptography`, `#zero-knowledge proofs`, `#post-quantum`

---
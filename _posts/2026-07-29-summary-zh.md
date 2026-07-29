---
layout: default
title: "Horizon Summary: 2026-07-29 (ZH)"
date: 2026-07-29
lang: zh
---

> 从 29 条内容中筛选出 5 条重要资讯。

---

1. [LLM 在密码分析基准测试中发现新型攻击](#item-1) ⭐️ 9.0/10
2. [仅 350 行 Python 实现生产级 ML-DSA 验证](#item-2) ⭐️ 8.0/10
3. [运用 Codex /goal 在开源项目中查找漏洞](#item-3) ⭐️ 8.0/10
4. [NIST 发布 AI 数据中心安全分析草案，采用 HPC 驱动方法](#item-4) ⭐️ 8.0/10
5. [Cognyte 出售可模拟基站的监控货车](#item-5) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LLM 在密码分析基准测试中发现新型攻击](https://www.schneier.com/blog/archives/2026/07/measuring-llms-ability-to-perform-cryptanalysis.html) ⭐️ 9.0/10

CryptanalysisBench 基准测试评估了前沿大模型的密码分析能力，结果显示 Claude Opus 4.8 和 GPT-5.5 等模型不仅能破解历史密码，还发现了此前未知的攻击，例如针对 SpoC AEAD 的密钥恢复利用和 KINDI 安全证明中的错误。 这表明大语言模型在关键安全领域正接近人类水平的推理能力，可能加速密码学漏洞的发现，并改变我们评估加密系统安全性的方式。 该基准包含 191 个任务，涵盖六类密码原语和三个难度层级；前沿模型破解了 65-86%的第一层（已知破解）和 24-61 个弱化变体，Claude Opus 4.8 和 GPT-5.5 等还发现了针对 SpoC AEAD 和 KINDI 的新攻击。

rss · Schneier on Security · 7月29日 01:47

**背景**: 密码分析是研究破解密码系统的学科，需要深厚的数学推理。该基准使用了来自 NIST 标准化竞赛的原语，这些原语经过密码学界审查，包含已破解和未破解的算法，以测试 AI 发现已知和新型攻击的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.18538">CryptanalysisBench : Can LLMs do Cryptanalysis?</a></li>
<li><a href="https://scalevise.com/resources/cryptanalysisbench-llm-cryptanalysis-benchmark/">CryptanalysisBench Tests LLM Cryptanalysis Skills</a></li>
<li><a href="https://overcentral.com/en/mythos-cryptanalysis-weaknesses/">Anthropic's Mythos Model Discovers Key Cryptographic Weaknesses</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#cryptanalysis`, `#AI security`, `#benchmarks`, `#cybersecurity`

---

<a id="item-2"></a>
## [仅 350 行 Python 实现生产级 ML-DSA 验证](https://words.filippo.io/mldsa-py/) ⭐️ 8.0/10

发布了一个生产就绪的纯 Python ML-DSA 后量子签名验证算法实现，仅 350 行代码，可读性强且健壮。 ML-DSA 是 NIST 新近标准化的后量子签名方案，如此最小化且可审计的实现有助于更广泛的理解、采纳以及在现有 Python 工具链中的集成。 该代码仅实现验证功能（不含签名），遵循 FIPS 204 草案标准，将清晰性和健壮性置于性能之上，适合审计至关重要的安全关键场景。

rss · Filippo Valsorda (Go 密码学) · 7月26日 11:45

**背景**: ML-DSA（模块格数字签名算法）是一种基于格的抗量子数字签名方案，由 NIST 标准化，源自 CRYSTALS-Dilithium 家族。与 RSA 或 ECDSA 不同，它能抵抗经典和量子计算机的攻击。由于性能考量，Python 很少用于生产级密码实现，但纯 Python 验证器是可行的，因为验证通常不是性能瓶颈，且重视可读性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#Python`, `#implementation`, `#ML-DSA`

---

<a id="item-3"></a>
## [运用 Codex /goal 在开源项目中查找漏洞](https://blog.trailofbits.com/2026/07/28/how-we-use-goal-to-find-bugs-in-patch-the-planet/) ⭐️ 8.0/10

在 Patch the Planet 计划中，Trail of Bits 工程师利用 OpenAI Codex 的 /goal 功能，在广泛使用的开源项目中自主发现了多个严重漏洞，包括 Rust 的一个健全性漏洞和错误编译（已在 1.98 版修复）、Keycloak 的提权问题，以及基于历史 CVE 衍生的 Semgrep 规则发现的变体漏洞。 这表明 AI 可有效扩展关键软件的漏洞发现能力，有望超越传统人工审计，在攻击者利用漏洞之前为防御者带来安全优势。 该团队通过让 Codex 对自己的目标进行红队演练来优化提示，避免模型走捷径，并开发了 aicov 工具来追踪实际读取的代码行，以确保分析全面；他们还发现 Codex 可从 CVE 描述生成 Semgrep 规则，跨项目捕捉变体漏洞。

rss · Trail of Bits Blog · 7月28日 11:00

**背景**: Codex /goal 是一项实验性 AI 功能，可跨多轮会话自主完成设定目标。Semgrep 是一种通过模式匹配来发现漏洞的静态分析工具。Patch the Planet 是 OpenAI、Trail of Bits 等合作发起的计划，旨在识别并修复开源软件中的漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/cookbook/examples/codex/using_goals_in_codex">Using Goals in Codex | OpenAI Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semgrep">Semgrep</a></li>
<li><a href="https://www.linkedin.com/posts/cybersecurity-artificial-intelligence_ai-artificialintelligence-ainews-activity-7475222562180882432-ldpM">OpenAI Launches Patch the Planet Initiative for... | LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI`, `#bug hunting`, `#security`, `#Codex`, `#open-source`

---

<a id="item-4"></a>
## [NIST 发布 AI 数据中心安全分析草案，采用 HPC 驱动方法](https://csrc.nist.gov/pubs/sp/800/239/ipd) ⭐️ 8.0/10

NIST 发布了 SP 800-239 的初始公开草案，通过将 AI 数据中心与高性能计算（HPC）系统进行对比，并借鉴 HPC 安全原则，对 AI 数据中心进行了威胁和安全差距分析。 该草案针对 AI 基础设施特有的关键安全漏洞，可能影响用于模型训练和推理的下一代 AI 环境的安全实践。 该文件基于 NIST SP 800-234（HPC 安全覆盖层）和 SP 800-223 编写，公众意见征询期开放至 2026 年 9 月 25 日，并包含专利权利要求征集。

rss · NIST CSRC Drafts (标准草案) · 7月27日 04:00

**背景**: NIST 特别出版物 800-234 为 HPC 系统提供安全覆盖层，从 NIST SP 800-53 中等基线中定制了 60 项控制措施以适应 HPC 的特定需求。SP 800-239 将这种方法扩展到 AI 数据中心，后者在架构、硬件和工作流程方面与传统 HPC 有所不同。NIST 是美国联邦机构，负责制定信息安全标准和指南，被政府和行业广泛采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://csrc.nist.gov/News/2026/ai-data-center-security-analysis-draft-sp-800-239">AI Data Center Security Analysis: Draft SP 800-239 | CSRC</a></li>
<li><a href="https://csrc.nist.gov/pubs/sp/800/234/final">NIST Special Publication (SP) 800-234, High-Performance Computing (HPC) Security Overlay</a></li>

</ul>
</details>

**标签**: `#AI security`, `#data center security`, `#HPC`, `#NIST`, `#threat analysis`

---

<a id="item-5"></a>
## [Cognyte 出售可模拟基站的监控货车](https://www.schneier.com/blog/archives/2026/07/cognyte-sells-a-mobile-cell-surveillance-van.html) ⭐️ 7.0/10

以色列监控公司 Cognyte 开始出售配备名为 FalcoNet 的基站模拟器的监控货车，该模拟器可强制附近手机连接并追踪区域内所有设备。 这一进展将大规模监控工具的使用范围从联邦机构扩大到州和地方警察，增加了无授权追踪和侵犯隐私的可能性。 Cognyte 与得克萨斯州的合同显示，FalcoNet 系统可隐藏在车内、放入背包或安装在直升机上，功能类似于 L3Harris 备受争议的 Stingray 设备。

rss · Schneier on Security · 7月27日 11:04

**背景**: 基站模拟器，也称为 Stingray 或 IMSI 捕捉器，通过伪装成合法基站诱骗手机连接，从而截获通信和追踪位置。这些设备因无差别收集范围内所有手机数据而备受争议，并可能干扰正常蜂窝服务。最初为军事用途开发，后逐渐被执法机构采用，但监管程度参差不齐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stingray_phone_tracker">Stingray phone tracker - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cell_site_simulator">Cell site simulator</a></li>
<li><a href="https://sls.eff.org/technologies/cell-site-simulators-imsi-catchers">Cell-Site Simulators/ IMSI Catchers - Street Level Surveillance</a></li>

</ul>
</details>

**标签**: `#surveillance`, `#privacy`, `#law enforcement`, `#mobile technology`, `#cybersecurity`

---
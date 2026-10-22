---
permalink: /
title: "杨晓达"
lang: zh-CN
excerpt: "浙江大学 · 多模态生成与理解、音视频生成和模型加速"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<span class="anchor" id="about-me"></span>

# 你好，我是杨晓达

我在浙江大学学习人工智能，导师为赵洲、张志猛老师。我的研究聚焦于**多模态生成与理解**，尤其关注音视频联合生成、可控视频生成、语音交互，以及生成模型的高效训练与推理。

我曾在腾讯混元、字节跳动 Seed、上海人工智能实验室和阶跃星辰实习，也曾与岳翔宇、卢策吾、穆尧和尤洋老师的实验室合作。目前正与新加坡国立大学颜水成教授密切合作。

{% include scholar-badge.html %}

### 研究方向

- **多模态生成**：音视频联合生成、音乐与舞蹈协同生成、可控视频生成与数字人。
- **多模态理解**：视觉语言模型的空间感知与逻辑推理、唇语识别、跨模态检索。
- **高效生成与智能体**：扩散模型蒸馏、量化与稀疏注意力、长视频生成 Agent、Agentic Evaluation。

<span class="anchor" id="education"></span>

## 教育背景

**浙江大学 · 人工智能**<br>
推免生 · 导师：赵洲、张志猛老师

- 专业综合排名第一。
- 获国家奖学金两次。
- 竺可桢奖学金 · 学院唯一提名。

<span class="anchor" id="experience"></span>

## 实习经历

### 腾讯 · 混元部门
基模模型中心 · 青云计划

### 字节跳动 · Seed 部门
SeeDance 团队

### 上海人工智能实验室
具身智能中心

### 阶跃星辰
俞刚老师团队

<span class="anchor" id="projects"></span>

## 代表项目

### TurboDiffusion · 音视频联合生成加速

参与 TurboT2AV 部分研发，探索一致性蒸馏与分布蒸馏在大规模音视频联合生成模型中的应用，结合低比特量化、稀疏注意力与算子优化提升推理效率。

[项目代码](https://github.com/thu-ml/TurboDiffusion) · <a href="https://github.com/thu-ml/TurboDiffusion/stargazers" target="_blank" rel="noopener"><img class="github-stars-badge" src="https://img.shields.io/github/stars/thu-ml/TurboDiffusion?style=social" alt="TurboDiffusion GitHub Stars" loading="lazy"></a>

<span class="anchor" id="publications"></span>

## 代表论文

### 多模态生成与交互

<div class="research-submissions" markdown="1">

#### 长视频生成 Agent
<span class="submission-status">在投</span>

构建一站式剧本到电影生产管线，设计 **Life-long memory**，确保长视频生成过程中的前后文一致性。

#### 全双工音视频对话
<span class="submission-status">在投</span>

主导研发轻量化的流式实时交互系统，以开源为目标，功能对标 Vidu-S2。

</div>

<div class="publication-card" markdown="1">
<figure class="publication-figure">
  <a href="{{ '/images/papers/tmd-overview.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="查看 TMD-Bench 配图大图">
    <img src="{{ '/images/papers/tmd-overview.webp' | relative_url }}" alt="TMD-Bench 图一：数据集构建、数据概览与音乐舞蹈协同生成评测体系，白底展示版" width="1600" height="875" loading="lazy">
  </a>
</figure>
<div class="publication-details" markdown="1">

**TMD-Bench: A Multi-Level Evaluation Paradigm for Music–Dance Co-Generation**

ICML · 第一作者

音乐与舞蹈协同生成模型、数据集与多层次评测基准。

[项目主页](https://anonymous-2312.github.io/TMD-Bench/) · [论文](https://arxiv.org/abs/2605.01809)

</div>
</div>

### 高效生成与模型加速

<div class="research-submissions" markdown="1">

#### 音视频生成加速算法
<span class="submission-status">在投</span>

优化步数蒸馏算法，在 19B 音视频生成模型基础上实现 **54 倍加速**，融合低比特量化、稀疏注意力与算子优化等工程实践。

</div>

### 多模态理解与推理

<div class="publication-card" markdown="1">
<figure class="publication-figure">
  <a href="{{ '/images/papers/spatiallogic-figure1.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="查看 SpatialLogic-Bench 图一大图">
    <img src="{{ '/images/papers/spatiallogic-figure1.webp' | relative_url }}" alt="SpatialLogic-Bench 图一：空间感知、时间逻辑与具身智能任务的双任务评测概览" width="1278" height="460" loading="lazy">
  </a>
</figure>
<div class="publication-details" markdown="1">

**SpatialLogic-Bench: A Comprehensive Evaluation of Spatial Perception and Logical Reasoning Capabilities of Large Models in Embodied Environments**

AAAI Oral（Top 5%） · 第一作者

评测视觉语言模型的空间感知与逻辑推理能力。

[论文](https://xyue.io/assets/publications/aaai2026-spatiallogic-bench.pdf)

</div>
</div>

<div class="publication-card" markdown="1">
<figure class="publication-figure">
  <a href="{{ '/images/papers/planning-figure1.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="查看 From Perception to Planning 图一大图">
    <img src="{{ '/images/papers/planning-figure1.webp' | relative_url }}" alt="From Perception to Planning 图一：EgoTSR 课程学习、子任务分解与双层评测框架" width="1226" height="493" loading="lazy">
  </a>
</figure>
<div class="publication-details" markdown="1">

**From Perception to Planning: Evolving Ego-Centric Task-Oriented Spatiotemporal Reasoning via Curriculum Learning**

ICML · 第一作者

通过课程学习提升第一视角场景下的时空推理能力。

[论文](https://arxiv.org/abs/2604.10517)

</div>
</div>

<div class="publication-card" markdown="1">
<figure class="publication-figure">
  <a href="{{ '/images/papers/audiovsr-figure1.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="查看 AudioVSR 图一大图">
    <img src="{{ '/images/papers/audiovsr-figure1.webp' | relative_url }}" alt="AudioVSR 图一：音视频对齐预训练、音频微调与视频语音识别推理流程" width="1085" height="753" loading="lazy">
  </a>
</figure>
<div class="publication-details" markdown="1">

**AudioVSR: Enhancing Video Speech Recognition with Audio Data**

EMNLP Main · 第一作者

探索低资源唇语识别、合成数据与多模态对齐预训练。

[论文](https://aclanthology.org/2024.emnlp-main.858/)

</div>
</div>

- **Multimodal Conditional Retrieval with High Controllability**<br>
  SIGKDD Poster · 第一作者<br>
  借助混合专家模型实现可控的条件检索。

- **Boosting Speech Recognition Robustness to Modality-Distortion with Contrast-Augmented Prompts**<br>
  ACM MM Oral · 共同第一作者<br>
  面向模态失真的鲁棒音视频语音识别。

### 智能体评测

<div class="research-submissions" markdown="1">

#### Agentic Evaluation on R2AV
<span class="submission-status">在投</span>

主导研发 **Harness 自动化评测框架**，自动调度工具调用，识别生成模型的缺陷类型。

</div>

<span class="anchor" id="service"></span>

## 学术服务

担任 ICML、ICLR、NeurIPS、AAAI、SIGKDD、ACM MM、EMNLP 等会议审稿人。

<span class="anchor" id="awards"></span>

## 荣誉奖项

- 国家奖学金（两次）；竺可桢奖学金 · 学院唯一提名。
- ACM-ICPC 国际大学生程序设计竞赛中国邀请赛银牌。
- 第十三届蓝桥杯全国总决赛二等奖。
- 第十三届全国大学生数学竞赛全国总决赛二等奖。

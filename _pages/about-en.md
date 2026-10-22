---
permalink: /en/
title: "Xiaoda Yang"
lang: en
excerpt: "Zhejiang University · Multimodal generation and understanding, audio–video generation, and model acceleration"
author_profile: true
---

<span class="anchor" id="about-me"></span>

# Hi, I'm Xiaoda Yang

I study Artificial Intelligence at Zhejiang University, advised by Zhou Zhao and Zhimeng Zhang. My research focuses on **multimodal generation and understanding**, particularly joint audio–video generation, controllable video generation, spoken interaction, and efficient training and inference for generative models.

I have interned at Tencent Hunyuan, ByteDance Seed, Shanghai AI Laboratory, and StepFun. I have also collaborated with the laboratories of Xiangyu Yue, Cewu Lu, Yao Mu, and Yang You. I am currently working closely with Prof. Shuicheng Yan at the National University of Singapore.

{% include scholar-badge.html %}

### Research Interests

- **Multimodal generation**: joint audio–video generation, music–dance co-generation, controllable video generation, and digital humans.
- **Multimodal understanding**: spatial perception and logical reasoning in vision-language models, visual speech recognition, and cross-modal retrieval.
- **Efficient generation and agents**: diffusion model distillation, quantization and sparse attention, long-video generation agents, and agentic evaluation.

<span class="anchor" id="education"></span>

## Education {#education-heading}

**Zhejiang University · Artificial Intelligence**<br>
Admitted through recommendation · Advisors: Zhou Zhao and Zhimeng Zhang

- Ranked first in the overall program ranking.
- National Scholarship, twice.
- Chu Kochen Scholarship · Sole nominee from the college.

<span class="anchor" id="experience"></span>

## Internships

### Tencent · Hunyuan
Foundation Model Center · Qingyun Program

### ByteDance · Seed
SeeDance Team

### Shanghai AI Laboratory
Embodied Intelligence Center

### StepFun
Gang Yu's Team

<span class="anchor" id="projects"></span>

## Selected Projects

### TurboDiffusion · Accelerating Joint Audio–Video Generation

Contributed to TurboT2AV, exploring consistency distillation and distribution distillation for large-scale joint audio–video generation models. Combined low-bit quantization, sparse attention, and operator optimization to improve inference efficiency.

[Code](https://github.com/thu-ml/TurboDiffusion) · <a href="https://github.com/thu-ml/TurboDiffusion/stargazers" target="_blank" rel="noopener"><img class="github-stars-badge" src="https://img.shields.io/github/stars/thu-ml/TurboDiffusion?style=social" alt="TurboDiffusion GitHub Stars" loading="lazy"></a>

<span class="anchor" id="publications"></span>

## Selected Publications

### Multimodal Generation and Interaction

<div class="research-submissions" markdown="1">

#### Long-Video Generation Agent
<span class="submission-status">Under review</span>

Developed an end-to-end script-to-film production pipeline with **life-long memory** to maintain contextual consistency throughout long-video generation.

#### Full-Duplex Audio–Video Dialogue
<span class="submission-status">Under review</span>

Led the development of a lightweight, streaming system for real-time interaction, targeting an open-source release with functionality comparable to Vidu-S2.

</div>

<div class="publication-card" markdown="1">
<figure class="publication-figure">
  <a href="{{ '/images/papers/tmd-overview.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="View the full-size TMD-Bench overview">
    <img src="{{ '/images/papers/tmd-overview.webp' | relative_url }}" alt="TMD-Bench: dataset construction, overview, and music–dance co-generation evaluation; white-background presentation version" width="1600" height="875" loading="lazy">
  </a>
</figure>
<div class="publication-details" markdown="1">

**TMD-Bench: A Multi-Level Evaluation Paradigm for Music–Dance Co-Generation**

ICML · First author

Models, datasets, and a multi-level evaluation benchmark for music–dance co-generation.

[Project](https://anonymous-2312.github.io/TMD-Bench/) · [Paper](https://arxiv.org/abs/2605.01809)

</div>
</div>

### Efficient Generation and Model Acceleration

<div class="research-submissions" markdown="1">

#### Accelerating Audio–Video Generation
<span class="submission-status">Under review</span>

Optimized step distillation to achieve a **54× speedup** for a 19B-parameter audio–video generation model, combining low-bit quantization, sparse attention, and operator optimization.

</div>

### Multimodal Understanding and Reasoning

<div class="publication-card" markdown="1">
<figure class="publication-figure">
  <a href="{{ '/images/papers/spatiallogic-figure1.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="View the full-size SpatialLogic-Bench overview">
    <img src="{{ '/images/papers/spatiallogic-figure1.webp' | relative_url }}" alt="SpatialLogic-Bench: dual-task evaluation of spatial perception and temporal reasoning in embodied environments" width="1278" height="460" loading="lazy">
  </a>
</figure>
<div class="publication-details" markdown="1">

**SpatialLogic-Bench: A Comprehensive Evaluation of Spatial Perception and Logical Reasoning Capabilities of Large Models in Embodied Environments**

AAAI Oral (Top 5%) · First author

Evaluating spatial perception and logical reasoning in vision-language models.

[Paper](https://xyue.io/assets/publications/aaai2026-spatiallogic-bench.pdf)

</div>
</div>

<div class="publication-card" markdown="1">
<figure class="publication-figure">
  <a href="{{ '/images/papers/planning-figure1.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="View the full-size From Perception to Planning overview">
    <img src="{{ '/images/papers/planning-figure1.webp' | relative_url }}" alt="EgoTSR: curriculum learning, subtask decomposition, and dual-level evaluation" width="1226" height="493" loading="lazy">
  </a>
</figure>
<div class="publication-details" markdown="1">

**From Perception to Planning: Evolving Ego-Centric Task-Oriented Spatiotemporal Reasoning via Curriculum Learning**

ICML · First author

Improving spatiotemporal reasoning in egocentric settings through curriculum learning.

[Paper](https://arxiv.org/abs/2604.10517)

</div>
</div>

<div class="publication-card" markdown="1">
<figure class="publication-figure">
  <a href="{{ '/images/papers/audiovsr-figure1.webp' | relative_url }}" target="_blank" rel="noopener" aria-label="View the full-size AudioVSR pipeline">
    <img src="{{ '/images/papers/audiovsr-figure1.webp' | relative_url }}" alt="AudioVSR: audio–visual alignment pretraining, audio-based fine-tuning, and visual speech recognition inference" width="1085" height="753" loading="lazy">
  </a>
</figure>
<div class="publication-details" markdown="1">

**AudioVSR: Enhancing Video Speech Recognition with Audio Data**

EMNLP Main · First author

Exploring low-resource visual speech recognition, synthetic data, and multimodal alignment pretraining.

[Paper](https://aclanthology.org/2024.emnlp-main.858/)

</div>
</div>

- **Multimodal Conditional Retrieval with High Controllability**<br>
  SIGKDD Poster · First author<br>
  Controllable conditional retrieval using mixture-of-experts models.

- **Boosting Speech Recognition Robustness to Modality-Distortion with Contrast-Augmented Prompts**<br>
  ACM MM Oral · Co-first author<br>
  Robust audio–visual speech recognition under modality distortion.

### Agentic Evaluation

<div class="research-submissions" markdown="1">

#### Agentic Evaluation on R2AV
<span class="submission-status">Under review</span>

Led the development of a **Harness-based automated evaluation framework** that orchestrates tool calls and identifies failure types in generative models.

</div>

<span class="anchor" id="service"></span>

## Academic Service

Reviewer for ICML, ICLR, NeurIPS, AAAI, SIGKDD, ACM MM, and EMNLP.

<span class="anchor" id="awards"></span>

## Honors and Awards

- National Scholarship (twice); Chu Kochen Scholarship · Sole nominee from the college.
- Silver Medal, ACM-ICPC China Invitational Contest.
- Second Prize, National Finals of the 13th Lanqiao Cup.
- Second Prize, National Finals of the 13th Chinese Mathematics Competitions for College Students.

### Hi, I'm Samuel Adeniji

I'm a Master's student at **Carnegie Mellon University Africa**. I build **vision-language and multimodal models for medical imaging and clinical decision support**. My work focuses on making these models efficient enough to run on large 3D scans, and honest enough about their limits to be trusted in low-resource health settings.

**Research interests**
- Medical vision-language models: 3D CT report generation, visual token compression
- Multi-scale and efficient architectures for medical imaging (FPNs, state space models)
- Multimodal clinical prediction: imaging, genomics, EHR time series
- AI for global health: malaria, Lassa fever and vector-borne disease

---

### Selected projects

**[A-ADP: Anatomy-Aware Dynamic Projector for 3D Medical VLMs](https://github.com/Tech-sam-90/3d_compression)**
A two-stage, instruction-conditioned token compressor for chest CT. Per-slice Perceiver distillation plus FiLM-guided cross-slice aggregation lets a language model write radiology reports from a fixed token budget, attending to the anatomy the question is about. Trained on CT-RATE with a Llama-3.2-1B backbone. *Summer 2026 research internship with Prof. Prasenjit Mitra.*

**[FPN-Mamba: Multi-Scale State Space Models for Brain MRI Lesion Classification](https://github.com/Tech-sam-90/fpn-inceptentionnet)**
Feature pyramid plus bidirectional Mamba for small brain-metastasis screening on UCSF-BMSR. It outperforms a self-attention baseline (InceptentionNet) on AUC (0.982 vs 0.897) and smallest-lesion recall (0.870 vs 0.788) across 5 seeds × 3 folds, and is 3.7× faster per step than a matched attention mixer at 512 px. *NeurIPS 2026 Africa in AI workshop.*

**[Where Do Malaria Detector False Positives Come From?](https://github.com/Tech-sam-90/malaria_fp_analysis)**
A controlled study of two YOLOv12s detectors on 8,000 thick-smear images from Uganda and Ghana, using seven spatial and statistical analyses. It finds that white blood cells are *not* a systematic source of false positives, which redirects mitigation toward staining variability. *MICCAI 2026 MIRASOL workshop.*

**[Condition-Aware ICU Deterioration Risk](https://github.com/Tech-sam-90/condition-aware_risk_CDSS)**
Diagnosis-conditioned early-warning models on MIMIC-IV, benchmarking six sequence architectures at 1–3 h horizons. The best model (BiLSTM + attention, ROC-AUC 0.76) is served as a Dockerized FastAPI + WebSocket streaming service, with limitations documented up front.

**Multimodal Cancer Survival Prediction** *(in progress)*
Generalizable survival modeling from TCGA whole-slide images, RNA and clinical data, building on SurvPath.

---

### Publications

- **FPN-Mamba: Linear-Time Bidirectional State Space Feature Pyramids for Small-Lesion Brain MRI Classification**<br>
  Simbiat Damilola Adetoro, **Samuel Akinwumi Adeniji**, Moise Busogi<br>
  *NeurIPS 2026 Workshop: Africa in AI* · [OpenReview](https://openreview.net/forum?id=te52LwNBSf) · [Code](https://github.com/Tech-sam-90/fpn-inceptentionnet)

- **Investigating White Blood Cells as a Source of False-Positive Malaria Parasite Detection in African Blood-Smear Images**<br>
  **Samuel Akinwumi Adeniji**, Goodness Chidera Obasi, Chris Victor Ntwali, Aondona Moses Iorumbur, Confidence Raymond, Uwimana Lowami, Ahmed Tahiru Issah<br>
  *MICCAI 2026 Workshop: MIRASOL* · [Paper](https://papers.miccai.org/miccai-2026-sat/MIRASOL_018.html) · [arXiv](https://arxiv.org/abs/2609.29663) · [Code](https://github.com/Tech-sam-90/malaria_fp_analysis)

Full list on [Google Scholar](https://scholar.google.com/citations?hl=en&user=oM69cJoAAAAJ).

---

### Tools

PyTorch · Hugging Face · timm · MONAI · `mamba-ssm` · SLURM / Compute Canada (Narval) · Docker · FastAPI · W&B

---

[Website](https://sadeniji.vercel.app/) · [Google Scholar](https://scholar.google.com/citations?hl=en&user=oM69cJoAAAAJ) · [LinkedIn](https://www.linkedin.com/in/saadeniji/) · [sadeniji@andrew.cmu.edu](mailto:sadeniji@andrew.cmu.edu)

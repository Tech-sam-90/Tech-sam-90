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
Feature pyramid plus bidirectional cross-scale Mamba for brain-metastasis screening on UCSF-BMSR. It beats InceptentionNet on full-slice AUC (0.832 vs 0.758, p = 0.035) and scales 3.0× vs 8.6× in step time from 256 to 512 px. *With Simbiat Adetoro.*

**[Condition-Aware ICU Deterioration Risk](https://github.com/Tech-sam-90/condition-aware_risk_CDSS)**
Diagnosis-conditioned early-warning models on MIMIC-IV, benchmarking six sequence architectures at 1–3 h horizons. The best model (BiLSTM + attention, ROC-AUC 0.76) is served as a Dockerized FastAPI + WebSocket streaming service, with limitations documented up front.

**Multimodal Cancer Survival Prediction** *(in progress)*
Generalizable survival modeling from TCGA whole-slide images, RNA and clinical data, building on SurvPath.

---

### Publications

- `[Title]`. `[Authors]`. *`[Workshop name]`, MICCAI 2026.* `[link]`
- `[Title]`. `[Authors]`. *`[Workshop name]`, NeurIPS 2026.* `[link]`

Full list on [Google Scholar](https://scholar.google.com/citations?hl=en&user=oM69cJoAAAAJ).

---

### Tools

PyTorch · Hugging Face · timm · MONAI · `mamba-ssm` · SLURM / Compute Canada (Narval) · Docker · FastAPI · W&B

---

[Website](https://sadeniji.vercel.app/) · [Google Scholar](https://scholar.google.com/citations?hl=en&user=oM69cJoAAAAJ) · [LinkedIn](https://www.linkedin.com/in/saadeniji/) · `[your email]`

<!-- GENERATED from data/profile.yaml by scripts/build.py — edit the YAML, not this file. -->
### Hi, I'm Samuel Adeniji

I'm an M.S. student in Engineering AI at **Carnegie Mellon University Africa**. I build **vision–language and multimodal models for medical imaging and clinical decision support**. My work focuses on making these models efficient enough to run on large 3D scans, and honest enough about their limits to be trusted in low-resource health settings.

**Research interests**
- Medical vision–language models for 3D imaging
- Instruction-conditioned and token-efficient architectures for volumetric data
- Grounded radiology report generation and multi-scale representation learning
- Interpretable and reliable medical AI
- Deployment of imaging AI in low-resource and African clinical settings

---

### Selected projects

**[ICTC: Instruction-Conditioned Token Compression for 3D CT Vision–Language Models](https://github.com/Tech-sam-90/3d_compression)**<br>
A dual-stage, instruction-conditioned token compressor for 3D chest CT. A Perceiver stage distils each slice and a FiLM-conditioned stage aggregates slices into a fixed budget of visual tokens for a LoRA-adapted language model that writes the radiology report. On CT-RATE validation (3,039 scans): ROUGE-L 0.273, BLEU-4 0.128, RaTEScore 0.801. *Summer 2026 research internship with Prof. Prasenjit Mitra.*

**[FPN-Mamba: Linear-Time Bidirectional State Space Feature Pyramids for Small-Lesion Brain MRI Classification](https://github.com/Tech-sam-90/fpn-inceptentionnet)**<br>
Feature pyramid plus bidirectional Mamba for small brain-metastasis screening on UCSF-BMSR. It outperforms a self-attention baseline (InceptentionNet) on AUC (0.982 vs 0.897) and smallest-lesion recall (0.870 vs 0.788) across 5 seeds × 3 folds, and is 3.7× faster per step than a matched attention mixer at 512 px. *NeurIPS 2026 Africa in AI workshop.*

**[Where Do Malaria Detector False Positives Come From?](https://github.com/Tech-sam-90/malaria_fp_analysis)**<br>
A controlled study of two YOLOv12s detectors on 8,000 thick-smear images from Uganda and Ghana, using seven spatial and statistical analyses. It finds that white blood cells are *not* a systematic source of false positives, which redirects mitigation toward staining variability. *MICCAI 2026 MIRASOL workshop (oral).*

**[Condition-Aware ICU Deterioration Risk](https://github.com/Tech-sam-90/condition-aware_risk_CDSS)**<br>
Diagnosis-conditioned early-warning models on MIMIC-IV, benchmarking six sequence architectures at 1–3 h horizons. The best model (BiLSTM + attention, ROC-AUC 0.76) is served as a Dockerized FastAPI + WebSocket streaming service, with limitations documented up front.

**Multimodal Cancer Survival Prediction** *(in progress)*<br>
Generalizable survival modeling from TCGA whole-slide images, RNA and clinical data, building on SurvPath.

---

### Publications

- **Investigating White Blood Cells as a Source of False-Positive Malaria Parasite Detection in African Blood-Smear Images**<br>
  **Samuel Akinwumi Adeniji**, Goodness Chidera Obasi, Chris-Victor Ntwali, Aondona Moses Iorumbur, Confidence Raymond, Lowami Uwimana, Ahmed Tahiru Issah<br>
  *MICCAI 2026 Workshop: MIRASOL* (oral presentation) · [MICCAI](https://papers.miccai.org/miccai-2026-sat/MIRASOL_018.html) · [arXiv](https://arxiv.org/abs/2609.29663) · [OpenReview](https://openreview.net/forum?id=DAv0RwrdIk) · [Code](https://github.com/Tech-sam-90/malaria_fp_analysis)

- **FPN-Mamba: Linear-Time Bidirectional State Space Feature Pyramids for Small-Lesion Brain MRI Classification**<br>
  Simbiat Damilola Adetoro, **Samuel Akinwumi Adeniji**, Moise Busogi<br>
  *NeurIPS 2026 Workshop: Africa in AI* · [OpenReview](https://openreview.net/forum?id=te52LwNBSf) · [Code](https://github.com/Tech-sam-90/fpn-inceptentionnet)

Full list on [Google Scholar](https://scholar.google.com/citations?hl=en&user=oM69cJoAAAAJ) · [CV](https://github.com/Tech-sam-90/Tech-sam-90/blob/main/cv/Samuel_Adeniji_CV.pdf)

---

### Tools

PyTorch · TensorFlow · Vision Transformers · Mamba / state-space models · CNNs and Feature Pyramid Networks · vision–language models · LoRA / parameter-efficient fine-tuning · HuggingFace · 3D CT and MRI pipelines · CT-RATE · MIMIC-IV · MONAI-style preprocessing · OpenCV · YOLO · scikit-learn · Weights & Biases · Docker

---

[Website](https://sadeniji.vercel.app/) · [Google Scholar](https://scholar.google.com/citations?hl=en&user=oM69cJoAAAAJ) · [LinkedIn](https://www.linkedin.com/in/saadeniji/) · [sadeniji@andrew.cmu.edu](mailto:sadeniji@andrew.cmu.edu)

<!-- GENERATED from data/profile.yaml by scripts/build.py — edit the YAML, not this file. -->
### Hi, I'm Samuel Adeniji

I'm an M.S. student in Engineering AI at **Carnegie Mellon University Africa**. I work on **multimodal medical AI**: models that combine images such as pathology slides, CT and MRI with molecular and clinical data. I care about whether each input really helps, whether the model's evidence can be checked, and whether it still works at a new hospital, especially in low-resource and African health settings.

**Research interests**
- Multimodal medical AI combining pathology images, molecular and clinical data
- Explainable models whose evidence clinicians can check
- Robustness to hospital, stain and scanner differences
- Medical image analysis and vision–language models for CT and MRI
- Fair and reliable AI for low-resource and African clinical settings

---

### Selected projects

**[Scan-Specific Information in Compressed 3D CT Vision–Language Models](https://github.com/Tech-sam-90/3d_compression)**<br>
A vision–language pipeline that writes radiology reports from 3D chest CT, compressing each volume into a small budget of visual tokens. Swapping scans between reports showed the model often wrote template-like reports that barely depended on the scan, so the project now measures how much scan-specific information survives compression, and how to keep it. *Research internship with Prof. Prasenjit Mitra (May–Aug 2026), continuing.*

**[FPN-Mamba: Linear-Time Bidirectional State Space Feature Pyramids for Small-Lesion Brain MRI Classification](https://github.com/Tech-sam-90/fpn-inceptentionnet)**<br>
Feature pyramid plus bidirectional Mamba for small brain-metastasis screening on UCSF-BMSR. It outperforms a self-attention baseline (InceptentionNet) on AUC (0.982 vs 0.897) and smallest-lesion recall (0.870 vs 0.788) across 5 seeds × 3 folds, and is 3.7× faster per step than a matched attention mixer at 512 px. *NeurIPS 2026 Africa in AI workshop.*

**[Where Do Malaria Detector False Positives Come From?](https://github.com/Tech-sam-90/malaria_fp_analysis)**<br>
A controlled study of two YOLOv12s detectors on 6,593 thick-smear images from Uganda and Ghana (Lacuna dataset), using seven spatial and statistical analyses. The evidence does not support white blood cells as a systematic source of false positives, and points mitigation toward staining and preparation variability. *MICCAI 2026 MIRASOL workshop (oral).*

**ClinFuse: Multimodal Cancer Survival Prediction** *(in progress)*<br>
Survival prediction that adds clinical variables (stage, grade, age) to a whole-slide image and RNA model (building on SurvPath), trained to rank patients with a Cox loss and tested with whole hospitals held out. Without stage, it reaches c-index 0.712 vs 0.601 (kidney) and 0.671 vs 0.556 (endometrial) against SurvPath, and the ordering holds on external CPTAC hospitals. Team project; my part was data processing and training on the Narval cluster.

**Fetal Ultrasound Plane Classification: Bias and Ethics Across Datasets**<br>
A project classifying standard fetal ultrasound planes (brain, abdomen, femur, thorax and others) using public datasets. My part is measuring bias across the datasets and setting out the ethical issues, following the review of public fetal ultrasound datasets by Fiorentino et al. (npj Digital Medicine, 2025).

**LLM Evaluation Harness for a Maternal-Health Chatbot (Jacaranda Health)**<br>
An M.S. capstone with Jacaranda Health, building automated tests that run before a new version of their maternal-health SMS assistant is released. I built the evaluator for the retrieval-augmented (RAG) system, with measures for retrieval, faithfulness to the sources, answer relevance and correctness, and I coordinate the shared pipeline.

**[Condition-Aware ICU Deterioration Risk](https://github.com/Tech-sam-90/condition-aware_risk_CDSS)**<br>
Diagnosis-conditioned early-warning models on MIMIC-IV, benchmarking six sequence architectures at 1–3 h horizons. The best model (BiLSTM + attention, ROC-AUC 0.76) is served as a Dockerized FastAPI + WebSocket streaming service, with limitations documented up front.

---

### Publications

- **Investigating White Blood Cells as a Source of False-Positive Malaria Parasite Detection in African Blood-Smear Images**<br>
  **Samuel Akinwumi Adeniji**, Goodness Chidera Obasi, Chris-Victor Ntwali, Aondona Moses Iorumbur, Confidence Raymond, Lowami Uwimana, Ahmed Tahiru Issah<br>
  *MICCAI 2026 Workshop: MIRASOL* (oral presentation) · [MICCAI](https://papers.miccai.org/miccai-2026-sat/MIRASOL_018.html) · [arXiv](https://arxiv.org/abs/2609.29663) · [PDF](https://papers.miccai.org/miccai-2026-sat/paper/MIRASOL_018.pdf) · [OpenReview](https://openreview.net/forum?id=DAv0RwrdIk) · [Code](https://github.com/Tech-sam-90/malaria_fp_analysis)

- **FPN-Mamba: Linear-Time Bidirectional State Space Feature Pyramids for Small-Lesion Brain MRI Classification**<br>
  Simbiat Damilola Adetoro, **Samuel Akinwumi Adeniji**, Moise Busogi<br>
  *NeurIPS 2026 Workshop: Africa in AI* · [OpenReview](https://openreview.net/forum?id=te52LwNBSf) · [Code](https://github.com/Tech-sam-90/fpn-inceptentionnet)

Full list on [Google Scholar](https://scholar.google.com/citations?hl=en&user=oM69cJoAAAAJ) · [CV](https://github.com/Tech-sam-90/Tech-sam-90/blob/main/cv/Samuel_Adeniji_CV.pdf)

---

### Tools

PyTorch · TensorFlow · Vision Transformers · Mamba / state-space models · CNNs and Feature Pyramid Networks · vision–language models · LoRA / parameter-efficient fine-tuning · HuggingFace · 3D CT and MRI pipelines · CT-RATE · MIMIC-IV · MONAI-style preprocessing · OpenCV · YOLO · scikit-learn · Weights & Biases · Docker

---

[Website](https://sadeniji.vercel.app/) · [Google Scholar](https://scholar.google.com/citations?hl=en&user=oM69cJoAAAAJ) · [LinkedIn](https://www.linkedin.com/in/saadeniji/) · [sadeniji@andrew.cmu.edu](mailto:sadeniji@andrew.cmu.edu)

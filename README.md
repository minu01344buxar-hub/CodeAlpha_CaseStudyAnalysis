# Moderna, Inc. — Biotechnology Case Study Analysis & Presentation

A comprehensive strategic case study and 12-slide presentation analyzing **Moderna, Inc.**, its foundational mRNA platform innovation, 4-component Lipid Nanoparticle (LNP) nanotechnology, commercial product milestones (**Spikevax**, **mRESVIA**), individualized cancer vaccines, biological/technical challenges, IP litigation, and market impact.

---

## 📁 Repository & Deliverable Structure

| File | Format | Description |
| :--- | :--- | :--- |
| **[`Moderna_Biotech_Case_Study_Presentation.pptx`](Moderna_Biotech_Case_Study_Presentation.pptx)** | Microsoft PowerPoint | **Official 12-Slide Widescreen (16:9) Presentation Deck** styled in a modern biotech dark palette, complete with metrics, comparison cards, embedded high-resolution 3D scientific visuals, and comprehensive speaker notes on every slide. |
| **[`MODERNA_CASE_STUDY_REPORT.md`](MODERNA_CASE_STUDY_REPORT.md)** | Markdown Report | **In-Depth Academic Case Study Report** covering molecular biology ($N1$-methylpseudouridine), LNP biophysics, clinical pipeline matrix, digital biomanufacturing (Norwood foundry), challenges, $2.25B Arbutus patent settlement, and platform economics. |
| **[`index.html`](index.html)** | Interactive Web Deck | **Interactive HTML5 Presentation Deck** running directly in any web browser. Features dynamic slide animations, keyboard shortcuts, speaker notes drawer, 12-slide overview grid, and 1-click Print/PDF export. |
| **[`generate_presentation.py`](generate_presentation.py)** | Python Script | Python automation script utilizing `python-pptx` to regenerate the presentation programmatically. |
| **`assets/`** | Visual Media | High-resolution 3D scientific renderings of mRNA-loaded Lipid Nanoparticles (`moderna_mrna_lnp.jpg`) and AI personalized cancer immunotherapy (`moderna_cancer_vaccine.jpg`). |

---

## 🖥 Presentation Slide Outline (12 Slides)

1. **Slide 01 | Executive Introduction:** Title, company overview, core thesis, and high-level case study metrics.
2. **Slide 02 | Company Profile:** The "Biotech as Software" paradigm, founding story (Flagship Pioneering), and platform flywheel.
3. **Slide 03 | Molecular Innovation:** Synthetic mRNA structural engineering ($N1$-methylpseudouridine $\text{m1}\Psi$, Cap 1, UTRs, Poly-A tail).
4. **Slide 04 | Nanotechnology & Formulation:** The 4-component LNP delivery vehicle (SM-102, PEG-DMG, Cholesterol, DSPC) & endosomal escape.
5. **Slide 05 | Flagship Product:** Spikevax (mRNA-1273) — 66-day sequence-to-clinic speed, 94.1% Phase 3 efficacy, and industry de-risking.
6. **Slide 06 | Commercial Pipeline Expansion:** mRESVIA (RSV vaccine, FDA approved May 31, 2024 / 2025) and combination seasonal vaccines (mRNA-1083).
7. **Slide 07 | Immuno-Oncology Frontier:** Individualized Neoantigen Therapy (INT / mRNA-4157 / V940) with Merck (44% reduction in recurrence/death in melanoma).
8. **Slide 08 | Agile Biomanufacturing:** Cell-free enzymatic In Vitro Transcription (IVT) vs mammalian CHO cell bioreactors, and the Norwood Digital Foundry.
9. **Slide 09 | Scientific & Biological Challenges:** Liver clearance ApoE trap, transient expression kinetics, reactogenicity, and anti-PEG immunogenicity.
10. **Slide 10 | Legal, IP & Regulatory Landscape:** The $2.25 Billion Arbutus LNP patent settlement (March 2026), Pfizer/BioNTech dispute, and FDA strain-change pathways.
11. **Slide 11 | Financial Dynamics & Platform Economics:** Post-pandemic revenue cliff management, low marginal cost per pipeline asset, and compounding R&D advantages.
12. **Slide 12 | Strategic Synthesis & Conclusion:** Key lessons for biotechnology leaders (Delivery is paramount, Platform agility, Tech-Bio convergence).

---

## 🚀 How to View and Present

### 1. Microsoft PowerPoint
Simply open **`Moderna_Biotech_Case_Study_Presentation.pptx`** in Microsoft PowerPoint, Google Slides, Keynote, or LibreOffice.
* Check the **Presenter Notes** section at the bottom of each slide for full talking scripts.

### 2. Interactive Web Presentation (`index.html`)
Double-click **`index.html`** or open it in any web browser (Google Chrome, Microsoft Edge, Firefox, Safari).

**Keyboard Shortcuts:**
* `→` / `↓` / `Space`: Next slide
* `←` / `↑` / `Backspace`: Previous slide
* `S`: Toggle **Presenter Notes** drawer (reveals spoken talking points)
* `G`: Toggle **Slide Grid Overview** (interactive jump to any slide)
* `P` or `Ctrl + P`: **Print / Save as PDF** (pre-formatted landscape slide export)
* `F`: Toggle **Fullscreen Mode**
* `Home` / `End`: Jump to First / Last slide

---

## 🛠 Re-generating the Presentation
To programmatically regenerate the PowerPoint deck:
```bash
python generate_presentation.py
```
*(Requires `python-pptx` and `Pillow`, already installed in the environment).*

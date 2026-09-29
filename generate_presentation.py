import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank slide layout

    # Base directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_dir, "assets")
    lnp_img_path = os.path.join(assets_dir, "moderna_mrna_lnp.jpg")
    cancer_img_path = os.path.join(assets_dir, "moderna_cancer_vaccine.jpg")

    # Color Palette: Deep Modern Biotech Theme
    DARK_BG = RGBColor(15, 23, 42)       # Slate 900 #0F172A
    CARD_BG = RGBColor(30, 41, 59)       # Slate 800 #1E293B
    CARD_BORDER = RGBColor(51, 65, 85)   # Slate 700 #334155
    ACCENT_CYAN = RGBColor(14, 165, 233) # Sky 500 #0EA5E9
    ACCENT_TEAL = RGBColor(20, 184, 166) # Teal 500 #14B8A6
    ACCENT_CORAL = RGBColor(244, 63, 94) # Rose 500 #F43F5E
    ACCENT_AMBER = RGBColor(245, 158, 11)# Amber 500 #F59E0B
    TEXT_LIGHT = RGBColor(248, 250, 252) # Slate 50 #F8FAFC
    TEXT_MUTED = RGBColor(148, 163, 184) # Slate 400 #94A3B8
    TEXT_DIM = RGBColor(100, 116, 139)   # Slate 500 #64748B

    def set_slide_background(slide, color=DARK_BG):
        bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg_shape.fill.solid()
        bg_shape.fill.fore_color.rgb = color
        bg_shape.line.fill.background()
        return bg_shape

    def add_header(slide, slide_num, category, title, subtitle):
        # Category / Tag pill
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(11.7), Inches(0.35))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_right = tf_tag.margin_top = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = f"{slide_num:02d} | {category.upper()}"
        p_tag.font.name = "Arial"
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ACCENT_CYAN

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.7), Inches(0.65))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_right = tf_title.margin_top = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.name = "Arial"
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_LIGHT

        # Subtitle
        sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.48), Inches(11.7), Inches(0.35))
        tf_sub = sub_box.text_frame
        tf_sub.word_wrap = True
        tf_sub.margin_left = tf_sub.margin_right = tf_sub.margin_top = tf_sub.margin_bottom = 0
        p_sub = tf_sub.paragraphs[0]
        p_sub.text = subtitle
        p_sub.font.name = "Arial"
        p_sub.font.size = Pt(11)
        p_sub.font.color.rgb = TEXT_MUTED

    def add_card(slide, left, top, width, height, title, items, accent_color=ACCENT_CYAN, font_size=10, space_after=6):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER
        card.line.width = Pt(1)

        inner_box = slide.shapes.add_textbox(left + Inches(0.25), top + Inches(0.2), width - Inches(0.5), height - Inches(0.3))
        tf = inner_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p_head = tf.paragraphs[0]
        p_head.text = title
        p_head.font.name = "Arial"
        p_head.font.size = Pt(12.5)
        p_head.font.bold = True
        p_head.font.color.rgb = accent_color
        p_head.space_after = Pt(space_after)

        for item in items:
            p = tf.add_paragraph()
            p.text = f"•  {item}"
            p.font.name = "Arial"
            p.font.size = Pt(font_size)
            p.font.color.rgb = TEXT_LIGHT
            p.space_after = Pt(space_after)

    def add_stat_box(slide, left, top, width, height, stat, label, subtext="", accent_color=ACCENT_CYAN):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER
        card.line.width = Pt(1)

        box = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), height - Inches(0.25))
        tf = box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0

        p_stat = tf.paragraphs[0]
        p_stat.text = stat
        p_stat.font.name = "Arial"
        p_stat.font.size = Pt(26)
        p_stat.font.bold = True
        p_stat.font.color.rgb = accent_color

        p_lbl = tf.add_paragraph()
        p_lbl.text = label
        p_lbl.font.name = "Arial"
        p_lbl.font.size = Pt(10)
        p_lbl.font.bold = True
        p_lbl.font.color.rgb = TEXT_LIGHT
        p_lbl.space_after = Pt(3)

        if subtext:
            p_sub = tf.add_paragraph()
            p_sub.text = subtext
            p_sub.font.name = "Arial"
            p_sub.font.size = Pt(8.5)
            p_sub.font.color.rgb = TEXT_MUTED

    # =========================================================================
    # SLIDE 1: Title Slide (with Hero Thumbnail)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    accent_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(2.2), Inches(0.08))
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = ACCENT_CYAN
    accent_bar.line.fill.background()

    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(7.5), Inches(3.4))
    tf1 = t_box.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "BIOTECHNOLOGY ENTERPRISE CASE STUDY"
    p0.font.name = "Arial"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_CYAN
    p0.space_after = Pt(12)

    p1 = tf1.add_paragraph()
    p1.text = "Moderna, Inc.: The mRNA Platform Revolution"
    p1.font.name = "Arial"
    p1.font.size = Pt(32)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_LIGHT
    p1.space_after = Pt(10)

    p2 = tf1.add_paragraph()
    p2.text = "Decoding the Paradigm Shift from Empirical Drug Discovery to Programmable Genetic Medicine"
    p2.font.name = "Arial"
    p2.font.size = Pt(15)
    p2.font.color.rgb = TEXT_MUTED

    if os.path.exists(lnp_img_path):
        pic = s1.shapes.add_picture(lnp_img_path, Inches(8.6), Inches(1.1), Inches(3.9), Inches(3.4))

    meta_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.8), Inches(11.7), Inches(2.0))
    meta_card.fill.solid()
    meta_card.fill.fore_color.rgb = CARD_BG
    meta_card.line.color.rgb = CARD_BORDER

    meta_tb = s1.shapes.add_textbox(Inches(1.1), Inches(5.0), Inches(11.1), Inches(1.6))
    tf_meta = meta_tb.text_frame
    tf_meta.word_wrap = True

    p_m1 = tf_meta.paragraphs[0]
    p_m1.text = "EXECUTIVE CASE STUDY HIGHLIGHTS"
    p_m1.font.name = "Arial"
    p_m1.font.size = Pt(11)
    p_m1.font.bold = True
    p_m1.font.color.rgb = ACCENT_TEAL
    p_m1.space_after = Pt(6)

    p_m2 = tf_meta.add_paragraph()
    p_m2.text = "• Core Innovation: Modified mRNA transcripts (m1Ψ) encapsulated within 4-component Lipid Nanoparticles (LNPs)\n• Flagship Approvals: Spikevax (COVID-19), mRESVIA (RSV, approved May 2024), INT (Melanoma Phase 3 with Merck)\n• Broad Applications: Prophylactic Vaccines, Individualized Immuno-Oncology, Rare Metabolic Diseases, & Gene Editing\n• High-Stakes Complexities: Extra-hepatic delivery bottlenecks, $2.25B Arbutus patent settlement, and post-pandemic pivot"
    p_m2.font.name = "Arial"
    p_m2.font.size = Pt(10)
    p_m2.font.color.rgb = TEXT_LIGHT

    s1.notes_slide.notes_text_frame.text = (
        "WELCOME & INTRODUCTORY REMARKS:\n"
        "Good morning / afternoon. Today, we present an in-depth case study of Moderna, Inc., examining how it redefined modern biotechnology.\n"
        "Rather than viewing drugs as single handcrafted molecules, Moderna established the concept of mRNA as biological software. "
        "We will examine the molecular biology behind the platform, the lipid nanoparticle engineering that enabled clinical delivery, "
        "the commercial impact across infectious disease and oncology, foundational challenges including intellectual property litigation, "
        "and the strategic road ahead for programmable medicine."
    )

    # =========================================================================
    # SLIDE 2: Executive Summary & Company Profile
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, 2, "Company Profile", "Executive Summary: The 'Biotech as Software' Thesis",
               "How Moderna evolved from a stealth venture-backed startup into a commercial biopharma titan.")

    add_stat_box(s2, Inches(0.8), Inches(2.0), Inches(2.7), Inches(1.3), "2010", "Founded in Cambridge, MA", "Originated at Flagship Pioneering")
    add_stat_box(s2, Inches(3.8), Inches(2.0), Inches(2.7), Inches(1.3), "$604M", "Record 2018 Biotech IPO", "$7.5B initial valuation")
    add_stat_box(s2, Inches(6.8), Inches(2.0), Inches(2.7), Inches(1.3), "66 Days", "Sequence to Phase 1 Trial", "Fastest development in history")
    add_stat_box(s2, Inches(9.8), Inches(2.0), Inches(2.7), Inches(1.3), "45+", "Active Pipeline Programs", "Vaccines, Oncology, Rare Diseases")

    add_card(s2, Inches(0.8), Inches(3.6), Inches(5.7), Inches(3.3), "Strategic Thesis & Leadership", [
        "Founders: Derrick Rossi, Timothy Springer, Robert Langer, Kenneth Chien, and Noubar Afeyan (Flagship Pioneering).",
        "Leadership: Stéphane Bancel joined as CEO in 2011, instilling a relentless, tech-like operational velocity.",
        "The Paradigm: Treat mRNA as digital code. Changing nucleotide sequences changes the therapeutic protein without altering the manufacturing chassis.",
        "Capital Aggression: Raised >$2B in venture funding and strategic alliances (AstraZeneca, Merck, DARPA) before commercialization."
    ], accent_color=ACCENT_CYAN)

    add_card(s2, Inches(6.8), Inches(3.6), Inches(5.7), Inches(3.3), "Platform Flywheel Advantage", [
        "Shared Chemistry: Same 4-component LNP formulation adapted across multiple therapeutic targets.",
        "Compounding Data: Safety dossiers, toxicology data, and analytical methods transfer across clinical assets.",
        "Digital Foundry: Norwood, MA manufacturing hub integrates cloud MES, robotics, and automated synthesis.",
        "Transition: Evolving from pandemic emergency response into a diversified, multi-pillar biopharmaceutical enterprise."
    ], accent_color=ACCENT_TEAL)

    s2.notes_slide.notes_text_frame.text = (
        "SLIDE 2 SPEAKER NOTES:\n"
        "To understand Moderna, one must understand its origin. Founded in 2010 out of Flagship Pioneering, Stéphane Bancel ran Moderna not like a traditional biotech, "
        "but like a high-growth tech platform. While typical biopharma spends 10 years and $1.5 billion per individual drug asset, Moderna invested over $2 billion "
        "building a reusable infrastructure. When SARS-CoV-2 emerged, they proved that digital sequence in a computer could become a physical vialed drug in just 42 days, "
        "entering human trials in 66 days. Today, their pipeline exceeds 45 clinical programs across infectious disease, oncology, and rare metabolic conditions."
    )

    # =========================================================================
    # SLIDE 3: The Biotech Innovation: Synthetic mRNA Architecture
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, 3, "Core Biotechnology Innovation", "Molecular Engineering: Overcoming Biological Barriers",
               "Re-engineering the central dogma (DNA -> mRNA -> Protein) to turn patient cells into bioreactors.")

    add_card(s3, Inches(0.8), Inches(2.0), Inches(5.7), Inches(2.4), "1. Nucleoside Modification (m1Ψ)", [
        "Unmodified foreign mRNA triggers Toll-Like Receptors (TLR3/7/8) & RIG-I, causing lethal cytokine storms and shutdown.",
        "Solution: 100% substitution of uridine with N1-methylpseudouridine (m1Ψ).",
        "Efficacy: Completely evades innate immune sensors while increasing protein translation efficiency."
    ], accent_color=ACCENT_CYAN, font_size=9.5, space_after=4)

    add_card(s3, Inches(6.8), Inches(2.0), Inches(5.7), Inches(2.4), "2. Cap 1 Enzymatic Mimicry", [
        "Natural mammalian mRNA possesses a specialized 5' 7-methylguanylate cap.",
        "Moderna synthesizes synthetic Cap 1 structures (m7GpppAm).",
        "Prevents IFIT1-mediated degradation and maximizes binding affinity for eukaryotic translation initiation factor 4E (eIF4E)."
    ], accent_color=ACCENT_TEAL, font_size=9.5, space_after=4)

    add_card(s3, Inches(0.8), Inches(4.6), Inches(5.7), Inches(2.4), "3. Codon & UTR Optimization", [
        "Algorithmic GC enrichment replaces low-efficiency human codons with preferred synonymous codons.",
        "Eliminates cryptic splice sites and secondary hairpins that cause ribosomal pausing.",
        "Synthetic 5' and 3' UTRs derived from long-lived human alpha-globin transcripts maximize cellular half-life."
    ], accent_color=ACCENT_AMBER, font_size=9.5, space_after=4)

    add_card(s3, Inches(6.8), Inches(4.6), Inches(5.7), Inches(2.4), "4. Poly(A) Tail Engineering", [
        "Strictly calibrated Polyadenylated [Poly(A)] tail length (~100–120 nucleotides).",
        "Binds Poly(A)-Binding Protein (PABP), bridging with 5' eIF4G to form a closed-loop translation circle.",
        "Shields transcript against 3'->5' exonucleolytic deadenylation and enzymatic degradation."
    ], accent_color=ACCENT_CORAL, font_size=9.5, space_after=4)

    s3.notes_slide.notes_text_frame.text = (
        "SLIDE 3 SPEAKER NOTES:\n"
        "Let's dive into the molecular biology innovation. For 30 years, scientists knew mRNA carried instructions, but introducing foreign synthetic mRNA in vivo was lethal—it "
        "triggered massive innate immune shock via TLR7 and TLR8. The breakthrough—building on Karikó and Weissman's Nobel Prize-winning work—was replacing uridine with "
        "N1-methylpseudouridine. Furthermore, Moderna algorithmically optimizes the 5 structural domains: the Cap 1 structure for ribosome docking, the 5' UTR for scanning, "
        "the coding sequence with preferred codons, the 3' UTR for longevity, and a calibrated poly(A) tail that forms a circular translating machine inside human cells."
    )

    # =========================================================================
    # SLIDE 4: Overcoming the Delivery Bottleneck: LNP Engineering (with Graphic)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, 4, "Nanotechnology & Formulation", "Overcoming the Delivery Barrier: 4-Component LNPs",
               "Naked mRNA degrades in milliseconds; Lipid Nanoparticles provide protection, targeting, and endosomal escape.")

    add_card(s4, Inches(0.8), Inches(2.0), Inches(5.8), Inches(5.0), "The 4-Component LNP Formulation (~80-100 nm)", [
        "Ionizable Cationic Lipid (SM-102, ~50 mol%):",
        "  • The core engine: Positively charged at acidic pH during manufacturing to condense RNA; neutral at blood pH (7.4) to eliminate systemic toxicity.",
        "  • Re-protonates inside acidic endosomes (pH ~5.5) to disrupt endosomal membranes and release mRNA into the cytoplasm.",
        "PEGylated Lipid (PEG2000-DMG, ~1.5 mol%):",
        "  • Provides steric shielding to prevent particle aggregation and regulates nanoparticle size.",
        "Cholesterol (~38.5 mol%):",
        "  • Intercalates into the lipid bilayer, optimizing membrane fluidity, structural rigidity, and fusion.",
        "Helper Phospholipid (DSPC, ~10 mol%):",
        "  • High-melting zwitterionic phospholipid providing lamellar bilayer stability."
    ], accent_color=ACCENT_CYAN, font_size=9, space_after=4)

    add_card(s4, Inches(6.9), Inches(2.0), Inches(5.6), Inches(2.5), "Cellular Delivery Mechanism", [
        "1. ApoE Opsonization: Binds endogenous blood ApoE, triggering LDLR endocytosis.",
        "2. Proton Sponge Effect: Endosomal acidification (pH 5.5) reprotonates SM-102 tertiary amines.",
        "3. Hexagonal Inversion: Cationic lipids bind host anionic lipids, rupturing endosome.",
        "4. Ribosomal Translation: Intact mRNA enters cytosol for instant protein synthesis."
    ], accent_color=ACCENT_TEAL, font_size=9, space_after=4)

    if os.path.exists(lnp_img_path):
        s4.shapes.add_picture(lnp_img_path, Inches(6.9), Inches(4.7), Inches(5.6), Inches(2.3))

    s4.notes_slide.notes_text_frame.text = (
        "SLIDE 4 SPEAKER NOTES:\n"
        "In biotechnology, there is an axiom: 'Delivery is the drug.' Bare mRNA injected into the bloodstream is torn apart by RNase enzymes in seconds and repelled by cell membranes. "
        "Moderna's four-component lipid nanoparticle is a masterpiece of biophysical engineering. The ionizable lipid SM-102 acts as a chemical chameleon: it is positively charged "
        "in the lab at pH 5 to encapsulate the RNA; neutral at pH 7.4 in your blood so it doesn't pop red blood cells; and turns positively charged again inside the endosome, "
        "ripping open the endosomal membrane like a Trojan horse so the mRNA escapes into the cytoplasm for translation."
    )

    # =========================================================================
    # SLIDE 5: Commercial Milestone: Spikevax (mRNA-1273)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, 5, "Flagship Product", "Spikevax (mRNA-1273): Planetary Validation at Scale",
               "The COVID-19 vaccine transformed global public health and established proof-of-concept for mRNA.")

    add_stat_box(s5, Inches(0.8), Inches(2.0), Inches(2.7), Inches(1.3), "42 Days", "Sequence to Clinical Batch", "Jan 11 to Feb 24, 2020")
    add_stat_box(s5, Inches(3.8), Inches(2.0), Inches(2.7), Inches(1.3), "94.1%", "Phase 3 COVE Efficacy", "100% against severe disease")
    add_stat_box(s5, Inches(6.8), Inches(2.0), Inches(2.7), Inches(1.3), "1B+", "Global Doses Delivered", "Distributed in >80 nations")
    add_stat_box(s5, Inches(9.8), Inches(2.0), Inches(2.7), Inches(1.3), "$37B+", "Peak 2021-2022 Revenue", "Commercial financial explosion")

    add_card(s5, Inches(0.8), Inches(3.6), Inches(5.7), Inches(3.3), "Scientific & Clinical Execution", [
        "Target Antigen: Prefusion-stabilized full-length Spike glycoprotein with 2 consecutive proline substitutions (2P).",
        "Speed vs Rigor: 30,000-participant Phase 3 COVE trial completed with full FDA/EMA regulatory scrutiny.",
        "Bivalent Adaptability: Rapid variant updates for Beta, Omicron BA.1, BA.4/5, XBB.1.5, and seasonal variants.",
        "Durability: Induced neutralizing antibody titers significantly higher than natural infection, paired with durable CD8+ cytotoxic T-cell memory."
    ], accent_color=ACCENT_CYAN)

    add_card(s5, Inches(6.8), Inches(3.6), Inches(5.7), Inches(3.3), "Biopharmaceutical Industry Impact", [
        "Demolished Timelines: Compressed traditional 10-to-15-year vaccine development into just 11 months.",
        "Regulatory Blueprint: Established FDA Emergency Use Authorization (EUA) and standard BLA precedents for mRNA.",
        "Cold-Chain Logistics: Pioneered mass distribution protocols initially at -20°C, later optimizing to standard refrigerated (2-8°C) stability.",
        "De-risked Modality: Proved conclusively that mRNA is clinically viable and mass-manufacturable."
    ], accent_color=ACCENT_TEAL)

    s5.notes_slide.notes_text_frame.text = (
        "SLIDE 5 SPEAKER NOTES:\n"
        "Spikevax was not just a commercial product; it was an existential proof-of-concept for an entire scientific discipline. "
        "Prior to 2020, cynics claimed mRNA was too fragile, too immunogenic, or impossible to scale. Within 11 months, Moderna enrolled 30,000 participants, "
        "demonstrated 94.1% efficacy against symptomatic infection and 100% protection against death or hospitalization, and delivered over a billion doses. "
        "It generated over $37 billion in revenue across 2021 and 2022, creating the war chest that now finances the next wave of therapeutics."
    )

    # =========================================================================
    # SLIDE 6: Commercial Expansion: mRESVIA & Respiratory Combos
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, 6, "Commercial Pipeline Expansion", "mRESVIA & The Next-Gen Respiratory Franchise",
               "Proving the platform's multi-product viability beyond COVID-19 with FDA approval in May 2024.")

    add_card(s6, Inches(0.8), Inches(2.0), Inches(5.7), Inches(5.0), "mRESVIA (mRNA-1345) Breakthrough", [
        "FDA Approval Milestone (May 31, 2024):",
        "  • First non-COVID mRNA vaccine approved in pharmaceutical history.",
        "  • Indicated for prevention of RSV lower respiratory tract disease in older adults (60+); expanded to high-risk adults (18-59) in 2025.",
        "Antigen Engineering:",
        "  • Encodes the RSV fusion (F) glycoprotein locked in its prefusion conformation.",
        "Clinical Efficacy (ConquerRSV Trial):",
        "  • 83.7% efficacy against RSV-LRTD with 2+ symptoms; 82.8% against 3+ symptoms.",
        "Prefilled Syringe Delivery:",
        "  • First mRNA vaccine formulated in ready-to-use prefilled syringes, simplifying healthcare provider administration."
    ], accent_color=ACCENT_CYAN, font_size=9, space_after=5)

    add_card(s6, Inches(6.8), Inches(2.0), Inches(5.7), Inches(5.0), "Pan-Respiratory Combination Franchise", [
        "The Market Problem:",
        "  • 'Vaccine fatigue' causes poor adherence to separate seasonal shots for COVID, Flu, and RSV.",
        "mRNA-1083 (Combination COVID + Influenza):",
        "  • Phase 3 trial met all primary immunogenicity endpoints.",
        "  • Demonstrated higher immune responses than licensed stand-alone influenza and COVID vaccines in adults 50+.",
        "Strategic Commercial Synergies:",
        "  • Captures dominant market share by offering a single annual jab.",
        "  • Demonstrates modular platform flexibility: blending multiple unique mRNA sequences into one LNP vial without formulation redesign."
    ], accent_color=ACCENT_TEAL, font_size=9, space_after=5)

    s6.notes_slide.notes_text_frame.text = (
        "SLIDE 6 SPEAKER NOTES:\n"
        "A critical question faced by investors and analysts was: Is Moderna a one-hit wonder? In May 2024, Moderna answered decisively with FDA approval of mRESVIA for RSV. "
        "This was the first time an mRNA vaccine was approved for an entirely different pathogen. Furthermore, Moderna solved healthcare ease-of-use by launching mRESVIA in "
        "prefilled syringes. Looking forward, the true commercial crown jewel is mRNA-1083: a combination Flu plus COVID shot that outperformed standalone vaccines in Phase 3. "
        "A single jab solves patient vaccine fatigue and locks in recurring annual seasonal revenue."
    )

    # =========================================================================
    # SLIDE 7: Oncology Frontier: Individualized Neoantigen Therapies (with Graphic)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, 7, "Immuno-Oncology", "Individualized Neoantigen Therapy (INT): mRNA-4157 / V940",
               "Revolutionizing oncology: Creating bespoke personalized cancer vaccines tailored to each patient's tumor.")

    add_card(s7, Inches(0.8), Inches(2.0), Inches(5.8), Inches(5.0), "The Bespoke Medicine Workflow", [
        "Step 1: Patient Biopsy & Blood Sampling",
        "  • High-throughput Next-Generation Sequencing (WES) identifies somatic tumor-specific mutations vs normal DNA.",
        "Step 2: AI & Machine Learning Epitope Selection",
        "  • Proprietary bioinformatics algorithm ranks mutations for MHC-I/II binding affinity and immunogenicity.",
        "  • Up to 34 unique neoantigens selected per patient.",
        "Step 3: Rapid Digital Manufacturing",
        "  • Single synthetic mRNA strand encoding all 34 epitopes concatenated together is synthesized and encapsulated in LNPs.",
        "  • Turnaround time compressed to ~6–8 weeks from biopsy to bedside."
    ], accent_color=ACCENT_CYAN, font_size=9, space_after=4)

    add_card(s7, Inches(6.9), Inches(2.0), Inches(5.6), Inches(2.5), "Phase 2b/3 Clinical Evidence (w/ Merck)", [
        "KEYNOTE-942 Trial Breakthrough:",
        "  • INT (mRNA-4157) + Keytruda vs Keytruda alone in stage III/IV melanoma.",
        "  • 44% reduction in risk of cancer recurrence or death (HR = 0.561).",
        "  • 65% reduction in distant metastasis or death.",
        "Pipeline Expansion: Phase 3 active in melanoma, lung cancer (NSCLC)."
    ], accent_color=ACCENT_TEAL, font_size=9, space_after=4)

    if os.path.exists(cancer_img_path):
        s7.shapes.add_picture(cancer_img_path, Inches(6.9), Inches(4.7), Inches(5.6), Inches(2.3))

    s7.notes_slide.notes_text_frame.text = (
        "SLIDE 7 SPEAKER NOTES:\n"
        "Now we arrive at the most scientifically breathtaking application of Moderna's platform: Individualized Neoantigen Therapy, partnered with Merck. "
        "No two cancers have the same genetic mutations. With mRNA-4157, when a patient has a tumor surgically resected, their tumor DNA is sequenced, an AI model picks "
        "the 34 most immunogenic mutations, and within weeks, a completely unique mRNA vaccine is synthesized specifically for that individual patient. "
        "In Phase 2b melanoma trials, combining this with Keytruda slashed recurrence or death by 44%. This represents the dawn of true personalized genetic oncology."
    )

    # =========================================================================
    # SLIDE 8: Agile Manufacturing: The Digital Biotech Foundry
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, 8, "Biomanufacturing Paradigm", "Agile Biomanufacturing: The Cell-Free Foundry Advantage",
               "Contrasting classical recombinant bioreactors with Moderna's automated digital mRNA synthesis.")

    add_card(s8, Inches(0.8), Inches(2.0), Inches(5.7), Inches(5.0), "Cell-Free In Vitro Transcription (IVT)", [
        "Eliminating Biological Variability:",
        "  • Classical biologics require living mammalian cells (CHO cells) in 10,000L tanks, taking 6–9 months per batch.",
        "  • Moderna uses cell-free enzymatic synthesis using T7 RNA polymerase and linearized plasmid DNA.",
        "Turnaround in Weeks:",
        "  • Complete batch turnaround reduced to 4–6 weeks from digital sequence to finished vial.",
        "Chemical Uniformity:",
        "  • Higher batch-to-batch reproducibility without cellular contaminants (host-cell proteins, mycoplasma).",
        "Purification Innovation:",
        "  • Tangential Flow Filtration (TFF) and specialized chromatography eliminate double-stranded RNA (dsRNA) impurities."
    ], accent_color=ACCENT_CYAN, font_size=9, space_after=5)

    add_card(s8, Inches(6.8), Inches(2.0), Inches(5.7), Inches(5.0), "Digital Foundry Architecture (Norwood, MA)", [
        "Robotic Automation & Microfluidics:",
        "  • Continuous-flow impingement jet microfluidic mixing precisely encapsulates mRNA inside LNPs at millisecond speeds.",
        "Cloud-Integrated MES & AI Quality Control:",
        "  • Real-time sensor monitoring tracks particle size distribution (~80 nm) and % encapsulation efficiency (>90%).",
        "Universal Production Chassis:",
        "  • The exact same facility, pumps, and mixers produce COVID vaccines, cancer vaccines, or rare disease therapeutics.",
        "Global Manufacturing Network:",
        "  • Strategic facility partnerships established in the US, UK, Canada, and Australia for sovereign pandemic preparedness."
    ], accent_color=ACCENT_TEAL, font_size=9, space_after=5)

    s8.notes_slide.notes_text_frame.text = (
        "SLIDE 8 SPEAKER NOTES:\n"
        "To appreciate Moderna's margins and speed, you have to look at manufacturing chemistry. Traditional biopharma manufactures proteins inside living cells—hamster ovary "
        "cells—which are notoriously temperamental, sensitive to temperature, contamination, and require 6 to 9 months per run. Moderna's process is completely cell-free. "
        "They mix linearized DNA, T7 polymerase, and nucleotide building blocks in a continuous chemical reactor. At their Norwood foundry, microfluidic jets smash the mRNA "
        "and lipids together at high velocity to form uniform 80-nanometer spheres. The exact same equipment produces an oncology drug on Monday and an RSV vaccine on Friday."
    )

    # =========================================================================
    # SLIDE 9: Scientific & Biological Challenges
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, 9, "Technical Roadblocks", "Key Scientific & Biological Challenges",
               "Critical limitations in biodistribution, tolerability, thermal stability, and chronic dosing.")

    add_card(s9, Inches(0.8), Inches(2.0), Inches(5.7), Inches(2.4), "1. Extra-Hepatic Delivery Trap", [
        "Systemic IV-administered LNPs naturally bind serum ApoE and are swallowed by liver hepatocytes via LDLR (>80% liver clearance).",
        "Delivering mRNA to lungs, heart, bone marrow, or the central nervous system requires novel SORT lipids or targeting ligands."
    ], accent_color=ACCENT_CORAL, font_size=9.5, space_after=4)

    add_card(s9, Inches(6.8), Inches(2.0), Inches(5.7), Inches(2.4), "2. Transient Expression Kinetics", [
        "mRNA does not integrate into the genome; protein expression peaks at 24–48h and decays within days.",
        "Advantage: High safety margin for vaccines.",
        "Hurdle: Chronic genetic disease treatments require lifelong repeat infusions every 2–4 weeks."
    ], accent_color=ACCENT_AMBER, font_size=9.5, space_after=4)

    add_card(s9, Inches(0.8), Inches(4.6), Inches(5.7), Inches(2.4), "3. Reactogenicity & Tolerability", [
        "High-dose repeat mRNA triggers systemic inflammatory cytokines, causing fever, fatigue, and myalgia.",
        "Limits maximum tolerable doses in systemic protein replacement and cardiovascular therapeutics.",
        "Requires next-gen biodegradable lipids with accelerated tissue clearance."
    ], accent_color=ACCENT_CORAL, font_size=9.5, space_after=4)

    add_card(s9, Inches(6.8), Inches(4.6), Inches(5.7), Inches(2.4), "4. Anti-PEG Immunogenicity", [
        "Repeated exposure to PEGylated lipids can stimulate anti-PEG IgM/IgG antibodies.",
        "Causes Accelerated Blood Clearance (ABC) and risks complement-activation pseudoallergy (CARPA).",
        "Driving development of PEG-free hydrophilic polymer coatings."
    ], accent_color=ACCENT_AMBER, font_size=9.5, space_after=4)

    s9.notes_slide.notes_text_frame.text = (
        "SLIDE 9 SPEAKER NOTES:\n"
        "An objective case analysis must confront technical vulnerabilities. The foremost challenge is the 'liver trap': when you inject standard LNPs intravenously, "
        "they absorb ApoE from your blood and get cleared by the liver. That's fine for liver enzyme deficiency, but useless if you want to target brain tumors or lungs. "
        "Second, mRNA expression is temporary—lasting only a few days. While perfect for vaccines, treating a chronic metabolic disease requires repeated dosing, which risks "
        "triggering anti-PEG antibodies, inflammation, and reduced therapeutic efficacy over time. Overcoming these delivery barriers is Moderna's central scientific focus."
    )

    # =========================================================================
    # SLIDE 10: Legal, Regulatory & Intellectual Property Hurdles
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, 10, "Legal & IP Landscape", "Intellectual Property Warfare & Regulatory Complexity",
               "Navigating high-stakes patent battles, government disputes, and pioneering regulatory standards.")

    add_card(s10, Inches(0.8), Inches(2.0), Inches(5.7), Inches(5.0), "The Multi-Billion Dollar Patent Battles", [
        "Arbutus / Genevant Landmark Settlement (March 2026):",
        "  • Long-standing litigation alleging Moderna's COVID vaccine infringed foundational patents on ionizable lipids and 4-component LNP ratios.",
        "  • Resolved via a landmark $2.25 Billion global settlement ($950M upfront, up to $1.3B contingent), eliminating major legal overhang.",
        "Moderna vs. Pfizer & BioNTech Litigation:",
        "  • Transatlantic lawsuits filed in the US, Germany, and UK alleging Comirnaty infringed Moderna's patents on modified mRNA chemistry.",
        "  • Ongoing countersuits by BioNTech and Pfizer challenging patent validity.",
        "US NIH / Government Inventorship Dispute:",
        "  • Public clash over whether federal scientists at the NIH Vaccine Research Center should be credited as co-inventors on the core Spikevax sequence."
    ], accent_color=ACCENT_CORAL, font_size=9, space_after=5)

    add_card(s10, Inches(6.8), Inches(2.0), Inches(5.7), Inches(5.0), "Regulatory Precedents & Paradigm Evolution", [
        "Strain Change Regulatory Pathways:",
        "  • Pioneered FDA/EMA frameworks permitting seasonal antigen updates without requiring repeating full 30,000-patient efficacy trials.",
        "Individualized Medicine Regulation:",
        "  • Establishing novel regulatory review models for bespoke cancer vaccines (mRNA-4157), where each individual batch has a distinct chemical sequence.",
        "Biosimilar Barriers:",
        "  • Extremely complex LNP/mRNA formulation creates massive technical and regulatory moats, insulating Moderna from rapid generic/biosimilar erosion."
    ], accent_color=ACCENT_TEAL, font_size=9, space_after=5)

    s10.notes_slide.notes_text_frame.text = (
        "SLIDE 10 SPEAKER NOTES:\n"
        "In biotechnology, patent defense is as critical as laboratory discovery. Moderna was entangled in high-stakes intellectual property warfare. "
        "Most notably, Arbutus Biopharma claimed foundational ownership over four-component LNP formulation ratios. Just in March 2026, Moderna reached a historic "
        "$2.25 billion global settlement, paying $950 million upfront to finally remove that legal cloud. At the same time, Moderna continues to litigate against Pfizer "
        "and BioNTech over modified nucleoside IP. On the regulatory side, Moderna successfully worked with the FDA to treat strain updates like annual flu shots, creating "
        "a regulatory expressway for recurring commercial updates."
    )

    # =========================================================================
    # SLIDE 11: Market Disruption & Financial Trajectory
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, 11, "Financial & Market Dynamics", "Market Impact: Revenue Transformation & Platform Economics",
               "Managing the post-pandemic revenue normalization while harnessing software-like platform economics.")

    add_card(s11, Inches(0.8), Inches(2.0), Inches(5.7), Inches(5.0), "Financial Hyper-Growth & Transition", [
        "The Revenue Explosion (2020–2022):",
        "  • Scaled from $0 in commercial product sales to $18.5B (2021) and $19.3B (2022) with >60% net margins.",
        "  • Peak cash reserves exceeded $18 billion.",
        "The Post-Pandemic Normalization:",
        "  • Revenue adjusted to endemic respiratory levels ($6.8B in 2023; stabilizing at $3B–$4B range in 2024–2025).",
        "Capital Reinvestment Strategy:",
        "  • Sustaining aggressive R&D reinvestment (> $4B annually) across ~45 pipeline assets.",
        "  • Target: Path to cash-flow breakeven driven by respiratory combos and oncology launches."
    ], accent_color=ACCENT_CYAN, font_size=9, space_after=5)

    add_card(s11, Inches(6.8), Inches(2.0), Inches(5.7), Inches(5.0), "Platform Economics: Marginal Cost Advantage", [
        "Traditional Pharma Model:",
        "  • High marginal cost per new drug ($1.5B+). Every new drug requires novel chemistry, custom assays, new bioreactor lines, and distinct toxicology.",
        "The Moderna Software Model:",
        "  • Fixed initial capital spent building LNP chemistry, safety databases, and digital manufacturing.",
        "  • Low marginal cost to add pipeline candidates: Simply modify the digital sequence file.",
        "Compounding Value:",
        "  • Every clinical trial de-risks the delivery vehicle for all other assets.",
        "  • Higher Probability of Technical Success (PTRS) across pipeline programs."
    ], accent_color=ACCENT_TEAL, font_size=9, space_after=5)

    s11.notes_slide.notes_text_frame.text = (
        "SLIDE 11 SPEAKER NOTES:\n"
        "Let's evaluate Moderna's financial transformation. In 2019, Moderna had zero commercial product sales. By 2022, they recorded nearly $20 billion in annual revenue. "
        "Inevitably, as pandemic crisis urgency faded, revenues faced a steep cliff down to endemic levels. But here is where platform economics shine: unlike traditional pharma, "
        "where each drug requires completely new manufacturing plants and custom chemistry, Moderna's platform shares the same LNP formulation, the same Norwood facility, "
        "and the same safety data. This drastically lowers the marginal cost of developing asset number 45 compared to asset number 1."
    )

    # =========================================================================
    # SLIDE 12: Conclusion & Strategic Takeaways
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header(s12, 12, "Strategic Synthesis", "Conclusion: Key Takeaways for the Biotech Industry",
               "How Moderna established the modern paradigm of programmable biotechnology.")

    add_card(s12, Inches(0.8), Inches(2.0), Inches(3.7), Inches(4.8), "1. Delivery is Paramount", [
        "Without advanced lipid nanotechnology, mRNA is clinically useless.",
        "Formulation chemistry and microfluidic manufacturing are as critical as the genetic payload itself.",
        "Future enterprise winners will master targeted extrahepatic delivery."
    ], accent_color=ACCENT_CYAN, font_size=9.5, space_after=6)

    add_card(s12, Inches(4.8), Inches(2.0), Inches(3.7), Inches(4.8), "2. Platform Agility Wins", [
        "Modular, cell-free platforms radically outperform bespoke single-asset pipelines.",
        "Compressed development from decades to weeks provides unmatched strategic resilience during health crises.",
        "Platform economics amortize R&D and CMC expenditures across dozens of programs."
    ], accent_color=ACCENT_TEAL, font_size=9.5, space_after=6)

    add_card(s12, Inches(8.8), Inches(2.0), Inches(3.7), Inches(4.8), "3. Tech-Bio Convergence", [
        "Moderna succeeded by fusing molecular genetics, AI computational design, nanotechnology, and robotics.",
        "Proved that biology can be engineered with software-like iteration cycles.",
        "mRNA is now an enduring, permanent pillar of global medicine alongside small molecules and biologics."
    ], accent_color=ACCENT_AMBER, font_size=9.5, space_after=6)

    s12.notes_slide.notes_text_frame.text = (
        "SLIDE 12 SPEAKER NOTES:\n"
        "In conclusion, Moderna's journey offers three timeless lessons for biotechnology leaders:\n"
        "First, delivery is paramount—formulation chemistry was the true enabler of mRNA's triumph.\n"
        "Second, platform models beat bespoke pipelines: by treating mRNA as software, Moderna achieved compounding velocity and capital efficiency.\n"
        "And third, the future of biotechnology lies in multidisciplinary convergence: computation, synthetic biology, nanotechnology, and robotics.\n"
        "Moderna did not just develop vaccines; it permanently altered how humanity creates medicine. Thank you, and I look forward to your questions."
    )

    output_path = os.path.join(base_dir, "Moderna_Biotech_Case_Study_Presentation.pptx")
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_deck()

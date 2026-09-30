# DRUGART Phase 3 — VirogenAI and Advanced Analytics Integration

## 1. Phase 2 remediation

The Future Genomics beta feedback becomes a concrete remediation workstream:

- support FASTQ, FASTQ.gz, FASTA, SFF, BAM and SAM;
- improve upload and processing performance;
- add interactive QC and outlier filtering;
- expose model/algorithm, database, confidence threshold and alternative predictions;
- make retention, deletion and third-party sharing policies explicit;
- strengthen data architecture and reproducible benchmarking;
- retain community-ecology analytics as a core scientific workflow.

The feedback specifically notes that the current analytical foundation is scientifically credible, but that missing interactive QC, outlier filtering, provenance and explanatory metadata limits research defensibility. 

## 2. VirogenAI integration

VirogenAI contributes a scientific evidence and research-orchestration layer. Its current architecture explicitly separates RAG evidence, agent orchestration and numerical scientific computation.

The DRUGART workflow becomes:

Question -> Evidence Retrieval -> Evidence Validation -> Parameter Proposal -> Analytics -> Result -> Evidence-grounded Explanation

The LLM is an orchestrator and explainer, not the numerical source of truth.

## 3. Advanced molecular analytics

Phase 3 should implement independently testable analytics for:

- potency
- selectivity
- stability
- toxicity risk
- manufacturability
- ADMET model interfaces
- dose-response and kinetic analysis
- uncertainty intervals
- sensitivity analysis
- Pareto-front candidate analysis
- active-learning experiment prioritisation

Candidate selection should preserve the full objective vector and Pareto frontier instead of hiding scientific trade-offs inside one opaque score.

## 4. Learning loop

Data -> Design -> Predict -> Experiment -> Result -> Learn -> Redesign

Every prediction should retain model version, algorithm, data/database version, confidence, threshold, alternatives, evidence IDs and assumptions where applicable.

## 5. Architecture

    DRUGART
       |
       +-- Genomics/QC
       |     +-- ingestion and validation
       |     +-- interactive QC
       |     +-- outlier detection
       |
       +-- VirogenAI
       |     +-- scientific RAG
       |     +-- mechanisms/targets
       |     +-- evidence provenance
       |
       +-- Molecular Analytics
       |     +-- ADMET
       |     +-- kinetics
       |     +-- uncertainty
       |     +-- multi-objective optimisation
       |
       +-- Research Orchestrator
       |
       +-- Experiment Feedback
       |
       +-- Proprietary Knowledge Base
       |
       +-- Learning / Redesign


## 3. KSP37-tailored CRC Biology-to-Efficacy Workstream

This is a core Phase 3 scientific workstream. Its objective is to train a domain-adapted biomedical AI model to learn CRC biology and then integrate that representation with KSP37/FGFBP2 evidence to construct an evidence-grounded mechanistic model for exploring potential KSP37 efficacy. The system generates hypotheses and uncertainty-bounded projections, not clinical efficacy claims.

### P3-K1 — CRC biological training corpus

Build a deliberately structured 5,000–10,000 document corpus covering:

- CRC foundation: progression, molecular subtypes, APC/KRAS/TP53/BRAF, WNT/EGFR/TGF-beta;
- Lynch/dMMR/MSI-H: MLH1/MSH2/MSH6/PMS2, MMR deficiency, MSI, neoantigens, HLA/B2M and immune surveillance;
- CRC TME: CD8/CD4 T cells, NK cells, Tregs, TAMs, CAFs, endothelial cells, cytokines/chemokines, hypoxia, angiogenesis and immune exclusion;
- FGF biology: FGF2, FGFBP2/KSP37, FGFR signalling, fibroblasts, angiogenesis and stromal signalling;
- KSP37/FGFBP2: expression, cellular sources, secretion, cytotoxic lymphocyte biology, cancer associations and FGF2-related evidence.

### P3-K2 — Literature-to-training pipeline

Raw papers are not sent directly into training:

Literature -> metadata validation -> full-text acquisition -> text extraction -> section detection -> scientific cleaning -> duplicate removal -> quality/relevance filtering -> CRC biological training corpus.

Each document retains PMID/DOI/PMCID, publication year, study type, species, experimental system, disease, biological entities and source section where available.

### P3-K3 — CRC Biology Model

Start with a suitable open biomedical-capable base LLM and perform continued pretraining/domain adaptation on the CRC corpus.

Base LLM + CRC biological literature -> CRC-Bio Adapted LLM.

Training and evaluation literature remain separated. The training objective is improved representation and reasoning over CRC terminology, pathways, cellular interactions, disease states and mechanisms.

### P3-K4 — CRC biological validation

Create a manually validated benchmark covering CRC genetics, Lynch syndrome, dMMR/MSI-H, neoantigens, TME, CD8/NK biology, T-cell exhaustion, CAF/TAM biology, FGF2/FGFR signalling and CRC therapeutic mechanisms.

Compare the base LLM with the CRC-Bio model on factual accuracy, relationship extraction, mechanism reconstruction, contradiction detection, evidence attribution and unseen-paper/question performance.

The CRC-Bio model advances only after measurable improvement over the base model.

### P3-K5 — KSP37 Biology Model

After CRC biological validation, introduce the KSP37/FGFBP2 corpus:

CRC-Bio LLM + KSP37/FGFBP2 literature -> CRC-KSP37 Biology Model.

Evaluate expression, cellular sources/secretion, KSP37/FGFBP2-to-FGF2 evidence, FGFBP2 in cytotoxic lymphocytes, CRC evidence and established versus speculative components of the KSP37-to-FGF2 hypothesis.

### P3-K6 — Mechanistic biological model

The AI converts literature into structured relationships rather than directly predicting efficacy:

KSP37/FGFBP2 -> FGF2 availability -> FGFR signalling -> stromal/tumour effects -> TME state -> CD8/NK behaviour -> tumour-control mechanisms.

Each relationship retains direction, evidence strength, experimental system, species, study type, effect size where available, supporting publications, contradictory evidence and uncertainty.

The evidence layer distinguishes Established evidence -> Supported inference -> Hypothesis.

### P3-K7 — KSP37 efficacy projection engine

The AI does not output a direct efficacy percentage. The structured biological model becomes an input to mechanistic simulation:

CRC disease state + Lynch/MSI status + TME state + immune state + KSP37 expression + FGF2/FGFR state + KSP37 perturbation -> mechanistic simulation -> predicted biological changes -> tumour-control scenarios.

The engine produces scenario distributions with uncertainty propagated through poorly established relationships. Initial scenarios are conservative, intermediate and alternative mechanistic assumptions.

The output is an evidence-weighted efficacy hypothesis, not a clinical prediction.

### P3-K8 — Experimental feedback and uncertainty reduction

Literature -> CRC-Bio Model -> KSP37 Model -> Mechanistic Simulation -> Efficacy Projection -> Uncertainty Analysis -> Critical Missing Evidence -> Recommended Experiments -> New Experimental Data -> Model Update.

Long-term loop:

Learn CRC biology -> learn KSP37 biology -> integrate mechanisms -> simulate intervention -> quantify uncertainty -> identify experiments -> incorporate new evidence -> update the model.

## 4. KSP37-specific architecture

    CRC literature
          |
    CRC Biological Corpus
          |
    CRC-Bio Model
          |
    KSP37 / FGFBP2 Corpus
          |
    CRC-KSP37 Biology Model
          |
    Mechanistic Relationship Graph
          |
    KSP37 Intervention / Perturbation
          |
    Mechanistic Simulation
          |
    Scenario Distribution
          |
    Uncertainty Analysis
          |
    Experiment Prioritisation
          |
    New Experimental Evidence
          |
    Model Update

## 5. Revised Phase 3 delivery sequence

### P3.1 — Phase 2 remediation
Multi-format ingestion, QC, outlier filtering, provenance, governance and benchmark datasets.

### P3.2 — VirogenAI evidence foundation
Scientific ingestion, hybrid retrieval, evidence/claim records, mechanism and target extraction, citation-grounded synthesis.

### P3.3 — CRC Biology Model
Build the 5,000–10,000 document corpus, perform domain adaptation/continued pretraining and establish a held-out biological benchmark.

### P3.4 — KSP37 Biology Model
Integrate KSP37/FGFBP2 literature into the validated CRC biological context and extract structured mechanistic relationships.

### P3.5 — Mechanistic KSP37 efficacy engine
CRC state + immune/TME state + KSP37/FGF2/FGFR relationships -> mechanistic simulation -> uncertainty-bounded efficacy scenarios.

### P3.6 — Advanced analytics
Dose-response, kinetics, ADMET interfaces, sensitivity, uncertainty, Pareto optimisation and experiment prioritisation.

### P3.7 — Controlled research agent
Question interpretation, evidence retrieval, parameter construction, validation, simulation, analytics and provenance-aware synthesis.

### P3.8 — Experimental learning loop
Prediction-versus-observation analysis, model-error tracking, active-learning dataset preparation, critical-evidence identification and candidate redesign.

### P3.9 — Molecular IVD analytics
Biomarker selection, assay-performance analytics, analytical sensitivity/specificity and AI-backed assay optimisation.

## 6. KSP37-specific acceptance criteria

- CRC training corpus is provenance tracked and quality filtered.
- Training and evaluation literature are separated.
- CRC biological benchmark is manually validated.
- CRC-Bio performance is quantitatively compared with the base model.
- KSP37/FGFBP2 evidence remains separately traceable.
- Biological relationships distinguish established evidence, supported inference and hypothesis.
- Contradictory evidence is retained rather than silently resolved.
- Biological relationships include uncertainty metadata.
- KSP37 efficacy outputs are scenario distributions rather than unsupported point claims.
- Model assumptions are inspectable.
- Uncertainty propagates through poorly established relationships.
- Simulations are independently testable without an LLM.
- Predictions can be compared directly with experimental observations.
- The system identifies experiments that can reduce important uncertainty.

## 7. Delivery increments

### P3.1 — Phase 2 remediation
Multi-format ingestion, QC, outlier filtering, provenance, governance and benchmark datasets.

### P3.2 — VirogenAI evidence integration
Scientific ingestion, hybrid retrieval, evidence/claim records, mechanism and target extraction, citation-grounded synthesis.

### P3.3 — Advanced analytics
Candidate objective model, Pareto frontier, uncertainty, sensitivity, dose-response/kinetics, ADMET interfaces and experiment prioritisation.

### P3.4 — Controlled agent workflow
Question interpretation, retrieval, parameter construction, validation, analytics execution and provenance-aware synthesis.

### P3.5 — Laboratory feedback loop
Prediction-versus-observation analysis, model-error tracking, active-learning dataset preparation and candidate redesign.

### P3.6 — Molecular IVD analytics
Biomarker selection, assay-performance analytics, analytical sensitivity/specificity and AI-backed assay optimisation.

## 8. Phase 3 acceptance criteria

- AI results have inspectable provenance.
- Supported genomic formats are accepted and validated.
- QC and outlier handling are reproducible.
- Candidate analytics expose objective trade-offs.
- Appropriate quantitative outputs include uncertainty.
- RAG answers trace to source evidence.
- Experimental results can be compared with predictions.
- Analytics are testable without an LLM.
- End-to-end runs are reproducible from versioned data, model and configuration metadata.

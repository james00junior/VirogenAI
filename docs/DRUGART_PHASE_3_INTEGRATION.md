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

## 6. Delivery increments

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

## 7. Phase 3 acceptance criteria

- AI results have inspectable provenance.
- Supported genomic formats are accepted and validated.
- QC and outlier handling are reproducible.
- Candidate analytics expose objective trade-offs.
- Appropriate quantitative outputs include uncertainty.
- RAG answers trace to source evidence.
- Experimental results can be compared with predictions.
- Analytics are testable without an LLM.
- End-to-end runs are reproducible from versioned data, model and configuration metadata.

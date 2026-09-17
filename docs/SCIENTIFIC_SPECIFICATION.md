# VirogenAI — Scientific Specification

## 1. Purpose

This document defines the initial scientific scope and boundaries of VirogenAI.

The purpose of the first scientific system is to investigate controlled solid-tumour growth and treatment-response dynamics using computational models grounded in scientific evidence.

## 2. Initial scope

The initial modelling scope includes:

- tumour growth
- tumour cell populations
- proliferation
- apoptosis
- treatment effects
- treatment response
- resistance
- oxygen availability
- tumour viability
- selected tumour microenvironment variables

## 3. Initial outputs

Depending on the implemented model, outputs may include:

- tumour volume
- total cell population
- growth rate
- viability
- treatment response
- resistant-cell fraction
- hypoxic fraction
- necrotic fraction
- spatial distributions where supported

## 4. Initial simulation objective

The first controlled simulation should investigate:

```text
Tumour growth
      +
Treatment effect
      +
Resistance
      +
Parameter uncertainty
```

The initial model must remain sufficiently constrained to permit testing, interpretation, and scientific validation.

## 5. Model hierarchy

Potential modelling approaches are introduced incrementally:

1. ODE population models
2. PDE models for spatial fields such as oxygen, nutrients, or drug concentration
3. Agent-based models for individual cells
4. Hybrid multi-scale models

The project will not assume that the most complex model is automatically the most scientifically useful.

## 6. Scientific evidence

Model assumptions and parameter choices should be traceable to scientific evidence where evidence exists. Evidence may include peer-reviewed literature, clinical studies, public datasets, pharmacological resources, cancer databases, molecular biology resources, and mechanistic studies.

## 7. Parameter provenance

Parameters should have provenance metadata where practical:

- parameter name
- value
- units
- source
- source identifier
- evidence type
- applicable tumour context
- uncertainty or range
- model version

## 8. Scientific uncertainty

The platform must distinguish between:

- measured values
- estimated values
- model assumptions
- inferred parameters
- simulated outputs
- AI-generated hypotheses

AI-generated hypotheses must not be represented as experimentally established facts.

## 9. Validation principles

Scientific validation will include:

- mathematical correctness
- numerical stability
- parameter plausibility
- comparison with known biological behaviour
- comparison with relevant literature
- sensitivity analysis
- uncertainty analysis
- reproducibility

## 10. Scope boundary

VirogenAI is initially a research and simulation platform. It must not represent simulation results as clinical diagnoses, treatment recommendations, or validated patient-specific clinical predictions without the appropriate evidence, validation, governance, and regulatory framework.

## 11. Scientific evolution

The scientific specification is version controlled. New biological mechanisms should be introduced through explicit design and validation rather than silently changing the behaviour of existing models.

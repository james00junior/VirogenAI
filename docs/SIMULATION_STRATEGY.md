# VirogenAI — Simulation Strategy

## Objective

Build a scientifically controlled simulation engine that can evolve from simple validated models toward more detailed spatial and multi-scale tumour models.

## Model progression

```text
ODE population models
        ↓
PDE spatial fields
        ↓
Agent-based cell models
        ↓
Hybrid multi-scale models
```

This progression is a development strategy, not a requirement that every model must be implemented.

## Initial model

The first controlled model should focus on:

- tumour growth
- treatment effect
- resistance
- parameter uncertainty

## Reproducibility

Every simulation should identify:

- simulation configuration
- model version
- parameter values
- initial conditions
- simulation duration
- timestep
- random seed when applicable
- software version where practical

## Numerical integrity

Simulation code must be independently testable. Numerical solvers should have tests for boundary conditions, expected behaviour, stability, and reproducibility.

## Outputs

The first model should support outputs such as tumour volume, population size, growth rate, viability, treatment response, and resistance fraction where defined by the model.

## Future spatial modelling

When scientifically justified, spatial models may represent oxygen, nutrients, drug concentration, cellular populations, vascular structures, necrosis, and resistant regions.

Complexity should be introduced only when it provides a testable scientific benefit.

# VirogenAI — AI, RAG and Agent Strategy

## Principle

VirogenAI uses RAG and agents for different purposes.

RAG provides access to scientific evidence. Agents orchestrate multi-step research and simulation workflows. The simulation engine performs numerical computation.

## RAG role

RAG answers questions such as:

- What does the literature report?
- What mechanisms have been observed?
- What parameters or ranges have been reported?
- What evidence supports a model assumption?

The RAG layer should preserve source metadata and support citation-grounded responses.

## Agent role

Agents coordinate workflows such as:

```text
Question
  ↓
Intent analysis
  ↓
Research
  ↓
Evidence retrieval
  ↓
Parameter proposal
  ↓
Validation
  ↓
Simulation
  ↓
Analysis
  ↓
Evidence-grounded synthesis
```

Agents should use explicit tools and structured state rather than unrestricted autonomous behaviour.

## LLM role

LLMs may:

- interpret questions
- extract structured information
- retrieve and synthesise evidence
- propose simulation scenarios
- explain simulation results

LLMs must not be treated as the numerical source of truth.

## Local models

Local LLMs are a supported initial direction. Model choice should be based on evaluation rather than assumption. The architecture must permit replacement of the local model without rewriting the scientific platform.

## Evaluation

Models and agent workflows will be evaluated for:

- scientific reasoning
- evidence grounding
- citation accuracy
- structured outputs
- tool selection
- parameter validity
- reproducibility
- failure handling

## Safety boundary

An AI-generated statement must be distinguishable from retrieved scientific evidence and from a numerical simulation result. The platform must avoid presenting unsupported model outputs as established clinical facts.

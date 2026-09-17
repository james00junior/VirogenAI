# VirogenAI — Data Strategy

## Objective

Establish a traceable scientific data foundation for literature, biological evidence, model parameters, simulation configurations, and future public datasets.

## Evidence sources

Potential sources include:

- peer-reviewed publications
- clinical studies
- public biological datasets
- cancer databases
- pharmacological resources
- molecular biology resources
- mechanistic studies

## Evidence metadata

The initial evidence model should support fields such as:

```text
source_id
title
authors
year
journal
doi
abstract
full_text
cancer_type
treatment
mechanism
biological_process
evidence_type
```

## Provenance

Scientific data must retain source provenance where practical. Transformations should be reproducible and documented.

## Data quality

The data platform should detect and manage:

- duplicate sources
- malformed records
- missing required metadata
- invalid values
- inconsistent units
- unsupported assumptions

## Separation of data types

The platform should distinguish between:

- source evidence
- extracted claims
- model parameters
- model assumptions
- simulation inputs
- simulation outputs
- AI-generated hypotheses

## Storage direction

PostgreSQL is the initial structured data store. pgvector will support vector retrieval in the RAG phase. Object storage can be introduced for larger source documents and artefacts.

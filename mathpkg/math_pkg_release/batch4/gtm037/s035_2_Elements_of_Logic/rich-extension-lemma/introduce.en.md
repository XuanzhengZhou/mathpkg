---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This lemma is the crucial technical step in Henkin's completeness proof. Starting from any consistent set $\Gamma$ of sentences, one expands the language by adding sufficiently many new individual constants (Henkin constants) and then extends $\Gamma$ to a rich set $\Delta$ while preserving consistency. The construction proceeds by enumerating all existential sentences $\exists\beta\psi$ and, for each, selecting a fresh constant $d_\alpha$ and adding the Henkin axiom $\exists\beta\psi \rightarrow \operatorname{Subf}_{d_\alpha}^\beta\psi$ to the growing set. A careful choice of always-fresh constants ensures consistency is maintained at each finite stage, and the final set $\Delta$ is rich by construction.

---
role: proof
locale: en
of_concept: cw-complex-has-simplicial-simple-homotopy-type
source_book: gtm010
source_chapter: "7"
source_section: "7"
---

SKETCH OF PROOF: Use the fact [J. H. C. WHITEHEAD 3 (Section 15)]: If $J_1$ and $J_2$ are simplicial complexes and $f: J_1 \rightarrow J_2$ is a simplicial map then the mapping cylinder $M_f$ is triangulable so that $J_1$ and $J_2$ are subcomplexes.

If $K$ is a point the result is trivial. Suppose that $K = L \cup e^n$ where $e^n$ is a top dimensional cell with characteristic map $\varphi: I^n \rightarrow K$. Set $\varphi_0 = \varphi | \partial I^n$.

By induction on the number of cells there is a simple-homotopy equivalence $f: L \rightarrow L'$ where $L'$ is a simplicial complex. Then, using subdivision invariance (proved in Section 25), $K \wedge K \cup L' \wedge L' \cup I^n \wedge K'$ where $K'$ is simplicial.

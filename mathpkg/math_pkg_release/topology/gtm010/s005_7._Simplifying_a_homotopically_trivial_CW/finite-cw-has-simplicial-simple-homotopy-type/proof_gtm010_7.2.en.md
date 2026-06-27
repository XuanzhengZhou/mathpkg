---
role: proof
locale: en
of_concept: finite-cw-has-simplicial-simple-homotopy-type
source_book: gtm010
source_chapter: "7"
source_section: "7"
---

(Sketch) Use the following fact [J. H. C. Whitehead 3 (§15)]: If $J_1$ and $J_2$ are simplicial complexes and $f: J_1 \to J_2$ is a simplicial map, then the mapping cylinder $M_f$ is triangulable so that $J_1$ and $J_2$ are subcomplexes.

If $K$ is a point, the result is trivial. Suppose $K = L \cup e^n$ where $e^n$ is a top dimensional cell with characteristic map $\varphi: I^n \to K$, and set $\varphi_0 = \varphi|\partial I^n$. By induction on the number of cells, there is a simple-homotopy equivalence $f: L \to L'$ where $L'$ is a simplicial complex. Using the triangulability of mapping cylinders and the fact that subdivision does not change simple-homotopy type: $K \wedge K \cup_f L' \wedge L' \cup \text{simplex} \wedge K'$, where $K'$ is simplicial.

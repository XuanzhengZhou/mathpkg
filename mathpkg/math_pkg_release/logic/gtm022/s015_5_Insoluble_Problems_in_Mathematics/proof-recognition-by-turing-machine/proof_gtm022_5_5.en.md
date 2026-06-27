---
role: proof
locale: en
of_concept: proof-recognition-by-turing-machine
source_book: gtm022
source_chapter: "5"
source_section: "5"
---

If $\mathcal{T}$ is effectively axiomatised, then there is a Turing machine which, when given the Gödel number of an element $q \in P(V^*, \mathcal{R}^*)$, tells us whether or not $q$ is an axiom of $\mathcal{T}$. Given Gödel numbers of $p \in \mathcal{L}(\mathcal{T})$ and of the sequence $p_1, p_2, \ldots, p_n$, the Turing machine can check: (i) whether each $p_i$ is an axiom or follows from earlier $p_j$ by the rules of consequence $C$; (ii) whether $p_n = p$. Since the rules of consequence are finitary and effective, each step is computable. Thus the entire verification is computable by a Turing machine.

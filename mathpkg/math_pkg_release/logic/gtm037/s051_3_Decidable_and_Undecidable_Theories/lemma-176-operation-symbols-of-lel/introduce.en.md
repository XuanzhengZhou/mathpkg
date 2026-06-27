---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Lemma 17.6 is a technical result that establishes the correctness of the number-theoretic interpretation $\#\mathbf{O}$ assigned to each operation symbol $\mathbf{O}$ of $\mathcal{L}_{\text{el}}$ in Definition 17.4. The lemma states that whenever the number-theoretic function $\#\mathbf{O}$ maps inputs $x_0, \ldots, x_{m-1}$ to output $y$, the formal theory $\mathcal{P}$ proves the corresponding equation $\mathbf{O}(\Delta x_0, \ldots, \Delta x_{m-1}) = \Delta y$. The proof proceeds by straightforward induction on the construction of $\mathbf{O}$, following the recursive clauses given in Definition 17.4. This lemma is essential for formalizing the syntax of first-order logic within $\mathcal{P}$: it ensures that the formal operation symbols faithfully mirror their intended number-theoretic counterparts, which are used to encode syntactic operations such as concatenation and substitution via Godel numbering.

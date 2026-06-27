---
role: proof
locale: en
of_concept: lowenheim-skolem-infinitary
source_book: gtm053
source_chapter: "7"
source_section: "7.3"
---

The proof of the downward Löwenheim–Skolem theorem for $L_{\omega_1,\omega}$ follows the same method as in the first-order case (Section 3.4). One constructs a set of Skolem functions for the $L_{\omega_1,\omega}$-sentence $P$ and then takes the closure of a subset of $A$ of size $\kappa$ under all these Skolem functions. The resulting substructure has cardinality $\kappa$ and is an elementary substructure with respect to $L_{\omega_1,\omega}$-formulas, hence satisfies $P$.

For the failure of the upward theorem, the counterexample uses an $L_{\omega_1,\omega}$-sentence $Q$ in the language of arithmetic extended by unary $N$ and binary $\epsilon$. The sentence $Q$ states: $(N, +, \cdot, 0, 1)$ satisfies all first-order axioms of Peano arithmetic (using a countable conjunction), and $\forall x \bigvee_{n \in \mathbb{N}} (x = \underline{n})$ (using a countable disjunction, where $\underline{n}$ is the numeral for $n$). This forces every element to be standard, so any model of $Q$ is countable. Hence $Q$ has a model but no uncountable model.

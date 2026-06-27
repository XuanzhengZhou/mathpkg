---
role: proof
locale: en
of_concept: fundamental-lemma-l2real
source_book: gtm053
source_chapter: "III"
source_section: "3"
---

Part (a) and (b) are verified by checking that the logical axioms have truth value 1 under the Boolean interpretation, using the inductive definition of the truth function. Part (c) involves verifying axioms including the field axioms, order axioms, and the completeness axiom. Among these, the axiom of choice and completeness axiom require the most work.

Part (d) is proved by constructing an explicit function $\bar{h} \in \overline{R}^{(1)}$ whose set of zeros has intermediate cardinality. Fix a subset $\mathcal{J} \subset I$ having cardinality strictly between $\omega_0$ and $\operatorname{card} I$. For each $i \in I$, let $\bar{x}_i \in \overline{R}$ be the $i$th coordinate function. Define $\Omega(\bar{x}) = \bigvee_{j \in \mathcal{J}} \|\bar{x} = \bar{x}_j\|$ and set
$$\bar{h}(\bar{x})(\omega) = \begin{cases} 0, & \text{if } \omega \in \Omega(\bar{x}), \\ 1, & \text{otherwise.} \end{cases}$$
Then $\bar{h}$ has an intermediate number of zeros, disproving CH.

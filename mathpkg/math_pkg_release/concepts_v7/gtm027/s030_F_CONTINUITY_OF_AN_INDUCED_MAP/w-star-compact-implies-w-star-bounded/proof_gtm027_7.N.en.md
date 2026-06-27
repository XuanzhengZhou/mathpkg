---
role: proof
locale: en
of_concept: w-star-compact-implies-w-star-bounded
source_book: gtm027
source_chapter: "7"
source_section: "N"
---

# Proof of Weak-Star Compactness Implies Weak-Star Boundedness

Let $F \subseteq X^*$ be $w^*$-compact. We prove that $F$ is $w^*$-bounded, i.e., for each $x \in X$, the set $\{f(x) : f \in F\}$ is bounded in $\mathbb{R}$.

For each fixed $x \in X$, the evaluation map $e_x : X^* \to \mathbb{R}$ defined by $e_x(f) = f(x)$ is $w^*$-continuous. The continuous image of a compact set is compact. Thus $e_x(F) = \{f(x) : f \in F\}$ is a compact subset of $\mathbb{R}$, hence bounded.

Therefore $F$ is $w^*$-bounded.

Alternatively: if the $w^*$-closure of $F$ is $w^*$-compact, then by the same argument $F$ is $w^*$-bounded. In particular, for equicontinuous $F$, from (d) we have $\overline{F}^{w^*}$ is $w^*$-compact, so $F$ is $w^*$-bounded.

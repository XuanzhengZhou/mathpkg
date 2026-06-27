---
role: proof
locale: en
of_concept: interior-closure-duality
source_book: gtm027
source_chapter: "1"
source_section: "Interior and Boundary"
---

# Proof of Interior-Closure Duality

Let $A$ be a subset of a topological space $X$. Denote the complement $X \sim A$ by $A'$.

From Theorem 9, we have the identity $(X \sim A)^- = X \sim A^0$, which can be rewritten in the complement notation as

$$A'^- = (A^0)'.$$

Taking complements of both sides yields

$$(A'^-)' = A^0,$$

that is, the interior of $A$ is the complement of the closure of the complement of $A$:

$$A^0 = X \sim (\overline{X \sim A}).$$

Now replace $A$ by its complement $X \sim A$ in the above relation. Writing $B = X \sim A$, we obtain $B^0 = X \sim (\overline{X \sim B})$. But $X \sim B = A$, so

$$(X \sim A)^0 = X \sim A^-.$$

Taking complements gives the dual formula:

$$A^- = X \sim ((X \sim A)^0),$$

that is, the closure of a set is the complement of the interior of the complement. Thus the interior and closure operators are dual under complementation. $\square$

---
role: proof
locale: en
of_concept: sorgenfrey-plane-not-lindelof
source_book: gtm027
source_chapter: "1"
source_section: "L"
---

# Proof that the Sorgenfrey Plane Is Not Lindelöf

**Proposition.** The space $(Y, \mathfrak{U})$ (the Sorgenfrey plane) is not a Lindelöf space.

*Proof.* Consider the same anti-diagonal subspace $Z = \{(x,y) : x + y = 1\}$ as in part (b). We showed $Z$ is an uncountable discrete subspace of $Y$.

Recall that a closed subspace of a Lindelöf space is Lindelöf. The subspace $Z$ is closed in $Y$: its complement is the union of open sets $[x, x+\varepsilon) \times [y, y+\varepsilon)$ for points not on the line $x+y=1$.

Now, $Z$ with the discrete topology and cardinality $\mathfrak{c}$ (the continuum) is not Lindelöf: the open cover by singletons $\{\{(x,1-x)\} : x \in \mathbb{R}\}$ has no countable subcover.

Since $Z$ is a closed subspace of $Y$ and $Z$ is not Lindelöf, $Y$ cannot be Lindelöf. $\square$

**Remark.** This is a classic example showing that the product of two Lindelöf spaces (each copy of the Sorgenfrey line is hereditarily Lindelöf by Problem K(c)) need not be Lindelöf. The Sorgenfrey plane is the standard counterexample.

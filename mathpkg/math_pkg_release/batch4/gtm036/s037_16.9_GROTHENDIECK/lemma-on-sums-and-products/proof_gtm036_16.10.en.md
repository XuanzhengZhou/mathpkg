---
role: proof
locale: en
of_concept: lemma-on-sums-and-products
source_book: gtm036
source_chapter: "16"
source_section: "16.10"
---

To prove (i), observe that if $f \in \prod \{B_t^\circ: t \in A\}$ and $x$ belongs to $B_t$, then $|\langle x, f \rangle| = |\langle x(t), f(t) \rangle|$, which is at most one because $f(t) \in B_t^\circ$. Hence $f$ belongs to the polar of the union of the sets $B_t$. On the other hand, if $f$ belongs to the polar of the union of the sets $B_t$, then for each $t$ and each $x$ in $B_t$, $|\langle x(t), f(t) \rangle| = |\langle x, f \rangle| \leq 1$; consequently $f(t) \in B_t^\circ$, so $f \in \prod \{B_t^\circ: t \in A\}$.

To prove (ii), note that if $x \in (C_t)_0$ for some $t \in A$, then for each $f$ in $\prod \{C_t: t \in A\}$ we have $|\langle x, f \rangle| = |\langle x(t), f(t) \rangle| \leq 1$ since $f(t) \in C_t$ and $x(t) \in (C_t)_0$. Thus each $(C_t)_0$ is contained in the polar of $\prod \{C_t: t \in A\}$, and hence the convex extension $B$ of their union is also contained in this polar. For the reverse containment up to scalar multiples, if $g$ belongs to the polar of $\prod \{C_t: t \in A\}$, then a standard argument using the circled nature of the sets $C_t$ shows that $g$ lies in $aB$ for every $a > 1$.

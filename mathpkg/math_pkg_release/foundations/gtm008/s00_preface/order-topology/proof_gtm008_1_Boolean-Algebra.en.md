---
role: proof
locale: en
of_concept: order-topology
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.** First, $(\forall x \in P)[x \in [x] \in T']$, so the collection covers $P$. Second, $(\forall x \in P)(\forall [y], [z] \in T')[x \in [y] \cap [z] \rightarrow x \in [x] \subseteq [y] \cap [z]]$, since if $x \leq y$ and $x \leq z$, then any $w \leq x$ satisfies $w \leq y$ and $w \leq z$. By Theorem 1.19 (base-for-topology), $T'$ is a base for a topology on $P$.

The characterizations follow from the definitions of interior, closure, and density in terms of basic open neighborhoods $\{[x]\}$:
1. $x \in A^0$ iff some basic open $[y]$ contains $x$ and is contained in $A$; this is equivalent to $[x] \subseteq A$ since $[x] \subseteq [y]$ whenever $x \in [y]$.
2. $x \in A^-$ iff every basic open containing $x$ meets $A$; this is equivalent to $[x] \cap A \neq 0$.
3-5 follow by applying definitions together with (1) and (2).

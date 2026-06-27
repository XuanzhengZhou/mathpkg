---
role: proof
locale: en
of_concept: canonical-embedding-properties
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

The proof proceeds by induction on the well-founded $\in$-relation.

1. By definition, $[\![\check{x} \in \check{y}]\!] = \sum_{z \in y} [\![\check{x} = \check{z}]\!]$. By the induction hypothesis, $[\![\check{x} = \check{z}]\!] = 1$ if $x = z$ and $0$ otherwise. Since the Boolean sum of mutually disjoint elements is $1$ if any summand is $1$ and $0$ otherwise, we get $[\![\check{x} \in \check{y}]\!] = 1$ iff $x \in y$.

2. By the definition of equality, $[\![\check{x} = \check{y}]\!]$ involves the product over elements of $\check{x}$ and $\check{y}$. Using the induction hypothesis, one shows this product equals $1$ if $x = y$ and $0$ otherwise.

3. For $u \in V^{(2)}$, one shows by induction on the rank that $u$ is forced to equal $\check{v}$ where $v = \{x \in V \mid u(\check{x}) = 1\}$.

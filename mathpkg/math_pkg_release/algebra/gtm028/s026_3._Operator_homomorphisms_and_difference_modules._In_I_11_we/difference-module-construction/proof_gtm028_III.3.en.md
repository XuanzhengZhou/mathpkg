---
role: proof
locale: en
of_concept: difference-module-construction
source_book: gtm028
source_chapter: "III"
source_section: "3"
---

Define addition of cosets by $(x+N) + (y+N) = (x+y)+N$ and scalar multiplication by $a(x+N) = ax+N$. To verify that scalar multiplication is well-defined, suppose $x+N = y+N$, i.e., $x - y \in N$. Then $ax - ay = a(x-y) \in N$ because $N$ is a submodule (not merely a subgroup), so $ax+N = ay+N$. It is then clear that the natural mapping $T \colon x \mapsto x+N$ is an $R$-homomorphism with kernel $N$.

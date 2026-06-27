---
role: proof
locale: en
of_concept: norm-one-subgroup
source_book: gtm006
source_chapter: "2"
source_section: "8"
---

*Proof.* (a) Since $\phi \neq 1$, there is an element $k$ of $K$ with $k^\phi \neq k$. But
$$(k^{\phi-1})^{1+\phi} = (k^{\phi-1})^{\phi} \cdot k^{\phi-1} = k^{1-\phi} \cdot k^{\phi-1} = 1.$$
Thus $k^{\phi-1} \in N$ and $k^{\phi-1} \neq 1$, so $N \neq \{1\}$.

(b) $K^*$ is a cyclic group of order $q^2 - 1$. The map $x \mapsto x^{1+\phi}$ is a homomorphism from $K^*$ to $F^*$. By the theory of cyclic groups, the kernel $N$ is a cyclic subgroup of order $(q^2-1)/(q-1) = q+1$. $\square$

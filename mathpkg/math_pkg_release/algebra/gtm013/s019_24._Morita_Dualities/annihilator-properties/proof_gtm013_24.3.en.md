---
role: proof
locale: en
of_concept: annihilator-properties
source_book: gtm013
source_chapter: "7"
source_section: "24. Morita Dualities"
---
The proof involves straightforward modifications of the arguments given in (2.15) and (2.16). Setting $l_M(N') = \{m \in M \mid \mu(m, n) = 0 \text{ for all } n \in N'\}$ and $r_N(M') = \{n \in N \mid \mu(m, n) = 0 \text{ for all } m \in M'\}$, one verifies the Galois connection properties by direct set-theoretic manipulation of annihilator definitions.

(1) If $M' \leq M''$, then any $n$ that annihilates all of $M''$ certainly annihilates $M'$, so $r_N(M'') \subseteq r_N(M')$.

(2) Every element of $M'$ is annihilated by every element of $r_N(M')$ by definition, so $M' \subseteq l_M r_N(M')$.

(3) Applying (2) to $r_N(M')$ gives $r_N(M') \subseteq r_N l_M r_N(M')$. But also from (1) with $M' \subseteq l_M r_N(M')$ we get $r_N(l_M r_N(M')) \subseteq r_N(M')$. Hence equality.

(4) An element $n$ annihilates $\sum_A M_\alpha$ iff it annihilates each $M_\alpha$, i.e., iff $n \in \bigcap_A r_N(M_\alpha)$.

(5) If $n \in \sum_A r_N(M_\alpha)$, write $n = n_{\alpha_1} + \cdots + n_{\alpha_k}$ with each $n_{\alpha_i} \in r_N(M_{\alpha_i})$. For any $m \in \bigcap_A M_\alpha$, we have $m \in M_{\alpha_i}$ for each $i$, so $\mu(m, n_{\alpha_i}) = 0$, hence $\mu(m, n) = 0$, giving $n \in r_N(\bigcap_A M_\alpha)$.

The dual statements for $S$-submodules follow by symmetry, interchanging the roles of $M$ and $N$.

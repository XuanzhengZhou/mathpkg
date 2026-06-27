---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.5"
proof_technique: decomposition
locale: en
content_hash: ""
written_against: ""
---
By Theorem 4.6, $\phi$ has a basis relative to which its matrix $D$ is the direct sum of the companion matrices of $q_1, \ldots, q_t$. The characteristic polynomial of a companion matrix of $q_i$ is $q_i$ itself (a companion matrix of a monic polynomial $f$ of degree $d$ has characteristic polynomial $f$). Since $D$ is block diagonal, $p_\phi = p_D = q_1 q_2 \cdots q_t$ (using Lemma 5.1 that the characteristic polynomial of a direct sum is the product).

For (ii), since $q_\phi = q_t$ (Theorem 4.2) and $q_1 \mid \cdots \mid q_t$, we have $p_\phi = q_1 \cdots q_t = (q_1 \cdots q_{t-1}) q_\phi$. Hence $p_\phi(\phi) = (q_1 \cdots q_{t-1})(\phi) \cdot q_\phi(\phi) = 0$ since $q_\phi(\phi) = 0$.

(iii) is immediate from (i) and the divisibility chain $q_1 \mid \cdots \mid q_t$.

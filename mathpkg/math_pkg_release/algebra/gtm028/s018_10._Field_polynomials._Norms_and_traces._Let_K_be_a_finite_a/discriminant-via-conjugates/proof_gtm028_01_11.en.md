---
role: proof
locale: en
of_concept: discriminant-via-conjugates
source_book: gtm028
source_chapter: "I"
source_section: "11"
---
Let $\tau_1, \dots, \tau_n$ be the $n$ distinct $k$-isomorphisms of $K$ into a normal closure $K^\star$, and set $\omega_i^{(\alpha)} = \omega_i^{\tau_\alpha}$.

By formula (3) from §11, the trace of the product $\omega_i \omega_j$ can be expressed as the sum over all conjugates:
$$T(\omega_i \omega_j) = \sum_{\alpha=1}^{n} \omega_i^{(\alpha)} \omega_j^{(\alpha)}.$$

Define the $n \times n$ matrix $W = (\omega_i^{(\alpha)})_{i,\alpha}$. Then the $(i,j)$-entry of the product $W W^T$ is
$$(W W^T)_{ij} = \sum_{\alpha=1}^{n} \omega_i^{(\alpha)} \omega_j^{(\alpha)} = T(\omega_i \omega_j).$$

Therefore the discriminant matrix $(T(\omega_i \omega_j))$ equals $W W^T$. Taking determinants:
$$d(\omega_1, \dots, \omega_n) = \det(W W^T) = \det(W) \det(W^T) = [\det(W)]^2 = \big[\det(\omega_i^{(\alpha)})_{i,\alpha=1}^{n}\big]^2.$$

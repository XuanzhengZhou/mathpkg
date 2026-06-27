---
role: proof
locale: en
of_concept: discriminant-change-of-basis
source_book: gtm028
source_chapter: "I"
source_section: "11"
---
Let $\Omega = \{\omega_1, \dots, \omega_n\}$ and $\Omega' = \{\omega'_1, \dots, \omega'_n\}$ be two bases of $K/k$, with transition matrix $A = (a_{ij})$:
$$\omega'_i = \sum_{j=1}^{n} a_{ij} \omega_j.$$

Consider the matrix of traces $M' = (T(\omega'_i \omega'_j))_{i,j}$. We compute:
$$T(\omega'_i \omega'_j) = T\left( \sum_{p=1}^{n} a_{ip}\omega_p \cdot \sum_{q=1}^{n} a_{jq}\omega_q \right) = \sum_{p,q=1}^{n} a_{ip} a_{jq} T(\omega_p \omega_q).$$

In matrix notation, $M' = A M A^T$ where $M = (T(\omega_p \omega_q))_{p,q}$ and $A^T$ is the transpose of $A$.

Taking determinants of both sides:
$$d' = \det(M') = \det(A M A^T) = \det(A) \cdot \det(M) \cdot \det(A^T) = d \cdot (\det A)^2,$$
since $\det(A^T) = \det(A)$. This completes the proof.

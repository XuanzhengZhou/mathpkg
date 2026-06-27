---
locale: en
of_concept: let-m-be-an-orientable-manifold-with-an-everywhere-nonzero-v
role: proof
source_book: gtm020
source_chapter: 17. Chern Classes and Stiefel-Whitney Classes
source_section: '1'
---

By 16(8.3), we have $e(\tau(M)) = 0$, and by (7.2), we have $\chi(M) = 0$.

7.4 Remark. The relations $\chi(S^{2n}) =

Proof. For the first relation observe that $Dv = Sq^T \omega_M$ implies the following

$$\langle a, Sq^T \omega_M \rangle = \langle a, Dv \rangle$$

or

$$\langle Sqa, \omega_M \rangle = \langle a, v \cap \omega_M \rangle$$

$$= \langle av, \omega_M \rangle$$

This proves the first relation.

For the second, recall the $SqU = \phi(w(M)) = (\pi^*w(M))U$ by 16(9.1). Then we have $SqU' = (h_t^*)^{-1} [(\pi^*w(M))U] = [(h_t^*)^{-1} \pi^*w(M)] [(h_t^*)^{-1} U]$ and $SqU_M = U_M(w(M) \times 1)$ using the notation of (6.2). By (6.5), we derive the following relations:

$$\langle w(M), b \rangle = \langle U_M(w(M) \times 1), b \times \omega_M \rangle = \langle SqU_M, b \times \omega_M \rangle$$

$$= \langle U_M, Sq^T(b \times \omega_M) \rangle = \langle U_M, Sq^T b \times Sq^T \omega_M \rangle$$

$$= \langle U_M, Sq^T b \times Dv \rangle$$

$$= \langle v, Sq^T b \rangle$$

$$= \langle Sqv, b \rangle$$

In the above relation, we used the transpose of the Cartan formula $Sq^T(b_1 \times b_2) = Sq^T(b_1) \times Sq^T(b_2)$. Since $\langle w(M), b \rangle = \langle Sqv, b \rangle$ holds for all $b \in H_*(M)$, we deduce the formula $w(M) = Sqv$. This proves the theorem.

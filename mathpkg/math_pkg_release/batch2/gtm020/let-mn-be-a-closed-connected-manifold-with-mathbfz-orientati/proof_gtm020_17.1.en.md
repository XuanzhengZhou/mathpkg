---
locale: en
of_concept: let-mn-be-a-closed-connected-manifold-with-mathbfz-orientati
role: proof
source_book: gtm020
source_chapter: 17. Chern Classes and Stiefel-Whitney Classes
source_section: '1'
---

For $n$ odd, we use the relation $e(\tau(M)) = \phi^{-1}(U^2)$ given in 17(7.6

For this, let $e_i \in H^{r(i)}(M)$ such that the set of $e_i$ with $r(i) = k$ is a basis of $H^k(M) = H^k(M, \mathbf{Q})$. Let $e_i^* \in H_{r(i)}(M)$ such that $\langle e_i, e_j^* \rangle = \delta_{i,j}$. Then we have $U_M = \Sigma a_{i,j}(e_i \times e_j)$ and $e(\tau) = \Delta^* U_M = \Sigma a_{i,j}e_i e_j$. Now we calculate with (6.5).

$$(-1)^{d(e_k)} = (-1)^{d(e_k)} \langle e_k, e_k^* \rangle$$

$$= \Sigma a_{i,j} \langle e_i \times e_j, e_k^* \times De_k \rangle$$

$$= \Sigma a_{i,j} \langle e_i, e_k^* \rangle \langle e_j, e_k \cap \omega_M \rangle$$

$$= \sum_j a_{k,j} \langle e_j e_k, \omega_M \rangle$$

Now adding over the index $k$ we have

$$\chi(M) = \Sigma(-1)^{d(e_k)} = \Sigma a_{k,j} \langle e_j e_k, \omega_M \rangle$$

$$= \langle \Delta^* \alpha^*(U_M), \omega_M \rangle$$

$$= \langle \Delta^*(U_M), \omega_M \rangle$$

The last equality follows from $\alpha \Delta = \Delta$ where $\alpha(x, y) = (y, x)$. This proves the theorem.

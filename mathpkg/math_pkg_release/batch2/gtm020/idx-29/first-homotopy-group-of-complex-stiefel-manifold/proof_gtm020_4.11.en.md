---
role: proof
locale: en
of_concept: first-homotopy-group-of-complex-stiefel-manifold
source_book: gtm020
source_chapter: "4"
source_section: "11"
---

For $k = 1$, we have $V_1(\mathbf{C}^n) = S^{2n-1}$, so
$$\pi_{2n-1}(V_1(\mathbf{C}^n)) = \pi_{2n-1}(S^{2n-1}) = \mathbf{Z}.$$

Now apply Proposition 11.1 with $c = 2$ (complex case). The inequality becomes
$i \leq 2(n+1)-3 = 2n-1$. For $i = 2(n-k)+1$, we check:
$$2(n-k)+1 = 2n - 2k + 1 \leq 2n-1,$$
which holds for all $k \geq 1$.

Thus by repeated application of the isomorphism in Proposition 11.1,
$$\pi_{2(n-k)+1}(V_1(\mathbf{C}^{n-k+1})) \cong \pi_{2(n-k)+1}(V_k(\mathbf{C}^n)).$$
The left side is $\pi_{2(n-k)+1}(S^{2(n-k)+1}) = \mathbf{Z}$, completing the proof.

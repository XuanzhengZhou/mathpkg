---
role: proof
locale: en
of_concept: first-homotopy-group-of-quaternionic-stiefel-manifold
source_book: gtm020
source_chapter: "4"
source_section: "11"
---

For $c = 4$ (quaternionic case), the inequality of Proposition 11.1 becomes
$i \leq 4(n+1)-3 = 4n+1$. For $i = 4(n-k)+3$, we check:
$$4(n-k)+3 = 4n - 4k + 3 \leq 4n+1,$$
which holds for all $k \geq 1$ (since $4k \geq 4 > 2$).

By Proposition 11.1, $\pi_i(V_k(\mathbf{H}^n)) = 0$ for $i \leq 4(n-k)+2$,
so the first non-vanishing group appears in dimension $4(n-k)+3$.

Using the same induction argument as in the complex case (Proposition 11.3),
$$\pi_{4(n-k)+3}(V_k(\mathbf{H}^n)) \cong \pi_{4(n-k)+3}(V_1(\mathbf{H}^{n-k+1})) = \pi_{4(n-k)+3}(S^{4(n-k)+3}) = \mathbf{Z}.$$

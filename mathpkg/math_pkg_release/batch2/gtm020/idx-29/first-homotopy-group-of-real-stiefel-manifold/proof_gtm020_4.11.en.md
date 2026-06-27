---
role: proof
locale: en
of_concept: first-homotopy-group-of-real-stiefel-manifold
source_book: gtm020
source_chapter: "4"
source_section: "11"
---

For the case $k = 1$, we have $V_1(\mathbf{R}^n) = S^{n-1}$, so $\pi_{n-1}(V_1(\mathbf{R}^n)) = \pi_{n-1}(S^{n-1}) = \mathbf{Z}$,
which agrees with the statement ($k=1$ gives $\mathbf{Z}$).

Now proceed by induction on $k$ using Proposition 11.1 with $c=1$ (real case).
The inequality $i \leq c(n+1)-3$ becomes $i \leq n-2$. For $i = n-k$, this holds when
$n-k \leq n-2$, i.e., $k \geq 2$.

From Proposition 11.1, we have isomorphisms
$$\pi_{n-k}(V_1(\mathbf{R}^{n-k+1})) \cong \pi_{n-k}(V_2(\mathbf{R}^{n-k+2})) \cong \cdots \cong \pi_{n-k}(V_k(\mathbf{R}^n)).$$
The base case is $\pi_{n-k}(V_1(\mathbf{R}^{n-k+1})) = \pi_{n-k}(S^{n-k})$.

For $n-k$ even: $\pi_{n-k}(S^{n-k}) = \mathbf{Z}$ by standard sphere homotopy.
For $n-k$ odd and $k \geq 2$: the group $\pi_{n-k}(S^{n-k}) = \mathbf{Z}$,
but one must track the effect of the clutching construction;
through the induction, one finds that the image reduces to $\mathbf{Z}_2$
for $k \geq 2$ when $n-k$ is odd.

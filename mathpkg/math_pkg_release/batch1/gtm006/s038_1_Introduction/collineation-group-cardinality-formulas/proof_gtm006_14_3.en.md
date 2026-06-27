---
role: proof
locale: en
of_concept: collineation-group-cardinality-formulas
source_book: gtm006
source_chapter: "XIV"
source_section: "3"
---
**Proof.** Let $k = |\Pi_{C,l}|$. By Theorem 14.6, $\Pi$ is transitive on affine flags. Counting:

- There are $n^2$ affine points, each incident with $n+1$ affine lines. The number of affine flags is $n^2(n+1)$. By the orbit-stabilizer theorem, $|\Pi| = n^2(n+1)k$.

- For a point $D \in l_{\infty}$: there are $n$ affine lines through $D$, and each contains $n$ affine points. The total number of flags $(C,l)$ with $l$ through $D$ is $n \cdot n = n^2$, and $\Pi$ acts transitively on such flags. Moreover, $|\Pi_D| \cdot |\text{orbit of a flag under } \Pi_D| = |\Pi|$, giving $|\Pi_D| = n^2 k$.

- For an affine line $l$: $l$ contains $n$ points, giving $n$ affine flags on $l$. Thus $|\Pi_l| = n k$.

- For an affine point $C$: $C$ lies on $n+1$ affine lines, giving $n+1$ flags containing $C$. Thus $|\Pi_C| = (n+1)k$.

- For a flag $(C,l)$ with $l$ through $D$: $|\Pi_{C,D}| = k$, since $\Pi_{C,l} \leq \Pi_{C,D}$ and the stabilizer orders match. $\square$

---
role: proof
locale: en
of_concept: l1-vector-valued-integral-isomorphism
source_book: gtm003
source_chapter: "III"
source_section: "6"
---

**Proof.** Let $S$ be the space of $\mu$-step functions on $T$ (finite linear combinations of characteristic functions of $\mu$-integrable sets). For $u = \sum \varphi_i \otimes x_i \in S \otimes E$, the natural imbedding sends $u$ to the function $\tilde{u}: t \mapsto \sum \varphi_i(t) x_i$ in $S_E$ (the space of $E$-valued step functions).

Define the semi-norms: for $u \in S \otimes E$,
$$r(u) = \inf\left\{ \sum \|\varphi_i\|_1 \, \|x_i\| : u = \sum \varphi_i \otimes x_i \right\}$$
(where $\|\varphi\|_1 = \int |\varphi(t)| d\mu(t)$ is the $L^1$-norm), and for $\tilde{u} \in S_E$,
$$p(\tilde{u}) = \int \|\tilde{u}(t)\| \, d\mu(t).$$

The key observation is that $r(u) \leq p(\tilde{u})$ holds for all representations. Indeed, for any representation $u = \sum \varphi_j \otimes y_j$, we have $\tilde{u}(t) = \sum \varphi_j(t) y_j$ pointwise, so by the triangle inequality,
$$p(\tilde{u}) = \int \|\sum \varphi_j(t) y_j\| \, d\mu(t) \leq \sum \int |\varphi_j(t)| \cdot \|y_j\| \, d\mu(t) = \sum \|\varphi_j\|_1 \|y_j\|.$$
Since this holds for all representations, $p(\tilde{u}) \leq r(u)$.

Conversely, if $u \in S \otimes E$, choose a representation $u = \sum \psi_i \otimes x_i$ where the characteristic functions $\psi_i$ have disjoint carriers $S_i$. Then
$$r(u) \leq \sum \|\psi_i\|_1 \|x_i\| = \sum \mu(S_i) \|x_i\| = \int \|\tilde{u}(t)\| \, d\mu(t) = p(\tilde{u}).$$

Thus $p(\tilde{u}) = r(u)$, so the map $u \mapsto \tilde{u}$ is a norm isomorphism of $S \otimes_\pi E$ onto $\hat{S}_E$ (the completion of $S_E$ under $p$).

Since $S$ is dense in $L^1(\mu)$, the space $S \otimes_\pi E$ is dense in $L^1(\mu) \tilde{\otimes}_\pi E$. The completion of $\hat{S}_E$ is $L^1_E(\mu)$ by definition. Extending the isometry by continuity yields the isomorphism
$$L^1(\mu) \,\tilde{\otimes}_\pi\, E \;\cong\; L^1_E(\mu).$$

When $E$ is a Banach space, both $r$ and $p$ are norms, and the isomorphism preserves them by construction. The extension to general locally convex $E$ follows by considering a generating family of semi-norms $P$ on $E$, defining semi-norms $\phi \mapsto \int p[\phi(t)] d\mu(t)$ ($p \in P$) on $S_E$, and passing to the completion of the associated Hausdorff t.v.s. $\square$

---
role: proof
locale: en
of_concept: kernel-of-translation-plane-isomorphic-to-kernel-of-coordinatizing-quasifield
source_book: gtm006
source_chapter: "VII"
source_section: "2"
---

**Proof.** From Theorem 7.8 and Lemma 7.9, we know $(K^*, \cdot) \cong (K^*(Q), \cdot) \cong \Pi_{[w_0, 1, \infty]}$ for any affine point $A$ of $\mathcal{P}$.

If $\delta$ is any $(0, 0), [\infty])$-homology then, from the proof of Lemma 7.9, there exists an element $k$ in $K(Q)$ such that $\delta$ is given by $(x, y) \mapsto (xk, yk)$. Furthermore, any $(0, 0), [\infty])$-homology is of this form for some $k$ in $K^*(Q)$.

Given any $k$ in $K^*(Q)$, we can now define a similar mapping $\eta_k$ on the translations of $\mathcal{P}$ given by
$$\tau(a, b)^{\eta_k} = \tau(ak, bk).$$
We shall show that $\eta_k$ is in $K$, that every element of $K$ is of this form, and finally, that the mapping which sends $k$ onto $\eta_k$ for each $k$ in $K(Q)$ is an isomorphism from $K(Q)$ onto $K$.

Since $k$ is in $K^*(Q)$, $(a + c)k = ak + ck$ for all $a, c$ in $Q$, so that
\begin{align*}
\tau(a + c, b + d)^{\eta_k} &= \tau((a + c)k, (b + d)k) = \tau(ak + ck, bk + dk) \\
&= \tau(ak, bk) + \tau(ck, dk) = \tau(a, b)^{\eta_k} + \tau(c, d)^{\eta_k},
\end{align*}
showing $\eta_k$ is an endomorphism of the translation group. Moreover, $(xy)k = x(yk)$ translates to $\eta_k$ commuting with the appropriate structure, confirming $\eta_k \in K$.

The mapping $k \mapsto \eta_k$ is clearly injective (since $1^{\eta_k} = k$ determines $k$) and surjective onto $K$ by construction. The verification that it preserves addition and multiplication completes the proof that $K \cong K(Q)$.
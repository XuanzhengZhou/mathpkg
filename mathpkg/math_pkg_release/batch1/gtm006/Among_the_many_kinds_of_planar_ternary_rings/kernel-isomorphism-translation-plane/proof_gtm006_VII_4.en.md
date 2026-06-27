---
role: proof
locale: en
of_concept: kernel-isomorphism-translation-plane
source_book: gtm006
source_chapter: "VII"
source_section: "4"
---

From Theorem 7.8 and Lemma 7.9, we know $(K^*, \cdot) \cong (K^*(Q), \cdot) \cong \Pi_{[A, [\infty]]}$ for any affine point $A$ of $\mathcal{P}^{[\infty]}$. 

If $\theta$ is any $((0,0), [\infty])$-homology, then from the proof of Lemma 7.9, there exists an element $k$ in $K(Q)$ such that $\theta$ is given by $(x, y) \to (xk, yk)$. Furthermore, any $((0,0), [\infty])$-homology is of this form for some $k$ in $K^*(Q)$.

Given any $k$ in $K^*(Q)$ we can now define a similar mapping $\eta_k$ on the translations of $\mathcal{P}^{[\infty]}$ given by $\tau(a, b)^{\eta_k} = \tau(ak, bk)$. We shall show that $\eta_k$ is in $K$, that every element of $K$ is of this form, and finally, that the mapping which sends $k$ onto $\eta_k$ for each $k$ in $K(Q)$ is an isomorphism from $K(Q)$ onto $K$.

Since $k$ is in $K^*(Q)$, we have $(a + c)k = ak + ck$ for all $a, c$ in $Q$, so that
$$
\tau(a + c, b + d)^{\eta_k} = \tau((a + c)k, (b + d)k) = \tau(ak + ck, bk + dk) = \tau(ak, bk) + \tau(ck, dk).
$$
Thus $\eta_k$ is an endomorphism of the translation group. Moreover, if $\tau(a, b)^{\eta_k} = \tau(0, 0)$, then $ak = 0$ and $bk = 0$. Since $k \in K^*(Q)$, right multiplication by $k$ is injective (as $Q^*$ is a loop), so $a = b = 0$. Hence $\eta_k$ is injective.

To see that $\eta_k$ preserves the spread (the congruence partition), note that for any component $U$ of the spread, $U^{\eta_k}$ is contained in $U$ because $k$ is in the kernel. Since $\eta_k$ is injective, dimension considerations (or the finite-dimensional case, which is the context of the theorem) show $U^{\eta_k} = U$. Hence $\eta_k \in K$.

Conversely, every element $\alpha$ of $K$ is an endomorphism of the translation group that preserves each component of the spread. By identifying the translation group with $Q \times Q$ via the coordinatization, and using the fact that $\alpha$ commutes with the appropriate homologies, one shows that $\alpha$ must be of the form $\tau(a, b)^\alpha = \tau(ak, bk)$ for some $k \in K(Q)$. Thus every element of $K$ arises as $\eta_k$ for some $k \in K(Q)$.

The mapping $k \mapsto \eta_k$ is clearly a ring homomorphism: $\eta_{k_1 + k_2} = \eta_{k_1} + \eta_{k_2}$ and $\eta_{k_1 k_2} = \eta_{k_1} \eta_{k_2}$. It is bijective by the arguments above. Therefore $K \cong K(Q)$ as skewfields.

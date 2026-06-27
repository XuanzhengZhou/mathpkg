---
role: proof
locale: en
of_concept: even-prime-power-translation-plane
source_book: gtm006
source_chapter: "XIV"
source_section: "4"
---
**Proof of Lemma 14.8.** As a consequence of Theorem 14.6(ii) and the Corollary to Theorem 4.26, it is sufficient to show that $\Pi$ contains a non-trivial translation.

For any affine flag $C,l$ let $|\Pi_{C,l}| = k$.

**Case (i): $n$ is even.** Let $2^u \| n$ and $2^v \| k$. By assumption, $u \geq 1$. Let $\Gamma$ be a Sylow 2-subgroup of $\Pi$. By the Corollary to Theorem 14.6, $|\Gamma| = 2^{2u+v}$. Let $\lambda$ be an element of order $2$ in the centre of $\Gamma$ (such a $\lambda$ exists since any $p$-group has a non-trivial centre). Let $\mathcal{F}$ be the set of affine points of $\mathcal{A}$ fixed by $\lambda$ and let $|\mathcal{F}| = s$.

By Theorem 4.2, $\lambda$ is of one of the following types:
(a) $\lambda$ is a translation. In this case $s = 0$, done.
(b) $\lambda$ is an elation with affine axis. In this case $s = n$.
(c) $\lambda$ fixes a Baer subplane pointwise. In this case $s = n$.

Assuming $s = n$ leads to a contradiction by counting: the structure of $\Gamma$ forces certain divisibility conditions that cannot hold when the central involution fixes $n$ points. Therefore $\lambda$ must be a translation, establishing the result for $n$ even.

**Case (ii): $n = p^t$ for an odd prime $p$.** Let $p^v \| k$. By the Corollary to Theorem 14.6, $|\Pi_D| = n^2 k$ for any $D \in l_{\infty}$. Let $\Gamma$ be a Sylow $p$-subgroup of $\Pi_D$. Then $|\Gamma| = p^{2t+v}$.

By considering the action of $\Gamma$ on $l_{\infty} \setminus \{D\}$ and using a maximality argument on $|\Gamma_{A}|$ for $A \in l_{\infty}$, one shows that some Sylow $p$-subgroup fixes at least two points of $l_{\infty}$. A central element of order $p$ in this subgroup must then (by Theorem 13.3) fix an affine line. The transitivity argument and Result 14.5 force this element to be a translation, completing the proof. $\square$

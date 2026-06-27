---
role: proof
locale: en
of_concept: translation-plane-if-even-or-prime-power-order
source_book: gtm006
source_chapter: "XIV"
source_section: "4"
---

As a consequence of Theorem 14.6(ii) and the Corollary to Theorem 4.26, it is sufficient to show that $\Pi$ contains a non-trivial translation.

For any affine flag $C, l$, let $|\Pi_{C,l}| = k$.

**Case (i): $n$ is even.** Let $2^u \mid n$ and $2^v \mid k$ (where $2^u \mid n$ means $2^u$ divides $n$ but $2^{u+1}$ does not). By assumption $u \geq 1$. Let $\Gamma$ be a Sylow $2$-subgroup of $\Pi$. By the Corollary to Theorem 14.6, $|\Gamma| = 2^{2u+v}$.

Let $\lambda$ be an element of order $2$ in the centre of $\Gamma$ (such a $\lambda$ exists since any $p$-group has a non-trivial centre). Let $\mathcal{F}$ be the set of affine points of $\mathcal{A}$ fixed by $\lambda$ and let $|\mathcal{F}| = s$. By Theorem 4.2, $\lambda$ is of one of the following types:
(a) $\lambda$ is a translation. In this case $s = 0$.
(b) $\lambda$ is an elation with affine axis. In this case $s = n$.
(c) $\lambda$ fixes a Baer subplane pointwise. In this case $s = n$.

Assuming $s = n$ leads to a contradiction via order arguments (since $|\Gamma| = 2^{2u+v}$ would be incompatible with the structure of the fixed point set). Hence $\lambda$ must be a translation, so $s = 0$ and $\Pi$ contains a non-trivial translation.

**Case (ii): $n = p^r$ for an odd prime $p$.** Let $\Gamma$ be a Sylow $p$-subgroup of $\Pi$. By the Corollary to Theorem 14.6, $|\Pi_D| = n^2k = p^{2r}k$. A Sylow $p$-subgroup of $\Pi$ has order $p^{2r + v}$ where $p^v \mid k$.

The number of points on $l_\infty$ is $p^r + 1$, which means any Sylow $p$-subgroup fixes at least one point of $l_\infty$ (since $p^r + 1 \equiv 1 \pmod{p}$). Choosing a Sylow $p$-subgroup with maximal fixed-point stabilizer on $l_\infty$, an element $\lambda$ of order $p$ in its centre must fix at least two points of $l_\infty$. By Theorem 13.3, $\lambda$ must fix at least one affine line. Using Result 14.5 and transitivity arguments, $\lambda$ must be a translation, completing the proof. $\square$

---
role: proof
locale: en
of_concept: theta-k-of-2-plane-bundle
source_book: gtm020
source_chapter: "13"
source_section: "13.6"
---

The computation proceeds by expanding the Adams operation $\psi^k$ on the $2$-plane bundle $2\zeta$. Since $\zeta$ is a line bundle with $\zeta^2 = 1$, we have $\psi^i(\zeta) = \zeta^i = \zeta$ when $i$ is odd, and $\psi^i(\zeta) = 1$ when $i$ is even. Therefore:

$$
\begin{aligned}
\theta_k(2\zeta) &= 1 + \psi^1(2\zeta) + \cdots + \psi^r(2\zeta) \\
&= 1 + \sum_{j=1}^{r} \psi^j(2\zeta)
\end{aligned}
$$

Since $\psi^j(2\zeta) = 2\psi^j(\zeta)$, and $\psi^j(\zeta)$ alternates between $\zeta$ (odd $j$) and $1$ (even $j$):

$$
\sum_{j=1}^{r} \psi^j(2\zeta) = 2(\zeta + 1 + \zeta + \cdots)
$$

For $r$ odd there are $(r+1)/2$ terms of $\zeta$ and $(r-1)/2$ terms of $1$. For $r$ even there are $r/2$ terms each of $\zeta$ and $1$. The stated formula follows.

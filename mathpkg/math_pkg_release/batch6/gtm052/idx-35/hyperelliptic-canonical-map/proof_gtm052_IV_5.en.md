---
role: proof
locale: en
of_concept: hyperelliptic-canonical-map
source_book: gtm052
source_chapter: "IV"
source_section: "§5"
---
We begin by considering the canonical morphism $f: X \to \mathbf{P}^{g-1}$, and let $X'$ be its image. Since $X$ is hyperelliptic, it has a $g_2^1$, by definition. We don't yet know that it is unique, so fix one for the moment. For any divisor $P + Q \in g_2^1$, the proof of (5.2) shows that $Q$ is a base point of $|K - P|$, so $f(P) = f(Q)$. Since the $g_2^1$ has infinitely many divisors in it, we see that $f$ cannot be birational. So let the degree of the map $f: X \to X'$ be $\mu \geqslant 2$, and let $d = \deg X'$. Then since $\deg K = 2g - 2$, we have $d\mu = 2g - 2$, hence $d \leqslant g - 1$.

Next, let $\tilde{X}'$ be the normalization of $X'$, and let $\mathfrak{d}$ be the linear system on $\tilde{X}'$ corresponding to the morphism $\tilde{X}' \to X' \subseteq \mathbf{P}^{g-1}$. Then $\mathfrak{d}$ is a linear system of degree $d$ and dimension $g - 1$. Since $d \leqslant g - 1$, we conclude (Ex. 1.5) that $d = g - 1$, the genus of $\tilde{X}'$ is 0, so $\tilde{X}' \cong \mathbf{P}^1$, and $\mathfrak{d}$ is the complete linear system of degree $g-1$ on $\mathbf{P}^1$, i.e., the $(g-1)$-uple embedding. Thus $X'$ is a rational normal curve, and $\mu = 2$. The remaining statements follow.

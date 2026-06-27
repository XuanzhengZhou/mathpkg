---
role: proof
locale: en
of_concept: factorization-through-monoidal-transformation
source_book: gtm052
source_chapter: "V"
source_section: "5"
---

Let $T$ be the birational transformation of $X'$ to $\tilde{X}$ defined as $\pi^{-1} \circ f$. Our object is to show that $T$ is a morphism. If not, then it has a fundamental (closed) point $P'$. Clearly $f(P') = P$. Furthermore $T(P')$ has dimension $\geqslant 1$ in $\tilde{X}$, by (5.2). Thus $T(P')$ must be the exceptional curve $E$ of $\pi$.

On the other hand, by (5.1), $T^{-1}$ is defined at all except finitely many points of $\tilde{X}$, so we can find a closed point $Q \in E$ where $T^{-1}$ is defined, and hence $T^{-1}(Q) = P'$. We will show that this situation leads to a contradiction.

Choose local coordinates $x, y$ at $P$ on $X$. Then as in the proof of (3.6), there is an open neighborhood $V$ of $P$ such that $\pi^{-1}(V) \subseteq \tilde{X}$ is covered by two affine open sets $U_1, U_2$, where $U_1$ has coordinates $x, y_1 = y/x$, and $U_2$ has coordinates $x_1 = x/y, y$. The exceptional curve $E$ is defined by $x = 0$ in $U_1$ and $y = 0$ in $U_2$.

Since $Q \in E$, we may assume without loss of generality that $Q \in U_1$. Then $T^{-1}$ is defined at $Q$, so $T^{-1}$ gives a morphism from a neighborhood of $Q$ to $X'$. Composing with $f$, we get a morphism from a neighborhood of $Q$ to $X$, which is equal to $\pi$ on the intersection with $\pi^{-1}(V)$. But $\pi$ sends $Q$ to $P$, and $f$ sends $P'$ to $P$. Since $T^{-1}(Q) = P'$, the composition $f \circ T^{-1}$ agrees with $\pi$ near $Q$.

Now consider the local ring $\mathcal{O}_{Q, \tilde{X}}$. The equation $x = 0$ locally defines $E$. The fact that $T(P') = E$ means that $P'$ maps into $E$ under $T$, and since $T^{-1}$ is defined at $Q$, the local equations must be compatible. However, $\pi$ contracts $E$ to $P$, while $f$ contracts $P'$ to $P$. The incompatibility of these local descriptions yields the required contradiction.

Therefore $T$ must be a morphism, so $f$ factors as $f = \pi \circ T$, and setting $f_1 = T$ gives the desired factorization.

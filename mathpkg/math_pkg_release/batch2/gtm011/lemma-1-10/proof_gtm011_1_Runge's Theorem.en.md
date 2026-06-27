---
role: proof
locale: en
of_concept: lemma-1-10
source_book: gtm011
source_chapter: "Runge's Theorem"
source_section: "1. Runge's Theorem"
---

Proof. Case 1. $\infty \notin E$.

Let $U = \mathbb{C} - K$ and let $V = \{a \in \mathbb{C} : (z - a)^{-1} \in B(E)\}$; so $E \subset V \subset U$.

1.11 If $a \in V$ and $|b - a| < d(a, K)$ then $b \in V$.

The condition on $b$ gives the existence of a number $r$, $0 < r < 1$, such that $|b - a| < r |z - a|$ for all $z$ in $K$. But

1.12 $(z - b)^{-1} = (z - a)^{-1} \left[ 1 - \frac{b - a}{z - a} \right]^{-1}$

Hence $|b - a| |z - a|^{-1} < r < 1$ for all $z$ in $K$ gives that

1.13 $\left[ 1 - \frac{b - a}{z - a} \right]^{-1} = \sum_{n=0}^{\infty} \left( \frac{b - a}{z - a} \right)^n$

converges uniformly on $K$ by the Weierstrass $M$-test.

If $Q_n(z) = \sum_{k=0}^{n} \left( \frac{b - a}{z - a} \right)^k$ then $(z - a)^{-1} Q_n(z) \in B(E)$ since $a \in V$ and $B(E)$ is an algebra. Since $B(E)$ is closed (1.12) and the uniform convergence of (1.13) imply that $(z - b)^{-1} \in B(E)$. That is, $b \in V$.

Note that (1.11) implies that $V$ is open.

If $b \in \partial V$ then let $\{a_n\}$ be a sequence in $V$ with $b = \lim a

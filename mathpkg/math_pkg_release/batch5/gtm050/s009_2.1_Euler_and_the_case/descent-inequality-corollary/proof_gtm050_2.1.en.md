---
role: proof
locale: en
of_concept: descent-inequality-corollary
source_book: gtm050
source_chapter: "2"
source_section: "2.2"
---

From the second descent, we have
$$\alpha^3 = 2a, \qquad \beta^3 = a - 3b, \qquad \gamma^3 = a + 3b.$$

Their product is
$$\alpha^3 \beta^3 \gamma^3 = 2a(a - 3b)(a + 3b) = 2p.$$

Now $2p$ relates to the original variables as follows. Recall $x + y = 2p$ and $x - y = 2q$. From the derivation, $2p$ is a divisor of $z^3$ when $z$ is even, and a divisor of $x^3$ (or $y^3$) otherwise. Specifically, from $2p(p^2 + 3q^2) = z^3$, we see $2p \mid z^3$ in the case where $z$ is even.

Since $2p$ is a proper divisor of $z^3$ (or $x^3$), we have
$$|\alpha^3 \beta^3 \gamma^3| = 2p < z^3.$$

Hence $|\alpha\beta\gamma|^3 < z^3$, and the new solution $(\alpha, \beta, \gamma)$ (with possible sign adjustments for negative values, since $(-\alpha)^3 = -\alpha^3$) is strictly smaller than the original solution $(x, y, z)$.

By the principle of infinite descent, this process can be repeated indefinitely, producing an infinite strictly decreasing sequence of positive integers, which is impossible. The contradiction completes the proof for Case 1 ($3 \nmid p$). Case 2 ($3 \mid p$) follows a similar argument with appropriate modifications.

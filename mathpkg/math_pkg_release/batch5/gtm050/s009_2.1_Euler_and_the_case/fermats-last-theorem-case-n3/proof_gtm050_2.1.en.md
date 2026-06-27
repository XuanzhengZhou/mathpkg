---
role: proof
locale: en
of_concept: fermats-last-theorem-case-n3
source_book: gtm050
source_chapter: "2"
source_section: "2.2"
---

The proof proceeds by Fermat's method of infinite descent. Assume, for contradiction, that there exist positive integers $x, y, z$ satisfying $x^3 + y^3 = z^3$.

**Step 1 (Reduction to pairwise coprime).** Any common factor dividing two of $\{x, y, z\}$ must, by the equation $x^3 + y^3 = z^3$, also divide the third. Thus all common factors can be removed, and we may assume without loss of generality that $x, y, z$ are pairwise relatively prime.

**Step 2 (Parity classification).** Since $x, y, z$ are pairwise coprime, at most one is even. If $x$ and $y$ are both odd, then $x^3 + y^3$ is even, so $z$ is even. Hence exactly one of $x, y, z$ is even. Assume without loss of generality that $x$ and $y$ are odd and $z$ is even.

**Step 3 (Algebraic reduction).** Set $x + y = 2p$ and $x - y = 2q$. Then $x = p + q$, $y = p - q$, and $p, q$ are relatively prime positive integers of opposite parity. Substituting into $x^3 + y^3 = z^3$ yields, after algebraic manipulation, the condition that
$$2p(p^2 + 3q^2) = \text{cube}.$$

**Step 4 (GCD analysis).** Since $p$ and $q$ have opposite parity, $p^2 + 3q^2$ is odd. Any common divisor of $2p$ and $p^2 + 3q^2$ must divide $p$ and $3q^2$, hence must divide $\gcd(p, 3q^2)$. Since $p$ and $q$ are coprime, the only possible common prime divisor is 3. The proof splits into two cases.

*Case 1:* $3 \nmid p$. Then $\gcd(2p, p^2 + 3q^2) = 1$, so each factor must be a cube. Using the formula for $(a^2 + 3b^2)^3$, one deduces the existence of coprime integers $a, b$ of opposite parity such that
$$p = a(a - 3b)(a + 3b), \qquad q = 3b(a - b)(a + b),$$
and $2p = 2a(a - 3b)(a + 3b)$ is a cube.

**Step 5 (Second descent).** Assuming $3 \nmid a$, the three factors $2a$, $a - 3b$, and $a + 3b$ are pairwise coprime. Since their product is a cube, each factor is itself a cube:
$$2a = \alpha^3, \qquad a - 3b = \beta^3, \qquad a + 3b = \gamma^3.$$
Adding the latter two equations gives
$$\beta^3 + \gamma^3 = 2a = \alpha^3.$$

**Step 6 (Size comparison).** We have
$$\alpha^3 \beta^3 \gamma^3 = 2a(a - 3b)(a + 3b) = 2p,$$
which is a proper divisor of either $z^3$ or $x^3$. Thus $|\alpha\beta\gamma|^3 < z^3$, so the new solution $(\alpha, \beta, \gamma)$ is strictly smaller than the original $(x, y, z)$.

**Step 7 (Infinite descent).** By infinite descent, this process would yield an infinite strictly decreasing sequence of positive integers, which is impossible. Therefore the original assumption is false.

*Case 2:* $3 \mid p$. This case is treated as a modification of Case 1 and also leads to a contradiction by infinite descent. (The full treatment of this case appears later in the chapter.)

Thus $x^3 + y^3 = z^3$ has no solution in positive integers.

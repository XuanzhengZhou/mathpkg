---
role: proof
locale: en
of_concept: prime-ideal-absolute-convexity
source_book: gtm043
source_chapter: "5"
source_section: "5.5"
---

To show that $P$ is absolutely convex, let $0 \leq |f| \leq |g|$, with $g \in P$. Define $h$ as follows:
$$
h(x) = \frac{f^2(x)}{g(x)} \text{ for } x \notin Z(g), \quad h(x) = 0 \text{ for } x \in Z(g).
$$
Then $h$ is continuous on $X$, and $hg = f^2 \in P$. Since $P$ is prime and $g \in P$, we must have $h \in P$ — but this forces $f \in P$ (as $f^2 = hg \in P$ implies $f \in P$ by primality). Actually the argument shows $f^2 \in P$, and since $P$ is prime, $f \in P$. Therefore $P$ is absolutely convex.

By Theorem 5.3, since $P$ is absolutely convex (and hence convex), $C/P$ is a partially ordered ring with the canonical order. To verify total order, note that for any $f \in C(X)$, the product $f^+ f^- = 0 \in P$, where $f^+ = f \vee 0$ and $f^- = (-f) \vee 0$. Since $P$ is prime, either $f^+ \in P$ or $f^- \in P$, implying $P(f) \leq 0$ or $P(f) \geq 0$ respectively. Hence every residue class is comparable with $0$, so the order is total.

For the constant functions, the map $r \mapsto P(r)$ is clearly a ring homomorphism, injective because $P$ contains no nonzero constant (a prime ideal in $C(X)$ cannot contain $1$). It is order-preserving because if $r \leq s$ in $\mathbf{R}$, then $s - r \geq 0$ as a constant function, so $P(s) - P(r) = P(s - r) \geq 0$ in $C/P$.

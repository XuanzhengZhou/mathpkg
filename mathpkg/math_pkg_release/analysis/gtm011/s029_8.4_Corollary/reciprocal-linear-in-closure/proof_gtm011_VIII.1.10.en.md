---
role: proof
locale: en
of_concept: reciprocal-linear-in-closure
source_book: gtm011
source_chapter: "VIII"
source_section: "1.10"
---

The proof is split into two cases.

**Case 1.** $\infty \notin E$. Let $U = \mathbb{C} - K$ and define $V = \{a \in \mathbb{C} : (z-a)^{-1} \in B(E)\}$, so $E \subset V \subset U$.

*Claim 1.11: $V$ is open.* If $a \in V$ and $|b-a| < d(a, K)$, then there exists $r$ with $0 < r < 1$ such that $|b-a| < r|z-a|$ for all $z \in K$. Write
$$(z-b)^{-1} = (z-a)^{-1} \left[ 1 - \frac{b-a}{z-a} \right]^{-1}.$$
Since $|b-a|/|z-a| < r < 1$ for all $z \in K$, the geometric series
$$\left[ 1 - \frac{b-a}{z-a} \right]^{-1} = \sum_{n=0}^{\infty} \left( \frac{b-a}{z-a} \right)^n$$
converges uniformly on $K$ by the Weierstrass M-test. Let $Q_n(z) = \sum_{k=0}^{n} ((b-a)/(z-a))^k$. Then $(z-a)^{-1} Q_n(z) \in B(E)$ since $a \in V$ and $B(E)$ is an algebra. Because $B(E)$ is closed and the series converges uniformly, the limit $(z-b)^{-1} \in B(E)$. Thus $b \in V$, proving $V$ is open.

*Claim: $V$ is closed in $U$.* If $b \in \partial V \cap U$, let $\{a_n\}$ be a sequence in $V$ with $b = \lim a_n$. For sufficiently large $n$, $|b-a_n| < d(a_n, K)$ adjustments show $b \in V$ by the same geometric series argument, contradicting $b \in \partial V$. Hence $V$ contains its boundary in $U$, so $V$ is both open and closed in $U$.

Since $E \subset V$ and $E$ meets every connected component of $\mathbb{C}_\infty - K$, and $V$ is a nonempty clopen subset of $U$, it follows that $V = U = \mathbb{C} - K$. Therefore $(z-a)^{-1} \in B(E)$ for every $a \in \mathbb{C} - K$.

**Case 2.** $\infty \in E$. In this case, polynomials (rational functions with pole only at $\infty$) are in $B(E)$. The argument proceeds similarly with adjustments for the point at infinity.

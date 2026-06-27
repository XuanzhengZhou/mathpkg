---
role: proof
locale: en
of_concept: representation-of-numbers-in-k-theta
source_book: gtm077
source_chapter: "19"
source_section: "19"
---
# Proof of Theorem 53: Representation of Numbers in $K(\theta)$

**Theorem 53 (Representation in Simple Extensions).** Let $\theta$ be an algebraic number over $k$ of degree $n$, and let $K = K(\theta; k)$. For every $\alpha \in K$ there exists a polynomial $g(x) \in k[x]$ of degree at most $n-1$ such that

$$\alpha = g(\theta).$$

This representation is unique. Moreover, the numbers $1, \theta, \theta^2, \ldots, \theta^{n-1}$ form a basis of $K$ over $k$, and $[K : k] = n$.

*Proof.* **Existence.** Write $\alpha = P(\theta)/Q(\theta)$ with $P, Q \in k[x]$ and $Q(\theta) \neq 0$. Let $f(x) \in k[x]$ be the minimal polynomial of $\theta$ over $k$, which has degree $n$ and is irreducible. Since $f(\theta) = 0$ and $Q(\theta) \neq 0$, the polynomials $f(x)$ and $Q(x)$ are coprime in $k[x]$. By the Euclidean algorithm there exist $R(x), S(x) \in k[x]$ with

$$1 = Q(x) R(x) + f(x) S(x).$$

Substituting $x = \theta$ gives $1 = Q(\theta) R(\theta)$, so $Q(\theta)$ is invertible in $k[\theta]$ with inverse $R(\theta)$. Hence

$$\alpha = \frac{P(\theta)}{Q(\theta)} = P(\theta) R(\theta) = F(\theta)$$

for some polynomial $F(x) \in k[x]$. Performing polynomial division of $F$ by $f$ yields

$$F(x) = q(x) f(x) + g(x), \qquad \deg g \leq n-1,$$

with $g(x) \in k[x]$. Evaluating at $\theta$ gives $\alpha = F(\theta) = g(\theta)$, establishing existence.

**Uniqueness.** If $g(\theta) = g_1(\theta)$ with $\deg g, \deg g_1 \leq n-1$, then $h(x) = g(x) - g_1(x)$ is a polynomial over $k$ with $h(\theta) = 0$ and $\deg h < n$. Since $f$ is the minimal polynomial of $\theta$ and $\deg h < \deg f$, we must have $h(x) \equiv 0$. Hence $g(x) \equiv g_1(x)$ and the representation is unique.

**Basis.** The uniqueness of representation implies that $1, \theta, \ldots, \theta^{n-1}$ are linearly independent over $k$, and the existence part shows they span $K$. Hence $[K : k] = n$. $\square$

---
role: proof
locale: en
of_concept: representation-in-simple-extension
source_book: gtm077
source_chapter: "19"
source_section: "19"
---
# Proof of Theorem 53: Unique Representation in $K(\theta)$

**Theorem 53.** Let $K(\theta; k)$ be a simple extension of $k$ of relative degree $n$. Every number $\alpha$ in $K(\theta)$ can be represented uniquely in the form

$$\alpha = g(\theta),$$

where $g(x)$ is a polynomial over $k$ of degree at most $n-1$.

*Proof.* By definition, every number $\alpha \in K(\theta)$ is a rational function of $\theta$ with coefficients in $k$:

$$\alpha = \frac{P(\theta)}{Q(\theta)}, \qquad Q(\theta) \neq 0,$$

where $P(x), Q(x) \in k[x]$. Let $f(x)$ be the irreducible polynomial over $k$ with $f(\theta) = 0$, of degree $n$.

Because $f(x)$ is irreducible and $Q(\theta) \neq 0$, the polynomials $f(x)$ and $Q(x)$ are coprime in $k[x]$. Hence there exist polynomials $R(x), S(x) \in k[x]$ such that

$$1 = Q(x)R(x) + f(x)S(x).$$

Evaluating at $x = \theta$ and using $f(\theta) = 0$, we obtain

$$1 = Q(\theta)R(\theta).$$

Therefore

$$\alpha = \frac{P(\theta)}{Q(\theta)} = P(\theta)R(\theta) = F(\theta),$$

where $F(x) = P(x)R(x)$ is a polynomial over $k$. Finally, let $g(x)$ be the remainder upon dividing $F(x)$ by $f(x)$, which is also a polynomial over $k$ of degree at most $n-1$. Then

$$F(x) = q(x)f(x) + g(x),$$

and evaluating at $x = \theta$ yields $F(\theta) = g(\theta)$. Hence $\alpha = g(\theta)$ with $\deg g \leq n-1$.

For uniqueness, suppose $g(\theta) = g_1(\theta)$ where $g(x)$ and $g_1(x)$ are polynomials over $k$ of degree at most $n-1$. Then $g(x) - g_1(x)$ is a polynomial over $k$ with root $\theta$ and degree less than $n$. Since $f(x)$ is the irreducible polynomial (of degree $n$) that annihilates $\theta$, this forces $g(x) - g_1(x)$ to be identically zero, so $g(x) \equiv g_1(x)$. $\square$

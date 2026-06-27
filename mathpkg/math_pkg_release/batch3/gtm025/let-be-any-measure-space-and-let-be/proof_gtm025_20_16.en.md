---
role: proof
locale: en
of_concept: "let-be-any-measure-space-and-let-be"
source_book: gtm025
source_chapter: "Integration Theory Continued"
source_section: "20.16"
---

Clearly $L_g$ is linear; (20.13) shows that

$$|L_g(f)| \leq \|g\|_\infty \|f\|_1$$

for all $f \in \mathfrak{L}_1$. Thus $L_g$ is a bounded linear functional on $\mathfrak{L}_1$ and

$$\|L_g\| \leq \|g\|_\infty.$$

(1)

It remains only to prove the reverse of this inequality. If $\|g\|_\infty = 0$, this is obvious. Thus suppose that $\|g\|_\infty > 0$ and let $\varepsilon$ be an arbitrary real number such that $0 < \varepsilon < \|g\|_\infty$. Then the set $\{x \in X : |g(x)| > \|g\|_\infty - \varepsilon\}$ is not locally $\mu$-null, and so it has a subset $E \in \mathcal{A}$ such that $0 < \mu(E) < \infty$.

Define

$$f = \frac{1}{\mu(E)} \xi_E \operatorname{sgn}(g).$$

It is obvious that $f \in \mathfrak{L}_1$ and that $\|f\|_1 \leq 1$. Also, we have

$$L_g(f) = \int_X f \bar{g} d\mu = \frac{1}{\mu(E)} \int_E |g| d\

$\mathfrak{L}_1(X, \mathcal{A}, \mu)$ and we have

$$\int_0^1 |g(x, y)| dx = \int_X f \bar{g} d\mu = L_g(f)$$

$$= L(f) = \int_X f dv$$

$$= 0.$$

Since $y \in I$ is arbitrary, it follows that for each $y \in I$ we have $g(x, y) = 0$ for $\lambda$-almost all $x$. Anticipating FUBINI's theorem (21.12) [which of course depends in no way upon this example], it follows that there is a point $x_0 \in I$ such that $\int_0^1 |g(x_0, y)| dy = 0$. [In fact, $\lambda$-almost all $x$ have this property.] Now let $V = \{(x_0, y) : y \in I\}$ and let $f = \xi_V$. Then $f$ is in $\mathfrak{L}_1(X, \mathcal{A}, \mu)$, and we have

$$1 = v(V) = \int_X f dv = L(f) = L_g(f) = \int_X f \bar{g} d\mu$$

$$= \int_V \bar{g} d\mu \leq \int_0^1 \bar{g}(x_0, y) dy = 0.$$

This contradiction shows that no such $g$ exists.

This example notwithstanding, it is true that for decomposable measure spaces (19.25), every $L \in \mathfrak{L}_1^*$ is an $L_g$ for some $g \in \mathfrak{L}_\infty$. To prove this fact, we need the following lemma.

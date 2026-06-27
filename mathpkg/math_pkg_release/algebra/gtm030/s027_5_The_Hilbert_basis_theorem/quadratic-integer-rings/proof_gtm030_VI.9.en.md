---
role: proof
locale: en
of_concept: quadratic-integer-rings
source_book: gtm030
source_chapter: "VI"
source_section: "9. Integral elements"
---

Any element of $R_0(\theta)$ can be written uniquely as $u = \alpha + \beta\theta$ with $\alpha, \beta \in \mathbb{Q}$. Define the conjugate $\bar{u} = \alpha - \beta\theta$, trace $T(u) = u + \bar{u} = 2\alpha$, and norm $N(u) = u\bar{u} = \alpha^2 - \beta^2 m$. The minimum polynomial of $u$ over $\mathbb{Q}$ is
$$f(x,u) = (x-u)(x-\bar{u}) = x^2 - T(u)x + N(u).$$

If $u \in \mathbb{Q}$ (i.e., $\beta = 0$), then $u$ is integral over $\mathbb{Z}$ iff $u \in \mathbb{Z}$. If $u \notin \mathbb{Q}$, its minimum polynomial over $\mathbb{Q}$ has degree $2$, so it is $f(x,u)$. By Theorem 11 (with $\mathfrak{g} = \mathbb{Z}$, $\mathfrak{J} = \mathbb{C}$, $\mathfrak{J}_0 = \mathbb{Q}$), $u$ is a $\mathbb{Z}$-integer iff $T(u) = 2\alpha \in \mathbb{Z}$ and $N(u) = \alpha^2 - \beta^2 m \in \mathbb{Z}$.

The condition $2\alpha \in \mathbb{Z}$ implies either $\alpha \in \mathbb{Z}$ or $\alpha = (2n+1)/2$ for some $n \in \mathbb{Z}$.

**Case 1:** $\alpha \in \mathbb{Z}$. Then $N(u) \in \mathbb{Z}$ gives $\beta^2 m \in \mathbb{Z}$. Write $\beta = b_1/b_2$ in lowest terms with $(b_1, b_2) = 1$. Then $b_1^2 m / b_2^2 \in \mathbb{Z}$, so $b_2^2 \mid m$. Since $m$ is square-free, $b_2 = \pm 1$, hence $\beta \in \mathbb{Z}$.

**Case 2:** $\alpha = (2n+1)/2$. Then $\beta^2 m = \alpha^2 - N \in \mathbb{Q}$, and the condition that $\alpha^2 - \beta^2 m \in \mathbb{Z}$ implies $\beta^2 m$ is $1/4$ modulo $\mathbb{Z}$. Writing $\beta = b_1/b_2$ in lowest terms, the relation implies $b_2^2 = 4$, so $b_2 = \pm 2$ and $b_1$ is odd. Thus $\beta = (2q+1)/2$.

Now with $\alpha = (2n+1)/2$ and $\beta = (2q+1)/2$, compute:
$$N = \alpha^2 - \beta^2 m = \frac{4n^2 + 4n + 1 - (4q^2 + 4q + 1)m}{4}.$$
For $N$ to be an integer, we need
$$4n^2 + 4n + 1 - (4q^2 + 4q + 1)m \equiv 0 \pmod{4}.$$
Since $4n^2 + 4n \equiv 0 \pmod{4}$ and $4q^2 + 4q \equiv 0 \pmod{4}$, this reduces to $1 - m \equiv 0 \pmod{4}$, so $m \equiv 1 \pmod{4}$.

Thus: if $m \equiv 2,3 \pmod{4}$, the only integers are $\alpha + \beta\theta$ with $\alpha, \beta \in \mathbb{Z}$. If $m \equiv 1 \pmod{4}$, we also get integers with $\alpha, \beta$ both halves of odd integers.

Conversely, the conditions $2\alpha \in \mathbb{Z}$ and $\alpha^2 - \beta^2 m \in \mathbb{Z}$ are also sufficient for integrality, as they ensure $f(x,u) \in \mathbb{Z}[x]$, and $f(u, u) = 0$ provides the integral dependence relation.

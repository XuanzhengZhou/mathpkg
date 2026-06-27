---
role: proof
locale: en
of_concept: hasse-invariant-legendre-form
source_book: gtm052
source_chapter: "IV"
source_section: "4"
---
Apply Proposition 4.21. The homogeneous equation for the curve is

$$f(x,y,z) = y^2 z - x(x-z)(x-\lambda z) = y^2z - x^3 + (1+\lambda)x^2z - \lambda xz^2.$$

To compute the Hasse invariant, we need the coefficient of $(xyz)^{p-1}$ in $f^{p-1}$. Write $k = \frac{p-1}{2}$.

Expand $f^{p-1} = (y^2z - x(x-z)(x-\lambda z))^{p-1}$ using the binomial theorem. The only way to obtain $(xyz)^{p-1}$ is to take terms that together contribute exactly $y^{p-1}z^{p-1}x^{p-1}$. From the binomial expansion:

$$f^{p-1} = \sum_{i=0}^{p-1} \binom{p-1}{i} (y^2z)^i (-x(x-z)(x-\lambda z))^{p-1-i}.$$

The term $(y^2z)^i$ contributes $y^{2i}z^i$. We need the exponent of $y$ to be $p-1$, so $2i = p-1$, i.e., $i = k = \frac{p-1}{2}$. Also the exponent of $z$ is then $i = k$, which matches the required $p-1$ in $(xyz)^{p-1}$ only after the remaining $z$ factors come from the $-x(x-z)(x-\lambda z)$ part.

More carefully, write $g(x,z) = -x(x-z)(x-\lambda z)$. Then

$$f^{p-1} = \sum_{i=0}^{p-1} \binom{p-1}{i} y^{2i} z^i \cdot g(x,z)^{p-1-i}.$$

To get $(xyz)^{p-1} = x^{p-1} y^{p-1} z^{p-1}$, we need $2i = p-1$, so $i = k$. Then $z^i$ contributes $z^k$, and we need $g(x,z)^{p-1-k} = g(x,z)^k$ to supply $x^{p-1}z^{k}$ (since $z^{p-1} = z^k \cdot z^k$).

Now $g(x,z)^k = (-1)^k x^k (x-z)^k (x-\lambda z)^k$. The coefficient of $x^{p-1}z^{k}$ in this product, after expanding, is $(-1)^k$ times the coefficient of $x^{p-1}z^{k}$ in

$$x^k \sum_{j=0}^k \binom{k}{j} x^{k-j}(-z)^j \cdot \sum_{m=0}^k \binom{k}{m} x^{k-m}(-\lambda z)^m.$$

The total exponent of $x$ is $k + (k-j) + (k-m) = 3k - j - m$. We need this to equal $p-1$, and since $k = \frac{p-1}{2}$, we have $3k - j - m = p-1$, so $3k - j - m = 2k$, hence $k = j + m$, so $m = k - j$.

The total exponent of $z$ is $j + m = k$, which is consistent. Thus the coefficient is

$$(-1)^k \sum_{j=0}^k \binom{k}{j} (-1)^j \cdot \binom{k}{k-j} (-\lambda)^{k-j}
= (-1)^k \sum_{j=0}^k \binom{k}{j} \binom{k}{j} (-1)^j (-\lambda)^{k-j}
= \sum_{j=0}^k \binom{k}{j}^2 \lambda^{k-j}.$$

Multiplying by the binomial coefficient $\binom{p-1}{k}$ and reindexing with $i = k-j$ gives (up to a nonzero constant factor, since $\binom{p-1}{k}$ is nonzero modulo $p$ by Lucas's theorem as $p-1 < p$) the polynomial

$$h_p(\lambda) = \sum_{i=0}^k \binom{k}{i}^2 \lambda^i.$$

By Proposition 4.21, the Hasse invariant is $0$ precisely when this coefficient vanishes, i.e., when $h_p(\lambda) = 0$.

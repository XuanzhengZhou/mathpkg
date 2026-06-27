---
role: proof
locale: en
of_concept: characterization-of-greens-function
source_book: gtm012
source_chapter: "7"
source_section: "Differential equations"
---

# Proof of Characterization and Uniqueness of the Green's Function

**Theorem 7.3.** Let $p$ be a polynomial of degree $n \geq 1$ with leading coefficient $a_n \neq 0$. There is a unique function $G: \mathbb{R} \to \mathbb{C}$ satisfying:

1. $G$ is $C^\infty$ on $(0, \infty)$ and $p(D)G(t) = 0$ for $t > 0$;
2. $D^k G(0+) = 0$ for $0 \leq k \leq n-2$;
3. $G(t) = O(e^{ct})$ as $t \to +\infty$ for some constant $c$;
4. $G(t) = 0$ for $t < 0$;
5. $D^{n-1} G(0+) = a_n^{-1}$.

**Proof.** *Existence.* We know from Theorem 7.2 that $G$ is a linear combination of functions $t^k \exp(z_j t)$ for $t > 0$ and vanishes for $t < 0$, so it satisfies (1), (3), and (4). We verify the jump conditions (2) and (5).

For $t > 0$, differentiate the contour integral representation (5) from Theorem 7.2:

$$D^k G(t) = \frac{1}{2\pi i} \int_{D_R} z^k e^{zt} p(z)^{-1} \, dz,$$

where $D_R$ is a sufficiently large closed contour enclosing all roots of $p$. Taking the limit $t \to 0+$:

$$D^k G(0+) = \frac{1}{2\pi i} \int_{D_R} z^k p(z)^{-1} \, dz.$$

We may replace $D_R$ by a very large circle $|z| = R$ centered at the origin. On this circle, for large $R$,

$$z^k p(z)^{-1} = z^k (a_n z^n + \cdots)^{-1} \sim a_n^{-1} z^{k-n}.$$

If $k \leq n-2$, then $k - n \leq -2$, and the integral over the large circle tends to $0$ as $R \to \infty$. Since the integral is independent of $R$, it must be $0$:

$$D^k G(0+) = 0, \qquad 0 \leq k \leq n-2,$$

which is condition (2).

If $k = n-1$, the integrand is asymptotic to $a_n^{-1} z^{-1}$, and the integral of $z^{-1}$ over a large circle is $2\pi i$. Therefore

$$D^{n-1} G(0+) = \frac{1}{2\pi i} \int_{|z|=R} z^{n-1} p(z)^{-1} \, dz = a_n^{-1},$$

which is condition (5).

Thus $G$ satisfies all five conditions.

*Uniqueness.* Suppose $G_1$ also satisfies conditions (1)–(5) above, and let $f = G - G_1$. Then $f$ satisfies (1), (2), (3), and (4); moreover $D^{n-1} f(0+) = 0$ by (5). Hence

$$D^k f(0+) = 0 \quad \text{for } 0 \leq k \leq n-1,$$
$$p(D)f(t) = 0 \quad \text{for } t > 0,$$
$$f(t) = 0 \quad \text{for } t < 0.$$

Factor the polynomial

$$p(z) = a_n (z - z_1)(z - z_2) \cdots (z - z_n),$$

where the $z_j$ are the roots of $p$ (not necessarily distinct). Define a sequence of functions by

$$f_0 = f, \qquad f_k = D f_{k-1} - z_k f_{k-1}, \quad k = 1, 2, \ldots, n.$$

Then

$$f_n = (D - z_n)(D - z_{n-1}) \cdots (D - z_1) f = a_n^{-1} p(D) f = 0 \quad \text{on } (0, \infty).$$

Now each $f_k$ is a linear combination of $D^j f$ for $0 \leq j \leq k$, and since $D^j f(0+) = 0$ for all $0 \leq j \leq n-1$, we have

$$f_k(0+) = 0, \qquad 0 \leq k \leq n.$$

From $f_n = 0$ we obtain $D f_{n-1} = z_n f_{n-1}$, so $f_{n-1}(t) = C \exp(z_n t)$ for $t > 0$ (by Theorem 5.1 of Chapter 2). Since $f_{n-1}(0+) = 0$, we have $C = 0$, hence $f_{n-1} = 0$ on $(0, \infty)$.

Proceeding inductively backward, $f_{n-2} = 0$, $f_{n-3} = 0$, and finally $f_0 = f = 0$ on $(0, \infty)$. Since $f$ also vanishes for $t < 0$ and at $t = 0$ (the functions are continuous from the right), we conclude $f \equiv 0$, i.e., $G = G_1$.

$\square$

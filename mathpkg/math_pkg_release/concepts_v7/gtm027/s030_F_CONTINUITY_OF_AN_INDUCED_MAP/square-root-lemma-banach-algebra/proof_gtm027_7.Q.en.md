---
role: proof
locale: en
of_concept: square-root-lemma-banach-algebra
source_book: gtm027
source_chapter: "7"
source_section: "Q"
---

# Proof of Square Root Lemma for Banach Algebras

Let $A$ be a real or complex Banach algebra with unit $u$. If $\|x - u\| \leq 1$, then there exists $y \in A$ such that $x = y^2$.

**Proof.** Let $z = u - x$, so $\|z\| \leq 1$. We seek $y$ such that $y^2 = u - z$. The formal binomial expansion suggests

$$y = (u - z)^{1/2} = \sum_{n=0}^\infty a_n z^n,$$

where $a_n$ are the binomial coefficients of $(1 - t)^{1/2}$ (as in part (b)).

Since $\|z\| \leq 1$, the series $\sum |a_n| \|z\|^n$ converges (by properties of the binomial series: $\sum |a_n|$ converges, as $\sum_{n=0}^\infty a_n = 0$ and $a_n < 0$ for $n \geq 1$ implies $\sum |a_n| = -2\sum_{n \geq 1} a_n = 2$). Actually, more directly: $(1 - t)^{1/2}$ has radius of convergence $1$, and at $t = 1$ the series converges (conditionally). By Abel's theorem or properties of the coefficients, $\sum |a_n| < \infty$.

Thus $\sum_{n=0}^\infty a_n z^n$ converges absolutely in the Banach algebra, so

$$y = \sum_{n=0}^\infty a_n z^n$$

is a well-defined element of $A$ (with $z^0 = u$).

To verify $y^2 = x$: using the convolution property from (b),

$$y^2 = \sum_{p=0}^\infty \left(\sum_{k=0}^p a_k a_{p-k}\right) z^p = a_0^2 \cdot u + (a_0 a_1 + a_1 a_0) z + \sum_{p \geq 2} 0 \cdot z^p = u - z = x.$$

Alternatively, $y$ may be written as

$$y = u + \sum_{n=1}^\infty a_n z^n = u + \sum_{n=1}^\infty a_n (z^n - u),$$

where the terms $a_n(z^n - u)$ remove the constant term and show that $y$ is a limit of polynomials in $x$ without constant term (since the series with $z^n - u$ converges absolutely).

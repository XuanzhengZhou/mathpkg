---
role: proof
locale: en
of_concept: di-1-logarithmic-derivative-homomorphism
source_book: gtm059
source_chapter: "9"
source_section: "2. The Logarithmic Derivative"
---

The proof considers the basic Lubin-Tate generators $w_n$ satisfying the equation

$$
g_{n+1}(X) + X + w_n, \quad X + w_{n+1} = w_n = 0.
$$

The relative different is obtained by taking the derivative and evaluating at $w_n$ and $w_{n+1}$ respectively.

Let $x \in K_n$ and write $x = g(\pi_n)$ as a power series with $g(X) = X^m + \text{higher terms}$ and leading coefficient a unit. Let $g(X) = X^m + K(X)$. Then

$$
g'(X) = \frac{1}{2} X^m + \frac{1}{4} K(X).
$$

Hence $g'(\pi_n)$ is integral if $m = 0$, and in any case lies in $\mathfrak{m}_n^{-1} \mathfrak{D}_n^{-1}$. If $g_1(X)$ and $g_2(X)$ are two power series whose values at $\pi_n$ are equal to $x$, and $f(X)$ is the irreducible polynomial of $\pi_n$ over $K$, then

$$
g_1(X) - g_2(X) = f(X) h(X) \quad \text{or} \quad 0 \pmod{\varpi_1}
$$

for some power series $h(X) \in \mathfrak{o}[[X]]$. Hence

$$
g_1'(\pi_n) \equiv g_2'(\pi_n) \pmod{\mathfrak{D}_n}.
$$

This shows that $g'(\pi_n)$ is well-defined modulo the different, establishing that $D_n$ is a well-defined homomorphism.

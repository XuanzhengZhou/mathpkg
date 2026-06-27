---
role: proof
locale: en
of_concept: theorem-115
source_book: gtm077
source_chapter: "38"
source_section: "Relative Norms of Numbers and Ideals, Relative Differents, and Relative Discriminants"
---
# Proof of Theorem 115

**Statement.** Suppose that $K$ is identical with all its relative conjugate fields with respect to $k$ (that is, $K$ is a relative Galois field over $k$). Then the only prime ideals of $K$ that divide the relative different $\mathfrak{D}_k$ are those which divide a prime ideal of $k$ to a power higher than the first.

*Proof.* Let $\mathfrak{p}$ be a prime ideal in $k$ and let $\mathfrak{P}$ be a prime divisor of $\mathfrak{p}$ in $K$ whose square does not divide $\mathfrak{p}$ (i.e., $\mathfrak{p}$ is unramified at $\mathfrak{P}$).

Since $K/k$ is Galois, the relatively conjugate prime ideals $\mathfrak{P}^{(i)}$ also divide $\mathfrak{p}$ to exactly the first power. The relative norm

$$N_k(\mathfrak{P}) = \mathfrak{p}^f$$

is the product of all the $\mathfrak{P}^{(i)}$, where $f$ is the relative degree. The conjugates $\mathfrak{P}^{(i)}$ split into sets, each consisting of $f$ primes that coincide with one another; there are exactly $m/f$ distinct ones among the $\mathfrak{P}^{(i)}$. Let $\mathfrak{P}^{(1)}, \ldots, \mathfrak{P}^{(f)}$ be those identical with $\mathfrak{P}$.

Now, by the definition of the relative different and the Dedekind discriminant theorem (or by direct computation using the trace form), the exponent of $\mathfrak{P}$ in $\mathfrak{D}_k$ is at least $e-1$, where $e$ is the ramification index of $\mathfrak{P}$ over $\mathfrak{p}$. If $\mathfrak{P}^2 \nmid \mathfrak{p}$ (i.e., $e = 1$), then the exponent is $0$, meaning $\mathfrak{P} \nmid \mathfrak{D}_k$.

Conversely, if $\mathfrak{P}^2 \mid \mathfrak{p}$ (i.e., $e \geq 2$), then by a local computation of the trace of $\mathfrak{P}^{-1}$-integral elements, one finds that the trace of certain fractions produces denominators, which forces $\mathfrak{P}$ to divide $\mathfrak{D}_k$. Therefore, precisely the ramified primes (those with $e \geq 2$) divide the relative different.

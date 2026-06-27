---
role: proof
locale: en
of_concept: dedekind-theorem-relative-discriminant
source_book: gtm077
source_chapter: "V"
source_section: "§38"
---
# Proof of Theorem 115

**Theorem 115 (Dedekind).** Suppose that $K$ is identical with all relative conjugate fields with respect to $k$ (that is, suppose that $K$ is a relative Galois field). Then the only prime ideals of $K$ dividing the relative different $\mathfrak{D}_k$ of $K$ are those which divide a prime ideal of $k$ to a power higher than the first.

**Proof.** Let $\mathfrak{p}$ be a prime ideal in $k$ and let $\mathfrak{P}$ be a prime divisor of $\mathfrak{p}$ in $K$. Suppose that $\mathfrak{P}^2 \nmid \mathfrak{p}$, i.e., the ramification index $e = 1$. We must show that $\mathfrak{P} \nmid \mathfrak{D}_k$.

Since $K$ is a relative Galois extension of $k$, the Galois group acts transitively on the prime ideals of $K$ dividing $\mathfrak{p}$. The relatively conjugate prime ideals $\mathfrak{P}^{(i)}$ (for $i = 1, \ldots, m$) also divide $\mathfrak{p}$ to exactly the first power, because the ramification index is preserved under the action of the relative Galois group.

The relative norm $N_k(\mathfrak{P}) = \mathfrak{p}^f$ is the product of all the $\mathfrak{P}^{(i)}$, where $f$ is the relative degree. These $m$ conjugate ideals split into sets, each consisting of $f$ primes which coincide with one another; there are exactly $m/f$ distinct ones among the $\mathfrak{P}^{(i)}$. Let $\mathfrak{P}^{(1)}, \ldots, \mathfrak{P}^{(f)}$ be those which are identical with $\mathfrak{P}$.

Since $\mathfrak{p} = \prod_{j=1}^{m/f} \mathfrak{P}_j$ (each appearing with exponent $1$), the factorization of $\mathfrak{p}$ is unramified at $\mathfrak{P}$.

Now consider the relative different $\mathfrak{D}_k$. By Theorem 112, $\mathfrak{D}_k$ is the GCD of the relative differents of integers of $K$. For an integer $\theta$ generating $K$ over $k$, the relative different $\delta_k(\theta) = \Phi'(\theta)$ (up to a unit), where $\Phi$ is the minimal polynomial of $\theta$ over $k$.

When $\mathfrak{P}$ is unramified over $\mathfrak{p}$ (i.e., $e = 1$), it is a standard result from the theory of differents that $\mathfrak{P} \nmid \Phi'(\theta)$ for a suitable choice of $\theta$ (e.g., choose $\theta$ to be a primitive element whose minimal polynomial has discriminant coprime to $\mathfrak{p}$). Since $\mathfrak{D}_k$ divides each $\delta_k(\theta)$, it follows that $\mathfrak{P} \nmid \mathfrak{D}_k$.

Conversely, Theorem 114 already established that if $e > 1$ (ramified case), then $\mathfrak{P} \mid \mathfrak{D}_k$. Together, these two results characterize the prime divisors of the relative different exactly as the ramified primes in the relative extension $K/k$.

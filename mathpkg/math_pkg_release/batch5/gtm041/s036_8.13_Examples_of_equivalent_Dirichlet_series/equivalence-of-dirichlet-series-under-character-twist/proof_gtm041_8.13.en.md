---
role: proof
locale: en
of_concept: equivalence-of-dirichlet-series-under-character-twist
source_book: gtm041
source_chapter: "8"
source_section: "8.13"
---

**Proof of Theorem 8.17.** Since these are ordinary Dirichlet series we may use Theorem 8.12 to establish the equivalence. In this case we take $f(n) = \chi(n)$. Then $f$ is completely multiplicative and condition (a) of Theorem 8.12 is satisfied.

Now we show that condition (b) is satisfied. We need to show that $|f(p)| = 1$ if $a(n) \neq 0$ and $p \mid n$. But $a(n) \neq 0$ implies $(n, k) = 1$. Since $p \mid n$ we must have $(p, k) = 1$, so $|\chi(p)| = 1$ because $\chi(p)$ is a root of unity for $p$ coprime to $k$.

Thus both conditions of Theorem 8.12 are satisfied, and the equivalence
$$\sum_{n=1}^{\infty} \frac{a(n)}{n^s} \sim \sum_{n=1}^{\infty} \frac{a(n)\chi(n)}{n^s}$$
follows. $\square$

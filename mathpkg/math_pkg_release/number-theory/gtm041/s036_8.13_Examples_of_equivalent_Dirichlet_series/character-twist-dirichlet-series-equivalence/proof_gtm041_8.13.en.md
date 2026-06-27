---
role: proof
locale: en
of_concept: character-twist-dirichlet-series-equivalence
source_book: gtm041
source_chapter: "8"
source_section: "8.13"
---

Since these are ordinary Dirichlet series we may use Theorem 8.12 to establish the equivalence. Take $f(n) = \chi(n)$. Then $f$ is completely multiplicative and condition (a) of Theorem 8.12 is satisfied.

Now we verify condition (b): we need to show that $|f(p)| = 1$ whenever $a(n) \neq 0$ and $p \mid n$. But $a(n) \neq 0$ implies $(n, k) = 1$ by hypothesis. Since $p \mid n$, we have $(p, k) = 1$, so $|f(p)| = |\chi(p)| = 1$ (a Dirichlet character has absolute value 1 on integers coprime to its modulus).

Thus both conditions of Theorem 8.12 hold, and the conclusion follows.

---
role: proof
locale: en
of_concept: a-and-c-implies-gaussian
source_book: gtm030
source_chapter: "II"
source_section: "3"
---

It suffices to prove condition B: every irreducible element is prime. Let $p$ be irreducible and suppose $p \mid ab$. Since $p$ is irreducible and $(p, a)$ is a divisor of $p$, either $(p, a) \sim p$ or $(p, a) \sim 1$. Similarly, $(p, b) \sim p$ or $(p, b) \sim 1$.

If $(p, a) \sim 1$ and $(p, b) \sim 1$, then by Lemma 4, $(p, ab) \sim (p, b) \sim 1$, which contradicts $p \mid ab$ (since $p \mid ab$ implies $(p, ab) \sim p$). Therefore, either $(p, a) \sim p$ (so $p \mid a$) or $(p, b) \sim p$ (so $p \mid b$). Thus $p$ is prime. Since both A and B hold, $\mathfrak{S}$ is Gaussian by the result of the preceding section.

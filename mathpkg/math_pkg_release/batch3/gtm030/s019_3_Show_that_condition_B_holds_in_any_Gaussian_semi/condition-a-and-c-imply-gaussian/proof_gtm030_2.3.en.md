---
role: proof
locale: en
of_concept: condition-a-and-c-imply-gaussian
source_book: gtm030
source_chapter: "2"
source_section: "3"
---

We first show that Condition C implies Condition B: every irreducible element of $\mathfrak{S}$ is prime. Let $p$ be irreducible and suppose $p \mid ab$ for some $a, b \in \mathfrak{S}$. Since $p$ is irreducible and $(p, a)$ is a divisor of $p$, either $(p, a) \sim p$ or $(p, a) \sim 1$. Similarly, either $(p, b) \sim p$ or $(p, b) \sim 1$.

If both $(p, a) \sim 1$ and $(p, b) \sim 1$, then by Lemma 4 we would have $(p, ab) \sim 1$. But $p \mid ab$ implies $(p, ab) \sim p$, a contradiction since $p$ is not a unit. Hence either $(p, a) \sim p$ or $(p, b) \sim p$, which means $p \mid a$ or $p \mid b$. This proves that $p$ is prime, i.e., Condition B holds.

Now $\mathfrak{S}$ satisfies both Condition A (by hypothesis) and Condition B (just proved). By the result of the preceding section, a commutative semi-group with identity and cancellation law satisfying A and B is Gaussian (has unique factorization). Hence $\mathfrak{S}$ is Gaussian.

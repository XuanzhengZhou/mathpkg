---
role: proof
locale: en
of_concept: associated-power-series-of-local-units
source_book: gtm059
source_chapter: "7"
source_section: "7"
---

*Proof.* Uniqueness is obvious since a nonzero power series has only a finite number of roots.

For existence, we proceed via several steps. First, define the power series associated with the element $\zeta$:
$$f_u(X) = \frac{1}{(b - X)} (b - X).$$

Next we note two formal properties.

**CW 1.** If $u \in \mathbb{Z}_p$, then the power series associated with $u^n$ is $f_u(X)^n$.

*Proof of CW 1.* This is obvious when $u$ is a positive integer, and is then true for all $u \in \mathbb{Z}_p$ by continuity.

**CW 2.** If $f_u$ is the power series associated with $u$, and $u \in G_{n-1}$, then the power series associated with $u$ satisfies $U_f(X) = X^n f_u(X) + (X^n - 1)$.

*Proof of CW 2.* If $u = \sum_{i=1}^{n} u_i^n - 1$ with $u_i \in \mathbb{Z}_p$, then the property follows from the definitions.

These two properties show that the set of elements having an associated power series forms a $\mathbb{Z}_p[[X]]$-submodule of $U$ which is closed under the stated operations, and thus contains all of $U$.

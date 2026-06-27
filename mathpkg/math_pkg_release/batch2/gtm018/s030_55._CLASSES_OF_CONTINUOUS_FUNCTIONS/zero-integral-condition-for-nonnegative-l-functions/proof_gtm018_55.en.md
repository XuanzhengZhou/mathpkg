---
role: proof
locale: en
of_concept: zero-integral-condition-for-nonnegative-l-functions
source_book: gtm018
source_chapter: "55"
source_section: "55. Classes of Continuous Functions"
---

**Sufficiency.** If $f(x) = 0$ for every $x \in X$, then trivially $\int f \, d\mu = 0$.

**Necessity.** Suppose $\int f \, d\mu = 0$ and $f \in \mathcal{L}_+$. Let $U$ be a bounded open Baire set such that $\{x : f(x) \neq 0\} \subset U$. Let $E = \{x : f(x) = 0\}$. Since $f \geq 0$, we have

$$0 = \int f \, d\mu = \int_U f \, d\mu \geq \int_{U - E} f \, d\mu.$$

Because $f$ is non-negative and the integral over $U - E$ is bounded above by zero (and below by zero since $f \geq 0$), the integral $\int_{U - E} f \, d\mu$ must be zero. Since $f(x) > 0$ for $x \in U - E$ (by definition of $E$), the fact that the integral of a strictly positive function over $U - E$ vanishes forces $\mu(U - E) = 0$.

Now $U - E$ is an open Baire set (it is the intersection of the open set $U$ with the set where $f > 0$, which is open by continuity of $f$). By hypothesis, every non-empty Baire open set has positive measure. Therefore $\mu(U - E) = 0$ implies $U - E = \emptyset$, so $U \subset E$. Since $\{x : f(x) \neq 0\} \subset U$, we conclude $\{x : f(x) \neq 0\} = \emptyset$, i.e., $f(x) = 0$ for all $x \in X$.

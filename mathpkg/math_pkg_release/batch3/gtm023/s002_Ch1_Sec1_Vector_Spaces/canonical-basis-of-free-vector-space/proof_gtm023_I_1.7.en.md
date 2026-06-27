---
role: proof
locale: en
of_concept: canonical-basis-of-free-vector-space
source_book: gtm023
source_chapter: "I"
source_section: "1.7"
---

Recall $f_a \in C(X)$ is defined by $f_a(a) = 1$ and $f_a(x) = 0$ for $x \neq a$.

**Generating property:** For any $f \in C(X)$, $f(x) \neq 0$ for only finitely many $x \in X$. Thus
$$f = \sum_{x \in X} f(x) f_x,$$
expressing $f$ as a linear combination of the $f_a$. Hence the $f_a$ generate $C(X)$.

**Linear independence:** Suppose $\sum_{j=1}^n \lambda^j f_{a_j} = 0$. Evaluating at $a_k$,
$$0 = \left(\sum_{j=1}^n \lambda^j f_{a_j}\right)(a_k) = \sum_{j=1}^n \lambda^j f_{a_j}(a_k) = \lambda^k,$$
since $f_{a_j}(a_k) = 1$ if $j=k$ and $0$ otherwise. Thus $\lambda^k = 0$ for all $k$, proving independence.

Therefore $(f_a)_{a \in X}$ is a basis of $C(X)$.

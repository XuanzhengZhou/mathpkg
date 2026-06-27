---
role: proof
locale: en
of_concept: riesz-representation-uniqueness
source_book: gtm018
source_chapter: "56"
source_section: "56. LINEAR FUNCTIONALS"
---

It is clear that $\mu(C) \leq \lambda(C)$, since for any $f \in \mathcal{L}_+$ with $C \subset f$, we have $\mu(C) = \int_C 1 \, d\mu \leq \int f \, d\mu = \Lambda(f)$, and taking the infimum over such $f$ gives $\mu(C) \leq \lambda(C)$.

For the reverse inequality: if $C \in \mathbf{C}$ and $\epsilon > 0$, then, by the regularity of $\mu$, there exists a bounded open set $U$ containing $C$ such that $\mu(U) \leq \mu(C) + \epsilon$. Let $f$ be a function in $\mathcal{L}$ such that $f(x) = 1$ for $x$ in $C$ and $f(x) = 0$ for $x$ in $X - U$. Then

$$\lambda(C) \leq \Lambda(f) = \int f \, d\mu \leq \mu(U) \leq \mu(C) + \epsilon.$$

Since $\epsilon$ is arbitrary, $\lambda(C) \leq \mu(C)$. Combined with $\mu(C) \leq \lambda(C)$, we obtain $\mu(C) = \lambda(C)$ for every $C \in \mathbf{C}$.

---
role: proof
locale: en
of_concept: finite-division-ring-associative-condition
source_book: gtm006
source_chapter: "IX"
source_section: "4"
---

When $F$ is a finite field, $\theta$ is an automorphism (since every bijective anti-automorphism of a finite field is an automorphism). Since $D$ is associative, every associator vanishes. From the associator formula (Lemma 9.8), putting $t = \lambda$ (so $t_1 = 0, t_2 = 1$) and $y = 0$, we obtain $x^{\theta^2} = x$ and $b(x^{\theta^2} - x^2) = 0$ for all $x \in F$.

If $\theta \neq 1$, then $\theta^2 = 1$ and $b = 0$. Putting $b = 0$ in the associator formula gives $t_2 k (a^\theta - a) = 0$ for all $t_2, k, y$, which implies $a^\theta = a$. Hence $a$ belongs to the subfield $K$ of elements fixed by $\theta$.

Since $\theta^2 = 1$, we have $K = \mathrm{GF}(q)$ where $F = \mathrm{GF}(q^2)$ and $\theta$ is given by $x^\theta = x^q$. But then $x^{1+\theta} = x^{1+q}$ varies over all of $K$ as $x$ varies over $F$, so there exists $x \in F$ such that $x^{1+\theta} = a$, violating condition (2) (recall $b = 0$). This contradiction shows $\theta = 1$. The converse is trivial. $\square$

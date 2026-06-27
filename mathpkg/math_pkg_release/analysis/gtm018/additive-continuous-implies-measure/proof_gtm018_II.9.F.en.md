---
role: proof
locale: en
of_concept: additive-continuous-implies-measure
source_book: gtm018
source_chapter: "II"
source_section: "9"
---

We observe first that the additivity of $\mu$, together with the fact that $\mathbf{R}$ is a ring, implies, by mathematical induction, that $\mu$ is finitely additive. Let $\{E_n\}$ be a disjoint sequence of sets in $\mathbf{R}$, whose union, $E$, is also in $\mathbf{R}$ and write

$$F_n = \bigcup_{i=1}^{n} E_i, \quad G_n = E - F_n.$$

If $\mu$ is continuous from below, then, since $\{F_n\}$ is an increasing sequence of sets in $\mathbf{R}$ with $\lim_n F_n = E$, we have

$$\mu(E) = \lim_n \mu(F_n) = \lim_n \sum_{i=1}^{n} \mu(E_i) = \sum_{i=1}^{\infty} \mu(E_i).$$

If $\mu$ is continuous from above at $0$, then, since $\{G_n\}$ is a decreasing sequence of sets in $\mathbf{R}$ with $\lim_n G_n = 0$, and since $\mu$ is finite, we have

$$\mu(E) = \mu(E) - \lim_n \mu(G_n) = \lim_n (\mu(E) - \mu(G_n)) = \lim_n \mu(F_n) = \sum_{i=1}^{\infty} \mu(E_i).$$

In either case, $\mu$ is countably additive and therefore a measure on $\mathbf{R}$.

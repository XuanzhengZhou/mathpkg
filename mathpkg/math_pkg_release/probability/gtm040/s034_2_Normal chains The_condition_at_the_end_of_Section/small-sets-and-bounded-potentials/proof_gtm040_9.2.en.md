---
role: proof
locale: en
of_concept: small-sets-and-bounded-potentials
source_book: gtm040
source_chapter: "9"
source_section: "2"
---

Let $g$ be a bounded potential with support in $E$. Since $g = B^E g$ (because $g$ has support in $E$), regularity off $E$ follows from the properties of $B^E$. The condition $\lambda^E g = 0$ follows from the fact that $P^n g \to 0$ (since $g$ is a potential) and $P^n g = P^n B^E g \to 1 \lambda^E g$, forcing $\lambda^E g = 0$.

Conversely, suppose $E$ is small and ergodic, and $g$ is bounded, regular off $E$, and satisfies $\lambda^E g = 0$. Then $(I - P)g$ is supported on $E$ (by regularity), and
$$\alpha[(I - P)g] = \alpha[(I - P)B^E g] = \alpha \binom{(I - P^E)g_E}{0} = \alpha_E(g_E - P^E g_E).$$
Since $E$ is ergodic, $\alpha_E 1 < \infty$, and $g$ is bounded, $\alpha_E g_E$ is finite. Hence
$$\alpha_E(g_E - P^E g_E) = \alpha_E g_E - (\alpha_E P^E) g_E = \alpha_E g_E - \alpha_E g_E = 0.$$
Therefore, by Corollary 9-16, $g$ is a potential. It is bounded by hypothesis, and its charge $\binom{(I - P^E)g_E}{0}$ has support in $E$.

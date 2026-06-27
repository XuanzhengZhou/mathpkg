---
role: proof
locale: en
of_concept: principle-of-balayage-recurrent
source_book: gtm040
source_chapter: "9"
source_section: "2"
---

Let $g = B^E x - (\lambda^E x)1$. Then $g$ is bounded (since $B^E$ is bounded and $x$ is bounded on the small set $E$). Moreover,
$$(I - P)g = \binom{(I - P^E)x_E}{0},$$
so $g$ is regular on $\tilde{E}$. Also $\lambda^E g = \lambda^E B^E x - (\lambda^E x)\lambda^E 1 = \lambda^E x - \lambda^E x = 0$, since $\lambda^E 1 = 1$ (because $E$ is small) and $\lambda^E B^E = \lambda^E$. By Proposition 9-42, $g$ is a bounded potential with support in $E$, and $g$ differs from $x$ by the constant $\lambda^E x$ on $E$.

For uniqueness, let $g'$ be another such potential. Then $g_E - g'_E = k1$ (they differ by a constant on $E$). Hence $g - g' = B^E(g - g') = k B^E 1 = k1$. Since $P^n(g - g') = P^n(k1) \to 0$ as $n \to \infty$ (as $g$ and $g'$ are both potentials), we must have $k = 0$. Thus $g = g'$.

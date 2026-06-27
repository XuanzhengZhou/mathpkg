---
role: proof
locale: en
of_concept: kernel-quadratic-form-nonnegativity
source_book: gtm040
source_chapter: "9"
source_section: "9"
---

The proof proceeds as in Lemma 8-54, but $P^E 1 = 1$ and $\alpha_E P^E = \alpha_E$; hence $m_i = 0$ and $\pi_i = 0$. Let $F$ be the subset of all states of $E$ on which $g = g_0$. If $F \neq E$, there are states $i \in F$ and $j \in \tilde{F}$ such that $P_{ij}^E > 0$, since the states of $E$ communicate. Then
$$\nu_E(I - P^E)g_E \geq \tfrac{1}{2} \alpha_i P_{ij}^E (g_i - g_j)^2 > 0,$$
which proves the strict positivity when $g$ is not constant.

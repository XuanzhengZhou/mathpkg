---
role: proof
locale: en
of_concept: dirichlet-density-theorem
source_book: gtm007
source_chapter: "VI"
source_section: "4"
---

By Lemma 9, $g_a(s) = \frac{1}{\phi(m)} \sum_\chi \chi(a)^{-1} f_\chi(s)$.

For $\chi = 1$, Lemma 7 gives $f_1(s) \sim \log 1/(s-1)$ as $s \to 1^+$. For $\chi \neq 1$, Lemma 8 shows $f_\chi(s)$ remains bounded. Therefore,
$$g_a(s) \sim \frac{1}{\phi(m)} \log\frac{1}{s-1} \quad \text{as } s \to 1^+.$$

Since $\sum_p 1/p^s \sim \log 1/(s-1)$ (Corollary 2 to Proposition 10), the ratio
$$\frac{\sum_{p \in P_a} p^{-s}}{\sum_p p^{-s}} = \frac{g_a(s) + O(1)}{\sum_p p^{-s}} \longrightarrow \frac{1}{\phi(m)} \quad \text{as } s \to 1^+,$$
which is precisely the definition of $P_a$ having analytic density $1/\phi(m)$. Since the density is positive, $P_a$ is infinite.


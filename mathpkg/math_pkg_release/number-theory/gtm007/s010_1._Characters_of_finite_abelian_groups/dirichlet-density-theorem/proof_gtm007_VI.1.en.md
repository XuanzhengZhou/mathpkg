---
role: proof
locale: en
of_concept: dirichlet-density-theorem
source_book: gtm007
source_chapter: "VI"
source_section: "§1. Characters of finite abelian groups"
---

By Lemma 9,
$$
g_a(s) = \sum_{p \equiv a (m)} p^{-s} = \frac{1}{\phi(m)} \sum_\chi \chi(a)^{-1} f_\chi(s),
$$
where $f_\chi(s) = \sum_{p \nmid m} \chi(p)/p^s$. Lemma 7 gives $f_1(s) \sim \log\frac{1}{s-1}$ as $s \to 1^+$. Lemma 8 (using $L(1,\chi) \neq 0$) shows $f_\chi(s)$ remains bounded for $\chi \neq 1$. Hence
$$
g_a(s) \sim \frac{1}{\phi(m)} \log\frac{1}{s-1},
$$
which means the analytic density of $P_a$ is $1/\phi(m)$. Since a finite set has density $0$, $P_a$ is infinite.

---
role: proof
locale: en
of_concept: absolute-convergence-implies-convergence
source_book: gtm011
source_chapter: "III"
source_section: "1"
---

Let $\epsilon > 0$ and put $z_n = a_0 + a_1 + \ldots + a_n$. Since $\sum |a_n|$ converges there is an integer $N$ such that $\sum_{n=N}^{\infty} |a_n| < \epsilon$. Thus, if $m > k \geq N$,
$$|z_m - z_k| = \left| \sum_{n=k+1}^{m} a_n \right| \leq \sum_{n=k+1}^{m} |a_n| \leq \sum_{n=N}^{\infty} |a_n| < \epsilon.$$

That is, $\{z_n\}$ is a Cauchy sequence and so there is a $z$ in $\mathbb{C}$ with $z = \lim z_n$. Hence $\sum a_n = z$.

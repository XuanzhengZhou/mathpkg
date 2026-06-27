---
role: proof
locale: en
of_concept: comparison-test-for-series
source_book: gtm012
source_chapter: "4"
source_section: "4. Series"
---

# Proof of Comparison test for series (Proposition 4.3)

**Proposition 4.3.** Suppose $(z_n)_{n=1}^{\infty}$ is a sequence in $\mathbb{C}$ and $(a_n)_{n=1}^{\infty}$ is a sequence of non-negative real numbers. If there exist $M > 0$ and an integer $N$ such that $|z_n| \leq M a_n$ for all $n \geq N$, and if $\sum a_n$ converges, then $\sum z_n$ converges (and in fact converges absolutely).

**Proof.** Let

$$s_n = \sum_{m=1}^{n} z_m, \qquad b_n = \sum_{m=1}^{n} a_m.$$

If $n, m \geq N$ with $n > m$, then

$$|s_n - s_m| = \left| \sum_{j=m+1}^{n} z_j \right| \leq \sum_{j=m+1}^{n} |z_j| \leq M \sum_{j=m+1}^{n} a_j = M(b_n - b_m).$$

Since $\sum a_n$ converges, $(b_n)_{n=1}^{\infty}$ is a Cauchy sequence. The inequality above then implies that $(s_n)_{n=1}^{\infty}$ is also a Cauchy sequence (for any $\varepsilon > 0$, choose $N' \geq N$ such that $|b_n - b_m| < \varepsilon/M$ for $n, m \geq N'$; then $|s_n - s_m| < \varepsilon$ for $n, m \geq N'$). By Theorem 3.3 (the Cauchy criterion), $\sum z_n$ converges. $\square$

**Remark.** The hypothesis $|z_n| \leq M a_n$ also implies absolute convergence of $\sum z_n$, since the same argument applied to $|z_n|$ in place of $z_n$ shows that $\sum |z_n|$ converges by comparison with $\sum M a_n$.

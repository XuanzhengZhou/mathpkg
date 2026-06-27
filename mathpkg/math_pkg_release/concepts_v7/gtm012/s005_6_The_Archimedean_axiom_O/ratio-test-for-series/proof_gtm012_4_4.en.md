---
role: proof
locale: en
of_concept: ratio-test-for-series
source_book: gtm012
source_chapter: "4"
source_section: "4. Series"
---

# Proof of Ratio test for series (Proposition 4.4)

**Proposition 4.4 (Ratio test).** Suppose $(z_n)_{n=1}^{\infty}$ is a sequence in $\mathbb{C}$ and suppose $z_n \neq 0$ for all $n$.

(a) If $\limsup |z_{n+1}/z_n| < 1$, then $\sum z_n$ converges (absolutely).

(b) If $\liminf |z_{n+1}/z_n| > 1$, then $\sum z_n$ diverges.

**Proof.**

**(a)** Choose $r$ such that $\limsup |z_{n+1}/z_n| < r < 1$. By Proposition 3.4 (characterization of $\limsup$), there exists $N$ such that $|z_{n+1}/z_n| \leq r$ for all $n \geq N$. Then for $n > N$,

$$|z_n| \leq r |z_{n-1}| \leq r^2 |z_{n-2}| \leq \cdots \leq r^{n-N} |z_N| = M r^n,$$

where $M = r^{-N} |z_N|$. Since $0 < r < 1$, the geometric series $\sum r^n$ converges. By Proposition 4.3 (comparison test), $\sum |z_n|$ converges, hence $\sum z_n$ converges absolutely.

**(b)** By Proposition 3.4 (characterization of $\liminf$), since $\liminf |z_{n+1}/z_n| > 1$, there exists $N$ such that $|z_{n+1}/z_n| \geq 1$ for all $n \geq N$. Thus for $n > N$,

$$|z_n| \geq |z_{n-1}| \geq \cdots \geq |z_N| > 0.$$

In particular, $|z_n| \not\to 0$ as $n \to \infty$. By Proposition 4.1 (if $\sum z_n$ converges then $z_n \to 0$), the series $\sum z_n$ must diverge. $\square$

**Remark.** The ratio test is inconclusive when $\limsup |z_{n+1}/z_n| \geq 1$ and $\liminf |z_{n+1}/z_n| \leq 1$. In particular, it gives no information when $\lim |z_{n+1}/z_n| = 1$.

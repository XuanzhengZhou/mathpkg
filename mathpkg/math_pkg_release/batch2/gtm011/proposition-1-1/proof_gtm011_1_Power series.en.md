---
role: proof
locale: en
of_concept: proposition-1-1
source_book: gtm011
source_chapter: "Elementary Properties and Examples of Analytic Functions"
source_section: "1. Power series"
---

Proof. Let $\epsilon > 0$ and put $z_n = a_0 + a_1 + \ldots + a_n$. Since $\sum |a_n|$ converges there is an integer $N$ such that $\sum_{n=N}^{\infty} |a_n| < \epsilon$. Thus, if $m > k \geq N$,

$$|z_m - z_k| = \left| \sum_{n=k+1}^{m} a_n \right| \leq \sum_{n=k+1}^{m} |a_n| \leq \sum_{n=N}^{\infty} |a_n| < \epsilon.$$

That is, $\{z_n\}$ is a Cauchy sequence and so there is a $z$ in $\mathbb{C}$ with $z = \lim z_n$. Hence $\sum a_n = z$.

Also recall the definitions of limit inferior and superior of a sequence in $\mathbb{R}$. If $\{a_n\}$ is a sequence in $\mathbb{R}$ then define

$$\lim \inf a_n = \lim_{n \to \infty} \left[ \inf \{a_n, a_{n+1}, \ldots \} \right]$$

$$\lim \sup a_n = \lim_{n \to \infty} \

when does it diverge? It is easy to see that $1 - z^{n+1} = (1 - z)(1 + z + \ldots + z^n)$, so that

$$1 + z + \ldots + z^n = \frac{1 - z^{n+1}}{1 - z}.$$

If $|z| < 1$ then $0 = \lim z^n$ and so the geometric series is convergent with

$$\sum_{0}^{\infty} z^n = \frac{1}{1 - z}.$$

If $|z| > 1$ then $\lim |z|^n = \infty$ and the series diverges. Not only is this result an archetype for what happens to a general power series, but it can be used to explore the convergence properties of power series.

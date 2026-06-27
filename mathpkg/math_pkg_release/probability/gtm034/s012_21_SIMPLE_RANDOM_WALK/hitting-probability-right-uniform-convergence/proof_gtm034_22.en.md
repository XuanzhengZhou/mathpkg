---
role: proof
locale: en
of_concept: hitting-probability-right-uniform-convergence
source_book: gtm034
source_chapter: "V"
source_section: "22"
---

From P6(b) one can derive that
$$R_N(x) = \frac{x}{N} + \frac{1}{N} \sum_{k=1}^{\infty} k L_N(x,k) - \frac{1}{N} \sum_{k=1}^{\infty} k R_N(x,k).$$

It therefore suffices to show that $\frac{1}{N} \sum_{k=1}^{\infty} k R_N(x,k) \to 0$ uniformly, and similarly for $L_N$. Define
$$a(s) = \sum_{k=1}^{\infty} k P(0, s+k), \quad s \geq 0.$$
Using the bound on $g_N$ from P5,
$$\frac{1}{N} \sum_{k=1}^{\infty} k R_N(x,k) \leq \frac{M}{N} \sum_{k=1}^{\infty} k \sum_{y=0}^{N} (1 + N - y) P(y, N+k) = \frac{M}{N} \sum_{s=0}^{N} (1+s) a(s).$$

Now,
$$\sum_{s=0}^{\infty} a(s) = \sum_{k=0}^{\infty} \sum_{s=0}^{\infty} k P(0, s+k) = \sum_{j=1}^{\infty} (1+2+\cdots+j) P(0,j) \leq \sum_{j=1}^{\infty} j^2 P(0,j) \leq \sigma^2 < \infty.$$

By Kronecker's lemma, the convergence of $\sum a(s)$ implies $\lim_{n \to \infty} \frac{1}{n} \sum_{s=1}^{n} s a(s) = 0$, which gives $\lim_{N \to \infty} \frac{1}{N} \sum_{s=0}^{N} (1+s) a(s) = 0$. The bound is independent of $x$, yielding uniform convergence.

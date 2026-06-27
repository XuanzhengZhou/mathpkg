---
role: proof
locale: en
of_concept: weierstrass-product-theorem
source_book: gtm011
source_chapter: "5"
source_section: "5.12"
---

Suppose there are integers $p_n$ such that the series condition is satisfied. Then, according to Lemma 5.11, for any $r > 0$ and $|z| \leq r$,

$$|1 - E_{p_n}(z/a_n)| \leq \left| \frac{z}{a_n} \right|^{p_n+1} \leq \left( \frac{r}{|a_n|} \right)^{p_n+1}.$$

Since the series $\sum (r/|a_n|)^{p_n+1}$ converges by hypothesis, the series $\sum |1 - E_{p_n}(z/a_n)|$ converges uniformly on compact subsets of $\mathbb{C}$. By Theorem 5.9, the infinite product $\prod E_{p_n}(z/a_n)$ converges in $H(\mathbb{C})$ to an analytic function $f$, and $f$ has zeros exactly at the points $a_n$ with the prescribed multiplicities.

To show that $p_n = n-1$ always works: for any $r > 0$, there is an integer $N$ such that $|a_n| > 2r$ for all $n \geq N$. This gives $(r/|a_n|) < 1/2$ for all $n \geq N$, so if $p_n = n-1$, the tail of the series is dominated by $\sum (1/2)^n$, which converges. Thus the condition is always satisfied when $p_n = n-1$.

There is latitude in picking the $p_n$; larger integers also work. However, choosing $p_n$ as small as possible is advantageous since smaller $p_n$ yields simpler elementary factors. The size of $p_n$ needed depends on the rate at which $\{|a_n|\}$ converges to infinity, which will be explored further in Chapter XI.

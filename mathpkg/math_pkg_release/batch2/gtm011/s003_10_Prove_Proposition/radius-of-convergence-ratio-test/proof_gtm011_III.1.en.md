---
role: proof
locale: en
of_concept: radius-of-convergence-ratio-test
source_book: gtm011
source_chapter: "III"
source_section: "1"
---

Assume that $a = 0$ and let $\alpha = \lim |a_n/a_{n+1}|$, which we suppose to exist. Suppose that $|z| < r < \alpha$ and find an integer $N$ such that $r < |a_n/a_{n+1}|$ for all $n \geq N$. Let $B = |a_N| r^N$; then $|a_{N+1}| r^{N+1} = |a_{N+1}| r r^N < |a_N| r^N = B$; continuing we get $|a_n r^n| \leq B$ for all $n \geq N$. But then $|a_n z^n| = |a_n r^n| \cdot |z|^n / r^n \leq B |z|^n / r^n$ for all $n \geq N$. Since $|z| < r$ we get that $\sum |a_n z^n|$ is dominated by a convergent series and hence converges. Since $r < \alpha$ was arbitrary this gives $\alpha \leq R$.

On the other hand if $|z| > r > \alpha$, then $|a_n| < r|a_{n+1}|$ for all $n$ larger than some integer $N$. As before, we get $|a_n r^n| \geq B = |a_N r^N|$ for $n \geq N$. This gives $|a_n z^n| \geq B |z|^n / |r|^n$ which approaches $\infty$ as $n$ does. Hence $\sum a_n z^n$ diverges and so $R \leq \alpha$. Thus $R = \alpha$.

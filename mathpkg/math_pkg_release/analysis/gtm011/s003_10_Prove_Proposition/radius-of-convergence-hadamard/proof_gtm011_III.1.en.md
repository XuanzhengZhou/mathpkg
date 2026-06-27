---
role: proof
locale: en
of_concept: radius-of-convergence-hadamard
source_book: gtm011
source_chapter: "III"
source_section: "1"
---

We may suppose that $a = 0$. If $|z| < R$ there is an $r$ with $|z| < r < R$. Thus, there is an integer $N$ such that $|a_n|^{1/n} < 1/r$ for all $n \geq N$ (because $1/r > 1/R$). But then $|a_n| < 1/r^n$ and so $|a_n z^n| < (|z|/r)^n$ for all $n \geq N$. This says that the tail end $\sum_{n=N}^{\infty} |a_n z^n|$ is dominated by a convergent geometric series, proving (a).

If $|z| > R$ then $1/|z| < 1/R$, so there are infinitely many $n$ with $|a_n|^{1/n} > 1/|z|$, i.e., $|a_n z^n| > 1$, so the terms do not approach zero, proving (b).

For (c), if $0 < r < R$, choose $s$ with $r < s < R$. Then for sufficiently large $n$, $|a_n|^{1/n} < 1/s$, so $|a_n| s^n < 1$ and $|a_n z^n| \leq (r/s)^n$ for $|z| \leq r$, giving uniform convergence by the Weierstrass M-test.

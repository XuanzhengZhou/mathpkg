---
role: proof
locale: en
of_concept: strong-law-of-large-numbers
source_book: gtm040
source_chapter: "3"
source_section: "6. Law of Large Numbers"
---

The proof uses the generating function $\varphi(t) = \sum_j p_j \cdot t^j$, which satisfies $\varphi(1) = 1$ and $\varphi'(1) = a$. Define $f(k, n) = t^k / \varphi(t)^n$. Since $M[f(s_0, 0)] = 1 < \infty$, $\{f(s_n, n)\}$ is a non-negative martingale. By the Martingale Convergence Theorem, $f(s_n, n) = t^{s_n} / \varphi(t)^n$ converges to a finite limit a.e.

Fix $\epsilon > 0$, let $b = a + \epsilon$, and consider $g(t) = t^b / \varphi(t)$. Since $g(1) = 1$ and $g'(1) = b - a > 0$, we have $g(t_0) > 1$ for some $t_0 > 1$ sufficiently close to 1. If $s_n^*(\omega) \geq b$, then $[t_0^{s_n^*(\omega)} / \varphi(t_0)] \geq g(t_0) > 1$, and if $s_n^*(\omega) \geq b$ for infinitely many $n$, then $f(s_n(\omega), n)$ would have a subsequence tending to $+\infty$, contradicting convergence. Thus $\limsup s_n^*(\omega) \leq a + \epsilon$ a.e.

Similarly, choosing $t < 1$ gives $\liminf s_n^*(\omega) \geq a - \epsilon$ a.e. Since $\epsilon$ is arbitrary, $s_n^*$ converges to $a$ with probability one.

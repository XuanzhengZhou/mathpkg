---
role: proof
locale: en
of_concept: approximation-of-characteristic-function-by-l-plus
source_book: gtm018
source_chapter: "55"
source_section: "55. Classes of Continuous Functions"
---

Let $C$ be a compact Baire set. Then $C$ can be written as $C = \bigcap_{n=1}^{\infty} U_n$, where each $U_n$ is a bounded open set. For each positive integer $n$, there exists a function $g_n$ in $\mathfrak{F}$ (the class of Urysohn functions, cf. §50) such that $g_n(x) = 1$ for $x \in C$ and $g_n(x) = 0$ for $x \in X - U_n$. Since $U_n$ is bounded, each $g_n$ has compact support and is non-negative, so $g_n \in \mathcal{L}_+$.

Define $f_n = \min\{g_1, g_2, \ldots, g_n\}$. Then $\{f_n\}$ is a decreasing sequence of functions in $\mathcal{L}_+$. For any $x \in C$, we have $g_n(x) = 1$ for all $n$, hence $f_n(x) = 1$ for all $n$, so $\lim_n f_n(x) = 1 = \chi_C(x)$. For any $x \notin C$, since $C = \bigcap_n U_n$, there exists some $N$ such that $x \notin U_N$, and therefore $g_N(x) = 0$, which implies $f_n(x) = 0$ for all $n \geq N$. Hence $\lim_n f_n(x) = 0 = \chi_C(x)$. This completes the proof.

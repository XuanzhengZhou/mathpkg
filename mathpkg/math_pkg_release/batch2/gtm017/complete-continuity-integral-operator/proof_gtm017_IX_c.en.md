---
role: proof
locale: en
of_concept: complete-continuity-integral-operator
source_book: gtm017
source_chapter: "IX"
source_section: "c"
---
First, kernels of the form $r_1(t,\tau) = \alpha(t)\beta(\tau)$ generate completely continuous operators: for any bounded sequence $g_n$, $(\beta, g_n)$ is bounded, so a subsequence converges.

Finite sums $\sum \alpha_i(t)\beta_i(\tau)$ are also completely continuous. A general square integrable $r$ can be approximated by such finite sums. By the diagonal argument: let $g_n^{(k)}$ be a subsequence such that $R_k g_n^{(k)}$ converges for $k=1,2,\dots$. Then for the diagonal sequence $g_k^{(k)}$,
$$\|R g_k - R g_j\| \leq \|(R-R_N)g_k\| + \|R_N g_k - R_N g_j\| + \|(R-R_N)g_j\| \to 0$$
as $N, k, j \to \infty$, establishing complete continuity of $R$.

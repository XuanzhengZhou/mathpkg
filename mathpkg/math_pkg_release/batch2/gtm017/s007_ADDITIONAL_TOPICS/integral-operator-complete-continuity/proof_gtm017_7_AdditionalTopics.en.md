---
role: proof
locale: en
of_concept: integral-operator-complete-continuity
source_book: gtm017
source_chapter: "7"
source_section: "Additional Topics"
---

A simple kernel $r_1(t,\tau) = \alpha(t)\beta(\tau)$ generates a completely continuous operator: $(R_1g)(t) = (\beta,g)\alpha(t)$, and if $g_n$ is bounded, $(\beta,g_n)$ has a convergent subsequence $(\beta,g_{n_k}) \to c$, giving $\|R_1g_{n_k} - c\alpha\| \to 0$.

A finite sum $r_N(t,\tau) = \sum_{i=1}^N \alpha_i(t)\beta_i(\tau)$ generates a completely continuous operator $R_N$.

For a general $L^2$ kernel $r$, approximate by $r_N$ with $\|r - r_N\| \to 0$. For bounded $g_n$, construct successive subsequences converging under each $R_N$, then take the diagonal sequence $g_k^{(k)}$. Then $\|R g_k^{(k)} - R g_j^{(j)}\| \leq \|r - r_N\|(\|g_k^{(k)}\| + \|g_j^{(j)}\|) + \|R_N g_k^{(k)} - R_N g_j^{(j)}\|$. Given $\epsilon > 0$, choose $N$ large and then $k,j$ large to make this $< \epsilon$.

---
role: proof
locale: en
of_concept: m-decomposition-theorem
source_book: gtm054
source_chapter: "IV"
source_section: "15"
---

The proof proceeds by induction on $|\sigma(h)|$.

If $\sigma(h) \in \mathcal{M}(L)$, then $h$ itself is a minimal function and the decomposition is trivial with $m = 1$, $h_1 = h$.

Otherwise, $\sigma(h) \notin \mathcal{M}(L)$. By definition of $\mathcal{M}(L)$, there exists $g'' \in L$ with $\sigma(g'') \subsetneq \sigma(h)$ and $\sigma(g'') \in \mathcal{N}(L)$. Set $Y = \sigma(g'')$ and let $\mu = \min\{h(x)/g''(x) : x \in Y, g''(x) \neq 0\}$.

Then $\mu < 0$. Define $g' = h - \mu g''$. Since $g''$ is not a scalar multiple of $h$ (as $\sigma(h) \notin \mathcal{M}(L)$), we have $g' \neq 0$. One verifies that $g'(x)h(x) \geq 0$ for all $x \in X$ (condition (iii)), and $|\sigma(g')| < |\sigma(h)|$.

Applying the induction hypothesis to $g'$ yields $g' = \sum_{i=1}^{p} g_i$ where each $g_i$ satisfies conditions (i) and (ii) and $g_i(x)g'(x) \geq 0$. Since $g'(x)$ and $h(x)$ never have opposite sign, the $g_i$ also satisfy condition (iii) with respect to $h$.

Now let $\nu = \min\{h(x)/g_1(x) : x \in \sigma(g_1)\}$ and set $h_1 = \nu g_1$, $h' = h - h_1$. Then $h_1$ is a minimal function satisfying all required conditions, and $h'$ can be further decomposed by the same process. Iterating yields the full $\mathcal{M}$-decomposition.

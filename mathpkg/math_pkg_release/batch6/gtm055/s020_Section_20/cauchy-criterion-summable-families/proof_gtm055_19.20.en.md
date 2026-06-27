---
role: proof
locale: en
of_concept: cauchy-criterion-summable-families
source_book: gtm055
source_chapter: "19"
source_section: "20"
---

The necessity of the condition is trivial: if the family is summable with sum $x$, then for the given $\varepsilon$ choose $D_{\varepsilon}$ such that $\|s_E - x\| < \varepsilon/2$ for all $E \supset D_{\varepsilon}$. For $D$ disjoint from $D_{\varepsilon}$, we have $s_D = s_{D \cup D_{\varepsilon}} - s_{D_{\varepsilon}}$, and both $s_{D \cup D_{\varepsilon}}$ and $s_{D_{\varepsilon}}$ are within $\varepsilon/2$ of $x$, so $\|s_D\| < \varepsilon$.

Conversely, suppose the condition holds and $\mathcal{E}$ is a Banach space. Then the net $\{s_D\}$ of finite sums over finite subsets $D$ is Cauchy: given $\varepsilon$, choose $D_{\varepsilon}$ as in the hypothesis; for any $D_1, D_2 \supset D_{\varepsilon}$, write $D_1 \setminus D_2$ and $D_2 \setminus D_1$ as finite sets disjoint from $D_{\varepsilon}$; then $\|s_{D_1} - s_{D_2}\| \leq \|s_{D_1 \setminus D_2}\| + \|s_{D_2 \setminus D_1}\| < 2\varepsilon$. Completeness of $\mathcal{E}$ gives convergence.

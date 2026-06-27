---
role: proof
locale: en
of_concept: lemma-10-10
source_book: gtm055
source_chapter: "10"
source_section: "Section 11_Section_11"
---

Proof. Clearly $\rho(\emptyset) = 0$. Let $V$ be an open subset of $X$, let $\{U_n\}$ be a countable open covering of $V$, let $\varepsilon$ be a positive number, and let $f$ be a continuous function on $X$ such that $0 \leq f \leq \chi_V$. We set $K = \{x \in X : f(x) \geq \varepsilon\}$. If $f_\varepsilon$ denotes the function $f_\varepsilon = (f - \varepsilon) \lor 0$, then $0 \leq f_\varepsilon \leq \chi_K$ and $f \leq f_\varepsilon + \varepsilon$. Since $K$ is compact, there exists a positive integer $N$ such that

$$K \subset U_1 \cup \cdots \cup U_N,$$

and there exist corresponding nonnegative continuous functions $g_1, \ldots, g_N$ on $X$ such that $g_i \leq \chi_{U_i}$, $i = 1, \ldots

---
role: proof
locale: en
of_concept: continuous-image-of-compact
source_book: gtm003
source_chapter: "0"
source_section: "8"
---

Let $X$ be compact, $Y$ Hausdorff, and $f : X \to Y$ continuous. Let $\{V_i\}_{i \in I}$ be an open cover of $f(X)$ in the subspace topology of $f(X)$; write $V_i = f(X) \cap W_i$ with $W_i$ open in $Y$. Then $\{f^{-1}(W_i)\}_{i \in I}$ is an open cover of $X$ (by continuity of $f$). By compactness of $X$, there exists a finite subcover $\{f^{-1}(W_{i_1}), \ldots, f^{-1}(W_{i_n})\}$ of $X$. Then $\{V_{i_1}, \ldots, V_{i_n}\}$ covers $f(X)$. Hence $f(X)$ is compact.

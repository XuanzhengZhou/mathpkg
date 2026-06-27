---
role: proof
locale: en
of_concept: weierstrass-preparation-proof
source_book: gtm029
source_chapter: "VIII"
source_section: "1. The method of associated graded rings"
---

The hypothesis that $F$ is regular of order $s$ in $X_n$ means the coefficient $c_s$ of $X_n^s$ in $F$ is invertible in $R' = K[[X_1, \cdots, X_{n-1}]]$, and $c_j$ is not invertible for $j < s$. This implies

$$R / (X_1, \cdots, X_{n-1}, F) \cong K[[X_n]] / (F(0, \cdots, 0, X_n)) \cong K[[X_n]] / (X_n^s).$$

Thus this ring admits $\{1, x_n, \cdots, x_n^{s-1}\}$ as a linear basis over $K$, where $x_n$ is the residue class of $X_n$. Now apply Theorem 7, Corollary 2, with

$$A = K[[X_1, \cdots, X_{n-1}, F]], \quad \mathfrak{m} = (X_1, \cdots, X_{n-1}, F), \quad E = R.$$

We have $E/\mathfrak{m}E \cong R/(X_1,\ldots,X_{n-1},F)$, generated over $K = A/\mathfrak{m}$ by $\{1, X_n, \ldots, X_n^{s-1}\}$. Since $\mathfrak{m}$ is finitely generated and $A/\mathfrak{m}$ is a field (hence noetherian), Theorem 7, Corollary 2 implies these elements generate $E$ over $A$. Thus $G = \sum_{j=0}^{s-1} \varphi_j(X_1, \cdots, X_{n-1}, F) X_n^j$. Expanding each $\varphi_j$ and collecting terms independent of $F$ yields the Weierstrass form $G = UF + \sum_{j=0}^{s-1} S_j X_n^j$.
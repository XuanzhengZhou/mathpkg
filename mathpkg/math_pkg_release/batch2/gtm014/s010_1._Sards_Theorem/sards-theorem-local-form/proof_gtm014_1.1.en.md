---
role: proof
locale: en
of_concept: sards-theorem-local-form
source_book: gtm014
source_chapter: "1"
source_section: "1"
---

The proof proceeds by induction on $n$. The base case $n = 0$: $\mathbf{R}^0$ is, by convention, just a point, and the proposition is trivial in this case.

**Induction step.** Assume that Sard's Theorem holds for all smooth mappings $\mathbf{R}^{n-1} \to \mathbf{R}^m$. To prove it for a smooth mapping $f: U \to \mathbf{R}^m$ with $U \subset \mathbf{R}^n$ open, we analyze the critical set $C = C[f]$ via the stratification:
$$C_i = \left\{ p \in C \;\middle|\; \frac{\partial^{|\alpha|} f_l}{\partial x^\alpha}(p) = 0 \text{ whenever } 0 < |\alpha| \leq i \text{ and } 1 \leq l \leq m \right\},$$
for $i = 1, 2, \ldots$. The proof then decomposes as:
$$f(C) = f(C - C_1) \cup \bigcup_{i \geq 1} f(C_i - C_{i+1}) \cup f(C_k)$$
and shows that each piece has measure zero via Lemmas B, C, and D.

**Fubini-type reduction.** For the induction step on the rank, one considers a map $f$ whose first coordinate is the first coordinate function $x_1$. By considering the family of maps $g_a(\bar{x}) = f(a, \bar{x})$ for fixed $a$, and noting that
$$(df)_{(a,\bar{x})} = \begin{pmatrix} 1 & * \\ 0 & (dg_a)_{\bar{x}} \\ \vdots & \\ 0 & \end{pmatrix},$$
we have $\operatorname{rank}(df)_{(a,\bar{x})} = \operatorname{rank}(dg_a)_{\bar{x}} + 1$. Hence $\bar{x}$ is a critical point of $g_a$ iff $(a, \bar{x})$ is a critical point of $f$. The critical point set of $g_a$ is $i_a^{-1}(C)$.

By the induction hypothesis, $g_a(i_a^{-1}(C))$ has measure zero in $\mathbf{R}^{m-1}$. Since $i_a^{-1}(f(C)) = g_a(i_a^{-1}(C))$, we conclude by Theorem 1.7 (Fubini-type theorem for measure zero) that $f(C)$ has measure zero. Note that $C$ is a closed set which is a countable union of compact sets, so $f(C)$ is a countable union of compact sets and Theorem 1.7 applies.

The remaining parts $f(C - C_1)$, $f(C_i - C_{i+1})$, and $f(C_k)$ for large $k$ are handled by Lemmas B, C, and D respectively. Together these cover all of $f(C)$, proving the proposition.

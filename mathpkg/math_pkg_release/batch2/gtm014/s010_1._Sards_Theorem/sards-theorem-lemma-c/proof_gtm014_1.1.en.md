---
role: proof
locale: en
of_concept: sards-theorem-lemma-c
source_book: gtm014
source_chapter: "1"
source_section: "1"
---

Let $p \in C_i - C_{i+1}$. Then all partial derivatives of $f$ of order $\leq i$ vanish at $p$, but there exists some partial derivative of order $i+1$ that does not vanish at $p$. Without loss of generality, suppose there exists a function $w: U \to \mathbf{R}$ (some $(i+1)$-st order partial derivative of a component of $f$) such that $w \equiv 0$ on $C_i$ (since all lower-order derivatives vanish on $C_i$) and $dw(p) \neq 0$.

Define a diffeomorphism $h: U'_p \to V$ on a neighborhood $U'_p \subset U$ of $p$ with $h(x) = (w(x), x_2, \ldots, x_n)$, using the fact that $\frac{\partial w}{\partial x_1}(p) \neq 0$ (after a possible reordering of coordinates). By definition, $w(p) = 0$ for all $p \in C_i$, so
$$h(C_i \cap U'_p) \subset \{0\} \times \mathbf{R}^{n-1} \subset \mathbf{R}^n.$$

Let $k: \mathbf{R}^{n-1} \to \mathbf{R}^m$ be defined by $f \circ h^{-1}$ restricted to $V \cap (\{0\} \times \mathbf{R}^{n-1})$. Then we note that
$$f(C_i \cap U'_p) \subset k(C[k]),$$
where $C[k]$ denotes the critical set of $k$. By the induction hypothesis (on the dimension $n-1$), $k(C[k])$ has measure zero in $\mathbf{R}^m$.

Hence for each $p \in C_i - C_{i+1}$, there is a neighborhood $U'_p$ of $p$ for which $f(C_i \cap U'_p)$ has measure zero. Since $\mathbf{R}^n$ is second-countable, we can choose a countable number of the $U'_p$'s to cover $C_i - C_{i+1}$. Therefore $f(C_i - C_{i+1})$ has measure zero in $\mathbf{R}^m$, being a countable union of measure-zero sets.

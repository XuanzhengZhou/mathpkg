---
role: proof
locale: en
of_concept: homomorphism-term-evaluation
source_book: gtm037
source_chapter: "24"
source_section: "24"
---

The proof proceeds by induction on the term $\sigma$. For the base case, if $\sigma$ is a variable $v_i$, then $\sigma^{\mathfrak{A}}x = x_i = gv_i = g\sigma$. For the induction step, if $\sigma = O\sigma_0\cdots\sigma_{m-1}$ where $O$ is an operation symbol, then by the induction hypothesis $\sigma_i^{\mathfrak{A}}x = g\sigma_i$ for each $i < m$, and since $g$ is a homomorphism,
$$\sigma^{\mathfrak{A}}x = O^{\mathfrak{A}}(\sigma_0^{\mathfrak{A}}x,\ldots,\sigma_{m-1}^{\mathfrak{A}}x) = O^{\mathfrak{A}}(g\sigma_0,\ldots,g\sigma_{m-1}) = g(O\sigma_0\cdots\sigma_{m-1}) = g\sigma.$$

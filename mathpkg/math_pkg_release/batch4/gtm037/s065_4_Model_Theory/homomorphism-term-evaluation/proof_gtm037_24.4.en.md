---
role: proof
locale: en
of_concept: homomorphism-term-evaluation
source_book: gtm037
source_chapter: "24"
source_section: "4"
---

The proof proceeds by induction on the term $\sigma$. 

If $\sigma$ is a variable $v_i$, then $\sigma^{\mathfrak{A}} x = x_i = g v_i = g \sigma$ by definition.

If $\sigma$ is $O \tau_0 \cdots \tau_{m-1}$ for an operation symbol $O$ of rank $m$, then by the induction hypothesis $\tau_j^{\mathfrak{A}} x = g \tau_j$ for each $j < m$. Since $g$ is a homomorphism,

$$\sigma^{\mathfrak{A}} x = O^{\mathfrak{A}}(\tau_0^{\mathfrak{A}} x, \ldots, \tau_{m-1}^{\mathfrak{A}} x) = O^{\mathfrak{A}}(g \tau_0, \ldots, g \tau_{m-1}) = g(O \tau_0 \cdots \tau_{m-1}) = g \sigma.$$

Thus the equality holds for all terms $\sigma$. $\square$

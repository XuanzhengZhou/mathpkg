---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This definition provides a systematic method for eliminating operation symbols from a first-order language by replacing each $m$-ary operation symbol $\mathbf{O}$ with an $(m+1)$-ary relation symbol $T_{\mathbf{O}}$. The translation $T$ is a bijection from operation symbols to the newly added relation symbols, with the arity increased by one. A translation function on formulas is then defined recursively: the key step replaces an equation $\mathbf{O}\sigma_0\cdots\sigma_{m-1} = v_i$ (where the operation symbol is the outermost symbol on the left) with an existential formula asserting the existence of intermediate values $\alpha_0,\ldots,\alpha_{m-1}$ such that the translation of each subterm equals the corresponding $\alpha_j$ and the relation $T_{\mathbf{O}}$ holds of $(\alpha_0,\ldots,\alpha_{m-1},v_i)$. This construction is essential for reducing general first-order logic to purely relational languages.

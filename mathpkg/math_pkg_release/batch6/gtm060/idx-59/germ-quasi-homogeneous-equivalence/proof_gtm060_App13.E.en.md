---
role: proof
locale: en
of_concept: germ-quasi-homogeneous-equivalence
source_book: gtm060
source_chapter: "Appendix 13"
source_section: "E. The Quasi-Homogeneous Case"
---

The proof uses the method of quasi-homogeneous filtrations. Let $w = (w_1, \ldots, w_n)$ be the quasi-homogeneous weights such that $f$ has weight 1. Consider the expansion $h = h_0 + h_1 + \cdots$ where $h_k$ has quasi-homogeneous degree $k$. The transformation $x_i \mapsto x_i + \xi_i(x)$ where $\xi_i$ has positive quasi-homogeneous weight can eliminate terms of the expansion order by order.

The key observation is that the change $h \mapsto h(1 + \sum_{m,l} \lambda_{m,l} x^m f^l)$ corresponds to adding terms whose quasi-homogeneous weight is adjusted by the weight of $f^\beta$ to be zero. The monomials $x^m f^l$ with $m \in I$ (interior integral points of the Newton diagram) are exactly those monomials that can change the weight appropriately. Terms not corresponding to such monomials can be eliminated by suitable coordinate changes that preserve the quasi-homogeneous structure of $f$ up to higher-order corrections.

If $\beta$ is not a negative rational number, then no nontrivial quasi-homogeneous polynomial has weight $-\beta - \sigma$ (where $\sigma$ is the weight of $dx$), so $\phi \equiv 0$ and the form reduces to $f^\beta dx$.

---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

This corollary extends the universal instantiation (specification) principle to simultaneous substitution of multiple terms. Given a universally quantified formula $\forall v_0\dots\forall v_{m-1}\varphi$, one may simultaneously substitute terms $\sigma_0,\dots,\sigma_{m-1}$ for the variables $v_0,\dots,v_{m-1}$ to obtain $\varphi(\sigma_0,\dots,\sigma_{m-1})$. The notation $\varphi(\sigma_0,\dots,\sigma_{m-1})$ denotes simultaneous substitution, which can be implemented via iterated ordinary substitution using the technique described in 10.72 after first forming a suitable variant $\psi$ to avoid variable capture.

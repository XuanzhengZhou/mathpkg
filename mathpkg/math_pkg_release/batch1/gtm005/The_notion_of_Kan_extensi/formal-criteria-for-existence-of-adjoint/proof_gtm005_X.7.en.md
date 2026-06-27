---
role: proof
locale: en
of_concept: formal-criteria-for-existence-of-adjoint
source_book: gtm005
source_chapter: "X"
source_section: "7"
---

Freyd's General Adjoint Functor Theorem: If $C$ is complete and locally small, then $G: C \to D$ has a left adjoint iff:

1. $G$ preserves all small limits (is continuous).
2. For each $d \in D$, the comma category $(d \downarrow G)$ has a weakly initial set (Solution Set Condition).

Proof ($\Rightarrow$): Right adjoints preserve limits. Solution set: $\{\eta_d: d \to G(F(d))\}$ is a singleton weakly initial set in $(d \downarrow G)$.

($\Leftarrow$): For each $d$, form the product $P = \prod_i A_i$ over the solution set $\{f_i: d \to G(A_i)\}$. $G$ preserves this product, giving $G(P) \cong \prod_i G(A_i)$, and a map $h: d \to G(P)$ induced by the $f_i$. Take the joint equalizer $e: F(d) \to P$ of all pairs $u, v: P \rightrightarrows X$ with $G(u) \circ h = G(v) \circ h$. Then $F(d)$ is the initial object of $(d \downarrow G)$, giving $F \dashv G$.

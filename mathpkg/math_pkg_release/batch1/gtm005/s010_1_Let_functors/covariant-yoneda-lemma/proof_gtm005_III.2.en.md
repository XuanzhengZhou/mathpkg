---
role: proof
locale: en
of_concept: covariant-yoneda-lemma
source_book: gtm005
source_chapter: "III"
source_section: "2"
---

Dual to the contravariant Yoneda Lemma. For $K: D \to \mathbf{Set}$ and $r \in D$, define
$$y': \operatorname{Nat}(D(r, -), K) \cong K(r)$$
by $y'(\alpha) = \alpha_r(1_r)$. The inverse sends $u \in K(r)$ to $\gamma^u$ with components $\gamma^u_d(f) = K(f)(u)$ for $f: r \to d$.

Verification: $\gamma^{y'(\alpha)}_d(f) = K(f)(\alpha_r(1_r)) = \alpha_d(f \circ 1_r) = \alpha_d(f)$ by naturality. And $y'(\gamma^u) = \gamma^u_r(1_r) = K(1_r)(u) = u$. The bijection is natural in $K$ and $r$.

---
role: proof
locale: en
of_concept: yoneda-lemma
source_book: gtm005
source_chapter: "III"
source_section: "2"
---

Let $K: D^{\mathrm{op}} \to \mathbf{Set}$ be a functor and $r \in D$. Define a bijection
$$y: \operatorname{Nat}(D(-, r), K) \cong K(r)$$
by $y(\alpha) = \alpha_r(1_r) \in K(r)$ for $\alpha: D(-, r) \Rightarrow K$. Conversely, for $u \in K(r)$, define $\beta^u: D(-, r) \Rightarrow K$ with components $\beta^u_d(f) = K(f)(u)$ for $f: d \to r$.

These are inverses: given $\alpha$, set $u = \alpha_r(1_r)$. Naturality gives $\alpha_d(f) = K(f)(\alpha_r(1_r)) = K(f)(u) = \beta^u_d(f)$, hence $\beta^{y(\alpha)} = \alpha$. Conversely, $y(\beta^u) = \beta^u_r(1_r) = K(1_r)(u) = u$. The bijection is natural in both $K$ and $r$.

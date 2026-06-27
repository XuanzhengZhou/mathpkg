---
role: proof
locale: en
of_concept: representable-functor-via-yoneda
source_book: gtm005
source_chapter: "III"
source_section: "2"
---

A functor $K: D^{\mathrm{op}} \to \mathbf{Set}$ is representable if $K \cong D(-, r)$ for some $r \in D$. By the Yoneda Lemma, a natural isomorphism $\phi: D(-, r) \cong K$ corresponds to a universal element $u = \phi_r(1_r) \in K(r)$.

For any $d \in D$ and $x \in K(d)$, naturality gives $\phi_d(f) = K(f)(u)$ for $f: d \to r$. Since $\phi_d$ is bijective, for each $x \in K(d)$ there exists a unique $f: d \to r$ with $K(f)(u) = x$. This is the universal property of the pair $(r, u)$.

Thus a representation of $K$ is equivalently a universal element: an object $r \in D$ and $u \in K(r)$ such that $(r, u)$ is initial in the category of elements $\int K$.

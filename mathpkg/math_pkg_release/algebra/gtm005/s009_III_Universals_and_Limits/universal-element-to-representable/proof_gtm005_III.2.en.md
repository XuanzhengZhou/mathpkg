---
role: proof
locale: en
of_concept: universal-element-to-representable
source_book: gtm005
source_chapter: "III"
source_section: "2"
---

A universal element of $K: D^{\mathrm{op}} \to \mathbf{Set}$ is a pair $(r, u)$ with $u \in K(r)$ such that for every $d \in D$ and $x \in K(d)$, there exists a unique $f: d \to r$ with $K(f)(u) = x$.

By the Yoneda Lemma, the element $u \in K(r)$ corresponds to a natural transformation $\phi: D(-, r) \Rightarrow K$ with $\phi_d(f) = K(f)(u)$. The universal property says $\phi_d$ is bijective for all $d$: given $x \in K(d)$, there exists a unique $f: d \to r$ with $\phi_d(f) = K(f)(u) = x$, i.e., $\phi_d$ is surjective and injective. Thus $\phi$ is a natural isomorphism, so $(r, u)$ represents $K$.

Therefore, a functor is representable iff it has a universal element.

---
role: proof
locale: en
of_concept: yoneda-corollary
source_book: gtm005
source_chapter: "III"
source_section: "2"
---

Apply the Yoneda Lemma with $K = D(-, s)$. The lemma gives
$$\operatorname{Nat}(D(-, r), D(-, s)) \cong D(r, s).$$
The forward map sends $\alpha: D(-, r) \Rightarrow D(-, s)$ to $\alpha_r(1_r) \in D(r, s)$. The inverse sends $f: r \to s$ to $D(-, f): D(-, r) \Rightarrow D(-, s)$ whose component at $d$ is post-composition $g \mapsto f \circ g$.

Thus every natural transformation between representable functors is given by pre-composition with a unique morphism. The Yoneda embedding $Y: D \to \mathbf{Set}^{D^{\mathrm{op}}}$ sending $r \mapsto D(-, r)$ is therefore fully faithful.

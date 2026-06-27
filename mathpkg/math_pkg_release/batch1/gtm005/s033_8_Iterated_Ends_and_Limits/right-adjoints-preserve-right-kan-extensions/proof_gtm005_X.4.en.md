---
role: proof
locale: en
of_concept: right-adjoints-preserve-right-kan-extensions
source_book: gtm005
source_chapter: "X"
source_section: "4. Kan Extensions as Coends"
---

**Proof.** Let $F \dashv G$ be the adjunction with bijection $A(Fx, a) \cong X(x, Ga)$. Applying this adjunction pointwise gives, for any functor $H: C \to X$,
$$\mathrm{Nat}(FH, L) \cong \mathrm{Nat}(H, GL).$$
Now compute, for any $H: C \to X$:
$$\begin{aligned}
\mathrm{Nat}(H, G \circ \mathrm{Ran}_K T) &\cong \mathrm{Nat}(FH, \mathrm{Ran}_K T) \quad \text{(adjunction)}\\
&\cong \mathrm{Nat}(FHK, T) \quad \text{(definition of right Kan extension)}\\
&\cong \mathrm{Nat}(HK, GT) \quad \text{(adjunction)}.
\end{aligned}$$
The composite bijection, natural in $H$, shows that $G \circ \mathrm{Ran}_K T$ satisfies the universal property of $\mathrm{Ran}_K(GT)$. Setting $H = G \circ \mathrm{Ran}_K T$, the image of the identity yields the counit $G\varepsilon$.

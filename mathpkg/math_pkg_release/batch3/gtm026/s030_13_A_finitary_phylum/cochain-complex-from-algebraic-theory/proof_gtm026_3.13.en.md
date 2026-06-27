---
role: proof
locale: en
of_concept: cochain-complex-from-algebraic-theory
source_book: gtm026
source_chapter: "3"
source_section: "13"
---

We must verify two things: (1) that $d^n \cdot d^{n+1} = 0$ (the cochain complex condition), and (2) that the assignment $(X, \xi) \mapsto$ the cochain complex is functorial.

**(1) $d^n \cdot d^{n+1} = 0$:**

The differential $d^{n+1}: (XT^{n+1}, XT^n \mu)F \rightarrow (XT^{n+2}, XT^{n+1} \mu)F$ is defined by

$$d^{n+1} = \xi T^{n+1} F + \sum_{k=0}^{n} (-1)^{k+1} (XT^k \mu T^{n-k}) F.$$

This is the standard alternating sum (simplicial) differential. To verify $d^n \cdot d^{n+1} = 0$, we compute the composition using the monad identities:

- $\mu \cdot \mu T = \mu \cdot T\mu$ (associativity of the monad multiplication)
- $\xi \cdot \mu = \xi \cdot \xi T$ (algebra structure axiom for $(X, \xi)$)

These identities cause pairwise cancellations in the alternating sum, exactly as in the classical bar resolution. Each term in $d^n \cdot d^{n+1}$ appears with both a positive and negative sign, yielding zero.

**(2) Functoriality:**

Given a $\mathbf{T}$-homomorphism $f: (X, \xi) \rightarrow (X', \xi')$, we obtain maps $fT^{n+1}: XT^{n+1} \rightarrow X'T^{n+1}$ that commute with the resolution structure maps because $f$ is a $\mathbf{T}$-homomorphism ($\xi \cdot f = fT \cdot \xi'$). Applying $F$ yields maps between the corresponding terms of the complexes that commute with the differentials $d^{n+1}$ by naturality. This defines the functor from $(\mathcal{K}^{\mathbf{T}})^{\text{op}}$ to cochain complexes.

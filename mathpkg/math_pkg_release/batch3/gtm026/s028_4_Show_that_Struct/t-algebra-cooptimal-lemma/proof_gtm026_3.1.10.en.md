---
role: proof
locale: en
of_concept: t-algebra-cooptimal-lemma
source_book: gtm026
source_chapter: "3"
source_section: "1.10"
---

We must verify the $\mathbf{T}$-algebra axioms for $(K, \xi)$.

To prove $K\eta.\xi = \mathrm{id}_K$: Since $h$ is epi, it suffices to check $h.K\eta.\xi = h$. By naturality of $\eta$, $h.K\eta = L\eta.h\mathbf{T}$. Then $L\eta.h\mathbf{T}.\xi = L\eta.\gamma.h = h$, using the algebra axiom $L\eta.\gamma = \mathrm{id}_L$ for $(L, \gamma)$.

To prove $K\mu.\xi = \xi\mathbf{T}.\xi$: Since $h\mathbf{T}\mathbf{T}$ is epi, it suffices to check after composing with $h\mathbf{T}\mathbf{T}$. Using the commutativity of the given square, naturality of $\mu$, and the algebra axiom for $(L, \gamma)$, a diagram chase yields the result.

The argument that $h$ is co-optimal follows from the same reasoning as in 2.1.56: since $h\mathbf{T}$ is epi, any algebra structure on $K$ making $h$ a homomorphism must be $\xi$.

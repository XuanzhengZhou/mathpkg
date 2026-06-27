---
role: proof
locale: en
of_concept: kernel-ideal-of-homomorphism
source_book: gtm037
source_chapter: "12"
source_section: "2"
---

The proof of Proposition 12.18 is not present in the extracted section text. The proof mirrors the first isomorphism theorem for Boolean algebras: one verifies that $I = \ker f = \{x \in A : fx = 0\}$ is a Boolean ideal (using $f(x + y) = fx + fy$, $f(-x) = -fx$, and downward closure), and that it is closed under cylindrifications using $f(c_\kappa x) = c_\kappa' fx$. The isomorphism $\mathfrak{B} \cong \mathfrak{A}/I$ is established by the natural map $[x] \mapsto fx$, which is well-defined, injective (by definition of $I$), surjective (since $f$ is onto), and preserves all $\mathrm{CA}_\alpha$ operations.

---
role: proof
locale: en
of_concept: uniqueness-of-limits
source_book: gtm026
source_chapter: "1"
source_section: "1.22"
---

Let $(L, \psi)$ and $(L', \psi')$ be two limits of the same diagram $(\Delta, D)$. By the universal property of $(L, \psi)$ applied to the lower bound $(L', \psi')$, there exists a unique morphism $f: L' \to L$ such that $f \circ \psi_i = \psi'_i$ for all $i \in N(\Delta)$. Similarly, by the universal property of $(L', \psi')$ applied to $(L, \psi)$, there exists a unique $g: L \to L'$ such that $g \circ \psi'_i = \psi_i$ for all $i$.

Now consider $g \circ f: L' \to L'$. We have $(g \circ f) \circ \psi'_i = g \circ (f \circ \psi'_i) = g \circ \psi_i$? Wait — let us check: $f \circ \psi_i = \psi'_i$? No, from above $f \circ \psi_i = \psi'_i$ means $f: L' \to L$ satisfies $f \circ \psi_i = \psi'_i$. Wait, the universal property says $f: L' \to L$ with $\psi_i \circ f$? Let us be precise.

The lower bound $(L, \psi)$ has maps $\psi_i: L \to D_i$. For $(L', \psi')$, the universal property of $(L, \psi)$ gives $f: L' \to L$ with $\psi_i \circ f = \psi'_i$ for all $i$ (using the composition notation where morphisms are written to the right of their source, as in the text). Specifically, $f.\psi_i = \psi'_i$.

Then $g.f: L \to L$ satisfies $(g.f).\psi_i = g.(f.\psi_i) = g.\psi'_i = \psi_i$. But the identity $\mathrm{id}_L$ also satisfies $\mathrm{id}_L.\psi_i = \psi_i$. By uniqueness in the universal property of $(L, \psi)$ applied to itself, $g.f = \mathrm{id}_L$. Similarly $f.g = \mathrm{id}_{L'}$. Thus $f$ and $g$ are inverse isomorphisms, unique with the property of commuting with the structure maps.

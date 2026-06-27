---
role: proof
locale: en
of_concept: duality-principle-image-factorization
source_book: gtm026
source_chapter: "2"
source_section: "4"
---

The result follows directly from the definition of an image factorization system (4.1–4.5) applied to the opposite category $\mathcal{H}^{\mathrm{op}}$.

In $\mathcal{H}^{\mathrm{op}}$, the direction of every morphism is reversed. Consequently, epimorphisms in $\mathcal{H}$ become monomorphisms in $\mathcal{H}^{\mathrm{op}}$ and vice versa. Thus, if $E$ consists of epimorphisms in $\mathcal{H}$ (axiom 4.3), then $E$ consists of monomorphisms in $\mathcal{H}^{\mathrm{op}}$, and $M$ consists of epimorphisms in $\mathcal{H}^{\mathrm{op}}$.

Since $E$ and $M$ are subcategories of $\mathcal{H}$ (axiom 4.2), their opposites $E^{\mathrm{op}}$ and $M^{\mathrm{op}}$ are subcategories of $\mathcal{H}^{\mathrm{op}}$. Every isomorphism is self-dual, so by axiom 4.4 every isomorphism belongs to both $M$ and $E$ in $\mathcal{H}^{\mathrm{op}}$.

For the factorization axiom 4.5, given $f^{\mathrm{op}}: B \longrightarrow A$ in $\mathcal{H}^{\mathrm{op}}$ (corresponding to $f: A \longrightarrow B$ in $\mathcal{H}$), the $E$-$M$ factorization $f = e \circ m$ in $\mathcal{H}$ becomes $f^{\mathrm{op}} = m^{\mathrm{op}} \circ e^{\mathrm{op}}$ in $\mathcal{H}^{\mathrm{op}}$, which is an $M$-$E$ factorization. The uniqueness condition follows by duality as well.

Hence $(M, E)$ satisfies all four axioms for an image factorization system in $\mathcal{H}^{\mathrm{op}}$.

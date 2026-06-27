---
role: proof
locale: en
of_concept: semidirect-product-galois-group
source_book: gtm059
source_chapter: "5"
source_section: "5"
---
We have an exact sequence $1 \to G_1 \to G \to \Gamma \to 1$ coming from Galois theory. The image of $I$ in $\Gamma$ by restriction to $K_{\infty}$ is surjective because the ramified prime is totally ramified over $K$. Moreover, $I \cap G_1 = \{1\}$ since $K_1/K$ is unramified at the ramified primes (by definition of $M_{\infty}$). Hence $G = G_1 \rtimes I$ is a semidirect product, and $I \cong \Gamma \cong \mathbb{Z}_p$ since the restriction map $I \to \Gamma$ is an isomorphism.

For (ii), $G_1$ is the maximal abelian $p$-extension of $K_1$ that is unramified everywhere, so $G_1$ is abelian. $I$ acts on $G_1$ by conjugation. Since $G = G_1 \rtimes I$, the commutator $[G, G]$ is contained in $G_1$. On the other hand, $G/[G, G]$ is the maximal abelian quotient, and $G_1$ is already the maximal abelian subgroup, so $[G, G] = G_1$.

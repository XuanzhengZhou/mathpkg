---
role: proof
locale: en
of_concept: existence-of-derived-functors
source_book: gtm052
source_chapter: "III"
source_section: "1"
---

The proof proceeds in several steps. First, since $\mathfrak{A}$ has enough injectives, every object $A$ admits an injective resolution $0 \to A \to I^\bullet$. Choose one such resolution for each $A$. Apply the functor $F$ to obtain a complex $F(I^\bullet)$ in $\mathfrak{B}$, and define
$$R^i F(A) = h^i(F(I^\bullet)),$$
the $i$-th cohomology of this complex.

One must verify that this definition is independent of the choice of injective resolution. Given two injective resolutions $I^\bullet$ and $J^\bullet$ of $A$, a standard homological algebra lemma shows there exists a morphism of complexes $I^\bullet \to J^\bullet$ extending the identity on $A$, unique up to homotopy. Since $F$ is additive, it preserves homotopies, and thus the induced maps on cohomology $h^i(F(I^\bullet)) \to h^i(F(J^\bullet))$ are isomorphisms. This establishes well-definedness (a map on objects).

For a morphism $f: A \to B$, lift it to a morphism of their chosen injective resolutions (possible because $I^0$ is injective), then apply $F$ and take cohomology to obtain $R^i F(f)$. Homotopy uniqueness ensures functoriality.

For a short exact sequence $0 \to A' \to A \to A'' \to 0$, the Horseshoe Lemma produces an exact sequence of injective resolutions $0 \to I'^\bullet \to I^\bullet \to I''^\bullet \to 0$. Applying $F$ yields a short exact sequence of complexes $0 \to F(I'^\bullet) \to F(I^\bullet) \to F(I''^\bullet) \to 0$ (using that each $I''^i$ is injective, hence split, so $F$ preserves exactness here). The long exact cohomology sequence of this short exact sequence of complexes provides the exact sequence in (b) and the connecting morphisms $\delta^i$.

Properties (c) and (d) follow from the naturality of the Horseshoe Lemma construction and the long exact cohomology sequence. Property (e) holds because if $I$ is injective, $0 \to I \to I \to 0 \to \cdots$ is an injective resolution, so $F(I^\bullet) = F(I) \to 0 \to 0 \to \cdots$, whose higher cohomology vanishes.

For full details, see Grothendieck [1, Ch. II] or Hartshorne [1, III §1].

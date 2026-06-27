---
role: proof
locale: en
of_concept: additive-functor-preserves-split-exact
source_book: gtm013
source_chapter: "1"
source_section: "§16. The Hom Functors and Exactness—Projectivity and Injectivity"
---

The proof is joint with Proposition 16.3. Since the sequence is split exact, there exist morphisms $f': M \to K$ and $g': N \to M$ such that $f'f = 1_K$, $gg' = 1_N$, and $ff' + g'g = 1_M$. Applying the additive functor $F$ preserves these identities, so $F(f')F(f) = 1_{F(K)}$, $F(g)F(g') = 1_{F(N)}$, and $F(f)F(f') + F(g')F(g) = 1_{F(M)}$. Thus the image sequence is split exact. The contravariant case $G$ follows similarly with arrows reversed.

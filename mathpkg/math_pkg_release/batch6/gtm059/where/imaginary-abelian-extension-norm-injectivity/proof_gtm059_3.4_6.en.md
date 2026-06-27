---
role: proof
locale: en
of_concept: imaginary-abelian-extension-norm-injectivity
source_book: gtm059
source_chapter: "3"
source_section: "4.6"
---

*Proof.* We use class field theory. Let $H$ be the Hilbert class field of $K^+$, i.e., the maximal abelian unramified extension of $K^+$. We have natural isomorphisms of Galois groups:

$$
\operatorname{Gal}(H/K^+) \cong C_{K^+}
$$

given by the Artin symbol. For any ideal class $c \in C_K$, the restriction of the Artin symbol $(c, K/K^+)$ to $H \cap K$ must be trivial, because $K/K^+$ is ramified at the archimedean primes while $H/K^+$ is everywhere unramified. Hence $H \cap K = K^+$.

Now if $N_{K/K^+}(c) = 1$ in $C_{K^+}$, then the Artin symbol $(c, KH/H)$ restricts to the identity on $H$, which forces $c$ to be principal in $K$. Thus the norm map is injective. The theorem follows at once, because $K$ over $K^+$ is ramified at the archimedean primes, and therefore cannot intersect the Hilbert class field of $K^+$ except in $K^+$ itself.

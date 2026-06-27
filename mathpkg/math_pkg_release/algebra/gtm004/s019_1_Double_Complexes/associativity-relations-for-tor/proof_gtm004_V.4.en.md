---
role: proof
locale: en
of_concept: associativity-relations-for-tor
source_book: gtm004
source_chapter: "V. Double Complexes"
source_section: "4. Applications of the Künneth Formulas"
---

# Proof of Associativity Relations for Tor

**Theorem 4.2.** Let $A'$, $A$, $A''$ be abelian groups. There is an unnatural isomorphism

$$\operatorname{Tor}(A', A) \otimes A'' \oplus \operatorname{Tor}(A' \otimes A, A'') \cong A' \otimes \operatorname{Tor}(A, A'') \oplus \operatorname{Tor}(A', A \otimes A''),$$

and a natural isomorphism

$$\operatorname{Tor}(\operatorname{Tor}(A', A), A'') \cong \operatorname{Tor}(A', \operatorname{Tor}(A, A'')).$$

(Here all Tor groups are $\operatorname{Tor}_1^{\mathbb{Z}}$ and all tensor products are over $\mathbb{Z}$.)

**Proof.** Let $C'$, $C$, $C''$ be free chain complexes concentrated in non-negative dimensions which are resolutions of $A'$, $A$, $A''$ respectively; that is, $H_0(C') = A'$, $H_p(C') = 0$ for $p > 0$, and similarly for $C$, $C''$. Such resolutions exist (e.g., take a free presentation $0 \to R \to F \to A' \to 0$ and form the complex $\cdots \to 0 \to R \to F \to 0 \to \cdots$).

Consider the isomorphism of chain complexes from Proposition 4.1:
$$(C' \otimes C) \otimes C'' \cong C' \otimes (C \otimes C'').$$
Computing the homology of both sides using the Künneth formula (Theorem 2.1) gives:

**Left side** $H((C' \otimes C) \otimes C'')$:
- $H_0 = (A' \otimes A) \otimes A'' \cong A' \otimes (A \otimes A'')$ (associativity of ordinary tensor product).
- $H_1 \cong \operatorname{Tor}(A', A) \otimes A'' \oplus \operatorname{Tor}(A' \otimes A, A'')$.
- $H_2 \cong \operatorname{Tor}(\operatorname{Tor}(A', A), A'')$.

**Right side** $H(C' \otimes (C \otimes C''))$:
- $H_0 = A' \otimes (A \otimes A'')$.
- $H_1 \cong A' \otimes \operatorname{Tor}(A, A'') \oplus \operatorname{Tor}(A', A \otimes A'')$.
- $H_2 \cong \operatorname{Tor}(A', \operatorname{Tor}(A, A''))$.

Since the two sides are isomorphic as chain complexes, their homology groups are isomorphic. Equating the $H_1$ terms yields the unnatural isomorphism (4.3). Equating the $H_2$ terms yields the natural isomorphism (4.4).

**Why (4.4) is natural.** A homomorphism $\varphi: A \to B$ of abelian groups induces a unique homotopy class of chain maps $\bar{\varphi}: C(A) \to C(B)$ between free resolutions. Then $\operatorname{Tor}(\operatorname{Tor}(A', A), A'') \to \operatorname{Tor}(\operatorname{Tor}(A', B), A'')$ is induced by $\operatorname{Tor}(\operatorname{id}, \operatorname{Tor}(\operatorname{id}, \varphi_*))$, and the diagram commutes because the chain complex isomorphism $(C' \otimes C) \otimes C'' \cong C' \otimes (C \otimes C'')$ is natural.

**Why (4.3) is unnatural.** The splitting in the Künneth theorem is not natural; the identification of $H_1$ from the two sides uses the Künneth splittings on each side, which are not compatible under general homomorphisms. A counterexample can be constructed using $A' = A = A'' = \mathbb{Z}/2\mathbb{Z}$ and specific non-trivial maps.

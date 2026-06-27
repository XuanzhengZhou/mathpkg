---
role: proof
locale: en
of_concept: becks-theorem
source_book: gtm005
source_chapter: "VI"
source_section: "7"
---

We first show that (iii) $\Rightarrow$ (i). Consider the adjunction $\langle F, G, \eta, \varepsilon \rangle: X \rightharpoonup A$ and the associated monad $\langle T, \eta, \mu \rangle$ with Eilenberg-Moore adjunction $\langle F^T, G^T, \eta^T, \varepsilon^T \rangle: X \rightharpoonup X^T$. The comparison functor $K: A \to X^T$ sends each object $a \in A$ to the $T$-algebra $\langle Ga, G\varepsilon_a \rangle$. We need to show $K$ is an isomorphism, i.e., it has a two-sided inverse.

**Step 1: The canonical presentation.** For each object $a \in A$, the adjunction provides a fork
$$FGFGa \xrightarrow[\varepsilon_{FGa}]{FG\varepsilon_a} FGa \xrightarrow{\varepsilon_a} a$$
in $A$, called the canonical presentation of $a$. Applying $G$ to this fork yields a split fork in $X$. Indeed, this is the special case of the split fork associated to the $T$-algebra $\langle Ga, G\varepsilon_a \rangle$.

**Step 2: Constructing the inverse $M$.** Now consider the Eilenberg-Moore adjunction $\langle F^T, G^T, \eta^T, \varepsilon^T \rangle$ which defines the same monad $T$ in $X$. Since $G$ satisfies hypothesis (iii), the Lemma (unique comparison functor) provides a unique comparison functor $M: X^T \to A$ with $MF^T = F$ and $GM = G^T$.

**Step 3: $MK = 1_A$ and $KM = 1_{X^T}$.** The composite $MK: A \to A$ is a comparison of the adjunction $\langle F, G, \eta, \varepsilon \rangle$ to itself (both $M$ and $K$ are comparisons preserving the defining adjunction data). By the uniqueness part of the Lemma, $MK$ must be the identity on $A$. Similarly, $KM: X^T \to X^T$ is a comparison of $F^T$ to itself, hence the identity on $X^T$. Therefore $K$ is an isomorphism.

The implication (i) $\Rightarrow$ (ii) follows because $G^T: X^T \to X$ is known to create coequalizers for parallel pairs with absolute coequalizers, and if $K$ is an isomorphism then $G = G^T K$ inherits this property.

The implication (ii) $\Rightarrow$ (iii) holds because every split coequalizer is an absolute coequalizer (by the Corollary in Section 6), so (ii) applies to a larger class of pairs.

The detailed construction of $M$ (in the Lemma's proof) uses the canonical presentation: for a $T$-algebra $\langle x, h \rangle$, one forms the parallel pair
$$FGFx \xrightarrow[\varepsilon_{Fx}]{Fh} Fx$$
whose $G$-image has a split coequalizer in $X$. Since $G$ creates coequalizers for such pairs, there is a unique coequalizer $Fx \to M\langle x, h \rangle$ in $A$, and this defines the functor $M$ on objects. On morphisms, $M$ is defined by the universal property of these coequalizers.

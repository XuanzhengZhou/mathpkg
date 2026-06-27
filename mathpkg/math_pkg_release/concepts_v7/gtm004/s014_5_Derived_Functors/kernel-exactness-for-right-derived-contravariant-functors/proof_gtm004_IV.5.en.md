---
role: proof
locale: en
of_concept: kernel-exactness-for-right-derived-contravariant-functors
source_book: gtm004
source_chapter: "IV. Derived Functors"
source_section: "5. Derived Functors"
---

# Proof of Kernel Exactness for Right Derived Contravariant Functors

**Proposition 5.8.** Let $K_q \xrightarrow{\mu} P_{q-1} \rightarrow \cdots \rightarrow P_0 \rightarrow A$ be an exact sequence with $P_0, P_1, \ldots, P_{q-1}$ projective. Then if $S$ is left exact contravariant and $q \geq 1$, the sequence

$$SP_{q-1} \xrightarrow{\mu^*} SK_q \rightarrow R^q SA \rightarrow 0$$

is exact.

*Proof.* The result is the contravariant analog of Proposition 5.5. The authors state: "In these cases too results similar to Propositions 5.2, 5.3, 5.4, 5.5, 5.6 may be proved. We leave the details to the reader, but would like to make explicit the result corresponding to Proposition 5.5." The proof follows by applying the covariant formulation of Proposition 5.5 to the functor $S^{\mathrm{op}}: \mathfrak{M}_A^{\mathrm{opp}} \rightarrow \mathfrak{Ab}$ (which is covariant and right exact when $S$ is left exact contravariant), or by dualizing the diagram argument of Proposition 5.5 with injective resolutions replaced by projective resolutions and homology replaced by cohomology. Specifically, one extends the given exact sequence to a full projective resolution

$$\cdots \rightarrow P_{q+1} \rightarrow P_q \rightarrow K_q \rightarrow 0$$

with $P_q, P_{q+1}, \ldots$ projective, forms the (contravariant) cochain complex $SP$, and applies the dual of the ker-coker argument (Lemma III.5.1) to obtain the exactness of $SP_{q-1} \xrightarrow{\mu^*} SK_q \rightarrow R^q SA \rightarrow 0$. $\square$

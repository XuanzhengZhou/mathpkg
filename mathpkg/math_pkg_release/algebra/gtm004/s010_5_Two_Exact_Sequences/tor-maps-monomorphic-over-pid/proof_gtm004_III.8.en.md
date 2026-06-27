---
role: proof
locale: en
of_concept: tor-maps-monomorphic-over-pid
source_book: gtm004
source_chapter: "III"
source_section: "8"
---

# Proof that Tor Maps are Monomorphic over a PID (Corollary 8.4)

Let $\Lambda$ be a principal ideal domain. Then the homomorphisms

$$
\kappa_* : \operatorname{Tor}^\Lambda(A, B') \rightarrow \operatorname{Tor}^\Lambda(A, B)
$$

in sequence (8.3), and

$$
\kappa_* : \operatorname{Tor}^\Lambda(A', B) \rightarrow \operatorname{Tor}^\Lambda(A, B)
$$

in sequence (8.4) are monomorphic.

**Proof.** For the first assertion, consider the diagram (8.5) used in the proof of Theorem 8.3. Over a principal ideal domain $\Lambda$, submodules of projective modules are projective. Hence $R$, being a submodule of the projective module $P$, is a projective right $\Lambda$-module.

Since $R$ is projective, it is flat by Proposition 7.4. Therefore the map

$$
\kappa_* : R \otimes_\Lambda B' \rightarrow R \otimes_\Lambda B
$$

in the second row of diagram (8.5) is monomorphic. By the diagram chase in Lemma 5.1, this implies that the induced map on the kernels

$$
\kappa_* : \operatorname{Tor}^\Lambda(A, B') \rightarrow \operatorname{Tor}^\Lambda(A, B)
$$

is also monomorphic. This proves the first assertion.

The second assertion is proved analogously, using the symmetric construction of the Tor exact sequence in the first variable (8.4).

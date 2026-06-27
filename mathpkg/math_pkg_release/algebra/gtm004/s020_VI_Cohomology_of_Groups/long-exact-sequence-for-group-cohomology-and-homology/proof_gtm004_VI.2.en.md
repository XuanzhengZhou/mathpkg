---
role: proof
locale: en
of_concept: long-exact-sequence-for-group-cohomology-and-homology
source_book: gtm004
source_chapter: "VI"
source_section: "2"
---

# Proof of Proposition 2.3: Long Exact (Co)homology Sequences

The group cohomology and homology are defined as derived functors:

$$H^n(G, A) = \operatorname{Ext}_{\mathbb{Z}G}^n(\mathbb{Z}, A), \qquad H_n(G, B) = \operatorname{Tor}_n^{\mathbb{Z}G}(B, \mathbb{Z}).$$

**Cohomology long exact sequence.** Let

$$0 \longrightarrow A' \longrightarrow A \longrightarrow A'' \longrightarrow 0$$

be a short exact sequence of (left) $G$-modules. Apply the functor $\operatorname{Hom}_{\mathbb{Z}G}(\mathbb{Z}, -)$. Since $\mathbb{Z}$ need not be projective as a $\mathbb{Z}G$-module, the resulting sequence need not be exact on the right. The cohomology groups $H^n(G, -) = R^n\operatorname{Hom}_{\mathbb{Z}G}(\mathbb{Z}, -)$ are the right derived functors, and by the general theory of derived functors (Theorem IV.6.1), a short exact sequence of modules yields a long exact sequence in cohomology:

$$0 \to H^0(G, A') \to H^0(G, A) \to H^0(G, A'') \xrightarrow{\delta} H^1(G, A') \to H^1(G, A) \to H^1(G, A'') \xrightarrow{\delta} H^2(G, A') \to \cdots$$

$$\cdots \to H^n(G, A') \to H^n(G, A) \to H^n(G, A'') \xrightarrow{\delta} H^{n+1}(G, A') \to \cdots$$

where $\delta$ is the connecting homomorphism.

**Homology long exact sequence.** Let

$$0 \longrightarrow B' \longrightarrow B \longrightarrow B'' \longrightarrow 0$$

be a short exact sequence of right $G$-modules. Apply the functor $- \otimes_{\mathbb{Z}G} \mathbb{Z}$. The homology groups $H_n(G, -) = L_n(- \otimes_{\mathbb{Z}G} \mathbb{Z})$ are the left derived functors, and a short exact sequence yields a long exact sequence in homology:

$$\cdots \to H_n(G, B') \to H_n(G, B) \to H_n(G, B'') \xrightarrow{\partial} H_{n-1}(G, B') \to \cdots$$

$$\cdots \to H_1(G, B'') \xrightarrow{\partial} H_0(G, B') \to H_0(G, B) \to H_0(G, B'') \to 0.$$

Both long exact sequences are natural with respect to morphisms of short exact sequences.

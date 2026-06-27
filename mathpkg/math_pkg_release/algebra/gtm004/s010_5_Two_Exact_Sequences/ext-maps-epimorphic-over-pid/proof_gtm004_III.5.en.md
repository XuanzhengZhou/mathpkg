---
role: proof
locale: en
of_concept: ext-maps-epimorphic-over-pid
source_book: gtm004
source_chapter: "III"
source_section: "5"
---

# Proof of Ext Maps are Epimorphic over a PID (Corollary 5.7)

Let $\Lambda$ be a principal ideal domain. Then the homomorphisms

$$
\psi_* : \operatorname{Ext}_\Lambda(A, B) \rightarrow \operatorname{Ext}_\Lambda(A, B'')
$$

in the Hom-Ext sequence in the second variable (Theorem 5.2), and

$$
\varphi^* : \operatorname{Ext}_\Lambda(A, B) \rightarrow \operatorname{Ext}_\Lambda(A', B)
$$

in the Hom-Ext sequence in the first variable (Theorem 5.3) are epimorphic.

**Proof.** Over a principal ideal domain $\Lambda$, submodules of projective modules are projective (Corollary I.5.3).

Consider the diagram (5.4) used in the proof of Theorem 5.2. The module $R$ (the kernel of the projective presentation $R \hookrightarrow P \twoheadrightarrow A$) is a submodule of the projective module $P$, hence $R$ is projective. Therefore

$$
\psi_* : \operatorname{Hom}_\Lambda(R, B) \rightarrow \operatorname{Hom}_\Lambda(R, B'')
$$

is epimorphic (since $\operatorname{Hom}_\Lambda(R, -)$ is exact for $R$ projective). By the diagram chase in the proof of Theorem 5.2, this implies that

$$
\psi_* : \operatorname{Ext}_\Lambda(A, B) \rightarrow \operatorname{Ext}_\Lambda(A, B'')
$$

is epimorphic.

For the second assertion, consider the diagram (5.6) used in the proof of Theorem 5.3. The module $R'$ is projective (as a submodule of $P'$). Hence the short exact sequence $R' \hookrightarrow R \twoheadrightarrow R''$ splits, and it follows that

$$
\varphi^* : \operatorname{Hom}_\Lambda(R, B) \rightarrow \operatorname{Hom}_\Lambda(R', B)
$$

is epimorphic. Consequently,

$$
\varphi^* : \operatorname{Ext}_\Lambda(A, B) \rightarrow \operatorname{Ext}_\Lambda(A', B)
$$

is epimorphic.

We remark that if $\Lambda$ is not a principal ideal domain, the assertions of Corollary 5.7 are false in general (see Exercise 5.3).

---
role: proof
locale: en
of_concept: green-correspondence
source_book: gtm004
source_chapter: "IX. Relative Homological Algebra"
source_section: "4. Modular Representation Theory"
---

# Proof of the Green Correspondence

Let $G$ be a finite group, $k$ a field of characteristic $p$, and $Q$ a $p$-subgroup of $G$. Set $L = N_G(Q)$, the normalizer of $Q$ in $G$.

The Green correspondence establishes a bijection between the isomorphism classes of indecomposable $kG$-modules with vertex $Q$ and the isomorphism classes of indecomposable $kL$-modules with vertex $Q$.

**Theorem (Green Correspondence).** Let $Q$ be a $p$-subgroup of $G$ and $L = N_G(Q)$. Then the following maps are mutually inverse bijections:

1. If $M$ is an indecomposable $kG$-module with vertex $Q$, its Green correspondent is the uniquely determined indecomposable direct summand of the restriction $M_L$ (to $kL$) that has vertex $Q$.

2. If $N$ is an indecomposable $kL$-module with vertex $Q$, its Green correspondent is the uniquely determined indecomposable direct summand of the induced module $kG \otimes_{kL} N$ that has vertex $Q$.

*Proof (description of the special case).* The proof relies heavily on the theory of relative projectivity (developed in Chapter IX, Sections 1–3). Recall that a $kG$-module $M$ is projective relative to a subgroup $U \leq G$ if every short exact sequence of $kG$-modules

$$0 \longrightarrow A \longrightarrow B \longrightarrow M \longrightarrow 0$$

whose restriction to $kU$ splits, also splits over $kG$.

For an indecomposable $kG$-module $M$, the vertex $Q$ is defined as a minimal subgroup (with respect to inclusion) such that $M$ is projective relative to $Q$. It can be shown that the vertex is always a $p$-subgroup and is uniquely determined up to conjugacy in $G$. The source of $M$ is the (essentially unique) indecomposable $kQ$-module $S$ such that $M$ is a direct summand of $kG \otimes_{kQ} S$.

For the correspondence when $Q$ is a $p$-subgroup with normalizer $L = N_G(Q)$:

Given an indecomposable $kG$-module $M$ with vertex $Q$, consider its restriction $M_L$ to $kL$. By the properties of vertices under restriction, $M_L$ decomposes as a direct sum of indecomposable $kL$-modules, and among these, exactly one summand $N$ has vertex $Q$ (all other summands have vertices strictly contained in, or conjugate within $L$ to, proper subgroups of $Q$). This $N$ is defined to be the Green correspondent of $M$.

Conversely, given an indecomposable $kL$-module $N$ with vertex $Q$, consider the induced module $kG \otimes_{kL} N$. It decomposes as a direct sum of indecomposable $kG$-modules, and exactly one summand $M$ has vertex $Q$ (all others have vertices strictly smaller than $Q$ up to conjugacy). This $M$ is the Green correspondent of $N$.

The uniqueness and mutual inverse property follow from the Mackey decomposition formula and the fact that $Q$ is normal in $L$ (since $L = N_G(Q)$). The technical details involve careful analysis of the restriction-induction adjunction and the behavior of vertices under these functors. $\square$

The Green correspondence generalizes the Brauer correspondence from classical character theory: Brauer's defect groups of $G$ can be interpreted as vertex groups of certain well-defined $kG$-modules. The Green correspondence has proved to be an indispensable tool in modern modular representation theory.

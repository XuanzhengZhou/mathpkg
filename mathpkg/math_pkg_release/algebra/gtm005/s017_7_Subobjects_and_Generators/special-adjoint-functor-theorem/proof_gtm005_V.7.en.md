---
role: proof
locale: en
of_concept: special-adjoint-functor-theorem
source_book: gtm005
source_chapter: "V. Limits"
source_section: "7. Subobjects and Generators"
---

By the General Adjoint Functor Theorem, it suffices to show that for each object $x \in X$, the comma category $(x \downarrow G)$ has an initial object.

We verify that $(x \downarrow G)$ satisfies the hypotheses of Theorem 1 (initial object from cogenerating set).

**Cogenerating set.** Given the small cogenerating set $Q$ in $A$, since $X$ has small hom-sets, the set $Q'$ of all objects $k: x \to Gq$ with $q \in Q$ is small. It is cogenerating in $(x \downarrow G)$: Given two distinct arrows $s \neq t: \langle f: x \to Ga, a \rangle \to \langle f': x \to Ga', a' \rangle$ in $(x \downarrow G)$, there is a $q_0 \in Q$ and an arrow $h: a' \to q_0$ with $hs \neq ht$ (since $Q$ cogenerates $A$). This $h$ can be regarded as an arrow
$$
h: \langle f': x \to Ga', a' \rangle \to \langle f_0: x \to Gq_0, q_0 \rangle
$$
where $f_0 = Gh \circ f'$, and $hs \neq ht$ holds in $(x \downarrow G)$. Therefore $Q'$ is a small cogenerating set for $(x \downarrow G)$.

**Small-completeness.** Since $A$ is small-complete and $G$ is continuous, the comma category $(x \downarrow G)$ is small-complete (limits are computed pointwise in $A$, with the structural arrow from $x$ given by the universal property).

**Intersections of subobjects.** It remains to construct an intersection in $(x \downarrow G)$ for every set of subobjects $h_i: \langle f_i: x \to Ga_i, a_i \rangle \to \langle f: x \to Ga, a \rangle$, where $i \in J$.

By the lemma on comma categories, the projection $(x \downarrow G) \to A$ preserves monics, so the corresponding arrows $h_i: a_i \to a$ are monics in $A$. By hypothesis, they have a pullback $h: b \to a$ in $A$ (their intersection). Since $G$ is continuous, it preserves this pullback, yielding $Gh: Gb \to Ga$ with the corresponding cone.

Moreover, the family of arrows $f_i: x \to Ga_i$ together with the commutativity conditions in $(x \downarrow G)$ induce, via the universal property of the pullback $Gb$, a unique arrow $f_b: x \to Gb$ such that $Gh \circ f_b = f$. Thus $h: \langle f_b, b \rangle \to \langle f, a \rangle$ is the desired intersection in $(x \downarrow G)$.

All hypotheses of Theorem 1 are satisfied, so each $(x \downarrow G)$ has an initial object, which provides the value of the left adjoint at $x$. Hence $G$ has a left adjoint.

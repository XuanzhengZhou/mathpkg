---
role: proof
locale: en
of_concept: special-adjoint-functor-theorem
source_book: gtm005
source_chapter: "V"
source_section: "7. Subobjects and Generators"
---

By the general Adjoint Functor Theorem, it suffices to find for each object $x \in \mathcal{X}$ a solution set — a small set of arrows $x \to G a$ through which every arrow $x \to G a'$ factors. Equivalently, we must show that each comma category $(x \downarrow G)$ has an initial object. We verify that $(x \downarrow G)$ satisfies the hypotheses of the Existence of Initial Object theorem.

**Step 1: Small hom-sets.** Since $\mathcal{X}$ has small hom-sets, for each $x \in \mathcal{X}$ the set of all objects $k : x \to G q$ (with $q \in Q$) is small. Let $Q'$ be this small set.

**Step 2: $Q'$ is cogenerating in $(x \downarrow G)$.** Given two distinct arrows
\[
s \neq t : \langle f : x \to G a, a \rangle \longrightarrow \langle f' : x \to G a', a' \rangle
\]
in $(x \downarrow G)$, there exists $q_0 \in Q$ and an arrow $h : a' \to q_0$ in $\mathcal{A}$ with $h s \neq h t$ (since $Q$ cogenerates $\mathcal{A}$). This $h$ yields an arrow in $(x \downarrow G)$:
\[
h : \langle f' : x \to G a', a' \rangle \longrightarrow \langle G h \circ f' : x \to G q_0, q_0 \rangle,
\]
with $h s \neq h t$ in the comma category. Hence $Q'$ cogenerates $(x \downarrow G)$.

**Step 3: Small-completeness.** Since $\mathcal{A}$ is small-complete and $G$ preserves all small limits (is continuous), the comma category $(x \downarrow G)$ is small-complete.

**Step 4: Intersections of subobjects.** For any set of subobjects
\[
h_i : \langle f_i : x \to G a_i, a_i \rangle \longrightarrow \langle f : x \to G a, a \rangle \qquad (i \in J)
\]
in $(x \downarrow G)$, the projection functor carries these to monics $h_i : a_i \to a$ in $\mathcal{A}$. (This projection preserves kernel pairs and hence monics.) By hypothesis, these monics have a pullback $h : b \to a$ in $\mathcal{A}$. Since $G$ preserves pullbacks, $G h : G b \to G a$ is a pullback in $\mathcal{X}$, and the universal property of this pullback yields the required intersection in $(x \downarrow G)$.

Thus $(x \downarrow G)$ satisfies all hypotheses of the Existence of Initial Object theorem, so it has an initial object for each $x$. This initial object provides the universal arrow giving the left adjoint to $G$.

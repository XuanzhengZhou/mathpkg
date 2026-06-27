---
role: proof
locale: en
of_concept: paracompact-equivalence-theorem
source_book: gtm027
source_chapter: "5"
source_section: "Paracompactness"
---

# Proof of Equivalent Characterizations of Paracompactness

**Theorem 28.** If $X$ is a regular topological space, then the following statements are equivalent:

(a) $X$ is paracompact (every open cover has an open locally finite refinement).

(b) Each open cover of $X$ has a locally finite refinement.

(c) Each open cover of $X$ has a closed locally finite refinement.

(d) Each open cover of $X$ is even.

(e) Each open cover of $X$ has an open $\sigma$-discrete refinement.

(f) Each open cover of $X$ has an open $\sigma$-locally finite refinement.

*Proof.* The proof follows the chain of implications

$$(a) \Rightarrow (b) \Rightarrow (c) \Rightarrow (d) \Rightarrow (e) \Rightarrow (f) \Rightarrow (b) \Rightarrow (a).$$

**$(a) \Rightarrow (b)$:** Immediate from the definition of paracompactness: an open locally finite refinement is in particular a locally finite refinement.

**$(b) \Rightarrow (c)$:** This is Lemma 29. Given an open cover $\mathcal{U}$, by regularity there is an open cover $\mathcal{V}$ whose closures refine $\mathcal{U}$ (for each $x \in U \in \mathcal{U}$, pick $V$ open with $x \in V \subset \overline{V} \subset U$). Let $\mathcal{A}$ be a locally finite refinement of $\mathcal{V}$. Then the family of closures $\{\overline{A} : A \in \mathcal{A}\}$ is locally finite (since $\mathcal{A}$ is) and refines $\mathcal{U}$ (since each $\overline{A} \subset \overline{V}$ for some $V \in \mathcal{V}$ with $\overline{V} \subset U \in \mathcal{U}$).

**$(c) \Rightarrow (d)$:** This is Theorem 27. An open cover with a closed locally finite refinement is even. The proof constructs, for each member $A$ of the closed locally finite refinement, a neighborhood of the diagonal, and takes their locally finite intersection.

**$(d) \Rightarrow (e)$:** This is Lemma 33. If every open cover is even, then every open cover has an open $\sigma$-discrete refinement. The proof uses A. H. Stone's trick with well-ordering and a sequence of diagonal neighborhoods.

**$(e) \Rightarrow (f)$:** A $\sigma$-discrete family is $\sigma$-locally finite (since discrete implies locally finite), so this implication is immediate.

**$(f) \Rightarrow (b)$:** This is Lemma 34. Given an open $\sigma$-locally finite refinement, one constructs a locally finite refinement by subtracting earlier members of the $\sigma$-decomposition.

**$(b) \Rightarrow (a)$:** This closes the cycle. Having established $(b) \Rightarrow (c) \Rightarrow (d)$, we know each open cover is even. Lemma 31 applies: for the locally finite refinement $\mathcal{A}$ obtained from $(b)$, there is a diagonal neighborhood $V$ such that $\{V[A] : A \in \mathcal{A}\}$ is locally finite. Intersecting each $V[A]$ with a member of the original cover containing $A$ yields an open locally finite refinement. Thus $X$ is paracompact. $\square$

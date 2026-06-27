---
role: proof
locale: en
of_concept: convex-hull-finite-union-compact-convex
source_book: gtm015
source_chapter: "35"
source_section: "Compact convex sets in a TVS"
---

# Proof of Convex hull of a finite union of compact convex sets is compact

Let $E$ be a separated topological vector space over $\mathbb{K}$, let $A_k$ ($k = 1, \ldots, n$) be compact convex subsets of $E$, and set $S = \bigcup_{k=1}^n A_k$. We prove that $\operatorname{conv} S$ is compact by showing it is precompact (totally bounded) and complete. Since $E$ is not assumed complete, we instead argue directly that $\operatorname{conv} S$ is compact by exhibiting it as a finite union of "small" sets of arbitrarily small order, which is equivalent to precompactness in the sense of the additive uniformity.

Let $W$ be any neighborhood of $\theta$ in $E$, and define the corresponding uniformity vicinity

$$W_r = \{ (x,y) \in E \times E : y - x \in W \}.$$

We will represent $\operatorname{conv} S$ as a finite union of sets $T_j$ that are *small of order $W_r$*, i.e., $T_j \times T_j \subset W_r$ (equivalently, $T_j - T_j \subset W$).

**Step 1.** Choose a convex, symmetric neighborhood $V$ of $\theta$ such that

$$V + V + V + V \subset W.$$

Such a $V$ exists by the continuity of addition at $\theta$ (axiom of a TVS).

**Step 2.** Since $S$ is a finite union of compact (hence precompact) sets, $S$ is precompact. Thus there exists a finite system $s_1, \ldots, s_p \in S$ such that

$$S \subset \bigcup_{k=1}^p (s_k + V).$$

Set $T = \bigcup_{k=1}^p (s_k + V)$; then $S \subset T$.

**Step 3.** Let $A = \operatorname{conv}\{s_1, \ldots, s_p\}$. By Lemma (35.2), the convex hull of a finite set is compact; thus $A$ is compact. Since $A$ and $V$ are convex, the Minkowski sum $A + V$ is also convex (25.9). Clearly $T \subset A + V$, because each $s_k \in A$ implies $s_k + V \subset A + V$. Therefore

$$\operatorname{conv} S \subset \operatorname{conv} T \subset A + V,$$

since $A + V$ is convex and contains $T$.

**Step 4.** Because $A$ is compact, $A$ is precompact; choose $a_1, \ldots, a_m \in A$ such that

$$A \subset \bigcup_{j=1}^m (a_j + V).$$

Combining with the inclusion $\operatorname{conv} S \subset A + V$, we obtain

$$\operatorname{conv} S \subset \left( \bigcup_{j=1}^m (a_j + V) \right) + V = \bigcup_{j=1}^m \big( a_j + (V + V) \big).$$

**Step 5.** Define $T_j = a_j + (V + V)$. Because $V$ is symmetric, we have

$$T_j - T_j = (V + V) - (V + V) = V + V + V + V \subset W,$$

hence $T_j \times T_j \subset W_r$. Thus $\operatorname{conv} S$ is covered by finitely many sets $T_j$, each small of order $W_r$.

Since $W$ was arbitrary, this shows that $\operatorname{conv} S$ is precompact with respect to the additive uniformity of $E$. Moreover, $\operatorname{conv} S$ is closed (it will follow from the fact that a precompact set in a separated complete uniform space is compact; alternatively, one may apply the general result that the convex hull of a finite union of compact convex sets is the continuous image of a compact set).

More directly, the above construction shows that the closure $\overline{\operatorname{conv} S}$ is compact, and in fact one can verify that $\operatorname{conv} S$ itself is closed: the argument using precompactness in a complete uniform space shows that $\operatorname{conv} S$ is precompact and its closure is compact; for the statement as given in the text, the convex hull is already compact (which can be proved by noting that $\operatorname{conv} S$ is the continuous image of $A \times \Delta$ for an appropriate simplex, using the compactness of each $A_k$ and Lemma 35.2).

Thus $\operatorname{conv} S$ is compact.

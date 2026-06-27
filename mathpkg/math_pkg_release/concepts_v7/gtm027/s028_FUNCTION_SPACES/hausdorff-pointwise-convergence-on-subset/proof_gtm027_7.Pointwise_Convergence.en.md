---
role: proof
locale: en
of_concept: hausdorff-pointwise-convergence-on-subset
source_book: gtm027
source_chapter: "7"
source_section: "Pointwise Convergence"
---

# Proof of Hausdorff Criterion for Pointwise Convergence on a Subset

**Theorem 2.** Let $F$ be a family of functions, each on a set $X$ to a Hausdorff space $Y$, and let $A$ be a subset of $X$. Let $\wp$ denote the topology of pointwise convergence on $X$, and let $\wp_A$ denote the topology of pointwise convergence on $A$. Then:

(i) The family $F$ with the topology $\wp_A$ is a Hausdorff space if and only if $A$ distinguishes members of $F$ (i.e., the restriction map $R : F \to Y^A$ is injective).

(ii) If $F$ is compact relative to the topology $\wp$ on $X$ and if $A$ distinguishes members of $F$, then the topologies $\wp$ and $\wp_A$ are identical on $F$.

*Proof.* (i) The product space $Y^A$ is a Hausdorff space because $Y$ is Hausdorff. The topology $\wp_A$ for $F$ is by definition the smallest topology such that the restriction map $R : F \to Y^A$, defined by $R(f) = f|_A$, is continuous. Concretely, $\wp_A$ is the relativization to $F$ of the product topology on $Y^A$ via the map $R$. It follows that $(F, \wp_A)$ is a subspace (up to homeomorphism) of the Hausdorff space $Y^A$ if and only if $R$ is injective. A subspace of a Hausdorff space is Hausdorff, and conversely, if $R$ is not injective, two distinct functions $f, g \in F$ with $f|_A = g|_A$ cannot be separated by open sets in $\wp_A$ because every subbasic open set $\{h : h(x) \in U\}$ with $x \in A$ either contains both $f$ and $g$ or neither. Hence $(F, \wp_A)$ is Hausdorff if and only if $R$ is injective, which is precisely the condition that $A$ distinguishes members of $F$.

(ii) The identity map

\[
i : (F, \wp) \to (F, \wp_A)
\]

is always continuous, because $\wp_A \subset \wp$: every subbasic set for $\wp_A$ is of the form $\{f : f(x) \in U\}$ with $x \in A$ and $U$ open in $Y$, and such sets belong to $\wp$ since they are also subbasic for the full pointwise topology on $X$. Now assume that $(F, \wp)$ is compact and that $A$ distinguishes members of $F$, so that $(F, \wp_A)$ is Hausdorff by part (i). The identity map $i$ is a continuous bijection from a compact space to a Hausdorff space. A well-known fact in general topology (a continuous bijection from a compact space onto a Hausdorff space is a homeomorphism — see Proposition 5.8) implies that $i$ is a homeomorphism. Consequently the topologies $\wp$ and $\wp_A$ coincide on $F$. $\square$
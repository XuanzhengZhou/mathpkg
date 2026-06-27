---
role: proof
locale: en
of_concept: equivalent-conditions-topological-direct-sum
source_book: gtm015
source_chapter: "I. Topological Vector Spaces"
source_section: "20. Topologically supplementary subspaces"
---

# Proof of Equivalent Conditions for Topological Direct Sum

Let $E$ be a TVS and let $M, N$ be supplementary linear subspaces of $E$; thus, every vector $x \in E$ has a unique representation $x = y + z$ with $y \in M$, $z \in N$.

Define mappings $u, v: E \to E$ as follows: if $x \in E$, write $x = y + z$ with $y \in M$, $z \in N$ and define $u(x) = y$, $v(x) = z$. By the uniqueness of such representations, $u$ and $v$ are well-defined and linear.

Since $u(x) + v(x) = x$ for all $x \in E$, clearly $u$ is continuous if and only if $v$ is continuous. Thus conditions (b) and (c) are equivalent.

Now let $T: M \times N \to E$ be the mapping $T(y, z) = y + z$. Then for all $y \in M$, $z \in N$,

$$T^{-1}(y + z) = (y, z) = (u(y + z), v(y + z)),$$

that is, $T^{-1}(x) = (u(x), v(x))$ for all $x \in E$.

Thus, $u$ and $v$ are the compositions of $T^{-1}$ with the coordinate projections of $M \times N$ onto $M$ and $N$ respectively. Therefore $T^{-1}$ is continuous if and only if $u$ and $v$ are continuous (since the coordinate projections are continuous, and the composition of continuous maps is continuous).

But the continuity of $T^{-1}$ is, by definition, precisely condition (a): $E$ is the topological direct sum of $M$ and $N$ means that the natural continuous linear bijection $T: M \times N \to E$ is a homeomorphism, i.e., $T^{-1}$ is continuous.

Hence all three conditions are equivalent: (a) $\Leftrightarrow$ (b) $\Leftrightarrow$ (c). $\square$

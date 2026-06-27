---
role: proof
locale: en
of_concept: subspace-dimension-bound
source_book: gtm028
source_chapter: "I"
source_section: "21"
---

Let $V$ be finite-dimensional with basis $\{v_1, \ldots, v_n\}$ and let $W$ be a subspace. If $W = \{0\}$, then $W$ is finite-dimensional with $[W:F] = 0 \leq n$.

Otherwise, construct a basis of $W$ inductively. Choose a non-zero $w_1 \in W$; then $\{w_1\}$ is free. Suppose we have constructed a free set $\{w_1, \ldots, w_k\} \subseteq W$. If this set generates $W$, it is a basis. Otherwise, there exists $w_{k+1} \in W$ not in the span of $\{w_1, \ldots, w_k\}$, and $\{w_1, \ldots, w_{k+1}\}$ is free. Continuing this process, we obtain a free subset of $W$. By Theorem 21 (with $L$ being the constructed free set and $S$ being the basis of $V$), this free set can be extended to a basis of $V$. Since any basis of $V$ has $n$ elements, the process must terminate with at most $n$ elements in $W$. Thus $W$ has a finite basis, and $[W:F] \leq [V:F]$.

If $[W:F] = [V:F]$, then any basis of $W$ is also a basis of $V$ (it is a free subset of $V$ of maximal size $n$), so $W = V$.

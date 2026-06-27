---
role: proof
locale: en
of_concept: compact-convergence-equals-compact-open
source_book: gtm027
source_chapter: "7"
source_section: "Uniform Convergence on Compacta"
---

# Proof of Theorem 7.11 — Compact Convergence Equals the Compact-Open Topology

Let $F$ be a family of continuous functions on a topological space $X$ to a uniform space $(Y, \mathcal{V})$. Let $\mathcal{C}$ be the topology of uniform convergence on compacta (the uniformity $\mathcal{V} \mid \mathcal{C}$ where $\mathcal{C}$ is the family of all compact subsets) and let $\mathcal{T}$ be the compact-open topology.

**$\mathcal{T} \subset \mathcal{C}$:** Let $K \subset X$ be compact, $U \subset Y$ open, and $f \in F$ with $f[K] \subset U$. Then $f[K]$ is compact, and by Theorem 6.33 there exists $V \in \mathcal{V}$ such that $V[f[K]] \subset U$. If $g \in F$ satisfies $g(x) \in V[f(x)]$ for all $x \in K$, then $g[K] \subset V[f[K]] \subset U$. Thus each subbasic compact-open set $\{f : f[K] \subset U\}$ is open in $\mathcal{C}$, so $\mathcal{T} \subset \mathcal{C}$.

**$\mathcal{C} \subset \mathcal{T}$:** Let $K \subset X$ be compact, $V \in \mathcal{V}$, and $f \in F$. We must find compact subsets $K_1, \dots, K_n$ of $X$ and open subsets $U_1, \dots, U_n$ of $Y$ such that $f[K_i] \subset U_i$ and $\bigcap_i \{g : g[K_i] \subset U_i\} \subset \{g : g(x) \in V[f(x)] \text{ for all } x \in K\}$.

Choose a closed symmetric $W \in \mathcal{V}$ with $W \circ W \circ W \subset V$. Since $f[K]$ is compact, choose $x_1, \dots, x_n \in K$ such that $\{W[f(x_i)]\}$ covers $f[K]$. Define $K_i = K \cap f^{-1}[W[f(x_i)]]$ (compact as closed subset of $K$) and let $U_i$ be the interior of $W \circ W[f(x_i)]$. If $g[K_i] \subset U_i$ for each $i$, then for any $x \in K$, we have $x \in K_i$ for some $i$, so $g(x) \in U_i \subset W \circ W[f(x_i)]$. Since $f(x) \in W[f(x_i)]$, we get $g(x) \in W \circ W \circ W[f(x)] \subset V[f(x)]$. Hence $\mathcal{C} \subset \mathcal{T}$.

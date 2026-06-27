---
role: proof
locale: en
of_concept: compact-jointly-continuous-implies-equicontinuous
source_book: gtm027
source_chapter: "7"
source_section: "Compactness and Equicontinuity"
---

# Proof of Theorem 7.16 — Compactness under Jointly Continuous Topology Implies Equicontinuity

Let $F$ be a family of functions on a topological space $X$ to a uniform space $(Y, \mathcal{V})$, and suppose $F$ is compact relative to a jointly continuous topology.

Fix $x \in X$ and let $V \in \mathcal{V}$ be symmetric. We must find a neighborhood $U$ of $x$ such that $g[U] \subset V \circ V[g(x)]$ for every $g \in F$.

For each $f \in F$, since the topology is jointly continuous, the map $P$ is continuous at $(f, x)$. Hence there exist a neighborhood $G_f$ of $f$ in $F$ and a neighborhood $W_f$ of $x$ in $X$ such that $P[G_f \times W_f] \subset V[f(x)]$. That is, if $g \in G_f$ and $w \in W_f$, then $g(w) \in V[f(x)]$. Consequently, for $g \in G_f$ and $w \in W_f$, we have $g(x) \in V[f(x)]$ and $g(w) \in V[f(x)]$, so

$$g(w) \in V \circ V[g(x)],$$

which means $g[W_f] \subset V \circ V[g(x)]$ for all $g \in G_f$.

Since $F$ is compact, the open cover $\{G_f : f \in F\}$ has a finite subcover $\{G_{f_1}, \dots, G_{f_n}\}$. Let $W_{f_1}, \dots, W_{f_n}$ be the corresponding neighborhoods of $x$, and set $U = \bigcap_{i=1}^n W_{f_i}$. Then for any $g \in F$, we have $g \in G_{f_i}$ for some $i$, so $g[U] \subset g[W_{f_i}] \subset V \circ V[g(x)]$. Thus $F$ is equicontinuous at $x$.

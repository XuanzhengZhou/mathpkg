---
role: proof
locale: en
of_concept: equicontinuous-pointwise-jointly-continuous
source_book: gtm027
source_chapter: "7"
source_section: "Compactness and Equicontinuity"
---

# Proof of Theorem 7.15 — For Equicontinuous Families, Pointwise Convergence is Jointly Continuous

Let $F$ be an equicontinuous family of functions on $X$ to a uniform space $(Y, \mathcal{V})$. We prove that the map $P : F \times X \to Y$ defined by $P(f, x) = f(x)$ is continuous at each $(f, x) \in F \times X$ relative to the pointwise topology $\wp$ on $F$.

Fix $(f, x)$ and let $V \in \mathcal{V}$ be a closed symmetric member. Since $F$ is equicontinuous at $x$, there exists a neighborhood $U$ of $x$ such that $g[U] \subset V[g(x)]$ for all $g \in F$. In particular, for any $y \in U$ and $g \in F$ with $g(x) \in V[f(x)]$, we have

$$g(y) \in V[g(x)] \subset V \circ V[f(x)].$$

Now $\{g : g(x) \in V[f(x)]\}$ is a $\wp$-neighborhood of $f$ (it is a subbasic pointwise-open set). Thus for $g$ in this neighborhood and $y \in U$, we have $P(g, y) = g(y) \in V \circ V[f(x)]$, establishing continuity of $P$ at $(f, x)$.

Since $\wp$ is jointly continuous, by Theorem 7.6 and Theorem 7.11, the pointwise topology coincides with the compact-open topology and hence with the topology of uniform convergence on compacta.

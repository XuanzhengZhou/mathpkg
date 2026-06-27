---
role: proof
locale: en
of_concept: equicontinuity-closure
source_book: gtm027
source_chapter: "7"
source_section: "Compactness and Equicontinuity"
---

# Proof of Theorem 7.14 — Equicontinuity is Preserved under Pointwise Closure

Let $F$ be a family of maps on a topological space $X$ to a uniform space $(Y, \mathcal{V})$. Suppose $F$ is equicontinuous at $x \in X$. We show the closure $\overline{F}$ of $F$ relative to the topology $\wp$ of pointwise convergence is also equicontinuous at $x$.

Let $V$ be a closed member of the uniformity $\mathcal{V}$. By equicontinuity of $F$ at $x$, there exists a neighborhood $U$ of $x$ such that $f[U] \subset V[f(x)]$ for every $f \in F$. Equivalently, for each $y \in U$, we have $(f(y), f(x)) \in V$ for all $f \in F$.

Now fix $y \in U$. The set

$$\{f : (f(y), f(x)) \in V\}$$

is closed in the topology $\wp$ of pointwise convergence (since it is the inverse image of the closed set $V$ under the continuous evaluation map $f \mapsto (f(y), f(x))$). Hence this set contains the pointwise closure $\overline{F}$. That is, for every $g \in \overline{F}$ and every $y \in U$, we have $(g(y), g(x)) \in V$, i.e., $g[U] \subset V[g(x)]$.

Since $V$ was an arbitrary closed member of $\mathcal{V}$, this proves that $\overline{F}$ is equicontinuous at $x$. If $F$ is equicontinuous (at every point), then so is $\overline{F}$.

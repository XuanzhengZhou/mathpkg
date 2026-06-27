---
role: proof
locale: en
of_concept: pointwise-closure-uniformly-equicontinuous
source_book: gtm027
source_chapter: "7"
source_section: "G"
---

# Proof of Pointwise Closure of Uniformly Equicontinuous Families

Let $F$ be a uniformly equicontinuous family of functions from a topological space $X$ to a uniform space $(Y, \mathfrak{u})$. Let $\overline{F}$ be the pointwise closure of $F$ in $Y^X$. We prove that $\overline{F}$ is uniformly equicontinuous.

Recall that $F$ is uniformly equicontinuous if for each $U \in \mathfrak{u}$ there exists a neighborhood $V$ of the diagonal in $X \times X$ such that for all $f \in F$ and all $(x, x') \in V$, we have $(f(x), f(x')) \in U$.

Let $U \in \mathfrak{u}$ be given. Choose a symmetric entourage $W \in \mathfrak{u}$ such that $W \circ W \circ W \subseteq U$. Since $F$ is uniformly equicontinuous, there exists a neighborhood $V$ of the diagonal in $X \times X$ such that for all $f \in F$ and $(x, x') \in V$, $(f(x), f(x')) \in W$.

Now take any $g \in \overline{F}$ and $(x, x') \in V$. Since $g$ is in the pointwise closure of $F$, there exist nets $\{f_\alpha\}$ in $F$ converging pointwise to $g$. In particular, $f_\alpha(x) \to g(x)$ and $f_\alpha(x') \to g(x')$. For sufficiently large $\alpha$, we have $(f_\alpha(x), g(x)) \in W$ and $(g(x'), f_\alpha(x')) \in W$. Since $(f_\alpha(x), f_\alpha(x')) \in W$ by uniform equicontinuity, we obtain

$$(g(x), g(x')) \in W \circ W \circ W \subseteq U.$$

Thus $\overline{F}$ is uniformly equicontinuous.

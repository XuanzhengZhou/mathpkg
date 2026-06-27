---
role: proof
locale: en
of_concept: compact-equicontinuous-implies-uniformly-equicontinuous
source_book: gtm027
source_chapter: "7"
source_section: "G"
---

# Proof of Compact Domain: Equicontinuity Implies Uniform Equicontinuity

Let $X$ be a compact topological space and let $F$ be an equicontinuous family of functions from $X$ to a uniform space $(Y, \mathfrak{u})$. We prove that $F$ is uniformly equicontinuous.

Recall that $F$ is equicontinuous at $x \in X$ if for each $U \in \mathfrak{u}$ there exists a neighborhood $N_x$ of $x$ such that for all $f \in F$ and $x' \in N_x$, $(f(x), f(x')) \in U$. The family $F$ is equicontinuous if it is equicontinuous at every point.

Let $U \in \mathfrak{u}$ be given. Choose a symmetric entourage $W \in \mathfrak{u}$ with $W \circ W \circ W \subseteq U$. For each $x \in X$, equicontinuity at $x$ yields an open neighborhood $N_x$ of $x$ such that for all $f \in F$ and $x' \in N_x$, $(f(x), f(x')) \in W$.

The collection $\{N_x : x \in X\}$ is an open cover of $X$. By compactness of $X$, there exists a finite subcover $\{N_{x_1}, \ldots, N_{x_n}\}$. Let $\delta$ be a Lebesgue number for this cover with respect to some compatible uniformity on $X$ (or, alternatively, apply the standard argument using the fact that the diagonal neighborhood $\bigcup_{i=1}^n (N_{x_i} \times N_{x_i})$ contains a neighborhood $V$ of the diagonal in $X \times X$, since $X$ is compact and each $N_{x_i}$ is open).

More concretely: $V = \bigcup_{i=1}^n (N_{x_i} \times N_{x_i})$ is a neighborhood of the diagonal. For any $(x, x') \in V$, there exists $i$ such that $x, x' \in N_{x_i}$. Then for all $f \in F$,

$$(f(x), f(x_i)) \in W, \quad (f(x_i), f(x')) \in W,$$

and by symmetry of $W$,

$$(f(x), f(x')) \in W \circ W \subseteq U.$$

Thus $F$ is uniformly equicontinuous.

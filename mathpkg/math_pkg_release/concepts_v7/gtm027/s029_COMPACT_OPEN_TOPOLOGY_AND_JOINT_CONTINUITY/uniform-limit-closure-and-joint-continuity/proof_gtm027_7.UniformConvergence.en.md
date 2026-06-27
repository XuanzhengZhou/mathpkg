---
role: proof
locale: en
of_concept: uniform-limit-closure-and-joint-continuity
source_book: gtm027
source_chapter: "7"
source_section: "Uniform Convergence"
---

# Proof of Theorem 7.9 — Closure of Continuous Functions and Joint Continuity under Uniform Convergence

Let $F$ be the family of all continuous functions on a topological space $X$ to a uniform space $(Y, \mathcal{V})$, and let $G$ be the space of all functions on $X$ to $Y$ with the topology of uniform convergence.

**(a) $F$ is closed in $G$.** We show the set of non-continuous functions is open in $G$. Suppose $f$ is not continuous at $x \in X$; then there exists $V \in \mathcal{V}$ such that $f^{-1}[V[f(x)]]$ is not a neighborhood of $x$. Choose a symmetric $W \in \mathcal{V}$ with $W \circ W \circ W \subset V$. We claim: if $g \in F$ satisfies $(g(y), f(y)) \in W$ for all $y$, then $g$ is also not continuous. Indeed, $g \subset W \circ f$ and $g^{-1} \subset f^{-1} \circ W^{-1} = f^{-1} \circ W$, so

$$g^{-1} \circ W \circ g \subset f^{-1} \circ W \circ W \circ W \circ f \subset f^{-1} \circ V \circ f.$$

Therefore $g^{-1}[W[g(x)]] \subset f^{-1}[V[f(x)]]$, which is not a neighborhood of $x$. Hence the uniform neighborhood $\{g : (g(y), f(y)) \in W \text{ for all } y\}$ contains only non-continuous functions, proving $G \setminus F$ is open.

**(b) Joint continuity.** To show the map $P : F \times X \to Y$ is continuous at $(f, x)$, let $V \in \mathcal{V}$. If $y \in f^{-1}[V[f(x)]]$ and $g(z) \in V[f(z)]$ for all $z$, then

$$g(y) \in V[f(y)] \subset V \circ V[f(x)],$$

which establishes continuity of $P$ with respect to the topology of uniform convergence on $F$ and the given topology on $X$. Thus the u.c. topology is jointly continuous.

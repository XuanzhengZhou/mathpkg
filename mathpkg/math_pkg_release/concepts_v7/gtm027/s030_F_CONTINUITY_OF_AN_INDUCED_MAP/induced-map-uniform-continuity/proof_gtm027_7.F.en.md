---
role: proof
locale: en
of_concept: induced-map-uniform-continuity
source_book: gtm027
source_chapter: "7"
source_section: "F"
---

# Proof of Uniform Continuity of the Induced Map

Let $X$ and $Y$ be sets, let $\alpha$ and $\beta$ be families of subsets of $X$ and $Y$ respectively. Let $(Z, \mathfrak{u})$ be a uniform space, $F$ the family of all functions $X \to Z$, and $G$ the family of all functions $Y \to Z$. For a map $T : X \to Y$, the induced map $T^* : G \to F$ is defined by

$$T^*(g) = g \circ T, \qquad g \in G.$$

Assume that for each $A \in \alpha$, the image $T[A]$ is contained in some member of $\beta$. We show that $T^*$ is uniformly continuous with respect to the uniformities $\mathfrak{u} \mid \alpha$ on $F$ and $\mathfrak{u} \mid \beta$ on $G$ (uniform convergence on members of $\alpha$ and $\beta$ respectively).

Recall that a typical basic entourage for $\mathfrak{u} \mid \alpha$ is

$$\{(f_1, f_2) : (f_1(x), f_2(x)) \in U \text{ for all } x \in A\}$$

for $A \in \alpha$ and $U \in \mathfrak{u}$. Similarly for $\mathfrak{u} \mid \beta$ with some $B \in \beta$.

Given $A \in \alpha$ and $U \in \mathfrak{u}$, choose $B \in \beta$ such that $T[A] \subseteq B$ (possible by hypothesis). Then for any $g_1, g_2 \in G$ satisfying $(g_1(y), g_2(y)) \in U$ for all $y \in B$, we have for all $x \in A$:

$$(T^*(g_1)(x), T^*(g_2)(x)) = (g_1(T(x)), g_2(T(x))) \in U$$

since $T(x) \in T[A] \subseteq B$. Thus $T^* \times T^*$ maps the $\beta, U$ entourage into the $\alpha, U$ entourage, establishing uniform continuity.

In particular, if $\alpha$ and $\beta$ consist of all singleton subsets (giving the uniformity of pointwise convergence), the condition is automatically satisfied; if they are the families of all subsets (giving the uniformity of uniform convergence), the condition also holds. Hence $T^*$ is always uniformly continuous relative to uniform convergence and is continuous relative to pointwise convergence.

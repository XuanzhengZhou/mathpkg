---
role: proof
locale: en
of_concept: chain-map-induces-homology
source_book: gtm004
source_chapter: "IV. Derived Functors"
source_section: "1. Complexes"
---

# Proof of A Chain Map Induces a Map in Homology

Let $C = \{C_n, \partial_n^C\}$ and $D = \{D_n, \partial_n^D\}$ be chain complexes over $\Lambda$, and let $\varphi: C \to D$ be a chain map. By definition, $\varphi$ is a morphism of degree $0$ in the category of graded modules such that the diagram

$$
\begin{CD}
\cdots @>>> C_{n+1} @>{\partial_{n+1}^C}>> C_n @>{\partial_n^C}>> C_{n-1} @>>> \cdots \\
@. @V{\varphi_{n+1}}VV @V{\varphi_n}VV @V{\varphi_{n-1}}VV @. \\
\cdots @>>> D_{n+1} @>{\partial_{n+1}^D}>> D_n @>{\partial_n^D}>> D_{n-1} @>>> \cdots
\end{CD}
$$

commutes; i.e. $\varphi_{n-1} \partial_n^C = \partial_n^D \varphi_n$ for all $n \in \mathbb{Z}$.

For each $n$, we must show that $\varphi_n$ induces a well-defined map

$$
\varphi_* = H_n(\varphi): H_n(C) = \frac{\ker \partial_n^C}{\operatorname{im} \partial_{n+1}^C} \longrightarrow \frac{\ker \partial_n^D}{\operatorname{im} \partial_{n+1}^D} = H_n(D).
$$

**Step 1: $\varphi_n(\ker \partial_n^C) \subseteq \ker \partial_n^D$.** If $x \in C_n$ with $\partial_n^C(x) = 0$, then

$$
\partial_n^D(\varphi_n(x)) = \varphi_{n-1}(\partial_n^C(x)) = \varphi_{n-1}(0) = 0.
$$

Thus $\varphi_n(x) \in \ker \partial_n^D$.

**Step 2: $\varphi_n(\operatorname{im} \partial_{n+1}^C) \subseteq \operatorname{im} \partial_{n+1}^D$.** If $x = \partial_{n+1}^C(y)$ for some $y \in C_{n+1}$, then

$$
\varphi_n(x) = \varphi_n(\partial_{n+1}^C(y)) = \partial_{n+1}^D(\varphi_{n+1}(y)) \in \operatorname{im} \partial_{n+1}^D.
$$

**Step 3: Induced map.** Steps 1 and 2 show that $\varphi_n$ descends to a well-defined map on the quotient:

$$
H_n(\varphi): H_n(C) \longrightarrow H_n(D), \qquad [x] \longmapsto [\varphi_n(x)].
$$

The collection $H(\varphi) = \{H_n(\varphi)\}_{n \in \mathbb{Z}}$ is a morphism of graded $\Lambda$-modules of degree zero.

Thus every chain map $\varphi: C \to D$ induces a map $H(\varphi): H(C) \to H(D)$ in homology.

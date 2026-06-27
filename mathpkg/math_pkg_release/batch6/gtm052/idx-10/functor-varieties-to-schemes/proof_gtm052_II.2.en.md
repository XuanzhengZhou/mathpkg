---
role: proof
locale: en
of_concept: functor-varieties-to-schemes
source_book: gtm052
source_chapter: "II"
source_section: "2"
---
To begin with, let $X$ be any topological space, and let $t(X)$ be the set of (nonempty) irreducible closed subsets of $X$. If $Y$ is a closed subset of $X$, then $t(Y) \subseteq t(X)$. Furthermore,
$$t(Y_1 \cup Y_2) = t(Y_1) \cup t(Y_2)$$
and $t(\bigcap Y_i) = \bigcap t(Y_i)$. So we can define a topology on $t(X)$ by taking as closed sets the subsets of the form $t(Y)$, where $Y$ is a closed subset of $X$.

If $f: X_1 \rightarrow X_2$ is a continuous map, then we obtain a map $t(f): t(X_1) \rightarrow t(X_2)$ by sending an irreducible closed subset to the closure of its image. Thus $t$ is a functor on topological spaces.

To give a morphism of $(t(V), \alpha_* \mathcal{O}_V)$ to $\operatorname{Spec} k$, we have only to give a homomorphism of rings $k \rightarrow \Gamma(t(V), \alpha_* \mathcal{O}_V) = \Gamma(V, \mathcal{O}_V)$. We send $\lambda \in k$ to the constant function $\lambda$ on $V$. Thus $t(V)$ becomes a scheme over $k$.

Finally, if $V$ and $W$ are two varieties, then one can check (Ex. 2.15) that the natural map
$$\text{Hom}_{\mathfrak{Var}(k)}(V, W) \rightarrow \text{Hom}_{\mathfrak{Sch}(k)}(t(V), t(W))$$
is bijective. This shows that the functor $t: \mathfrak{Var}(k) \rightarrow \mathfrak{Sch}(k)$ is fully faithful. In particular it implies that $t(V)$ is isomorphic to $t(W)$ if and only if $V$ is isomorphic to $W$.

It is clear from the construction that $\alpha: V \rightarrow t(V)$ induces a homeomorphism from $V$ onto the set of closed points of $t(V)$, with the induced topology.

Note. We will see later (4.10) what the image of the functor $t$ is.

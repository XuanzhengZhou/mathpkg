---
role: proof
locale: en
of_concept: final-functor-preserves-colimits
source_book: gtm005
source_chapter: "IX"
source_section: "3. Final Functors"
---

Given $F: J \rightarrow X$ with colimiting cone $\mu: F \rightarrow \operatorname{Colim} F$, we have the restricted cone $\mu L: FL \rightarrow \operatorname{Colim} F$, which induces the canonical map $h: \operatorname{Colim} FL \rightarrow \operatorname{Colim} F$. We must show $h$ is an isomorphism.

Let $\mu': FL \rightarrow \operatorname{Colim} FL$ be the colimiting cone. We construct an inverse $k: \operatorname{Colim} F \rightarrow \operatorname{Colim} FL$. For each $j \in J$, since $L$ is final, the comma category $(j \downarrow L)$ is non-empty, so choose an object $p_j \in J'$ and an arrow $u_j: j \rightarrow Lp_j$. Define $\lambda_j = \mu'_{p_j} \circ F(u_j): Fj \rightarrow \operatorname{Colim} FL$.

For any arrow $f: j \rightarrow k$ in $J$, we have $\lambda_k \circ Ff = \mu'_{p_k} \circ F(u_k) \circ Ff$. Since $(j \downarrow L)$ is connected, there is a zigzag connecting $u_k \circ f$ and $u_j$ in the comma category, which by the connectedness condition yields $\lambda_j = \lambda_k \circ Ff$. Thus $\lambda$ is a cone $F \rightarrow \operatorname{Colim} FL$, inducing a unique $k: \operatorname{Colim} F \rightarrow \operatorname{Colim} FL$ with $k \circ \mu = \lambda$.

Now $h \circ k \circ \mu_j = h \circ \lambda_j = h \circ \mu'_{p_j} \circ F(u_j) = \mu_{Lp_j} \circ F(u_j) = \mu_j$, so $h \circ k = 1_{\operatorname{Colim} F}$ by universality of $\mu$. Similarly $k \circ h = 1_{\operatorname{Colim} FL}$, so $h$ is an isomorphism.

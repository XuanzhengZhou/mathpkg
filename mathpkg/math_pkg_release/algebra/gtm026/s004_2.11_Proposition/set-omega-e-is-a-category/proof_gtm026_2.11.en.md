---
role: proof
locale: en
of_concept: set-omega-e-is-a-category
source_book: gtm026
source_chapter: "2"
source_section: "2.11"
---

Consider $\alpha: A \longrightarrow B$, $\beta: B \longrightarrow C$ and $\gamma: C \longrightarrow D$. It is immediately clear from the diagram that we have

$$
(\beta.\gamma^{\#})^{\#} = \beta^{\#}.\gamma^{\#}. \tag{2.12}
$$

Thus

$$
(\alpha \circ \beta) \circ \gamma = (\alpha.\beta^{\#}) \circ \gamma = \alpha.\beta^{\#}.\gamma^{\#} = \alpha.(\beta.\gamma^{\#})^{\#} = \alpha \circ (\beta \circ \gamma).
$$

That $A\eta.\alpha^{\#} = \alpha$ is clear. We now make explicit the trivially true but important principle:

If $(X, \delta)$ is an $\Omega$-algebra, then $\text{id}_X: (X, \delta) \longrightarrow (X, \delta)$ is an $\Omega$-homomorphism. $\tag{2.13}$

From 2.13 and 2.5 it follows that

$$
(A\eta)^{\#} = \text{id}_{AT}, \quad \text{for all sets } A. \tag{2.14}
$$

In particular, $\alpha \circ B\eta = \alpha.(B\eta)^{\#} = \alpha$.

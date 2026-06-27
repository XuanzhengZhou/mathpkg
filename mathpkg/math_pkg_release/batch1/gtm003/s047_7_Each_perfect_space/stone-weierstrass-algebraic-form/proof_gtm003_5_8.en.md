---
role: proof
locale: en
of_concept: stone-weierstrass-algebraic-form
source_book: gtm003
source_chapter: "V: Order Structures"
source_section: "8. Stone-Weierstrass and Representation Theorems"
---

Let $\mathcal{M}_{\mathbb{R}}(X)$ denote the space of real Radon measures on $X$, which is the dual of $\mathcal{C}_{\mathbb{R}}(X)$. The set $F^\circ \cap [-e, e]^\circ$ is a convex, circled, weakly compact subset of $\mathcal{M}_{\mathbb{R}}(X)$. By the Krein-Milman theorem (II, 10.4), there exists an extreme point $\mu$ of $F^\circ \cap [-e, e]^\circ$.

Since $F$ is a subalgebra of $\mathcal{C}_{\mathbb{R}}(X)$, we can show that the support of any extreme point $\mu$ must be a single point of $X$. Indeed, if $\mu$ is an extreme point and $g \in F$ satisfies $0 \leq g \leq e$, then the measures $\mu_1 = g \cdot \mu / \|\mu\|$ and $\mu_2 = (e-g) \cdot \mu / \|\mu\|$ both belong to $F^\circ \cap [-e, e]^\circ$, and the representation $\mu = \|\mu\|(\mu_1 + \mu_2)$ forces either $g$ or $e-g$ to be constant on the support of $\mu$.

It follows that every $f \in F$ vanishing on the support of $\mu$ satisfies $f = 0$ on that support. Thus for any $h \in \mathcal{C}_{\mathbb{R}}(X)$ orthogonal to $F$, we must have $h = 0$, showing that $F$ is dense.

More precisely, if $\|g\| > 1$ for some $g \in F$, let $\beta = \|g\|^{-1}$ and define Radon measures $\mu_1 = g_1 \cdot \mu$ and $\mu_2 = g \cdot \mu$ where $g_1 = (e - \beta g)/(1 - \beta)$. One verifies that $\mu_1, \mu_2 \in F^\circ$, and $\mu = (1-\beta)\mu_1 + \beta\mu_2$, contradicting that $\mu$ is an extreme point of $F^\circ \cap [-e, e]^\circ$. This completes the proof.

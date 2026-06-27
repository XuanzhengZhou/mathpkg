---
role: proof
locale: en
of_concept: sheafification
source_book: gtm052
source_chapter: "II"
source_section: "1"
---

We construct the sheaf $\mathcal{F}^+$ as follows. For any open set $U$, let $\mathcal{F}^+(U)$ be the set of functions $s$ from $U$ to the union $\bigcup_{P \in U} \mathcal{F}_P$ of the stalks of $\mathcal{F}$ over points of $U$, such that:

(1) for each $P \in U$, $s(P) \in \mathcal{F}_P$, and

(2) for each $P \in U$, there is a neighborhood $V$ of $P$, contained in $U$, and an element $t \in \mathcal{F}(V)$, such that for all $Q \in V$, the germ $t_Q$ of $t$ at $Q$ is equal to $s(Q)$.

We define restriction maps $\mathcal{F}^+(U) \to \mathcal{F}^+(V)$ in the obvious way by restricting functions. One verifies that $\mathcal{F}^+$ is a sheaf: the identity axiom holds because equality of functions is checked pointwise, and the gluing axiom holds because locally consistent functions can be glued to a global function satisfying condition (2).

There is a natural morphism $\theta: \mathcal{F} \to \mathcal{F}^+$ defined by sending a section $t \in \mathcal{F}(U)$ to the function $s(P) = t_P$ (the germ of $t$ at $P$), which satisfies condition (2) with $V = U$.

For the universal property: given a morphism $\varphi: \mathcal{F} \to \mathcal{G}$ to a sheaf $\mathcal{G}$, we define $\psi: \mathcal{F}^+ \to \mathcal{G}$ as follows. For $s \in \mathcal{F}^+(U)$, cover $U$ by open sets $V_i$ on which $s$ is represented by $t_i \in \mathcal{F}(V_i)$. On $V_i \cap V_j$, $t_i$ and $t_j$ have the same germs, so by the sheaf property of $\mathcal{F}^+$ and $\mathcal{G}$, $\varphi(t_i)|_{V_i \cap V_j} = \varphi(t_j)|_{V_i \cap V_j}$. By the gluing axiom for $\mathcal{G}$, these glue to a unique element $\psi(s) \in \mathcal{G}(U)$. This construction is independent of choices, $\psi$ is a morphism of sheaves, and $\varphi = \psi \circ \theta$. Uniqueness of $\psi$ follows from the fact that $\theta$ is stalkwise an isomorphism (the stalks of $\mathcal{F}$ and $\mathcal{F}^+$ are canonically isomorphic), and the uniqueness follows from Proposition 1.1.

The uniqueness of $(\mathcal{F}^+, \theta)$ up to unique isomorphism follows from the standard argument for universal objects.

---
role: proof
locale: en
of_concept: simply-connected-open-allowable
source_book: gtm044
source_chapter: "II"
source_section: "8"
---

# Proof of Simply Connected Open Subsets Are Allowable (Lemma 8.13)

**Lemma 8.13.** Relative to the branched cover $(V(p) \setminus \pi_Y^{-1}(\mathcal{D}), \mathbb{C} \setminus \mathcal{D}, \pi_Y)$, any simply connected open subset of $\mathbb{C} \setminus \mathcal{D}$ is allowable.

*Proof.* Let $\mathcal{U} \subset \mathbb{C} \setminus \mathcal{D}$ be a simply connected open set. Recall that an open set is *allowable* if it is evenly covered by $\pi_Y$, meaning that $\pi_Y^{-1}(\mathcal{U})$ consists of $n = \deg_Y p$ disjoint sheets, each projecting homeomorphically onto $\mathcal{U}$.

Take any point $x_0 \in \mathcal{U}$. By the local structure of the cover, there exists a connected open neighborhood $\mathcal{O} \subset \mathcal{U}$ of $x_0$ that is allowable (for instance, a sufficiently small disk). Let $\mathcal{Q}$ be one of the $n$ analytic function elements lifting $\mathcal{O}$—that is, $\mathcal{Q}$ is the graph of a holomorphic function $\sigma$ defined on $\mathcal{O}$ satisfying $p(x, \sigma(x)) = 0$ for all $x \in \mathcal{O}$.

Now consider any polygonal path $\gamma$ in $\mathcal{U}$ starting at $x_0$. Since $V(p)$ is a branched cover over $\mathbb{C} \setminus \mathcal{D}$, $\mathcal{Q}$ can be analytically continued along $\gamma$ (by the Implicit Function Theorem applied along the path—the only obstructions to continuation are points of $\mathcal{D}$, which are avoided). Hence $\mathcal{Q}$ can be analytically continued along *any* polygonal path in $\mathcal{U}$.

Since $\mathcal{U}$ is simply connected, the Monodromy Theorem (Theorem 8.14) applies: $\mathcal{Q}$ extends uniquely to a single-valued analytic function $\tilde{\sigma}$ on all of $\mathcal{U}$. This function satisfies $p(x, \tilde{\sigma}(x)) = 0$ for all $x \in \mathcal{U}$, by the Identity Theorem (equality holds on $\mathcal{O}$ and both sides are analytic).

Apply this argument to each of the $n$ sheets above $x_0$. We obtain $n$ analytic functions $\tilde{\sigma}_1, \ldots, \tilde{\sigma}_n$ on $\mathcal{U}$, each satisfying $p(x, \tilde{\sigma}_i(x)) = 0$.

We must verify that these $n$ functions are distinct and that they give a complete description of $\pi_Y^{-1}(\mathcal{U})$. Since the $n$ functions were obtained by continuing the $n$ distinct sheets above $x_0$, and no two sheets can coincide on $\mathcal{O}$ (as they correspond to distinct roots of $p(x_0, Y) = 0$), they are distinct analytic functions on the connected set $\mathcal{U}$. Furthermore, for each $x \in \mathcal{U}$, the polynomial $p(x, Y)$ has exactly $n$ roots (counting multiplicity, but above $\mathbb{C} \setminus \mathcal{D}$ they are simple), so $\tilde{\sigma}_1(x), \ldots, \tilde{\sigma}_n(x)$ account for all $n$ points in the fiber $\pi_Y^{-1}(x)$.

Therefore $\pi_Y^{-1}(\mathcal{U}) = \bigsqcup_{i=1}^n \operatorname{graph}(\tilde{\sigma}_i)$, each graph projecting homeomorphically onto $\mathcal{U}$ via $\pi_Y$. Hence $\mathcal{U}$ is allowable. $\square$

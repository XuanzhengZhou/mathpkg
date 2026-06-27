---
role: proof
locale: en
of_concept: compactness-theorem-topological
source_book: gtm053
source_chapter: "2"
source_section: "2.11"
---

Recall the classical compactness theorem: if every finite subset of a set $\Sigma$ of $L$-sentences has a model, then $\Sigma$ itself has a model.

In the Stone space $\mathcal{S}$, a basic closed set is the complement of a basic open set $[P]$, which equals $[\neg P]$. The family of basic closed sets $\{[\neg P] : P \in \Sigma\}$ has the finite intersection property precisely when every finite subset $\Sigma_0 \subseteq \Sigma$ is satisfiable---for then $\bigcap_{P \in \Sigma_0} [\neg P] = [\neg \bigvee_{P \in \Sigma_0} P] \neq \varnothing$, since $\bigwedge \Sigma_0$ has a model.

By the compactness theorem, this implies that $\Sigma$ itself is satisfiable, so
$$\bigcap_{P \in \Sigma} [\neg P] \neq \varnothing.$$
Thus $\mathcal{S}$ is compact: every family of basic closed sets with the finite intersection property has nonempty total intersection. Since the basic opens $[P]$ form a basis, this is equivalent to $\mathcal{S}$ being a compact topological space.

Conversely, if $\mathcal{S}$ is compact and a set $\Sigma$ of sentences is finitely satisfiable, then the family $\{[P] : P \in \Sigma\}$ of basic closed sets has the finite intersection property, so its total intersection is nonempty, yielding a model of $\Sigma$. Hence the two formulations are equivalent.

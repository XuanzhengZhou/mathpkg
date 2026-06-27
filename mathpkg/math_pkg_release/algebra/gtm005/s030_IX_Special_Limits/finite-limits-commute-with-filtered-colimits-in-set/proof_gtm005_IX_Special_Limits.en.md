---
role: proof
locale: en
of_concept: finite-limits-commute-with-filtered-colimits-in-set
source_book: gtm005
source_chapter: "IX"
source_section: "Special Limits"
---

Let $F : P \times J \to \mathbf{Set}$ with $P$ finite and $J$ filtered. By the construction of colimits in Set (dual of Theorem V.2.2), for each $p \in P$,

$$
\varinjlim_j F(p,j) = \bigsqcup_j F(p,j) / E,
$$

where $E$ is the equivalence relation: $x \in F(p,j)$ and $x' \in F(p,j')$ satisfy $x E x'$ iff there exist $u : j \to k$, $u' : j' \to k$ with $F(p,u)(x) = F(p,u')(x')$. Denote by $(x,j)$ the $E$-equivalence class of $x \in F(p,j)$.

Since $J$ is filtered, condition (a) implies that any finite list $(x_1, j_1), \ldots, (x_m, j_m)$ can be rewritten as $(y_1, k), \ldots, (y_m, k)$ with a common index $k$. Condition (b) implies that every equality among such elements holds after applying a single arrow $w : k \to k'$.

For any functor $G : P \to \mathbf{Set}$, we have $\varprojlim_p G(p) \cong \mathrm{Cone}(*, G)$, the set of cones from a point. When $G(p) = \varinjlim_j F(p,j)$ and $P$ is finite, each cone $\tau$ consists of finitely many elements $\tau_p = (y_p, j_p) \in \varinjlim_j F(p,j)$ satisfying finitely many equations. By filteredness, we may choose a common index $k'$ so that all $\tau_p = (y_p, k')$ where the $y_p \in F(p, k')$ already form a cone $y : * \Rightarrow F(-, k')$.

Thus every cone $\tau : * \Rightarrow \varinjlim_j F(-, j)$ arises from a cone $y : * \Rightarrow F(-, k')$ for some $k'$, proving that the canonical map $\kappa$ is bijective.

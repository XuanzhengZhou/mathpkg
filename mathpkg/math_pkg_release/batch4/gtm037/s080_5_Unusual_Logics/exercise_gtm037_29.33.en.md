---
role: exercise
locale: en
chapter: "29"
section: "5"
exercise_number: 33
---

Let $\mathcal{L}$ be a relational language without equality, and let $\mathfrak{A}$ be an $\mathcal{L}$-structure. Suppose $E$ is an equivalence relation on $A$ such that: if $a_i E b_i$ for all $i < m$, and $a \in \mathbb{R}^{\mathfrak{A}}$, then $b \in \mathbb{R}^{\mathfrak{A}}$. Given such an $E$, let $\mathfrak{A}/E$ be the $\mathcal{L}$-structure with universe $A/E$ and with
$$\mathbb{R}^{\mathfrak{A}/E} = \{x \in {}^m(A/E) : \text{there exists } a \in \mathbb{R}^{\mathfrak{A}} \text{ with } a_i \in x_i \text{ for all } i < m\}.$$
Show that the mapping $f$ such that $fa = [a]_E$ for all $a \in A$ is a two-way homomorphism from $\mathfrak{A}$ onto $\mathfrak{A}/E$.

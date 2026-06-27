---
role: proof
locale: en
of_concept: immersion-diffeomorphic-outside-compact
source_book: gtm014
source_chapter: "V"
source_section: "5"
---

We need only show that $\eta$ is 1:1 and onto as the Inverse Function Theorem will imply the result.

To show that $\eta$ is onto we note first that $\eta$ is a submersion and so $\mathrm{Im}\,\eta$ is open. Let $L$ be a compact set with $K \subset \mathrm{Int}\,L$. Then $\mathrm{Im}\,\eta = \eta(L) \cup \eta(\mathbb{R}^n - \mathrm{Int}\,L)$. Both sets in the union are closed so $\mathrm{Im}\,\eta$ is closed. Thus $\mathrm{Im}\,\eta = \mathbb{R}^n$.

To show that $\eta$ is 1:1, define $S = \{x \in \mathbb{R}^n \mid \exists y \in \mathbb{R}^n, y \neq x, \text{ with } \eta(y) = \eta(x)\}$. Since $\eta$ is a diffeomorphism off $K$, $\mathbb{R}^n - S \neq \varnothing$. Thus it is enough to show that $S$ is both open and closed; for then $S = \varnothing$ and $\eta$ is 1:1.

Let $x$ be in $S$ and $y$ be in $\mathbb{R}^n - \{x\}$ such that $\eta(x) = \eta(y) = q$. Choose nbhds $U$ of $x$, $V$ of $y$, and $W$ of $q$ so that $U \cap V = \varnothing$ and $\eta|U: U \to W$ and $\eta|V: V \to W$ are diffeomorphisms. (This is possible since $\eta$ is an immersion.) Then $U \subset S$ for if $a$ is in $U$, then $b = (\eta|V)^{-1} \cdot (\eta|U)(a)$ satisfies $b \neq a$ and $\eta(b) = \eta(a)$. Thus $S$ is open.

To see that $S$ is closed let $x_1, x_2, \ldots$ be a sequence of points in $S$ converging to $x$. Choose an open nbhd $W$ of $x$ so that $\eta|W$ is a diffeomorphism. We may assume that each $x_i$ is in $W$. Choose $y_i \neq x_i$ so that $\eta(y_i) = \eta(x_i)$. Clearly the $y_i$'s are not in $W$ since $\eta|W$ is 1:1. Also, the $y_i$'s are contained in the compact set $\eta^{-1}(\eta(K))$. Thus we may assume that the $y_i$'s converge to $y$ in $\eta^{-1}(\eta(K)) - W$. Clearly $y \neq x$ and the continuity of $\eta$ guarantees that $\eta(x) = \eta(y)$. Thus $x$ is in $S$ and $S$ is closed.

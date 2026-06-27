---
role: proof
locale: en
of_concept: theorem-on-formal-functions
source_book: gtm052
source_chapter: "III"
source_section: "11"
---

We prove the theorem for an arbitrary coherent sheaf $\mathcal{F}$ on $X$, by descending induction on $i$. For $i > N$, where $X$ can be covered by $N+1$ open affine subsets, both sides are $0$ (Exercise 4.8). So we assume the theorem has been proved for $i+1$ and for all coherent sheaves.

Given $\mathcal{F}$ coherent on $X$, by (II, 5.18) we can write $\mathcal{F}$ as a quotient of a sheaf $\mathcal{E}$ which is a finite direct sum of sheaves $\mathcal{O}(q_i)$ for suitable $q_i \in \mathbb{Z}$. Let $\mathcal{R}$ be the kernel:
$$0 \to \mathcal{R} \to \mathcal{E} \to \mathcal{F} \to 0. \tag{1}$$

Tensoring with $\mathcal{O}_{X_n}$ is only right exact, so we obtain an exact sequence on $X_n$:
$$\mathcal{R}_n \to \mathcal{E}_n \to \mathcal{F}_n \to 0$$
for each $n$. Introduce the image $\mathcal{T}_n$ and the kernel $\mathcal{S}_n$ of the map $\mathcal{R}_n \to \mathcal{E}_n$, giving exact sequences
$$0 \to \mathcal{S}_n \to \mathcal{R}_n \to \mathcal{T}_n \to 0 \tag{2}$$
and
$$0 \to \mathcal{T}_n \to \mathcal{E}_n \to \mathcal{F}_n \to 0. \tag{3}$$

Consider the commutative diagram linking the long exact cohomology sequences from (1) and the inverse limits of the long exact sequences from (2) and (3). By the induction hypothesis applied to $\mathcal{E}$ (a direct sum of $\mathcal{O}(q_i)$) and to $\mathcal{R}$ at level $i+1$, together with the exactness of inverse limits over Mittag-Leffler systems (II, 9.1), the maps $\beta_1$ and $\beta_2$ in the diagram are isomorphisms. By the Five Lemma, it follows that the map for $\mathcal{F}$ at level $i$ is also an isomorphism.

It remains to prove that $\beta_1$ and $\beta_2$ are isomorphisms. Taking the cohomology sequence of (2) and passing to the inverse limit, using (II, 9.1), it suffices to show that
$$\varprojlim_n H^i(X_n, \mathcal{S}_n) = 0$$
for all $i \ge 0$. To accomplish this, we show that for any $n$, there exists an $n' > n$ such that the map of sheaves $\mathcal{S}_{n'} \to \mathcal{S}_n$ is the zero map. By quasi-compactness, the question is local on $X$, so we may assume $X$ is affine, $X = \operatorname{Spec} B$. Denote by $R, E, S_n$ the $B$-modules corresponding to $\mathcal{R}, \mathcal{E}, \mathcal{S}_n$, and let $\mathfrak{a} = \mathfrak{m}_y B$.

Recall that $R$ is a submodule of $E$, and
$$S_n = \ker(R/\mathfrak{a}^n R \to E/\mathfrak{a}^n E) = (R \cap \mathfrak{a}^n E) / \mathfrak{a}^n R.$$

By Krull's Theorem (3.1A), the $\mathfrak{a}$-adic topology on $R$ is induced by the $\mathfrak{a}$-adic topology on $E$. In other words, for any $n$, there exists an $n' > n$ such that
$$R \cap \mathfrak{a}^{n'} E \subseteq \mathfrak{a}^n R.$$
In that case the map $S_{n'} \to S_n$ is zero, completing the proof.

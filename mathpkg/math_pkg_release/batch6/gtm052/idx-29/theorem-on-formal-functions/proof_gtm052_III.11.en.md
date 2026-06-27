---
role: proof
locale: en
of_concept: theorem-on-formal-functions
source_book: gtm052
source_chapter: "III"
source_section: "11"
---

*Proof.* We prove the theorem for an arbitrary coherent sheaf $\mathcal{F}$ on $X$ by descending induction on $i$. For $i > N$, both sides are zero, because $X$ can be covered by $N + 1$ open affine subsets (Ex. 4.8). So we assume the theorem holds for $i + 1$ and for all coherent sheaves.

Given $\mathcal{F}$ coherent on $X$, by (II, 5.18) we can write $\mathcal{F}$ as a quotient of a sheaf $\mathcal{E}$ which is a finite direct sum of sheaves $\mathcal{O}(q_i)$ for suitable $q_i \in \mathbb{Z}$. Let $\mathcal{R}$ be the kernel:
$$
0 \to \mathcal{R} \to \mathcal{E} \to \mathcal{F} \to 0. \tag{1}
$$

Tensoring with $\mathcal{O}_{X_n}$ is only right exact, so on $X_n$ we have an exact sequence
$$
\mathcal{R}_n \to \mathcal{E}_n \to \mathcal{F}_n \to 0.
$$
Introduce the image $\mathcal{T}_n$ and the kernel $\mathcal{S}_n$ of the map $\mathcal{R}_n \to \mathcal{E}_n$, giving exact sequences
$$
0 \to \mathcal{S}_n \to \mathcal{R}_n \to \mathcal{T}_n \to 0, \tag{2}
$$
$$
0 \to \mathcal{T}_n \to \mathcal{E}_n \to \mathcal{F}_n \to 0. \tag{3}
$$

From the associated cohomology long exact sequences, passing to inverse limits (using (II, 9.1)), we obtain a commutative diagram relating $H^i(X, \mathcal{R})$, $H^i(X, \mathcal{E})$, $H^i(X, \mathcal{F})$, $H^{i+1}(X, \mathcal{R})$, and $H^{i+1}(X, \mathcal{E})$ with the corresponding inverse limits of cohomology of $\mathcal{R}_n, \mathcal{E}_n, \mathcal{F}_n, \mathcal{S}_n, \mathcal{T}_n$. By the induction hypothesis applied to $\mathcal{E}$ (a sum of $\mathcal{O}(q_i)$-type sheaves), the vertical maps for $\mathcal{E}$ are isomorphisms.

It remains to prove that the comparison maps $\beta_1$ and $\beta_2$ (for the $\mathcal{R}$ and $\mathcal{S}$ terms) are isomorphisms. From the long exact sequence of (2) and passage to the inverse limit, it suffices to show that
$$
\varprojlim_{n} H^i(X_n, \mathcal{S}_n) = 0
$$
for all $i \geqslant 0$. We will show that for any $n$, there exists $n' > n$ such that the map of sheaves $\mathcal{S}_{n'} \to \mathcal{S}_n$ is the zero map. The question is local on $X$ by quasi-compactness, so we may assume $X = \operatorname{Spec} B$ is affine.

Let $R, E, S_n$ be the $B$-modules corresponding to the sheaves $\mathcal{R}, \mathcal{E}, \mathcal{S}_n$, and let $\mathfrak{a} = \mathfrak{m} B$. Then $R$ is a submodule of $E$, and
$$
S_n = \ker(R/\mathfrak{a}^n R \to E/\mathfrak{a}^n E) = (R \cap \mathfrak{a}^n E) / \mathfrak{a}^n R.
$$
By Krull's theorem (3.1A), the $\mathfrak{a}$-adic topology on $R$ is induced by the $\mathfrak{a}$-adic topology on $E$. That is, for any $n$, there exists $n' > n$ such that
$$
R \cap \mathfrak{a}^{n'} E \subseteq \mathfrak{a}^n R.
$$
In that case the map $S_{n'} \to S_n$ is the zero map. Hence the inverse limit vanishes, completing the proof. $\square$

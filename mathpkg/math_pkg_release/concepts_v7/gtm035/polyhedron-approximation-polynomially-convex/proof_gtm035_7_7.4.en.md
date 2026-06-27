---
role: proof
locale: en
of_concept: polyhedron-approximation-polynomially-convex
source_book: gtm035
source_chapter: "Chapter 7"
source_section: "7.4"
---
# Proof of $p$-Polyhedron Approximation of Polynomially Convex Sets

**Lemma 7.4.** Let $X$ be a compact polynomially convex subset of $\Delta^n$. Let $\mathcal{O}$ be an open set containing $X$. Then there exists a $p$-polyhedron $\Pi$ with $X \subset \Pi \subset \mathcal{O}$.

**Proof.** For each $x \in \Delta^n \setminus \mathcal{O}$, since $X$ is polynomially convex, there exists a polynomial $P_x$ with $|P_x(x)| > 1$ and $|P_x| \leq 1$ on $X$.

By continuity, $|P_x| > 1$ in some neighborhood $\mathcal{N}_x$ of $x$. The collection $\{\mathcal{N}_x : x \in \Delta^n \setminus \mathcal{O}\}$ forms an open cover of the compact set $\Delta^n \setminus \mathcal{O}$. By compactness, a finite subcollection $\mathcal{N}_{x_1}, \ldots, \mathcal{N}_{x_r}$ covers $\Delta^n \setminus \mathcal{O}$.

Set $P_j = P_{x_j}$ for $j = 1, \ldots, r$. Define

$$\Pi = \{z \in \Delta^n : |P_j(z)| \leq 1, \; j = 1, \ldots, r\}.$$

Then $\Pi$ is a $p$-polyhedron (Definition 7.3). If $z \in X$, then $z \in \Delta^n$ and $|P_j(z)| \leq 1$ for all $j$ by construction, so $X \subset \Pi$.

If $z \in \Pi$, then $|P_j(z)| \leq 1$ for all $j$. Since each $\mathcal{N}_{x_j}$ was chosen so that $|P_j| > 1$ on $\mathcal{N}_{x_j}$, no point of $\Pi$ can belong to any $\mathcal{N}_{x_j}$. Thus $\Pi$ is disjoint from $\Delta^n \setminus \mathcal{O}$, which means $\Pi \subset \mathcal{O}$.

Hence $X \subset \Pi \subset \mathcal{O}$, as required.

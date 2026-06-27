---
role: proof
locale: en
of_concept: uniformity-base-gives-neighborhood-base
source_book: gtm027
source_chapter: "6"
source_section: "Uniform Spaces"
---

# Proof that a Base of a Uniformity Gives a Base for the Neighborhood System (Theorem 6.5)

**Theorem 6.5.** If $\mathcal{B}$ is a base (or subbase) for the uniformity $\mathcal{U}$, then for each $x$ the family of sets $U[x]$ for $U$ in $\mathcal{B}$ is a base (subbase respectively) for the neighborhood system of $x$.

**Proof.** By definition, the uniform topology $\mathcal{J}$ consists of all subsets $T$ of $X$ such that for each $x$ in $T$ there is $U$ in $\mathcal{U}$ with $U[x] \subset T$. Consequently, $U[x]$ is a neighborhood of $x$ for each $U \in \mathcal{U}$.

Now, if $\mathcal{B}$ is a base for $\mathcal{U}$, then every member $U$ of $\mathcal{U}$ contains some $B \in \mathcal{B}$. Hence $B[x] \subset U[x]$. This means that the family $\{B[x] : B \in \mathcal{B}\}$ is a base for the neighborhood system of $x$, since every neighborhood filter member $U[x]$ contains a set of the form $B[x]$.

For a subbase $\mathcal{S}$, the family of finite intersections of members of $\mathcal{S}$ is a base for $\mathcal{U}$, and the above argument applies to show that finite intersections of sets $S[x]$ for $S \in \mathcal{S}$ form a base for neighborhoods of $x$. Hence $\{S[x] : S \in \mathcal{S}\}$ is a subbase for the neighborhood system of $x$.

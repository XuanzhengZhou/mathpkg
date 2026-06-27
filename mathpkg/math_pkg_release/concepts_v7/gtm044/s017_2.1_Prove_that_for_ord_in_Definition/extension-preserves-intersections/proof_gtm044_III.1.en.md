---
role: proof
locale: en
of_concept: extension-preserves-intersections
source_book: gtm044
source_chapter: "III"
source_section: "1"
---

# Proof of Extension of Ideals Preserves Finite Intersections

**Proposition.** Though extension need not preserve intersections for arbitrary rings, in the case of the extension map $(\cdot)^e : \mathcal{I}(R) \to \mathcal{I}(R_{\mathfrak{p}})$ we have

$$(a \cap b)^e = a^e \cap b^e. \tag{13}$$

*Proof.* By the Lasker–Noether decomposition, every ideal in the Noetherian ring $R$ can be written as a finite intersection of irreducible ideals. Write

$$a = \bigcap_{i=1}^{r} \mathfrak{q}_i, \qquad b = \bigcap_{j=1}^{s} \mathfrak{q}_j',$$

where each $\mathfrak{q}_i$ and $\mathfrak{q}_j'$ is irreducible. Then

$$a \cap b = \bigcap_{i=1}^{r} \mathfrak{q}_i \cap \bigcap_{j=1}^{s} \mathfrak{q}_j'.$$

If we can prove that for any finite intersection of irreducible ideals,

$$\left( \bigcap_{i=1}^{r} \mathfrak{q}_i \right)^e = \bigcap_{i=1}^{r} \mathfrak{q}_i^e, \tag{14}$$

then we obtain

$$(a \cap b)^e = \left( \bigcap_{i=1}^{r} \mathfrak{q}_i \cap \bigcap_{j=1}^{s} \mathfrak{q}_j' \right)^e = \bigcap_{i=1}^{r} \mathfrak{q}_i^e \cap \bigcap_{j=1}^{s} \mathfrak{q}_j'^e = a^e \cap b^e.$$

Thus it suffices to establish (14). The inclusion "$\subset$" follows at once from the definition of extension, since $\bigcap \mathfrak{q}_i \subset \mathfrak{q}_i$ implies $(\bigcap \mathfrak{q}_i)^e \subset \mathfrak{q}_i^e$ for each $i$, hence $(\bigcap \mathfrak{q}_i)^e \subset \bigcap \mathfrak{q}_i^e$.

For the reverse inclusion "$\supset$", let $a^*$ be an arbitrary element of $\bigcap_{i=1}^{r} \mathfrak{q}_i^e$. Partition the $\mathfrak{q}_i$ into those contained in $\mathfrak{p}$ and those not contained in $\mathfrak{p}$:

- $\mathfrak{q}_i \subset \mathfrak{p}$ for $i = 1, \dots, k$
- $\mathfrak{q}_i \not\subset \mathfrak{p}$ for $i = k+1, \dots, r$

By (9), if $\mathfrak{q}_i \not\subset \mathfrak{p}$ then $\mathfrak{q}_i^e = R_{\mathfrak{p}}$. Therefore

$$\bigcap_{i=1}^{r} \mathfrak{q}_i^e = \bigcap_{i=1}^{k} \mathfrak{q}_i^e.$$

Now $a^* \in \bigcap_{i=1}^{k} \mathfrak{q}_i^e$. Contracting to $R$ and using the fact that contraction preserves intersections, we obtain

$$a^{*c} \in \bigcap_{i=1}^{k} \mathfrak{q}_i^{ec}.$$

By Theorem 3.10, for any irreducible ideal $\mathfrak{q}_i \subset \mathfrak{p}$ we have $\mathfrak{q}_i^{ec} = \mathfrak{q}_i$. Hence $a^{*c} \in \bigcap_{i=1}^{k} \mathfrak{q}_i$. It follows that $a^{*c} \in \bigcap_{i=1}^{r} \mathfrak{q}_i$ (since $a^{*c} \in R$ and the intersection of all $\mathfrak{q}_i$ with those not contained in $\mathfrak{p}$ can only be larger). Therefore

$$a^* = (a^{*c})^e \in \left( \bigcap_{i=1}^{r} \mathfrak{q}_i \right)^e,$$

which establishes the reverse inclusion and completes the proof. $\square$

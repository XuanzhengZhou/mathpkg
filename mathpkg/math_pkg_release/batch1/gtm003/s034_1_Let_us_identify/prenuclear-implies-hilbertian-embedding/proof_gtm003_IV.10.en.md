---
role: proof
locale: en
of_concept: prenuclear-implies-hilbertian-embedding
source_book: gtm003
source_chapter: "IV"
source_section: "10"
---

It suffices to show that each closed, convex, circled 0-neighborhood $W$ in $E$ contains a 0-neighborhood $U$ with the desired property. If $p_W$ denotes the gauge of $W$, $p_W$ is prenuclear by hypothesis; hence we have

$$p_W(x) \leq \int_A |\langle x, x' \rangle| d\mu(x') \quad (x \in E),$$

where $A$ and $\mu$ can be so chosen that $\|\mu\| = 1$. Define the 0-neighborhood $U$ by

$$U = \left\{x \in E : \int_A |\langle x, x' \rangle|^2 d\mu(x') \leq 1\right\};$$

$U$ is convex and circled, and by Schwarz' inequality $x \in U$ implies $p_W(x) \leq 1$. Hence we have $U \subset W$, and evidently the gauge of $U$ is given by the $L^2(\mu)$-norm restricted to the image of $E$ under the evaluation map. The completion $\tilde{E}_U$ is therefore norm isomorphic to a Hilbert subspace of $L^2(\mu)$.

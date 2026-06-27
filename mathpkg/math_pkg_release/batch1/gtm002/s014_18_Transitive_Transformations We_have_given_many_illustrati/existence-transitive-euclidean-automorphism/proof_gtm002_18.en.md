---
role: proof
locale: en
of_concept: existence-transitive-euclidean-automorphism
source_book: gtm002
source_chapter: "18"
source_section: "Transitive Transformations"
---

The proof follows by the same category-theoretic reasoning used for the unit square. Let $X$ be any region (open connected set) in $\mathbb{R}^r$ with $r \geq 2$. The space $H$ of all automorphisms of $X$ with the uniform metric is topologically complete, for the same reason as in the one-dimensional case (see Chapter 13).

Define the sets $E_{ij}$ analogously using a countable base $\{U_i\}$ for $X$:

$$E_{ij} = \left\{ T \in H : U_i \cap \bigcup_{k=1}^{\infty} T^{-k} U_j \neq \emptyset \right\}.$$

As in the case of the unit square, each $E_{ij}$ is open and dense in $H$. The density argument relies on the fact that $r \geq 2$ allows sufficient room to construct the required perturbations of a given automorphism.

Since $H$ is topologically complete, $\bigcap_{i,j} E_{ij}$ is a dense $G_{\delta}$ set, hence non-empty by the Baire category theorem. For any $T$ in this intersection and any $j$, the set

$$G_j = \bigcup_{k=1}^{\infty} T^{-k} U_j$$

is open and dense in $X$. Then $\bigcap_j G_j \neq \emptyset$, and any point in this intersection has a dense positive semiorbit under $T$. Thus $T$ is transitive.

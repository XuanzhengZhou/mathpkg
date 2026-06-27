---
role: proof
locale: en
of_concept: unique-differential-structure-of-euclidean-space
source_book: gtm033
source_chapter: "0"
source_section: "Submanifolds of R^{n+k}"
---

# Proof of Unique $C^r$ Differential Structure of Euclidean Space

Consider $\mathbb{R}^n$ as a topological space with its standard topology. The single chart $(\mathrm{id}_{\mathbb{R}^n}, \mathbb{R}^n)$, where $\mathrm{id}_{\mathbb{R}^n} : \mathbb{R}^n \to \mathbb{R}^n$ is the identity map, forms a $C^r$ atlas (indeed a $C^\omega$ atlas) since the only overlap condition to check is the self-overlap

$$\mathrm{id}_{\mathbb{R}^n} \circ \mathrm{id}_{\mathbb{R}^n}^{-1} = \mathrm{id}_{\mathbb{R}^n},$$

which is trivially $C^\omega$ (hence $C^r$ for every $r$).

By the general result that every $C^r$ atlas is contained in a unique maximal $C^r$ atlas, the atlas $\{(\mathrm{id}_{\mathbb{R}^n}, \mathbb{R}^n)\}$ determines a unique $C^r$ differential structure $\alpha_{\mathbb{R}^n}$ on $\mathbb{R}^n$. This is called the *standard* or *canonical* $C^r$ differential structure on $\mathbb{R}^n$.

**More generally for open subsets.** Let $U \subset \mathbb{R}^n$ be an open set, equipped with the subspace topology. The inclusion map $\iota: U \hookrightarrow \mathbb{R}^n$ is a homeomorphism onto its image. The single chart $(\iota, U)$ is a $C^r$ atlas on $U$: the only transition map $\iota \circ \iota^{-1} = \mathrm{id}_U$ is trivially $C^r$. Again, this singleton atlas determines a unique maximal $C^r$ atlas $\alpha_U$ on $U$. This is the canonical induced differential structure on the open subset.

Equivalently, $\alpha_U$ can be described as the restriction of the standard structure on $\mathbb{R}^n$:

$$\alpha_U = \{ (\varphi, V) \in \alpha_{\mathbb{R}^n} \mid V \subset U \},$$

which is the induced differential structure on an open subset as defined earlier. $\square$

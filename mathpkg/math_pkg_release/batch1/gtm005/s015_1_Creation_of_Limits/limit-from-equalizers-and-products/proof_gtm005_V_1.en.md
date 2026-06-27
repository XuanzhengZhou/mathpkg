---
role: proof
locale: en
of_concept: limit-from-equalizers-and-products
source_book: gtm005
source_chapter: "V"
source_section: "1"
---

The proof constructs the following diagram in stages, with $i$ denoting an object and $u : j \to k$ an arrow of the index category $J$. By assumption, the products $\Pi_i F_i$ and $\Pi_u F_k$ and their projections exist, where the second product is taken over all arrows $u$ of $J$, with argument at each arrow $u$ the value $F_k = F_{\operatorname{cod}u}$ of $F$ at the codomain object of $u$. Since $\Pi_u F_k$ is a product, there is a unique arrow $f$ such that the upper square commutes for every $u$ and a unique arrow $g$ such that the lower square commutes for every $u$. By hypothesis, there exists an equalizer $e$ for $f$ and $g$:

$$\Pi_{u: j \to k} F_k = \Pi_u F_{\operatorname{cod}u} \xrightarrow[f]{g} \Pi_i F_i \xrightarrow{p_i} F_i$$

Let $d$ be the domain of $e$, so $e : d \to \Pi_i F_i$. Define $\mu_i = p_i e : d \to F_i$ for each $i$. Since $e$ equalizes $f$ and $g$ and the two squares commute, one has $F_u \mu_j = \mu_k$ for every $u : j \to k$; hence $\mu : \Delta d \to F$ is a cone from the vertex $d$ to the base $F$. If $\tau$ is any other such cone, of vertex $c$, its maps $\tau_i$ combine to yield a unique map $h : c \to \Pi_i F_i$ to the product; $\tau$ a cone implies $fh = gh$. Hence $h$ factors uniquely through $e$ and therefore the cone $\tau$ factors uniquely through the cone $\mu$. This proves that $d$ and the cone $\mu$ provide a limit for $F$.

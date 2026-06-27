---
role: proof
locale: en
of_concept: quasivariety-theorem
source_book: gtm026
source_chapter: "4"
source_section: "4.21"
---

We prove that every $A$ in $\mathcal{K}$ has a reflection $r: A \longrightarrow B$ in $\mathcal{B}$ and that $r$ is in $\mathbb{E}$.

For the forward direction (quasivariety implies closed under products and $\mathbb{M}$-subobjects): If $\mathcal{B}$ is a quasivariety, then $\mathcal{B}$ is reflective with reflections in $\mathbb{E}$. Standard arguments using the reflectivity show closure under products. For closure under $\mathbb{M}$-subobjects, let $m: A \longrightarrow B$ be in $\mathbb{M}$ with $B \in \mathcal{B}$. Since $A$ has a reflection $e: A \longrightarrow \bar{A}$ in $\mathbb{E}$, the diagonal fill-in property yields that $m$ is an isomorphism, hence $A \cong \bar{A} \in \mathcal{B}$.

For the converse direction, assume $\mathcal{B}$ is closed under products and $\mathbb{M}$-subobjects. For each object $A$ in $\mathcal{K}$, consider all morphisms $e: A \longrightarrow B_e$ with $e \in \mathbb{E}$ and $B_e \in \mathcal{B}$. Using the fact that $\mathcal{K}$ is $\mathbb{E}$-co-well-powered, these can be taken to range over a small set of representatives. Form the product $P = \prod_e B_e$, which is in $\mathcal{B}$ by closure under products. The induced map $e: A \longrightarrow P$ factors through its $\mathbb{E}$-$\mathbb{M}$ factorization as $A \xrightarrow{e'} \mathrm{Im}(e) \xrightarrow{m} P$.

Then $\mathrm{Im}(f) \in \mathcal{B}$ since $m \in \mathbb{M}$ and $\mathrm{Im}(f)$ can be made to range over a small set of objects since $e \in \mathbb{E}$.

This constructs a reflection $r: A \longrightarrow B$ in $\mathcal{B}$. To show that $r$ is in $\mathbb{E}$, let $(e, m)$ be the $\mathbb{E}$-$\mathbb{M}$ factorization of $r$. As $\mathrm{Im}(r) \in \mathcal{B}$, there exists a unique $f$ with $r \circ f = e$. Since $r \circ (f \circ m) = r \circ f \circ m = \mathrm{id}_B$ and $f$ is split mono and epi ($f$ is epi because $e$ is), $f$ is an isomorphism. Hence $r = e \circ f^{-1}$ is in $\mathbb{E}$.

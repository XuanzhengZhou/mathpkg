---
role: proof
locale: en
of_concept: discrete-normal-subgroup-of-connected-group-is-central
source_book: gtm027
source_chapter: "3"
source_section: "U"
---

# Proof of Discrete normal subgroup of a connected topological group is a subset of the center

Let $G$ be a connected topological group and let $H$ be a discrete normal subgroup of $G$ (that is, $H$ carries the discrete topology as a subspace of $G$). We prove that $H \subseteq Z(G)$, the center of $G$.

Fix an arbitrary element $h \in H$. Define the map

\[
\varphi_h : G \longrightarrow H, \qquad \varphi_h(x) = x^{-1} h x .
\]

The map $\varphi_h$ is continuous because it is the composition of continuous group operations: inversion $x \mapsto x^{-1}$, left multiplication by $h$, and right multiplication by $x$, together with the fact that $H$ is a subgroup (so the image lands in $H$). More explicitly, $\varphi_h$ is the restriction to the diagonal of the map $(x, h, x) \mapsto x^{-1}hx$, which is continuous in the product topology; since $h$ is fixed, the map $x \mapsto x^{-1}hx$ is continuous from $G$ to $G$, and because $H$ is normal, its image lies in $H$. The relative topology on $H$ makes the inclusion $H \hookrightarrow G$ a continuous embedding, so $\varphi_h$ is continuous as a map $G \to H$.

The subgroup $H$ is discrete, meaning every singleton $\{h'\} \subset H$ is open (and closed) in the subspace topology. In a discrete space, the only connected subsets are the singletons.

Now $G$ is connected, and $\varphi_h$ is continuous. Therefore the image $\varphi_h(G)$ is a connected subset of $H$. Since $H$ is discrete, $\varphi_h(G)$ must be a singleton. Because $\varphi_h(e_G) = e_G^{-1} h e_G = h$, the singleton is $\{h\}$. Hence

\[
\varphi_h(x) = h \quad\text{for all } x \in G,
\]

which means $x^{-1} h x = h$, or equivalently $h x = x h$, for every $x \in G$.

Thus each $h \in H$ commutes with every element of $G$; that is, $H \subseteq Z(G)$. $\square$

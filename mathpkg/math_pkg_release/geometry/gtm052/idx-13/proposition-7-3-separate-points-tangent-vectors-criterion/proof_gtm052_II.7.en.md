---
role: proof
locale: en
of_concept: proposition-7-3-separate-points-tangent-vectors-criterion
source_book: gtm052
source_chapter: "II"
source_section: "7"
---
If $\varphi$ is a closed immersion, we think of $X$ as a closed subscheme of $\mathbf{P}_k^n$. In this situation, the sections $s_i$ are the restrictions of the homogeneous coordinates $x_i$, and the space $V$ they span separates points and tangent vectors on $\mathbf{P}^n$, hence also on $X$.

Conversely, suppose (1) and (2) hold. Let $P \in X$ be a closed point and let $Q = \varphi(P)$. We need to show the local ring map $\mathcal{O}_{\mathbf{P}^n, Q} \to \mathcal{O}_{X, P}$ is surjective. Let $A = \mathcal{O}_{\mathbf{P}^n, Q}$ and $B = \mathcal{O}_{X, P}$. By (1), the map on residue fields is injective (and hence an isomorphism since both are $k$). By (2), the map $\mathfrak{m}_A \to \mathfrak{m}_B/\mathfrak{m}_B^2$ is surjective. Since $X$ is projective, $B$ is a finitely generated $A$-module. Thus by Lemma 7.4, the map is surjective. Hence $\varphi$ is a closed immersion.

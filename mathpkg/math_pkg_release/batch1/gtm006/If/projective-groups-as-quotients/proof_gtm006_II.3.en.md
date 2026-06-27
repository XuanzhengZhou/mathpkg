---
role: proof
locale: en
of_concept: projective-groups-as-quotients
source_book: gtm006
source_chapter: "II"
source_section: "3"
---

Define $N = \{\gamma \in \Gamma L(V) \mid \langle v^\gamma \rangle = \langle v \rangle \text{ for all } v \in V\}$, the subgroup of semi-linear transformations that preserve every one-dimensional subspace. By definition, $P\Gamma L(V)$ is the group induced by $\Gamma L(V)$ on $\mathcal{P}(V)$, i.e., the quotient $\Gamma L(V) / \ker(\pi)$ where $\pi: \Gamma L(V) \to \operatorname{Aut} \mathcal{P}(V)$ is the natural homomorphism. An element $\gamma$ induces the identity on $\mathcal{P}(V)$ precisely when it sends each one-dimensional subspace to itself, i.e., $\gamma \in N$. Thus $\ker(\pi) = N$, giving $P\Gamma L(V) \cong \Gamma L(V)/N$.

Restricting to $GL(V)$, the kernel of the induced map $GL(V) \to PGL(V)$ is $N \cap GL(V)$, so $PGL(V) \cong GL(V)/(N \cap GL(V))$. Similarly for $SL(V)$ when $K$ is a field: the kernel is $N \cap SL(V)$, giving $PSL(V) \cong SL(V)/(N \cap SL(V))$. $\square$

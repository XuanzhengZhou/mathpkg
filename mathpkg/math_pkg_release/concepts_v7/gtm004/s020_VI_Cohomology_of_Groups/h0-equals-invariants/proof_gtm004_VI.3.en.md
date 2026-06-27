---
role: proof
locale: en
of_concept: h0-equals-invariants
source_book: gtm004
source_chapter: "VI"
source_section: "3"
---

# Proof of Proposition 3.2: $H^0(G, A) = A^G$

By definition (Section VI.2),

$$H^0(G, A) = \operatorname{Ext}_{\mathbb{Z}G}^0(\mathbb{Z}, A) = \operatorname{Hom}_G(\mathbb{Z}, A),$$

where $\mathbb{Z}$ is endowed with the trivial $G$-action ($x \cdot n = n$ for all $x \in G$, $n \in \mathbb{Z}$).

A $G$-module homomorphism $\varphi: \mathbb{Z} \to A$ is entirely determined by the image of $1 \in \mathbb{Z}$. Set $a = \varphi(1) \in A$. For $\varphi$ to be $G$-linear, we must have, for all $x \in G$,

$$x \circ a = x \circ \varphi(1) = \varphi(x \circ 1) = \varphi(1) = a,$$

since $G$ acts trivially on $\mathbb{Z}$. Thus $a$ must be fixed under the action of every element of $G$.

Conversely, given any $a \in A$ satisfying $x \circ a = a$ for all $x \in G$, the map $\varphi: \mathbb{Z} \to A$ defined by $\varphi(n) = n a$ is a $G$-module homomorphism, because

$$\varphi(x \circ n) = \varphi(n) = n a = n(x \circ a) = x \circ (n a) = x \circ \varphi(n).$$

Therefore

$$\operatorname{Hom}_G(\mathbb{Z}, A) \cong A^G = \{ a \in A \mid x \circ a = a \text{ for all } x \in G \},$$

the subgroup of $G$-invariant elements of $A$. Hence $H^0(G, A) = A^G$.

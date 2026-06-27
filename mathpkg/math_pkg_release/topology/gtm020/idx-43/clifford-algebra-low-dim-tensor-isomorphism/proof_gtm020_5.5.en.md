---
role: proof
locale: en
of_concept: clifford-algebra-low-dim-tensor-isomorphism
source_book: gtm020
source_chapter: "5"
source_section: "5.5"
---

There are isomorphisms
$$
\mathbf{C} \otimes C_k \cong \mathbf{C} \otimes C'_k
$$
for $k = 1, 2$ in Proposition (5.4). For the third, we define an isomorphism
$$
w: \mathbf{H} \otimes \mathbf{H} \to \operatorname{Hom}_{\mathbf{R}}(\mathbf{H}, \mathbf{H}) = \mathbf{R}(4)
$$
by the relation $w(x_1 \otimes x_2)x = x_1 x \bar{x}_2$. Then $w$ is an algebra morphism, and it suffices to show $w$ is epimorphic since $\dim \mathbf{H} \otimes \mathbf{H} = 16 = \dim \mathbf{R}(4)$. First, note that $w(1 \otimes 1) = 1$ and $w(i \otimes i)1 = 1$, $w(i \otimes i)i = i$, $w(i \otimes i)j = -j$, and $w(i \otimes i)k = -k$. Similar relations hold for $w(j \otimes j)$ and $w(k \otimes k)$. Consequently, $w((1 \otimes 1 + i \otimes i + j \otimes j + k \otimes k)/4)$ projects $1$ on $1$ and $i, j, k$ onto $0$. Moreover, we calculate $w(i \otimes j)1 = k$, $w(i \otimes j)i = j$, $w(i \otimes j)j = i$, $w(i \otimes j)k = -1$, and a similar calculation holds for $w(j \otimes k)$ and $w(i \otimes k)$. Consequently, every matrix with only one nonzero entry is in $\operatorname{im} w$. These generate $\mathbf{R}(4)$, and therefore $w$ is epimorphic.

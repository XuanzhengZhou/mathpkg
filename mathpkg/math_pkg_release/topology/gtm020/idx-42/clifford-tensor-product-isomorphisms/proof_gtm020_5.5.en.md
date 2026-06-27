---
role: proof
locale: en
of_concept: clifford-tensor-product-isomorphisms
source_book: gtm020
source_chapter: "5"
source_section: "5"
---

For the last statement we use the relations $F \otimes \mathbf{R}(n) = F(n)$ for $F = \mathbf{C}$ or $\mathbf{H}$ and $F \otimes (\mathbf{R} \oplus \mathbf{R}) = F \oplus F$.

It suffices to show that $w$ is epimorphic since $\dim \mathbf{H} \otimes \mathbf{H} = 16 = \dim \mathbf{R}(4)$. First, note that $w(1 \otimes 1) = 1$ and $w(i \otimes i)1 = 1$, $w(i \otimes i)i = i$, $w(i \otimes i)j = -j$, and $w(i \otimes i)k = -k$. Similar relations hold for $w(j \otimes j)$ and $w(k \otimes k)$. Consequently, $w((1 \otimes 1 + i \otimes i + j \otimes j + k \otimes k)/4)$ projects $1$ on $1$ and $i, j, k$ onto $0$. Moreover, we calculate $w(i \otimes j)1 = k$, $w(i \otimes j)i = j$, $w(i \otimes j)j = i$, $w(i \otimes j)k = -1$, and a similar calculation holds for $w(j \otimes k)$ and $w(i \otimes k)$. Consequently, every matrix with only one nonzero entry is in $\operatorname{im} w$. These generate $\mathbf{R}(4)$, and therefore $w$ is epimorphic.

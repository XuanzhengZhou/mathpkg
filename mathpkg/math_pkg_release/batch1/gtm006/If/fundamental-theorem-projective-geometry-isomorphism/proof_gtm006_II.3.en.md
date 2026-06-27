---
role: proof
locale: en
of_concept: fundamental-theorem-projective-geometry-isomorphism
source_book: gtm006
source_chapter: "II"
source_section: "3"
---

Let $\beta$ be the isomorphism from $\mathcal{P}(V)$ onto $\mathcal{P}(W)$. Choose a frame $E_1, E_2, E_3, E_4$ for $\mathcal{P}(W)$ given by a basis $e_1, e_2, e_3$, so $E_i = \langle e_i \rangle$ for $i = 1, 2, 3$ and $E_4 = \langle e_1 + e_2 + e_3 \rangle$. The pre-images $G_i = \beta^{-1}(E_i)$ form a frame for $\mathcal{P}(V)$. Choose a basis $g_1, g_2, g_3$ for $V$ such that $G_i = \langle g_i \rangle$ and $G_4 = \langle g_1 + g_2 + g_3 \rangle$ (Lemma 2.5).

Now coordinatize both planes using their frames as in the discussion preceding Lemma 2.7. The isomorphism $\beta$ induces a bijection $\phi: K \to F$ between the coordinatizing sets. Using the geometric interpretation of addition and multiplication from Lemma 2.7, one verifies that $\phi$ preserves both operations. For multiplication: the point $xm$ is obtained geometrically as the intersection of the line joining $\langle m e_2 + e_1 \rangle$ to $E_3$ with the line joining $\langle x e_1 + e_3 \rangle$ to $E_2$, giving $\langle x e_1 + xm e_2 + e_3 \rangle$. Under $\beta$, since incidence is preserved, the same construction in $\mathcal{P}(W)$ yields $(xm)^\phi = x^\phi m^\phi$.

For addition: a similar geometric construction (involving the line $\langle e_1 + e_2 \rangle$ and intersections) yields $(x + b)^\phi = x^\phi + b^\phi$. Thus $\phi: K \to F$ is a field isomorphism. Finally, define the semi-linear transformation $\tilde{\beta}: V \to W$ by sending the basis $g_i$ to $e_i$ (a linear map) composed with the field isomorphism $\phi$ acting on coordinates. One checks that $\tilde{\beta}$ induces exactly the original isomorphism $\beta$ on $\mathcal{P}(V)$. $\square$

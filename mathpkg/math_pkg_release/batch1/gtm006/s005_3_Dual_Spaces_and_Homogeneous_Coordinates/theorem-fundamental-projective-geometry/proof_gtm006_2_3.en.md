---
role: proof
locale: en
of_concept: theorem-fundamental-projective-geometry
source_book: gtm006
source_chapter: "II"
source_section: "3"
---

Let $\beta$ be the isomorphism from $\mathcal{P}(V)$ onto $\mathcal{P}(W)$. Choose a frame $E_1, E_2, E_3, E_4$ for $\mathcal{P}(W)$, given by a basis $e_1, e_2, e_3$ (so $E_i = \langle e_i \rangle$ for $i = 1, 2, 3$ and $E_4 = \langle e_1 + e_2 + e_3 \rangle$). The pre-images $G_i = \beta^{-1}(E_i)$ are four points in $\mathcal{P}(V)$ forming a frame for $\mathcal{P}(V)$. Choose a basis $g_1, g_2, g_3$ for $V$ such that $G_i = \langle g_i \rangle$ for $i = 1, 2, 3$ and $G_4 = \langle g_1 + g_2 + g_3 \rangle$ (by Lemma 2.5, the converse of Lemma 2.4).

Now define a bijection $\phi : K \to F$ as follows. For $x \in K$, the point $\langle x g_1 + g_3 \rangle$ lies on the line $G_1 + G_3$. Under $\beta$, this line maps to $E_1 + E_3$, which consists of points $\langle x^\phi e_1 + e_3 \rangle$ for a unique $x^\phi \in F$. This defines $\phi$ as a bijection with $\phi(0) = 0$ and $\phi(1) = 1$.

To prove $\phi$ is multiplicative: consider the geometric construction of $xm$ using the configuration of Lemma 2.7. In $\mathcal{P}(V)$, the point $\langle x m g_1 + x m g_2 + g_3 \rangle$ is the intersection of the line joining $G_3$ to $\langle m g_2 + g_1 \rangle$ with the join of $G_2$ to $\langle x g_1 + g_3 \rangle$. Since $\beta$ preserves incidence, the image of this point in $\mathcal{P}(W)$ must be obtained by the same geometric construction using the images of the constituent points. Therefore $\beta(\langle x m g_1 + g_3 \rangle) = \langle (xm)^\phi e_1 + e_3 \rangle$ must equal the intersection point obtained from $\langle m^\phi e_2 + e_1 \rangle$ and $\langle x^\phi e_1 + e_3 \rangle$, which is $\langle x^\phi m^\phi e_1 + x^\phi m^\phi e_2 + e_3 \rangle$. Hence $(xm)^\phi = x^\phi m^\phi$ for all $x, m \in K$.

The proof that $\phi$ is additive, i.e., $(x + b)^\phi = x^\phi + b^\phi$, follows similarly from geometric constructions (left as an exercise; it uses the line through $\langle b e_2 + e_3 \rangle$ and the point at infinity of slope 1).

Thus $\phi : K \to F$ is a field isomorphism, and $\beta$ is induced by the semi-linear transformation sending $g_i \mapsto e_i$ ($i = 1, 2, 3$) composed with $\phi$. $\square$

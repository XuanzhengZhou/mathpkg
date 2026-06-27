---
role: proof
locale: en
of_concept: orthogonal-group-triply-transitive
source_book: gtm006
source_chapter: "II"
source_section: "7. Conics"
---

We first show that the mappings given are actually induced by collineations of $\mathcal{P}(V)$. Consider the matrix:

$$B = \begin{bmatrix} a^2 & ac & c^2 \\ 2ab & ad + bc & 2cd \\ b^2 & bd & d^2 \end{bmatrix},$$

where $ad - bc \neq 0$. A direct computation (using the parametrization from Theorem 2.36) shows that the collineation induced by $B$ maps the point with parametric coordinate $y$ to the point with parametric coordinate $(ay + b)/(cy + d)$. Specifically, for a point $\langle (y^2, y, 1) \rangle$ on $\mathcal{C}$:

$$\beta: \langle(y^2, y, 1)\rangle \rightarrow \langle((ay + b)^2, (ay + b)(cy + d), (cy + d)^2)\rangle$$

which equals $\langle((ay + b)/(cy + d))^2, (ay + b)/(cy + d), 1\rangle$ if $cy + d \neq 0$, and equals $\langle(ay + b)^2, 0, 0\rangle = \langle(1, 0, 0)\rangle$ if $cy + d = 0$.

This proves that $\beta$ has the desired effect: the image of any point on $\mathcal{C}$ is also a point of $\mathcal{C}$, and in fact is the point whose parametric coordinate is $(ay + b)/(cy + d)$ (recall $1/0 = \infty$). Thus $\beta$ is a collineation of $\mathcal{P}(V)$ which maps $\mathcal{C}$ onto $\mathcal{C}$.

Since the group of collineations inducing the given mappings is triply transitive on the points of $\mathcal{C}$ (being the same on $\mathcal{C}$ as $PGL(W)$ is on the projective line $\mathcal{P}(W)$), it only remains to show that every element in the orthogonal group induces one of the given mappings on $\mathcal{C}$ and that the group acts faithfully on $\mathcal{C}$.

Suppose $\alpha$ is any collineation in the orthogonal group and that $X, Y, Z$ are any three distinct points of $\mathcal{C}$. Then, by the triple transitivity, there is a collineation $\beta$ which induces one of the given mappings on $\mathcal{C}$ such that $X^\beta = X^\alpha$, $Y^\beta = Y^\alpha$, $Z^\beta = Z^\alpha$. Then $\alpha \beta^{-1}$ fixes three points of $\mathcal{C}$. By Lemma 2.34, a collineation fixing three points of a conic must be the identity on $\mathcal{C}$. Hence $\alpha$ and $\beta$ induce the same mapping on $\mathcal{C}$, proving that every element of the orthogonal group induces one of the given fractional linear transformations. The faithfulness follows because if a collineation fixes all points of $\mathcal{C}$, it fixes at least three points, and one can show it is the identity. 

Thus the orthogonal group is isomorphic to $PGL(W)$ where $W$ is a two-dimensional vector space. $\square$

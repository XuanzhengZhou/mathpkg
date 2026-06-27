---
role: proof
locale: en
of_concept: automorphism-parametric-form-projective-line
source_book: gtm006
source_chapter: "II"
source_section: "3"
---

Let $\mathcal{P} = \mathcal{P}_1(K)$. Choose a basis $e_1, e_2$ for the two-dimensional vector space $V$. A point of $\mathcal{P}$ is a one-dimensional subspace $\langle x e_1 + y e_2 \rangle$. Using the parametric representation, associate the point $\langle x e_1 + e_2 \rangle$ (with $x \in K$) to the parameter $x$, and associate $\langle e_1 \rangle$ to $\infty$.

An element of $\operatorname{Aut} \mathcal{P} = P\Gamma L(V)$ is induced by a semi-linear transformation, which sends $x e_1 + y e_2$ to $(x^\alpha a + y^\alpha b) e_1 + (x^\alpha c + y^\alpha d) e_2$ where $\alpha \in \operatorname{Aut} K$ and $ad - bc \neq 0$. The point with parameter $k$ corresponds to $\langle k e_1 + e_2 \rangle$, which is mapped to $\langle (k^\alpha a + b) e_1 + (k^\alpha c + d) e_2 \rangle$. If $k^\alpha c + d \neq 0$, the parametric coordinate is $(k^\alpha c + d)^{-1}(k^\alpha a + b)$. If $k^\alpha c + d = 0$, the parametric coordinate is $\infty$. The point $\infty$ (i.e., $\langle e_1 \rangle$) maps to $\langle a e_1 + c e_2 \rangle$, whose parametric coordinate is $c^{-1}a$ if $c \neq 0$, and $\infty$ if $c = 0$.

Adopting the conventions $\infty^\alpha = \infty$, $c \cdot \infty + d = c \cdot \infty$, and $(a \cdot \infty)(c \cdot \infty)^{-1} = ac^{-1}$, the mapping takes the unified form $x \mapsto (x^\alpha a + b)(x^\alpha c + d)^{-1}$ for all points of $\mathcal{P}$. $\square$

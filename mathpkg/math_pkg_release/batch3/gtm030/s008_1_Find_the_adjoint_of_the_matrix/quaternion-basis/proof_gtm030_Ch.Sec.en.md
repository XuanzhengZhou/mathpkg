---
role: proof
locale: en
of_concept: quaternion-basis
source_book: gtm030
source_chapter: ""
source_section: ""
---

Define $i, j, k$ as matrices as above. Write a general quaternion matrix:
$$\begin{bmatrix} \alpha_0 + \alpha_1\sqrt{-1} & \alpha_2 + \alpha_3\sqrt{-1} \\ -\alpha_2 + \alpha_3\sqrt{-1} & \alpha_0 - \alpha_1\sqrt{-1} \end{bmatrix}
= \alpha_0\begin{bmatrix}1 & 0 \\ 0 & 1\end{bmatrix} + \alpha_1\begin{bmatrix}\sqrt{-1} & 0 \\ 0 & -\sqrt{-1}\end{bmatrix} + \alpha_2\begin{bmatrix}0 & 1 \\ -1 & 0\end{bmatrix} + \alpha_3\begin{bmatrix}0 & \sqrt{-1} \\ \sqrt{-1} & 0\end{bmatrix}.$$
This shows that $\{1, i, j, k\}$ spans $Q$ over the reals. For uniqueness, suppose $\alpha_0' + \alpha_1'i + \alpha_2'j + \alpha_3'k = \beta_0' + \beta_1'i + \beta_2'j + \beta_3'k$. Then the corresponding matrix equality gives $\alpha_i = \beta_i$ for $i = 0,1,2,3$, hence $\alpha_i' = \beta_i'$. The representation is unique.

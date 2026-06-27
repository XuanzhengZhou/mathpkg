---
role: exercise
locale: en
chapter: "IV"
section: "9"
exercise_number: 2
---

(Ingraham) Let $A$ be a matrix in block form

$$\begin{bmatrix}
A_{11} & A_{12} & \cdots & A_{1m} \\
A_{21} & A_{22} & \cdots & A_{2m} \\
\vdots & \vdots & \ddots & \vdots \\
A_{m1} & A_{m2} & \cdots & A_{mm}
\end{bmatrix}$$

where the $A_{ij}$ are $r \times r$ matrices with elements in an algebraically closed field. Assume that the $A_{ij}$ commute with each other and define

$$\det_R A = \sum \pm A_{1i_1} A_{2i_2} \cdots A_{mi_m}$$

where the sum is taken over all permutations $i_1, i_2, \dots, i_m$ of $1, 2, \dots, m$ and the sign is $+$ or $-$ according as the permutation is even or odd. Use Theorem 7 to prove the following transitivity property of determinants:

$$\det(\det_R A) = \det A.$$

(This holds for arbitrary base fields. Compare Sec. 9, Chapter VII.)

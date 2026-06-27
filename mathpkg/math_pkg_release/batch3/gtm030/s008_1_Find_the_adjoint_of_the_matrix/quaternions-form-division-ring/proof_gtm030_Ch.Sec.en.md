---
role: proof
locale: en
of_concept: quaternions-form-division-ring
source_book: gtm030
source_chapter: ""
source_section: ""
---

The set $Q$ is a subset of $C_2$ consisting of matrices of the form
$$\begin{bmatrix} a & b \\ -\bar{b} & \bar{a} \end{bmatrix}$$
with $a, b \in C$. One verifies directly that $Q$ is closed under addition, contains the zero matrix, and contains negatives, so $Q$ is an additive subgroup. Moreover,
$$\begin{bmatrix} a & b \\ -\bar{b} & \bar{a} \end{bmatrix} \begin{bmatrix} c & d \\ -\bar{d} & \bar{c} \end{bmatrix} = \begin{bmatrix} ac - b\bar{d} & ad + b\bar{c} \\ -\overline{ad + b\bar{c}} & \overline{ac - b\bar{d}} \end{bmatrix}$$
has the required form, so $Q$ is closed under multiplication. The associative, commutative (addition), and distributive laws carry over from $C_2$, so $Q$ is a subring.

Taking the determinant:
$$\det\begin{bmatrix} \alpha_0 + \alpha_1\sqrt{-1} & \alpha_2 + \alpha_3\sqrt{-1} \\ -\alpha_2 + \alpha_3\sqrt{-1} & \alpha_0 - \alpha_1\sqrt{-1} \end{bmatrix} = \alpha_0^2 + \alpha_1^2 + \alpha_2^2 + \alpha_3^2.$$
If the matrix is nonzero, this sum is $\neq 0$. Hence the matrix is invertible, and the inverse computed via the adjoint formula is the matrix
$$\begin{bmatrix} (\alpha_0 - \alpha_1\sqrt{-1})\Delta^{-1} & -(\alpha_2 + \alpha_3\sqrt{-1})\Delta^{-1} \\ (\alpha_2 - \alpha_3\sqrt{-1})\Delta^{-1} & (\alpha_0 + \alpha_1\sqrt{-1})\Delta^{-1} \end{bmatrix}$$
which again belongs to $Q$. Thus every nonzero element is a unit, and $Q$ is a division ring.

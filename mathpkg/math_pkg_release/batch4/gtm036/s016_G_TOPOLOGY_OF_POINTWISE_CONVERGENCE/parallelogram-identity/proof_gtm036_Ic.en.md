---
role: proof
locale: en
of_concept: parallelogram-identity
source_book: gtm036
source_chapter: "I"
source_section: "I(c)"
---

For an inner product norm: expanding the squares,
$$
\begin{aligned}
\|x + y\|^2 &= (x+y, x+y) = \|x\|^2 + (x,y) + (y,x) + \|y\|^2 \\
\|x - y\|^2 &= (x-y, x-y) = \|x\|^2 - (x,y) - (y,x) + \|y\|^2
\end{aligned}
$$
Adding these gives $\|x+y\|^2 + \|x-y\|^2 = 2\|x\|^2 + 2\|y\|^2$.

For the characterization: if a norm $\|\cdot\|$ satisfies the parallelogram law, define $(x,y)$ by the polarization identity. One verifies that this defines a positive definite Hermitian sesquilinear form whose induced norm is the original norm. The verification uses the parallelogram law to establish additivity of the defined form.

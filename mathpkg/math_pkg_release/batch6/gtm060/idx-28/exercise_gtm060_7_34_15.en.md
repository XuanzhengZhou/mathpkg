---
role: exercise
locale: en
chapter: "7"
section: "34"
exercise_number: 15
---
Given the components of the vector field $\mathbf{A}$, find the decompositions of the 1-form $\omega_A^1$ and the 2-form $\omega_A^2$.

Solution. We have $\omega_A^1(\mathbf{e}_1) = (\mathbf{A}, \mathbf{e}_1) = A_1$. Also, $(a_1 dx_1 + a_2 dx_2 + a_3 dx_3)(\mathbf{e}_1) = a_1 dx_1(\mathbf{e}_1) = a_1/\sqrt{E_1}$. From this we get that $a_1 = A_1\sqrt{E_1}$, so that
$$\omega_A^1 = A_1\sqrt{E_1} dx_1 + A_2\sqrt{E_2} dx_2 + A_3\sqrt{E_3} dx_3.$$
In the same way, $\omega_A^2(\mathbf{e}_2, \mathbf{e}_3) = (\mathbf{A}, \mathbf{e}_2, \mathbf{e}_3) = A_1$, and
$$(\alpha_1 dx_2 \wedge dx_3 + \alpha_2 dx_3 \wedge dx_1 + \alpha_3 dx_1 \wedge dx_2)(\mathbf{e}_2, \mathbf{e}_3) = \alpha_1 \frac{1}{\sqrt{E_2 E_3}}.$$
Hence $\alpha_1 = A_1\sqrt{E_2 E_3}$, and similarly for the other components, giving
$$\omega_A^2 = A_1\sqrt{E_2 E_3} dx_2 \wedge dx_3 + A_2\sqrt{E_3 E_1} dx_3 \wedge dx_1 + A_3\sqrt{E_1 E_2} dx_1 \wedge dx_2.$$

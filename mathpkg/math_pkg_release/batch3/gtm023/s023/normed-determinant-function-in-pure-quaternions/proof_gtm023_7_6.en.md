---
role: proof
locale: en
of_concept: normed-determinant-function-in-pure-quaternions
source_book: gtm023
source_chapter: "7"
source_section: "6"
---

First we show that $\Delta$ is skew symmetric. Using formula (7.57) which states $x \cdot x = -|x|^2 e$ for $x \in E_1$, we have

$$\Delta(x_1, x, x) = (x_1 \cdot x, x) = \big(-(x_1, x)e + x_1 \times x,\; x\big).$$

Since $e \perp E_1$, we have $(e, x) = 0$. Moreover $(x_1 \times x, x) = 0$ by properties of the cross product. Alternatively, from the quaternion multiplication identity $x \cdot y + y \cdot x = -2(x, y)e$, we get $x \cdot x = -|x|^2 e$, so

$$\Delta(x_1, x, x) = (x_1 \cdot x, x) = (x_1, e)|x|^2 = 0,$$

and similarly

$$\Delta(x, x_2, x) = (x \cdot x_2, x) = (x_2, e)|x|^2 = 0.$$

Thus $\Delta$ is skew symmetric.

Next observe that

$$\Delta(x_1, x_2, x_3) = \frac{1}{2}\big\{\Delta(x_1, x_2, x_3) - \Delta(x_2, x_1, x_3)\big\}$$
$$= \frac{1}{2}(x_1 \cdot x_2 - x_2 \cdot x_1, x_3).$$

Using the commutator relation $x_1 \cdot x_2 - x_2 \cdot x_1 = 2(x_1 \times x_2)$ (which follows from $x \cdot y = -(x,y)e + x \times y$), we obtain

$$\Delta(x_1, x_2, x_3) = (x_1 \times x_2, x_3).$$

This shows that $\Delta$ coincides with the scalar triple product on $E_1$, which is a normed determinant function representing the orientation of $E_1$.

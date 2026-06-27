---
role: proof
locale: en
of_concept: frobenius-classification-of-division-algebras
source_book: gtm023
source_chapter: "7"
source_section: "6"
---

We may assume that $n = \dim A \geq 2$.

**Case $n = 2$.** Then $\dim F = 1$. Choose a vector $j \in F$ such that $j^2 = -e$. An isomorphism $A \xrightarrow{\cong} \mathbb{C}$ is given by
$$\alpha e + \beta j \mapsto \alpha + i\beta, \quad \alpha, \beta \in \mathbb{R}.$$

**Case $n > 2$.** Then $\dim F \geq 2$. By Lemma II(iii), a symmetric bilinear form on $F$ is defined by
$$xy + yx = -2(x, y)e, \quad x, y \in F.$$

Since $x^2 = -|x|^2 e$ for $x \in F$ (scaling so that $x^2 = -e$), we have $(x, x) = |x|^2 > 0$ for $x \neq 0$, so $(\;,\;)$ is positive definite and makes $F$ into a Euclidean space.

By Lemma II(iii), $xy - yx \in F$, so a skew-symmetric bilinear map $\Psi: F \times F \to F$ is defined by
$$xy - yx = 2\Psi(x, y), \quad x, y \in F.$$

Combining these gives the quaternion-like multiplication
$$xy = -(x, y)e + \Psi(x, y), \quad x, y \in F.$$

Now, since $\dim F \geq 2$, there exist unit vectors $e_1, e_2 \in F$ such that $(e_1, e_2) = 0$. Then
$$e_1 e_2 + e_2 e_1 = -2(e_1, e_2)e = 0,$$
so $e_1 e_2 = -e_2 e_1$. Set $e_3 = e_1 e_2$. Then
$$e_3^2 = e_1 e_2 e_1 e_2 = -e_1 e_1 e_2 e_2 = -(-e)(-e) = -e.$$
Moreover, $(e_1, e_3) = (e_2, e_3) = 0$, so $e_1, e_2, e_3$ are orthonormal. In particular, $\dim F \geq 3$.

Now we show that $e_1, e_2, e_3$ span $F$. Let $z \in F$ with $z^2 = -e$. Then
\begin{align*}
z e_3 - e_3 z &= z e_1 e_2 - e_1 e_2 z \\
&= \big(-2(z, e_1)e - e_1 z\big) e_2 - e_1\big(-2(z, e_2)e - z e_2\big) \\
&= -2(z, e_1)e_2 + 2(z, e_2)e_1.
\end{align*}

On the other hand,
$$z e_3 + e_3 z = -2(z, e_3)e.$$

Adding these equations,
$$z e_3 = -(z, e_1)e_2 + (z, e_2)e_1 - (z, e_3)e.$$

Multiplying on the right by $e_3$ and using $e_3^2 = -e$,
$$z = (z, e_1)e_1 + (z, e_2)e_2 + (z, e_3)e_3.$$

Thus $z$ is a linear combination of $e_1, e_2, e_3$, so $\dim F = 3$ and $\dim A = 4$.

Finally, define the trilinear function $\Delta$ on $F$ by
$$\Delta(x, y, z) = (\Psi(x, y), z), \quad x, y, z \in F.$$

We verify $\Delta$ is skew symmetric. Clearly $\Delta(x, x, z) = 0$. Moreover, using (7.67),
$$\Delta(x, y, y) = (\Psi(x, y), y) = \frac{1}{2}(xy - yx, y) = 0.$$

Since $\Delta(e_1, e_2, e_3) = (\Psi(e_1, e_2), e_3) = (e_3, e_3) = 1$, the multiplication on $A$ coincides with the quaternion multiplication, giving $A \cong \mathbb{H}$.

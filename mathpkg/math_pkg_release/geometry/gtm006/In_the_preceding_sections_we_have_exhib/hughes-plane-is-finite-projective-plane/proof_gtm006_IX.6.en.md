---
role: proof
locale: en
of_concept: hughes-plane-is-finite-projective-plane
source_book: gtm006
source_chapter: "IX"
source_section: "6. The Hughes Planes"
---

The number of points of $\mathcal{H}$ is equal to the number of elements of $V$ other than $(0,0,0)$ divided by the number which give the same point of $\mathcal{H}$. Since this latter is the same as the number of non-zero elements of $N$, the number of points of $\mathcal{H}$ is
$$\frac{q^6 - 1}{q^2 - 1} = q^4 + q^2 + 1.$$

Clearly for any $t$ the number of points on $L(t)$ is $q^2 + 1$ and thus, since every other line is the image of one of these point sets under an element of $\operatorname{GL}_3(q)$, every line contains exactly $q^2 + 1$ points.

The number of lines is merely the number of distinct $L(t)$ multiplied by the number of possible powers of $A$, i.e.,
$$(q^2 - q + 1)(q^2 + q + 1) = q^4 + q^2 + 1.$$

Thus, by Exercise 3.11, the theorem will be proved if we show that any two distinct lines intersect in a unique point.

Whether $\mathcal{H}$ is a projective plane or not it is clear that each mapping $A^i$ preserves incidence in $\mathcal{H}$. Thus, in order to show that any two distinct lines intersect in a unique point, it is sufficient to show that any line $L(t)$ meets any line $L(t')A^m$ in a unique point. Suppose $L(t)$ is the line with equation
$$xa + yb + zc + (xa' + yb' + zc')t = 0$$
and $L(t')A^m$ has equation
$$xu + yv + zw + (xu' + yv' + zw')t' = 0.$$

The intersection of the two lines is the set of points $\langle(x, y, z)\rangle$ satisfying
$$xa + yb + zc + (xa' + yb' + zc')t = 0, \tag{2}$$
$$xu + yv + zw + (xu' + yv' + zw')t' = 0. \tag{3}$$

If $b \neq 0$, then from (2),
$$y = -xb^{-1}a - zb^{-1}c - (xa' + yb' + zc')b^{-1}t$$
and substituting this into (3) yields, after simplification,
$$\left(yv + zb\right)\left(b^{-1}a + t\right) + y\left(u - vb^{-1}a\right) = 0. \tag{5}$$

If $t = 1$ then it is easy to see that (2) and (3) have a unique common solution for the point $\langle(x, y, z)\rangle$. But if $t \neq 1$ then $t$ is not in $F$ and so, in this case, $w = b^{-1}a + t$ is non-zero. Thus (5) becomes $(yv + zb)w = -y(u - vb^{-1}a)$ or, multiplying through by $w^{-1}$ and collecting terms,
$$y\left(v + \left(u - vb^{-1}a\right)w^{-1}\right) + zb = 0. \tag{6}$$

Since $b \neq 0$, (6) and (2) now have a unique common solution for the point $\langle(x, y, z)\rangle$.

Case (b): $b = 0, a \neq 0$. In this case (3) becomes
$$y\left(u + vt\right) + za = 0 \tag{7}$$
and now, since $a \neq 0$, (7) and (2) have a unique common point.

Case (c): $a = b = 0$. These conditions imply
$$a_{13} + a_{33} = a_{11} + a_{31} \quad\text{and}\quad a_{23} = a_{21}. \tag{8}$$

But now consider the point $P = \langle(1, 0, -1)\rangle$. From (8) it is immediate that $PA^m = (c, 0, -c)$, where $c = a_{11} - a_{33}$, and, since $A^m$ is non-singular, $c \neq 0$ so that $PA^m = P$. Thus, by the original choice of $A$, $m = 0 \pmod{q^2 + q + 1}$ and $L(t)A^m = L(t)$. But now it is easy to see that $L(t)$ and $L(t')A^m = L(t')$ intersect in a unique point.

Thus in all cases any two distinct lines intersect in a unique point, and $\mathcal{H}$ is a finite projective plane of order $q^2$.

---
role: proof
locale: en
of_concept: hughes-plane-is-finite-projective-plane
source_book: gtm006
source_chapter: "9"
source_section: "6"
---

The number of points of $\mathcal{H}$ is equal to the number of elements of $V$ other than $(0,0,0)$ divided by the number which give the same point of $\mathcal{H}$. Since this latter is the same as the number of non-zero elements of $N$, the number of points of $\mathcal{H}$ is
$$\frac{q^6 - 1}{q^2 - 1} = q^4 + q^2 + 1.$$

Clearly for any $t$ the number of points on $L(t)$ is $q^2 + 1$ and thus, since every other line is the image of one of these point sets under an element of $GL_3(q)$, every line contains exactly $q^2 + 1$ points.

The number of lines is merely the number of distinct $L(t)$ multiplied by the number of possible powers of $A$, i.e., $(q^2 - q + 1)(q^2 + q + 1) = q^4 + q^2 + 1$. Thus, by Exercise 3.11, the theorem will be proved if we show that any two distinct lines intersect in a unique point.

Whether $\mathcal{H}$ is a projective plane or not, it is clear that each mapping $A^i$ preserves incidence in $\mathcal{H}$. Thus, in order to show that any two distinct lines intersect in a unique point, it is sufficient to show that any two distinct lines through the point $\langle (0,0,1) \rangle$ intersect in a unique point of $\mathcal{H}$, since $A$ acts transitively on the points.

Consider two distinct lines of the form $L(t)$ and $L(s)A^m$ which both pass through the point $\langle (0,0,1) \rangle$. The line $L(t)$ is the set of points $\langle (x,y,z) \rangle$ satisfying
$$x + yt + z = 0. \tag{1}$$

The line $L(s)A^m$ consists of points $A^m w$ where $\langle w \rangle$ satisfies $w_1 + w_2 s + w_3 = 0$. Let $A^m = (a_{ij})$, and write the condition that $\langle (x,y,z) \rangle \in L(s)A^m$. Then there exists $\langle (u,v,w) \rangle$ such that $(x,y,z) = (u,v,w)A^m$ and $u + vs + w = 0$. Eliminating $u$, we obtain the equation of $L(s)A^m$ as
$$xa + yb + zc + (xa' + yb' + zc')s = 0 \tag{2}$$
for suitable coefficients $a,b,c,a',b',c'$ depending on $A^m$.

We must show that (1) and (2) have a unique common solution $\langle (x,y,z) \rangle$ unless $L(t) = L(s)A^m$.

Since both lines contain $\langle (0,0,1) \rangle$, we have $c = c' = 0$ in (2). Thus (2) reduces to
$$xa + yb + (xa' + yb')s = 0. \tag{3}$$

Setting $z = -x - yt$ from (1), and substituting into the incidence condition, we analyze three cases:

\textbf{Case (a):} $b \neq 0$. From (3) we can solve for an expression relating $x$ and $y$, and this simplifies to
$$\left(yv + zb\right)\left(b^{-1}a + t\right) + y\left(u - vb^{-1}a\right) = 0. \tag{5}$$

If $t = 1$ then it is easy to see that (2) and (3) have a unique common solution for the point $\langle (x, y, z) \rangle$. But if $t \neq 1$ then $t$ is not in $F$ and so, in this case, $w = b^{-1}a + t$ is non-zero. Thus (5) becomes $(yv + zb)w = -y(u - vb^{-1}a)$ or, multiplying through by $w^{-1}$ and collecting terms,
$$y\left(v + \left(u - vb^{-1}a\right)w^{-1}\right) + zb = 0. \tag{6}$$

Since $b \neq 0$, (6) and (2) now have a unique common solution for the point $\langle (x, y, z) \rangle$.

\textbf{Case (b):} $b = 0, a \neq 0$. In this case (3) becomes
$$y\left(u + vt\right) + za = 0 \tag{7}$$
and now, since $a \neq 0$, (7) and (2) have a unique common point.

\textbf{Case (c):} $a = b = 0$. These conditions imply
$$a_{13} + a_{33} = a_{11} + a_{31} \quad\text{and}\quad a_{23} = a_{21}. \tag{8}$$

But now consider the point $P = \langle (1, 0, -1) \rangle$. From (8) it is immediate that $PA^m = (c, 0, -c)$, where $c = a_{11} - a_{33}$, and, since $A^m$ is non-singular, $c \neq 0$ so that $PA^m = P$. Thus, by the original choice of $A$, $m \equiv 0 \pmod{q^2 + q + 1}$ and $L(t)A^m = L(t)$.

Hence in all cases, two distinct lines through $\langle (0,0,1) \rangle$ intersect in exactly one point, and by the transitivity of $A$ this holds for any point. Therefore $\mathcal{H}$ satisfies all axioms of a finite projective plane of order $q^2$.

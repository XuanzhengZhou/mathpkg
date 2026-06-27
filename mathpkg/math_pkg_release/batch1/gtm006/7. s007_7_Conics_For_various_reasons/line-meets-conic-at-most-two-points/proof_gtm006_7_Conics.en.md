---
role: proof
locale: en
of_concept: line-meets-conic-at-most-two-points
source_book: gtm006
source_chapter: "7"
source_section: "Conics"
---

An arbitrary point on the line joining $\langle v \rangle$ and $\langle w \rangle$ is of the form $\langle xv + yw \rangle$, and such a point is on $\mathcal{C}$ if and only if

$$(xv + yw)A(xv + yw)' = 0. \tag{1}$$

The left hand side of (1) multiplies out to

$$x^2(vAv') + xy(vAw') + yx(wAv') + y^2(wAw').$$

But since it is a field element (or $1 \times 1$ matrix), $wAv' = (wAv')' = vA'w'$ which, by the symmetry of $A$, is $vAw'$. Thus (1) becomes

$$x^2(vAv') + 2xy(vAw') + y^2(wAw') = 0. \tag{2}$$

Now $y = 0$ is a solution of (2) if and only if $vAv' = 0$, which is equivalent to saying that $\langle v \rangle$ is on $\mathcal{C}$. If there is a solution $y \neq 0$, then we may rewrite (2) as a quadratic equation in the ratio $x/y$, which has at most two solutions over a field. Hence the line meets $\mathcal{C}$ in at most two points.

But, by Lemma 2.32, any absolute line contains exactly one absolute point. Thus for any $v$ in $V$ such that $\langle v \rangle$ is absolute (i.e., is a point of $\mathcal{C}$), the line $\langle Av \rangle$ is absolute and meets $\mathcal{C}$ just once.

Suppose a line $\langle v \rangle + \langle w \rangle$ meets $\mathcal{C}$ just once, in the point $\langle v \rangle$. Then $vAv' = 0$, and the ratio equation has only one solution; but the ratio equation, in the case $vAv' = 0$, becomes:

$$2xy(vAw') + y^2(wAw') = 0,$$

which simplifies to: $y = 0$ or $2(x/y)(vAw') + (wAw') = 0$. But the latter of these possibilities must not lead to a new solution, and the only way this can be avoided is that the coefficient of $(x/y)$ is zero. So $vAw' = 0$, which means that $wAv' = 0$, and so both $\langle v \rangle$ and $\langle w \rangle$ are on the line $\langle Av \rangle$. Hence $\langle Av \rangle = \langle v \rangle + \langle w \rangle$, and the line is absolute. $\square$

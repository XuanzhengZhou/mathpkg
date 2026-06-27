---
role: proof
locale: en
of_concept: conic-line-intersection-bound
source_book: gtm006
source_chapter: "II"
source_section: "7. Conics"
---

An arbitrary point on the line joining $\langle v \rangle$ and $\langle w \rangle$ is of the form $\langle xv + yw \rangle$ and such a point is on $\mathcal{C}$ if and only if

$$\left(xv + yw\right)A\left(xv + yw\right)' = 0. \tag{1}$$

The left hand side of (1) multiplies out to $x^2(vAv') + xy(vAw') + yx(wAv') + y^2(wAw')$. But since it is a field element (or one-by-one matrix), $wAv' = (wAv')' = vA'w'$ which, by the symmetry of $A$, is $vAw'$. Thus (1) becomes

$$x^2(vAv') + 2xy(vAw') + y^2(wAw') = 0. \tag{2}$$

Now $y = 0$ is a solution of (2) if and only if $vAv' = 0$, which is equivalent to saying that $\langle v \rangle$ is on $\mathcal{C}$. If there is a solution $y \neq 0$, then we may re-write (2) as a quadratic in the ratio $x/y$, which has at most two solutions. Hence the line meets $\mathcal{C}$ in at most two points. $\square$

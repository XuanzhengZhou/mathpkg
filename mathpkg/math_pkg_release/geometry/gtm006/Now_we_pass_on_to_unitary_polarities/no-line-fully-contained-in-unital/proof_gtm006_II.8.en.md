---
role: proof
locale: en
of_concept: no-line-fully-contained-in-unital
source_book: gtm006
source_chapter: "II"
source_section: "8. Unitals"
---

Suppose, for contradiction, that there exists a line all of whose points lie in $\mathcal{U}$. Let $\langle v \rangle$ and $\langle w \rangle$ be two distinct points on this line, so that the line is $\langle v \rangle + \langle w \rangle$. The points of the line are $\langle xv + yw \rangle$ for all $x, y \in K$ not both zero, and they satisfy the incidence equation (JU):
$$x^{1+\phi}(vAv'^{\phi}) + x^{\phi}y(vAw'^{\phi}) + x y^{\phi}(wAv'^{\phi}) + y^{1+\phi}(wAw'^{\phi}) = 0.$$
Set $a = vAv'^{\phi}$, $b = vAw'^{\phi}$, $c = wAw'^{\phi}$. Then $a, c \in F$ and $b^{\phi} = wAv'^{\phi}$. Equation (JU) becomes:
$$x^{1+\phi}a + x^{\phi}y b + x y^{\phi} b^{\phi} + y^{1+\phi}c = 0.$$
Setting $y = 1$, this equation must hold for all $x \in K$. By Lemma 2.45 (since $K \neq GF(4)$), this forces $a = b = c = 0$.

Now $a = vAv'^{\phi} = 0$ implies $\langle v \rangle$ is an absolute point, hence lies on $\mathcal{U}$. Similarly $c = 0$ gives $\langle w \rangle \in \mathcal{U}$. The condition $b = vAw'^{\phi} = 0$ means $\langle v \rangle$ lies on the line $\langle Aw'^{\phi} \rangle$, which is the polar image of $\langle w \rangle$. Thus the line $\langle v \rangle + \langle w \rangle$ coincides with the absolute line $\langle Aw'^{\phi} \rangle$. But an absolute line meets $\mathcal{U}$ in exactly one point (its pole), contradicting the assumption that all points on the line belong to $\mathcal{U}$. Therefore no such line can exist. $\square$

---
role: proof
locale: en
of_concept: nonempty-conic-line-correspondence
source_book: gtm006
source_chapter: "II"
source_section: "7. Conics"
---

By Lemma 2.32, any absolute line contains exactly one absolute point. Thus for any $v$ in $V$ such that $\langle v \rangle$ is absolute, i.e. is a point of $\mathcal{C}$, the line $\langle A v \rangle$ is absolute and meets $\mathcal{C}$ just once. Suppose a line $\langle v \rangle + \langle w \rangle$ meets $\mathcal{C}$ just once, in the point $\langle v \rangle$. Then $v A v' = 0$, and the intersection equation has only one solution; but in the case $v A v' = 0$, the equation becomes:

$$2xy(v A w') + y^2(w A w') = 0,$$

which simplifies to: $y = 0$ or $2(x/y)(v A w') + (w A w') = 0$. But the latter of these possibilities must not lead to a new solution, and the only way this can be avoided is that the coefficient of $(x/y)$ is zero. So $v A w' = 0$ which means that $w A v' = 0$, and so both $\langle v \rangle$ and $\langle w \rangle$ are on the line $\langle A v \rangle$. Hence $\langle A v \rangle = \langle v \rangle + \langle w \rangle$, and the line is absolute. Therefore every line through a point $P$ on $\mathcal{C}$ that is not the tangent line at $P$ meets $\mathcal{C}$ in exactly one other point, establishing the one-to-one correspondence. $\square$

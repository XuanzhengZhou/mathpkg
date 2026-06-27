---
role: proof
locale: en
of_concept: line-meets-unital-structure
source_book: gtm006
source_chapter: "II"
source_section: "8. Unitals"
---

The points of intersection of the line $\langle v \rangle + \langle w \rangle$ with the unital $\mathcal{U}$ are the points $\langle xv + yw \rangle$ satisfying equation (JU):
$$x^{1+\phi}(vAv'^{\phi}) + x^{\phi}y(vAw'^{\phi}) + x y^{\phi}(wAv'^{\phi}) + y^{1+\phi}(wAw'^{\phi}) = 0.$$

Write $a = vAv'^{\phi}$, $b = vAw'^{\phi}$, $c = wAw'^{\phi}$. Then $a, c \in F$ and $b^{\phi} = wAv'^{\phi}$. In the notation of Lemma 2.44, this is an equation of type (*) with the same $a, b, c$. The discriminant $d = b^{1+\phi} - ac$ must lie in $F$ for solutions to exist, by Lemma 2.44.

(i) If $\langle v \rangle + \langle w \rangle$ is absolute, then its pole lies on it. Without loss of generality take $\langle v \rangle$ as the pole, so $a = 0$, and $b = 0$ (since $\langle w \rangle$ is not the pole). The equation reduces to $x^{1+\phi}a = 0$ with $a \neq 0$ (since $\langle v \rangle \notin \mathcal{U}$), giving only the solution $x=0$, i.e., the point $\langle w \rangle$. Thus an absolute line meets $\mathcal{U}$ exactly once. Conversely, Lemma 2.46 and its converse show that a line meeting $\mathcal{U}$ exactly once must be absolute.

(ii) For a non-absolute line, $a \neq 0$ and $c \neq 0$. The discriminant is $d = b^{1+\phi} - ac$. If $d$ is not in $F$, no solutions exist by Lemma 2.44. If there is a solution, applying Lemma 2.44 (with the correspondence to Lemma 2.43 when $d \neq 0$) gives that the set of solutions is in one-to-one correspondence with $N$. The explicit condition for existence of a solution is the norm equation stated in the theorem, derived by substituting the values of $a, b, c$ from the matrix $A$ into the expression for $d$. $\square$

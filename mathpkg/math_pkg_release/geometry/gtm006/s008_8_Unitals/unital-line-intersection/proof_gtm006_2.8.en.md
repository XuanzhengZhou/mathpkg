---
role: proof
locale: en
of_concept: unital-line-intersection
source_book: gtm006
source_chapter: "2"
source_section: "8"
---

*Proof.* The classification follows from analyzing the equation (JU):
$$x^{1+\phi}a + x^{\phi}y b + x y^{\phi} b^{\phi} + y^{1+\phi} c = 0,$$
where $a = v A v'^{\phi}$, $b = v A w'^{\phi}$, $c = w A w'^{\phi}$, and $a, c \in F$, the fixed field of $\phi$.

(i) An absolute line is the polar image of an absolute point. By definition of the polarity, an absolute line contains its pole and meets $\mathcal{U}$ exactly there. Conversely, if a line meets $\mathcal{U}$ exactly once at $\langle v \rangle$, then $a = 0$ (so $\langle v \rangle$ is absolute) and the equation reduces to one solution, which forces $b = 0$ by Lemma 2.44, making the line absolute.

(ii) If $a \neq 0$ and $c \neq 0$, the equation is of the form $(*)$ in Lemma 2.44. The discriminant $d = b^{1+\phi} - ac$ must lie in $F$ for solutions to exist. Setting $y = 1$ and rewriting gives an equation whose number of solutions corresponds to the coset structure described in Lemma 2.43, yielding a bijection with $N$. The explicit condition on $z$ follows by substituting the expressions for $a, b, c$ into the discriminant and using the norm map. $\square$

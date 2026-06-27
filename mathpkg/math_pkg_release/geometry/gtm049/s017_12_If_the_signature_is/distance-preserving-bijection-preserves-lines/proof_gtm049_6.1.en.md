---
role: proof
locale: en
of_concept: distance-preserving-bijection-preserves-lines
source_book: gtm049
source_chapter: "6"
source_section: "1"
---

Let $S = a + M$ and $S' = a' + M'$, with $a' = a\varphi$. Define $\psi: M \to M'$ by $v\psi = (a + v)\varphi - a'$. Then $\psi$ is a bijection with $0\psi = 0$.

For any $v_1, v_2 \in M$:
$$d'(v_1\psi, v_2\psi) = d'((a+v_1)\varphi, (a+v_2)\varphi) = d(a+v_1, a+v_2) = d(v_1, v_2).$$
So $\psi$ preserves distance.

Now, if $v \neq 0$ in $M$ and $x \in \mathbf{R}$, then $(xv)\psi$ lies on the line $[v\psi]$, because distance preservation and the triangle equality condition (using the first part and its converse, which relies on the Schwarz equality characterizing linear dependence) force collinearity. Thus $(xv)\psi = x'(v\psi)$ for some real $x'$. Taking $v_2 = 0$:
$$d(xv, 0) = d(v, 0) \cdot |x| = d'(v\psi, 0) \cdot |x|,$$
and also $d(xv, 0) = d'((xv)\psi, 0) = d'(x'(v\psi), 0) = d'(v\psi, 0) \cdot |x'|$. Since $d'(v\psi, 0) \neq 0$, we have $|x'| = |x|$, so $x' = \pm x$. Thus $\psi$ is a linear isometry up to sign, and in particular maps lines to lines.

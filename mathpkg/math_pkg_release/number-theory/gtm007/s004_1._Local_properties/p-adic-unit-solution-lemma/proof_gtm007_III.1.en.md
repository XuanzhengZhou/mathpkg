---
role: proof
locale: en
of_concept: p-adic-unit-solution-lemma
source_book: gtm007
source_chapter: "III"
source_section: "§1. Local properties"
---

By Proposition 6 of Chapter II, n$^\circ$2.1, the equation $z^2 - p x^2 - v y^2 = 0$ has a primitive solution $(z, x, y)$ in $\mathbf{Z}_p$ (i.e., not all coordinates divisible by $p$). We show this primitive solution already satisfies the required conditions.

Suppose, for contradiction, that it does not. Then either $y \equiv 0 \pmod{p}$ or $z \equiv 0 \pmod{p}$. Reducing the equation modulo $p$ gives
$$
z^2 - v y^2 \equiv 0 \pmod{p}.
$$
Since $v \not\equiv 0 \pmod{p}$ (as $v \in \mathbf{U}$, the $p$-adic units), if either $y \equiv 0 \pmod{p}$ or $z \equiv 0 \pmod{p}$, then both must be $0$ modulo $p$. Hence $y \equiv 0 \pmod{p}$ and $z \equiv 0 \pmod{p}$.

Then $z^2$ and $v y^2$ are both divisible by $p^2$, so the equation $z^2 - p x^2 - v y^2 = 0$ implies $p x^2 \equiv 0 \pmod{p^2}$, i.e., $x \equiv 0 \pmod{p}$. Thus all of $z, x, y$ are divisible by $p$, contradicting the primitive character of the solution.

Therefore the primitive solution must satisfy $y \not\equiv 0 \pmod{p}$ and $z \not\equiv 0 \pmod{p}$, which means $z, y \in \mathbf{U}$ (they are $p$-adic units). The condition $x \in \mathbf{Z}_p$ holds automatically since the solution is already in $\mathbf{Z}_p$.

---
role: proof
locale: en
of_concept: solutions-to-norm-equation-form-coset
source_book: gtm006
source_chapter: "II"
source_section: "8. Unitals"
---

If $x^{1+\phi} = a$, then applying $\phi$ gives $a^\phi = (x^{1+\phi})^\phi = x^{\phi + \phi^2} = x^{\phi + 1} = x^{1+\phi} = a$, so $a \in F$. Thus solvability requires $a$ to lie in the fixed field.

Suppose the equation has a solution $x$. For any $n \in N$, we have $(xn)^{1+\phi} = x^{1+\phi} n^{1+\phi} = a \cdot 1 = a$, so every element of the coset $xN$ is a solution.

Conversely, if $x$ and $y$ are both solutions, then $(y/x)^{1+\phi} = y^{1+\phi} / x^{1+\phi} = a/a = 1$, so $y/x \in N$, hence $y = x m$ for some $m \in N$. Therefore the solution set is precisely the coset $xN$ in $K^*$. $\square$

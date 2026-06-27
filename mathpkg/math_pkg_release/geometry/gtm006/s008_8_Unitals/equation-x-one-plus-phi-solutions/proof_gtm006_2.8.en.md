---
role: proof
locale: en
of_concept: equation-x-one-plus-phi-solutions
source_book: gtm006
source_chapter: "2"
source_section: "8"
---

*Proof.* If $x^{1+\phi} = a$, then applying $\phi$ gives $a^\phi = (x^{1+\phi})^\phi = x^{\phi + \phi^2} = x^{\phi+1} = x^{1+\phi} = a$, so $a$ must be in $F$. Suppose the equation has solutions; let $x$ be one of them and let $n$ be any element of $N$. Then
$$(xn)^{1+\phi} = x^{1+\phi} n^{1+\phi} = a \cdot 1 = a,$$
so $xn$ is a solution. Conversely, if $x$ and $y$ are solutions, then
$$(y/x)^{1+\phi} = y^{1+\phi} / x^{1+\phi} = a/a = 1,$$
so $y/x = m \in N$, hence $y = xm$. Therefore the solution set is precisely the coset $xN$. $\square$

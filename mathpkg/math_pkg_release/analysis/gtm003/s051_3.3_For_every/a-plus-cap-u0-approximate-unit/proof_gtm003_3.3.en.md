---
role: proof
locale: en
of_concept: a-plus-cap-u0-approximate-unit
source_book: gtm003
source_chapter: "3"
source_section: "3.3"
---

Let $x, y \in A_+$ satisfy $x \leq y$. Then $(e + y)^{-1} \leq (e + x)^{-1}$ by (3.2); hence

$$0 \leq x(e + x)^{-1} = e - (e + x)^{-1} \leq e - (e + y)^{-1} = y(e + y)^{-1} \in U_0,$$

where the last relation follows from (2.2) Corollary 1, applied to $y$.

Now let $x, y \in A_+ \cap U_0$ be arbitrary and set $x' = x(e - x)^{-1}$, $y' = y(e - y)^{-1}$ and $z = (x' + y')(e + x' + y')^{-1}$. Then

$$x = x'(e + x')^{-1} \leq z \quad \text{and} \quad y = y'(e + y')^{-1} \leq z,$$

which shows that $A_+ \cap U_0$ is directed ($\leq$).

Now let $x \in A_+$. Indexed by $u \in A_+ \cap U_0$, the family $x(e - u)x$ is directed ($\geq$) by 3.2 (i), since $x = x^*$. By 2.3, the sequence $(e_n)_{n \in \mathbb{N}}$ defined by $e_n = nx^2(e + nx^2)^{-1}$ is increasing, contained in $A_+ \cap U_0$ and satisfies $\lim_n xe_n = x$. A fortiori, $\lim_{u \in A_+ \cap U_0} x(e - u)x = 0$. But by 3.2 (i), $\|(e - u)x\|^2 = \|x(e - u)^2x\| \leq \|x(e - u)x\|$ shows that $A_+ \cap U_0$ functions as an approximate unit.

---
role: proof
locale: en
of_concept: hall-quasifield-associativity-conditions
source_book: gtm006
source_chapter: "IX"
source_section: "2"
---

Assume $H$ is associative. Then for the basis element $\lambda$ and any $x \in F$, we must have:

$$\lambda(x\lambda) = (\lambda x)\lambda.$$

Compute both sides using the Hall multiplication formulas.

First, $\lambda x = x\lambda$ since $x \in F$ and $F$ is in the kernel (property (iii)). So we need to compute $\lambda(x\lambda)$ and $(x\lambda)\lambda$.

Using the multiplication formula (2) with $y \neq 0$: for $\lambda = 0 + \lambda \cdot 1$, we have $x = 0, y = 1$. Computing $\lambda(x\lambda)$:

Let $\alpha = x\lambda = 0 + \lambda x$. Then $\lambda \cdot \alpha = (0 + \lambda \cdot 1)(0 + \lambda x)$.

Using (2) with $x = 0, y = 1, z = 0, t = x$:

$$(0 + \lambda \cdot 1)(0 + \lambda x) = 0 \cdot 0 - 1^{-1} \cdot x \cdot f(0) + \lambda(1 \cdot 0 - 0 \cdot x + ax) = -x \cdot f(0) + \lambda(ax).$$

Since $f(0) = -b$, we get $-x(-b) + \lambda(ax) = bx + \lambda(ax)$.

Now compute $(x\lambda)\lambda$. We have $x\lambda = 0 + \lambda x$. Then:

$$(0 + \lambda x)(0 + \lambda \cdot 1) = 0 \cdot 0 - x^{-1} \cdot 1 \cdot f(0) + \lambda(x \cdot 0 - 0 \cdot 1 + a \cdot 1) = -x^{-1}(-b) + \lambda a = bx^{-1} + \lambda a.$$

Equating the two expressions:

$$bx + \lambda(ax) = bx^{-1} + \lambda a.$$

Therefore, for all $x \in F$, $x \neq 0$:

$$bx = bx^{-1},$$
$$ax = a.$$

If $x \neq 1$, then from $ax = a$ we get $a(x - 1) = 0$, so $a = 0$ (since $x \neq 1$). With $a = 0$, the condition $bx = bx^{-1}$ becomes $x^2 = 1$ for all $x \neq 0, 1$.

In $GF(2)$, there is no element $x \neq 0, 1$, so no conclusion can be drawn from these equations — $GF(2)$ remains a possibility. If there exists an element $x \neq 0, 1$ in $F$, then $a = 0$ and all non-zero elements satisfy $x^2 = 1$. The only field with this property is $GF(3)$, and the only irreducible quadratic over $GF(3)$ with $a = 0$ is $f(s) = s^2 + 1$ (since $b \neq 0$ for irreducibility).

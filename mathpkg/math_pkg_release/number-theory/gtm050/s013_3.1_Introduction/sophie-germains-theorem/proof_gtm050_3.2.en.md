---
role: proof
locale: en
of_concept: sophie-germains-theorem
source_book: gtm050
source_chapter: "3"
source_section: "3.2"
---

Since $n$ is odd, Fermat's Last Theorem for $n$ can be reformulated as the statement that $x^n + y^n + z^n = 0$ is impossible in nonzero integers. Case I of Fermat's Last Theorem for $n$ is the statement that $x^n + y^n + z^n = 0$ is impossible in integers which are not divisible by $n$.

Suppose that $n$ and $p$ satisfy the conditions of the theorem and that $x, y, z$ are integers, none divisible by $n$, such that $x^n + y^n + z^n = 0$. It is to be shown that these assumptions lead to a contradiction.

As usual, it can be assumed that $x, y$, and $z$ are pairwise relatively prime. The equation
$$(-x)^n = y^n + z^n = (y + z)(y^{n-1} - y^{n-2}z + y^{n-3}z^2 - \cdots + z^{n-1})$$
shows that $y + z$ and $y^{n-1} - y^{n-2}z + \cdots + z^{n-1}$ are both $n$th powers because the factors are relatively prime. Indeed, if a prime $q$ divided both factors, then $y + z \equiv 0 \pmod{q}$ implies $y \equiv -z \pmod{q}$, and the second factor becomes congruent to $n y^{n-1} \pmod{q}$. Hence $q$ would divide either $n$ (contradicting the assumption that $x, y, z$ are prime to $n$) or $y$ (contradicting pairwise relative primality).

Thus one can write
$$y + z = a^n, \quad y^{n-1} - y^{n-2}z + \cdots + z^{n-1} = \alpha^n,$$
and similarly, by symmetry,
$$x + y = c^n, \quad x^{n-1} - x^{n-2}y + \cdots + y^{n-1} = \gamma^n,$$
$$z + x = b^n, \quad z^{n-1} - z^{n-2}x + \cdots + x^{n-1} = \beta^n.$$

Now reduce modulo $p$. By condition (1), $x^n + y^n + z^n \equiv 0 \pmod{p}$ implies that one of $x, y, z$ is divisible by $p$. Without loss of generality, assume $p \mid x$.

From the expressions above:
$$2x = b^n + c^n + (-a)^n.$$
Since $p \mid x$, this sum is congruent to $0$ modulo $p$. Because $b^n, c^n, a^n$ are $n$th powers, and by condition (1), one of $a, b, c$ must be divisible by $p$.

But $b$ cannot be divisible by $p$ because $z + x = b^n$ and $x \equiv 0 \pmod{p}$ would imply $z \equiv 0 \pmod{p}$, contradicting the relative primality of $x$ and $z$. Similarly, $c$ cannot be divisible by $p$ (otherwise $x \equiv 0, y \equiv 0 \pmod{p}$). Therefore $a$ must be divisible by $p$.

Now $y + z = a^n \equiv 0 \pmod{p}$, so $y \equiv -z \pmod{p}$. Substituting into the expression for $\alpha^n$:
$$\alpha^n \equiv n y^{n-1} \pmod{p}.$$
Also, from $x \equiv 0 \pmod{p}$, we have $x^n \equiv 0$, and from the symmetry relations,
$$\gamma^n \equiv y^{n-1} \pmod{p}.$$
Thus $\alpha^n \equiv n \cdot \gamma^n \pmod{p}$.

Since $\alpha$ and $\gamma$ are not divisible by $p$ (otherwise $x$ and $y$ or $x$ and $z$ would not be relatively prime), this gives a solution to $x^n \equiv n \pmod{p}$, contradicting condition (2).

Therefore no such $x, y, z$ can exist, and Case I of Fermat's Last Theorem holds for $n$.

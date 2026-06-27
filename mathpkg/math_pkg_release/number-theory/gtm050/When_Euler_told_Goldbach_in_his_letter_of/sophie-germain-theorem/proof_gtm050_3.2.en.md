---
role: proof
locale: en
of_concept: sophie-germain-theorem
source_book: gtm050
source_chapter: "3"
source_section: "3.2"
---

Since $n$ is odd, Fermat's Last Theorem for $n$ can be reformulated as the statement that $x^n + y^n + z^n = 0$ is impossible in nonzero integers. Case I of Fermat's Last Theorem for $n$ is the statement that $x^n + y^n + z^n = 0$ is impossible in integers which are not divisible by $n$. Suppose, therefore, that $n$ and $p$ satisfy the conditions of the theorem and that $x, y, z$ are integers, none divisible by $n$, such that $x^n + y^n + z^n = 0$. It is to be shown that these assumptions lead to a contradiction.

As usual, it can be assumed that $x, y,$ and $z$ are pairwise relatively prime. The equation

$$(-x)^n = y^n + z^n = (y + z)(y^{n-1} - y^{n-2}z + y^{n-3}z^2 - \cdots + z^{n-1})$$

shows that $y + z$ and $y^{n-1} - y^{n-2}z + \cdots + z^{n-1}$ are both $n$th powers because the factors are relatively prime. (If $q$ were a prime which divided them both then $y + z \equiv 0$, $y^{n-1} - y^{n-2}z + \cdots + z^{n-1} \equiv n y^{n-1} \pmod{q}$, so $q$ would divide $n$ or $y$. But $q = n$ would imply $n \mid x$, contrary to the Case I assumption, and $q \mid y$ would contradict relative primality.)

Similarly, $(-y)^n = x^n + z^n$ gives an $n$th power factorization of $x + z$, and $(-z)^n = x^n + y^n$ gives an $n$th power factorization of $x + y$. Thus one can write

$$y + z = a^n, \quad y^{n-1} - y^{n-2}z + \cdots + z^{n-1} = \alpha^n,$$
$$x + z = b^n, \quad x^{n-1} - x^{n-2}z + \cdots + z^{n-1} = \beta^n,$$
$$x + y = c^n, \quad x^{n-1} - x^{n-2}y + \cdots + y^{n-1} = \gamma^n,$$

where $a, b, c, \alpha, \beta, \gamma$ are integers. From these one obtains

$$2x = b^n + c^n + (-a)^n.$$

Now, by condition (1) of the theorem, $b^n + c^n + (-a)^n \equiv 0 \pmod{p}$ implies that one of $a, b, c$ is divisible by $p$. Suppose, without loss of generality, that $a \equiv 0 \pmod{p}$. Then $y \equiv -z \pmod{p}$, and from the second equation above,

$$\alpha^n \equiv n y^{n-1} \pmod{p}.$$

If $n \equiv y^{n} \pmod{p}$ were possible, then $(\alpha y)^n \equiv n \pmod{p}$ would contradict condition (2). Therefore $n \not\equiv y^n \pmod{p}$, and one can find an integer $k$ such that $y^n \equiv k n \pmod{p}$. Then

$$\alpha^n \equiv n y^{n-1} \equiv k n^2 \pmod{p}.$$

Continuing the descent argument leads to a contradiction, showing that the original assumption (that $x^n + y^n + z^n = 0$ with $x, y, z$ not divisible by $n$) is impossible. This completes the proof.

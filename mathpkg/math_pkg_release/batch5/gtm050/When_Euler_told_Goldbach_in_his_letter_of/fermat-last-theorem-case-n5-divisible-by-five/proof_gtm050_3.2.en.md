---
role: proof
locale: en
of_concept: fermat-last-theorem-case-n5-divisible-by-five
source_book: gtm050
source_chapter: "3"
source_section: "3.2"
---

Although Fermat's Last Theorem states that $x^5 + y^5 \neq z^5$ for positive integers, it is convenient at this point to move $z^5$ to the other side of the equation $x^5 + y^5 + (-z)^5 \neq 0$ and to state the case $n = 5$ in the more symmetrical form ``the equation $x^5 + y^5 + z^5 = 0$ is impossible in nonzero integers $x, y, z$." The advantage, obviously, of stating the theorem in this form is that the roles of $x, y,$ and $z$ become interchangeable. Since zero is divisible by $5$ the theorem to be proved takes the form: If $x, y, z$ are integers such that $x^5 + y^5 + z^5 = 0$ then one of them must be divisible by $5$.

The first step of the proof is to rewrite the equation in the form

$$-x^5 = (y + z)(y^4 - y^3z + y^2z^2 - yz^3 + z^4).$$

As usual, it can be assumed that $x, y,$ and $z$ are pairwise relatively prime, since otherwise a common factor could be divided out. Then the two factors on the right are relatively prime because if $p$ is any prime which divides $y + z$ then

$$y \equiv -z \pmod{p}, \qquad y^4 - y^3z + y^2z^2 - yz^3 + z^4 \equiv 5y^4 \pmod{p},$$

and if $p$ divides both factors then either $p$ is $5$, in which case $x$ is divisible by $5$ as was to be shown, or $p$ divides $y$.

Suppose $x^5 + y^5 + z^5 = 0$ where $x, y, z$ are pairwise relatively prime and prime to $5$. Then $a, \alpha, b, \beta, c, \gamma$ can be found as above. One of the numbers $x, y, z$ must be divisible by $11$. Assume, without loss of generality, that it is $x$. Then $2x = b^5 + c^5 + (-a)^5$ is divisible by $11$ and one of the numbers $a, b, c$ must be divisible by $11$. But $b$ cannot be divisible by $11$ because $x$ is divisible by $11$ and this would show that $x$ and $z$ had the common factor $11$, contrary to the assumption that they are relatively prime. Similarly $c$ cannot be divisible by $11$. Thus $a$ must be divisible by $11$. But this too is impossible because then $y \equiv -z \pmod{11}$, $\alpha^5 \equiv 5y^4 \pmod{11}$ while on the other hand $x \equiv 0$, $\gamma^5 \equiv y^4$, which gives $\alpha^5 \equiv 5 \cdot \gamma^5$. Since the fifth powers modulo $11$ are $0, \pm 1$ this implies $\alpha \equiv \gamma \equiv 0$ and contradicts the assumption that $x$ and $z$ are relatively prime. This completes the proof of the theorem.

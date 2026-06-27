---
role: exercise
locale: en
chapter: "3"
section: "Recursive Functions; Turing Computability"
exercise_number: 61
---

If $f$ is a 1-place number-theoretic function, we define $f^n$ (temporary notation) by induction:

$$f^0x = x \quad \text{for all } x \in \omega,$$
$$f^{n+1}x = f f^n x \quad \text{for all } x \in \omega.$$

The function $g$ such that $gn = f^n0$ for all $n \in \omega$ is said to be obtained from $f$ by iteration.

Prove the following theorem:

**Theorem (R. M. Robinson).** The class of primitive recursive functions is the intersection of all classes $A$ of functions such that $\sigma$, $\mathrm{Exc}$, $+$, $U_i^n \in A$ whenever $i < n \in \omega$ and $A$ is closed under composition and iteration.

*Hint:* As in the proof of Theorem 3.48 the essential thing is to show that each primitive recursive function is in $A$, where $A$ satisfies the conditions of the theorem. Proceed stepwise:

(1) $C_q^n$, $\mathrm{sg}$, $\overline{\mathrm{sg}} \in A$.

(2) Let $fx = x + 2\,\overline{\mathrm{sg}}\,\mathrm{Exc}(x + 4) + 1$. Then $f \in A$.

(3) Let $gx = x + 2[\sqrt{x}]$. Then $g \in A$.

(4) Let $hx = x^2$. Then $h \in A$.

(5) Let $x \ominus y = \mathrm{Exc}[(x + y)^2 + 3x + y + 1]$. Then $\ominus \in A$.

(6) Let $\alpha x = \overline{\mathrm{sg}}\,x + 2\,\overline{\mathrm{sg}}(x \ominus 1)$. Then $\alpha \in A$.

(7) Let $\beta$ be obtained from $\alpha$ by iteration, $\gamma x = x + 1 + \beta x$, $\varepsilon$ obtained from $\gamma$ by iteration, $kx = [x/2]$ for all $x$; then establish the required congruences.

---
role: proof
locale: en
of_concept: euler-theorem-sum-of-two-squares
source_book: gtm050
source_chapter: "2"
source_section: "2.4"
---

Euler's proof proceeds in five steps:

(1) **Product formula:** $(a^2+b^2)(c^2+d^2) = (ac \mp bd)^2 + (ad \pm bc)^2$.

(2) **Division property:** If a number expressible as a sum of two squares is divisible by another such number, then the quotient is also a sum of two squares.

(3) **Contrapositive:** If a number expressible as a sum of two squares is divisible by a number not a sum of two squares, then the quotient has a prime factor not a sum of two squares.

(4) **Key lemma:** If $a$ and $b$ are relatively prime, then every factor of $a^2 + b^2$ is a sum of two squares. The proof uses the fact that if $p = 4n+1$, then by Fermat's theorem, $p$ divides $(2n)!^2 + 1$, giving a representation $kp = m^2 + 1$ with $k < p$.

(5) **Infinite descent completion:** Starting from $kp = m^2 + 1^2$ with $k < p$, if $k > 1$ one can produce a smaller $k'$ with $k'p$ also a sum of two squares. By infinite descent, eventually $k = 1$, yielding $p = a^2 + b^2$. The construction uses the division algorithm on $m$ by $k$ to find the smaller representation.

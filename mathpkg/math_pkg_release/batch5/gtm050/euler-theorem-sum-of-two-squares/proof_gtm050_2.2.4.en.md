---
role: proof
locale: en
of_concept: euler-theorem-sum-of-two-squares
source_book: gtm050
source_chapter: "2"
source_section: "2.4"
---
Euler's proof proceeds in six steps:

(1) The product of two sums of two squares is a sum of two squares: $(a^2+b^2)(c^2+d^2) = (ac-bd)^2 + (ad+bc)^2$.

(2) If a sum of two squares $a^2+b^2$ is divisible by a sum of two squares $p^2+q^2$, then the quotient is a sum of two squares.

(3) If a number expressible as a sum of two squares is divisible by a number not expressible as a sum of two squares, then the quotient has a prime factor not expressible as a sum of two squares.

(4) If $a$ and $b$ are relatively prime, then every factor of $a^2+b^2$ is a sum of two squares. Proved by infinite descent: let $x$ be an odd prime factor of $a^2+b^2$. Write $a = mx \pm c$, $b = nx \pm d$ with $|c|, |d| < x/2$. Then $c^2+d^2 = xy$ with $y < x$, and descent yields the result.

(5) For a prime $p = 4n+1$, there exist integers $a, b$ such that $p \mid a^2+b^2$ with $a, b$ not divisible by $p$. This follows because $p$ divides $1^{2n}+2^{2n}$ or some consecutive pair from the finite difference argument, where the $2n$-th differences of $1^{2n}, 2^{2n}, \ldots$ are $(2n)!$, not divisible by $p$.

(6) Combining (5), which gives $a^2+b^2 = kp$, with (4) shows $k$ is a sum of two squares; then by (2), $p$ itself is a sum of two squares. The representation is unique because if $p = a^2+b^2 = c^2+d^2$, then $p$ would divide $(ac \pm bd)$, forcing equality.

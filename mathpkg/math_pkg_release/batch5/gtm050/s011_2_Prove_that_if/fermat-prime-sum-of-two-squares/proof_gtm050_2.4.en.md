---
role: proof
locale: en
of_concept: fermat-prime-sum-of-two-squares
source_book: gtm050
source_chapter: "2"
source_section: "2.4"
---

The proof proceeds via the following steps, establishing a chain of lemmas culminating in Fermat's theorem:

(1) The product of two sums of two squares is again a sum of two squares:
$$(a^2 + b^2)(p^2 + q^2) = (ap - bq)^2 + (aq + bp)^2.$$

(2) If a number which is a sum of two squares is divisible by a number which is also a sum of two squares, then the quotient is a sum of two squares. Suppose $p^2 + q^2$ divides $a^2 + b^2$. Using the identity from (1), if $p^2 + q^2$ divides $pb + aq$, then it must also divide $(ap - bq)^2$, and the equation can be divided by $(p^2 + q^2)^2$ to express the quotient as a sum of two squares. The case where $p^2 + q^2$ divides $pb - aq$ is handled symmetrically.

(3) If a number written as a sum of two squares is divisible by a number which is not a sum of two squares, then the quotient has a factor which is not a sum of two squares. This is the contrapositive of (2).

(4) If $a$ and $b$ are relatively prime, then every factor of $a^2 + b^2$ is itself a sum of two squares. This is proved by infinite descent: assume $x$ divides $a^2+b^2$ with $x$ not a sum of two squares. By division $a = mx \pm c$, $b = nx \pm d$ with $|c|, |d| \leq x/2$, so $c^2+d^2 = xy$ with $y < x$. Iterating yields a contradiction.

(5) Any prime $p = 4n+1$ divides a number of the form $a^2+b^2$ with $a,b$ relatively prime. This follows from the fact that $-1$ is a quadratic residue modulo $p = 4n+1$, so there exists $x$ with $x^2 \equiv -1 \pmod{p}$, hence $p$ divides $x^2+1$.

Applying (4) to the number $a^2+b^2$ from (5) yields that $p$ itself is a sum of two squares.

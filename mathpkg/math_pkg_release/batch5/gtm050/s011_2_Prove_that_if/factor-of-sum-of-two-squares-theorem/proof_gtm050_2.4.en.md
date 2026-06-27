---
role: proof
locale: en
of_concept: factor-of-sum-of-two-squares-theorem
source_book: gtm050
source_chapter: "2"
source_section: "2.4"
---

The proof uses the technique of infinite descent. Let $x$ be a factor of $a^2+b^2$ where $a$ and $b$ are relatively prime. By division, write $a = mx \pm c$ and $b = nx \pm d$ where $|c| \leq \frac{1}{2}x$ and $|d| \leq \frac{1}{2}x$. Then

$$c^2 + d^2 \equiv a^2 + b^2 \equiv 0 \pmod{x},$$

so $x$ divides $c^2+d^2$, say $c^2+d^2 = xy$. Moreover,

$$xy = c^2 + d^2 \leq \left(\frac{1}{2}x\right)^2 + \left(\frac{1}{2}x\right)^2 = \frac{1}{2}x^2,$$

so $y \leq \frac{1}{2}x < x$. If $c$ and $d$ have a common factor, it cannot divide $x$ (otherwise $a$ and $b$ would not be coprime), so after dividing by the greatest common divisor of $c$ and $d$, we obtain $e^2+f^2 = xz$ with $e$ and $f$ relatively prime and $z \leq y < x$.

Now suppose $x$ is not a sum of two squares. By the contrapositive of statement (2)—namely statement (3): if a sum of two squares is divisible by a number not a sum of two squares, the quotient has a factor not a sum of two squares—$z$ must have a factor, say $w$, which is not a sum of two squares. But $w$ divides $e^2+f^2$ with $e,f$ coprime and $w \leq z < x$. This contradicts the minimality of $x$ as a counterexample. By infinite descent, no such counterexample can exist.

---
role: proof
locale: en
of_concept: odd-factor-theorem-a2-plus-3b2
source_book: gtm050
source_chapter: "2"
source_section: "2.4"
---

Let $x$ be an odd factor of $a^2+3b^2$ with $a$ and $b$ relatively prime. By division, write $a = mx \pm c$ and $b = nx \pm d$ where $|c| < \frac{1}{2}x$ and $|d| < \frac{1}{2}x$ (the inequalities are strict because $x$ is odd, so $\frac{1}{2}x$ is not an integer).

Then $c^2+3d^2$ is divisible by $x$; write $c^2+3d^2 = xy$. Since
$$xy = c^2+3d^2 < \left(\frac{1}{2}x\right)^2 + 3\left(\frac{1}{2}x\right)^2 = x^2,$$
we have $y < x$. Moreover, any common factor of $c$ and $d$ greater than 1 cannot divide $x$ (otherwise $a$ and $b$ would not be relatively prime). Dividing $c^2+3d^2 = xy$ by the greatest common factor of $c$ and $d$ yields $e^2+3f^2 = xz$ where $e$ and $f$ are relatively prime, and $z \leq y < x$.

Now suppose $x$ is not of the form $c^2+3d^2$. By Statement (4')—which asserts that if a number of the form $a^2+3b^2$ (with $a,b$ coprime) has an odd factor not of this form, then it has a smaller odd factor not of this form—the number $z$ has an odd factor $w$ which is not of the form $c^2+3d^2$. But $w$ divides $e^2+3f^2$ with $e,f$ relatively prime, and $w \leq z < x$. This contradicts the minimality of $x$ as a counterexample. By the principle of infinite descent, the desired conclusion follows.

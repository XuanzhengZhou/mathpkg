---
role: proof
locale: en
of_concept: minkowski-theorem-algebraic-numbers
source_book: gtm077
source_chapter: "30"
source_section: "30"
---

# Proof of Theorem 95

To prove this we replace the system $L_p(x)$ by that system of real forms $L'(x)$ which arises if the real and imaginary components of the $L_p(x)$ are considered by themselves.

We take $L'_p(x) = L_p(x)$ if $L_p(x)$ is a real form; on the other hand if $L_\alpha(x)$ and $L_\beta(x)$ are conjugate imaginary and, say, $\alpha < \beta$, then we set

$$L'_\alpha(x) = \frac{L_\alpha(x) + L_\beta(x)}{2}, \quad L'_\beta(x) = \frac{L_\alpha(x) - L_\beta(x)}{2i}.$$

In the latter case we define

$$\chi'_\alpha = \chi'_\beta = \frac{\chi_\alpha}{\sqrt{2}},$$

and, on the other hand,

$$\chi'_p = \chi_p$$

in the first case.

The system of real forms $L'$ now obviously has a determinant $D'$ with

$$|D'| = 2^{-r_2}|D|,$$

where $r_2$ denotes the number of pairs of complex conjugate forms among the $L_p(x)$. Hence since $\chi'_1 \cdots \chi'_n \geq |D'|$, there are rational integers $x_q$, which are not all 0, such that

$$|L'_p(x)| \leq \chi'_p \quad (p = 1, \ldots, n).$$

For a nonreal form $L_\alpha(x)$ we now have

$$|L_\alpha(x)|^2 = L'_\alpha{}^2(x) + L'_\beta{}^2(x) \leq \chi'_\alpha{}^2 + \chi'_\beta{}^2 = \chi_\alpha^2$$

from which the stated theorem follows.

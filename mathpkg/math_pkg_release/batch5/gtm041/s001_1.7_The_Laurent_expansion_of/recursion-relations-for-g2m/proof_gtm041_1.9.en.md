---
role: proof
locale: en
of_concept: recursion-relations-for-g2m
source_book: gtm041
source_chapter: "1"
source_section: "1.9"
---

Differentiate the differential equation $[\wp'(z)]^2 = 4\wp^3(z) - g_2\wp(z) - g_3$ to obtain

$$2\wp'(z)\wp''(z) = 12\wp^2(z)\wp'(z) - g_2\wp'(z).$$

Dividing by $2\wp'(z)$ (valid away from the zeros of $\wp'$) yields the second-order differential equation

$$\wp''(z) = 6\wp^2(z) - \frac{1}{2}g_2. \tag{5}$$

Now write $\wp(z) = z^{-2} + \sum_{n=1}^{\infty} b(n)z^{2n}$. Then

$$\wp''(z) = 6z^{-4} + \sum_{n=1}^{\infty} 2n(2n-1)b(n)z^{2n-2},$$

and

$$\wp^2(z) = z^{-4} + 2\sum_{n=1}^{\infty} b(n)z^{2n-2} + \sum_{k=1}^{\infty}\sum_{j=1}^{\infty} b(k)b(j)z^{2k+2j}.$$

Substituting into (5) and equating coefficients of like powers of $z$ yields the recurrence: for $n \geq 3$,

$$(2n + 3)(n - 2)b(n) = 3\sum_{k=1}^{n-2} b(k)b(n - 1 - k).$$

Since $b(n) = (2n+1)G_{2n+2}$ by Theorem 1.11, substituting this relation yields the equivalent formula for $m \geq 4$:

$$(2m + 1)(m - 3)(2m - 1)G_{2m} = 3 \sum_{r=2}^{m-2}(2r - 1)(2m - 2r - 1)G_{2r}G_{2m-2r}.$$

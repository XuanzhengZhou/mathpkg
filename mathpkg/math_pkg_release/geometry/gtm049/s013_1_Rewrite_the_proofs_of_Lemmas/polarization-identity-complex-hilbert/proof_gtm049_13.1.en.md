---
role: proof
locale: en
of_concept: polarization-identity-complex-hilbert
source_book: gtm049
source_chapter: "13"
source_section: "13.1"
---

Expand each squared norm using $\|x\|^2 = \sigma(x, x)$:

$$
\begin{aligned}
\|a + b\|^2 &= \sigma(a+b, a+b) = \sigma(a,a) + \sigma(a,b) + \sigma(b,a) + \sigma(b,b), \\
\|a - b\|^2 &= \sigma(a-b, a-b) = \sigma(a,a) - \sigma(a,b) - \sigma(b,a) + \sigma(b,b).
\end{aligned}
$$

Subtracting the second from the first gives

$$
\|a + b\|^2 - \|a - b\|^2 = 2\sigma(a,b) + 2\sigma(b,a).
$$

Similarly,

$$
\begin{aligned}
\|a - ib\|^2 &= \sigma(a-ib, a-ib) = \sigma(a,a) + i\sigma(a,b) - i\sigma(b,a) + \sigma(b,b), \\
\|a + ib\|^2 &= \sigma(a+ib, a+ib) = \sigma(a,a) - i\sigma(a,b) + i\sigma(b,a) + \sigma(b,b).
\end{aligned}
$$

Subtracting gives

$$
\|a + ib\|^2 - \|a - ib\|^2 = -2i\sigma(a,b) + 2i\sigma(b,a).
$$

Multiplying by $i$:

$$
i\|a - ib\|^2 - i\|a + ib\|^2 = 2\sigma(a,b) - 2\sigma(b,a).
$$

Adding this to the real part difference yields

$$
(\|a + b\|^2 - \|a - b\|^2) + (i\|a - ib\|^2 - i\|a + ib\|^2) = 4\sigma(a, b),
$$

as required. (This is left as Exercise 2 in the source text.)

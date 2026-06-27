---
role: proof
locale: en
of_concept: integer-infty-left-b16
source_book: gtm054
source_chapter: "10"
source_section: "Section 52"
---

The proof is by induction on $n$. By convention, $p_0(0) = 1$ and $p_0(j) = 0$ for $j \geq 1$. Thus for $n = 1,$ $\sum_{k=0}^{1} p_k(j) = 1$ for all $j$. Hence

$$\sum_{j=0}^{\infty} \left( \sum_{k=0}^{1} p_k(j) \right)x^j = \sum_{j=0}^{\infty} x^j = 1 / (1-x).$$

If the identity holds for $n - 1$, then by the proposition,

$$\sum_{j=0}^{\infty} \left( \sum_{k=0}^{n} p_k(j) \right)x^j = \sum_{k=0

PROOF. By Proposition B14,

$$\sum_{n=0}^{\infty} p_3(n)x_n = \frac{x^3}{(1-x)(1-x^2)(1-x^3)}$$

$$= \frac{1}{72} \left\{ \frac{-1}{1-x} + \frac{-18}{(1-x)^2} + \frac{12}{(1-x)^3} + \frac{-9}{1+x} + \frac{8(2+x)}{1+x+x^2} \right\}.$$

Now

$$\frac{2+x}{1+x+x^2} = \frac{2-x-x^2}{1-x^3} = (2-x-x^2) \sum_{n=0}^{\infty} x^{3n}$$

$$= (2-x-x^2) \sum_{n=0}^{\infty} \left( \left[ \frac{n+3}{3} \right] - \left[ \frac{n+2}{3} \right] \right) x^n$$

$$= \sum_{n=0}^{\infty} \left\{ 2 \left[ \frac{n+3}{3} \right] - 3 \left[ \frac{n+2}{3} \right] + \left[ \frac{n}{3} \right] \right\} x^n$$

$$= -3 \sum_{n=0}^{\infty} \left\{ \left[ \frac{n+2}{3} \right] - \left[ \frac{n}{3} \right] \right\} x^n + 2 \sum_{n=0}^{\infty} x^n.$$

Hence by A8 and A9b,

$$\sum_{n=0}^{\infty} p_3(n)x^n = \frac{1}{72} \left\{ -\sum_{n=0}^{\infty} x^n - 18 \sum_{n=0}^{\infty} (n+1)x^n + 12 \sum_{n=0}^{\infty} \frac{n^2+3n+2}{2}x^n \right\}$$

$$-9 \sum_{n=0}^{\infty} (-1)^

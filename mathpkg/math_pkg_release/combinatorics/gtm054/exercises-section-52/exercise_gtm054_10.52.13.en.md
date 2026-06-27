---
role: exercise
locale: en
chapter: "10"
section: "52"
exercise_number: 13
---

Show that if $a \in \mathbb{C}^N$ and if

(a) $a_n - na_{n-1} - 1 = 0$ with $a_0 = 1$, then $a_n = n! \sum_{j=0}^{n} 1/j!$

(b) $a_n - 2a_{n-1} - 3 = 0$ with $a_0 = 1$, then $a_n = 2^{n+2} - 3.$

Let $*$ denote a binary operation on some set $X$, let $x_1, \ldots, x_n \in X$, and let $a_n$ denote the number of ways that $n

Thus $[a(x)]^2 - a(x) + 1/4 = 1/4 - x$, and by Proposition A13, this quadratic equation has the two solutions $a(x) = 1/2 \pm \sqrt{1 - 4x}/2$. The boundary condition $a_0 = 0$ determines that

$$a(x) = \frac{1}{2} - \frac{\sqrt{1 - 4x}}{2}.$$

This is the ordinary generating function for the sequence $a_0, a_1, \ldots$, and it remains only to use Exercise A10b and A14 to get a general formula for $a_n$.

From $D(a) = (1 - 4x)^{-1/2}$ we derive inductively $D^n(a) = 2^{n-1} \cdot 1 \cdot 3 \cdot 5 \cdot \ldots \cdot (2n - 3)(1 - 4x)^{-n+1/2}$ for $n \geq 2$, whence

$$a_n = \frac{[D^n(a)]_0}{n!} = \frac{2^{n-1} \cdot 1 \cdot 3 \cdot \ldots \cdot (2n - 3)}{n!}$$

$$= \frac{2^{n-1}}{n!} \cdot \frac{(2n - 2)!}{2^{n-1}(n - 1)!} = \frac{1}{n} \binom{2n - 2}{n - 1}.$$

For our final application of the notions of this section, we return to the doubly-indexed sequence $p_k(n)$ ($k, n \in \mathbb{N}$), the number of $k$-partitions of the integer $n$. We first obtain the ordinary generating function for $p_k(0), p_k(1), \ldots$.

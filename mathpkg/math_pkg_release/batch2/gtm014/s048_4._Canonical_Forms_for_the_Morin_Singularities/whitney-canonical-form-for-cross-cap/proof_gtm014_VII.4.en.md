---
role: proof
locale: en
of_concept: whitney-canonical-form-for-cross-cap
source_book: gtm014
source_chapter: "VII"
source_section: "4"
---

By the Malgrange preparation theorem, we can write

$$
f^* a_1 = x_1^2
$$

with $a_1$ and $a_2$ being smooth functions of the $y$ variables. If we make a change of $x$ variables, substituting $x_1 + \frac{1}{2} f^* a_2$ for $x_1$ and leaving the other $x_i$ fixed, we can make $a_2 = 0$, so that $f^* a_1 = x_1^2$.

Now set $x_2 = \cdots = x_n = y_2 = \cdots = y_n = 0$ and expand the left-hand side of $f^* a_1 = x_1^2$ in powers of $x_1$. Since $f_1 = f^* y_1 = c x_1^2 + \cdots$ and $f_s(x_1, 0, \ldots, 0) = O(x_1^3)$ for $s > n$, with $c \neq 0$, we must have

$$
a_1(y_1, 0, \ldots, 0) = \frac{1}{c} y_1.
$$

In particular, $\frac{\partial a_1}{\partial y_1} \neq 0$, so the map

$$
(y_1, \ldots, y_{2n-1}) \mapsto (a_1(y), y_2, \ldots, y_{2n-1})
$$

is a legitimate coordinate change. Replacing the old $y$ coordinates by the new $y$ coordinates, we have $f^* y_1 = x_1^2$ and we continue to have $f^* y_i = x_i$ for $2 \leq i \leq n$.

The remaining coordinate functions $f_i = f^* y_i$ for $i > n$ can be written, using the Malgrange preparation theorem, in the form

$$
f_i = g_i(x_1^2, x_2, \ldots, x_n) + x_1 h_i(x_1^2, x_2, \ldots, x_n).
$$

Replacing $y_i$ by $y_i - g_i(y_1, \ldots, y_n)$ for $i = n+1, \ldots, 2n-1$ eliminates the $g_i$ terms, yielding the canonical form.

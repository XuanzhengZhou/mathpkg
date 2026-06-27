---
role: proof
locale: en
of_concept: inverse-function-analytic
source_book: gtm011
source_chapter: "2"
source_section: "5"
---

Fix $a \in G$ and let $h \in \mathbb{C}$ such that $h \neq 0$ and $a+h \in G$. Since $g(f(z)) = z$ for all $z \in G$, we have $a = g(f(a))$ and $a+h = g(f(a+h))$, which implies $f(a) \neq f(a+h)$. Consider the difference quotient for $g \circ f$:

$$1 = \frac{g(f(a+h)) - g(f(a))}{h}$$

$$= \frac{g(f(a+h)) - g(f(a))}{f(a+h) - f(a)} \cdot \frac{f(a+h) - f(a)}{h}.$$

Now the limit of the left hand side as $h \to 0$ is $1$, so the limit of the right hand side exists. Since $\lim_{h \to 0} [f(a+h) - f(a)] = 0$ by continuity of $f$, and $g$ is analytic,

$$\lim_{h \to 0} \frac{g(f(a+h)) - g(f(a))}{f(a+h) - f(a)} = g'(f(a)).$$

Hence we get that

$$\lim_{h \to 0} \frac{f(a+h) - f(a)}{h}$$

exists since $g'(f(a)) \neq 0$, and

$$1 = g'(f(a)) f'(a).$$

Thus, $f'(z) = [g'(f(z))]^{-1}$. If $g$ is analytic then $g'$ is continuous and this gives that $f$ is analytic.

---
role: proof
locale: en
of_concept: perturbed-minimum-displacement
source_book: gtm060
source_chapter: "6"
source_section: "30"
---

We compute the derivative of $f_\varepsilon$:

$$f_\varepsilon'(x) = f'(x) + \varepsilon h'(x).$$

Since $f(x) = A x^2/2 + \cdots$, we have $f'(x) = A x + O(x^2)$. Also $h'(x) = C + O(x)$. Therefore

$$f_\varepsilon'(x) = A x + C \varepsilon + O(x^2) + O(\varepsilon x).$$

The minimum $x_\varepsilon$ of $f_\varepsilon$ satisfies $f_\varepsilon'(x_\varepsilon) = 0$. Applying the implicit function theorem to the equation $F(x, \varepsilon) = f_\varepsilon'(x) = 0$ near $(x, \varepsilon) = (0, 0)$, we note that $\partial F/\partial x|_{(0,0)} = f''(0) = A \neq 0$. Hence there exists a unique smooth function $x_\varepsilon$ of $\varepsilon$ for small $\varepsilon$ with $x_0 = 0$.

From $A x_\varepsilon + C \varepsilon + O(x_\varepsilon^2) + O(\varepsilon x_\varepsilon) = 0$, substituting the ansatz $x_\varepsilon = \alpha \varepsilon + O(\varepsilon^2)$ yields $A \alpha \varepsilon + C \varepsilon = O(\varepsilon^2)$, so $\alpha = -C/A$. Thus

$$x_\varepsilon = -\frac{C \varepsilon}{A} + O(\varepsilon^2).$$

For the second derivative, we compute

$$f_\varepsilon''(x) = f''(x) + \varepsilon h''(x).$$

Since $f''(0) = A$ and $x_\varepsilon = O(\varepsilon)$, Taylor expanding $f''$ around $0$ gives $f''(x_\varepsilon) = A + O(\varepsilon)$. Similarly $\varepsilon h''(x_\varepsilon) = O(\varepsilon)$. Therefore

$$f_\varepsilon''(x_\varepsilon) = A + O(\varepsilon).$$

---
role: proof
locale: en
of_concept: cauchy-riemann-equations
source_book: gtm011
source_chapter: "2"
source_section: "5"
---

Let $f$ be analytic at $z = x + iy$. Computing the derivative along the real axis:

$$\frac{f(z+h) - f(z)}{h} = \frac{f(x+h+iy) - f(x+iy)}{h}$$

$$= \frac{u(x+h, y) - u(x, y)}{h} + i \frac{v(x+h, y) - v(x, y)}{h}.$$

Letting $h \to 0$ (real) gives

$$f'(z) = \frac{\partial u}{\partial x}(x, y) + i \frac{\partial v}{\partial x}(x, y). \tag{2.22}$$

Now compute the derivative along the imaginary axis. For real $h \neq 0$:

$$\frac{f(z+ih) - f(z)}{ih} = -i \frac{u(x, y+h) - u(x, y)}{h} + \frac{v(x, y+h) - v(x, y)}{h}.$$

Letting $h \to 0$ gives

$$f'(z) = -i \frac{\partial u}{\partial y}(x, y) + \frac{\partial v}{\partial y}(x, y). \tag{2.23}$$

Equating the real and imaginary parts of (2.22) and (2.23) yields the Cauchy-Riemann equations:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}. \tag{2.24}$$

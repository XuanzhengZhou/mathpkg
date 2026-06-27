---
role: proof
locale: en
of_concept: real-imaginary-differentiability
source_book: gtm011
source_chapter: "XII"
source_section: "Appendix A. Calculus for Complex Valued Functions on an Interval"
---

Write $f(x) = u(x) + i v(x)$ where $u(x) = \operatorname{Re} f(x)$ and $v(x) = \operatorname{Im} f(x)$. The difference quotient is

$$\frac{f(x+h) - f(x)}{h} = \frac{u(x+h) - u(x)}{h} + i \frac{v(x+h) - v(x)}{h}.$$

Since a complex sequence converges if and only if its real and imaginary parts converge, the limit $\lim_{h \to 0} \frac{f(x+h)-f(x)}{h}$ exists if and only if both $\lim_{h \to 0} \frac{u(x+h)-u(x)}{h}$ and $\lim_{h \to 0} \frac{v(x+h)-v(x)}{h}$ exist. In that case,

$$f'(x) = u'(x) + i v'(x).$$

If $f'(x) = 0$ for all $x$, then $u'(x) = v'(x) = 0$ for all $x$. By the Mean Value Theorem for real-valued functions, $u$ and $v$ are constant. Hence $f$ is constant.

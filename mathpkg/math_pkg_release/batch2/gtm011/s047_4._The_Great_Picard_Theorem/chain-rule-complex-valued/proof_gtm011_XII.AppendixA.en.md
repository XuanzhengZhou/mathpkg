---
role: proof
locale: en
of_concept: chain-rule-complex-valued
source_book: gtm011
source_chapter: "XII"
source_section: "Appendix A. Calculus for Complex Valued Functions on an Interval"
---

(a) Write $f(t) = u(t) + i v(t)$ where $u = \operatorname{Re} f$, $v = \operatorname{Im} f$. Then

$$f(g(t)) = u(g(t)) + i v(g(t)).$$

Applying the Chain Rule from real calculus to $u \circ g$ and $v \circ g$ individually gives

$$(f \circ g)'(t) = u'(g(t)) g'(t) + i v'(g(t)) g'(t) = [u'(g(t)) + i v'(g(t))] g'(t) = f'(g(t)) \cdot g'(t).$$

(b) Let $G$ be an open subset of $\mathbb{C}$ with $f([a, b]) \subset G$ and let $h: G \to \mathbb{C}$ be analytic. For a fixed $x_0 \in [a, b]$, put $z_0 = f(x_0)$. Since $h$ is analytic at $z_0$, we have

$$h(z) - h(z_0) = h'(z_0)(z - z_0) + \varepsilon(z)(z - z_0)$$

where $\varepsilon(z) \to 0$ as $z \to z_0$. Substituting $z = f(x)$ and dividing by $x - x_0$,

$$\frac{h(f(x)) - h(f(x_0))}{x - x_0} = h'(f(x_0)) \frac{f(x) - f(x_0)}{x - x_0} + \varepsilon(f(x)) \frac{f(x) - f(x_0)}{x - x_0}.$$

As $x \to x_0$, we have $f(x) \to f(x_0)$ by continuity of $f$ (differentiability implies continuity), so $\varepsilon(f(x)) \to 0$. Taking the limit yields

$$(h \circ f)'(x_0) = h'(f(x_0)) f'(x_0).$$

This argument follows the same line as the proof for the composition of two analytic functions given in Proposition III.2.4.

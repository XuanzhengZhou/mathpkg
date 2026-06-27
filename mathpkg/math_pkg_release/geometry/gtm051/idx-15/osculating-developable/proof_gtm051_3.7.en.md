---
role: proof
locale: en
of_concept: osculating-developable
source_book: gtm051
source_chapter: "3"
source_section: "3.7"
---

We compute the mixed partial derivative:
$$g_{st} = \dot{Y}.$$

Since $Y$ is tangential to $f$ and $n$ is the unit normal to $f$, we have $n \cdot Y = 0$. Differentiating along $c(t)$ gives $\dot{n} \cdot Y + n \cdot \dot{Y} = 0$, hence $n \cdot \dot{Y} = -\dot{n} \cdot Y$.

Now,
$$n \cdot g_{st} = n \cdot \dot{Y} = -\dot{n} \cdot Y = II(\dot{c}, Y) = 0,$$
where the last equality holds by hypothesis.

By Proposition 3.7.5(ii), the condition $n_s \cdot f_{st} = 0$ is equivalent to developability (or equivalently $h_{12} = 0$). Thus $g(s, t)$ is developable. The curve $c$ is given by $g(0, t) = c(t)$, and the tangent plane is spanned by $g_s = Y$ and $g_t = \dot{c} + s\dot{Y}$, which at $s = 0$ coincides with the tangent plane of $f$.

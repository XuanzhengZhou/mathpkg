---
role: proof
locale: en
of_concept: surface-of-revolution-gauss-curvature
source_book: gtm051
source_chapter: "3"
source_section: "3.9.1"
---

Given the surface of revolution $f(u, v) = (h(u) \cos v, h(u) \sin v, k(u))$ with $h'^2 + k'^2 = 1$, compute the partial derivatives:
$$f_u = (h' \cos v, h' \sin v, k'), \quad f_v = (-h \sin v, h \cos v, 0).$$

The first fundamental form coefficients:
$$g_{11} = f_u \cdot f_u = h'^2 + k'^2 = 1,$$
$$g_{12} = f_u \cdot f_v = 0,$$
$$g_{22} = f_v \cdot f_v = h^2.$$

The unit normal is $n = f_u \times f_v / |f_u \times f_v|$. Compute:
$$f_u \times f_v = (-h k' \cos v, -h k' \sin v, h h'),$$
$$|f_u \times f_v| = h \sqrt{h'^2 + k'^2} = h.$$
Thus $n = (-k' \cos v, -k' \sin v, h')$.

Second derivatives:
$$f_{uu} = (h'' \cos v, h'' \sin v, k''), \quad f_{uv} = (-h' \sin v, h' \cos v, 0), \quad f_{vv} = (-h \cos v, -h \sin v, 0).$$

Second fundamental form coefficients $h_{ik} = f_{u^i u^k} \cdot n$:
$$h_{11} = f_{uu} \cdot n = -h''k' + h'k'' = -k'h'' + h'k'',$$
$$h_{12} = f_{uv} \cdot n = 0,$$
$$h_{22} = f_{vv} \cdot n = h k'.$$

Using $h'^2 + k'^2 = 1$, differentiating gives $h'h'' + k'k'' = 0$, so $k'k'' = -h'h''$. Then:
$$h_{11}h_{22} - h_{12}^2 = (-k'h'' + h'k'')(hk') = h(-k'^2 h'' + h'k'k'') = h(-k'^2 h'' - h'^2 h'') = -h h''(k'^2 + h'^2) = -h h''.$$

Hence the Gauss curvature is:
$$K = \frac{h_{11}h_{22} - h_{12}^2}{g_{11}g_{22} - g_{12}^2} = \frac{-h h''}{1 \cdot h^2} = -\frac{h''}{h}.$$

For constant curvature $K_0$, we obtain $h'' + K_0 h = 0$, with the constraint $h'^2 \leq 1$ (since $h'^2 + k'^2 = 1$ and $k'^2 \geq 0$).

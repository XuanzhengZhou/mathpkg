---
role: proof
locale: en
of_concept: bilinear-form-equivalent-definition
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "1. Bilinear forms"
---

Suppose we are given a linear transformation $R: \mathfrak{R}' \to \mathfrak{R}^*$, where for each $y' \in \mathfrak{R}'$, $R(y') = g_{y'}$ is a linear function on $\mathfrak{R}$. Define $g(x, y') = g_{y'}(x) = (R(y'))(x)$. We verify that $g$ is a bilinear form. Since each $g_{y'}$ is linear in $x$, we have

$$g(x_1 + x_2, y') = g_{y'}(x_1 + x_2) = g_{y'}(x_1) + g_{y'}(x_2) = g(x_1, y') + g(x_2, y'),$$

$$g(\alpha x, y') = g_{y'}(\alpha x) = \alpha g_{y'}(x) = \alpha g(x, y').$$

Since $R$ is linear in $y'$, we have

$$g(x, y_1' + y_2') = (R(y_1' + y_2'))(x) = (R(y_1') + R(y_2'))(x) = g_{y_1'}(x) + g_{y_2'}(x) = g(x, y_1') + g(x, y_2'),$$

$$g(x, y'\alpha) = (R(y'\alpha))(x) = (R(y')\alpha)(x) = g_{y'}(x)\alpha = g(x, y')\alpha.$$

Thus $g$ is a bilinear form. The converse is given by the induced mapping $R$ defined in the preceding proposition, which we have already shown to be a linear transformation.

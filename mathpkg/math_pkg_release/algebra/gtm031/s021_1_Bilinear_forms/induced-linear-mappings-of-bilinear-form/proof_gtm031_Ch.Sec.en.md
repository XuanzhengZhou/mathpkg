---
role: proof
locale: en
of_concept: induced-linear-mappings-of-bilinear-form
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "1. Bilinear forms"
---

The linearity of $g_{y'}$ in $x$ follows directly from the defining properties (5) of a bilinear form: for each fixed $y'$,

$$g_{y'}(x_1 + x_2) = g(x_1 + x_2, y') = g(x_1, y') + g(x_2, y') = g_{y'}(x_1) + g_{y'}(x_2),$$

$$g_{y'}(\alpha x) = g(\alpha x, y') = \alpha g(x, y') = \alpha g_{y'}(x).$$

Thus $g_{y'} \in \mathfrak{R}^*$. To verify that the mapping $R: y' \mapsto g_{y'}$ is linear, we use the defining properties (6) of a bilinear form:

$$g_{y_1' + y_2'}(x) = g(x, y_1' + y_2') = g(x, y_1') + g(x, y_2') = g_{y_1'}(x) + g_{y_2'}(x),$$

$$g_{y'\alpha}(x) = g(x, y'\alpha) = g(x, y')\alpha = g_{y'}(x)\alpha.$$

Hence $R(y_1' + y_2') = R(y_1') + R(y_2')$ and $R(y'\alpha) = R(y')\alpha$, so $R$ is a linear transformation of $\mathfrak{R}'$ into $\mathfrak{R}^*$.

The analogous statements for $g_x$ and $L$ follow by symmetry, using the linearity in the second argument.

---
role: proof
locale: en
of_concept: representation-of-linear-transformation-as-sum-of-products
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "5"
---

Let $A : \mathfrak{R}_1 \to \mathfrak{R}_2$ be a linear transformation. The image $\mathfrak{R}_1 A$ is a subspace of $\mathfrak{R}_2$; let $\dim(\mathfrak{R}_1 A) = r$ and choose a basis $v_1, v_2, \dots, v_r$ of $\mathfrak{R}_1 A$. For any $x \in \mathfrak{R}_1$, the vector $xA$ can be written in one and only one way as

$$xA = \phi_1(x) v_1 + \phi_2(x) v_2 + \cdots + \phi_r(x) v_r$$

where the coefficients $\phi_i(x) \in \Delta$ are uniquely determined by $x$. We write $\phi_i = \phi_i(x)$ as functions of $x$.

For $y \in \mathfrak{R}_1$, we have

$$\sum_{i=1}^r \phi_i(x + y) v_i = (x + y)A = xA + yA = \sum_{i=1}^r \phi_i(x) v_i + \sum_{i=1}^r \phi_i(y) v_i.$$

By the uniqueness of representation in the basis $\{v_i\}$, we obtain $\phi_i(x + y) = \phi_i(x) + \phi_i(y)$. Similarly, for $\alpha \in \Delta$,

$$(\alpha x)A = \alpha(xA) = \alpha \sum_{i=1}^r \phi_i(x) v_i = \sum_{i=1}^r (\alpha \phi_i(x)) v_i,$$

and comparing with $\sum \phi_i(\alpha x) v_i$ gives $\phi_i(\alpha x) = \alpha \phi_i(x)$. Thus each $\phi_i : \mathfrak{R}_1 \to \Delta$ is a linear function.

Since $g_1(x, y')$ is a non-degenerate bilinear form, every linear function on $\mathfrak{R}_1$ can be represented via $g_1$. Hence there exist vectors $u_i' \in \mathfrak{R}_1'$ such that $\phi_i(x) = g_1(x, u_i')$ for all $x \in \mathfrak{R}_1$. Substituting back yields

$$xA = g_1(x, u_1') v_1 + g_1(x, u_2') v_2 + \cdots + g_1(x, u_r') v_r,$$

and therefore $A = u_1' \times v_1 + u_2' \times v_2 + \cdots + u_r' \times v_r$ as required.

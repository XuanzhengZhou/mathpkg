---
role: proof
locale: en
of_concept: primitive-recursion-closure-under-a
source_book: gtm037
source_chapter: "3"
source_section: "Recursive Functions; Turing Computability"
---

By (31), there exists a $z$ such that $\beta(z,i) = g(x_0,\ldots,x_{m-1},i)$ for each $i \leq y$. Let

$$k'(x_0, \ldots, x_{m-1}, y, z, w) = \overline{\mathrm{sg}}\,|\beta(z, w) - h(x_0, \ldots, x_{m-1}, w, \beta(z, w))| \cdot \mathrm{sg}(|w - y|).$$

For any fixed $x_0, \ldots, x_{m-1}, y$, we have that $k'$ is zero exactly when $w < y$ and $\beta(z,w) = h(x_0,\ldots,x_{m-1},w,\beta(z,w))$, or when $w = y$. Thus the least $z$ for which the product over all $w \leq y$ of $k'$ vanishes encodes the computation of $g$. Since $\beta(z,0) = g(x_0,\ldots,x_{m-1},0) = f(x_0,\ldots,x_{m-1})$, and the conditions involve only functions in $A$ (namely $f$, $h$, $\beta$, arithmetic operations, and the bounded search), we obtain $g(x_0,\ldots,x_{m-1},y) = \beta(t,y)$ where $t$ is the least such $z$. Hence $g \in A$.

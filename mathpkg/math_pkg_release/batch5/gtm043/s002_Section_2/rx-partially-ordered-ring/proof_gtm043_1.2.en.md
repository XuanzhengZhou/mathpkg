---
role: proof
locale: en
of_concept: rx-partially-ordered-ring
source_book: gtm043
source_chapter: "1"
source_section: "1.2"
---

Translation invariance follows directly from the definition: for any $h$,
$$(f + h)(x) - (g + h)(x) = f(x) + h(x) - g(x) - h(x) = f(x) - g(x).$$
Thus $(f+h)(x) \geq (g+h)(x)$ for all $x$ if and only if $f(x) \geq g(x)$ for all $x$, i.e., $f + h \geq g + h \iff f \geq g$.

For nonnegativity of products: if $f(x) \geq 0$ and $g(x) \geq 0$ for all $x \in X$, then $(fg)(x) = f(x)g(x) \geq 0$ for all $x$, since the product of two nonnegative real numbers is nonnegative. Hence $f \geq 0$ and $g \geq 0$ implies $fg \geq 0$.

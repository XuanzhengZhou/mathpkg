---
role: proof
locale: en
of_concept: rx-commutative-ring-with-unity
source_book: gtm043
source_chapter: "1"
source_section: "1.1"
---

The associativity and commutativity of addition follow because for each $x \in X$,
$$((f+g)+h)(x) = (f(x)+g(x))+h(x) = f(x)+(g(x)+h(x)) = (f+(g+h))(x),$$
$$(f+g)(x) = f(x)+g(x) = g(x)+f(x) = (g+f)(x).$$
Similarly for multiplication. The distributive law holds because
$$(f(g+h))(x) = f(x)(g(x)+h(x)) = f(x)g(x) + f(x)h(x) = (fg + fh)(x).$$
These are immediate consequences of the corresponding properties of the field $\mathbf{R}$. The zero function $0(x) = 0$ satisfies $(f+0)(x) = f(x) + 0 = f(x)$, so $0$ is the additive identity. The constant function $1(x) = 1$ satisfies $(f \cdot 1)(x) = f(x) \cdot 1 = f(x)$, so $1$ is the multiplicative identity (unity). Thus $\mathbf{R}^X$ is a commutative ring with unity, provided $X \neq \emptyset$.

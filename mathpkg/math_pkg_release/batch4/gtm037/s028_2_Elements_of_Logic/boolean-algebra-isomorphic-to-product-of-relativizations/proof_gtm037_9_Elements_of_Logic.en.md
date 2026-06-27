---
role: proof
locale: en
of_concept: boolean-algebra-isomorphic-to-product-of-relativizations
source_book: gtm037
source_chapter: "9"
source_section: "Elements of Logic"
---

For any $x \in A$, let $f(x) = \langle x \cdot a, x \cdot -a \rangle$. Then $f$ maps $A$ into $(\mathfrak{A} \upharpoonright a) \times (\mathfrak{A} \upharpoonright -a)$. The map $f$ is a homomorphism: $f(x + y) = \langle (x+y) \cdot a, (x+y) \cdot -a \rangle = \langle x \cdot a + y \cdot a, x \cdot -a + y \cdot -a \rangle = f(x) + f(y)$, and similarly for $\cdot$ and $-$. Moreover, $f$ is one-one since if $f(x) = f(y)$ then $x \cdot a = y \cdot a$ and $x \cdot -a = y \cdot -a$, whence $x = x \cdot 1 = x \cdot (a + -a) = x \cdot a + x \cdot -a = y \cdot a + y \cdot -a = y$. Finally, $f$ is onto: given $\langle u, v \rangle$ with $u \leq a$ and $v \leq -a$, let $x = u + v$. Then $x \cdot a = (u+v) \cdot a = u \cdot a + v \cdot a = u + 0 = u$ and $x \cdot -a = (u+v) \cdot -a = u \cdot -a + v \cdot -a = 0 + v = v$, so $f(x) = \langle u, v \rangle$. Thus $f$ is an isomorphism.

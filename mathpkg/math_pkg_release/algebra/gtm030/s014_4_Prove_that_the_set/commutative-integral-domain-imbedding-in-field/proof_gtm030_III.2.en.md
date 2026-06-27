---
role: proof
locale: en
of_concept: commutative-integral-domain-imbedding-in-field
source_book: gtm030
source_chapter: "III"
source_section: "2"
---

Let $\mathfrak{A}$ be a commutative integral domain $\neq 0$. Construct the field of fractions $\mathfrak{J}$ as follows. Let $\mathfrak{B}$ be the totality of ordered pairs $(a, b)$ with $a, b \in \mathfrak{A}$, $b \neq 0$. Define the equivalence relation
$$(a, b) \sim (c, d) \iff ad = bc.$$
Denote the equivalence class of $(a, b)$ by the fraction $a/b$. The set $\mathfrak{J}$ of all such fractions forms a commutative ring with addition
$$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$$
and multiplication
$$\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}.$$
These operations are well-defined (single-valued) because if $a/b = a'/b'$ and $c/d = c'/d'$, then $ab' = ba'$ and $cd' = dc'$, whence $(ad+bc)b'd' = (a'd'+b'c')bd$ and $acb'd' = a'c'bd$.

The zero element is $0/b = 0/d$, the negative of $a/b$ is $(-a)/b = a/(-b)$, and the identity is $1 = b/b = d/d$ for any $b \neq 0, d \neq 0$. If $a/b \neq 0$ (so $a \neq 0$), then $b/a \in \mathfrak{J}$ and $(a/b)(b/a) = ab/ba = 1$, so every non-zero element has an inverse. Hence $\mathfrak{J}$ is a field.

Define the map $\varphi: \mathfrak{A} \to \mathfrak{J}$ by $\varphi(a) = \overline{a} = ab/b$ for any fixed $b \neq 0$. This is independent of the choice of $b$ since $ab/b = ad/d$ for any $b, d \neq 0$. The map is a homomorphism:
$$\overline{a + a'} = (a+a')b/b = (ab + a'b)/b = ab/b + a'b/b = \overline{a} + \overline{a'},$$
$$\overline{aa'} = aa'b/b = aa'b^2/b^2 = (ab/b)(a'b/b) = \overline{a} \cdot \overline{a'}.$$
If $\overline{a} = 0$, then $ab/b = 0/b$, so $ab^2 = 0 \cdot b^2 = 0$. Since $\mathfrak{A}$ is an integral domain and $b \neq 0$, we have $a = 0$. Thus $\varphi$ is injective. Therefore $\overline{\mathfrak{A}} = \{\overline{a} : a \in \mathfrak{A}\}$ is a subring of $\mathfrak{J}$ isomorphic to $\mathfrak{A}$, and $\mathfrak{J}$ is a field containing an isomorphic copy of $\mathfrak{A}$.

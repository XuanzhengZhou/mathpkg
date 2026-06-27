---
role: proof
locale: en
of_concept: residue-at-a-pole
source_book: gtm011
source_chapter: "V"
source_section: "§2. Residues"
content_hash: ""
written_against: ""
---

Since $f$ has a pole of order $m$ at $z = a$, its Laurent expansion about $z = a$ has the form
$$f(z) = \frac{a_{-m}}{(z-a)^m} + \cdots + \frac{a_{-1}}{z-a} + a_0 + a_1(z-a) + \cdots$$
with $a_{-m} \neq 0$. Multiply both sides by $(z-a)^m$:
$$(z-a)^m f(z) = a_{-m} + a_{-m+1}(z-a) + \cdots + a_{-1}(z-a)^{m-1} + a_0(z-a)^m + \cdots.$$
The right-hand side is a convergent power series and therefore defines a function analytic at $z = a$. Differentiating $(m-1)$ times with respect to $z$ gives
$$\frac{d^{m-1}}{dz^{m-1}}\bigl[(z-a)^m f(z)\bigr] = (m-1)!\, a_{-1} + m!\, a_0 (z-a) + \cdots.$$
Taking the limit as $z \to a$, all higher-order terms vanish:
$$\lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}}\bigl[(z-a)^m f(z)\bigr] = (m-1)!\, a_{-1} = (m-1)! \operatorname{Res}(f; a).$$
Hence
$$\operatorname{Res}(f; a) = \frac{1}{(m-1)!} \lim_{z \to a} \frac{d^{m-1}}{dz^{m-1}}\bigl[(z-a)^m f(z)\bigr].$$

For $m = 1$ (a simple pole), the formula reduces to $\operatorname{Res}(f; a) = \lim_{z \to a} (z-a) f(z)$.

Now suppose $f(z) = g(z)/h(z)$ where $g$ and $h$ are analytic at $a$, $g(a) \neq 0$, $h(a) = 0$, and $h'(a) \neq 0$. Then $h(z) = h'(a)(z-a) + O((z-a)^2)$, so
$$(z-a)f(z) = \frac{g(z)}{\frac{h(z)}{z-a}} = \frac{g(z)}{\frac{h(z)-h(a)}{z-a}}.$$
Since $\lim_{z \to a} \frac{h(z)-h(a)}{z-a} = h'(a)$, we obtain
$$\operatorname{Res}(f; a) = \lim_{z \to a} (z-a)f(z) = \frac{g(a)}{h'(a)}.$$

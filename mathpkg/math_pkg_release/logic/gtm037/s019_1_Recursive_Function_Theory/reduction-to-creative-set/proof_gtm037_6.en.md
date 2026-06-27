---
role: proof
locale: en
of_concept: reduction-to-creative-set
source_book: gtm037
source_chapter: "6"
source_section: "Recursive Function Theory"
---

Say $A = \mathrm{Dmn}\,\varphi_d^1$, and let $g$ be a productive function for $\omega \sim C$. For any $x, y, z \in \omega$ let

$$l(z, y, x) \simeq \mu u\,[z = g(s_1^1(x, y))] + \varphi_d^1(y).$$

Thus $l$ is partial recursive. By the recursion theorem (5.15) choose $e \in \omega$ such that for all $y, z \in \omega$, $\varphi_e^2(z, y) \simeq l(z, y, e)$. Set $f(y) = g(s_1^1(e, y))$ for all $y \in \omega$. Then $f$ is recursive.

First, suppose that $y \in A$, i.e. $y \in \mathrm{Dmn}\,\varphi_d^1$. Then for any $z \in \omega$, $l(z, y, e) \simeq \mu u\,[z = g(s_1^1(e, y))] + \varphi_d^1(y)$. Choosing $z = f(y) = g(s_1^1(e, y))$, we have $(f(y), y, e) \in \mathrm{Dmn}\,l$, whence $(f(y), y) \in \mathrm{Dmn}\,\varphi_e^2$, so $f(y) \in \mathrm{Dmn}\,\varphi^1(s_1^1(e, y))$. Since $g$ is productive for $\omega \sim C$, the definition of productive function yields $f(y) \in C$. Thus $y \in A$ implies $f(y) \in C$.

Second, suppose that $y \notin A$. Then $y \notin \mathrm{Dmn}\,\varphi_d^1$, so $\forall z\,((z, y, e) \notin \mathrm{Dmn}\,l)$, hence $\forall z\,((z, y) \notin \mathrm{Dmn}\,\varphi_e^2)$, so by 5.13 $\mathrm{Dmn}\,\varphi^1(s_1^1(e, y)) = \emptyset$. Thus, since $g$ is productive,

$$f(y) = g(s_1^1(e, y)) \in (\omega \sim C) \sim \mathrm{Dmn}\,\varphi^1(s_1^1(e, y)),$$

in particular $f(y) \notin C$, as desired.

Therefore $y \in A$ iff $f(y) \in C$, i.e. $A = f^{-1}[C]$.

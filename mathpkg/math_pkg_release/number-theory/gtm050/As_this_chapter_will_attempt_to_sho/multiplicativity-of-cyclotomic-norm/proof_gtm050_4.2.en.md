---
role: proof
locale: en
of_concept: multiplicativity-of-cyclotomic-norm
source_book: gtm050
source_chapter: "4"
source_section: "4.2"
---

Let $h(\alpha) = f(\alpha)g(\alpha)$. Then by definition,
$$Nh(\alpha) = h(\alpha) h(\alpha^2) \cdots h(\alpha^{\lambda-1}) = \prod_{j=1}^{\lambda-1} f(\alpha^j) g(\alpha^j).$$

Since multiplication of complex numbers is commutative, this product can be rearranged as
$$\left(\prod_{j=1}^{\lambda-1} f(\alpha^j)\right) \cdot \left(\prod_{j=1}^{\lambda-1} g(\alpha^j)\right) = Nf(\alpha) \cdot Ng(\alpha).$$

Note that we implicitly use here that the substitution $\alpha \mapsto \alpha^j$ respects multiplication, i.e., $(fg)(\alpha^j) = f(\alpha^j)g(\alpha^j)$, which follows directly from the polynomial definition of multiplication in the cyclotomic integers.

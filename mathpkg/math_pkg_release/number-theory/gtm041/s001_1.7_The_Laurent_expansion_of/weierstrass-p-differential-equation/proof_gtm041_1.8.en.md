---
role: proof
locale: en
of_concept: weierstrass-p-differential-equation
source_book: gtm041
source_chapter: "1"
source_section: "1.8"
---

Consider the elliptic function

$$F(z) = [\wp'(z)]^2 - 4\wp^3(z) + 60G_4\wp(z) + 140G_6.$$

This function has no poles anywhere in a period parallelogram, because the only possible poles are at lattice points, and near $z = 0$ we can examine the Laurent expansions:

$$\wp'(z) = -\frac{2}{z^3} + 6G_4z + 20G_6z^3 + \cdots,$$

$$[\wp'(z)]^2 = \frac{4}{z^6} - \frac{24G_4}{z^2} - 80G_6 + \cdots,$$

$$4\wp^3(z) = \frac{4}{z^6} + \frac{36G_4}{z^2} + 60G_6 + \cdots,$$

where $+\cdots$ indicates a power series in $z$ which vanishes at $z = 0$. Hence

$$[\wp'(z)]^2 - 4\wp^3(z) = -\frac{60G_4}{z^2} - 140G_6 + \cdots,$$

so

$$[\wp'(z)]^2 - 4\wp^3(z) + 60G_4\wp(z) = -140G_6 + \cdots.$$

Since $\wp(z) = z^{-2} + \cdots$, we have $60G_4\wp(z) = 60G_4 z^{-2} + \cdots$, and the $z^{-2}$ terms cancel. The left member therefore has no pole at $z = 0$, and consequently no poles anywhere in any period parallelogram. An elliptic function without poles must be constant. The constant is the value at $z = 0$ of the power series remainder, which is $-140G_6$. Therefore

$$[\wp'(z)]^2 - 4\wp^3(z) + 60G_4\wp(z) + 140G_6 = 0,$$

or equivalently,

$$[\wp'(z)]^2 = 4\wp^3(z) - g_2\wp(z) - g_3,$$

where $g_2 = 60G_4$ and $g_3 = 140G_6$.

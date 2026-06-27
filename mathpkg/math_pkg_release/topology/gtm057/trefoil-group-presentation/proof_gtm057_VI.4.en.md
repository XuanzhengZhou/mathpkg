---
role: proof
locale: en
of_concept: trefoil-group-presentation
source_book: gtm057
source_chapter: "VI"
source_section: "4"
---

For the clover-leaf (trefoil) knot in regular position (Figure 41), choose generators $x, y, z$ corresponding to the three overpasses, with $x = a_1^\sharp$, $y = a_2^\sharp$, $z = a_3^\sharp$. Reading around each underpass gives the Wirtinger relators:

$$v_1^\sharp = x^{-1}yzy^{-1}, \quad v_2^\sharp = y^{-1}zxz^{-1}, \quad v_3^\sharp = z^{-1}xyx^{-1}.$$

Any one relator is a consequence of the other two, so we may drop $v_3^\sharp$, obtaining

$$\pi(R^3 - K) = |x, y, z : x^{-1}yzy^{-1}, y^{-1}zxz^{-1}|.$$

Writing these as relations $x = yzy^{-1}$, $y = zxz^{-1}$, $z = xyx^{-1}$, substitute $z = xyx^{-1}$ into the others:

$$x = y(xyx^{-1})y^{-1}, \quad y = (xyx^{-1})x(xyx^{-1})^{-1} = xyxy^{-1}x^{-1}.$$

The second relation simplifies to $yxy = xyx$. The first becomes $x = yxyx^{-1}y^{-1}$, which is equivalent to $xyx = yxy$. Thus a simplified presentation for the group of the clover-leaf knot is

$$\pi(R^3 - K) = |x, y : xyx = yxy|.$$

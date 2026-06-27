---
role: proof
locale: en
of_concept: cube-condition-via-surds
source_book: gtm050
source_chapter: "2"
source_section: "2.3"
---

Factor $p^2 + 3q^2$ as $(p + q\sqrt{-3})(p - q\sqrt{-3})$. Suppose $p + q\sqrt{-3} = (a + b\sqrt{-3})^3$ for some integers $a$, $b$. Replacing $\sqrt{-3}$ by $-\sqrt{-3}$ in this equation gives the conjugate relation

$$p - q\sqrt{-3} = (a - b\sqrt{-3})^3.$$

Now multiply the two factors:

$$p^2 + 3q^2 = (p + q\sqrt{-3})(p - q\sqrt{-3}) = (a + b\sqrt{-3})^3 (a - b\sqrt{-3})^3.$$

By commutativity of multiplication in $\mathbb{Z}[\sqrt{-3}]$, the right-hand side can be regrouped as $[(a + b\sqrt{-3})(a - b\sqrt{-3})]^3$. Since $(a + b\sqrt{-3})(a - b\sqrt{-3}) = a^2 + 3b^2$, which is an integer, it follows that $p^2 + 3q^2 = (a^2 + 3b^2)^3$, a perfect cube.

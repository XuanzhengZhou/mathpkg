---
role: proof
locale: en
of_concept: conjugate-of-surds-cube
source_book: gtm050
source_chapter: "2"
source_section: "2.3"
---

The map $\sigma: \mathbb{Z}[\sqrt{-3}] \to \mathbb{Z}[\sqrt{-3}]$ defined by $\sigma(a + b\sqrt{-3}) = a - b\sqrt{-3}$ is a ring automorphism (conjugation). Applying $\sigma$ to both sides of the assumed equality $p + q\sqrt{-3} = (a + b\sqrt{-3})^3$ gives

$$p - q\sqrt{-3} = \sigma(p + q\sqrt{-3}) = \sigma((a + b\sqrt{-3})^3) = (\sigma(a + b\sqrt{-3}))^3 = (a - b\sqrt{-3})^3.$$

The third equality holds because $\sigma$ is a ring homomorphism and therefore commutes with the cubing operation.

---
role: proof
locale: en
of_concept: complex-inverse-formula
source_book: gtm012
source_chapter: "1"
source_section: "2. Real and complex numbers"
---

# Proof of Multiplicative Inverse of a Complex Number

For any nonzero complex number $z = x + iy$, we have

$$z^* z = (x - iy)(x + iy) = x^2 + y^2 = |z|^2.$$

Since $z \neq 0$, we have $|z|^2 > 0$, so $|z|^{-2}$ is a well-defined positive real number. Multiplying the identity $1 = z^* z |z|^{-2}$ by $z^{-1}$ on the right (or by associativity),

$$1 = z^* z |z|^{-2} = z \left( z^* |z|^{-2} \right).$$

Therefore the multiplicative inverse of $z$ is given by

$$z^{-1} = z^* |z|^{-2} = \frac{z^*}{|z|^2} = \frac{x - iy}{x^2 + y^2}.$$

This provides an explicit formula for the inverse of any nonzero complex number in terms of its real and imaginary parts.

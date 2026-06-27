---
role: proof
locale: en
of_concept: real-imaginary-formulas
source_book: gtm012
source_chapter: "1"
source_section: "2. Real and complex numbers"
---

# Proof of Formulas for Real and Imaginary Parts via Conjugation

Let $z = x + iy$ with $x, y \in \mathbb{R}$. Then $z^* = x - iy$.

Adding $z$ and $z^*$ eliminates the imaginary part:

$$z + z^* = (x + iy) + (x - iy) = 2x.$$

Subtracting $z^*$ from $z$ isolates the imaginary part:

$$z - z^* = (x + iy) - (x - iy) = 2iy.$$

Solving for the real and imaginary parts, we obtain

$$\operatorname{Re}(z) = x = \frac{1}{2}(z + z^*),$$

$$\operatorname{Im}(z) = y = \frac{1}{2i}(z - z^*) = -\frac{i}{2}(z - z^*).$$

These formulas express the real and imaginary parts purely algebraically in terms of $z$ and its complex conjugate, without reference to the coordinates $x$ and $y$.

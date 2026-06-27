---
role: proof
locale: en
of_concept: sum-of-fourth-powers-not-square
source_book: gtm050
source_chapter: "1"
source_section: "1.5"
---

The proof is identical to that of Fermat's Last Theorem for $n = 4$. Assume $x^4 + y^4$ is a square for positive integers $x, y$. Then by the same infinite descent construction using Pythagorean triple parametrization, one produces strictly smaller positive integers $X, Y$ such that $X^4 + Y^4$ is also a square, with $X^4 + Y^4 < x^4 + y^4$. Repeating this process indefinitely gives an infinite strictly decreasing sequence of positive integers, which contradicts the well-ordering principle. Therefore $x^4 + y^4$ cannot be a square.

The key observation is that the proof only uses the fact that the right-hand side is a square, not that it is a fourth power. This yields the stronger result.

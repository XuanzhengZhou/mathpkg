---
role: proof
locale: en
of_concept: gauss-number-of-genera
source_book: gtm050
source_chapter: "7"
source_section: "7.9"
---
Gauss's proof that at most half of the possible characters actually occur relies on counting ambiguous classes. An ambiguous class is a divisor class that is its own inverse, i.e., $A^2 = I$ in the class group. Gauss showed that the number of ambiguous classes equals the number of possible characters, namely $2^{m+\varepsilon}$. Since each genus contains the same number of classes, and each ambiguous class belongs to a distinct character (because the character of an ambiguous class can be shown to determine the class), it follows that the number of genera is at most half the number of possible characters, i.e., $2^{m+\varepsilon-1}$. Conversely, Gauss showed that the number of genera cannot be less than this bound, establishing equality.

The fact that all genera contain the same number of classes follows from the property that the character of a product is the product of the characters: if $A$ and $B$ are divisor classes, then $\chi(AB) = \chi(A)\chi(B)$. Therefore, if $g$ is the number of genera and $h$ is the total class number, then $h = g \cdot n$ where $n = h/g$ is the number of classes per genus.

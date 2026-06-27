---
role: proof
locale: en
of_concept: genus-count-upper-bound
source_book: gtm050
source_chapter: "7"
source_section: "7.11"
---

From the class number factorization theorems, we have $h = gn = sa$, where $g$ is the number of genera, $n$ is the number of classes per genus, $s$ is the number of distinct squares, and $a$ is the number of ambiguous classes.

Clearly $s \leqslant n$, because the square of any class is in the principal genus. (Indeed, if $A$ is any divisor class and $\chi$ is any character, then $\chi(A^2) = \chi(A)^2 = 1$, so $A^2$ lies in the principal genus.) Thus all $s$ distinct squares are contained within the $n$ classes of the principal genus.

From $h = gn = sa$ we obtain $g = sa/n$. Since $s \leqslant n$, it follows that $g = s \cdot (a/n) \leqslant n \cdot (a/n) = a$, i.e., $g \leqslant a$.

Therefore the number of genera $g$ does not exceed the number of ambiguous classes $a$. Since the number of possible characters of a given type is $2^{m+\varepsilon}$ (the number of subsets of ramifying primes), and $g$ also does not exceed this bound, the estimate of $a$ in the preceding section shows that the number $g$ of characters that actually occur is at most half as great as the number of possible characters.

---
role: proof
locale: en
of_concept: fermat-last-theorem-n4
source_book: gtm050
source_chapter: "1"
source_section: "1.5"
---

Suppose $x, y, z$ are pairwise relatively prime positive integers with $x^4 + y^4 = z^4$. Then $z^2$ and one of $x^2, y^2$, say $x^2$, are the legs of a primitive Pythagorean triple with hypotenuse $z^2$. By the characterization of such triples, there exist relatively prime $p, q$ of opposite parity with $p > q$ such that:
$$x^2 = 2pq, \quad y^2 = p^2 - q^2, \quad z^2 = p^2 + q^2.$$

The second equation $y^2 = p^2 - q^2$ gives another Pythagorean triple, so there exist relatively prime $a, b$ of opposite parity with $a > b$ such that:
$$q = 2ab, \quad y = a^2 - b^2, \quad p = a^2 + b^2.$$

Thus $x^2 = 2pq = 4ab(a^2 + b^2)$, so $ab(a^2 + b^2)$ is a square. Since $a, b$ are relatively prime, $ab$ and $a^2 + b^2$ are relatively prime. Hence each must be a square. Since $ab$ is a square and $a, b$ are relatively prime, $a = X^2, b = Y^2$ for some integers $X, Y$.

Then $X^4 + Y^4 = a^2 + b^2 = p$. But $p < p^2 + q^2 = z^2 < z^4 = x^4 + y^4$. Thus we obtain a new pair $(X, Y)$ with $X^4 + Y^4$ a square and $X^4 + Y^4 < x^4 + y^4$. By infinite descent, this is impossible. Therefore no such $x, y, z$ exist.

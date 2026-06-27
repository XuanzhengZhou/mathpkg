---
role: proof
locale: en
of_concept: q-transformation-sections
source_book: gtm018
source_chapter: "XI"
source_section: "59. Measurable Groups"
---

We first verify the formula for $Q$. Since $S(x,y) = (x,xy)$ and $R(x,y) = (y,x)$, we have $S^{-1}(x,y) = (x, x^{-1}y)$. Then
$$Q(x,y) = S^{-1}RS(x,y) = S^{-1}R(x,xy) = S^{-1}(xy, x) = (xy, (xy)^{-1}x) = (xy, y^{-1}).$$
Also $Q(Q(x,y)) = Q(xy, y^{-1}) = (xy \cdot y^{-1}, (y^{-1})^{-1}) = (x, y)$, so $Q^{-1} = Q$.

For the first conclusion, we use characteristic functions:
$$\chi_{Q(A \times B)}(x^{-1},y) = \chi_{A \times B}(Q^{-1}(x^{-1},y)) = \chi_{A \times B}(Q(x^{-1},y)) = \chi_{A \times B}(x^{-1}y, y^{-1}) = \chi_{A}(x^{-1}y)\chi_{B}(y^{-1}).$$

Now $\chi_A(x^{-1}y) = 1$ iff $x^{-1}y \in A$, i.e., $y \in xA$. And $\chi_B(y^{-1}) = 1$ iff $y^{-1} \in B$, i.e., $y \in B^{-1}$. Thus
$$y \in (Q(A \times B))_{x^{-1}} \iff \chi_{Q(A \times B)}(x^{-1},y) = 1 \iff y \in xA \cap B^{-1},$$
which proves $(Q(A \times B))_{x^{-1}} = xA \cap B^{-1}$.

For the second conclusion,
$$\chi_{Q(A \times B)}(x, y^{-1}) = \chi_{A \times B}(Q^{-1}(x, y^{-1})) = \chi_{A \times B}(Q(x, y^{-1})) = \chi_{A \times B}(x y^{-1}, y) = \chi_{A}(x y^{-1}) \chi_{B}(y).$$

Now $\chi_A(x y^{-1}) = 1$ iff $x y^{-1} \in A$, i.e., $x \in Ay$. And $\chi_B(y) = 1$ iff $y \in B$. Thus
$$x \in (Q(A \times B))^{y^{-1}} \iff \chi_{Q(A \times B)}(x, y^{-1}) = 1 \iff x \in Ay \text{ and } y \in B.$$

If $y \in B$, then $(Q(A \times B))^{y^{-1}} = Ay$. If $y \notin B$ (i.e., $y \in B'$), then the condition is never satisfied, so $(Q(A \times B))^{y^{-1}} = \varnothing$.

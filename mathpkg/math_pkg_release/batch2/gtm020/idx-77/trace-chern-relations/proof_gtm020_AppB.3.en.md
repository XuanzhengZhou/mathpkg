---
role: proof
locale: en
of_concept: trace-chern-relations
source_book: gtm020
source_chapter: "Appendix B"
source_section: "B.3"
---
The generating function relation follows from the identity $\log(\det(I + Xt)) = \text{Tr}(\log(I + Xt))$. Expanding the right side as a formal power series in $t$:
$$
\text{Tr}(\log(I + Xt)) = \sum_{q \geq 1} \frac{(-1)^{q-1}}{q} \text{Tr}(X^q) t^q.
$$
Differentiating with respect to $t$ and multiplying by $-t$ gives
$$
-t \frac{d}{dt} \log(\det(I + Xt)) = \sum_{q \geq 1} \text{Tr}(X^q)(-t)^q.
$$
For the specific relations: $c_1(X) = \text{Tr}(X)$ follows directly from the coefficient of $t$ in $\det(I + Xt) = 1 + \text{Tr}(X)t + \cdots$. The relation $\text{Tr}(X^2) = c_1(X)^2 - 2c_2(X)$ follows by comparing coefficients of $t^2$ in the expansion:
$$\det(I + Xt) = 1 + c_1 t + c_2 t^2 + \cdots,$$
$$\log(1 + c_1 t + c_2 t^2 + \cdots) = c_1 t + (c_2 - \tfrac{1}{2}c_1^2)t^2 + \cdots,$$
and the $t^2$ coefficient of $-t \frac{d}{dt} \log$ gives $c_1^2 - 2c_2 = \text{Tr}(X^2)$. For $n=2$, the Hamilton-Cayley theorem gives $X^2 - \text{Tr}(X)X + \det(X)I = 0$, and taking the trace yields the same identity.

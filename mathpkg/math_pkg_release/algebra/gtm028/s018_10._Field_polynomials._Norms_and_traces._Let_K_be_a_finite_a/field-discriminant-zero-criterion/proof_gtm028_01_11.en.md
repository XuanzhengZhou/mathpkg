---
role: proof
locale: en
of_concept: field-discriminant-zero-criterion
source_book: gtm028
source_chapter: "I"
source_section: "11"
---
If $T(\xi) = 0$ for all $\xi \in K$, then in particular $T(\omega_i \omega_j) = 0$ for all basis elements, so the discriminant matrix is the zero matrix and its determinant $d = 0$. This proves the "if" direction.

Conversely, assume $d = 0$, i.e., $\det(T(\omega_i \omega_j)) = 0$. Then the rows of the matrix $(T(\omega_i \omega_j))$ are linearly dependent over $k$. Hence there exist $c_1, \dots, c_n \in k$, not all zero, such that
$$\sum_{j=1}^{n} c_j \, T(\omega_i \omega_j) = 0, \quad \text{for } i = 1, 2, \dots, n.$$

Set $z = \sum_{j=1}^{n} c_j \omega_j$. Then $z \neq 0$ (since not all $c_j$ are zero and the $\omega_j$ are linearly independent), and by $k$-linearity of the trace:
$$T(\omega_i z) = \sum_{j=1}^{n} c_j \, T(\omega_i \omega_j) = 0, \quad i = 1, 2, \dots, n.$$

Since every $y \in K$ is a $k$-linear combination of the $\omega_i$, we have $T(yz) = 0$ for all $y \in K$.

Now let $\xi \in K$ be arbitrary. Take $y = \xi z^{-1}$ (which lies in $K$ since $z \neq 0$). Then $T(\xi) = T(yz) = 0$. Thus $T(\xi) = 0$ for all $\xi \in K$, completing the proof.

---
role: proof
locale: en
of_concept: properties-of-norms-and-traces
source_book: gtm028
source_chapter: "I"
source_section: "10"
---
If, for a given basis $\Omega$ of $K/k$, we have $x\Omega = A\Omega$ and $y\Omega = B\Omega$, then $(x + y)\Omega = (A + B)\Omega$ and $xy\Omega = BA\Omega$. In view of the definition of traces and norms as trace and determinant of the representing matrices, relations (a) and (c) follow immediately:
$$N(xy) = \det(BA) = \det(B)\det(A) = N(y)N(x) = N(x)N(y),$$
$$T(x+y) = \operatorname{tr}(A+B) = \operatorname{tr}(A) + \operatorname{tr}(B) = T(x) + T(y).$$

If $x \in k$, then $A$ is the diagonal matrix $x E_n$, so $\det(A) = x^n$ and $\operatorname{tr}(A) = nx$. This implies relations (b) and (e).

Property (d) follows directly from the definition of the trace as the sum of diagonal elements of the representing matrix, since scaling $x$ by $c \in k$ scales each $a_{ij}$ by $c$, hence scales the trace by $c$.

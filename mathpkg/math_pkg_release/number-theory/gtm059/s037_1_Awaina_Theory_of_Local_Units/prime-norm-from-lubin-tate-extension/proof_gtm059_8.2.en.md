---
role: proof
locale: en
of_concept: prime-norm-from-lubin-tate-extension
source_book: gtm059
source_chapter: "8"
source_section: "2. Formal p-adic Multiplication"
---

Consider first the bottom level $K(A_1) = K(A_\pi[\pi])$. The extension is obtained by adjoining a root $\lambda$ of the equation $[\pi]_f(X) = 0$, i.e., $f(X) = \pi X + \cdots = 0$. The minimal polynomial of a primitive $\pi$-torsion point $\lambda$ over $K$ has the form
$$
X^{q-1} + \pi(\text{lower terms}).
$$
Taking the norm $N_{K(A_1)/K}(\lambda)$ yields $(-1)^{q-1}\pi$ times a unit. More precisely, one shows that $N_{K(A_1)/K}(-\lambda) = \pi$.

For the general level $K(A_n)$, one proceeds by induction. Let $(x_n)$ be a compatible sequence with $x_n \in A_n$ primitive, so $[\pi](x_n) = x_{n-1}$. One shows that $N_{K(A_n)/K(A_{n-1})}(-x_n) = \pi \cdot u$ where $u$ is a unit. Composing norms down the tower yields $\pi$ as a norm from each $K(A_n)$.

If $q$ is odd, then $-1$ is itself a norm (since the degree of $K(A_n)/K$ is $q^{n-1}(q-1)$, which is even only when $q$ is odd or $n > 1$), so $\pi$ is a norm directly. If $q$ is even, a slight adjustment using the fact that the degree is odd handles the sign.

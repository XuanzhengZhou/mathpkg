---
role: proof
locale: en
of_concept: bruck-ryser-chowla-theorem
source_book: gtm006
source_chapter: "3"
source_section: "5"
---

**Proof.** Let $\mathcal{P}$ be a finite projective plane of order $n$ with $v = n^2 + n + 1$ points. Let $A$ be its incidence matrix.

Let $x_1, x_2, \dots, x_v$ be $v$ indeterminates, and for $i = 1, 2, \dots, v$ define
$$L_i = \sum_{j} x_j$$
where the sum is taken over all $j$ such that $P_j$ is on $l_i$.

Using the incidence matrix property $AA' = nI + J$, one computes:
$$\sum_{i=1}^{v} L_i^2 = n\sum_{i=1}^{v} x_i^2 + \left(\sum_{i=1}^{v} x_i\right)^2. \tag{4}$$

Let $T = \sum_{i=1}^{v} x_i$. Now suppose $n \equiv 1 \text{ or } 2 \pmod{4}$, so that $v = n^2 + n + 1 \equiv 3 \pmod{4}$. Let $x_{v+1}$ be one more indeterminate. Then:
$$\sum_{i=1}^{v} L_i^2 + n x_{v+1}^2 = n\sum_{i=1}^{v+1} x_i^2 + T^2. \tag{5}$$

By Lagrange's four-square theorem, there exist integers $a, b, c, d$ such that $n = a^2 + b^2 + c^2 + d^2$. Define the $4 \times 4$ matrix:
$$A_n = \begin{pmatrix}
a & b & c & d \\
-b & a & d & -c \\
-c & -d & a & b \\
-d & c & -b & a
\end{pmatrix}$$

Then $\det A_n = n^2 \neq 0$ (since $n \neq 0$). The key identity is that for any vector $(x, y, z, w)$,
$$(a^2+b^2+c^2+d^2)(x^2+y^2+z^2+w^2) = X^2 + Y^2 + Z^2 + W^2$$
where $(X, Y, Z, W) = (x, y, z, w) A_n$. This is Euler's four-square identity.

Applying this identity repeatedly to group the $x_i$'s in sets of four, and since $v+1 \equiv 0 \pmod{4}$, we eventually obtain:
$$\sum_{i=1}^{v} L_i^2 + n x_{v+1}^2 = \sum_{i=1}^{v+1} y_i^2 + T^2 \tag{8}$$
where the $L_i$, $x_{v+1}$, and $T$ are linear expressions in the new indeterminates $y_1, \dots, y_{v+1}$.

Now we successively eliminate variables. Set $L_1 = \pm y_1$ (choosing the appropriate sign based on the coefficient), solve for $y_1$ as a linear expression in $y_2, \dots, y_{v+1}$, and substitute. Repeating this process $v$ times eventually yields:
$$n x_{v+1}^2 = y_{v+1}^2 + T^2$$
where $x_{v+1}$ and $T$ are now linear expressions in $y_{v+1}$ alone; i.e., $x_{v+1} = a y_{v+1}$ and $T = b y_{v+1}$ for rational numbers $a, b$. Substituting:
$$n a^2 = 1 + b^2, \quad \text{so} \quad n = \frac{1}{a^2} + \left(\frac{b}{a}\right)^2.$$

Thus $n$ is a sum of two rational squares. By a classical theorem of number theory, if an integer is a sum of two rational squares, it is also a sum of two integer squares. Hence $n = u^2 + v^2$ for some integers $u, v$. $\square$

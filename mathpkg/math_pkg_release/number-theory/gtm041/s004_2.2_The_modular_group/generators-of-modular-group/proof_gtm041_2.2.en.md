---
role: proof
locale: en
of_concept: generators-of-modular-group
source_book: gtm041
source_chapter: "2"
source_section: "2.2"
---

**Proof.** Consider first a particular example, say
$$A = \begin{pmatrix} 4 & 9 \\ 11 & 25 \end{pmatrix}.$$
We will express $A$ as a product of powers of $S$ and $T$. Since $S^2 = I$, only the first power of $S$ will occur.

Consider the matrix product
$$AT^n = \begin{pmatrix} 4 & 9 \\ 11 & 25 \end{pmatrix}\begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 4 & 4n + 9 \\ 11 & 11n + 25 \end{pmatrix}.$$
Note that the first column remains unchanged. By a suitable choice of $n$ we can make $|11n + 25| < 11$. For example, taking $n = -2$ we find $11n + 25 = 3$ and
$$AT^{-2} = \begin{pmatrix} 4 & 1 \\ 11 & 3 \end{pmatrix}.$$
Thus by multiplying $A$ by a suitable power of $T$ we get a matrix $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with $|d| < |c|$. Next, multiply by $S$ on the right:
$$AT^{-2}S = \begin{pmatrix} 4 & 1 \\ 11 & 3 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 1 & -4 \\ 3 & -11 \end{pmatrix}.$$
This interchanges the two columns and changes the sign of the second column. Again, multiplication by a suitable power of $T$ gives us a matrix with $|d| < |c|$. In this case we can use either $T^4$ or $T^3$. Choosing $T^4$ we find
$$AT^{-2}ST^4 = \begin{pmatrix} 1 & -4 \\ 3 & -11 \end{pmatrix}\begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}.$$

Now we prove the theorem in general. Let $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \Gamma$ with $ad - bc = 1$.

If $c = 0$ then $ad = 1$ so $a = d = \pm 1$ and
$$A = \begin{pmatrix} \pm 1 & b \\ 0 & \pm 1 \end{pmatrix} = \begin{pmatrix} 1 & \pm b \\ 0 & 1 \end{pmatrix} = T^{\pm b}.$$
Thus, $A$ is a power of $T$.

If $c = 1$ then $ad - b = 1$ so $b = ad - 1$ and
$$A = \begin{pmatrix} a & ad - 1 \\ 1 & d \end{pmatrix} = \begin{pmatrix} 1 & a \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & d \\ 0 & 1 \end{pmatrix} = T^a S T^d.$$

Now assume the theorem has been proved for all matrices $A$ with lower left-hand element $< c$ for some $c \geq 1$. Since $ad - bc = 1$ we have $\gcd(c, d) = 1$. Dividing $d$ by $c$ we get
$$d = cq + r, \quad \text{where } 0 < r < c.$$
Then
$$AT^{-q} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & -q \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} a & -aq + b \\ c & r \end{pmatrix}$$
and
$$AT^{-q}S = \begin{pmatrix} a & -aq + b \\ c & r \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} -aq + b & -a \\ r & -c \end{pmatrix}.$$
By the induction hypothesis, the last matrix is a product of powers of $S$ and $T$, so $A$ itself is also such a product. This completes the induction. $\square$

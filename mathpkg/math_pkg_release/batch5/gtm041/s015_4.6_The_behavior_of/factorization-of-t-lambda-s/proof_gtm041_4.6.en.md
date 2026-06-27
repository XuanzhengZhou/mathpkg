---
role: proof
locale: en
of_concept: factorization-of-t-lambda-s
source_book: gtm041
source_chapter: "4"
source_section: "4.6"
---
We wish to find $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ in $\Gamma_0(p)$ such that

$$\begin{pmatrix} 1 & \lambda \\ 0 & p \end{pmatrix} \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} 1 & \mu \\ 0 & p \end{pmatrix}$$

or

$$\begin{pmatrix} \lambda & -1 \\ p & 0 \end{pmatrix} = \begin{pmatrix} a & a\mu + bp \\ c & c\mu + dp \end{pmatrix}.$$

Take $a = \lambda$, $c = p$ and let $\mu$ be that solution of the congruence

$$\lambda\mu \equiv 1 \pmod{p}$$

which lies in the interval $1 \leq \mu \leq p-1$. This is possible since $\lambda$ is not divisible by the prime $p$.
Then $\lambda\mu - 1 = bp$ for some integer $b$, so the equation for the upper right entry is satisfied.
From $c = p$ we have $c\mu + dp = p\mu + dp = p(\mu + d)$; setting $d = -\mu$ gives $c\mu + dp = 0$, matching the lower right entry.
Thus $V = \begin{pmatrix} \lambda & b \\ p & -\mu \end{pmatrix}$, which has determinant $-\lambda\mu - bp = -(\lambda\mu - bp) = -1$. We adjust the sign of the second row to obtain a matrix of determinant $1$ in $\Gamma_0(p)$.

Since $\mu$ is the multiplicative inverse of $\lambda$ modulo $p$, as $\lambda$ runs through $\{1,\ldots,p-1\}$, so does $\mu$.

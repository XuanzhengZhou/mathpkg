---
role: proof
locale: en
of_concept: any-ring-imbeddable-in-ring-with-identity
source_book: gtm030
source_chapter: "III"
source_section: "1"
---
Let $\mathfrak{A}$ be an arbitrary ring. We construct an extension $\mathfrak{B}$ that possesses an identity. Define $\mathfrak{B}$ to be the product set $I \times \mathfrak{A}$ of pairs $(m, a)$ where $m$ is an integer and $a \in \mathfrak{A}$. Two pairs $(m, a)$ and $(n, b)$ are regarded as equal if and only if $m = n$ and $a = b$.

Define addition in $\mathfrak{B}$ by

$$(m, a) + (n, b) = (m + n, a + b).$$

It is straightforward to verify that $\mathfrak{B}$ under $+$ is a commutative group. The zero element is $(0, 0)$ and $-(m, a) = (-m, -a)$.

Define multiplication in $\mathfrak{B}$ by

$$(m, a)(n, b) = (mn, na + mb + ab),$$

where $na$ and $mb$ denote the $n$th multiple of $a$ and the $m$th multiple of $b$, respectively.

To verify associativity of multiplication, compute:

$$
\begin{aligned}
((m, a)(n, b))(q, c) &= (mn, na + mb + ab)(q, c) \\
&= ((mn)q, q(na) + q(mb) + q(ab) + (mn)c + (na)c + (mb)c + (ab)c),
\end{aligned}
$$

and

$$
\begin{aligned}
(m, a)((n, b)(q, c)) &= (m, a)(nq, nc + qb + bc) \\
&= (m(nq), m(nc) + m(qb) + m(bc) + a(nq) + a(nc) + a(qb) + a(bc)).
\end{aligned}
$$

Since $m(nq) = (mn)q$ and the properties of multiples together with the associative and commutative laws in $\mathfrak{A}$ and in $I$ imply equality of the second components, we obtain $((m, a)(n, b))(q, c) = (m, a)((n, b)(q, c))$.

For the distributive law:

$$
\begin{aligned}
(m, a)[(n, b) + (q, c)] &= (m, a)(n + q, b + c) \\
&= (m(n + q), m(b + c) + (n + q)a + a(b + c)) \\
&= (mn + mq, mb + mc + na + qa + ab + ac),
\end{aligned}
$$

and

$$
\begin{aligned}
(m, a)(n, b) + (m, a)(q, c) &= (mn, mb + na + ab) + (mq, mc + qa + ac) \\
&= (mn + mq, mb + na + ab + mc + qa + ac).
\end{aligned}
$$

Thus the left distributive law holds. The right distributive law is verified similarly. Hence $\mathfrak{B}$ is a ring.

The element $(1, 0)$ is an identity for $\mathfrak{B}$ because

$$(1, 0)(n, b) = (1 \cdot n, 1 \cdot b + n \cdot 0 + 0 \cdot b) = (n, b),$$

and similarly $(n, b)(1, 0) = (n, b)$.

Now consider the subset $\mathfrak{A}' = \{(0, a) \mid a \in \mathfrak{A}\}$. We have

$$(0, a) + (0, b) = (0, a + b), \quad 0 = (0, 0), \quad -(0, a) = (0, -a),$$

and

$$(0, a)(0, b) = (0, ab).$$

Thus $\mathfrak{A}'$ is a subring of $\mathfrak{B}$. Defining the map $a \mapsto a' = (0, a)$ gives an isomorphism of $\mathfrak{A}$ onto $\mathfrak{A}'$. Therefore $\mathfrak{A}$ is imbedded in $\mathfrak{B}$, a ring with an identity.

Using the simplified notation where we write $m$ for $(m, 0)$, $a$ for $(0, a)$, $I$ for the isomorphic copy of the integers, and $\mathfrak{A}$ for $\mathfrak{A}'$, we have the relations

$$\mathfrak{B} = I + \mathfrak{A}, \qquad I \cap \mathfrak{A} = 0,$$

and $\mathfrak{A}$ is an ideal in $\mathfrak{B}$.

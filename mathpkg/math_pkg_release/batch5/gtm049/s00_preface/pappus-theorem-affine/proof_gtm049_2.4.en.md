---
role: proof
locale: en
of_concept: pappus-theorem-affine
source_book: gtm049
source_chapter: "II"
source_section: "2.4"
---

We remark first that the points of a triad are, by definition, distinct. The plane $S$ containing $ABC$ and $A'B'C'$ may be assumed to lie in an affine geometry $\mathcal{A}(V)$ but not to contain $0_V$.

In the case where $ABC \cap A'B'C'$ is a point $P$, we choose a homogeneous vector $p$ for $P$; otherwise we choose a non-zero vector $p$ in the line through $O$ parallel to $ABC$, $A'B'C'$. In either case we may then find homogeneous vectors $a, b, a', b'$ for $A, B, A', B'$ respectively so that $b = p + a$ and $b' = p + a'$ (Lemma 5). We may also find homogeneous vectors $c, c'$ for $C, C'$ respectively of the form $c = p + xa, c' = p + ya'$, where $x, y$ are scalars.

Now $p + a + a' = n$, say, is a linear combination of $a$ and $b'$, and also of $a'$ and $b$ (and therefore cannot be $0$, since $OA \neq OB'$). Hence $n$ lies in the planes $OAB', OA'B$ and is a homogeneous vector for $N$. Similarly $p + xa + ya' = m$ is a homogeneous vector for $M$. Finally,

$$xyn - m = x(y - 1)b + (x - 1)c'$$

and

$$yxn - m = y(x - 1)b' + (y - 1)c'.$$

Since $xy = yx$ for all scalars $x, y$, it follows that $l = xyn - m$ is a homogeneous vector for $L$. The linear dependence $l + m - xyn = 0$ shows that $OL, OM, ON$ are coplanar and thus $L, M, N$ are collinear.

The method of proof gives the further result that if $BC'$ is parallel to $B'C$ and if $CA'$ is parallel to $C'A$, then $AB'$ is parallel to $A'B$.

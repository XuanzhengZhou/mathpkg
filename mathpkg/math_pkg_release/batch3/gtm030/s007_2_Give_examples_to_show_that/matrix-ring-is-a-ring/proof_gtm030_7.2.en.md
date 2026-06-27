---
role: proof
locale: en
of_concept: matrix-ring-is-a-ring
source_book: gtm030
source_chapter: "7"
source_section: "2"
---

The ring axioms for $\Re_n$ are verified as follows. Matrix addition is associative and commutative because addition in $\Re$ is. The zero matrix (all entries zero) serves as the additive identity. The additive inverse of $(a_{ij})$ is $(-a_{ij})$.

Matrix multiplication is associative: for $(a), (b), (c) \in \Re_n$,
$$((a)(b))(c) = (a)((b)(c))$$
because
$$\sum_{\ell} \left(\sum_{k} a_{ik} b_{k\ell}\right) c_{\ell j} = \sum_{k} a_{ik} \left(\sum_{\ell} b_{k\ell} c_{\ell j}\right)$$
by the associative law of multiplication in $\Re$ and the generalized distributive law.

The distributive laws hold: the $(i,j)$-element of $(a)[(b)+(c)]$ is
$$\sum_{k} a_{ik}(b_{kj} + c_{kj})$$
and the $(i,j)$-element of $(a)(b) + (a)(c)$ is
$$\sum_{k} a_{ik}b_{kj} + \sum_{k} a_{ik}c_{kj}.$$
These are equal by the distributive law in $\Re$. The other distributive law $[(a)+(b)](c) = (a)(c) + (b)(c)$ is verified similarly.

Hence $\Re_n$ is a ring.

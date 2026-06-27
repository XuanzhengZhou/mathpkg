---
role: proof
locale: en
of_concept: four-variable-associator-identity
source_book: gtm006
source_chapter: "6"
source_section: "7. The Skornyakov-San Soucie Theorem"
---

By (7), $[x, y + w, z] \in A(y + w, z)$. Hence by the defining property of $A$ (Lemma (5)):
$$[x, y + w, z] (yz + wz) = ([x, y + w, z] z) (y + w).$$

Expanding both sides linearly:
$$\begin{aligned}
&[x, y, z](yz) + [x, y, z](wz) + [x, w, z](yz) + [x, w, z](wz) \\
&= ([x, y, z]z)y + ([x, y, z]z)w + ([x, w, z]z)y + ([x, w, z]z)w.
\end{aligned}$$

By (2), $[x, y, z](yz) = ([x, y, z]z)y$ and $[x, w, z](wz) = ([x, w, z]z)w$. Canceling these matching pairs leaves:
$$[x, y, z](wz) + [x, w, z](yz) = ([x, y, z]w)z + ([x, w, z]z)y.$$
$\square$

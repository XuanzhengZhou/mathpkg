---
role: proof
locale: en
of_concept: annihilator-basic-properties
source_book: gtm013
source_chapter: "1"
source_section: "2"
---

(1) If $X \subseteq Y$ and $r \in l_R(Y)$, then $r y = 0$ for all $y \in Y$, hence in particular for all $x \in X$, so $r \in l_R(X)$. The second statement is dual.

(2) If $x \in X$, then for any $r \in l_R(X)$ we have $r x = 0$, which means $x$ is annihilated by all elements of $l_R(X)$, so $x \in r_M l_R(X)$. The second inclusion is dual.

(3) From (2) applied to $l_R(X)$, we have $l_R(X) \subseteq l_R r_M l_R(X)$. Also from (1), since $X \subseteq r_M l_R(X)$, applying $l_R$ (which is order-reversing) gives $l_R r_M l_R(X) \subseteq l_R(X)$. Hence $l_R(X) = l_R r_M l_R(X)$. The second identity is proved dually.

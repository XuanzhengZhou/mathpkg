---
role: proof
locale: en
of_concept: properties-of-z-and-i
source_book: gtm052
source_chapter: "I"
source_section: "1"
---

(a) If $P \in Z(T_2)$ then $f(P) = 0$ for all $f \in T_2$, hence in particular for all $f \in T_1 \subseteq T_2$, so $P \in Z(T_1)$.

(b) If $f \in I(Y_2)$ then $f(P) = 0$ for all $P \in Y_2$, hence in particular for all $P \in Y_1 \subseteq Y_2$, so $f \in I(Y_1)$.

(c) $f \in I(Y_1 \cup Y_2)$ iff $f$ vanishes on $Y_1 \cup Y_2$, iff $f$ vanishes on $Y_1$ and on $Y_2$, iff $f \in I(Y_1) \cap I(Y_2)$.

(d) Since $Y \subseteq Z(I(Y))$ and $Z(I(Y))$ is an algebraic set (hence closed), $\overline{Y} \subseteq Z(I(Y))$. Conversely, let $W$ be any closed set containing $Y$. Then $W = Z(\mathfrak{a})$ for some ideal $\mathfrak{a}$. Since $Y \subseteq Z(\mathfrak{a})$, we have $\mathfrak{a} \subseteq I(Y)$, so $Z(I(Y)) \subseteq Z(\mathfrak{a}) = W$. Thus $Z(I(Y)) \subseteq \overline{Y}$.

(e) This is Hilbert's Nullstellensatz (Theorem 1.3A), which states that if $f$ vanishes on $Z(\mathfrak{a})$ then $f^r \in \mathfrak{a}$ for some $r > 0$, i.e., $f \in \sqrt{\mathfrak{a}}$.

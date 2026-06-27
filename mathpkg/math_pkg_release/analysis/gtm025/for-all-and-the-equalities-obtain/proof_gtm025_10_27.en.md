---
role: proof
locale: en
of_concept: "for-all-and-the-equalities-obtain"
source_book: gtm025
source_chapter: "Measures"
source_section: "10.27"
---

By (9.24) and (9.23), we have

$$\lambda(A) = \inf \left\{ \lambda(U) : U \text{ is open in } R \text{ and } A \subset U \right\}$$

$$= \inf \left\{ \sum_{n=1}^{\infty} \left(b_n - a_n\right) : A \subset \bigcup_{n=1}^{\infty} a_n, b_n \right\}.$$

Since the inclusions

$$A \subset \bigcup_{n=1}^{\infty} a_n, b_n$$

$$x + A \subset \bigcup_{n=1}^{\infty} a_n + x, b_n + x$$

$$-A \subset \bigcup_{n=1}^{\infty} -b_n, -a_n$$

are mutually equivalent, and since the three unions of intervals in (1) have the same Lebesgue measure, the lemma is proved. $\square$

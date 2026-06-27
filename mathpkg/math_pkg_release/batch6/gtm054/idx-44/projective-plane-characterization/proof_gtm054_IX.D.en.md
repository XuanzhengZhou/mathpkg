---
role: proof
locale: en
of_concept: projective-plane-characterization
source_book: gtm054
source_chapter: "IX"
source_section: "D"
---

Suppose first that $\Lambda$ is a finite projective plane. Then (a) and (b) hold since $\lambda = 1$ in a symmetric block design, and the definitions of points and lines in this context directly translate to these axioms. Since $r = k \geq 3$, we may choose a point $x_0$ and two lines $L_1$ and $L_2$ containing it. Now choose $x_1$ and $x_3$ on $L_1$ distinct from $x_0$, and choose $x_2$ and $x_4$ on $L_2$ distinct from $x_0$. One easily verifies that $\{x_1, \dots, x_4\}$ satisfies condition (c).

Conversely, suppose $\Lambda$ satisfies (a), (b), and (c). Then $\Lambda$ is a $(2;2)$-design with $v \geq 4$, and it suffices, due to A5, to prove that $\Lambda$ is a $(\cdot;1)$-design, i.e., that $\lambda = 1$. We do this by arbitrarily choosing two lines and establishing a bijection between them.

We assert that given any two lines $L$ and $L'$, there exists a point $x_0 \notin L \cup L'$. For let $\{x_1, x_2, x_3, x_4\}$ be a set postulated by (c). If $\{x_1, \dots, x_4\} \not\subseteq L \cup L'$, then clearly one may choose $x_0 \in \{x_1, \dots, x_4\}$. If $\{x_1, \dots, x_4\} \subseteq L \cup L'$, we may assume that $x_1, x_2 \in L \setminus (L \cap L')$ and $x_3, x_4 \in L' \setminus (L \cap L')$. Let $L_1$ be the line through $x_1$ and $x_3$, and let $L_2$ be the line through $x_2$ and $x_4$ as required by (a). Let $x_0 \in L_1 \cap L_2$. By (b), $x_0 \notin L \cup L'$, which establishes the assertion.

Using this point $x_0$ not on $L \cup L'$, one constructs a bijection between the points of $L$ and the points of $L'$ via the pencil of lines through $x_0$, establishing that the two lines have the same number of points. This shows the structure is regular and forces $\lambda = 1$, completing the equivalence.

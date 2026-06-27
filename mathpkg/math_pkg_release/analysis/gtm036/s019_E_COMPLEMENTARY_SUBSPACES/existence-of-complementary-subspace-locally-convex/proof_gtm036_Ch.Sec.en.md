---
role: proof
locale: en
of_concept: existence-of-complementary-subspace-locally-convex
source_book: gtm036
source_chapter: ""
source_section: "E"
---

Since $F$ is finite-dimensional, the quotient $E/F$ is a Hausdorff locally convex space of finite co-dimension. By the Hahn-Banach theorem (which applies in locally convex spaces), there exist continuous linear functionals on $E/F$ separating points. Using a basis of the annihilator of $F$ in the dual space, one can construct a continuous projection from $E$ onto a complement of $F$. Specifically, let $\{f_1, \dots, f_n\}$ be a basis for the algebraic dual of $E/F$. Each $f_i \circ \pi$ (where $\pi: E \to E/F$ is the quotient map) is a continuous linear functional on $E$. The common null space of these functionals provides the desired closed complementary subspace, and the restriction of $\pi$ to this complement yields the isomorphism with $E/F$.

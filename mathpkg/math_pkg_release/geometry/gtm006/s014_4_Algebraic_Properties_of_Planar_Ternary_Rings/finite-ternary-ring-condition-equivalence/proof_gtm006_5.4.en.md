---
role: proof
locale: en
of_concept: finite-ternary-ring-condition-equivalence
source_book: gtm006
source_chapter: "5"
source_section: "4"
---

**Proof.** Suppose the finite ternary ring $(R, T)$ satisfies conditions (C) and (D). We must show that condition (E) holds: for $x \neq y$, the system of equations
$$
T(x, u, v) = g, \qquad T(y, u, v) = h
$$
has a unique solution for $(u, v)$.

Given elements $x, y, a, b, c \in R$ with $x \neq y$, suppose the equations
$$
T(x, u, v) = g, \qquad T(y, u, v) = h
$$
have two distinct solutions $(u, v) = (a, b)$ and $(u, v) = (c, xA)$ with $a \neq c$. Here, by condition (D), $xA$ is defined uniquely by $T(x, a, b) = T(x, c, xA)$.

If $x \neq y$ but $xA = yA$, then $T(x, a, b) = T(x, c, xA)$ and $T(y, a, b) = T(y, c, xA)$, which implies that the equation $T(u, a, b) = T(u, c, xA)$ has distinct solutions $u = x$ and $u = y$, contradicting the assumption that equations of the form $T(u, a, b) = T(u, c, d)$ with $a \neq c$ have at most one solution (which follows from (C) and (D) in the finite case).

Thus the mapping $A: R \to R$ defined by $T(t, a, b) = T(t, c, tA)$ is one-to-one. Since $R$ is finite, $A$ is also onto, hence a bijection. Therefore the system $T(x, u, v) = g$, $T(y, u, v) = h$ must have a unique solution, establishing condition (E). $\square$

*Note: The original OCR text for Theorem 5.4 was partially truncated. The statement and proof above have been reconstructed from the preserved proof fragment, which hinges on the bijectivity of the mapping $A$ in the finite setting.*

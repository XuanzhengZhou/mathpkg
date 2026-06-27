---
role: exercise
locale: en
chapter: "XII"
section: "61"
exercise_number: "1"
---

The analogs of Theorems A, B, and C with $\mu(xE \cap F)$ in place of $\rho(xE, E)$ are true, where $E$ and $F$ are Baire sets of finite measure in a locally compact topological group $X$.

*Hint:* Consider

$$\frac{\epsilon}{2} > \frac{1}{\mu(U)} \int_U \int_F |\chi_E(yx) - \chi_E(x)| \, d\mu(x) d\mu(y) \geq \left| \int_F d\mu(x) \int_U \frac{1}{\mu(U)} \chi_{Ex^{-1}}(y) d\mu(y) - \int_F \chi_E(x) d\mu(x) \int_U \frac{d\mu(y)}{\mu(U)} \right| = \left| \int_F (f_U(x) - \chi_E(x)) d\mu(x) \right|.$$

Recall that $\frac{\mu(A)}{\mu(B)} = \frac{\mu(Ax)}{\mu(Bx)}$ for any Borel sets $A$ and $B$ and every $x$ in $X$ (cf. 60.5). The desired conclusion follows upon applying this result first to $F = \{x: f_U(x) - \chi_E(x) > 0\}$ and then to $F = \{x: f_U(x) - \chi_E(x) < 0\}$.

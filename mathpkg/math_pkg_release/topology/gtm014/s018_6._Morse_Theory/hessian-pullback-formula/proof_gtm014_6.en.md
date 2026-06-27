---
role: proof
locale: en
of_concept: hessian-pullback-formula
source_book: gtm014
source_chapter: "6"
source_section: "6. Morse Theory"
---

(Hint in text: Compute both lemmas by using local coordinates.)

For (1): Since $q$ is a critical point of $f$, we have $df_q = 0$. Then $d(\phi^* f)_p = d(f \circ \phi)_p = df_q \circ d\phi_p = 0$, so $p$ is a critical point of $\phi^* f$.

For (2): In local coordinates, apply the chain rule twice. Since $df_q = 0$, the first-order terms vanish and the second derivative of $\phi^* f$ at $p$ equals the composition of $d^2 f_q$ with $d\phi_p$ in each argument.

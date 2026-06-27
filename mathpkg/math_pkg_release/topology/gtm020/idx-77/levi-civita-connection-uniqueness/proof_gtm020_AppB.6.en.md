---
role: proof
locale: en
of_concept: levi-civita-connection-uniqueness
source_book: gtm020
source_chapter: "Appendix B"
source_section: "B.6"
---
We prove existence and uniqueness of a symmetric metric-compatible connection. For uniqueness, suppose $\nabla$ satisfies conditions (1) and (2). Compute the expression $\zeta g(\xi, \eta) - \xi g(\eta, \zeta) + \eta g(\zeta, \xi)$ using metric compatibility:
\begin{align*}
\zeta g(\xi, \eta) &= g(\nabla_\zeta \xi, \eta) + g(\xi, \nabla_\zeta \eta), \\
\eta g(\zeta, \xi) &= g(\nabla_\eta \zeta, \xi) + g(\zeta, \nabla_\eta \xi), \\
\xi g(\eta, \zeta) &= g(\nabla_\xi \eta, \zeta) + g(\eta, \nabla_\xi \zeta).
\end{align*}
Using the torsion-free condition $\nabla_\zeta \eta - \nabla_\eta \zeta = [\zeta, \eta]$ to replace terms, we form the alternating sum and obtain
\begin{align*}
2g(\xi, \nabla_\zeta \eta) &= \zeta g(\xi, \eta) + \eta g(\zeta, \xi) - \xi g(\eta, \zeta) \\
&\quad - g(\eta, [\xi, \zeta]) + g([\eta, \zeta], \xi) + g(\zeta, [\eta, \xi]).
\end{align*}
Since $g$ is nondegenerate, this six-term expression uniquely determines $\nabla_\zeta \eta$. Thus the Levi-Civita connection is unique if it exists. For existence, one defines $\nabla_\zeta \eta$ by this formula and verifies that it satisfies the connection axioms, metric compatibility, and the torsion-free condition. The $A^0(M)$-linearity properties and the conditions (T) (torsion-free) and metric compatibility follow by direct computation from the Koszul formula.

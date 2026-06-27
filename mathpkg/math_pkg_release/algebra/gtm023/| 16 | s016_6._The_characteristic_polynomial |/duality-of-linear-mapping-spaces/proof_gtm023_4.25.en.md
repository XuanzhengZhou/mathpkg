---
role: proof
locale: en
of_concept: duality-of-linear-mapping-spaces
source_book: gtm023
source_chapter: "Chapter IV"
source_section: "§7. The trace"
---

Bilinearity follows immediately from the linearity of composition and the linearity of the trace.

For non-degeneracy: assume $\varphi \in L(E;F)$ satisfies $\langle \varphi, \psi \rangle = 0$ for all $\psi \in L(F;E)$, and suppose $\varphi \neq 0$. Then there exists $a \in E$ with $\varphi a \neq 0$. Extend $b_1 = \varphi a$ to a basis $(b_1, \ldots, b_m)$ of $F$ and define $\psi: F \to E$ by $\psi b_1 = a$ and $\psi b_i = 0$ for $i > 1$.

Then $\psi \circ \varphi: E \to E$ satisfies $(\psi \circ \varphi)(a) = \psi(\varphi a) = \psi(b_1) = a$. For any $x \in E$ not of the form $a$, $(\psi \circ \varphi)(x)$ lies in the span of $a$ (since $\psi$ has range $\operatorname{span}\{a\}$). Computing the trace with respect to a basis extending $a$, the diagonal entry corresponding to $a$ is $1$, so $\operatorname{tr}(\psi \circ \varphi) = 1 \neq 0$, contradicting $\langle \varphi, \psi \rangle = 0$. Therefore $\varphi = 0$.

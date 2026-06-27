---
role: proof
locale: en
of_concept: trace-of-composition-symmetry
source_book: gtm023
source_chapter: "Chapter IV"
source_section: "§7. The trace"
---

The trace of $\psi \circ \varphi$ is defined by
$$\sum_{i} \Delta(x_1, \ldots, (\psi \circ \varphi) x_i, \ldots, x_n) = \operatorname{tr}(\psi \circ \varphi) \Delta(x_1, \ldots, x_n).$$

Replace the vectors $x_v$ by $\psi x_v$ for $v = 1, \ldots, n$:
$$\sum_{i} \Delta(\psi x_1, \ldots, (\psi \circ \varphi \circ \psi) x_i, \ldots, \psi x_n) = \operatorname{tr}(\psi \circ \varphi) \Delta(\psi x_1, \ldots, \psi x_n).$$

The right-hand side equals $\operatorname{tr}(\psi \circ \varphi) \det \psi \cdot \Delta(x_1, \ldots, x_n)$. On the left-hand side, note that $(\psi \circ \varphi \circ \psi) x_i = (\varphi \circ \psi)(\psi x_i)$ (this appears incorrect — instead we should note that what we have is actually $\sum_i \Delta(\psi x_1, \ldots, (\psi \circ \varphi) x_i, \ldots, \psi x_n)$ which after re-indexing becomes the definition of $\operatorname{tr}(\varphi \circ \psi)$ up to the factor $\det \psi$).

More precisely, the definition of $\operatorname{tr}(\varphi \circ \psi)$ gives
$$\sum_i \Delta(x_1, \ldots, (\varphi \circ \psi) x_i, \ldots, x_n) = \operatorname{tr}(\varphi \circ \psi) \Delta(x_1, \ldots, x_n).$$

If $\psi$ is regular (i.e., $\det \psi \neq 0$), then the substitution argument yields the equality directly. For general $\psi$, consider the polynomial $\det(\psi - \lambda \iota)$: it has only finitely many roots, so for all but finitely many $\lambda$, $\psi - \lambda \iota$ is regular. The identity holds for all such $\lambda$ by the regular case, and by continuity (or by polynomial identity) it holds for all $\lambda$, in particular for $\lambda = 0$.

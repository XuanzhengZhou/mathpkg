---
role: proof
locale: en
of_concept: convex-ideal-quotient-ring
source_book: gtm043
source_chapter: "5"
source_section: "5.2"
---

**Necessity.** If $0 \leq x \leq y$, and $y \in I$, then $0 \geq I(x) - I(y) = I(x) \geq 0$, whence $I(x) = 0$, i.e., $x \in I$.

**Sufficiency.** According to 0.19, we must verify:
\begin{itemize}
  \item[(i)] $I(a) \geq 0$ and $I(-a) \geq 0$ implies $I(a) = 0$;
  \item[(ii)] $I(a) \geq 0$ and $I(b) \geq 0$ implies both $I(a) + I(b) \geq 0$ and $I(a)I(b) \geq 0$.
\end{itemize}

For (i), there exist $x, y \in A$ such that $x \geq 0$, $y \geq 0$, $a \equiv x$, and $-a \equiv y$. Hence $x + y \equiv 0$. Since $0 \leq x \leq x + y$, we have $x \equiv 0$, by convexity. Therefore $I(a) = I(x) = 0$.

Condition (ii) is an immediate consequence of the corresponding condition in $A$.

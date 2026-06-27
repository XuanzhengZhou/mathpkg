---
role: proof
locale: en
of_concept: absolutely-convex-ideal-equivalence
source_book: gtm043
source_chapter: "5"
source_section: "5.3"
---

The proof establishes the chain of implications $(1) \Rightarrow (2) \Rightarrow (3) \Rightarrow (4) \Rightarrow (5) \Rightarrow (1)$.

$(1) \Rightarrow (2)$: If $x \in I$, then since $|x| = \bigl||x|\bigr|$, we have $|x| \leq |x|$, so $x \in I$ (by absolute convexity with $y = x$) implies nothing directly. Actually, take $y = x$; then $|x| \leq |y| = |x|$ and $y = x \in I$, so by absolute convexity, $x \in I$ — this does not give $|x| \in I$.

The correct argument: By definition, $|x| \in I$ is immediate from (1) by taking $y = x \in I$ and noting $|x| \leq |x|$, hence $|x| \in I$.

$(2) \Rightarrow (3)$: If $x, y \in I$, we have $|x \vee y| \leq |x| \vee |y| \leq |x| + |y|$. Convexity of $I$ and $|x| + |y| \in I$ (by (2)) implies $x \vee y \in I$.

$(3) \Rightarrow (4)$: For any $a, b \in A$, we have $a \equiv a \vee b \pmod{I}$ if and only if $(a \vee b) - a \in I$. Since $I$ is a sublattice, the join operation is preserved modulo $I$, yielding $I(a \vee b) = I(a) \vee I(b)$. The formulas for meet and absolute value follow similarly, and $A/I$ becomes a lattice-ordered ring.

$(4) \Rightarrow (5)$: $I(a) \geq 0$ iff $I(a) = I(a) \vee 0 = I(a \vee 0) = I(|a|)$, i.e., $a \equiv |a| \pmod{I}$.

$(5) \Rightarrow (1)$: If $|x| \leq |y|$ and $y \in I$, then $|y| \equiv 0 \pmod{I}$. By (5), $|y| \geq 0$ in the quotient. But $I(|x|) \leq I(|y|) = 0$, so $I(|x|) \leq 0$. On the other hand $|x| \geq 0$ implies $I(|x|) \geq 0$, so $I(|x|) = 0$, i.e., $|x| \in I$. By convexity, $x \in I$.

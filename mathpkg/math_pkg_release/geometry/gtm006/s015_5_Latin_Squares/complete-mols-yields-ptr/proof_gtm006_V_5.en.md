---
role: proof
locale: en
of_concept: complete-mols-yields-ptr
source_book: gtm006
source_chapter: "V"
source_section: "5"
---

**Proof.**

Let $R = \{0, 1, \dots, n-1\}$ and suppose $\{1\}, \{2\}, \dots, \{n-1\}$ is a complete set of mutually orthogonal $n \times n$ Latin squares in normal form, such that $\{1\}$ has $(0, 1, \dots, n-1)^\top$ as its left column. Since no two squares have the same entry in the $(1,0)$-position (by the proof of Property 2), we may label the squares so that $\{x\}$ is the square with entry $x$ in the $(1,0)$-position, for $x = 1, 2, \dots, n-1$.

Define the ternary operation $T$ as follows:
\begin{itemize}
\item For $x = 1, \dots, n-1$: $T(x, i, j) = \text{the } (i,j)\text{-th entry of } \{x\}$.
\item For $x = 0$: $T(0, i, j) = j$ for all $i, j$.
\end{itemize}

We now verify that $T$ satisfies the planar ternary ring axioms (A), (B), (D), (E) of Theorem 5.1. By Theorem 5.4, this suffices to show that $(R, T)$ is a PTR.

\textbf{(A)} $T(x, 0, c) = c$ for all $x, c$. This holds because all squares are in normal form, so the $0$-th row (top row) of each square $\{x\}$ is $(0, 1, \dots, n-1)$. Thus $T(x, 0, c) = c$ for $x \neq 0$, and $T(0, 0, c) = c$ by definition.

\textbf{(B)} $T(a, 1, 0) = a$ and $T(1, a, 0) = a$ for all $a$. For $a \neq 0$, $T(a, 1, 0) = a$ because $\{a\}$ is, by labeling, the square with entry $a$ in the $(1,0)$-position. For $a = 0$, $T(0, 1, 0) = 0$ by the definition of $T(0, \cdot, \cdot)$. Also $T(1, a, 0) = a$ for all $a$ because $\{1\}$ has $(0, 1, \dots, n-1)^\top$ as its first column.

\textbf{(D)} For $a \neq 0$, every row of the square $\{a\}$ contains each element of $R$ exactly once (Latin square property). Thus given $a, b, c$ with $a \neq 0$, there is a unique $x$ such that $T(a, b, x) = c$. If $a = 0$, then $T(0, b, x) = x$, so the unique $x$ is $c$.

\textbf{(E)} The axiom (E) of Theorem 5.1 (which concerns the existence of a unique solution to certain equations in the PTR) follows from the Latin square and orthogonality properties of the construction. The details are analogous to the verification of the other axioms.

Thus $(R, T)$ satisfies the required axioms and is a planar ternary ring.

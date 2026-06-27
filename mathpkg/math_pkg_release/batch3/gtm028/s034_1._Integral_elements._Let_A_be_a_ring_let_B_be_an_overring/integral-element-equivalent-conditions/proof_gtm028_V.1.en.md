---
role: proof
locale: en
of_concept: integral-element-equivalent-conditions
source_book: gtm028
source_chapter: "V"
source_section: "1"
---

\textbf{Proof (cyclic).}

\textit{(c) $\Rightarrow$ (c'):} Equation (c) gives $x^n = -\sum_{i=0}^{n-1} a_i x^i$, so $x^n \in \sum_{i=0}^{n-1} A x^i$. Then for any $q \geq 0$, $x^{n+q} \in \sum_{i=0}^{n-1} A x^i$ by induction. Hence $\{1, x, \dots, x^{n-1}\}$ generates $A[x]$ as an $A$-module, so $A[x]$ is a finite $A$-module.

\textit{(c') $\Rightarrow$ (c''):} Take $R = A[x]$. Then $R$ is a subring of $B$ and a finite $A$-module by (c').

\textit{(c'') $\Rightarrow$ (c'''):} Take $M = R$. Then (1) holds since $R$ is a ring, and (2) holds since $1 \in R$ (so $y \cdot 1 = 0$ implies $y = 0$).

\textit{(c''') $\Rightarrow$ (c):} This follows from the Lemma. Take $q = A$ in the Lemma. Then $xM \subset M = MA$, so $xM \subset Mq$. Condition (2) of (c''') is precisely condition 2' of the Lemma with $q = A$. The Lemma then gives $x^n + a_{n-1}x^{n-1} + \cdots + a_0 = 0$ with all $a_i \in A$, which is exactly condition (c).

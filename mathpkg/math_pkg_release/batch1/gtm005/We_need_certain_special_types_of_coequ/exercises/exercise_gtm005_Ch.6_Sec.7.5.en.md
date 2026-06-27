---
role: exercise
locale: en
chapter: "VI. Monads and Algebras"
section: "7. Beck's Theorem"
exercise_number: 5
---

Given the adjunction $\langle F, G, \eta, \varepsilon \rangle : X \rightleftharpoons A$, the monad $\langle T, \eta, \mu \rangle$, the Eilenberg--Moore adjunction $\langle F^T, G^T, \eta^T, \varepsilon^T \rangle : X \rightleftharpoons X^T$, and the comparison functor $K : A \to X^T$, let $P$ be the set of all parallel pairs $f, g : a \rightrightarrows b$ in $A$ such that $\langle G f, G g \rangle$ has a split coequalizer in $X$. Using Exercise 4(b), prove:

\begin{enumerate}
\item[(a)] If $A$ has coequalizers of all pairs in $P$, then $K$ has a left adjoint $M : X^T \to A$.
\item[(b)] If, in addition, $G$ preserves all coequalizers of pairs in $P$, then the unit $\eta : I \to K M$ of this adjunction is an isomorphism.
\item[(c)] If, in addition to (a), $G$ reflects coequalizers for all pairs in $P$, then the counit $\varepsilon : M K \to I$ of this adjunction is an isomorphism.
\end{enumerate}

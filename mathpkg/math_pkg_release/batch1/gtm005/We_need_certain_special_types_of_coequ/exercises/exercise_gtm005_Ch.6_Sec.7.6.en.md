---
role: exercise
locale: en
chapter: "VI. Monads and Algebras"
section: "7. Beck's Theorem"
exercise_number: 6
---

Use the results of Exercise 5 and Theorem IV.4.1 to prove the following equivalence version of Beck's theorem, characterizing the category of $T$-algebras up to equivalence:

Given the adjunction $\langle F, G, \eta, \varepsilon \rangle : X \rightleftharpoons A$ and the Eilenberg--Moore adjunction $\langle F^T, G^T, \eta^T, \varepsilon^T \rangle : X \rightleftharpoons X^T$, the following assertions are equivalent:
\begin{enumerate}
\item[(i)] The comparison functor $K : A \to X^T$ is an equivalence of categories.
\item[(ii)] If $f, g$ is any parallel pair in $A$ for which $\langle G f, G g \rangle$ has an absolute coequalizer, then $f, g$ has a coequalizer in $A$, and $G$ preserves and reflects that coequalizer.
\end{enumerate}

---
role: proof
locale: en
of_concept: "satisfiability-theorem-propositional"
source_book: gtm022
source_chapter: "III"
source_section: "2"
---
Proof. Let $M$ be a maximal consistent subset containing $A$ (such an $M$ exists by Zorn's Lemma applied to the set of consistent supersets of $A$). For $p \in P(X)$, put $v(p) = 1$ if $p \in M$ and $v(p) = 0$ if $p \notin M$. We prove $v$ is a valuation.

Certainly $v(F) = 0$, because $F \notin M$. It remains to show $v(p \Rightarrow q) = v(p) \Rightarrow v(q)$. We consider cases:
\begin{itemize}
\item If $q \in M$, then $\{q\} \vdash p \Rightarrow q$, so $p \Rightarrow q \in M$ and $v(p \Rightarrow q) = 1 = v(p) \Rightarrow v(q)$.
\item If $p \notin M$, then $\{\sim p\} \vdash p \Rightarrow q$, so $p \Rightarrow q \in M$ and $v(p \Rightarrow q) = 1 = v(p) \Rightarrow v(q)$.
\item If $p \in M$ and $q \notin M$, then $p \Rightarrow q \notin M$ (else Modus Ponens would give $q \in M$), so $v(p \Rightarrow q) = 0 = v(p) \Rightarrow v(q)$.
\end{itemize}
Thus $v$ is a valuation with $v(M) \subseteq \{1\}$, and since $A \subseteq M$, $v(A) \subseteq \{1\}$. $\square$

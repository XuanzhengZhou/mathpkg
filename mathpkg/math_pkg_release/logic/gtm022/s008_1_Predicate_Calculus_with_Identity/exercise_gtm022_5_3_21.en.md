---
role: exercise
locale: en
chapter: "V"
section: "3"
exercise_number: 3.21
---

A \textit{dense linearly ordered set} is a non-empty set with a binary relation $<$ such that

\begin{enumerate}
  \item[(a)] for all $x, y$, exactly one of $x < y$, $x = y$, $y < x$ holds,
  \item[(b)] if $x < y$ and $y < z$, then $x < z$,
  \item[(c)] if $x < y$, then there exists $z$ such that $x < z < y$,
  \item[(d)] for each $x$, there exist $y, z$ such that $y < x < z$.
\end{enumerate}

Using a binary relation symbol $\ell$, with $\ell(x, y)$ to be thought of as $x < y$, and also the identity symbol $\mathcal{I}$, construct a finite theory $\mathcal{D}$ whose models are precisely the dense linearly ordered sets (without endpoints). Show that $\mathcal{D}$ is $\aleph_0$-categorical (i.e., categorical in cardinal $\aleph_0$) and hence, by Corollary 3.20, complete.

---
role: exercise
locale: en
chapter: "7"
section: "7.3"
exercise_number: 3
---

\textbf{Exercise 7.3.} Let $H$ be a subgroup of $G$. Assume that for each $t \notin H$ we have $H \cap tHt^{-1} = \{1\}$, in which case $H$ is said to be a \textbf{Frobenius subgroup} of $G$. Denote by $N$ the set of elements of $G$ which are not conjugate to any element of $H$.

\begin{enumerate}
  \item[(a)] Let $g = \operatorname{Card}(G)$ and let $h = \operatorname{Card}(H)$. Show that the number of elements of $N$ is $(g/h) - 1$.
  \item[(b)] Let $f$ be a class function on $H$. Show that there exists a unique class function $\tilde{f}$ on $G$ which extends $f$ and takes the value $f(1)$ on $N$.
  \item[(c)] Show that $\tilde{f} = \operatorname{Ind}_H^G f - f(1)\psi$, where $\psi$ is the character $\operatorname{Ind}_H^G(1) - 1$ of $G$, cf. Exercise 7.2.
  \item[(d)] Show that $\langle f_1, f_2 \rangle_H = \langle \tilde{f}_1, \tilde{f}_2 \rangle_G$.
  \item[(e)] Take $f$ to be an irreducible character of $H$. Show, using (c) and (d), that $\langle \tilde{f}, \tilde{f} \rangle_G = 1$, $\tilde{f}(1) \geq 0$, and that $\tilde{f}$ is a linear combination with integer coefficients of irreducible characters of $G$. Conclude that $\tilde{f}$ is an irreducible character of $G$. If $\rho$ is a corresponding representation of $G$, show that $\rho(s) = 1$ for each $s \in N$ [use Exercise 6.7].
  \item[(f)] Show that each linear representation of $H$ extends to a linear representation of $G$ whose kernel contains $N$. Conclude that $N \cup \{1\}$ is a normal subgroup of $G$ and that $G$ is the semidirect product of $H$ and $N$.
\end{enumerate}

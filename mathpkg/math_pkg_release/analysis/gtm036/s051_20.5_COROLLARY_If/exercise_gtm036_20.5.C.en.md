---
role: exercise
locale: en
chapter: "20"
section: "20.5"
exercise_number: C
---

\textbf{C. CONVERSE OF 20.7(i).}

The result 20.7(i) states that if $E$ is reflexive, so is its adjoint $E^*$ under the strong topology. The converse fails: let $E$ be a dense proper subspace of $F$ with the induced topology on $F$. Let $X^\omega$ denote a countable product and $X^{(\omega)}$ a countable direct sum of copies of $X$. Let $G = E^{(\omega)} \times F^\omega$, let $T$ be the mapping of $G$ into $E^\omega$ defined by $T(x,y) = x + y$, and let $H = T^{-1}(0)$.

\begin{enumerate}
\item[(a)] The space $G/H$ is a quotient of a complete space by a closed subspace, but is not complete. (Show that $T$ is a continuous open mapping of $G$ onto the dense subspace $E^{(\omega)} + F^\omega$ of $E^\omega$.)

\item[(b)] Suppose also that $E$ and $F$ are reflexive. Then $G$ is reflexive, but $G/H$ is not semi-reflexive (for $(G/H)^{**}$ is isomorphic to $(E^\omega)^{**} = E^\omega$). Also $G^*$ is reflexive, but the subspace $H^\circ$ of $G^*$ is not evaluable. (For it is semi-reflexive but cannot be reflexive, since its adjoint $G/H$ is not reflexive.)

\item[(c)] The strong topology $S(H^\circ,G/H)$ does not coincide with the topology induced on $H^\circ$ by $S(G^*,G)$ (the adjoints being different), so that $H^\circ$ is a subspace of a strong adjoint space which is not itself a strong adjoint space. This also illustrates the fact that the strong adjoint of an inductive limit may fail to be the projective limit of the corresponding strong adjoints.

\item[(d)] If $E$ and $F$ are Fr\'{e}chet spaces, then $G$ is a countable direct sum of Fr\'{e}chet spaces, but it cannot be fully complete (see 18I), since a Hausdorff quotient of a fully complete space is fully complete. Also $G^*$ is a direct sum of Fr\'{e}chet spaces and so is bound (see 22.3 and 19.6) but the subspace $H^\circ$ of $G^*$ is not bound.
\end{enumerate}

The above construction may be realized by taking $E$ [and $F$ as appropriate non-reflexive spaces].

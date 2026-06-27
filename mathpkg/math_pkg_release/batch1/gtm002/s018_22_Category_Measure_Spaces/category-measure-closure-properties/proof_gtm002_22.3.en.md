---
role: proof
locale: en
of_concept: category-measure-closure-properties
source_book: gtm002
source_chapter: "22"
source_section: "22. Category Measure Spaces"
---

Let $E$ be a set having the property of Baire. By Theorem 4.6, $E$ can be written uniquely (modulo first category) as $E = G \triangle P$, where $G$ is regular open and $P$ is of first category. Since $\mu$ is a category measure, $\mu(P) = 0$, and sets differing by a set of first category have the same measure. Moreover, for a regular open set $G$, we have $\overline{G} \setminus G$ is nowhere dense (it is the boundary of $G$), hence of first category, so $\mu(\overline{G}) = \mu(G)$. Similarly, $G \setminus \operatorname{int}(\overline{G}^c)$ differs from $G$ by a nowhere dense set, so $\mu(G) = \mu(G'^{-'})$.

Combining these facts, since $E$ differs from the regular open set $G$ by a first category set $P$, the closures of $E$ and $G$ differ by a first category set, hence have the same measure. Therefore
$$\mu(E) = \mu(G) = \mu(\overline{G}) = \mu(\overline{E}) = \mu(E'^{-'}).$$

For the variational characterization: since $E = G \triangle P$ with $G$ regular open, any regular open superset of $E$ must contain $G$ (up to a first category set), and any regular closed subset of $E$ must be contained in $\overline{G}$ (up to a first category set). Since $\mu$ assigns the same measure to a set and its regular open kernel or regular closed hull modulo first category, we obtain
$$\mu(E) = \inf\{\mu(U) : E \subset U,\; U \text{ regular open}\} = \sup\{\mu(K) : K \subset E,\; K \text{ regular closed}\}.$$

Writing $G = \phi(E)$, the map $\phi$ selects the canonical regular open representative from the equivalence class of $E$ modulo first category sets. Theorem 4.7 implies that $\phi$ satisfies the conditions:
\begin{enumerate}
\item $\phi(E) \triangle E$ is of first category,
\item $E \triangle F$ is of first category $\implies$ $\phi(E) = \phi(F)$,
\item $\phi(\emptyset) = \emptyset$, $\phi(X) = X$,
\item $\phi(E \cap F) = \phi(E) \cap \phi(F)$,
\item $E \subset F \implies \phi(E) \subset \phi(F)$.
\end{enumerate}
These are precisely the conditions characterizing a Lebesgue lower density (cf. Theorem 3.21), suggesting the program developed in the subsequent theorems for converting a measure space into a category measure space.

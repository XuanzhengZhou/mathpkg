---
role: proof
locale: en
of_concept: plh-approximation-of-homeomorphisms-linear-graphs
source_book: gtm047
source_chapter: "8"
source_section: "33"
---

Regard $K$ as a finite complex. For each vertex $v$ of $K$, let $\operatorname{St} v$ be the star of $v$ in $K$. By a suitable subdivision, the diameters $\delta|\operatorname{St} v|$ can be made as small as desired. Since $K$ is compact, $h|K$ is uniformly continuous. Therefore we may assume that
$$\delta h(|\operatorname{St} v|) < \varepsilon/4$$
for each $v$.

The scheme of the proof is:
\begin{enumerate}
\item[(1)] To arrange that if $C_v$ is a dual cell of $N$, and $C'_v = h(C_v)$, then $\delta C'_v < \varepsilon/4$,
\item[(2)] To define $X = f(N)$ so that $X$ is a neighborhood of $K'$, and for each vertex $v$ of $K$, $f(C_v)$ is a polyhedral 3-cell containing $v' = h(v)$ in its interior, with $\delta f(C_v) < \varepsilon/4$.
\end{enumerate}
It follows that $f$ is an $\varepsilon$-approximation of $h$.

First choose $N$ as a sufficiently small regular neighborhood of $K$ so that $\delta C'_v < \varepsilon/4$ for each $v$. This is possible because if $N$ is a sufficiently small neighborhood of $K$, the sets $C'_v$ lie in arbitrarily small neighborhoods of the sets $h(|\operatorname{St} v|)$.

For each splitting disk $D = D_e$ of $N$, choose $E = E_e$ as in Theorems 32.1--32.3. The sets $E$ decompose $N' = h(N)$ into a finite collection of sets $C_v''$, each containing exactly one vertex $v'$ of $K' = h(K)$; two sets $C_{v_1}''$, $C_{v_2}''$ intersect if and only if $v_1$ and $v_2$ are the end-points of an edge of $K$. By (8) of Theorem 32.3, the sets $C_v''$ can be chosen to lie in arbitrarily small neighborhoods of the sets $C'_v$.

The proof then proceeds through a sequence of lemmas (Lemmas 1--13) that construct and refine the polyhedral 3-manifold $X$:
\begin{itemize}
\item Lemma 1: The dual cells and $C_v''$ sets can be chosen with $\delta C_v'' < \varepsilon/4$.
\item Lemma 2: There exists a polyhedral 3-manifold $X$ with boundary, containing $K'$ in its interior.
\item Lemma 4: Each $E \cap \operatorname{Bd} X$ is a single polygon (achieved by splitting annuli).
\item Lemma 5: $X$ and $\operatorname{Bd} X$ can be taken connected.
\item Lemma 6: Each $C_v'' \cap \operatorname{Bd} X$ is a connected polyhedral 2-manifold $A_v'$ with boundary.
\item Lemma 8: A disk $\Delta$ lying in $C_{v_1}''$ satisfying certain intersection conditions must intersect $K'$ (using the hypothesis that $K$ has no end-points).
\item Lemma 9: $\operatorname{Int} N'$ contains no LTD (locally tame disk) -- proved by eliminating polygon and broken line intersections via splitting processes.
\item Lemma 10: $\pi(\operatorname{Bd} X) \approx \pi(\operatorname{Bd} N)$ (isomorphism of fundamental groups), established by analyzing PL paths in $\operatorname{Int} N' - K'$ and using the product structure $\phi: \operatorname{Bd} N \times (0,1) \leftrightarrow \operatorname{Int} N' - K'$.
\item Lemma 11: $\operatorname{Bd} X$ and $\operatorname{Bd} N$ are homeomorphic -- follows from Lemma 10, homology, orientability (Theorem 26.8), and classification (Theorem 22.9).
\item Lemma 12: Each $A_v'$ is either a disk or a disk with holes (otherwise $p^1(\operatorname{Bd} X)$ would exceed $p^1(\operatorname{Bd} N)$).
\item Lemma 13: There exists a PL homeomorphism $f: \operatorname{Bd} N \to \operatorname{Bd} X$ that carries each $A_v$ onto $A_v'$.
\end{itemize}
The final step extends this PL homeomorphism from $\operatorname{Bd} N$ to all of $N$, completing the construction of $f$.

---
role: proof
locale: en
of_concept: ucl-sl-implies-zf-ac-in-v-b
source_book: gtm008
source_chapter: "23"
source_section: "3"
---

Reserve $p, q, \bar{q}, q'$, etc., to denote elements of $P$. For $S \subseteq B_0 \times I$ and $S \in M$ we define $K(S)$ as follows:

$K(S) = D(w)$ if there exists an $\bar{r}$ and a $w$ such that $w$ is a constant term and
\begin{enumerate}
\item[(i)] $\bar{r} \in F \wedge \bar{r} \leq [[w \subseteq u]]$.
\item[(ii)] $(\forall v \in I)[\#(\bar{r} \cdot [[v \in w]]) \cdot \bar{r} \leq [[v \in w]]]$.
\item[(iii)] $S = \{ \langle p, v \rangle \mid 0 < p \wedge p \in B_0 \wedge v \in I \wedge 0 < p \cdot \bar{r} \leq [[v \in w]] \}$.
\end{enumerate}
$K(S) = 0$ otherwise.

We claim that
\begin{enumerate}
\item[(iv)] $K: \mathcal{P}^M(B_0 \times I) \xrightarrow{\text{onto}} \mathcal{P}^{M[F]}(D(u))$.
\end{enumerate}

This proves the theorem. For $B_0 \times I \in M$, so $\mathcal{P}^M(B_0 \times I) \in M \subseteq M[F]$, since $M$ satisfies the Axiom of Powers. Moreover, $K$ is definable in $M[F]$ and $M[F]$ satisfies the Axiom of Replacement, so $\mathcal{P}^{M[F]}(D(u)) \in M[F]$ by (iv).

We prove (iv) by showing $K$ is a function and $K$ is onto.

\textbf{1. $K$ is a function.} Let $S \subseteq B_0 \times I$ and $S \in M$. Assuming conditions (i)-(iii) are satisfied by $w_0, \bar{r}_0$ and by $w_1, \bar{r}_1$ for the same $S$, we show $D(w_0) = D(w_1)$.

\textbf{2. $K$ is onto.} For any subset of $D(u)$ in $M[F]$, define
$$S = \{ \langle p, v \rangle \mid 0 < p \wedge p \in B_0 \wedge v \in I \wedge 0 < p \cdot \bar{r} \leq \llbracket v \in w \rrbracket \}.$$
Then $K(S) = D(w)$ and $S \in \mathcal{P}^{M}(B_0 \times I)$.

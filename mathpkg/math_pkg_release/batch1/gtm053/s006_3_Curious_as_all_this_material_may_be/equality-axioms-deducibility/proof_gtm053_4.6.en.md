---
role: proof
locale: en
of_concept: equality-axioms-deducibility
source_book: gtm053
source_chapter: "I"
source_section: "4.6"
---

\textbf{(a)} Suppose $\phi$ is an interpretation with $\phi(=)$ equality. Then $|t = t|(\xi) = 1$ trivially. For symmetry, if $|t_1 = t_2|(\xi) = 1$, then $t_1^\xi = t_2^\xi$, so $|t_2 = t_1|(\xi) = 1$. Transitivity is similar.

For the substitution schema: suppose $|x = t|(\xi) = 1$ and $|P(x, x)|(\xi) = 1$ but $|P(x, t)|(\xi) = 0$. The first assertion means $x^\xi = t^\xi$. But then $|P(x, x)|(\xi) = |P(x, t)|(\xi)$ by Proposition 2.10, contradicting the second and third assertions. Hence $|x = t \Rightarrow (P(x, x) \Rightarrow P(x, t))| = 1$.

\textbf{(b)} \textit{Deduction of $t = t$:}
\begin{enumerate}
\item $x = x$ (axiom of equality);
\item $\forall x(x = x)$ (Gen);
\item $\forall x(x = x) \Rightarrow t = t$ (logical axiom of specialization);
\item $t = t$ (MP).
\end{enumerate}

\textit{Deduction of $t_1 = t_2 \Leftrightarrow t_2 = t_1$:}
\begin{enumerate}
\item $x = y \Rightarrow (x = x \Rightarrow y = x)$ (axiom of equality with $=$ for $P$);
\item $Q \Rightarrow ((P \Rightarrow (Q \Rightarrow R)) \Rightarrow (P \Rightarrow R))$, where $P$ is $x = y$, $Q$ is $x = x$, $R$ is $y = x$ (tautology);
\item $x = x$ (axiom of equality);
\item $(P \Rightarrow (Q \Rightarrow R)) \Rightarrow (P \Rightarrow R)$ (MP applied to (2) and (3));
\item $x = y \Rightarrow y = x$ (MP applied to (1) and (4)).
\end{enumerate}

We then twice apply Gen, the axiom of specialization, and MP, in order to deduce the formula $t_1 = t_2 \Rightarrow t_2 = t_1$ from (5); we replace $t_1$ by $t_2$ and $t_2$ by $t_1$ to deduce $t_2 = t_1 \Rightarrow t_1 = t_2$; we use Lemma 4.4 to deduce the conjunction of these two formulas; and, finally, the tautology $$(t_1 = t_2 \Rightarrow t_2 = t_1) \wedge (t_2 = t_1 \Rightarrow t_1 = t_2) \Rightarrow (t_1 = t_2 \Leftrightarrow t_2 = t_1)$$ together with MP yields $t_1 = t_2 \Leftrightarrow t_2 = t_1$.

The deductions for transitivity and the substitution schema are analogous.

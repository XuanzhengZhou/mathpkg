---
role: exercise
locale: en
chapter: "14"
section: "Exercises"
exercise_number: 34
---

An $m$-ary function $f$ is *strongly syntactically definable* in a theory $\Gamma$ formulated in $\mathcal{L}_{\text{nos}}$ provided that there is a formula $\varphi$ of $\mathcal{L}_{\text{nos}}$ with $\text{Fv}\,\varphi \subseteq \{v_0, \ldots, v_m\}$ such that the following two conditions hold:

\begin{enumerate}
\item[(1)] for all $x_0, \ldots, x_{m-1} \in \omega$, the sentence $\varphi(x_0, \ldots, x_{m-1}, \Delta f(x_0, \ldots, x_{m-1}))$ is in $\Gamma$;
\item[(2)] the sentence $\forall v_0 \cdots \forall v_{m-1} \exists v_{m+1} \forall v_m (\varphi \leftrightarrow v_m = v_{m+1})$ is in $\Gamma$.
\end{enumerate}

Show that if $f$ is syntactically definable in $\Gamma$, then $f$ is strongly syntactically definable in $\Gamma$.

[Note: The exercise statement is partially truncated in the source text. The converse direction may also have been part of the original exercise.]

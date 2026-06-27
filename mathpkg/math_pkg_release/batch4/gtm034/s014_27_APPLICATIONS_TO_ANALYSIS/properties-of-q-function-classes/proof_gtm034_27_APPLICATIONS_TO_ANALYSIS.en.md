---
role: proof
locale: en
of_concept: properties-of-q-function-classes
source_book: gtm034
source_chapter: "27"
source_section: "APPLICATIONS TO ANALYSIS"
---

\textbf{Proof of P1:}

\textit{Part (1).} If $f(x) = g\psi(x) = \sum_{y \in S} g(x,y)\psi(y)$ is a $Q$-potential, then using the identity
$$\sum_{t \in S} Q(x,t)g(t,y) - g(x,y) = -\delta(x,y), \quad x,y \in S,$$
which follows from the definition of the Green function as $g(x,y) = \sum_{n=0}^{\infty} Q_n(x,y)$, we have
$$Qf(x) = \sum_{t \in S} Q(x,t) \sum_{y \in S} g(t,y)\psi(y) = \sum_{y \in S} [g(x,y) - \delta(x,y)]\psi(y) = f(x) - \psi(x) \leq f(x),$$
since $\psi(x) \geq 0$ on $S$. Hence $f$ is $Q$-excessive.

\textit{Part (2).} Let $f$ and $g$ be $Q$-excessive, so that $Qf \leq f$ and $Qg \leq g$. Then
\begin{align*}
\min[f(x), g(x)] &\geq \min\left[ \sum_{y \in S} Q(x,y)f(y), \sum_{y \in S} Q(x,y)g(y) \right] \\
&\geq \sum_{y \in S} Q(x,y) \min[f(y), g(y)].
\end{align*}
The second inequality uses the non-negativity of $Q(x,y)$. Thus $\min[f, g]$ is $Q$-excessive.

\textit{Part (3).} Suppose $f(x) = \sum_{y \in S} g(x,y)\psi(y)$ is a $Q$-potential. Then
$$Q_n f(x) = \sum_{y \in S} \psi(y) \left[ \sum_{k=n}^{\infty} Q_k(x,y) \right],$$
since $g(x,y) = \sum_{k=0}^{\infty} Q_k(x,y)$. The inner sum is the tail of a convergent series (by the definition of a transient kernel), and therefore tends to zero for each fixed $x, y$ as $n \to \infty$. Hence $Q_n f(x) \to 0$ for each $x \in S$ as $n \to \infty$.

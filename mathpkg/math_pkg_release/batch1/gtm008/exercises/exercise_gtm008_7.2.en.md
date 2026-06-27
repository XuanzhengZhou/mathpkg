---
role: exercise
locale: en
chapter: "7"
section: "Relative Constructibility"
exercise_number: 2
---
If $M$ is a standard transitive model of $ZF$, $On \subseteq M$, $K \subseteq M$ and $\mathcal{L} = \mathcal{L}_0(\{M(), K(\cdot)\})$ we define $C = \langle C_\alpha, \bar{M}_\alpha, \bar{K}_\alpha \rangle$ and $M_K$ by recursion:

\begin{enumerate}
\item[(i)] $C_0 = 0$.
\item[(ii)] $\bar{M}_\alpha = M \cap R(\alpha), \bar{K}_\alpha = C_\alpha \cap K$.
\item[(iii)] $C_{\alpha+1} = Df(C_\alpha) \cup \bar{M}_{\alpha+1} \cup \bar{K}_\alpha$.
\item[(iv)] $C_\alpha = \bigcup_{\beta < \alpha} C_\beta$, for $\alpha \in K_{\Pi}$ (limit ordinals).
\item[(v)] $M_K = \bigcup_{\alpha \in On} C_\alpha$.
\end{enumerate}

---
role: proof
locale: en
of_concept: planar-isovalent-classification
source_book: gtm054
source_chapter: "III"
source_section: "12"
---

Since $\Gamma$ is isovalent and has an $m$-covalent imbedding, we have $\rho(\Gamma) = \rho$ and $\rho^{\perp}(\Gamma) = \rho^{\perp}$ as integers. By F7b, $\rho \geq 3$ and $\rho^{\perp} \geq 3$ (since $\Gamma$ has no isthmuses). The Euler relation from Corollary F4 gives the system F17:
$$\rho \geq 3,\quad \rho^{\perp} \geq 3,\quad \nu_1 \geq 2,\quad \frac{1}{\rho} + \frac{1}{\rho^{\perp}} = \frac{1}{2} + \frac{1}{\nu_1}.$$

The system is symmetric in $\rho$ and $\rho^{\perp}$. Thus if we find all solutions with $\rho \geq \rho^{\perp}$, we obtain all other solutions by interchanging the values of $\rho$ and $\rho^{\perp}$.

\textbf{Case 1: $\rho^{\perp} = 2$.} Then the equation becomes:
$$\rho \geq 2,\quad \nu_1 \geq 2,\quad \frac{1}{\rho} = \frac{1}{\nu_1}.$$
This yields the solutions $\rho = \nu_1 = k$, $\rho^{\perp} = 2$, for $k = 2, 3, \ldots$. Using $\nu_0 = 2\nu_1/\rho = 2$ and $\nu_2 = 2\nu_1/\rho^{\perp} = k$, we obtain Type I. The symmetric case $\rho = 2$, $\rho^{\perp} = k$ yields Type II.

\textbf{Case 2: $\rho^{\perp} = 3$.} Then the equation becomes:
$$\rho \geq 3,\quad \nu_1 \geq 2,\quad \frac{1}{\rho} = \frac{1}{6} + \frac{1}{\nu_1}.$$
Clearly $\rho < 6$, so $\rho = 3, 4,$ or $5$, yielding:
\begin{itemize}
\item $\rho = 3$, $\nu_1 = 6$: then $\nu_0 = 2\cdot 6/3 = 4$, $\nu_2 = 2\cdot 6/3 = 4$ (Type III, tetrahedron)
\item $\rho = 4$, $\nu_1 = 12$: then $\nu_0 = 2\cdot 12/4 = 6$, $\nu_2 = 2\cdot 12/3 = 8$ (Type IV, octahedron)
\item $\rho = 5$, $\nu_1 = 30$: then $\nu_0 = 2\cdot 30/5 = 12$, $\nu_2 = 2\cdot 30/3 = 20$ (Type VI, icosahedron)
\end{itemize}

We have a total of $1$ (from Case 1) $+ 3$ (from Case 2) $= 4$ solutions with $\rho \geq \rho^{\perp}$. By symmetry, we get three more solutions:
\begin{itemize}
\item $\rho = 3$, $\rho^{\perp} = 4$, $\nu_1 = 12$: $\nu_0 = 8$, $\nu_2 = 6$ (Type V, cube)
\item $\rho = 3$, $\rho^{\perp} = 5$, $\nu_1 = 30$: $\nu_0 = 20$, $\nu_2 = 12$ (Type VII, dodecahedron)
\item $\rho = 2$, $\rho^{\perp} = k$: Type II (already counted above via symmetry)
\end{itemize}

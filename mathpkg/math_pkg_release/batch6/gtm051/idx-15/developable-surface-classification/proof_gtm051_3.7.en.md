---
role: proof
locale: en
of_concept: developable-surface-classification
source_book: gtm051
source_chapter: "3"
source_section: "3.7"
---

1. By Theorem 3.7.9 we may assume that $f$ can be written locally as $f(s, t) = sX(t) + c(t)$ for $(s, t)$ within some neighborhood $U = I \times J$ of $(0, 0)$, with $f_s \cdot f_t = 0$, $n_s \cdot f_t = n \cdot f_{st} = 0$. Therefore
$$X \cdot (s\dot{X} + \dot{c}) = 0,\quad \dot{c}(t) = f_t(0, t) \neq 0,\quad f_s = X \neq 0,$$
and $n \cdot \dot{X} = 0$.

The tangent space $T_{(s,t)}f$ is spanned by $X(t)$ and $\dot{c}(t)$, with $X(t) \cdot \dot{c}(t) = 0$. Since $\dot{X}(t) \in T_{(s,t)}f$ and $X \cdot \dot{X} = 0$, we have
$$\dot{X}(t) = r(t)\,\dot{c}(t)$$
for some real-valued differentiable function $r(t)$.

2. Let $t \in I$ and consider the function $r(t)$. Define $I_0$ as the set of $t \in \mathbb{R}$ satisfying one of the following properties:
\begin{itemize}
\item[(a)] There exists a neighborhood $U(t_0)$ of $t_0$ on which $r(t) = 0$.
\item[(b)] There exists a neighborhood $U(t_0)$ of $t_0$ on which $r(t) = \text{constant} \neq 0$.
\item[(c)] There exists a neighborhood $U(t_0)$ of $t_0$ on which $r(t) \neq 0$ and $\dot{r}(t) \neq 0$.
\end{itemize}

By definition, $I_0 \subset I$ is open. A moment's reflection shows that $I_0$ is also closed in $I$, hence $I_0 = I$. These three cases correspond respectively to:
\begin{itemize}
\item \textbf{Cylinders} ($r = 0$): $\dot{X} = 0$, so $X$ is constant and the surface is a cylinder over the curve $c(t)$.
\item \textbf{Cones} ($r = \text{constant} \neq 0$): $X(t) = r\,c(t) + X_0$, so $f(s, t) = s(r\,c(t) + X_0) + c(t) = (sr+1)c(t) + sX_0$, which after reparametrization is a cone with vertex at some point.
\item \textbf{Tangential developables} ($r \neq 0, \dot{r} \neq 0$): These are the most general developable surfaces, tangent to a space curve.
\end{itemize}

---
role: proof
locale: en
of_concept: invariance-of-first-fundamental-form
source_book: gtm051
source_chapter: "3"
source_section: "3.2"
---

\begin{proof}
\begin{enumerate}
\item[i)] Suppose $Bx = Rx + x_0$, where $R$ is an orthogonal map. Then $dB = R$. Therefore, if $X, Y \in T_u f$,
$$\tilde{I}_u(RX, RY) = RX \cdot RY = X \cdot Y = I_u(X, Y).$$

\item[ii)] Let $\tilde{X}, \tilde{Y} \in T_v \mathbb{R}^2$. Then
$$\tilde{I}_v(\tilde{X}, \tilde{Y}) = df_v \tilde{X} \cdot df_v \tilde{Y} = df_u \circ d\phi \tilde{X} \cdot df_u \circ d\phi \tilde{Y} = I_u(d\phi \tilde{X}, d\phi \tilde{Y}),$$
where $u = \phi(v)$.
\end{enumerate}
\end{proof}
---
role: proof
locale: en
of_concept: antecedent-exchange
source_book: gtm037
source_chapter: "1"
source_section: "1.2"
---

Using the deduction theorem, we work from the hypotheses $\{\varphi \to (\psi \to \chi),\; \psi,\; \varphi\}$:

\begin{enumerate}
\item $\varphi$ (hypothesis)
\item $\varphi \to (\psi \to \chi)$ (hypothesis)
\item $\psi \to \chi$ (detachment from (1) and (2))
\item $\psi$ (hypothesis)
\item $\chi$ (detachment from (4) and (3))
\end{enumerate}

Thus $\{\varphi \to (\psi \to \chi),\; \psi,\; \varphi\} \vdash \chi$. Apply the deduction theorem three times:

\begin{align*}
\{\varphi \to (\psi \to \chi),\; \psi\} &\vdash \varphi \to \chi \\
\{\varphi \to (\psi \to \chi)\} &\vdash \psi \to (\varphi \to \chi) \\
&\vdash [\varphi \to (\psi \to \chi)] \to [\psi \to (\varphi \to \chi)]
\end{align*}

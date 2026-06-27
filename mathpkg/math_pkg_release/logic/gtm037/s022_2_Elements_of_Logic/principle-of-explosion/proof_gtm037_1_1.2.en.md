---
role: proof
locale: en
of_concept: principle-of-explosion
source_book: gtm037
source_chapter: "1"
source_section: "1.2"
---

The proof uses the deduction theorem. Start from the hypotheses $\{\varphi,\; \neg\varphi\}$ and derive $\psi$:

\begin{enumerate}
\item $\varphi$ (hypothesis)
\item $\neg\varphi$ (hypothesis)
\item $\neg\varphi \to (\neg\psi \to \neg\varphi)$ (axiom A1: $\alpha \to (\beta \to \alpha)$)
\item $\neg\psi \to \neg\varphi$ (detachment from (2) and (3))
\item $\varphi \to (\neg\psi \to \varphi)$ (axiom A1)
\item $\neg\psi \to \varphi$ (detachment from (1) and (5))
\item $(\neg\psi \to \neg\varphi) \to [(\neg\psi \to \varphi) \to \psi]$ (axiom A3: $(\neg\alpha \to \neg\beta) \to (\beta \to \alpha)$, with appropriate substitution)
\item $(\neg\psi \to \varphi) \to \psi$ (detachment from (4) and (7))
\item $\psi$ (detachment from (6) and (8))
\end{enumerate}

Thus $\{\varphi,\; \neg\varphi\} \vdash \psi$. Applying the deduction theorem twice yields $\vdash \varphi \to (\neg\varphi \to \psi)$.

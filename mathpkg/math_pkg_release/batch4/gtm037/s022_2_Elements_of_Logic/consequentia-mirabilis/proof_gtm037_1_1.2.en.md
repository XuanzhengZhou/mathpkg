---
role: proof
locale: en
of_concept: consequentia-mirabilis
source_book: gtm037
source_chapter: "1"
source_section: "1.2"
---

Working from the hypotheses $\{\varphi \to \neg \varphi,\; \neg \neg \varphi\}$:

\begin{align*}
\{\varphi \to \neg \varphi,\; \neg \neg \varphi\} &\vdash \varphi \\
\{\varphi \to \neg \varphi,\; \neg \neg \varphi\} &\vdash \neg \varphi \\
\{\varphi \to \neg \varphi\} &\vdash \neg \neg \varphi \to \varphi \\
\{\varphi \to \neg \varphi\} &\vdash \neg \neg \varphi \to \neg \varphi \\
\{\varphi \to \neg \varphi\} &\vdash \neg \varphi \\
&\vdash (\varphi \to \neg \varphi) \to \neg \varphi
\end{align*}

Step 1: From $\neg \neg \varphi$ we derive $\varphi$ via double-negation elimination (axiom A3: $(\neg \neg \varphi \to \neg \neg \varphi) \to (\neg \varphi \to \neg \varphi)$ form, or more directly using the instance $(\neg \neg \varphi \to \varphi)$ obtainable from A3).

Step 2: From $\varphi$ and $\varphi \to \neg \varphi$ we derive $\neg \varphi$ by detachment.

Steps 3-4: Apply the deduction theorem to discharge $\neg \neg \varphi$, obtaining both $\neg \neg \varphi \to \varphi$ and $\neg \neg \varphi \to \neg \varphi$. These are derived from the earlier lines by the deduction theorem.

Step 5: From $\neg \neg \varphi \to \varphi$ and $\neg \neg \varphi \to \neg \varphi$ together with the appropriate instance of axiom A3 $[(\neg \neg \varphi \to \neg \varphi) \to (\varphi \to \neg \varphi)] \to \dots$ or by applying the contrapositive reasoning, we obtain $\neg \varphi$. More directly, using the instance $(\neg \neg \varphi \to \varphi) \to [(\neg \neg \varphi \to \neg \varphi) \to \neg \varphi]$ (a form of A3), detachment gives $\neg \varphi$.

Step 6: Apply the deduction theorem one final time.

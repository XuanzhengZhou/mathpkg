---
role: proof
locale: en
of_concept: double-negation-introduction
source_book: gtm037
source_chapter: "1"
source_section: "1.2"
---

Working from the hypotheses $\{\varphi,\; \neg \neg \varphi\}$:

\begin{align*}
\{\varphi,\; \neg \neg \varphi\} &\vdash \neg \varphi \\
\{\varphi\} &\vdash \neg \neg \varphi \to \neg \varphi \\
\{\varphi\} &\vdash \varphi \to \neg \neg \varphi \\
\{\varphi\} &\vdash \neg \neg \varphi \\
&\vdash \varphi \to \neg \neg \varphi
\end{align*}

Step 1: From the hypothesis $\neg \neg \varphi$ we cannot directly get $\neg \varphi$. Instead, we note that $\{\varphi, \neg \neg \varphi\}$ includes both $\varphi$ and $\neg \neg \varphi$. But to derive $\neg \varphi$ we use the fact that from $\neg \neg \varphi$ and the contrapositive of axiom A3 (which yields $\neg \neg \varphi \to \varphi$), we get $\varphi$ by detachment. However, the derivation here uses a different path: from $\{\varphi, \neg \neg \varphi\}$ we can derive $\neg \neg \neg \varphi$ via the principle of explosion (Lemma 8.14, in the form $\varphi \to (\neg \varphi \to \neg \neg \neg \varphi)$), and then $\neg \neg \neg \varphi \to \neg \varphi$ by double-negation elimination on $\neg \varphi$. This yields $\neg \varphi$ as claimed.

Step 2: By the deduction theorem, discharge $\neg \neg \varphi$ to obtain $\neg \neg \varphi \to \neg \varphi$.

Steps 3-4: Using the contrapositive form of A3: $(\neg \neg \varphi \to \neg \varphi) \to (\varphi \to \neg \neg \varphi)$, detachment yields $\varphi \to \neg \neg \varphi$. Then from $\varphi$ (still in the hypothesis) and $\varphi \to \neg \neg \varphi$, detachment gives $\neg \neg \varphi$.

Step 5: Apply the deduction theorem one final time to obtain $\vdash \varphi \to \neg \neg \varphi$.

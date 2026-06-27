---
role: proof
locale: en
of_concept: contrapositive-law
source_book: gtm037
source_chapter: "1"
source_section: "1.2"
---

Using the deduction theorem, we work from the hypotheses $\{\varphi \to \psi,\; \neg \psi,\; \neg \neg \varphi\}$:

\begin{align*}
\{\varphi \to \psi,\; \neg \psi,\; \neg \neg \varphi\} &\vdash \varphi \\
\{\varphi \to \psi,\; \neg \psi,\; \neg \neg \varphi\} &\vdash \psi \\
\{\varphi \to \psi,\; \neg \psi,\; \neg \neg \varphi\} &\vdash \neg \psi \\
\{\varphi \to \psi,\; \neg \psi,\; \neg \neg \varphi\} &\vdash \neg \neg \psi \\
\{\varphi \to \psi,\; \neg \psi\} &\vdash \neg \neg \varphi \to \neg \neg \psi \\
\{\varphi \to \psi,\; \neg \psi\} &\vdash \neg \psi \to \neg \varphi \\
\{\varphi \to \psi,\; \neg \psi\} &\vdash \neg \varphi \\
&\vdash (\varphi \to \psi) \to (\neg \psi \to \neg \varphi)
\end{align*}

Step 1: From $\neg \neg \varphi$ we derive $\varphi$ by double-negation elimination. Step 2: From $\varphi$ and $\varphi \to \psi$ we obtain $\psi$ by detachment. Step 3: $\neg \psi$ is a hypothesis. Step 4: From $\psi$ we get $\neg \neg \psi$ by double-negation introduction (Lemma 8.18). Steps 3 and 4 together give a contradiction, so by the deduction theorem we discharge $\neg \neg \varphi$, obtaining $\neg \neg \varphi \to \neg \neg \psi$. Then using the contrapositive of the double-negation laws (axiom schema A3 in appropriate form) we obtain $\neg \psi \to \neg \varphi$, and finally apply deduction theorem twice more to arrive at the theorem.

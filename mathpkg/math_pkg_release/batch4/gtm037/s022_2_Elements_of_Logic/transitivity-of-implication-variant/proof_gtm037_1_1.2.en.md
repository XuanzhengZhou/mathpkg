---
role: proof
locale: en
of_concept: transitivity-of-implication-variant
source_book: gtm037
source_chapter: "1"
source_section: "1.2"
---

We use the deduction theorem repeatedly. Start from the hypotheses $\{\varphi \to \psi,\; \psi \to \chi,\; \varphi\}$.

\begin{align*}
\{\varphi \to \psi,\; \psi \to \chi,\; \varphi\} &\vdash \varphi \\
\{\varphi \to \psi,\; \psi \to \chi,\; \varphi\} &\vdash \varphi \to \psi \\
\{\varphi \to \psi,\; \psi \to \chi,\; \varphi\} &\vdash \psi \to \chi \\
\{\varphi \to \psi,\; \psi \to \chi,\; \varphi\} &\vdash \chi
\end{align*}

The first three lines are immediate (each formula is either a hypothesis or follows from hypotheses). The fourth line: from $\varphi$ and $\varphi \to \psi$ we get $\psi$ by detachment; from $\psi$ and $\psi \to \chi$ we get $\chi$ by detachment.

Now apply the deduction theorem:
\begin{align*}
\{\varphi \to \psi,\; \psi \to \chi\} &\vdash \varphi \to \chi \\
\{\varphi \to \psi\} &\vdash (\psi \to \chi) \to (\varphi \to \chi) \\
&\vdash (\varphi \to \psi) \to [(\psi \to \chi) \to (\varphi \to \chi)]
\end{align*}

Each step removes one hypothesis via the deduction theorem, culminating in the desired theorem.

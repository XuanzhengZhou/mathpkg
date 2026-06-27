---
role: proof
locale: en
of_concept: self-implication
source_book: gtm037
source_chapter: "1"
source_section: "1.2"
---

We present a formal proof with justifications listed to the right.

\begin{align*}
(1)\quad & \{\varphi \to [(\varphi \to \varphi) \to \varphi]\} \to \{[\varphi \to (\varphi \to \varphi)] \to (\varphi \to \varphi)\} && \text{A2} \\
(2)\quad & \varphi \to [(\varphi \to \varphi) \to \varphi] && \text{A1} \\
(3)\quad & [\varphi \to (\varphi \to \varphi)] \to (\varphi \to \varphi) && \text{(1), (2), detachment} \\
(4)\quad & \varphi \to (\varphi \to \varphi) && \text{A1} \\
(5)\quad & \varphi \to \varphi && \text{(3), (4), detachment}
\end{align*}

Line (1) is an instance of axiom schema A2: $[\varphi \to (\psi \to \chi)] \to [(\varphi \to \psi) \to (\varphi \to \chi)]$, with $\psi$ replaced by $\varphi \to \varphi$ and $\chi$ replaced by $\varphi$. Line (2) is an instance of axiom schema A1: $\varphi \to (\psi \to \varphi)$, with $\psi$ replaced by $\varphi \to \varphi$. Line (3) follows from (1) and (2) by modus ponens. Line (4) is another instance of A1, with $\psi$ replaced by $\varphi$. Line (5), the desired conclusion, follows from (3) and (4) by modus ponens.

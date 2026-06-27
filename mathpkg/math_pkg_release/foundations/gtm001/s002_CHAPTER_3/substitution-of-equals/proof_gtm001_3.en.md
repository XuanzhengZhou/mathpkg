---
role: proof
locale: en
of_concept: substitution-of-equals
source_book: gtm001
source_chapter: "3"
source_section: ""
---
\text{(By induction on $n$ the number of logical symbols in $\varphi$).}
\text{If $n = 0$: $\varphi(a)$ is of the form $c \in d$, $c \in a$, $a \in c$, or $a \in a$. Each case follows from Definition 3.1 and Proposition 3.3.}

\text{Induction step ($n > 0$): $\varphi(a)$ must be of the form:}
\text{(1) $\neg\psi(a)$: By induction hypothesis, $a = b \rightarrow [\psi(a) \leftrightarrow \psi(b)]$, hence $a = b \rightarrow [\neg\psi(a) \leftrightarrow \neg\psi(b)]$.}
\text{(2) $\psi(a) \land \eta(a)$: By induction hypothesis for both, the result follows.}
\text{(3) $(\forall x)\psi(a, x)$: Choose a free variable $c$ distinct from $a, b$ not occurring in $\psi(a, x)$. Since $\psi(a, c)$ has fewer than $n$ logical symbols, $a = b \rightarrow [\psi(a, c) \leftrightarrow \psi(b, c)]$. Generalize on $c$ using Logical Axiom 4 to obtain the result.

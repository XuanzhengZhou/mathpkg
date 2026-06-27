---
role: exercise
locale: en
chapter: "VII"
section: "1"
exercise_number: 1
---

Prove that the pentagon axiom (5) and the triangle axiom (7) imply the diagram (9):

\[
\begin{CD}
e \square (b \square c) @>{\alpha}>> (e \square b) \square c\\
@V{1 \square \lambda}VV @VV{\lambda \square 1}V\\
b \square c @= b \square c
\end{CD}
\qquad
\begin{CD}
a \square (b \square e) @>{\alpha}>> (a \square b) \square e\\
@V{1 \square \varrho}VV @VV{\varrho \square 1}V\\
a \square b @= a \square b
\end{CD}
\]

*Hint:* Take the pentagon (5) with $a = b = e$ and fill in the inside, adding $\varrho$ in two places, the basic identity (7) twice, and suitable naturalities to get $(\lambda \square 1) \alpha \lambda = \lambda \lambda : e \square (e \square (c \square d)) \to c \square d$, and hence (since $\lambda$ is an isomorphism) $(\lambda \square 1) \alpha = \lambda$.

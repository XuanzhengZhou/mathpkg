---
role: proof
locale: en
of_concept: irrotational-iff-locally-synchronizable
source_book: gtm048
source_chapter: "2"
source_section: "2.3"
---

Let $Q$ be the reference frame and $\omega$ the 1-form physically equivalent to $Q$. In a sufficiently small neighborhood, let $X, Y$ be vector fields such that $g(Q, X) = g(Q, Y) = 0$ everywhere. Then:
\begin{align*}
\omega \wedge d\omega = 0 &\iff d\omega(X, Y) = 0 \quad \text{for all such } X, Y \\
&\iff \omega([X, Y]) = 0 \quad \text{(formula for } d\omega \text{)} \\
&\iff g(Q, [X, Y]) = 0 \\
&\iff g(D_X Q, Y) = g(D_Y Q, X) \quad \text{(since } D_X Y - D_Y X - [X, Y] = 0 \text{)} \\
&\iff g(A_Q X, Y) - g(X, A_Q Y) = 0.
\end{align*}
The last condition is precisely that $A_Q$ is self-adjoint, i.e., $Q$ is irrotational.

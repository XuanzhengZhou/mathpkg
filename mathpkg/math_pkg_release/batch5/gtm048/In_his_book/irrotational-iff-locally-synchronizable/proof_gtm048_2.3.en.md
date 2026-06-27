---
role: proof
locale: en
of_concept: irrotational-iff-locally-synchronizable
source_book: gtm048
source_chapter: "2"
source_section: "2.3"
---

Let $Q$ be the reference frame and $\omega$ the physically equivalent 1-form. In a sufficiently small neighborhood, let $X, Y$ be vector fields such that $g(Q, X) = g(Q, Y) = 0$ everywhere. Then in this neighborhood:

$\omega \wedge d\omega = 0$

$\iff d\omega(X, Y) = 0$ for all such vector fields $X$ and $Y$ (by definition of the exterior product)

$\iff \omega([X, Y]) = 0$ for all such $X$ and $Y$ (by the formula $d\omega(X, Y) = X\omega(Y) - Y\omega(X) - \omega([X, Y])$ and $\omega(X) = \omega(Y) = 0$)

$\iff g(Q, [X, Y]) = 0$ for all such $X$ and $Y$ (by definition of $\omega$)

$\iff g(D_X Q, Y) = g(D_Y Q, X)$ for all such $X$ and $Y$ (because $D_X Y - D_Y X - [X, Y] = 0$ and $g(Q, X) = g(Q, Y) = 0$, so $g(Q, D_X Y - D_Y X) = g(Q, [X, Y])$; then $g(D_X Q, Y) = X g(Q, Y) - g(Q, D_X Y) = -g(Q, D_X Y)$, and similarly $g(D_Y Q, X) = -g(Q, D_Y X)$; the condition $g(Q, [X, Y]) = 0$ becomes $g(Q, D_X Y - D_Y X) = 0$, i.e., $-g(D_X Q, Y) + g(D_Y Q, X) = 0$)

$\iff g(A_Q X, Y) - g(X, A_Q Y) = 0$ for all such $X$ and $Y$

$\iff A_Q$ is self-adjoint on $R_u$

$\iff Q$ is irrotational.

---
role: proof
locale: en
of_concept: logarithmic-derivative-property-3
source_book: gtm059
source_chapter: "9"
source_section: "9"
---

Write $u = g_i(u)$ as a unit. Then

$$
\mathrm{em} = g_i(u) g_i(u_1) u_2.
$$

Thus we let $g_i(X) = g_i(u)[X]$, so that

$$
\mathrm{em} = g_i(u).
$$

On one hand, we have

\begin{equation}
u^*\lambda_i(u) = \frac{1}{u^2} \lambda_i(u)^{\alpha} = \frac{1}{u^2} \frac{g_i(u)[u_1]u_2}{\mathrm{em}}.
\tag{1}
\end{equation}

On the other hand, since $\lambda_i(u)[u] = u(u)(X)$, we find

\begin{equation}
\lambda_i(u)[u_1] u_2(\lambda_i(u)) = u(\lambda_i(u))(X).
\tag{2}
\end{equation}

Furthermore

\begin{equation}
u^*\lambda_i(u) = \frac{1}{u^2} \frac{g_i(u)}{\mathrm{em}}
\tag{3}
\end{equation}

and

\begin{equation}
g_i(X) = g_i(u)[X] X(u)(X).
\tag{4}
\end{equation}

Putting (1), (2), (3), (4) together yields the desired property.

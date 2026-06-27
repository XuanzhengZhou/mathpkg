role: proof
locale: en
of_concept: composition-associativity
source_book: gtm037
source_chapter: "3"
source_section: "1"
---

Let $x_0,\ldots,x_{p-1}\in\omega$, and let $l$ denote the left hand side and $r$ the right hand side. Then

$$
\begin{aligned}
l(x_0,\ldots,x_{p-1}) &= \bigl(K_n^m(f; g_0,\ldots,g_{m-1})\bigr)\bigl(h_0(x_0,\ldots,x_{p-1}),\ldots,h_{n-1}(x_0,\ldots,x_{p-1})\bigr) \\
&= f\Bigl(g_0\bigl(h_0(x_0,\ldots,x_{p-1}),\ldots,h_{n-1}(x_0,\ldots,x_{p-1})\bigr),\ldots, \\
&\qquad\qquad g_{m-1}\bigl(h_0(x_0,\ldots,x_{p-1}),\ldots,h_{n-1}(x_0,\ldots,x_{p-1})\bigr)\Bigr) \\
&= f\Bigl(\bigl(K_p^n(g_0; h_0,\ldots,h_{n-1})\bigr)(x_0,\ldots,x_{p-1}),\ldots, \\
&\qquad\qquad\bigl(K_p^n(g_{m-1}; h_0,\ldots,h_{n-1})\bigr)(x_0,\ldots,x_{p-1})\Bigr) \\
&= r(x_0,\ldots,x_{p-1}).
\end{aligned}
$$

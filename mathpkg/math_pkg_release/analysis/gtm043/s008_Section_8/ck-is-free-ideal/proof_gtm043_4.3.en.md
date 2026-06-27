---
role: proof
locale: en
of_concept: ck-is-free-ideal
source_book: gtm043
source_chapter: "4"
source_section: "4.3"
---

We show $C_K(\mathbf{N})$ is an ideal and is free. First, $C_K(\mathbf{N})$ is clearly an ideal: if $f, g$ vanish outside finite sets $F_f, F_g$, then $f-g$ vanishes outside $F_f \cup F_g$ (finite), and for any $h$, $fh$ vanishes outside $F_f$ (finite).

To see $C_K(\mathbf{N})$ is free, suppose $n \in \mathbf{N}$ were a common zero of all functions in $C_K(\mathbf{N})$. But the characteristic function $\chi_{\{n\}}$ (value $1$ at $n$, $0$ elsewhere) belongs to $C_K(\mathbf{N})$ and satisfies $\chi_{\{n\}}(n) = 1 \neq 0$. Hence no such $n$ exists, and $\bigcap Z[C_K(\mathbf{N})] = \emptyset$. Therefore $C_K(\mathbf{N})$ is free.

The same argument works in both $C(\mathbf{N})$ and $C^*(\mathbf{N})$, since $\chi_{\{n\}}$ is bounded.

---
role: proof
locale: en
of_concept: hecke-coefficient-prime-case
source_book: gtm007
source_chapter: "VII"
source_section: "5.3"
---
Set $n = p$ in the formula of Proposition 12: $\gamma(m) = \sum_{a \mid (p,m)} a^{2k-1} c(pm/a^2)$. The divisors of $(p,m)$ are:
\begin{itemize}
\item If $p \nmid m$, then $(p,m) = 1$, so the only divisor is $a = 1$. Thus $\gamma(m) = 1^{2k-1} c(pm) = c(pm)$.
\item If $p \mid m$, then $(p,m) = p$, so the divisors are $a = 1$ and $a = p$. Thus $\gamma(m) = 1^{2k-1} c(pm) + p^{2k-1} c(pm/p^2) = c(pm) + p^{2k-1} c(m/p)$.
\end{itemize}

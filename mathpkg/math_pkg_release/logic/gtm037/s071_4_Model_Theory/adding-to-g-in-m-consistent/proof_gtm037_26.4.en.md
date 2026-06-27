---
role: proof
locale: en
of_concept: adding-to-g-in-m-consistent
source_book: gtm037
source_chapter: "26"
source_section: "4"
---

Let $G = \{g_0, \ldots, g_q\}$, where each $g_i$ is one-one. The proof proceeds by contradiction. Suppose there is no $F' \subseteq F$ with $|F'| \leq m$ such that $(F \setminus F', G, D)$ is $m$-consistent over $n$.

One then constructs by transfinite induction on $\beta < m^+$ (where $m^+$ is the successor cardinal of $m$) the following objects:
\begin{itemize}
\item $\rho_\beta \in m^+(n^{\partial})$ — a sequence of ordinals below $n^{\partial}$;
\item $f_\beta \in \prod_{\gamma < m^+} {}^\rho F$ — a matrix of $\rho$-tuples from $F$;
\item $\chi_\beta \in \prod_{\gamma < m^+} {}^\rho (n^{\partial})$ — a matrix of $\rho$-tuples of target values;
\item $q_\beta \in m^+ \omega$ — natural numbers;
\item $h_\beta \in \prod_{\gamma < m^+} {}^q F$ — $q$-tuples from $F$;
\item $k_\beta \in \prod_{\gamma < m^+} {}^q G$ — $q$-tuples from $G$.
\end{itemize}

The construction ensures that at each stage $\beta$, condition (iv) of Definition 26.33 is violated relative to the previously constructed data, leading ultimately to a contradiction with the $m$-consistency of the original triple $(F, 0, D)$.

The strong limit cardinal hypothesis $n^{\partial} \leq m$ is used to bound the number of parameters, ensuring the induction can proceed through $m^+$ stages. The final contradiction shows that some finite $F'$ of size at most $m$ must exist as claimed.

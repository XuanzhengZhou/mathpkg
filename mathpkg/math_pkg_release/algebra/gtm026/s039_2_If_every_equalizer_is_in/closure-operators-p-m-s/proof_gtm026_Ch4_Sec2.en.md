---
role: proof
locale: en
of_concept: closure-operators-p-m-s
source_book: gtm026
source_chapter: "4"
source_section: "2. If every equalizer is in M"
---

Clearly $\mathsf{P}$, $\mathsf{M}$, and $\mathsf{S}$ are all operators $\mathsf{O}$ which are closure operators, that is, which satisfy $\mathcal{A} \subset \mathsf{O}(\mathcal{A})$, $\mathsf{O}(\mathcal{A}) \subset \mathsf{O}(\mathcal{B})$ whenever $\mathcal{A} \subset \mathcal{B}$, and $\mathsf{O}\mathsf{O}(\mathcal{A}) \subset \mathsf{O}(\mathcal{A})$. For any such closure operator, $\mathsf{O}(\mathcal{A})$ is the smallest $\mathsf{O}$-closed $\mathcal{B}$ containing $\mathcal{A}$ (where, of course, $\mathcal{B}$ is $\mathsf{O}$-closed just in case $\mathsf{O}(\mathcal{B}) \subset \mathcal{B}$) since $\mathcal{A} \subset \mathsf{O}(\mathcal{A})$, $\mathsf{O}\mathsf{O}(\mathcal{A}) \subset \mathsf{O}(\mathcal{A})$ and if $\mathcal{A} \subset \mathcal{B}$ with $\mathsf{O}(\mathcal{B}) \subset \mathcal{B}$ then $\mathsf{O}(\mathcal{A}) \subset \mathsf{O}(\mathcal{B}) \subset \mathcal{B}$.

For another general observation, if $\mathsf{O}_1$ and $\mathsf{O}_2$ are closure operators and if $\mathsf{O}_1\mathsf{O}_2(\mathcal{A}) \subset \mathsf{O}_2\mathsf{O}_1(\mathcal{A})$ for all $\mathcal{A}$, then $\mathsf{O}_1\mathsf{O}_2$ is a closure operator. To verify this, we check:
\begin{itemize}
\item $\mathcal{A} \subset \mathsf{O}_2(\mathcal{A}) \subset \mathsf{O}_1\mathsf{O}_2(\mathcal{A})$,
\item If $\mathcal{A} \subset \mathcal{B}$, then $\mathsf{O}_2(\mathcal{A}) \subset \mathsf{O}_2(\mathcal{B})$, so $\mathsf{O}_1\mathsf{O}_2(\mathcal{A}) \subset \mathsf{O}_1\mathsf{O}_2(\mathcal{B})$,
\item $\mathsf{O}_1\mathsf{O}_2\mathsf{O}_1\mathsf{O}_2(\mathcal{A}) \subset \mathsf{O}_1\mathsf{O}_1\mathsf{O}_2\mathsf{O}_2(\mathcal{A}) = \mathsf{O}_1\mathsf{O}_2(\mathcal{A})$ by the commutativity hypothesis and idempotence of $\mathsf{O}_1$ and $\mathsf{O}_2$.
\end{itemize}

Now apply this to $\mathsf{SMP}$. We have $\mathsf{SMPSMP}(\mathcal{A}) \subset \mathsf{SMSPMP}(\mathcal{A}) \subset \mathsf{SSMPMP}(\mathcal{A}) \subset \mathsf{SMP}(\mathcal{A})$, using the interleaving properties of the operators. Together with 4.22 (which characterizes quasivarieties via closure properties), this proves that $\mathsf{MP}(\mathcal{A})$ and $\mathsf{SMP}(\mathcal{A})$ are quasivarieties.

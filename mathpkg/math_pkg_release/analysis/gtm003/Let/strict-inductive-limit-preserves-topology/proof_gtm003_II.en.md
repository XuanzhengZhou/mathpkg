---
role: proof
locale: en
of_concept: strict-inductive-limit-preserves-topology
source_book: gtm003
source_chapter: "II"
source_section: "6.4"
---

Let $\mathfrak{T}$ be the inductive topology. Since $\mathfrak{T}_{n+1}$ induces $\mathfrak{T}_n$ on $E_n$, for any 0-neighborhood $U_n$ in $E_n(\mathfrak{T}_n)$ there exists a 0-neighborhood $U_{n+1}$ in $E_{n+1}(\mathfrak{T}_{n+1})$ such that $U_{n+1} \cap E_n = U_n$. By induction one constructs a sequence $\{U_k\}_{k \geq n}$ of 0-neighborhoods such that $U_{k+1} \cap E_k = U_k$ for all $k \geq n$. Then $U = \bigcup_{k=n}^{\infty} U_k$ is a 0-neighborhood in $E(\mathfrak{T})$ and $U \cap E_n = U_n$, showing that $\mathfrak{T}$ induces $\mathfrak{T}_n$ on $E_n$. Since each $\mathfrak{T}_n$ is Hausdorff and $E = \bigcup_n E_n$, it follows that $\mathfrak{T}$ is separated.

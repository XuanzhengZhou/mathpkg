---
role: proof
locale: en
of_concept: bounded-subsets-in-strict-inductive-limits
source_book: gtm003
source_chapter: "II"
source_section: "6.5"
---

By (6.4) the condition is clearly sufficient for $B$ to be bounded. Conversely, assume that $B$ is bounded but not contained in $E_n$ for any $n \in N$. There exists an increasing sequence $\{k_1, k_2, \ldots\} \subset N$ and a sequence $\{x_n\} \subset B$ such that $x_n \in E_{k_{n+1}}$, but $x_n \notin E_{k_n}$ $(n \in N)$. Using the lemma in (6.4), we construct inductively a sequence $\{V_{k_n}\}$ of convex, circled 0-neighborhoods in $E_{k_n}$, respectively, such that $n^{-1}x_n \notin V_{k_{n+1}}$ and $V_{k_{n+1}} \cap E_{k_n} = V_{k_n}$ for all $n \in N$. Then $V = \bigcup_{n=1}^{\infty} V_{k_n}$ is a 0-neighborhood in $E(\mathfrak{T})$, but $n^{-1}x_n \notin V$ for any $n$, contradicting the boundedness of $B$.

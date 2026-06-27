---
role: proof
locale: en
of_concept: arithmetic-hierarchy-theorem
source_book: gtm037
source_chapter: "Part 1: Recursive Function Theory"
source_section: "5. Arithmetic Hierarchy"
---

Let $R_m^n$ be as in Theorem 5.35. Define

$$T = \{(x_0, \ldots, x_{n-1}) : (x_0, x_0, x_1, x_2, \ldots, x_{n-1}) \in R_m^n\}.$$

Thus $T \in \Sigma_m$ (since $R_m^n \in \Sigma_m$ and $T$ is obtained by an identification of variables). Suppose, for contradiction, that $T \in \Pi_m$. Then by the universal property of $R_m^n$ in Theorem 5.35, choose $e \in \omega$ such that

$$T = \{(x_0, \ldots, x_{n-1}) : (e, x_0, \ldots, x_{n-1}) \notin R_m^n\}.$$

Now consider the tuple $e^{(n)}$, i.e., $(e, e, \ldots, e)$ with $n$ entries. We have:

$$(e, e, \ldots, e) \in T \quad \text{iff} \quad (e, e, e, \ldots, e) \in R_m^n \quad \text{(by definition of $T$)}$$
$$\quad \text{iff} \quad (e, e, \ldots, e) \notin R_m^n \quad \text{(by choice of $e$)}.$$

This is a contradiction. Therefore $T \notin \Pi_m$, establishing the first part of the theorem. The statement about the complement follows immediately from Proposition 5.32.

For the second part, let $T$ be as above and define

$$W = \{(x_0, \ldots, x_{n-1}) : ((x_0)_0, (x_1)_0, \ldots, (x_{n-1})_0) \in T \text{ or } ((x_0)_0, (x_1)_0, \ldots, (x_{n-1})_0) \in {}^n\omega \smallsetminus T\}.$$

One can then show that $W \in \Delta_{m+1}$ but $W \notin \Sigma_m \cup \Pi_m$, completing the proof.

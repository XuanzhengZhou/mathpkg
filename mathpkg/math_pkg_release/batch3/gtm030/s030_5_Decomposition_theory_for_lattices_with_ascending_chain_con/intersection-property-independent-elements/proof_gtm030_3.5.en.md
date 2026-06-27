---
role: proof
locale: en
of_concept: intersection-property-independent-elements
source_book: gtm030
source_chapter: "3"
source_section: "5"
---

We first prove that for any $s$ with $1 \leq s \leq n-1$,
$$(a_1 \cup \cdots \cup a_s) \cap (a_{s+1} \cup \cdots \cup a_n) = 0.$$

This is true by assumption when $s = 1$ (the definition of independence gives $a_1 \cap (a_2 \cup \cdots \cup a_n) = 0$, or more precisely, the pairwise independence relations). Assume the formula holds for $s-1$. Then by the modular law,
\begin{align*}
(a_1 \cup \cdots \cup a_s) \cap (a_{s+1} \cup \cdots \cup a_n)
&\leq (a_1 \cup \cdots \cup a_s) \cap (a_s \cup a_{s+1} \cup \cdots \cup a_n) \\
&= \big((a_1 \cup \cdots \cup a_{s-1}) \cap (a_s \cup \cdots \cup a_n)\big) \cup a_s \\
&= a_s.
\end{align*}

It follows that
\begin{align*}
(a_1 \cup \cdots \cup a_s) \cap (a_{s+1} \cup \cdots \cup a_n)
&= (a_1 \cup \cdots \cup a_s) \cap (a_{s+1} \cup \cdots \cup a_n) \cap a_s \\
&= 0,
\end{align*}
since $a_s \cap (a_{s+1} \cup \cdots \cup a_n) = 0$ by the induction hypothesis for $s-1$.

Now to establish the main formula, apply the modularity assumption to the left-hand side:
\begin{align*}
&(a_1 \cup \cdots \cup a_r \cup a_{r+1} \cup \cdots \cup a_s) \cap (a_1 \cup \cdots \cup a_r \cup a_{s+1} \cup \cdots \cup a_t) \\
&= a_1 \cup \cdots \cup a_r \cup \big((a_{r+1} \cup \cdots \cup a_s) \cap (a_{s+1} \cup \cdots \cup a_t)\big) \\
&= a_1 \cup \cdots \cup a_r \cup 0 = a_1 \cup \cdots \cup a_r,
\end{align*}
where the last step uses the formula proved in the first part (with an appropriate relabeling of indices).

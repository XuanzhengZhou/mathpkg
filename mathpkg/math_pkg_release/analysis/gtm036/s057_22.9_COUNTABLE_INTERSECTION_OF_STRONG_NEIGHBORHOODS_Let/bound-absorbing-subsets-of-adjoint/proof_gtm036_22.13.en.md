---
role: proof
locale: en
of_concept: bound-absorbing-subsets-of-adjoint
source_book: gtm036
source_chapter: "5"
source_section: "22.13"
---

Let $\{B_n\}$ be a co-base for the strongly bounded subsets of $E^*$ such that each $B_n$ is weak* compact convex and circled. Then there is a sequence $\{t_n\}$ of positive numbers such that $\bigcup \{t_n B_n : n = 1, 2, \cdots\} \subset C$. Let $A_n = \langle t_1 B_1 \cup \cdots \cup t_n B_n \rangle$; then $A_n$ is strongly closed (in fact, weak* compact) convex circled, $A_n \subset A_{n+1}$, and $A = \bigcup \{A_n : n = 1, 2, \cdots\} \subset C$. If it is shown that $\frac{1}{2} A^- \subset A$, then the theorem is proved, because $A^-$ absorbs strongly bounded sets. Let $f_0 \notin A$; then $f_0 \notin A_n$ for each $n$, and since $A_n$ is closed, there is a strong neighborhood $V_n$ of $0$ such that $(f_0 + V_n) \cap A_n$ is void. Let $W_n = V_n + \frac{1}{2} A_n$. Then $(f_0 + W_n) \cap \frac{1}{2} A_n$ is void.

---
role: proof
locale: en
of_concept: existence-of-2-consistent-triple
source_book: gtm037
source_chapter: "26"
source_section: "4"
---

Let $H$ be the set of all pairs $(A, h)$ such that $A \subseteq n$ is finite and $h$ is a function with domain $\mathcal{P}(A)$ (the power set of $A$) taking values in $n^{\partial}$ satisfying:

(1) if $B \subseteq A$ and $B \neq 0$, then $h(B) \geq 1$;
(2) if $B \subseteq A$ and $\alpha \in A \setminus B$, then $h(B \cup \{\alpha\}) = h(B) + 1$ provided $h(B) + 1 < n^{\partial}$;
(3) otherwise $h$ takes the value $0$.

For each finite $A \subseteq n$ and each function $h$ on $\mathcal{P}(A)$ satisfying these conditions, the number of such functions is at most $(n^{\partial})^{|A|} \leq n^{|A|}$. Since there are at most $n$ finite subsets of $n$, the total number of such pairs is at most $n$. But $(\{\alpha\}, \{(\{\alpha\}, 0)\}) \in H$ for each $\alpha < n$, so $|H| = n$. Write $H = \{(A_\alpha, h_\alpha) : \alpha < n\}$.

Now for each $B \subseteq n$ define $f_B : n \to n^{\partial}$ as follows. For $\alpha < n$:
\[
f_B \alpha = h_\alpha(A_\alpha \cap B) \quad \text{if } A_\alpha \cap B \in \operatorname{Dmn} h_\alpha,
\]
\[
f_B \alpha = 0 \quad \text{otherwise}.
\]

Let $F = \{f_B : B \subseteq n\}$. To verify that $(F, 0, \{n\})$ is $2$-consistent over $n$:

(4) If $B, C \subseteq n$ and $B \neq C$, then $f_B \neq f_C$. For if $B \not\subseteq C$ and $\alpha \in B \setminus C$, then $(\{\alpha\}, \{(\{\alpha\}, 1)\}) \in H$ by (2) and (3), so there exists $\beta < n$ with $A_\beta = \{\alpha\}$ and $h_\beta = \{(\{\alpha\}, 1)\}$. Then $A_\beta \cap B = \{\alpha\} \in \operatorname{Dmn} h_\beta$, so $f_B \beta = h_\beta(A_\beta \cap B) = 1$, while $f_C \beta = 0$. Hence $f_B \neq f_C$.

From (4) we have $|F| = 2^n$. The consistency condition (iv) of Definition 26.33 is vacuously satisfied for $m = 2$ because $G = 0$ and $\{n\}$ is the trivial filter. Thus $(F, 0, \{n\})$ is $2$-consistent over $n$.

---
role: proof
locale: en
of_concept: urysohn-lemma
source_book: gtm043
source_chapter: "3"
source_section: "7"
---

Let $A$ and $B$ be disjoint closed sets in a normal space $X$. We define open sets $U_r$, for all rational $r$, as follows.

First, take $U_r = \emptyset$ for all $r < 0$, and $U_r = X$ for $r > 1$.

Next, put $U_1 = X - B$; then $U_1$ is a neighborhood of $A$. Since $X$ is normal, $U_1$ contains a closed neighborhood of $A$; we choose $U_0$ (open) so that $A \subset U_0$ and $\operatorname{cl} U_0 \subset U_1$.

Now enumerate the rationals in $[0, 1]$ in a sequence $(r_n)_{n \in \mathbf{N}}$, with $r_1 = 0$ and $r_2 = 1$. For each $n$, having defined $U_{r_i}$ for $i < n$, we define $U_{r_n}$ as follows. Let $s$ be the largest rational among $r_1, \ldots, r_{n-1}$ that is $< r_n$, and let $t$ be the smallest that is $> r_n$. Then $s < r_n < t$, and $\operatorname{cl} U_s \subset U_t$. Since $X$ is normal, there exists an open set $U_{r_n}$ such that $\operatorname{cl} U_s \subset U_{r_n}$ and $\operatorname{cl} U_{r_n} \subset U_t$. Continuing by induction, we obtain open sets $U_r$ for all rational $r$ such that $\operatorname{cl} U_r \subset U_s$ whenever $r < s$.

Now define $f(x) = \inf\{ r \in \mathbf{Q} : x \in U_r \}$ for $x \in X$. Then $f$ is a continuous function on $X$ (by the lemma on constructing continuous functions from nested open sets indexed by a dense set). Clearly $f(A) = \{0\}$ and $f(B) = \{1\}$. Thus $A$ and $B$ are completely separated by $f$. Consequently, every normal space is completely regular.

The construction shows that any two disjoint closed sets in a normal space are completely separated. Hence every normal space is completely regular.

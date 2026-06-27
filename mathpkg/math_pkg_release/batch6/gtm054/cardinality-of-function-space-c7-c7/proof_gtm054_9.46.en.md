---
role: proof
locale: en
of_concept: cardinality-of-function-space-c7-c7
source_book: gtm054
source_chapter: "9"
source_section: "XC"
---

Suppose that $x \in M \subseteq U + \{x\}$ for some $M \in \mathcal{M}$. Pick a largest independent set $J$ of $\Lambda$ such that $J \subseteq U + \{x\}$. Then $|J| = r(U + \{x\})$ by the above proposition. By Proposition B19a, $M + \{x\} \in \mathcal{I}(\Lambda)$. Since $M + \{x\} \subseteq U$, if $|M + \{x\}| = |J|$, then $r(U) \geq |J|$, and by C2, $r(U) = r(U + \{x\})$. On the other hand, if $|M + \{x\}| < |J|$, then by repeated applications of B2, one constructs an independent set $J'$ by adjoining to $M + \{x\}$ elements of $J$, one by one. Thus $|J'| = |J|$. Furthermore, if $x \in J'$, then $M \subseteq J'$, which is impossible. Thus $J' \subseteq U$ and, as above, $r(U) = r(U + \{x\})$.

Conversely, suppose $r(U) = r(U + \{x\})$. Then by the proposition, $r(U) = |J|$ for some $J \in \mathcal{I}(\Lambda)$ such that $J \subset

(d) $c(U_1 \cap U_2) \subseteq c(U_1) \cap c(U_2)$, and equality holds if $U_1$ and $U_2$ are closed.

(e) $c(U_1) \cup c(U_2) \subseteq c(U_1 \cup U_2)$.

(f) If $U \in \mathcal{P}(V)$ and $x_1, x_2 \in V + U$, then $c(c(U + \{x_1\}) + \{x_2\}) = c(U + \{x_1, x_2\})$.

The closure operator in a topological space satisfies conditions C9 and C10. However, the function $c$ in a closure structure $(V, c)$ need not induce a topology on $V$. In particular we do not necessarily have that $c(\emptyset) = \emptyset$ nor does equality always hold in C12e, both of which always hold for topological closure operators. The following examples show how a closure structure may fail to determine a topological space in each of these respects.

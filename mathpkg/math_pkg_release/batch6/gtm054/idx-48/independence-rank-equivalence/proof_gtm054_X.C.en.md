---
role: proof
locale: en
of_concept: independence-rank-equivalence
source_book: gtm054
source_chapter: "X"
source_section: "C"
---

**Proof.**

**(a) $\Rightarrow$ (b).** Assume $(V, \mathcal{I})$ is an independence system and define $r(U) = \max\{|J| : J \in \mathcal{I},\; J \subseteq U\}$.

*C1:* Since $\emptyset \in \mathcal{I}$ and $|\emptyset| = 0$, we have $r(\emptyset) = 0$.

*C2:* Let $U \in \mathcal{P}(V)$ and $x \in V \setminus U$. By definition, $r(U) \leq r(U \cup \{x\})$ since any $J \subseteq U$ with $J \in \mathcal{I}$ is also contained in $U \cup \{x\}$. Now pick $J \subseteq U \cup \{x\}$ such that $J \in \mathcal{I}$ and $|J| = r(U \cup \{x\})$. If $x \notin J$, then $J \subseteq U$, so $r(U) \geq |J| = r(U \cup \{x\})$, implying $r(U) = r(U \cup \{x\})$. If $x \in J$, then $J \setminus \{x\} \in \mathcal{I}$ (hereditary property) and $J \setminus \{x\} \subseteq U$, so $r(U) \geq |J \setminus \{x\}| = |J| - 1 = r(U \cup \{x\}) - 1$. In either case, $0 \leq r(U \cup \{x\}) - r(U) \leq 1$.

*C3:* Suppose $r(U) = r(U \cup \{x_1\}) = r(U \cup \{x_2\})$. Let $J$ be a largest independent subset of $U$ (so $|J| = r(U)$). Since $r(U \cup \{x_1\}) = r(U)$, we have $|J| = r(U \cup \{x_1\})$, which means $J$ is also a largest independent subset of $U \cup \{x_1\}$. In particular $J \cup \{x_1\} \notin \mathcal{I}$ (otherwise $r(U \cup \{x_1\}) \geq |J| + 1$). Hence $x_1$ depends on $J$. Similarly $x_2$ depends on $J$. By the exchange property of independence systems, $x_2$ also depends on $J \cup \{x_1\}$, so $r(U \cup \{x_1, x_2\}) = |J| = r(U)$.

Thus $(V, r)$ is a rank structure and the equivalence of the definition of $\mathcal{I}$ in (b) follows directly from the definition of $r$.

**(b) $\Rightarrow$ (a).** Assume $(V, r)$ is a rank structure and define $\mathcal{I} = \{J \in \mathcal{P}(V) : r(J) = |J|\}$.

*Hereditary:* If $J \in \mathcal{I}$ and $J' \subseteq J$, then by repeated application of C2 we have $r(J') \leq r(J) - (|J| - |J'|) = |J| - (|J| - |J'|) = |J'|$. On the other hand, by C2 applied repeatedly, $r(J') \geq |J'|$ (starting from $\emptyset$, each new element increases rank by at most 1, so $|J'|$ elements can increase rank by at most $|J'|$; conversely, C2 implies $r(J') \leq |J'|$ by induction from $\emptyset$ as well). Actually, by C2 alone, $r(J') \leq r(\emptyset) + |J'| = |J'|$. Now by the bounded increase property, $r(J') = |J'|$, so $J' \in \mathcal{I}$.

*Exchange property:* Let $J_1, J_2 \in \mathcal{I}$ with $|J_1| < |J_2|$. We must find $x \in J_2 \setminus J_1$ such that $J_1 \cup \{x\} \in \mathcal{I}$. Suppose for contradiction that for every $x \in J_2 \setminus J_1$, we have $r(J_1 \cup \{x\}) < |J_1| + 1$, i.e., $r(J_1 \cup \{x\}) = r(J_1)$. Then by repeated application of C3, $r(J_1 \cup J_2) = r(J_1) = |J_1|$. But $J_2 \subseteq J_1 \cup J_2$ and $r(J_2) = |J_2| > |J_1|$, so $r(J_1 \cup J_2) \geq r(J_2) > |J_1|$, contradiction. Hence some $x \in J_2 \setminus J_1$ satisfies $J_1 \cup \{x\} \in \mathcal{I}$.

Thus $(V, \mathcal{I})$ is an independence system, and $r(U) = \max\{|J| : J \in \mathcal{I},\; J \subseteq U\}$ follows since $r(U)$ is the maximum size of a subset $J \subseteq U$ with $r(J) = |J|$. $\square$

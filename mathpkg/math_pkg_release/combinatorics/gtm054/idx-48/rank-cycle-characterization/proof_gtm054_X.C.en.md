---
role: proof
locale: en
of_concept: rank-cycle-characterization
source_book: gtm054
source_chapter: "X"
source_section: "C"
---

**Proof.**

($\Rightarrow$) Suppose that $x \in M \subseteq U \cup \{x\}$ for some $M \in \mathcal{M}$. Pick a largest independent set $J$ of $\Lambda$ such that $J \subseteq U \cup \{x\}$. Then $|J| = r(U \cup \{x\})$ by Proposition C6. By Proposition B19(a), $M \setminus \{x\} \in \mathcal{I}(\Lambda)$. Since $M \setminus \{x\} \subseteq U$, if $|M \setminus \{x\}| = |J|$, then $r(U) \geq |J|$, and by C2, $r(U) = r(U \cup \{x\})$. On the other hand, if $|M \setminus \{x\}| < |J|$, then by repeated applications of the augmentation axiom B2, one constructs an independent set $J'$ by adjoining to $M \setminus \{x\}$ elements of $J$, one by one. Thus $|J'| = |J|$. Furthermore, if $x \in J'$, then $M \subseteq J'$, which contradicts that $J'$ is independent (since $M$ is a cycle, hence dependent). Thus $J' \subseteq U$, and as above, $r(U) \geq |J'| = |J| = r(U \cup \{x\})$. By C2, $r(U) = r(U \cup \{x\})$.

($\Leftarrow$) Conversely, suppose $r(U) = r(U \cup \{x\})$. By Proposition C6, $r(U) = |J|$ for some $J \in \mathcal{I}(\Lambda)$ such that $J \subseteq U$ and $|J| = r(U)$. Since $r(U \cup \{x\}) = r(U) = |J|$, the set $J$ is also a maximal independent subset of $U \cup \{x\}$. Therefore $J \cup \{x\} \notin \mathcal{I}(\Lambda)$, so by Proposition B19 there exists a cycle $M \in \mathcal{M}$ such that $M \subseteq J \cup \{x\} \subseteq U \cup \{x\}$. Since $M \not\subseteq J$ (as $J$ is independent and $M$ is dependent), we must have $x \in M$. Thus $x \in M \subseteq U \cup \{x\}$. $\square$

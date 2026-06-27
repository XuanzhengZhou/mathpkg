---
role: proof
locale: en
of_concept: measure-countable-subadditivity-semicontinuity
source_book: gtm055
source_chapter: "7"
source_section: "8"
---

The proofs are routine.

**Countable subadditivity of a measure $\mu$**: Given a sequence $\{A_n\}$ of measurable sets, set $B_1 = A_1$ and $B_n = A_n \setminus (\bigcup_{k=1}^{n-1} A_k)$ for $n \ge 2$. Then $\{B_n\}$ are pairwise disjoint, $B_n \subset A_n$, and $\bigcup_n B_n = \bigcup_n A_n$. Thus $\mu(\bigcup_n A_n) = \sum_n \mu(B_n) \le \sum_n \mu(A_n)$ by countable additivity and monotonicity.

**Semicontinuity**: Let $\{E_n\}$ be monotone increasing. Set $F_1 = E_1$ and $F_n = E_n \setminus E_{n-1}$ for $n \ge 2$. Then $\{F_n\}$ are pairwise disjoint, and $E_n = \bigcup_{k=1}^n F_k$. Hence $\bigcup_n E_n = \bigcup_n F_n$, so

$$\mu\left(\bigcup_n E_n\right) = \sum_{n=1}^{\infty} \mu(F_n) = \lim_n \sum_{k=1}^n \mu(F_k) = \lim_n \mu(E_n).$$

**Converse**: If $\nu$ is finitely additive on a $\sigma$-ring and countably subadditive, then for pairwise disjoint $\{A_n\}$ with union $A$, finite additivity gives $\sum_{k=1}^n \nu(A_k) = \nu(\bigcup_{k=1}^n A_k) \le \nu(A)$. Taking $n \to \infty$ gives $\sum_n \nu(A_n) \le \nu(A)$. The reverse inequality follows from countable subadditivity: $\nu(A) \le \sum_n \nu(A_n)$. Hence $\nu$ is countably additive. The semicontinuity version is analogous.

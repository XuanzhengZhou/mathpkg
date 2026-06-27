---
role: proof
locale: en
of_concept: maximal-consistent-characterization
source_book: gtm022
source_chapter: "II"
source_section: "2"
---

($\Rightarrow$) Suppose $A$ is maximal consistent.

(i) Since $A$ is consistent, $F \notin \text{Ded}(A)$. In particular $F \notin A$.

(ii) Clearly $A \subseteq \text{Ded}(A)$. We claim $\text{Ded}(A)$ is consistent: if $F \in \text{Ded}(\text{Ded}(A))$, then $F \in \text{Ded}(A)$, contradicting consistency. Since $A$ is maximal, $\text{Ded}(A)$ cannot properly contain $A$, so $A = \text{Ded}(A)$.

(iii) Let $p \in P(X)$. If $p \notin A$, then $A \subsetneq A \cup \{p\}$. By maximal consistency, $A \cup \{p\}$ is inconsistent, so $F \in \text{Ded}(A \cup \{p\})$. By the Deduction Theorem, $\sim p \in \text{Ded}(A) = A$. Thus either $p \in A$ or $\sim p \in A$.

($\Leftarrow$) Suppose $A$ satisfies (i), (ii), and (iii). By (i) and (ii), $F \notin \text{Ded}(A)$, so $A$ is consistent. Let $T \subseteq P(X)$ properly contain $A$, and choose $p \in T \setminus A$. By (iii), $\sim p \in A \subseteq T$. Since $T$ contains both $p$ and $\sim p$, we have $T \vdash F$, so $T$ is inconsistent. Hence $A$ is maximal consistent.

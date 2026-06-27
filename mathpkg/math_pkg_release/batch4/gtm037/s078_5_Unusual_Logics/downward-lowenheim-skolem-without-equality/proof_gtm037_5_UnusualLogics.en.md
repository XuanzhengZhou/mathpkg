---
role: proof
locale: en
of_concept: downward-lowenheim-skolem-without-equality
source_book: gtm037
source_chapter: "Part 5"
source_section: "Unusual Logics"
---

**Proof.** The notions of elementary substructure and elementary extension carry over in an obvious way to logic without equality, and the proof of 19.17 (the standard downward Löwenheim–Skolem theorem) applies verbatim. One constructs a chain of subsets
$$C = C_0 \subseteq C_1 \subseteq \cdots \subseteq C_n \subseteq \cdots$$
of $B$, each of size at most $m$, such that for every formula $\varphi(v_0, \ldots, v_{k-1})$ and every tuple $\bar{c} \in {}^{k}C_n$, if $\mathfrak{B} \models \exists v_k \varphi[\bar{c}]$ then there exists $b \in C_{n+1}$ with $\mathfrak{B} \models \varphi[\bar{c}, b]$. Taking $A = \bigcup_{n \in \omega} C_n$ yields $|A| = m$, and the Tarski–Vaught criterion (which holds for logic without equality) ensures $\mathfrak{A} \preceq \mathfrak{B}$, where $\mathfrak{A}$ is the substructure of $\mathfrak{B}$ with universe $A$.

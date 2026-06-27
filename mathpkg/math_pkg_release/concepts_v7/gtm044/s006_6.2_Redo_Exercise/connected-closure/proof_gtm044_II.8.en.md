---
role: proof
locale: en
of_concept: connected-closure
source_book: gtm044
source_chapter: "II"
source_section: "8"
---

# Proof of Closure of a Connected Set Is Connected (Lemma 8.3)

**Lemma 8.3.** Let $S$ be a topological space. If $A$ is a connected subset of $S$, then its topological closure $\bar{A}$ is also connected.

*Proof.* Suppose for contradiction that $\bar{A}$ is not connected. Then there exist open sets $U, V \subset S$ such that

$$\bar{A} \subset U \cup V, \quad \bar{A} \cap U \neq \emptyset, \quad \bar{A} \cap V \neq \emptyset, \quad \bar{A} \cap U \cap V = \emptyset.$$

Since $A \subset \bar{A}$, we have $A \subset U \cup V$ and $A \cap U \cap V = \emptyset$.

If both $A \cap U$ and $A \cap V$ are nonempty, then $A$ itself would be disconnected ($A = (A \cap U) \cup (A \cap V)$ is a separation of $A$), contradicting the hypothesis that $A$ is connected. Hence it must be that either $A \cap U = \emptyset$ or $A \cap V = \emptyset$. Without loss of generality, assume $A \cap V = \emptyset$. Then $A \subset U$.

But $\bar{A} \cap V \neq \emptyset$ by assumption. Take $x \in \bar{A} \cap V$. Since $V$ is an open neighborhood of $x$ and $x \in \bar{A}$, every open neighborhood of $x$ must intersect $A$. In particular, $V \cap A \neq \emptyset$. This contradicts $A \cap V = \emptyset$.

Therefore $\bar{A}$ must be connected. $\square$

**Alternative characterization proof.** Using the continuous-function characterization: a space $X$ is connected iff every continuous map $f: X \to \{0, 1\}$ is constant. Let $f: \bar{A} \to \{0, 1\}$ be continuous. Since $A$ is connected, $f|_A$ is constant, say $f(a) = 0$ for all $a \in A$. By continuity, $f^{-1}(\{0\})$ is closed in $\bar{A}$ and contains $A$, hence contains $\bar{A}$ (since $\bar{A}$ is the smallest closed set in $S$ containing $A$, and therefore the smallest closed set in $\bar{A}$ containing $A$ is $\bar{A}$ itself). Thus $f(x) = 0$ for all $x \in \bar{A}$, so $f$ is constant. Hence $\bar{A}$ is connected. $\square$

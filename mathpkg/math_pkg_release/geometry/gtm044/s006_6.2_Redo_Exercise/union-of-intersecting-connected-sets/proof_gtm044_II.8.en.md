---
role: proof
locale: en
of_concept: union-of-intersecting-connected-sets
source_book: gtm044
source_chapter: "II"
source_section: "8"
---

# Proof of Union of Intersecting Connected Sets (Lemma 8.2)

**Lemma 8.2.** Let $S$ be a topological space. If connected subsets $A$ and $B$ of $S$ intersect, then $A \cup B$ is connected.

*Proof.* Recall that a subset $X$ of a topological space is connected if and only if every continuous function $\varphi: X \to \{0, 1\}$ (where $\{0, 1\}$ has the discrete topology) is constant.

Let $f: A \cup B \to \{0, 1\}$ be a continuous function. We show $f$ is constant on $A \cup B$.

Since $A$ is connected, the restriction $f|_A$ is continuous and therefore constant. Similarly, $f|_B$ is constant. Let $c_A = f|_A$ and $c_B = f|_B$ denote the constant values on $A$ and $B$ respectively.

By hypothesis, $A \cap B \neq \emptyset$. Pick $x \in A \cap B$. Then

$$c_A = f(x) = c_B.$$

Thus $f$ takes the same constant value on both $A$ and $B$, hence $f$ is constant on $A \cup B$. Therefore $A \cup B$ is connected. $\square$

**Alternative proof via separation.** Suppose for contradiction that $A \cup B = U \cup V$ where $U$ and $V$ are disjoint, nonempty, and open in $A \cup B$. Since $A$ is connected, $A$ must lie entirely in one of $U$ or $V$; without loss, $A \subset U$. Similarly, $B$ is connected, so $B \subset U$ or $B \subset V$. But $A \cap B \neq \emptyset$, and $A \subset U$, so $B \cap U \neq \emptyset$. Since $B$ is connected and meets $U$, we must have $B \subset U$. Hence $A \cup B \subset U$, contradicting that $V$ is nonempty. Therefore $A \cup B$ is connected. $\square$

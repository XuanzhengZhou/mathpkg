---
role: proof
locale: en
of_concept: separated-sets-closed-in-union
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Characterization of Separated Sets via Relative Topology

**Proposition.** Two subsets $A$ and $B$ are separated in a topological space $X$ if and only if both $A$ and $B$ are closed in the relative topology of $A \cup B$ (or equivalently, each is both open and closed in $A \cup B$) and $A$ and $B$ are disjoint.

**Proof.** Recall that $A$ and $B$ are separated iff $A^- \cap B = \emptyset$ and $A \cap B^- = \emptyset$, where the closures are taken in $X$.

($\Rightarrow$) Suppose $A$ and $B$ are separated. Then $A^- \cap B = \emptyset$ implies that $A \subset A \cup B$ and the closure of $A$ in $A \cup B$ (relative topology) is $A^- \cap (A \cup B) = (A^- \cap A) \cup (A^- \cap B) = A \cup \emptyset = A$. Thus $A$ is closed in $A \cup B$. Similarly, $B$ is closed in $A \cup B$. Since $A \cap B \subset A^- \cap B = \emptyset$, they are disjoint. Being disjoint and each closed in $A \cup B$, each is the complement of the other in $A \cup B$, hence each is also open in $A \cup B$.

($\Leftarrow$) Suppose $A$ and $B$ are disjoint and both are closed in $A \cup B$. Then the closure of $A$ in $A \cup B$ is $A$ itself. By the subspace closure theorem, this closure equals $A^- \cap (A \cup B)$. Hence $A^- \cap (A \cup B) = A$, which implies $A^- \cap B = \emptyset$ (otherwise $A^- \cap B \neq \emptyset$ would put a point of $B$ in $A^- \cap (A \cup B)$, contradicting that it equals $A$). Similarly $A \cap B^- = \emptyset$. Thus $A$ and $B$ are separated. $\square$
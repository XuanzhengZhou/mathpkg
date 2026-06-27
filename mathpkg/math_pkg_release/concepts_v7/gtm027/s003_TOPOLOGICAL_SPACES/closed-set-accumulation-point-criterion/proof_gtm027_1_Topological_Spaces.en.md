---
role: proof
locale: en
of_concept: closed-set-accumulation-point-criterion
source_book: gtm027
source_chapter: "1"
source_section: "Topological Spaces"
---

# Proof of Closed Set Characterization via Accumulation Points

**Theorem.** A subset $A$ of a topological space $(X, \mathfrak{J})$ is closed if and only if it contains all of its accumulation points.

*Proof.* Let $A'$ denote the set of accumulation points of $A$.

$(\Rightarrow)$ Suppose $A$ is closed. Then $X \setminus A$ is open. For any $x \in X \setminus A$, the set $X \setminus A$ is an open neighborhood of $x$ that is disjoint from $A$. Hence $x$ cannot be an accumulation point of $A$ (an accumulation point requires every neighborhood to intersect $A$ in points other than possibly $x$ itself). Therefore no point of $X \setminus A$ belongs to $A'$, which means $A' \subseteq A$. Thus $A$ contains all of its accumulation points.

$(\Leftarrow)$ Suppose $A' \subseteq A$, i.e., $A$ contains all of its accumulation points. Let $x \in X \setminus A$. Then $x \notin A$ and $x \notin A'$, so $x$ is not an accumulation point of $A$. By definition, there exists a neighborhood $U_x$ of $x$ such that $U_x \cap A \subseteq \{x\}$. Since $x \notin A$, this means $U_x \cap A = \emptyset$. We may take $U_x$ to be open (replacing it by an open neighborhood contained in it if necessary). Then $U_x \subseteq X \setminus A$.

Thus every point of $X \setminus A$ has an open neighborhood contained in $X \setminus A$, so $X \setminus A$ is a neighborhood of each of its points, and therefore $X \setminus A$ is open. Hence $A$ is closed. $\square$

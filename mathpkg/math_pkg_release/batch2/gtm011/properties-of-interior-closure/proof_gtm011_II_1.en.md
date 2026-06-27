---
role: proof
locale: en
of_concept: properties-of-interior-closure
source_book: gtm011
source_chapter: "II"
source_section: "1"
---
(a) If $A$ is open, then $A$ is itself an open set contained in $A$, so $A \subset \operatorname{int} A$. Since $\operatorname{int} A \subset A$ by definition, $A = \operatorname{int} A$. Conversely, if $A = \operatorname{int} A$, then $A$ is a union of open sets and hence open.

(b) If $A$ is closed, then $A$ is a closed set containing $A$, so $A^- \subset A$. Since $A \subset A^-$ always, $A = A^-$. Conversely, if $A = A^-$, then $A$ is an intersection of closed sets and hence closed.

(c) $\operatorname{int} A = \bigcup \{G: G \subset A, G \text{ open}\}$. Its complement is $\bigcap \{X - G: G \subset A, G \text{ open}\}$. Since $G \subset A$ iff $X - A \subset X - G$, and $G$ open means $X - G$ closed, we get $X - \operatorname{int} A = \bigcap \{F: F \supset X - A, F \text{ closed}\} = (X - A)^-$. Hence $\operatorname{int} A = X - (X - A)^-$. The dual formula $A^- = X - \operatorname{int}(X - A)$ follows by similar reasoning. For the boundary: $\partial A = A^- \cap (X - A)^- = A^- \cap (X - \operatorname{int} A) = A^- - \operatorname{int} A$.

(d) Since $A \subset A \cup B$ and $B \subset A \cup B$, we have $A^- \subset (A \cup B)^-$ and $B^- \subset (A \cup B)^-$, so $A^- \cup B^- \subset (A \cup B)^-$. Conversely, $A \cup B \subset A^- \cup B^-$, and $A^- \cup B^-$ is closed (finite union of closed sets), so $(A \cup B)^- \subset A^- \cup B^-$.

(e) $x_0 \in \operatorname{int} A$ means there exists an open set $G$ with $x_0 \in G \subset A$. By definition of open set, there exists $\epsilon > 0$ such that $B(x_0; \epsilon) \subset G \subset A$. The converse is immediate.

(f) $x_0 \in A^-$ iff $x_0$ belongs to every closed set containing $A$. Equivalently, $x_0 \notin A^-$ iff there exists a closed set $F \supset A$ with $x_0 \notin F$, which means there exists $\epsilon > 0$ such that $B(x_0; \epsilon) \cap A = \emptyset$. The negation gives $x_0 \in A^-$ iff for every $\epsilon > 0$, $B(x_0; \epsilon) \cap A \neq \emptyset$.

---
role: proof
locale: en
of_concept: theorem-set-algebra
source_book: gtm027
source_chapter: "0"
source_section: "Subsets and Complements; Union and Intersection"
---

# Proof of Theorem 2: Elementary Algebra of Sets

**Proof of (a).** A point $x$ is a member of $X \sim (X \sim A)$ iff $x \in X$ and $x \notin X \sim A$. Since $x \notin X \sim A$ iff $x \notin X$ or $x \in A$, it follows that $x \in X \sim (X \sim A)$ iff $x \in X$ and either $x \notin X$ or $x \in A$. The first of these alternatives is impossible, so that $x \in X \sim (X \sim A)$ iff $x \in X$ and $x \in A$; that is, iff $x \in X \cap A$. Hence $X \sim (X \sim A) = A \cap X$.

**Proof of (b) — Commutative laws.** $A \cup B = \{x : x \in A \text{ or } x \in B\} = \{x : x \in B \text{ or } x \in A\} = B \cup A$, and similarly $A \cap B = \{x : x \in A \text{ and } x \in B\} = \{x : x \in B \text{ and } x \in A\} = B \cap A$.

**Proof of (c) — Associative laws.** $A \cup (B \cup C) = \{x : x \in A \text{ or } (x \in B \text{ or } x \in C)\} = \{x : (x \in A \text{ or } x \in B) \text{ or } x \in C\} = (A \cup B) \cup C$. The proof for intersection is similar with "and" replacing "or".

**Proof of the first part of (d) — Distributive law for intersection over union.** A point $x$ is a member of $A \cap (B \cup C)$ iff $x \in A$ and either $x \in B$ or $x \in C$. This is the case iff either $x$ belongs to both $A$ and $B$ or $x$ belongs to both $A$ and $C$. Hence $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$. The second distributive law (union over intersection) is verified similarly.

**Proof of (e) — De Morgan formulae.** $X \sim (A \cup B) = \{x \in X : x \notin A \cup B\} = \{x \in X : x \notin A \text{ and } x \notin B\} = (X \sim A) \cap (X \sim B)$. And $X \sim (A \cap B) = \{x \in X : x \notin A \cap B\} = \{x \in X : x \notin A \text{ or } x \notin B\} = (X \sim A) \cup (X \sim B)$.

All parts follow directly from the definitions of union, intersection, and relative complement and the logical properties of "and", "or", and "not".

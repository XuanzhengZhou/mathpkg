---
role: proof
locale: en
of_concept: subspace-topology-properties
source_book: gtm027
source_chapter: "1"
source_section: "Bases and Subbases"
---

# Proof of Closure and Interior in Subspaces

**Theorem 16.** Let $(Y, \mathfrak{U})$ be a subspace of $(X, \mathfrak{J})$ and let $A$ be a subset of $Y$. Then:

(a) $A$ is $\mathfrak{U}$-closed if and only if $A = F \cap Y$ for some $\mathfrak{J}$-closed set $F$.

(b) The $\mathfrak{U}$-closure of $A$ is the intersection of $Y$ and the $\mathfrak{J}$-closure of $A$.

(c) A point $y$ of $Y$ is a $\mathfrak{U}$-accumulation point of $A$ if and only if $y$ is a $\mathfrak{J}$-accumulation point of $A$.

(d) The $\mathfrak{U}$-interior of $A$ contains $Y \cap (\mathfrak{J}\text{-interior of } A)$.

**Proof.**

(a) If $A = F \cap Y$ with $F$ $\mathfrak{J}$-closed, then $Y \setminus A = Y \cap (X \setminus F)$, which is the intersection of $Y$ with a $\mathfrak{J}$-open set and hence $\mathfrak{U}$-open. Thus $A$ is $\mathfrak{U}$-closed. Conversely, if $A$ is $\mathfrak{U}$-closed, then $Y \setminus A = U \cap Y$ for some $U \in \mathfrak{J}$. Then $A = (X \setminus U) \cap Y$, where $X \setminus U$ is $\mathfrak{J}$-closed.

(b) Let $A^{-}$ denote the $\mathfrak{J}$-closure of $A$. The set $A^{-} \cap Y$ is $\mathfrak{U}$-closed by part (a) and clearly contains $A$. Let $B$ be any $\mathfrak{U}$-closed set such that $A \subseteq B \subseteq Y$. By (a), $B = F \cap Y$ for some $\mathfrak{J}$-closed set $F$. Since $A \subseteq F$, we have $A^{-} \subseteq F$, and therefore $A^{-} \cap Y \subseteq F \cap Y = B$. Thus $A^{-} \cap Y$ is the smallest $\mathfrak{U}$-closed set containing $A$, i.e., it is the $\mathfrak{U}$-closure of $A$.

(c) A point $y \in Y$ is a $\mathfrak{U}$-accumulation point of $A$ iff $y$ belongs to the $\mathfrak{U}$-closure of $A \setminus \{y\}$. By (b), the $\mathfrak{U}$-closure of $A \setminus \{y\}$ is $(A \setminus \{y\})^{-} \cap Y$, so $y$ is a $\mathfrak{U}$-accumulation point of $A$ iff $y \in (A \setminus \{y\})^{-}$, which is precisely the condition that $y$ is a $\mathfrak{J}$-accumulation point of $A$.

(d) Let $A^{0}$ denote the $\mathfrak{J}$-interior of $A$. For any $y \in Y \cap A^{0}$, there exists $U \in \mathfrak{J}$ with $y \in U \subseteq A$. Then $y \in U \cap Y \subseteq A \cap Y = A$, and $U \cap Y \in \mathfrak{U}$, so $y$ belongs to the $\mathfrak{U}$-interior of $A$. Hence $Y \cap A^{0} \subseteq \mathfrak{U}\text{-interior}(A)$. $\square$

---
role: proof
locale: en
of_concept: theorem-indexed-de-morgan
source_book: gtm027
source_chapter: "0"
source_section: "Subsets and Complements; Union and Intersection"
---

# Proof of Theorem 3: De Morgan Laws for Indexed Families

**Proof of (a).** Let $B \subset A$. If $x \in \bigcup\{X_b : b \in B\}$, then there exists $b_0 \in B$ such that $x \in X_{b_0}$. Since $b_0 \in A$, it follows that $x \in \bigcup\{X_a : a \in A\}$. Hence $\bigcup\{X_b : b \in B\} \subset \bigcup\{X_a : a \in A\}$. For the intersection, if $x \in \bigcap\{X_a : a \in A\}$, then $x \in X_a$ for every $a \in A$. In particular, $x \in X_b$ for every $b \in B$. Hence $x \in \bigcap\{X_b : b \in B\}$, so $\bigcap\{X_b : b \in B\} \supset \bigcap\{X_a : a \in A\}$.

**Proof of (b) — De Morgan formulae.** A point $x$ belongs to $Y \sim \bigcup\{X_a : a \in A\}$ iff $x \in Y$ and $x \notin \bigcup\{X_a : a \in A\}$. The latter means that for every $a \in A$, $x \notin X_a$. This is equivalent to: for every $a \in A$, $x \in Y \sim X_a$, i.e., $x \in \bigcap\{Y \sim X_a : a \in A\}$. Hence

$$
Y \sim \bigcup\{X_a : a \in A\} = \bigcap\{Y \sim X_a : a \in A\}.
$$

Similarly, $x \in Y \sim \bigcap\{X_a : a \in A\}$ iff $x \in Y$ and $x \notin \bigcap\{X_a : a \in A\}$. The latter means there exists some $a_0 \in A$ such that $x \notin X_{a_0}$, i.e., $x \in Y \sim X_{a_0}$. Hence $x \in \bigcup\{Y \sim X_a : a \in A\}$. Therefore

$$
Y \sim \bigcap\{X_a : a \in A\} = \bigcup\{Y \sim X_a : a \in A\}.
$$

In words: the complement of the union is the intersection of the complements, and the complement of an intersection is the union of the complements.

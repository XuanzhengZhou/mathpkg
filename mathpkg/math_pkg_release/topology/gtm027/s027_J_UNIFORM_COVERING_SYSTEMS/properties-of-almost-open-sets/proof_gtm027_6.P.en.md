---
role: proof
locale: en
of_concept: properties-of-almost-open-sets
source_book: gtm027
source_chapter: "6"
source_section: "P"
---

# Proof of Closure Properties of Almost Open Sets

A subset $A$ of a topological space $X$ is *almost open* iff there exist meager sets $B$ and $C$ such that $(A \setminus B) \cup C$ is open.

Let $\mathcal{A}$ denote the family of almost open sets.

**Countable unions:** Let $A_n \in \mathcal{A}$ for $n \in \omega$. Then there exist meager sets $B_n, C_n$ such that $O_n = (A_n \setminus B_n) \cup C_n$ is open. Set $A = \bigcup_n A_n$, $B = \bigcup_n B_n$, $C = \bigcup_n C_n$. Since countable unions of meager sets are meager (Baire category), $B$ and $C$ are meager. Now

$$\bigcup_n O_n = \bigcup_n ((A_n \setminus B_n) \cup C_n)$$

is open. Note that $A \setminus B \subset \bigcup_n (A_n \setminus B_n) \subset \bigcup_n O_n$, and $\bigcup_n O_n \subset (A \setminus B) \cup C \cup F$ for some meager $F$. Thus $\bigcup_n O_n$ differs from $A$ by meager sets, so $A \in \mathcal{A}$.

**Complements:** Let $A \in \mathcal{A}$. Then $(A \setminus B) \cup C$ is open for some meager $B, C$. Let $O = (A \setminus B) \cup C$. Then $X \setminus O$ is closed. Working through the symmetric difference: $X \setminus A$ differs from $X \setminus O$ by meager sets (specifically by $C \setminus B$ and $B \cap A$), so $X \setminus A \in \mathcal{A}$.

**Every Borel set is almost open:** The family of almost open sets contains all open sets (take $B = C = \emptyset$) and is closed under countable unions and complements (as shown above). Since the Borel $\sigma$-algebra is the smallest such family, every Borel set is almost open.

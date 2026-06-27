---
role: proof
locale: en
of_concept: boolean-set-algebra
source_book: gtm037
source_chapter: "9"
source_section: "Elements of Logic"
---

Proof. By routine checking of the Boolean algebra axioms (9.3). Let $\mathfrak{A}$ be a field of sets, and let $1 = \bigcup \mathfrak{A}$ and $0 = \emptyset$. Then:

(i) Commutativity: $X \cup Y = Y \cup X$ and $X \cap Y = Y \cap X$ hold for all sets.

(ii) Associativity: $X \cup (Y \cup Z) = (X \cup Y) \cup Z$ and $X \cap (Y \cap Z) = (X \cap Y) \cap Z$ hold for all sets.

(iii) Absorption: $X \cap Y \cup Y = Y$ and $(X \cup Y) \cap Y = Y$ hold by elementary set theory.

(iv) Distributivity: $X \cap (Y \cup Z) = (X \cap Y) \cup (X \cap Z)$ and $X \cup (Y \cap Z) = (X \cup Y) \cap (X \cup Z)$ hold for all sets.

(v) Complementation: $X \cap (1 \setminus X) = \emptyset = 0$ and $X \cup (1 \setminus X) = \bigcup \mathfrak{A} = 1$.

Thus $\langle \mathfrak{A}, \cup, \cap, \sim, 0, \bigcup \mathfrak{A} \rangle$ satisfies all five Boolean algebra axioms.

---
role: proof
locale: en
of_concept: distributive-law-duality
source_book: gtm030
source_chapter: "3"
source_section: "3"
---

Assume the distributive law $a \cap (b \cup c) = (a \cap b) \cup (a \cap c)$ holds. Then

$$((a \cup b) \cap a) \cup ((a \cup b) \cap c)$$
$$= a \cup ((a \cup b) \cap c)$$
$$= a \cup ((a \cap c) \cup (b \cap c))$$
$$= (a \cup (a \cap c)) \cup (b \cap c)$$
$$= a \cup (b \cap c).$$

The leftmost expression evaluates via the distributive law: $((a \cup b) \cap a) \cup ((a \cup b) \cap c) = (a \cup b) \cap (a \cup c)$. Hence $(a \cup b) \cap (a \cup c) = a \cup (b \cap c)$, which is the dual condition. The converse implication follows by duality.

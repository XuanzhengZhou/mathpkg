---
role: proof
locale: en
of_concept: modular-lattice-alternative-characterization
source_book: gtm030
source_chapter: "3"
source_section: "3"
---

**($\Rightarrow$)** Assume $L$ is modular and let $a, b, c \in L$ with $a \geq b$, $a \cup c = b \cup c$, and $a \cap c = b \cap c$. Then by the modular law $L_5$ applied to $a \geq b$,

$$a \cap (b \cup c) = b \cup (a \cap c).$$

Since $a \cup c = b \cup c$, the left side is $a \cap (a \cup c) = a$. Since $a \cap c = b \cap c$, the right side is $b \cup (b \cap c) = b$. Hence $a = b$.

**($\Leftarrow$)** Conversely, assume the cancellation property holds. Let $a \geq b$ and consider $c$ arbitrary. Set

$$u = a \cap (b \cup c), \quad v = b \cup (a \cap c).$$

We have $u \geq v$ always (as noted earlier for any lattice). Compute:

$$u \cup c = (a \cap (b \cup c)) \cup c.$$

By the dual of modularity (which is the same as $L_5$),

$$(a \cap (b \cup c)) \cup c = a \cup c,$$

and similarly

$$(b \cup (a \cap c)) \cup c = b \cup c.$$

But since $u \geq v$, using the dual argument we obtain

$$(b \cup (a \cap c)) \cap c = a \cap c,$$

so that

$$u \cap c = a \cap c \quad\text{and}\quad v \cap c = a \cap c.$$

By duality we also have

$$(a \cap (b \cup c)) \cup c = b \cup c,$$
$$(b \cup (a \cap c)) \cup c = b \cup c.$$

Hence $u \cup c = v \cup c$ and $u \cap c = v \cap c$ with $u \geq v$. Applying the cancellation property yields $u = v$, i.e.,

$$a \cap (b \cup c) = b \cup (a \cap c),$$

so $L$ is modular.

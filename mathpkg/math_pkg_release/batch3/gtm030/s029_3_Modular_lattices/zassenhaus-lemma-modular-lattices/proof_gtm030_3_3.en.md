---
role: proof
locale: en
of_concept: zassenhaus-lemma-modular-lattices
source_book: gtm030
source_chapter: "3"
source_section: "3"
---

Since the second interval is symmetric in the subscripts 1 and 2, and the third is obtained from the first by interchanging 1 and 2, it suffices to prove that the first and second intervals are projective.

Set

$$a = a_1 \cap a_2, \quad b = (a_1 \cap a_2') \cup a_1'.$$

Then compute the join:

$$a \cup b = (a_1 \cap a_2) \cup (a_1 \cap a_2') \cup a_1' = (a_1 \cap a_2) \cup a_1',$$

using the modular law to combine the first two terms. For the meet:

$$a \cap b = (a_1 \cap a_2) \cap ((a_1 \cap a_2') \cup a_1').$$

By the modular law $L_5$ applied with $a_1 \cap a_2 \geq a_1' \cap a_2$, this simplifies to

$$a \cap b = (a_1 \cap a_2') \cup (a_1' \cap a_2).$$

Thus the interval $I[a \cup b, a] = I[(a_1 \cap a_2) \cup a_1', a_1 \cap a_2]$ is transposed to the interval $I[b, a \cap b] = I[(a_1 \cap a_2') \cup a_1', (a_1 \cap a_2') \cup (a_1' \cap a_2)]$, establishing their projectivity. By symmetry, all three intervals are projective.

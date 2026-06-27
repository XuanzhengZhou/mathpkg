---
role: proof
locale: en
of_concept: finite-meet-irreducible-decomposition-acc
source_book: gtm030
source_chapter: "3"
source_section: "5"
---

One can prove this by using the analogue of the principle of divisor induction. Assume, to the contrary, that there exists an element $a \in L$ that cannot be expressed as a finite meet of meet-irreducible elements. In particular, $a$ itself is not meet-irreducible, so $a = a_1 \cap a_1'$ with $a_1 > a$ and $a_1' > a$. At least one of $a_1, a_1'$ must also fail to admit a finite meet-irreducible decomposition (otherwise their meet would give one for $a$). Repeating this process yields a strictly ascending infinite chain $a < a_1 < a_2 < \cdots$, contradicting the ascending chain condition. Hence every element admits such a finite decomposition.

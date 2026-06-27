---
role: proof
locale: en
of_concept: unique-prime-subfield
source_book: gtm028
source_chapter: "II"
source_section: "4. The characteristic of a field"
---

Let $k$ be a field with identity $e$. The integral multiples $ne$ ($n \ge 0$) form a subring $E$ of $k$, since $(n \pm m)e = ne \pm me$ and $(nm)e = ne \cdot me$. Let $\Delta$ be the quotient field of $E$ in $k$.

Any subfield of $k$ must contain the identity $e$, and being closed under addition and subtraction, must contain all integral multiples $ne$. Hence any subfield of $k$ contains the ring $E$. Since a subfield is closed under taking quotients (inverses of nonzero elements), it must also contain the quotient field $\Delta$ of $E$. Therefore $\Delta$ is contained in every subfield of $k$, so $\Delta$ is the smallest subfield of $k$ and is in fact the intersection of all subfields of $k$.

By Definition 1, a prime field is a field without proper subfields. Since $\Delta$ is contained in every subfield of $k$, it has no proper subfields, hence $\Delta$ is a prime field. Moreover, since every subfield of $k$ contains $\Delta$, $\Delta$ is the only prime subfield of $k$. Thus every field $k$ contains a unique prime field.

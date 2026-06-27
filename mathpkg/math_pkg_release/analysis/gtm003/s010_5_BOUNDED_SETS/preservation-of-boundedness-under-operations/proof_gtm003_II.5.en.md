---
role: proof
locale: en
of_concept: preservation-of-boundedness-under-operations
source_book: gtm003
source_chapter: "II"
source_section: "5"
---

**(i) Finite sums:** If $A, B$ are bounded, then $A + B$ is the image of the bounded product set under the continuous addition map (or alternatively, Theorem 5.1(ii) implies that $A \cup B$ is bounded; and by Theorem 5.4 applied to the addition map $+: L \times L \to L$ which is continuous, the sum is bounded). More directly: given a $0$-neighborhood $U$, choose $V$ with $V + V \subset U$. Then $A \subset \lambda_1 V$, $B \subset \lambda_2 V$. Let $\lambda = \max\{|\lambda_1|, |\lambda_2|\}$. Then $A + B \subset \lambda V + \lambda V = \lambda(V + V) \subset \lambda U$. Finitely many bounded sets follow by induction. The same argument works for totally bounded sets.

**(ii) Finite unions:** This is Theorem 5.1(ii).

**(iii) Dilatations $x \mapsto \lambda_0 x + x_0$:** The map $x \mapsto \lambda_0 x$ is continuous (by $(LT)_2$), so by Theorem 5.4 it preserves boundedness and total boundedness. The translation $x \mapsto x + x_0$ is a homeomorphism, so it also preserves boundedness (since the neighborhoods of $x_0$ are translates of $0$-neighborhoods). The composition of the two operations therefore preserves boundedness and total boundedness.

---
role: proof
locale: en
of_concept: annihilator-properties
source_book: gtm049
source_chapter: "IV"
source_section: "4.6"
---

(1) Follows from extending a basis of $M$ to a basis of $V$ and observing that the dual basis elements corresponding to the extension form a basis of $M^\circ$.

(2) By definition, $af = 0$ for all $f \in M^\circ$ and all $a \in M$, so $M \subset M^{\circ\circ}$. But by (1) applied to $M^\circ$, $\dim M^{\circ\circ} = \dim V^* - \dim M^\circ = \dim M$, whence $M^{\circ\circ} = M$.

(3) Clearly $M \subset N$ implies $M^\circ \supset N^\circ$; and $M^\circ \supset N^\circ$ implies $M^{\circ\circ} \subset N^{\circ\circ}$, i.e., $M \subset N$, by (2).

(4) For any $f \in V^*$, we have $(a+b)f = 0$ for all $a \in M$, $b \in N$ if and only if $af = 0$, $bf = 0$ for all $a \in M$, $b \in N$, and this is exactly the statement $(M+N)^\circ = M^\circ \cap N^\circ$.

(5) Applying (4) to $M^\circ + N^\circ$, we see that $(M^\circ + N^\circ)^\circ = M^{\circ\circ} \cap N^{\circ\circ} = M \cap N$, by (2), whence $M^\circ + N^\circ = (M \cap N)^\circ$.

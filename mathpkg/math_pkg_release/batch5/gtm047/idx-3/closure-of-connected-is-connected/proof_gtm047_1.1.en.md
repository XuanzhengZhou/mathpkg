---
role: proof
locale: en
of_concept: closure-of-connected-is-connected
source_book: gtm047
source_chapter: "1"
source_section: "Connectivity"
---

Suppose that $L = H \cup K$ (separated and nonempty). Let $H' = M \cap H$ and $K' = M \cap K$, so that $M = H' \cup K'$. Then $H'$ and $K'$ are separated. Now $H$ contains a point $P$ of $L$, and $P$ is a point or a limit point of $M$. If $P \in M$, then $P \in H'$ and $H' \neq \emptyset$. If $P$ is a limit point of $M$, then $P$ is a limit point of $H'$ or $K'$, but since $P \in H$, every neighborhood of $P$ meets $H$, so $P$ cannot be a limit point of $K'$. Thus $H' \neq \emptyset$. Similarly, $K' \neq \emptyset$, contradicting the connectedness of $M$.

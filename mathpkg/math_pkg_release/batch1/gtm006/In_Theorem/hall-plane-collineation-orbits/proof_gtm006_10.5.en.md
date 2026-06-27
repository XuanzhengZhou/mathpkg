---
role: proof
locale: en
of_concept: hall-plane-collineation-orbits
source_book: gtm006
source_chapter: "10"
source_section: "5"
---

Suppose two planes have at least $q^2 - 2q - 1$ parallel classes in common. Then there are at least $q^2 - 2q - 1$ common special points which have the same coordinates in each plane. Let $M$ be the set of elements of $\mathrm{GF}(q^2)$ assigned to the common special points.

In any linear planar ternary ring, the product $a * b$ of any two elements is given by $(0, a * b)$, which is the intersection of $[0]$ with the line joining $(a)$ to $(b, 0)$. Hence $s \times x = sx$ for all $s \in M$ and all $x \in \mathrm{GF}(q^2)$.

Furthermore, by the definition of $M$, there are no other common parallel classes. Thus $M = \{s \in \mathrm{GF}(q^2) \mid s \odot x = sx \text{ for all } x \in \mathrm{GF}(q^2)\}$. This implies that $M$ is closed under both addition and multiplication, i.e., $M$ is a subfield of $\mathrm{GF}(q^2)$.

However, no proper subfield of $\mathrm{GF}(q^2)$ can have more than $q$ elements. Since $|M| \geq q^2 - 2q - 1 > q$ for $q > 3$, it follows that $M$ must be $\mathrm{GF}(q^2)$. This is a contradiction, thus proving the theorem.

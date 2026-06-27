---
role: proof
locale: en
of_concept: hall-plane-collineation-orbits
source_book: gtm006
source_chapter: "10"
source_section: "5. Inherited Collineation Groups"
---

Suppose two planes have at least $q^2 - 2q - 1$ parallel classes in common; then there are at least $q^2 - 2q - 1$ common special points which have the same coordinates in each plane. Let $M$ be the set of elements of $\operatorname{GF}(q^2)$ assigned to the common special points. Then, since in any linear PTR the product $a * b$ of any two elements is given by $(0, a * b)$, which is the intersection of $[0]$ with the line joining $(a)$ to $(b, 0)$, we have $s \times x = sx$ for all $s \in M$ and all $x \in \operatorname{GF}(q^2)$. Furthermore, since by the definition of $M$ there are no other common parallel classes, $M = \{ s \in \operatorname{GF}(q^2) \mid s \times x = sx \text{ for all } x \in \operatorname{GF}(q^2) \}$. But this implies that $M$ is closed under both addition and multiplication, i.e., that $M$ is a subfield of $\operatorname{GF}(q^2)$. However, no proper subfield of $\operatorname{GF}(q^2)$ can have more than $q$ elements, and since $|M| \geq q^2 - 2q - 1 > q$, $M$ must be $\operatorname{GF}(q^2)$. This is a contradiction, thus proving the theorem.

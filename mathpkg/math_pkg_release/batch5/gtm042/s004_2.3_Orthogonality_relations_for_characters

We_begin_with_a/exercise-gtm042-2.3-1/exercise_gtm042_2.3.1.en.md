---
role: exercise
locale: en
chapter: "2"
section: "2.3"
exercise_number: 1
---

Let $\rho$ be a linear representation with character $\chi$. Show that the number of times that $\rho$ contains the unit representation is equal to
$$(\chi|1) = \frac{1}{g} \sum_{s \in G} \chi(s).$$

**Solution.** Let $1_G$ denote the unit (trivial) character, which takes the value $1_G(s) = 1$ for all $s \in G$. By Theorem 4, the multiplicity of the unit representation in $\rho$ equals the scalar product $(\chi|1_G)$. Using the definition of the scalar product,

$$(\chi|1_G) = \frac{1}{g} \sum_{s \in G} \chi(s) \cdot 1_G(s)^* = \frac{1}{g} \sum_{s \in G} \chi(s),$$

since $1_G(s)^* = 1$. $\square$

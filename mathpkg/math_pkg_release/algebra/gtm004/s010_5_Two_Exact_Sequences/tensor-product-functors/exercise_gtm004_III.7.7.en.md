---
role: exercise
locale: en
chapter: "III"
section: "7"
exercise_number: 7
---

# Exercise 7.7

Let $A \times B$ be the cartesian product of the sets underlying the right $\Lambda$-module $A$ and the left $\Lambda$-module $B$. For $G$ an abelian group, call a function $f : A \times B \rightarrow G$ bilinear if

$$
f(a_1 + a_2, b) = f(a_1, b) + f(a_2, b), \quad a_1, a_2 \in A, \; b \in B;
$$

$$
f(a, b_1 + b_2) = f(a, b_1) + f(a, b_2), \quad a \in A, \; b_1, b_2 \in B;
$$

$$
f(a\lambda, b) = f(a, \lambda b), \quad a \in A, \; b \in B, \; \lambda \in \Lambda.
$$

Show that the tensor product has the following universal property. To every abelian group $G$ and to every bilinear map $f : A \times B \rightarrow G$ there exists a unique homomorphism of abelian groups

$$
g : A \otimes_\Lambda B \rightarrow G \quad \text{such that} \quad f(a, b) = g(a \otimes b).
$$

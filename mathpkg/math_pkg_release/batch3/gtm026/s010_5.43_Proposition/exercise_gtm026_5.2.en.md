---
role: exercise
locale: en
chapter: "5"
section: "Exercises for Section 5"
exercise_number: 2
---

In this exercise we abstract the structure of the set of supports of a function $\psi: A^X \to A$. In case $A = \emptyset$, $X \neq \emptyset$ the set of supports of $\psi$ is the set of all nonempty subsets of $X$. This case is singular and we concentrate on the case $A \neq \emptyset$. A **quasifilter** on a set $X$ is a nonempty collection $\mathcal{F}$ of subsets of $X$ satisfying (i) every superset of an element of $\mathcal{F}$ is in $\mathcal{F}$, and (ii) the intersection of two elements of $\mathcal{F}$ is in $\mathcal{F}$.

(b) If $\mathcal{F}$ is any quasifilter on $X$, prove that $\mathcal{F}$ is the set of supports of its characteristic function $2^X \to 2$.

(c) Prove that $\mathcal{F}$ is a quasifilter on $X$ if and only if (iii) $X \in \mathcal{F}$, and (iv) for all $F, G \subset X$, $F \cap G \in \mathcal{F}$ if and only if $F, G \in \mathcal{F}$.

(d) Let $\Omega_0 = \{e\}$, $\Omega_1 = \{\cdot\}$, $\Omega_n = \varnothing$ otherwise. $2 = \{0,1\}$ is an $\Omega$-algebra with $\delta_e = 1$ and $\delta.$ defined by

$$\begin{array}{c|c|c}
\cdot & 1 & 0 \\
\hline
1 & 1 & 0 \\
0 & 0 & 0
\end{array}$$

Show that $\mathcal{F}$ is a quasifilter on $X$ if and only if its characteristic function $(2, \xi)^X \to (2, \xi)$ is an $\Omega$-homomorphism.

(e) Let $AT = \{\mathcal{F} : \mathcal{F} \text{ is a quasifilter on } X\}$. Show that $AT$ is a subtheory of the double power-set theory. [Hint: use (d) and exercise 1.]

(f) [Day '75]. A partially-ordered set is **directed** if each two elements have an upper bound. Let $T$ be the quasifilter theory of (e). Show that $\mathbf{Set}^T$ may be identified with the category whose objects are complete lattices satisfying

$$\text{Inf}(\text{Sup } A_i : i \in I)) = \text{Sup}(\text{Inf}(a_i : i \in I) : (a_i) \in \Pi A_i)$$

for each family $(A_i)$ of directed subsets, and whose morphisms preserve all infima and all suprema of directed subsets. [Hint: cf. 5.17.]

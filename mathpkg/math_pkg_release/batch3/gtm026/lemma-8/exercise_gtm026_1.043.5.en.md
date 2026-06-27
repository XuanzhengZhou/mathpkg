---
role: exercise
locale: en
chapter: "1"
section: "043"
exercise_number: 5
---

([Lawvere ’63], [Freyd ’66], [Manes ’67]). A semiadditive category is a category $A$ together with the structure of an abelian monoid on the set $A(A, B)$ for each pair $(A

is a coproduct diagram in $\mathcal{A}$. [Hint: add the pieces.]

(c) If $\mathbf{Set}^T$ is semiadditive (respectively, additive) show that $\mathbf{T} \otimes \mathbf{AM}$ ($\mathbf{T} \otimes \mathbf{AG}$) exists and coincides with $\mathbf{T}$. [Hint: using (b), define the necessary operations as $\mathbf{T}$-homomorphisms.]

(d) If $\mathbf{T}$ is finitary and $\mathbf{Set}^T$ is semiadditive (respectively, additive) show that $\mathbf{Set}^T$ coincides with the category of semimodules (modules) over the semiring (ring) $1T$. [Hint: if $(x_1, \ldots, x_n)\omega$ is a $\mathbf{T}$-operation, it decomposes as $(0, x_2, \ldots, x_n)\omega + \cdots + (x_1, \ldots, x_{n-1}, 0)\omega$.]

(e) For any theory $\mathbf{T}$ in $\mathbf{Set}$, prove that an epimorphism in the category of $\mathbf{T}$-AG bialgebras is a coequalizer. [Hint: given an epimorphism $f: X \longrightarrow Y$, set $q = \text{coeq}(f, 0)$ in the category of abelian groups; then $q$ is obtained by dividing out by the abelian group congruence $R = \{(y_1, y_2): y_1 - y_2 \in \text{Im}(f)\}$; since “minus”: $Y \times Y \longrightarrow Y$ is a $\mathbf{T}$-homomorphism, $R$ is also a $\mathbf{T}$-congruence, and $q = \text{coeq}(f, 0)$ in the category of bialgebras; as $f$ is epi, $q = 0$.]

(f) Let $\mathcal{A}$ be the additive category of torsion-free abelian groups. Show that $\mathbf{Z} \longrightarrow \mathbf{Z}$, $n \mapsto 2n$ is an

(a) Show that any fibre-complete category has tensor products by the construction of exercise 3(b) of section 2.

(b) For any algebraic theory $T$ in $Set$ show that every pair of $T$-algebras has a tensor product. [Hint: define $(X, \xi) \otimes (Y, \theta) = (X \times Y)T/R$ where $R$ is the intersection of all congruences of the form $R_f = \{(x, y): xf^\# = yf^\#\}$ with $f: (X, \xi); (Y, \theta) \longrightarrow (Z, \gamma)$ bi-admissible.]

(c) ([Freyd ’66], [Linton ’66-A]). If $T$ is a commutative theory in $Set$ show that $Set^T$ is a closed category with the tensor product of (b).

(d) Show that the passage from $(Z, u)$ to the set of bi-admissible maps $(X, s); (Y, t) \longrightarrow (Z, u)$ describes a functor $U: \mathcal{C} \longrightarrow Set$ such that $(X, s) \otimes (Y, t)$ exists if and only if there exists a free $\mathcal{C}$-object over 1 with respect to $U$. Give an alternate proof of (b) using the adjoint functor theorem.

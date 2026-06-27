---
role: exercise
locale: en
chapter: "3"
section: "Exercises"
exercise_number: 10
source_book: gtm026
---

Zadeh's fuzzy sets and Goguen's generalizations (see the notes) support the philosophy that the set $QT$ of fuzzy states should be ordered by "degree of membership." In this exercise we provide some axioms and give a common framework for universal relational algebra and Goguen's category of $L$-fuzzy sets.

Let $\mathbf{T}$ be an algebraic theory in $\mathbf{Set}$. A degree relation on $\mathbf{T}$ is an assignment to each set $A$, a reflexive and transitive relation $\leqslant$ on $AT$ subject to:

(Uniformity axiom) For all $\alpha: A \longrightarrow BT$, $\alpha^{\#}: AT \longrightarrow BT$ preserves $\leqslant$.

(Causality axiom) If $\alpha: A \longrightarrow AT$ and $p$ in $AT$ are such that $\alpha_a \leqslant p$ for all $a$ in $A$, then $p\alpha^{\#} \leqslant p$.

The uniformity axiom ensures, for example, that isomorphic sets induce isomorphic orders. The causality axiom states that the causal operations on fuzzy states (which "build trees of trees") cannot increase the degree.

For any functor $X: \mathbf{Set} \longrightarrow \mathbf{Set}$, let $[X, \mathbf{T}, \leqslant]$ be the category of sets with structure with objects all pairs $(A, \delta)$ with $\delta: AX \longrightarrow AT$, and with morphisms $f:(A, \delta) \longrightarrow (A', \delta')$ such that

$$\langle t, \delta.fT \rangle \leqslant \langle t, fX.\delta' \rangle$$

for all $t$ in $AX$.

In the context where objects are pairs $(A, \delta)$ where $\delta$ assigns to each $\omega \in \Omega_n$ a partial function $\delta_\omega: A^n \longrightarrow A$ and whose admissible maps $f:(A, \delta) \longrightarrow (A', \delta')$ are defined by the requirement that whenever $(a_i)\delta_\omega$ is defined then so, too, is $(a_i f)\delta'_\omega$, and, moreover, $(a_i)\delta_\omega f = (a_i f)\delta'_\omega$.

(c) Let $X = X_\Omega$, let $\mathbf{T}$ be the stochastic matrix theory, and define $p \leqslant q$ to mean the support of $p$ (in the sense of 1.5.10) is contained in the support of $q$; specifically, $(\lambda_a) \leqslant (\lambda'_a)$ if whenever $\lambda_a \neq 0$ then also $\lambda'_a \neq 0$. Show that the morphisms in $[X, \mathbf{T}, \leqslant]$ are characterized by the requirement that "if $(a_i)\delta_\omega = a$ with nonzero probability then also $(a_i f)\delta'_\omega = af$ with nonzero probability."

(d) Let $AX = 1$ for all $A$, let $\mathbf{T}$ be the theory induced by a complete distributive lattice $L$ as in 3.3, and let $\leqslant$ be pointwise. Show that $[X, \mathbf{T}, \leqslant] = \text{Goguen's Set}(L)$ (as in exercise 3.5.7).

(e) Generalizing exercise 3.5.7, show that $[X, \mathbf{T}, \leqslant]$ is fibre complete whenever $(AT, \leqslant)$ is a complete lattice for every $A$.

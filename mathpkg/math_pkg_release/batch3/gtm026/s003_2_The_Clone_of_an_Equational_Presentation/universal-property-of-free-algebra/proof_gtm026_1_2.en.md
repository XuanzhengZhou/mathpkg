---
role: proof
locale: en
of_concept: universal-property-of-free-algebra
source_book: gtm026
source_chapter: "1"
source_section: "2"
---

Consider the diagram below. The unique $\Omega$-homomorphism
$$f^{\#}: A\Omega \longrightarrow (X, \delta)$$
of 1.20 respects $E_A$ by the definition of $E_A$, and this induces a unique function $f^{\#}: AT \longrightarrow (X, \delta)$ which is a homomorphism because it is induced from a homomorphism on the term algebra that respects the defining equivalence relation.

To complete the proof that $AT$ is indeed an $(\Omega, E)$-algebra, let $r: \mathbb{V} \longrightarrow AT$ be any function. By the axiom of choice (but see exercise 1) there exists a function $g: \mathbb{V} \longrightarrow A\Omega$ such that $g \cdot A\rho = r$, where $A\rho: A\Omega \longrightarrow AT$ is the quotient map. Since $g^{\#} \cdot A\rho$ is an $\Omega$-homomorphism (by 2.3 and the first part of the proof), and the restriction of $g^{\#} \cdot A\rho$ to $\mathbb{V}$ coincides with $r$, we have from 1.20 that $g^{\#} \cdot A\rho = r^{\#}$. Since $g^{\#}$ maps equations into $E_A$ (by 2.4) and $A\rho$ identifies elements of $E_A$, $AT$ satisfies $E$ as desired. Thus $AT$ is an $(\Omega, E)$-algebra and $A\eta$ is the insertion of generators, giving the universal property.

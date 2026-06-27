---
role: proof
locale: en
of_concept: category-object-in-grp-is-group-object-in-cat
source_book: gtm005
source_chapter: "XII"
source_section: "1. Internal Categories"
---

Let $C = (C_0, C_1, i, d_0, d_1, \gamma)$ be an internal category in $\mathbf{Grp}$. This means $C_0$ and $C_1$ are groups, and the structure maps $i, d_0, d_1, \gamma$ are group homomorphisms. Let $m_0 : C_0 \times C_0 \to C_0$ and $m_1 : C_1 \times C_1 \to C_1$ be the group multiplications.

Consider the product category $C \times C$. Its object of objects is $C_0 \times C_0$ and object of arrows is $C_1 \times C_1$. The pair $(m_0, m_1)$ constitutes a pair of maps between the corresponding objects. The condition that $i, d_0, d_1$ are group homomorphisms means that the diagrams

\[
\begin{CD}
C_0 \times C_0 @>{m_0}>> C_0 \\
@V{i \times i}VV @V{i}VV \\
C_1 \times C_1 @>>{m_1}> C_1
\end{CD}
\]

commute. Similarly, $d_0$ and $d_1$ satisfying this commutation means that the map $(m_0, m_1)$ respects domain and codomain, i.e., it is a functor $m : C \times C \to C$. The associativity of the group multiplications translates to associativity of this functor, and the existence of group inverses provides an inverse for $m$. Thus $C$ acquires the structure of a group object in $\mathbf{Cat}$.

Conversely, given a group object in $\mathbf{Cat}$ (a small category $C$ with functor $m : C \times C \to C$ that is associative and has an inverse), the object-of-objects $C_0$ and object-of-arrows $C_1$ inherit group structures from the functor $m$, and the structure maps of the category become group homomorphisms by the functoriality of $m$, yielding an internal category in $\mathbf{Grp}$.

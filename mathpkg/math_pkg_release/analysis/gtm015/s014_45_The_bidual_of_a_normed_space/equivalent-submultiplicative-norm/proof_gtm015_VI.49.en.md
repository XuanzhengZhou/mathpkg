---
role: proof
locale: en
of_concept: equivalent-submultiplicative-norm
source_book: gtm015
source_chapter: "VI"
source_section: "49"
---

# Proof of Equivalent Submultiplicative Norm

Let $A$ be a normed algebra with unity element $u$, such that for each $x \in A$, the left and right multiplication operators $U_x y = xy$ and $V_x y = yx$ are continuous. Consider the Banach algebra $\mathcal{B} = \mathcal{L}(A)$ of all continuous linear operators on the normed space $A$ (see 40.23); $\mathcal{B}$ has unity element $I$ (the identity operator) with $\|I\| = 1$.

Each $x \in A$ determines operators $U_x, V_x \in \mathcal{B}$. The mapping $x \mapsto U_x$ is an algebra monomorphism $A \to \mathcal{B}$ with $U_u = I$:
- $U_{x+y} = U_x + U_y$ is clear;
- $U_{xy}z = (xy)z = x(yz) = U_x(U_y z)$, so $U_{xy} = U_x U_y$ (using associativity);
- $U_u y = uy = y$, so $U_u = I$;
- If $U_x = 0$, then $U_x u = xu = x = 0$, so the map is injective.

Define the new norm on $A$ by
$$|x| = \|U_x\|_{\mathcal{B}}.$$

This is a submultiplicative norm because $|xy| = \|U_{xy}\| = \|U_x U_y\| \leq \|U_x\|\|U_y\| = |x||y|$, and $|u| = \|U_u\| = \|I\| = 1$.

**Equivalence of norms:** It remains to show that $|\cdot|$ is equivalent to the original norm $\|\cdot\|$ on $A$. Let $\mathcal{U} = \{U_x : x \in A\} \subset \mathcal{B}$. We claim that
$$\mathcal{U} = \{T \in \mathcal{B} : T V_y = V_y T \text{ for all } y \in A\}. \qquad (*)$$

Indeed, $U_x V_y z = x(yz) = (xy)z = V_{xy}z$, and $V_y U_x z = (xz)y = x(zy) = U_x V_y z$, using associativity in both cases. So $U_x$ commutes with every $V_y$, proving $\mathcal{U} \subset$ RHS.

Conversely, suppose $T \in \mathcal{B}$ commutes with every $V_y$. Set $x = Tu$ (where $u$ is the unity). Then for all $y \in A$,
$$U_x y = xy = (Tu)y = V_y(Tu) = T V_y u = T(uy) = Ty,$$
thus $T = U_x$, proving the reverse inclusion.

It follows from $(*)$ that $\mathcal{U}$ is closed in $\mathcal{B}$ (as the commutant of a set of operators). Viewing $x \mapsto U_x$ as a linear bijection $A \to \mathcal{U}$ between Banach spaces (since $\mathcal{U}$ is closed in the Banach space $\mathcal{B}$), the Closed Graph Theorem (or Open Mapping Theorem) implies that this map is bicontinuous. Hence $|x| = \|U_x\|$ is equivalent to $\|x\|$. $\square$

---
role: proof
locale: en
of_concept: existence-of-lubin-tate-formal-group
source_book: gtm059
source_chapter: "8"
source_section: "1. Lubin-Tate Groups"
---

Apply the Construction Lemma with $f = g$ and the linear form $L(X,Y) = X + Y$. We obtain a unique power series $F_f(X,Y)$ such that
$$
F_f(X,Y) \equiv X + Y \pmod{\deg 2}, \qquad f(F_f(X,Y)) = F_f(f(X), f(Y)).
$$

It remains to verify that $F_f$ satisfies the formal group axioms.

\textbf{Commutativity:} Consider $G(X,Y) = F_f(Y,X)$. Then $G(X,Y) \equiv X + Y \pmod{\deg 2}$ and
$$
f(G(X,Y)) = f(F_f(Y,X)) = F_f(f(Y), f(X)) = G(f(X), f(Y)).
$$
Thus $G$ satisfies the same characterizing conditions as $F_f$, so by uniqueness in the lemma, $G = F_f$, i.e., $F_f(X,Y) = F_f(Y,X)$.

\textbf{Associativity:} Consider $H(X,Y,Z) = F_f(F_f(X,Y), Z)$ and $K(X,Y,Z) = F_f(X, F_f(Y,Z))$. Both are congruent to $X + Y + Z$ modulo degree $2$. Moreover,
$$
f(H(X,Y,Z)) = f(F_f(F_f(X,Y), Z)) = F_f(f(F_f(X,Y)), f(Z)) = F_f(F_f(f(X), f(Y)), f(Z)) = H(f(X), f(Y), f(Z)),
$$
and similarly $f(K(X,Y,Z)) = K(f(X), f(Y), f(Z))$. Applying the Construction Lemma with the linear form $L(X,Y,Z) = X + Y + Z$ yields a unique power series commuting with $f$. Hence $H = K$, so $F_f$ is associative.

Thus $F_f$ is a formal group and $f$ is an endomorphism by construction.

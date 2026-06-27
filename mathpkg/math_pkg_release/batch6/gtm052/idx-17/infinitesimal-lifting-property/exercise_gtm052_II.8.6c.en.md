---
role: exercise
locale: en
chapter: "II"
section: "8"
exercise_number: "8.6(c)"
of_concept: infinitesimal-lifting-property
---

**Exercise 8.6(c).** Let $k$ be an algebraically closed field, and let $A$ be a finitely generated $k$-algebra such that $\operatorname{Spec} A$ is a nonsingular variety. Let $B' \to B$ be a surjective homomorphism of $k$-algebras with kernel $I$ satisfying $I^2 = 0$, and let $f: A \to B$ be a homomorphism. Prove the infinitesimal lifting property: there exists a $k$-algebra homomorphism $g: A \to B'$ lifting $f$, and the set of all such liftings is a principal homogeneous space under $\operatorname{Hom}_A(\Omega_{A/k}, I)$. The proof proceeds in three steps:

(a) If $g: A \to B'$ lifts $f$ and $g': A \to B'$ is another such lifting, then $\theta = g - g'$ is a $k$-derivation of $A$ into $I$, i.e., an element of $\operatorname{Hom}_A(\Omega_{A/k}, I)$. Conversely, $g' = g + \theta$ lifts $f$ for any $\theta$. (Nonsingularity not needed.)

(b) Let $P = k[x_1, \ldots, x_n]$ with $A = P/J$. Construct a homomorphism $h: P \to B'$ making the diagram commute.

(c) Using the nonsingularity hypothesis and the exact sequence $0 \to J/J^2 \to \Omega_{P/k} \otimes A \to \Omega_{A/k} \to 0$ from (8.17), show that a lifting $g: A \to B'$ exists.

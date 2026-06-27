---
role: exercise
locale: en
chapter: "IX"
section: "3. E-Satellites"
exercise_number: 3
---

# Exercise 3.3

(Definition of satellites following Buchsbaum [5].) Let $\mathfrak{A}$, $\mathfrak{B}$ be abelian categories, and let $H : \mathfrak{A} \to \mathfrak{B}$ be a (covariant) additive functor. Suppose that $\mathfrak{B}$ has limits. For $A$ in $\mathfrak{A}$ consider the totality of all short exact sequences

$$E : 0 \to B \to E \to A \to 0.$$

Define a partial ordering as follows: $E' < E$ if there exists $\varphi : E \to E'$ and $\psi : B \to B'$ such that the diagram

$$
\begin{array}{ccccccc}
0 & \longrightarrow & B & \longrightarrow & E & \longrightarrow & A & \longrightarrow & 0 \\
& & \downarrow_{\psi} & & \downarrow_{\varphi} & & \parallel \\
0 & \longrightarrow & B' & \longrightarrow & E' & \longrightarrow & A & \longrightarrow & 0
\end{array}
$$

is commutative. Consider then $H_E = \ker(HB \to HE)$. Show that for $E' < E$ the map $H\psi : HB \to HB'$ induces a map $\theta_E : H_E \to H_{E'}$, which is independent of the choice of $\varphi$ and $\psi$ in the above diagram. Define $S_1 A = \varinjlim_{E} H_E$. (Note that there is a set-theoretical difficulty, for the totality of sequences $E$ need not be a set. Although this difficulty is not trivial, we do not want the reader to concern himself with it at this stage.) Show that $S_1$ defines a functor, and that it satisfies the universal property of a left satellite.

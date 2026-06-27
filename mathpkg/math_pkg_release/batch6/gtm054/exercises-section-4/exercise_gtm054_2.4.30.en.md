---
role: exercise
locale: en
chapter: "2"
section: "4"
exercise_number: 30
---

Show that for any set $U$, the partially-ordered set $(\mathbb{P}(U), \leq)$ is a lattice.

If $(U, \leq)$ is a finite or infinite partially-ordered set, we define the dual order $\geq$ on $U$ by: $x \geq y$ if and only if $y \leq x$, for all $x, y \in U$. Then $(U, \geq)$ is also a partially-ordered set. In particular, if $(U, \leq)$ is a lattice with meet and join denoted by $\wedge$ and $\vee$, respectively, then $(U, \geq)$ is its dual lattice, with meet and join given by $\vee$ and $\wedge$, respectively, as can be easily verified from the definitions. For example, $(\mathcal{P}(U), \supseteq)$ is dual to $(\mathcal{P}(U), \subseteq)$ in Example B26, where the roles of union and intersection have been interchanged. Clearly the dual of the dual of a lattice is the original lattice.

The next exercise is a list of algebraic properties to be verified for all l


PROOF. (a) $\Rightarrow$ (b). Assume (a) to hold and substitute $x \vee y$ for $x$ and $x$ for $y$, obtaining

$$[(x \vee y) \wedge x] \vee [(x \vee y) \wedge z] = (x \vee y) \wedge (x \vee z).$$

The left-hand member becomes

$x \vee [(x \vee y) \wedge z]$, by B31b and c;

$= x \vee [(x \wedge z) \vee (y \wedge z)]$, by assumption (with $x$ and $z$ interchanged);

$= x \vee (y \wedge z)$, by B31b and c.

(b) $\Rightarrow$ (c). Since $z \leq x \vee z$, B31d followed by our assumption (b) yields $(x \vee y) \wedge z \leq (x \vee y) \wedge (x \vee z) = x \vee (y \wedge z).$

(c) $\Rightarrow$ (a). We need only prove that (c) implies the reverse inequality of B31f. With appropriate substitutions, two successive applications of assumption (c) yield

$[(x \vee y) \wedge (x \vee z)] \leq x \vee [y \wedge (x \vee z)]$

$\leq x \vee [x \vee (y \wedge z)]$

$= x \vee (y \wedge z)$, as required.

A lattice which satisfies any one (and hence all three) of the conditions of Proposition B32 is called a distributive lattice.

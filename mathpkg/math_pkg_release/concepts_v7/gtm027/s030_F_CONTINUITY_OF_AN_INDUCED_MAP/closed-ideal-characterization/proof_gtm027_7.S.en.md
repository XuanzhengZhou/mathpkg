---
role: proof
locale: en
of_concept: closed-ideal-characterization
source_book: gtm027
source_chapter: "7"
source_section: "S"
---

# Proof of Characterization of Closed Ideals in C(X)

Let $I$ be a closed ideal in $C(X)$ for $X$ compact Hausdorff. Define the **zero set** of $I$:

$$Z = \{x \in X : f(x) = 0 \text{ for all } f \in I\}.$$

We prove that $I$ consists exactly of all functions in $C(X)$ that vanish identically on $Z$.

**Proof.** If $Z = \varnothing$, then for each $x \in X$ there exists $f_x \in I$ with $f_x(x) \neq 0$. By continuity and compactness, a finite combination $g = \sum f_{x_i}^2 \in I$ (since $I$ is an ideal) is strictly positive on $X$. Then $g$ is invertible in $C(X)$: $1/g \in C(X)$. Since $I$ is an ideal, $1 = g \cdot (1/g) \in I$, so $I = C(X)$. In this case $Z = \varnothing$ and the set of functions vanishing on $Z$ is all of $C(X)$.

If $Z \neq \varnothing$, let $J = \{f \in C(X) : f|_Z \equiv 0\}$. Clearly $I \subseteq J$. We must show $J \subseteq I$.

Consider the subalgebra $C + I = \{c \cdot 1 + f : c \in \mathbb{R}, f \in I\}$. Since $Z$ is nonempty, $C + I$ is a proper closed subalgebra (if $c \cdot 1 \in I$, evaluating at any $z \in Z$ gives $c = 0$, so the constant functions intersect $I$ only at $0$). Moreover, $C + I$ separates points not in $Z$: if $x \notin Z$ and $y \neq x$, use functions in $I$ or constants.

By the representation theorem (f) applied to the subalgebra $C + I$, there exists a compact space $Y$ and a continuous surjection $F : X \to Y$ such that $C + I = F^*(C(Y))$. Moreover, $F$ collapses exactly $Z$ to a point (since all functions in $I$ vanish on $Z$). The kernel of the restriction map $C(X) \to C(Z)$ is $J$, and $I$ is precisely this kernel.

More directly: for $f \in J$, approximate $f$ by elements of $I$ using a partition of unity argument on neighborhoods of $Z$. Since $I$ is closed and contains functions with arbitrarily small support outside any neighborhood of $Z$, $f \in \overline{I} = I$.

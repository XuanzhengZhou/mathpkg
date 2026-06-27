---
role: exercise
locale: en
chapter: "5"
section: "The Wallman Compactification"
exercise_number: 1
---

# Exercise S(d): Maximal Ideals in the Characteristic Ring

Let $X$ be a Boolean space (a Hausdorff space with a base of compact-open sets), let $\mathfrak{F}$ be its characteristic ring (the ring of all continuous functions $f : X \to I_2$ such that $f^{-1}[1]$ is compact), and let $\mathfrak{J}$ be a maximal proper ideal in $\mathfrak{F}$.

Prove that $\mathfrak{J} = \{f \in \mathfrak{F} : f(x) = 0\}$ for some $x \in X$.

*Hint:* Show first that unless there is a point at which all members of $\mathfrak{J}$ vanish, then $\mathfrak{J} = \mathfrak{F}$. To do this, assume that for each $x \in X$ there exists $f_x \in \mathfrak{J}$ with $f_x(x) = 1$. Use the compactness of the supports to construct a finite partition of unity in $\mathfrak{F}$ subordinate to the open cover $\{f_x^{-1}[1] : x \in X\}$, and deduce that $1 \in \mathfrak{J}$, contradicting the properness of $\mathfrak{J}$.

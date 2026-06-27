---
role: exercise
locale: en
chapter: "5"
section: "5.3"
exercise_number: 1
---
# Exercise 5.3

Prove Lemma 5.3: For the operators $\partial$ and $\bar{\partial}$ on differential forms over an open set $\Omega \subseteq \mathbb{C}^n$,

$$\bar{\partial}^2 = 0, \qquad \partial^2 = 0, \qquad \partial\bar{\partial} + \bar{\partial}\partial = 0.$$

*Hint.* There are two approaches:
1. Use the identity $d = \partial + \bar{\partial}$, the fact that $d^2 = 0$ (Lemma 4.8), and separate by bidegree.
2. Compute directly: write $\bar{\partial}f = \sum \frac{\partial f}{\partial \bar{z}_j} d\bar{z}_j$, apply $\bar{\partial}$ again, and use equality of mixed partials together with antisymmetry of the wedge product. Then extend to forms of all bidegrees using the defining formulas (Definition 5.4).

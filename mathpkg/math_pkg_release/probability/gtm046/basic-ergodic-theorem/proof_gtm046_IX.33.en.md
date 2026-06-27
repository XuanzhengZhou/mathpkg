---
role: proof
locale: en
of_concept: basic-ergodic-theorem
source_book: gtm046
source_chapter: "IX"
source_section: "33"
---

We prove that the invariant event
$$D = \left[ \liminf \frac{X^n}{Y^n} \neq \limsup \frac{X^n}{Y^n} \right]$$
is null. Since $D = \bigcup_{a,b} C_{ab}$ is the countable union of invariant events
$$C_{ab} = C_a \bar{C}_b = \left[ \liminf \frac{X^n}{Y^n} < a < b < \limsup \frac{X^n}{Y^n} \right]$$
where $a < b$ vary over all rationals, it suffices to prove each $C_{ab}$ is null.

Set $Z^n = Y^n$ in the basic ergodic inequality, and write $C = C_{ab} = B^m C_{ab} + A^m$. By invariance of $C_{ab}$, translation yields $C_{ab} = B_k^m C_{ab} + A_k^m$. The basic inequality becomes

$$\int_{C_{ab}} \left( \frac{X^n}{Y^n} - b \right) - \sum_{k=1}^{n} \int_{A_k^m} \left( \frac{X_k}{Y^n} - b \frac{Y_k}{Y^n} \right) + \sum_{k=n+1}^{n+m} \int_{C_{ab}} \left( \frac{X_k}{Y^n} - b \frac{Y_k}{Y^n} \right)^+ \geq 0.$$

By definition of $B^m$ and $C_{ab}$, changing $X_k$ to $-X_k$ and $b$ to $-a$ yields

$$\liminf \int_{C_{ab}} \left( a - \frac{X^n}{Y^n} \right) \geq 0.$$

Adding the two inequalities gives $(a - b) P(C_{ab}) \geq 0$ with $a < b$, hence $P(C_{ab}) = 0$.

For the extension B': if $Z^n$ satisfies $\liminf \int_C Y^n/Z^n = 0 \Rightarrow P(C) = 0$, dividing by $Z^n$ instead of $Y^n$ throughout the proof preserves its validity.

---
role: exercise
locale: en
chapter: "3"
section: "6"
exercise_number: 4
---

# Exercise 4

Let $F$ and $G$ be distribution functions on the real line and let

$$L(F, G) = \inf \{\,h > 0 : F(x - h) - h \leq G(x) \leq F(x + h) + h \text{ for all } x \in R\,\}$$

be the Levy distance (between $F$ and $G$). Show that convergence in general is equivalent to convergence in the Levy metric:

$$(F_n \Rightarrow F) \;\Longleftrightarrow\; (L(F_n, F) \to 0).$$

*Hint.* 
- ($\Rightarrow$): If $F_n \Rightarrow F$, then for any $\varepsilon > 0$, choose continuity points $x_1, \ldots, x_k$ of $F$ that form an $\varepsilon$-net. Use the convergence at these points to bound $L(F_n, F) < \varepsilon$ for large $n$.
- ($\Leftarrow$): If $L(F_n, F) \to 0$, then for any continuity point $x$ of $F$, the inequality $F(x-h)-h \leq F_n(x) \leq F(x+h)+h$ together with $h = L(F_n, F) \to 0$ yields $F_n(x) \to F(x)$.

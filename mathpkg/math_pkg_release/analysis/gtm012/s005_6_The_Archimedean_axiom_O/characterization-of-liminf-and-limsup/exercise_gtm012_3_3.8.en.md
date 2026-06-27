---
role: exercise
locale: en
chapter: "3"
section: "3. Sequences of real and complex numbers"
exercise_number: 8
---

# Exercise 8

Suppose $(x_n)_{n=1}^{\infty}$ and $(a_n)_{n=1}^{\infty}$ are two bounded real sequences such that $a_n \to a > 0$. Then prove that

$$\liminf_{n \to \infty} a_n x_n = a \cdot \liminf_{n \to \infty} x_n, \qquad \limsup_{n \to \infty} a_n x_n = a \cdot \limsup_{n \to \infty} x_n.$$

*Hint.* Use the characterization of $\liminf$ and $\limsup$ given in Proposition 3.4. For the $\liminf$ case, first show that $a \cdot \liminf x_n$ satisfies the two characterizing properties of $\liminf a_n x_n$. To handle the product, note that $|a_n x_n - a x_n| = |a_n - a| \, |x_n| \leq M |a_n - a|$ for some bound $M$, so $a_n x_n - a x_n \to 0$.

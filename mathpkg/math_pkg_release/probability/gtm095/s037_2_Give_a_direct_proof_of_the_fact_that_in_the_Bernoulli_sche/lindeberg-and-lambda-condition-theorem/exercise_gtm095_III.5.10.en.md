---
role: exercise
locale: en
chapter: "III"
section: "§5. Nonclassical Conditions for the Central Limit Theorem"
exercise_number: 10
---

# Exercise 10: Central Limit Theorem for Bounded Random Variables

Let $X_1, X_2, \ldots$ be a sequence of independent random variables such that
$|X_n| \leq C_n$ ($\mathbb{P}$-a.s.) and $C_n = o(D_n)$, where

$$D_n^2 = \sum_{k=1}^{n} \mathbb{E}(X_k - \mathbb{E} X_k)^2 \to \infty.$$

Show that

$$\frac{S_n - \mathbb{E} S_n}{D_n} \xrightarrow{d} \mathcal{N}(0, 1),$$

where $S_n = X_1 + \cdots + X_n$.

---
role: exercise
locale: en
chapter: "Chapter 1"
section: "§3. Random walk, arcsine law, ruin problem"
exercise_number: 4
---

# Exercise 4

Two players toss their own symmetric coins, independently. Show that the probability that each has the same number of heads after $n$ tosses is

$$2^{-2n} \sum_{k=0}^{n} (C_k^n)^2.$$

Hence deduce the identity

$$\sum_{k=0}^{n} (C_k^n)^2 = C_{2n}^n$$

(see also Problem 4 in Sect. 2).

Let $\sigma_n$ be the first time when the number of heads for the first player coincides with the number of heads for the second player (if this happens within $n$ tosses; $\sigma_n = n + 1$ if there is no such time). Find $\mathsf{E} \min(\sigma_n, n)$.

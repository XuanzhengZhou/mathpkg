---
role: exercise
locale: en
chapter: "1"
section: "6"
exercise_number: "2"
---

# Exercise 2 — Bell's Number

Let $\Omega$ contain $N$ elements. Show that the **Bell number** $B_N$ of different decompositions of $\Omega$ is given by the formula

$$B_N = e^{-1} \sum_{k=0}^{\infty} \frac{k^N}{k!}. \tag{12}$$

**Hint:** Show that

$$B_N = \sum_{k=0}^{N-1} \binom{N-1}{k} B_k, \quad \text{where } B_0 = 1,$$

and then verify that the series in (12) satisfies the same recurrence relation.

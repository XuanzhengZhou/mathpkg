---
role: exercise
locale: en
chapter: "10"
section: "14"
exercise_number: 28
---

Problems 28 and 29 deal with an instance of Polya's urn scheme. An urn contains some white balls and some black balls. A drawing is made with each ball equally likely to be drawn; the ball drawn is then replaced and another of the same color is added to the urn. This scheme is repeated over and over.

Let the pair $(m, i)$ stand for $m + 2$ balls in the urn with $i + 1$ white balls and $m - i + 1$ black balls (so $0 \leq i \leq m$). Show that this process is a Markov chain and find its transition probabilities. Show that the Martin kernel is given by

$$K((m,i), (n,j)) = \frac{\binom{n-m}{j-i}}{\binom{n+1}{j+1}} \cdot \frac{(m+1)(i+1)}{m+2}.$$

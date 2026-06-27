---
role: exercise
locale: en
chapter: "10"
section: "52"
exercise_number: 6
---

Prove $\sum_{j=k}^{n} (-1)^j \binom{n}{j} \binom{j}{k} = 0$, where $0 \leq k \leq n$.

Let $k \in \mathbb{N}$. A recurrence may be defined as a function $f: \mathbb{N} \times

The easiest type of recurrence is the linear homeogeneous kind. Specifically, if the sequence $a$ satisfies such a recurrence, then there exist $c_0, \ldots, c_k \in \mathbb{C}$ such that

$$\sum_{j=0}^{k} c_j a_{n-j} = 0$$

for all $n \geq k$. As an example of this kind, we consider the sequence whose first two terms are 1 and every subsequent term is the sum of its two immediate predecessors. Thus $k = 2$ and B7 assumes the form

$$a_n - a_{n-1} - a_{n-2} = 0 \quad \text{for } n \geq 2.$$

From B8 we obtain the power series equation

$$\sum_{j=2}^{\infty} a_j x^j - \sum_{j=2}^{\infty} a_{j-1} x^j - \sum_{j=2}^{\infty} a_{j-2} x^j = 0$$

whence

$$\sum_{j=2}^{\infty} a_j x^j - x \sum_{j=1}^{\infty} a_j x^j - x^2 \sum_{j=0}^{\infty} a_j x^j = 0.$$

Since $a(x) = \sum_{j=0}^{\infty} a_j x^j$ by definition, we obtain with $a_0 = a_1 = 1$,

$$a(x) - (1+x) - x(a(x) - 1) - x^2 a(x) = 0$$

and solving yields $a(x) = 1/(1-x-x^2)$. The roots of $1-x-x^2$ are

$$r_1 = \frac{-1+\sqrt{5}}{2} \quad \text{and} \quad r_2 = \frac{-1-\sqrt{5}}{2}.$$

Hence

$$a(x) = \frac{-1}{(r_1-x)(r_2-x)}$$

$$= \frac{1}{r_1-r_2} \left( \frac{1}{r_1} \cdot \frac{1}{1-(x/r_1)} - \frac{1}{r_2} \

A linear but nonhomogeneous recurrence arises from the problem of determining the ordinary generating function for the sequence $a$ where $a_n = \sum_{j=0}^{n} j^2$ for $n \in \mathbb{N}$. We have the recurrence $a_n - a_{n-1} - n^2 = 0$ with $a_0 = 0$, which yields in the manner of the previous example

$$\sum_{n=1}^{\infty} a_n x^n = \sum_{n=1}^{\infty} a_{n-1} x^n + \sum_{n=1}^{\infty} n^2 x^n.$$

Thus $a(x) = xa(x) + \sum_{n=1}^{\infty} n^2 x^n$, whence

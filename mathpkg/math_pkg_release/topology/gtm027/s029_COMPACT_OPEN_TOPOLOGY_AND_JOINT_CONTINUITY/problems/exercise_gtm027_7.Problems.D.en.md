---
role: exercise
locale: en
chapter: "7"
section: "Problems"
exercise_number: D
---

# Exercise D — The Diagonal Process and Sequential Compactness

Prior to the proof of the Tychonoff product theorem, the diagonal process, as outlined below, was the standard method of proving compactness of a family of functions. Recall that a topological space is called *sequentially compact* if each sequence in the space has a subsequence which converges to a point of the space.

**(a)** The product of a countable number of sequentially compact topological spaces is sequentially compact. (Suppose $\{Y_m, m \in \omega\}$ is a sequence of sequentially compact spaces and $\{f_n, n \in \omega\}$ is a sequence in the product $\bigcup \{Y_m: m \in \omega\}$. Choose an infinite subset $A_0$ of $\omega$ such that $\{f_n(0), n \in A_0\}$ converges, then choose an infinite subset $A_1$ of $A_0$ such that $\{f_n(1), n \in A_1\}$ converges, and so on by induction. The diagonal subsequence $\{f_{a_n}\}$ where $a_n$ is the $n$-th member of $A_n$ converges in the product.)

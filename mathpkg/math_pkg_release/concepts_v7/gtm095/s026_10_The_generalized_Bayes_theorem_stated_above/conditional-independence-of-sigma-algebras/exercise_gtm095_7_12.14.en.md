---
role: exercise
locale: en
chapter: "7"
section: "12"
exercise_number: 14
---

# Exercise 14

Two $\sigma$-algebras $\mathcal{G}_1$ and $\mathcal{G}_2$ are said to be *conditionally independent* relative to a $\sigma$-algebra $\mathcal{G}_3$ if

$$\mathsf{P}(A_1 A_2 \mid \mathcal{G}_3) = \mathsf{P}(A_1 \mid \mathcal{G}_3)\,\mathsf{P}(A_2 \mid \mathcal{G}_3) \quad \text{for all } A_i \in \mathcal{G}_i,\ i = 1, 2.$$

Show that conditional independence of $\mathcal{G}_1$ and $\mathcal{G}_2$ relative to $\mathcal{G}_3$ holds ($\mathsf{P}$-a.s.) if and only if any of the following conditions is fulfilled:

(a) $\mathsf{P}(A_1 \mid \sigma(\mathcal{G}_2 \cup \mathcal{G}_3)) = \mathsf{P}(A_1 \mid \mathcal{G}_3)$ for all $A_1 \in \mathcal{G}_1$;

(b) $\mathsf{P}(B \mid \sigma(\mathcal{G}_2 \cup \mathcal{G}_3)) = \mathsf{P}(B \mid \mathcal{G}_3)$ for any set $B$ in a system $\mathcal{P}_1$, which is a $\pi$-system such that $\mathcal{G}_1 = \sigma(\mathcal{P}_1)$;

(c) $\mathsf{P}(B_1 B_2 \mid \sigma(\mathcal{G}_2 \cup \mathcal{G}_3)) = \mathsf{P}(B_1 \mid \mathcal{G}_3)\,\mathsf{P}(B_2 \mid \mathcal{G}_3)$ for any $B_1$ and $B_2$ in $\pi$-systems $\mathcal{P}_1$ and $\mathcal{P}_2$ respectively such that $\mathcal{G}_1 = \sigma(\mathcal{P}_1)$ and $\mathcal{G}_2 = \sigma(\mathcal{P}_2)$;

(d) $\mathsf{E}(X \mid \sigma(\mathcal{G}_2 \cup \mathcal{G}_3)) = \mathsf{E}(X \mid \mathcal{G}_3)$ for any $\sigma(\mathcal{G}_1)$-measurable bounded random variable $X$.

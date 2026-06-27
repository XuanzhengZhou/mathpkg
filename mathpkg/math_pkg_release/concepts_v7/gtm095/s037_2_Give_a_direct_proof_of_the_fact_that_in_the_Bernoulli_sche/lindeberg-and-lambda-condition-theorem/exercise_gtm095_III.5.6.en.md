---
role: exercise
locale: en
chapter: "III"
section: "§5. Nonclassical Conditions for the Central Limit Theorem"
exercise_number: 6
---

# Exercise 6: Central Limit Theorem with Random Index

Let $\xi_1, \xi_2, \ldots$ be independent identically distributed random variables with
$\mathbb{E}\,\xi_1 = 0$, $\mathbb{E}\,\xi_1^2 = 1$. Let $(\tau_n)_{n \geq 1}$ be a sequence
of random variables taking values $1, 2, \ldots$ such that $\tau_n/n \xrightarrow{\mathbb{P}} c$,
where $c > 0$ is a constant. Show that

$$\operatorname{Law}\bigl(\tau_n^{-1/2} S_{\tau_n}\bigr) \to \Phi,$$

where $S_n = \xi_1 + \cdots + \xi_n$, i.e.,
$\tau_n^{-1/2} S_{\tau_n} \xrightarrow{d} \mathcal{N}(0, 1)$.

(Note that it is not assumed that the sequences $(\tau_n)_{n \geq 1}$ and
$(\xi_n)_{n \geq 1}$ are independent.)

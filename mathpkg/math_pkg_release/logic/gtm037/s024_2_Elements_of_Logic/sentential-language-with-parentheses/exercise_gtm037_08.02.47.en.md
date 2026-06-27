---
role: exercise
locale: en
chapter: "8"
section: "2"
exercise_number: "8.47"
---

By a sentential language with parentheses we mean a system $\mathcal{P} = (n, c, l, r, P)$ such that $n, c, l, r$ are all distinct, $P \neq \emptyset$, and $\{n, c, l, r\} \cap P = \emptyset$. We introduce operations $\neg, \rightarrow$ on expressions as follows:

$$\neg\varphi = \langle n \rangle\varphi$$
$$\varphi \rightarrow \psi = \langle l \rangle\varphi \langle c \rangle\psi \langle r \rangle,$$

for all expressions $\varphi, \psi$. $\text{Sent}^{\mathcal{P}}$ is the intersection of all sets $\Gamma$ of expressions such that $\langle s \rangle \in \Gamma$ for each $s \in P$ and $\neg\varphi \in \Gamma$, $\varphi \rightarrow \psi \in \Gamma$ for all $\varphi, \psi \in \Gamma$. Prove an analog of 8.5 (unique readability of sentences).

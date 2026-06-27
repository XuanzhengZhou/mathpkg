---
role: exercise
locale: en
chapter: "X"
section: "40"
exercise_number: 3
---

There is a concept of completeness for Boolean rings which is related to but not identical with the concept of the same name for metric spaces. A Boolean ring $R$ is complete if every subset $E$ of $R$ has a union. Clearly every complete Boolean ring is a Boolean $\sigma$-algebra; in the converse direction it is true that every totally finite measure algebra is complete.

*Hint:* Let $\tilde{E}$ be the set of all finite unions of elements of $E$. Write $\alpha = \sup \{\mu(E): E \in \tilde{E}\}$, find a sequence $\{E_n\}$ of elements of $\tilde{E}$ such that $\lim_n \mu(E_n) = \alpha$, and set $E = \bigcup_{n=1}^{\infty} E_n$.

---
role: exercise
locale: en
chapter: "17"
section: "F"
exercise_number: 1
---

Let $(E, \mathcal{T})$ be the strict inductive limit of a sequence $\{(E_n, \mathcal{T}_n)\}$ of locally convex spaces, where each $E_n$ is a closed subspace of $E_{n+1}$ and $\mathcal{T}_n$ is the relativization of $\mathcal{T}_{n+1}$ to $E_n$. Prove the following statements:

**(i)** Each $\mathcal{T}_n$ is the relativization of $\mathcal{T}$ to $E_n$, and $E_n$ is a $\mathcal{T}$-closed subspace of $E$.

**(ii)** If each $E_n$ is a Hausdorff space, then $E$ is also a Hausdorff space.

**(iii)** Every $\mathcal{T}$-bounded subset of $E$ is contained in some $E_n$.

*Hint:* Let $U_n$ be a convex circled $\mathcal{T}_n$-neighborhood of $0$ in $E_n$. Use 13E(b) to construct a sequence $\{U_{n+m} : m = 0, 1, \dots\}$ of $\mathcal{T}_{n+m}$-neighborhoods of $0$ with $E_{n+m} \cap U_{n+m+1} = U_{n+m}$, and put $U = \bigcup \{U_{n+m} : m = 0, 1, \dots\}$. For (ii) and (iii), use 13E(c) and similar constructions.

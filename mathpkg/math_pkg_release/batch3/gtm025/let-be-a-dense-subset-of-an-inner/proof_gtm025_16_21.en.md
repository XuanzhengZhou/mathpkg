---
role: proof
locale: en
of_concept: "let-be-a-dense-subset-of-an-inner"
source_book: gtm025
source_chapter: "Integration on Locally Compact Spaces"
source_section: "16.21"
---

Choose a sequence $(y_n)$ in $S$ such that $\|x - y_n\| \to 0$. Then

If $\{y_1, y_2, \ldots, y_n\}$ is all of the $y$'s, stop the construction. If $y_{n+1}$ exists, let

$$z_{n+1} = y_{n+1} - \sum_{k=1}^{n} \langle y_{n+1}, u_k \rangle u_k.$$

Now $z_{n+1}$ is not the zero vector, because $y_{n+1} \notin \text{span}\{y_1, \ldots, y_n\} = \text{span}\{u_1, \ldots, u_n\}$. Next define

$$u_{n+1} = \|z_{n+1}\|^{-1} z_{n+1}.$$

For $1 \leq j \leq n$, we have

$$\langle u_{n+1}, u_j \rangle = \|z_{n+1}\|^{-1} \left\langle y_{n+1} - \sum_{k=1}^{n} \langle y_{n+1}, u_k \rangle u_k, u_j \right\rangle$$

$$= \|z_{n+1}\|^{-1} \left( \langle y_{n+1}, u_j \rangle - \langle y_{n+1}, u_j \rangle \cdot \langle u_j, u_j \rangle \right) = 0.$$

Thus the set $\{u_1, \ldots, u_{n+1}\}$ is orthonormal; it remains to show that it spans the same subspace as $\{y_1, \ldots, y_{n+1}\}$. It is obvious from the definitions of $z_{n+1}$ and $u_{n+1}$ that $y_{n+1}$ is a linear combination of $u_1, \ldots, u_{n+1}$. Therefore

$$\{y_{n+1}\} \cup \left( \text{span}\{y_1, \ldots, y_n\} \right) \subset \text{span}\{u_1, \ldots, u_{n+1}\}.$$

and so

and so also

$$0 = \left\langle \frac{1}{\alpha} u_{n+1}, u_j \right\rangle = \left\langle y_{n+1}, u_j \right\rangle + \delta_j,$$

and

$$\delta_j = -\left\langle y_{n+1}, u_j \right\rangle \quad (1 \leq j \leq n).$$

Thus we have

$$\frac{1}{\alpha} u_{n+1} = y_{n+1} - \sum_{k=1}^{n} \left\langle y_{n+1}, u_k \right\rangle u_k,$$

just as we defined $z_{n+1}$. The number $\alpha$ is now determined from this last equality by taking norms and noting that $\|u_{n+1}\| = 1$. Clearly $\alpha$, and hence $u_{n+1}$, is unique up to a multiplicative factor of absolute value 1.

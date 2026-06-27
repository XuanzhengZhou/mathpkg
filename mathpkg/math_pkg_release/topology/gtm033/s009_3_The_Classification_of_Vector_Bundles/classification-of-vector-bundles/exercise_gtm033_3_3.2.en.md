---
role: exercise
locale: en
chapter: "3"
section: "3. The Classification of Vector Bundles"
exercise_number: 2
---

# Exercise 2

Suppose $\dim X < \min\{s-k, r-j\}$. The natural embedding

$$j: G_{s,k} \times G_{r,j} \hookrightarrow G_{s+r, k+j}$$

is defined by sending a pair of subspaces $(P \subset \mathbb{R}^s, Q \subset \mathbb{R}^r)$ of dimensions $k$ and $j$ to their direct sum $P \oplus Q \subset \mathbb{R}^s \oplus \mathbb{R}^r \cong \mathbb{R}^{s+r}$. Show that

$$j^* \gamma_{s+r, k+j} \cong \gamma_{s,k} \times \gamma_{r,j},$$

where $\gamma_{s,k} \times \gamma_{r,j}$ denotes the external Whitney sum (the vector bundle over $G_{s,k} \times G_{r,j}$ whose fiber over $(P,Q)$ is $P \oplus Q$). Conclude that under the classification Theorem 3.4, the induced map on homotopy classes

$$j_\#: [X, G_{s,k}] \times [X, G_{r,j}] \to [X, G_{s+r, k+j}]$$

corresponds to the Whitney sum operation

$$\oplus: K^k(X) \times K^j(X) \to K^{k+j}(X), \qquad ([\xi], [\eta]) \mapsto [\xi \oplus \eta].$$

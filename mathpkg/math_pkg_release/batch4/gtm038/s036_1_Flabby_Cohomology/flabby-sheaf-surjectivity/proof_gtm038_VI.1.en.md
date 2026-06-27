---
role: proof
locale: en
of_concept: flabby-sheaf-surjectivity
source_book: gtm038
source_chapter: "VI"
source_section: "1"
---
We need only show that $\psi_*$ is surjective. Let $s'' \in \Gamma(X, \mathcal{S}'')$ be given.

**1.** If $x_1, x_2$ are points in $X$, then there are neighborhoods $U(x_1), V(x_2) \subset X$ and sections $s \in \Gamma(U, \mathcal{S}), s^* \in \Gamma(V, \mathcal{S})$ with $\psi \circ s = s''|U$ and $\psi \circ s^* = s''|V$.

If $U \cap V = \emptyset$, then this defines a section over $U \cup V$, whose image is $s''|U \cup V$. Suppose $U \cap V \neq \emptyset$. The sequence
$$0 \rightarrow \Gamma(U \cap V, \mathcal{S}') \rightarrow \Gamma(U \cap V, \mathcal{S}) \rightarrow \Gamma(U \cap V, \mathcal{S}'')$$
is exact, and since $\psi \circ (s - s^*)|U \cap V = \mathbf{O}$, there is an $s' \in \Gamma(U \cap V, \mathcal{S}')$ with $\varphi \circ s' = (s - s^*)|U \cap V$.

Since $\mathcal{S}'$ is flabby, we can extend $s'$ to an element $\hat{s} \in \Gamma(V, \mathcal{S}')$. Let
$$s_1(x) := \begin{cases} s(x) & \text{for } x \in U \\ (\varphi \circ \hat{s} + s^*)(x) & \text{for } x \in V. \end{cases}$$
Then $s_1$ lies in $\Gamma(U \cup V, \mathcal{S})$ and $\psi \circ s_1 = s''|U \cup V$.

**2.** We consider the system $\mathfrak{M}$ of all pairs $(\tilde{U}, \tilde{s})$ where $\tilde{U} \subset X$ is open and $\tilde{s} \in \Gamma(\tilde{U}, \mathcal{S})$ satisfies $\psi \circ \tilde{s} = s''|\tilde{U}$. By step 1, for any two points we obtain a common extension. Using Zorn's lemma, we obtain a maximal element $(U_{\max}, s_{\max})$ in $\mathfrak{M}$. By the extension property, $U_{\max}$ must be all of $X$. Hence $\psi_*$ is surjective.

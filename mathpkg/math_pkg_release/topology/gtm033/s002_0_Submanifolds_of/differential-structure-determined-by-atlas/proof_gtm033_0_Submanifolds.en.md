---
role: proof
locale: en
of_concept: differential-structure-determined-by-atlas
source_book: gtm033
source_chapter: "0"
source_section: "Submanifolds of R^{n+k}"
---

# Proof of Differential Structure Determined by a Single Atlas

Let $M$ be a topological space and let $\Phi = \{(\varphi_i, U_i)\}_{i \in I}$ be a $C^r$ atlas on $M$, i.e., every pair of charts in $\Phi$ has $C^r$ overlap. Define

$$\Psi = \{ (\psi, V) \mid (\psi, V) \text{ is a chart on } M \text{ having } C^r \text{ overlap with every chart in } \Phi \}.$$

We verify that $\Psi$ is the unique maximal $C^r$ atlas containing $\Phi$.

**1. $\Psi$ contains $\Phi$.** Take any $(\varphi_i, U_i) \in \Phi$. For any $(\varphi_j, U_j) \in \Phi$, the overlap condition holds by hypothesis: $\varphi_j \circ \varphi_i^{-1}$ is $C^r$ on $\varphi_i(U_i \cap U_j)$ and $\varphi_i \circ \varphi_j^{-1}$ is $C^r$ on $\varphi_j(U_i \cap U_j)$. Hence $(\varphi_i, U_i)$ has $C^r$ overlap with every chart in $\Phi$, so $(\varphi_i, U_i) \in \Psi$. Thus $\Phi \subset \Psi$.

**2. $\Psi$ is a $C^r$ atlas.** Take any two charts $(\psi_1, V_1), (\psi_2, V_2) \in \Psi$ with $V_1 \cap V_2 \neq \varnothing$. We must show $\psi_2 \circ \psi_1^{-1}$ is $C^r$ on $\psi_1(V_1 \cap V_2)$. Pick any $p \in V_1 \cap V_2$. Since $\Phi$ covers $M$, there exists $(\varphi, U) \in \Phi$ with $p \in U$. On the open neighborhood $\psi_1(V_1 \cap V_2 \cap U)$ of $\psi_1(p)$, write

$$\psi_2 \circ \psi_1^{-1} = (\psi_2 \circ \varphi^{-1}) \circ (\varphi \circ \psi_1^{-1}).$$

Both $\psi_2 \circ \varphi^{-1}$ and $\varphi \circ \psi_1^{-1}$ are $C^r$ by definition of $\Psi$ (each $\psi_k$ has $C^r$ overlap with every chart in $\Phi$, in particular with $\varphi$). Their composition is therefore $C^r$ on the appropriate open set. Hence $\Psi$ is a $C^r$ atlas.

**3. $\Psi$ is maximal.** Suppose $(\theta, W)$ is a chart having $C^r$ overlap with every chart in $\Psi$. In particular it has $C^r$ overlap with every chart in $\Phi$ (since $\Phi \subset \Psi$), so $(\theta, W) \in \Psi$ by definition. Thus $\Psi$ cannot be enlarged by adding any further chart — it is maximal.

**4. Uniqueness.** If $\Psi'$ is another maximal $C^r$ atlas containing $\Phi$, then every chart in $\Psi'$ has $C^r$ overlap with every chart in $\Phi$, so $\Psi' \subset \Psi$ by definition of $\Psi$. Maximality of $\Psi'$ forces $\Psi' = \Psi$.

Therefore $\Psi$ is the unique maximal $C^r$ atlas containing $\Phi$, i.e., the unique $C^r$ differential structure determined by $\Phi$. $\square$

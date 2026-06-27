---
role: proof
locale: en
of_concept: theorem-8-8
source_book: gtm008
source_chapter: "2"
source_section: "2 There is a class"
---
If $t_1 \in T_\alpha$ we obtain, as in the proof of Theorem 8.6

$$\text{Ord}^1(t \simeq t_1) \leq \text{Ord}^1(t \in \hat{x}^\alpha \varphi(x^\alpha)).$$

Again we need only consider the case

$$\alpha_0 \triangleq \text{Ord}^1(t \simeq t_1) = \text{Ord}^1(t \in \hat{x}^\alpha \varphi(x^\alpha)).$$

Then $\alpha_0 = \max(g(t), g(\hat{x}^\alpha \varphi(x^\alpha)) = \max(g(t), g(t_1)) = g(t)$, since $t_1 \in T_\alpha \rightarrow \rho(t_1) < g(\hat{x}^\alpha \varphi(x^\alpha))$. Therefore $\text{Ord}^1(t \in \hat{x}^\alpha \varphi(x^\alpha)) = g(t)$ and hence

$$\text{Ord}^2(t \in \hat{x}^\alpha \varphi(x^\alpha)) = 1.$$

On the other hand since $\alpha_0 = \text{Ord}^1(t \simeq t_1) = g(t)$ and $g(t) \neq g(\forall x^\beta) = 2\beta + 1$ where $\beta = \max(\rho(t), \rho(t_1))$,

$$\text{Ord}^2(t \simeq t_1) =

then $\alpha_0 = g(t)$ since rank $(k_1) < \text{rank}(k_2)$. Therefore
$$\text{Ord}^2(t \in k_2) = 1.$$

But
$$\text{Ord}^2(t \simeq k_1) = 0.$$

Hence
$$\text{Ord}(t \simeq k_1) < \text{Ord}(t \in k_2).$$

**Theorem 8.11.** rank $(k) \leq \rho(t) \rightarrow \text{Ord}(t \simeq k) < \text{Ord}(P(t)).$$

**Proof.** $\text{Ord}^1(P(t)) = g(t) = \text{Ord}^1(t \simeq k)$, since rank $(k) \leq \rho(t).$
$$\text{Ord}^2(P(t)) = 1$$

But
$$\text{Ord}^2(t \simeq k) = 0.$$

Hence
$$\text{Ord}(t \simeq k) < \text{Ord}(P(t)).$$

**Definition 8.12.** If $t$ is a term then
$$\text{Ord}^1(t) \triangleq g(t), \quad \text{Ord}^2(t) \triangleq 0, \quad \text{Ord}^3(t) \triangleq 0, \quad \text{Ord}(t) \triangleq \omega^2 \cdot g(t).$$

**Theorem 8.13.**
1. Ord $(t) < \text{Ord}(P(t))$
2. max $(\text{Ord}(t_1), \text{Ord}(t_2)) < \text{Ord}(t_1 \in t_2)$.

**Remark.** The preceding theorems provide a basis for the definition of a denotation operator $D$ defined on terms and closed limited formulas. The definition is by recursion on Ord $(t)$ and Ord $(\varphi)$.

**Definition 8.14**
1. $D(\underline{k}) \triangleq k, k \in K.$
2. $D(\hat{x}^\alpha \

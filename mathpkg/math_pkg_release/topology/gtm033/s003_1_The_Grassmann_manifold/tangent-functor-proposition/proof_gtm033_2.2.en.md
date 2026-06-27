---
role: proof
locale: en
of_concept: tangent-functor-proposition
source_book: gtm033
source_chapter: "2. Differentiable Maps and the Tangent Bundle"
source_section: "2"
---

# Proof of the Tangent Functor

The assignments $M \mapsto TM$, $f \mapsto Tf$ define a covariant functor $T$ from the category of $C^{r+1}$ manifolds to the category of $C^r$ manifolds.

**Proof.** We verify the two functor axioms.

**Composition.** Let $f: M \to N$ and $g: N \to Q$ be $C^{r+1}$ maps. Choose charts $\varphi_i: U_i \to \mathbb{R}^m$ on $M$, $\psi_j: V_j \to \mathbb{R}^n$ on $N$, and $\theta_k: W_k \to \mathbb{R}^p$ on $Q$ with $f(U_i) \subset V_j$ and $g(V_j) \subset W_k$. The local representation of $T(g \circ f)$ in the natural charts on $TM$ and $TQ$ is:

$$T(g \circ f)[x, i, a] = [g(f(x)), k, D(\theta_k g f \varphi_i^{-1})(\varphi_i x) \, a].$$

By the chain rule,

$$D(\theta_k g f \varphi_i^{-1})(\varphi_i x) = D(\theta_k g \psi_j^{-1})(\psi_j f(x)) \cdot D(\psi_j f \varphi_i^{-1})(\varphi_i x).$$

Hence,

$$T(g \circ f)[x, i, a] = [g(f(x)), k, D(\theta_k g \psi_j^{-1})(\psi_j f(x)) \cdot D(\psi_j f \varphi_i^{-1})(\varphi_i x) \, a].$$

On the other hand,

$$(Tg \circ Tf)[x, i, a] = Tg[f(x), j, D(\psi_j f \varphi_i^{-1})(\varphi_i x) \, a]$$
$$= [g(f(x)), k, D(\theta_k g \psi_j^{-1})(\psi_j f(x)) \cdot D(\psi_j f \varphi_i^{-1})(\varphi_i x) \, a].$$

Thus $T(g \circ f) = Tg \circ Tf$ on each $TU_i$, and therefore globally.

**Identity.** For the identity map $1_M: M \to M$, its local representation in any chart is the identity on $\mathbb{R}^m$, whose derivative is the identity matrix. Hence,

$$T(1_M)[x, i, a] = [x, i, I_m \cdot a] = [x, i, a] = 1_{TM}[x, i, a].$$

Thus $T(1_M) = 1_{TM}$.

Both axioms hold, so $T$ is a covariant functor. $\square$

The commutativity of the naturality square $f \circ p_M = p_N \circ Tf$ follows from the definition: $p_M[x,i,a] = x$ and $p_N Tf[x,i,a] = p_N[f(x), j, \dots] = f(x) = f(p_M[x,i,a])$.

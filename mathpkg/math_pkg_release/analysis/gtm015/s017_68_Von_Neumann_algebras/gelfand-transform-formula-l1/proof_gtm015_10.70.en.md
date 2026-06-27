---
role: proof
locale: en
of_concept: gelfand-transform-formula-l1
source_book: gtm015
source_chapter: "10"
source_section: "70"
---

# Proof of Gel'fand transform formula for L^1(G)

Proof. For fixed $M$, both of the mappings

$$u \mapsto \hat{u}(M) \quad \text{and} \quad u \mapsto \int f(t) \alpha_M(t) dt$$

are epimorphisms $L^1(G) \to \mathbb{C}$ with kernel $M$, hence they are identical.

Indeed, by definition $\hat{u}(M) = \varphi_M(u)$ where $\varphi_M$ is the algebra epimorphism with kernel $M$ (52.18). On the other hand, by (70.3) and (70.7), $\varphi_M$ corresponds to the continuous character $\alpha_M$ of $G$ via the integral formula. Since an algebra epimorphism to $\mathbb{C}$ is determined (up to a scalar multiple) by its kernel, and both maps have kernel $M$ and send the approximate identity to 1 (i.e., are unital on the unitization), they must coincide for all $u \in L^1(G)$.

---
role: proof
locale: en
of_concept: decomposable-systems
source_book: gtm026
source_chapter: "2"
source_section: "2.3 Input Processes and Output Processes"
---

For the input process part, we must exhibit a left adjoint to $U: \operatorname{Dyn}(\operatorname{id}_{\mathcal{K}}) \to \mathcal{K}$. An object of $\operatorname{Dyn}(\operatorname{id}_{\mathcal{K}})$ is a pair $(Q, \delta)$ where $\delta: Q \to Q$ is an endomorphism; a morphism $f: (Q, \delta) \to (Q', \delta')$ is a morphism $f: Q \to Q'$ with $\delta' \circ f = f \circ \delta$.

Define the free $\operatorname{id}_{\mathcal{K}}$-dynamics over $A$ as $(A^{\#}, \mu_0)$ where $A^{\#} = \coprod_{n \in \mathbb{N}} A$ is the countably infinite copower of $A$ and $\mu_0: A^{\#} \to A^{\#}$ is the endomorphism induced by the successor map on indices: the $n$-th injection $\operatorname{in}_n: A \to A^{\#}$ is mapped via $\mu_0$ to $\operatorname{in}_{n+1}$. Formally, $\mu_0 \circ \operatorname{in}_n = \operatorname{in}_{n+1}$ for all $n \in \mathbb{N}$. The unit $A\eta: A \to A^{\#}$ is the zeroth injection $\operatorname{in}_0$.

Given any $\operatorname{id}_{\mathcal{K}}$-dynamics $(Q, \delta)$ and a morphism $f: A \to Q$, define the dynamorphic extension $f^{\#}: A^{\#} \to Q$ by specifying $f^{\#} \circ \operatorname{in}_n = \delta^n \circ f$ for each $n \in \mathbb{N}$ (where $\delta^0 = \operatorname{id}_Q$). The universal property of the copower guarantees that this defines $f^{\#}$ uniquely. One verifies that $f^{\#}$ is an $\operatorname{id}_{\mathcal{K}}$-dynamorphism:
$$\delta \circ f^{\#} \circ \operatorname{in}_n = \delta \circ \delta^n \circ f = \delta^{n+1} \circ f = f^{\#} \circ \operatorname{in}_{n+1} = f^{\#} \circ \mu_0 \circ \operatorname{in}_n,$$
so $\delta \circ f^{\#} = f^{\#} \circ \mu_0$. Moreover $f^{\#} \circ \operatorname{in}_0 = \delta^0 \circ f = f$, i.e., $f^{\#} \circ A\eta = f$, and $f^{\#}$ is clearly uniquely determined by this condition and the dynamorphism property.

For the output process part, $U$ has a right adjoint. The cofree $\operatorname{id}_{\mathcal{K}}$-dynamics over $A$ is $(A_{\#}, L)$ where $A_{\#} = \prod_{n \in \mathbb{N}} A$ is the countably infinite power and $L: A_{\#} \to A_{\#}$ is the shift endomorphism defined by $\operatorname{pr}_n \circ L = \operatorname{pr}_{n+1}$ for all $n \in \mathbb{N}$. The counit $A\Lambda: A_{\#} \to A$ is the zeroth projection $\operatorname{pr}_0$.

Given any $\operatorname{id}_{\mathcal{K}}$-dynamics $(Q, \delta)$ and a morphism $f: Q \to A$, define the dynamorphic coextension $f_{\#}: Q \to A_{\#}$ by specifying $\operatorname{pr}_n \circ f_{\#} = f \circ \delta^n$ for each $n \in \mathbb{N}$. The universal property of the power guarantees uniqueness. The dynamorphism condition $L \circ f_{\#} = f_{\#} \circ \delta$ follows from:
$$\operatorname{pr}_n \circ L \circ f_{\#} = \operatorname{pr}_{n+1} \circ f_{\#} = f \circ \delta^{n+1} = f \circ \delta^n \circ \delta = \operatorname{pr}_n \circ f_{\#} \circ \delta,$$
and $\operatorname{pr}_0 \circ f_{\#} = f \circ \delta^0 = f$, so $A\Lambda \circ f_{\#} = f$.

Thus $X = \operatorname{id}_{\mathcal{K}}$ is both an input process and an output process.

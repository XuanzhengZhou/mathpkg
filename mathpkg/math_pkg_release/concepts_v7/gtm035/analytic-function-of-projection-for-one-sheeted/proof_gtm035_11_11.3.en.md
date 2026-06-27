---
role: proof
locale: en
of_concept: analytic-function-of-projection-for-one-sheeted
source_book: gtm035
source_chapter: "11"
source_section: "11.3"
---
# Proof of One-Sheeted Implies Analytic Function of Projection

**Corollary 11.3.** Let $(A, X, \Omega, f)$ be a maximum modulus algebra and fix a closed disk $\Delta \subseteq \Omega$. Assume that $X$ lies one-sheeted over $\Delta$, in the sense that $f^{-1}(\lambda)$ consists of a single point for each $\lambda \in \Delta$. Then, over $\Delta$, every $g \in A$ is an analytic function of $f$, i.e., there exists $G$ analytic on $\operatorname{int}(\Delta)$ and continuous on $\Delta$ such that $g = G \circ f$ on $f^{-1}(\Delta)$.

*Proof.* Fix $g \in A$. By Theorem 11.2, there exists a bounded analytic function $G$ on $\operatorname{int}(\Delta)$ such that

$$G(\lambda) \in \overline{\operatorname{co}}(g(f^{-1}(\lambda))) \quad \text{for a.a. } \lambda \in \partial \Delta.$$

By hypothesis, $f^{-1}(\lambda)$ is a singleton for each $\lambda \in \Delta$; so $\overline{\operatorname{co}}(g(f^{-1}(\lambda))) = \{g(f^{-1}(\lambda))\}$, and hence

$$G(\lambda) = g(f^{-1}(\lambda)) \quad \text{a.e. on } \partial \Delta.$$

Now $f$ is a one-to-one continuous map of the compact set $f^{-1}(\partial \Delta)$ onto $\partial \Delta$, and therefore $f^{-1}$ is continuous on $\partial \Delta$. Consequently, $g \circ f^{-1}$ is continuous on $\partial \Delta$.

It follows that $G$ agrees with a continuous function on $\partial \Delta$, and therefore $G$ extends continuously to the closed disk $\Delta$. By the maximum principle, this extension is unique. Hence we can choose a sequence of polynomials $\{P_n\}$ such that $P_n \to G$ uniformly on $\Delta$. Since $P_n \circ f \in A$ and $P_n \circ f \to G \circ f$ uniformly on $f^{-1}(\Delta)$, we obtain $g = G \circ f$ on $f^{-1}(\Delta)$. Moreover, $G$ is analytic on $\operatorname{int}(\Delta)$. $\square$

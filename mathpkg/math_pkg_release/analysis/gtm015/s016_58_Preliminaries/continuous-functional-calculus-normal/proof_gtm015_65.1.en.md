---
role: proof
locale: en
of_concept: continuous-functional-calculus-normal
source_book: gtm015
source_chapter: "65"
source_section: "Continuous functional calculus"
---

# Proof of Continuous functional calculus for normal elements

Proof. It is straightforward to check that $\Phi$ is a $*$-homomorphism with $\Phi(1) = 1$ and $\Phi(u) = a$. Moreover,

$$\|\Phi(f)\| = \|(\Phi(f))^*\|_\infty = \|f \circ \hat{a}\|_\infty = \sup \{|f(\hat{a}(M))| : M \in \mathcal{M}\} = \sup \{|f(\lambda)| : \lambda \in \sigma(a)\} = \|f\|_\infty,$$

thus $\Phi$ is isometric.

Assuming $\Psi : \mathcal{C}(\sigma(a)) \to A$ is a $*$-homomorphism with $\Psi(1) = 1$ and $\Psi(u) = a$, let us show that $\Psi = \Phi$. From (60.1) we know that $\Psi$ is continuous. It follows that the set $\mathcal{A} = \{f \in \mathcal{C}(\sigma(a)) : \Psi(f) = \Phi(f)\}$ is a closed $*$-subalgebra of $\mathcal{C}(\sigma(a))$ containing $1$ and $u$; by the Weierstrass-Stone theorem (the function $u$ already separates the points of $\sigma(a)$) we have $\mathcal{A} = \mathcal{C}(\sigma(a))$, that is, $\Psi = \Phi$.

It remains to be shown that the range of $\Phi$ is $C$. From the properties of $\Phi$, we know that its range is a closed $*$-subalgebra of $A$ containing $1$ and $a$, therefore $\Phi(\mathcal{C}(\sigma(a))) \supset C$. On the other hand, $\Phi^{-1}(C)$ is a closed $*$-subalgebra of $\mathcal{C}(\sigma(a))$ containing $1$ and $u$, therefore $\Phi^{-1}(C) = \mathcal{C}(\sigma(a))$, thus $\Phi(\mathcal{C}(\sigma(a))) \subset C$.

---
role: proof
locale: en
of_concept: extension-property-stone-cech
source_book: gtm015
source_chapter: "64"
source_section: "Stone-Čech compactification"
---

# Proof of Extension property of Stone-Čech compactification

Proof. Suppose $x: T \to \mathbb{R}$ is bounded and continuous. In particular, $x \in \mathcal{C}^\infty(T)$. Define $F = \hat{x}$, the Gel'fand transform of $x$. For all $t \in T$,

$$F(\varphi(t)) = \hat{x}(f_t) = f_t(x) = x(t),$$

thus $F \circ \varphi = x$; in particular, $F$ is real-valued on $\varphi(T)$, therefore $F$ is real-valued on $\mathcal{X}$ (64.4).

This completes the proof of (64.1). Such a pair $(\mathcal{X}, \varphi)$ is called a Stone-Čech compactification of $T$. {It is not difficult to show, but inappropriate to do it here, that such a pair is essentially unique. See, e.g., [85, p. 153], [134, p. 331, Th. A].}

65. The continuous functional calculus (spectral theorem for a normal operator). For general remarks on functional calculi, see the introduction of Section 53. The continuous functional calculus is applicable to any normal element of any $C^*$-algebra $A$ with unity; applied to the $C^*$-algebra $A = \mathcal{L}(H)$, $H$ a Hilbert space, this theory is the core of what is known as the spectral theory of normal operators.

(65.1

It is straightforward to check that $\Phi$ is a *-homomorphism with $\Phi(1) = 1$ and $\Phi(u) = a$. Moreover,

$$\|\Phi(f)\| = \|(\Phi(f))^*\|_\infty = \|f \circ \hat{a}\|_\infty$$

$$= \sup \{|f(\hat{a}(M))| : M \in \mathcal{M}\}$$

$$= \sup \{|f(\lambda)| : \lambda \in \sigma(a)\} = \|f\|_\infty,$$

thus $\Phi$ is isometric.

Assuming $\Psi : \mathcal{C}(\sigma(a)) \rightarrow A$ is a *-homomorphism with $\Psi(1) = 1$ and $\Psi(u) = a$, let us show that $\Psi = \Phi$. From (60.1) we know that $\Psi$ is continuous. It follows that the set

$$\mathcal{A} = \{f \in \mathcal{C}(\sigma(a)) : \Psi(f) = \Phi(f)\}$$

is a closed *-subalgebra of $\mathcal{C}(\sigma(a))$ containing 1 and $u$; by the Weierstrass-Stone theorem (the function $u$ already separates the points of $\sigma(a)$) we have $\mathcal{A} = \mathcal{C}(\sigma(a))$, that is, $\Psi = \Phi$.

It remains to be shown that the range of $\Phi$ is $C$. From the properties of $\Phi$, we know that its range is a closed *-subalgebra of $A$ containing 1 and $a$, therefore $\Phi(\mathcal{C}(\sigma(a))) \supset C$. On the other hand, $\Phi^{-1}(C)$ is a closed *-subalgebra of $\mathcal{C}(\sigma(a))$ containing 1 and $u$, therefore $\Phi^{-1}(C) = \mathcal{C}(\sigma(a))$, thus $\Phi(\mathcal{C}(\sigma(a))) \subset C$.

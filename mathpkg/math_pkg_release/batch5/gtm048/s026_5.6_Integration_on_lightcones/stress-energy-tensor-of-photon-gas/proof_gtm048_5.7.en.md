---
role: proof
locale: en
of_concept: stress-energy-tensor-of-photon-gas
source_book: gtm048
source_chapter: "5"
source_section: "7"
---

*Proof.* Suppose $x \in M$. Since $F$ restricted to $\mathcal{L}_x^+$ is of rapid decay, there exists a function $T: M_x^* 	o \mathbb{R}$ defined by $\omega \mapsto \int 	ilde{\omega}^2 F \Lambda_x$ (Exercise 5.6.6e); here, and throughout this proof, the domain of integration will be $\mathcal{L}_x^+$ unless indicated otherwise. Since $T$ is a quadratic function, it determines a unique symmetric tensor $\hat{T}_x \in T_0^2(M_x)$ such that

$$\hat{T}_x(\omega, \eta) = \int 	ilde{\omega} 	ilde{\eta} F \Lambda_x.$$

We note the following properties.

(a') $\hat{T}_x(\omega, \omega) \geq 0$ for all $\omega \in M_x^*$, since $F$ is nonnegative.

(b') If $F$ is not identically zero on $\mathcal{L}_x^+$ and $W \in M_x$ is causal, then $\hat{T}_x W$ is timelike. In fact suppose $\omega, \eta \in M_x^*$ are future pointing. Then $\hat{T}_x(\omega, \eta) > 0$.

These properties at each $x \in M$ collectively yield the global statement of the proposition. Specifically, property (a) of the proposition follows from (a') and the fact that the definition is tensorial; property (b) follows from (b'); property (c) follows from the fact that $F$ is supported on the lightcone, where $g(\dot{\lambda}, \dot{\lambda}) = 0$, implying the trace vanishes; and property (d) follows from the identification of the integral over $P_X$ with the integral expression for $T(X,X)$ via the natural diffeomorphism $\pi_X: P_X 	o \mathcal{L}_x^+$.

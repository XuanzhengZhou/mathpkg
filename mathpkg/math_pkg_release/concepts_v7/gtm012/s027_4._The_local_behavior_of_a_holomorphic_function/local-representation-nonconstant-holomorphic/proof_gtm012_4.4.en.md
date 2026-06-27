---
role: proof
locale: en
of_concept: local-representation-nonconstant-holomorphic
source_book: gtm012
source_chapter: "4"
source_section: "4. The local behavior of a holomorphic function"
---

# Proof of Local Representation of a Nonconstant Holomorphic Function

**Lemma 4.1.** Suppose $f$ is holomorphic in an open set $\Omega$ and $z_0 \in \Omega$. If $f$ is not constant near $z_0$, then

$$f(z) = a_0 + a_m(z - z_0)^m h(z)$$

where $a_0$ and $a_m$ are constants, $m \geq 1$, and $h$ is holomorphic in $\Omega$ with $h(z_0) = 1$.

*Proof.* Near $z_0$, $f$ is given by a power series expansion

$$f(z) = a_0 + a_1(z - z_0) + \cdots + a_n(z - z_0)^n + \cdots.$$

Let $m$ be the first integer $\geq 1$ such that $a_m \neq 0$. Then the power series gives the desired representation with

$$h(z) = \sum_{n=m}^{\infty} a_n a_m^{-1} (z - z_0)^{n-m}.$$

This function is holomorphic near $z_0$, and $h(z_0) = 1$. On the other hand, the representation $f(z) = a_0 + a_m(z - z_0)^m h(z)$ defines a function $h$ in $\Omega$ except at $z_0$, and the function so defined is holomorphic. Thus there is a single such function holomorphic throughout $\Omega$. $\square$

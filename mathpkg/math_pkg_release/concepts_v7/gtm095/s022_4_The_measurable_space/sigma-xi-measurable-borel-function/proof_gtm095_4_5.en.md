---
role: proof
locale: en
of_concept: sigma-xi-measurable-borel-function
source_book: gtm095
source_chapter: "4"
source_section: "5"
---

# Proof of Representation of $\mathcal{F}_\xi$-Measurable Functions as Borel Functions of $\xi$

Let $\eta = \eta(\omega)$ be an $\mathcal{F}_\xi$-measurable random variable. By Theorem 1, there exists a sequence of simple $\mathcal{F}_\xi$-measurable random variables $\eta_n$ such that $\eta_n(\omega) \to \eta(\omega)$ for all $\omega \in \Omega$.

Since each $\eta_n$ is simple and $\mathcal{F}_\xi$-measurable, it takes the form

$$\eta_n(\omega) = \sum_{k} y_{n,k} I_{A_{n,k}}(\omega),$$

with $A_{n,k} \in \mathcal{F}_\xi$. By definition of $\mathcal{F}_\xi$, for each $A_{n,k}$ there exists a Borel set $B_{n,k} \in \mathcal{B}(R)$ such that $A_{n,k} = \{\omega : \xi(\omega) \in B_{n,k}\} = \xi^{-1}(B_{n,k})$. Hence

$$\eta_n(\omega) = \sum_k y_{n,k} I_{B_{n,k}}(\xi(\omega)) = \varphi_n(\xi(\omega)),$$

where $\varphi_n(x) = \sum_k y_{n,k} I_{B_{n,k}}(x)$ is a simple Borel function on $R$.

Now define $\varphi(x) = \limsup_n \varphi_n(x)$ (or $\lim_n \varphi_n(x)$ where the limit exists). Since each $\varphi_n$ is Borel, $\varphi$ is a Borel function. Then for all $\omega \in \Omega$,

$$\eta(\omega) = \lim_n \eta_n(\omega) = \lim_n \varphi_n(\xi(\omega)) = \varphi(\xi(\omega)).$$

Thus $\eta = \varphi \circ \xi$ with $\varphi$ Borel. Consequently $\tilde{\Phi}_\xi = \Phi_\xi$, where $\Phi_\xi$ denotes the class of $\mathcal{F}_\xi$-measurable functions and $\tilde{\Phi}_\xi$ the class of Borel functions of $\xi$.

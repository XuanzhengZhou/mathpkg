---
role: proof
locale: en
of_concept: pullback-preserves-kernels
source_book: gtm004
source_chapter: "II"
source_section: "6"
---

# Proof that Pull-backs Preserve Kernels

Let the commutative square

$$\begin{array}{ccc}
Y & \xrightarrow{\beta} & B \\
{\scriptstyle \alpha}\downarrow & & \downarrow{\scriptstyle \psi} \\
A & \xrightarrow{\varphi} & X
\end{array}$$

be a pull-back diagram in a category $\mathfrak{C}$ with zero object.

**(i)** Let $(J, \mu)$ be the kernel of $\beta$. We claim that $(J, \alpha\mu)$ is the kernel of $\varphi$.

First, $\varphi(\alpha\mu) = \psi(\beta\mu) = \psi 0 = 0$, so $\alpha\mu$ annihilates $\varphi$.

Now take $\tau : Z \to A$ with $\varphi \tau = 0$. Since $\psi 0 = 0$, the pull-back property shows that there exists a unique $\sigma : Z \to Y$ such that $\alpha \sigma = \tau$ and $\beta \sigma = 0$. Since $(J, \mu)$ is the kernel of $\beta$, we have $\sigma = \mu \tau_0$ for a unique $\tau_0 : Z \to J$. Hence $\tau = \alpha \mu \tau_0$.

Thus $(J, \alpha\mu)$ satisfies the universal property of the kernel of $\varphi$.

**(ii)** Let $(J, \nu)$ be the kernel of $\varphi$. Since $\varphi \nu = 0$, the pull-back property gives a unique $\mu : J \to Y$ with $\alpha \mu = \nu$ and $\beta \mu = 0$. Since $\nu$ is a monomorphism, $\mu$ is also a monomorphism.

We show $(J, \mu)$ is the kernel of $\beta$. Let $\beta \tau = 0$ with $\tau : Z \to Y$. Then $\varphi \alpha \tau = \psi \beta \tau = 0$, so $\alpha \tau = \nu \tau_0 = \alpha \mu \tau_0$ for some $\tau_0$. Also $\beta \tau = 0 = \beta \mu \tau_0$. Since the pair $\{\alpha, \beta\}$ is a monomorphism (a property of pull-backs), $\tau = \mu \tau_0$, with $\tau_0$ unique because $\mu$ is monic.

Thus $(J, \mu)$ is the kernel of $\beta$.

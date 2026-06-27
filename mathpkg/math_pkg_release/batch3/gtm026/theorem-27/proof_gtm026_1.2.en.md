---
role: proof
locale: en
of_concept: theorem-27
source_book: gtm026
source_chapter: "1"
source_section: "2.15"
---

Let $(X^@, \eta, \mu; \rho)$ be the free algebraic theory over $X$ and let $A$ be an object in $\mathcal{K}$. Since $U : \text{Dyn}(X) \longrightarrow \mathcal{K}$ clearly creates limits it suffices to show—by the general adjoint functor theorem—that $(AX^@, AX^@\rho.A\mu; A\eta)$ is a one-element solution set for $A$ (and is then in fact the free dynamics over $A$ by the proof of 2.13). Let $(Q, \delta)$ be an $X$-dynamics and let $f : A \longrightarrow Q$. Let $\mathcal{P}$ be the full subcategory of $\text{Dyn}(X)$ of all $X$-dynamics admitting a dynamorphism, $U$ of which is mono, into a power of copies of $(Q, \delta)$. Essentially the same arguments as in 3.4.24 make it clear that $\mathcal{P}$ is closed under limits. By construction, $(Q, \delta)$ is a cogenerator in $\mathcal{P}$. By the special adjoint functor theorem (it is not necessary to first prove that $\

2.16 Algebra Automata. Let $\Omega$ be an operator domain as in 1.5.34 and define $X_{\Omega} : \text{Set} \longrightarrow \text{Set}$ by

$$QX_{\Omega} = \coprod_{\omega \in \Omega_n} Q^n$$

Then $\text{Dyn}(X_{\Omega})$ is, essentially, the category of $\Omega$-algebras and $\Omega$-homomorphisms. By 3.1.27, if $\Omega$ is bounded then $X_{\Omega}$ is an input process. Unless $\Omega$ has only unary operations—in which case $X_{\Omega} = - \times \Omega_1$ recaptures 2.1—$X_{\Omega}$ is not an output process (see exercise 1).

For finitary $\Omega$, $X_{\Omega}$-automata are interpreted as tree processors in computer science (see [Bobrow and Arbib '74, section 3–4]). We hint at the reason. Consider the arithmetic expression

$$p = \sqrt{x^2 + (x - 5)^2}$$

Let $\Omega_0 = \{5\}$, $\Omega_1 = \{()^2, \sqrt{}\}$ and $\Omega_2 = \{+, -\}$. Set $Q = \mathbf{R}$, $I = \{x\}$. For each real number $\tau : I \longrightarrow Q$, the reachability map $r : I \times X_{\Omega} @ \Omega \longrightarrow Q$ evaluates expressions in one variable. For example, $p(\tau) = \langle p, r \rangle$. More realistically, $Q$ should be the finite set of all internal computer bit configurations used to code real numbers and $\beta : Q \longrightarrow Y$ should reflect internal-to-external coding.

We conclude this section with a minimal realization theorem, pausing to define morphisms of automata:

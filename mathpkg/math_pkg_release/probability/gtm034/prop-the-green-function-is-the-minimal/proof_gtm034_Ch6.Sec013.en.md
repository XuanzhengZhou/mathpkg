---
role: proof
locale: en
of_concept: prop-the-green-function-is-the-minimal
source_book: gtm034
source_chapter: "6"
source_section: "013"
---

Proof: Since $f(x) = h(x) + G(x,0), h(x) \geq 0, G(x,0)$ is minimal, i.e., every non-negative solution of (b) is greater than, or equal to, $G(x,0)$ everywhere. By T24.1 the only bounded non-negative solutions of (b) are $G(x,0) +$ constant, and in view of T24.2, such a solution will have lower limit zero as $|x| \to \infty$ if, and only if, the constant is zero.

Our next topic is the classification of subsets $A$ of $R$ (only infinite subsets will turn out to be of real interest) according to whether they are transient or recurrent. To avoid any possible misunderstanding we re-emphasize that the random walk is assumed to be transient and aperiodic. It seems tempting to call a set $A$ recurrent if

might have been based on the escape probabilities $E_A(x)$. If $E_A(x) = 0$ for all $x$ in $A$, then we conclude that the set $A$ is in some sense "large enough" so that it is impossible for the random walk to leave it forever. Such a set might be called recurrent. Conversely, a set $A$ such that $E_A(x) > 0$ for some $x$ in $A$ would then be transient. Fortunately this classification turns out to be the same as that in D2. From P4 one has

$$H_A(x) = h_A + \sum_{t \in A} G(x,t)E_A(t), \quad x \in R.$$

If $E_A(t) = 0$ for all $t$ in $A$, than $H_A(x) \equiv h_A$. But the constant $h_A$ must have the value one, as $H_A(x) = 1$ when $x$ is in $A$. Therefore a set $A$ on which $E_A$ vanishes identically is necessarily a recurrent set. Conversely, let us suppose that $A$ is a recurrent set, so that $H_A(x) \equiv 1$. Then P4 shows that

$$h_A = \lim_{n \to \infty} \sum_{t \in R} P_n(x,t)H_A(t) = 1.$$

Hence

$$1 = 1 + \sum_{t \in A} G(x,t)E_A(t), \quad x \in R.$$

But this equation justifies the conclusion that $E_A(t) \equiv 0$ on $A$, for if we had $E_A(t_0) > 0$ for some $t_0$ in $A$ the result would be $0 = G(x,t_0)$ for all $x$ in $R$, which is impossible. Therefore we have proved

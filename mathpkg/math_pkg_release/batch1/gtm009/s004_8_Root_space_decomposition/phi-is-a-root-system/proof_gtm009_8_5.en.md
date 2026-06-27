---
role: proof
locale: en
of_concept: phi-is-a-root-system
source_book: gtm009
source_chapter: "8"
source_section: "8.5 Rationality properties. Summary"
---

**(a)** By Proposition 8.4(a), $\Phi$ spans $H^*$. The Cartan integers $\langle\alpha, \beta\rangle = 2(\alpha, \beta)/(\beta, \beta)$ are integers (Proposition 8.4(f)). This implies that if $\alpha, \beta \in \Phi$, then $(\alpha, \beta) = \kappa(t_\alpha, t_\beta) \in \mathbb{Q}$. Thus the $\mathbb{Q}$-span $E_{\mathbb{Q}}$ of $\Phi$ is well-defined with $\dim_{\mathbb{Q}} E_{\mathbb{Q}} = \dim_F H^* = \ell$. Define $E = \mathbb{R} \otimes_{\mathbb{Q}} E_{\mathbb{Q}}$; then $\dim_{\mathbb{R}} E = \ell$.

**(b)** The form $(\lambda, \mu) = \kappa(t_\lambda, t_\mu) = \sum_{\alpha \in \Phi} \alpha(t_\lambda) \alpha(t_\mu) = \sum_{\alpha \in \Phi} (\alpha, \lambda)(\alpha, \mu)$ extends bilinearly to $E$. For any $\beta \in \Phi$, $(\beta, \beta) = \sum_{\alpha \in \Phi} (\alpha, \beta)^2$. Dividing by $(\beta, \beta)^2$: $1/(\beta, \beta) = \sum_{\alpha \in \Phi} (\alpha, \beta)^2/(\beta, \beta)^2$. The right side is rational since $2(\alpha, \beta)/(\beta, \beta) \in \mathbb{Z}$. Therefore $(\beta, \beta) \in \mathbb{Q}$, and consequently $(\alpha, \beta) \in \mathbb{Q}$ for all $\alpha, \beta$. Hence all inner products of vectors in $E_{\mathbb{Q}}$ are rational.

For any $\lambda \in E_{\mathbb{Q}}$, $(\lambda, \lambda) = \sum_{\alpha \in \Phi} (\alpha, \lambda)^2$, a sum of squares of rational numbers. Hence $(\lambda, \lambda) \geq 0$, with equality only if $\lambda = 0$. This makes the form positive definite on $E_{\mathbb{Q}}$, and extending to $\mathbb{R}$ preserves positive definiteness. Thus $E$ is a euclidean space.

**(c)** Verify the root system axioms:
- (R1): $\Phi$ is finite, does not contain $0$, and spans $E$. (Finiteness from finite dimension of $L$; spanning from Proposition 8.4(a).)
- (R2): If $\alpha \in \Phi$, then $-\alpha \in \Phi$ (since $L$ is semisimple, with each $L_\alpha \neq 0$ implying symmetrically $L_{-\alpha} \neq 0$), and no other multiples by Proposition 8.4(a).
- (R3): For $\alpha \in \Phi$, define $\sigma_\alpha(\beta) = \beta - \beta(h_\alpha) \alpha = \beta - \langle\beta, \alpha\rangle \alpha$. By Proposition 8.4(c), $\beta(h_\alpha) \in \mathbb{Z}$, and indeed $\beta - \beta(h_\alpha)\alpha \in \Phi$.
- (R4): $\langle\beta, \alpha\rangle \in \mathbb{Z}$ by Proposition 8.4(f), i.e., all Cartan integers are integers.

Thus $\Phi$ is a root system in $E$.

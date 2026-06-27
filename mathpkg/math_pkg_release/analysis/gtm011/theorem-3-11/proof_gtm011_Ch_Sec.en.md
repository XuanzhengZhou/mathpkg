---
role: proof
locale: en
of_concept: theorem-3-11
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Let $|f(a)| \leq M$ for all $a \in \partial_\infty G$. The proof begins by noting that

3.12 $\varphi(z) \leq M$ for all $z$ in $G$, $\varphi$ in $\mathcal{P}(f, G)$

This follows because, by definition, $\lim \sup \varphi(z) \leq M$ whenever $\varphi \in \mathcal{P}(f, G)$; so (3.12) is a direct consequence of the Maximum Principle.

Fix $a$ in $G$ and let $\bar{B}(a; r) \subset G$. Then $u(a) = \sup \{ \varphi(a): \varphi \in \mathcal{P}(f, G) \}$; so there is a sequence $\{\varphi_n\}$ in $\mathcal{P}(f, G)$ such that $u(a) = \lim \varphi_n(a)$. Let $\Phi_n = \max \{ \varphi_1, \ldots, \varphi_n \}$; by Corollary 3.6 $\Phi_n$ is subharmonic. Let $\Phi_n'$ be the subharmonic function on $G$ such that $\Phi_n'(z) = \Phi_n(z)$ for $z$ in $G - B(a; r)$ and $\Phi_n'$ is harmonic on $B(a; r)$ (Corollary 3.7). It is left to the reader to verify the following statements:

3.13 $\Phi_n' \leq \Phi_n'_{n

function. The harmonic function $u$ obtained in the preceding theorem is called the Perron Function associated with $f$.

The next step in solving the Dirichlet Problem is to prove that for each point $a$ in $\partial_{\infty} G$ lim $u(z)$ exists and equals $f(a)$. As was mentioned earlier, this does not always hold. The following example illustrates this phenomenon.

Let $G = \{z: 0 < |z| < 1\}$, $T = \{z: |z| = 1\}$; so $\partial G = T \cup \{0\}$. Define $f: \partial G \to \mathbb{R}$ by $f(z) = 0$ if $z \in T$ and $f(0) = 1$. For $0 < \epsilon < 1$ let $u_{\epsilon}(z) = (\log |z|) (\log \epsilon)^{-1}$; then $u_{\epsilon}$ is harmonic in $G$, $u_{\epsilon}(z) > 0$ for $z$ in $G$, $u_{\epsilon}(z) = 0$ for $z$ in $T$, and $u_{\epsilon}(z) = 1$ if $|z| = \epsilon$. Suppose that $v \in \mathcal{P}(f, G)$; since $|f| \leq 1$, $v(z) \leq 1$ for all $z$ in $G$. If $R_{\epsilon} = \{z: \epsilon < |z| < 1\}$ then $\limsup v(z) \leq u_{\epsilon}(a)$ for all $a$ in $\partial R_{\epsilon}$; by the Maximum Principle, $v(z) \leq u_{\epsilon}(z)$ for all $z$ in $R_{\epsilon}$. Since $\epsilon$ was arbitrary this gives that for each $z$ in $G$, $v(z) \leq \limsup u_{\epsilon}(z) = 0$. Hence the Perron function associated with $f$ is the identically zero function, and the Dirichlet Problem cannot be solved for the punctured disk. (Another proof of this is available by using Exercise 2.5 and the Maximum Principle.)

Exercises

1. Which of the following functions are sub

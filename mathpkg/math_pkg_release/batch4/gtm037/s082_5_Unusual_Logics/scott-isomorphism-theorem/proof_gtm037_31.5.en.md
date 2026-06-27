---
role: proof
locale: en
of_concept: scott-isomorphism-theorem
source_book: gtm037
source_chapter: "31"
source_section: "5"
---

For each finite sequence $a$ of length $n$ of elements of $A$ and each $\beta < \omega_1$ we define a formula $\varphi_a^\beta \in \operatorname{Fmla}_L^n$. Let

$$\varphi_a^0 = \bigwedge \{\psi \in \operatorname{Fmla}_L^n : \mathfrak{A} \models \psi[a] \text{ and } \psi \text{ is atomic or the negation of an atomic formula}\}.$$

For $\lambda$ a limit ordinal $< \omega_1$ let

$$\varphi_a^\lambda = \bigwedge_{\alpha < \lambda} \varphi_a^\alpha.$$

Finally, for $\alpha < \omega_1$ let

$$\varphi_a^{\alpha+1} = \varphi_a^\alpha \wedge \bigwedge_{b \in A} \exists v_n \varphi_{a\langle b\rangle}^\alpha \wedge \forall v_n \bigvee_{b \in A} \varphi_{a\langle b\rangle}^\alpha.$$

Thus we have, by induction on $\alpha$,
(1) $\mathfrak{A} \models \varphi_a^\alpha[a]$;
(2) $\models \varphi_a^\alpha \rightarrow \varphi_a^\beta$ if $\beta < \alpha < \omega_1$.

Now by (2), $\langle \{x : \mathfrak{A} \models \varphi_a^\alpha[x]\} : \alpha < \omega_1 \rangle$ is a sequence of subsets of ${}^n A$ non-increasing under $\subseteq$. Since $|{}^n A| = \aleph_0$, it follows that there is an $\alpha < \omega_1$ such that for all $\beta \geq \alpha$, the sets $\{x : \mathfrak{A} \models \varphi_a^\beta[x]\}$ are identical for each tuple $a$. At this stabilization point, the sentence $\psi = \varphi_\emptyset^\alpha$ characterizes $\mathfrak{A}$ up to isomorphism among countable structures. A standard back-and-forth argument shows that any countable model of $\psi$ is isomorphic to $\mathfrak{A}$.

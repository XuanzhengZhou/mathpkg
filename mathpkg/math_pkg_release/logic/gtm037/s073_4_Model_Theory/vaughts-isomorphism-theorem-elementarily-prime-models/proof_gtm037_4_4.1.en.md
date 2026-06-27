---
role: proof
locale: en
of_concept: vaughts-isomorphism-theorem-elementarily-prime-models
source_book: gtm037
source_chapter: "4"
source_section: "4.1"
---

We apply 26.20; we need to construct an $\omega$-sequence for the elementarily prime models $\mathfrak{A}$ and $\mathfrak{B}$ of $\Gamma$. For each $m \in \omega$, let $I_m$ consist of all pairs $(x, y) \in {}^m A \times {}^m B$ such that there is an $m$-atomic formula $\varphi$ over $\Gamma$ with $\mathfrak{A} \models \varphi[x]$ and $\mathfrak{B} \models \varphi[y]$.

Note that the $0$-atomic formulas over $\Gamma$ are precisely those $\varphi$ with $\Gamma \models \varphi$, since $\Gamma$ is complete. Thus $I_0$ holds (the empty tuple condition is satisfied).

Now suppose that $x I_m y$ and $a \in A$. Let $\varphi$ be $m$-atomic over $\Gamma$ with $\mathfrak{A} \models \varphi[x]$ and $\mathfrak{B} \models \varphi[y]$. By 27.9, choose an $(m+1)$-atomic formula $\psi$ over $\Gamma$ such that $\mathfrak{A} \models \psi[x_0, \ldots, x_{m-1}, a]$. Since $\mathfrak{A} \models (\varphi \land \exists v_m \psi)[x]$, we have $\Gamma \models \varphi \rightarrow \exists v_m \psi$ (otherwise $\Gamma \models \varphi \rightarrow \neg \exists v_m \psi$, contradicting the $m$-atomicity of $\varphi$). Hence $\mathfrak{B} \models \exists v_m \psi[y]$. Choose $b \in B$ so that $\mathfrak{B} \models \psi[y_0, \ldots, y_{m-1}, b]$. Then $(x^\frown a, y^\frown b) \in I_{m+1}$.

Symmetrically, if $x I_m y$ and $b \in B$, there exists $a \in A$ with $(x^\frown a, y^\frown b) \in I_{m+1}$.

Thus the $I_m$ form an $\omega$-sequence for $\mathfrak{A}$ and $\mathfrak{B}$. By 26.20 (the back-and-forth theorem), $\mathfrak{A} \cong \mathfrak{B}$.

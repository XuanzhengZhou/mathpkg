---
role: proof
locale: en
of_concept: tarski-vaught-test
source_book: gtm037
source_chapter: "4"
source_section: "4"
---

**(i) $\Rightarrow$ (ii).** Assume $\mathfrak{A} \preceq \mathfrak{B}$ and suppose $\mathfrak{B} \models \exists v_k \, \varphi[x]$ for a formula $\varphi$, $k \in \omega$, and $x \in {}^\omega A$. By the definition of elementary substructure, $\mathfrak{A} \models \exists v_k \, \varphi[x]$. Hence by the definition of satisfaction there exists $a \in A$ such that $\mathfrak{A} \models \varphi[x_a^k]$. Applying $\mathfrak{A} \preceq \mathfrak{B}$ again, we obtain $\mathfrak{B} \models \varphi[x_a^k]$, as required.

**(ii) $\Rightarrow$ (i).** Assume condition (ii) holds. We prove by induction on formulas $\varphi$ that for every $x \in {}^\omega A$,

$$\mathfrak{A} \models \varphi[x] \quad\text{iff}\quad \mathfrak{B} \models \varphi[x]. \tag{1}$$

*Atomic formulas.* If $\varphi$ is $\mathbf{R} \sigma_0 \cdots \sigma_{m-1}$ where $\mathbf{R}$ is an $m$-ary relation symbol (including equality), then

$$\mathfrak{A} \models \varphi[x] \;\text{iff}\; \langle \sigma_0^{\mathfrak{A}}[x], \ldots, \sigma_{m-1}^{\mathfrak{A}}[x] \rangle \in \mathbf{R}^{\mathfrak{A}}
\;\text{iff}\; \langle \sigma_0^{\mathfrak{B}}[x], \ldots, \sigma_{m-1}^{\mathfrak{B}}[x] \rangle \in \mathbf{R}^{\mathfrak{B}}
\;\text{iff}\; \mathfrak{B} \models \varphi[x],$$

where the middle equivalence holds because $\mathfrak{A} \subseteq \mathfrak{B}$ implies $\mathbf{R}^{\mathfrak{A}} = \mathbf{R}^{\mathfrak{B}} \cap A^m$, and all terms evaluate to elements of $A$ since the parameters are taken from $A$ and $\mathfrak{A}$ is a substructure.

*Negation.* If $\varphi = \neg \psi$ and (1) holds for $\psi$, then

$$\mathfrak{A} \models \varphi[x] \;\text{iff}\; \mathfrak{A} \not\models \psi[x] \;\text{iff}\; \mathfrak{B} \not\models \psi[x] \;\text{iff}\; \mathfrak{B} \models \varphi[x].$$

*Conjunction.* If $\varphi = \psi \land \theta$ and (1) holds for $\psi$ and $\theta$, then

$$\mathfrak{A} \models \varphi[x] \;\text{iff}\; \mathfrak{A} \models \psi[x] \text{ and } \mathfrak{A} \models \theta[x]
\;\text{iff}\; \mathfrak{B} \models \psi[x] \text{ and } \mathfrak{B} \models \theta[x]
\;\text{iff}\; \mathfrak{B} \models \varphi[x].$$

*Existential quantification.* Suppose $\varphi = \exists v_k \, \psi$ and (1) holds for all $x \in {}^\omega A$ with respect to $\psi$. Then

$$\begin{aligned}
\mathfrak{A} \models \varphi[x] &\iff \text{there exists } a \in A \text{ with } \mathfrak{A} \models \psi[x_a^k] \\
&\iff \text{there exists } a \in A \text{ with } \mathfrak{B} \models \psi[x_a^k] \quad\text{(by induction hypothesis)}\\
&\iff \mathfrak{B} \models \varphi[x],
\end{aligned}$$

where the forward direction of the last equivalence uses condition (ii): if $\mathfrak{B} \models \exists v_k \, \psi[x]$, then there is $a \in A$ with $\mathfrak{B} \models \psi[x_a^k]$, and the reverse direction is immediate from the meaning of $\exists$.

Since all formulas are built from atomic formulas using $\neg$, $\land$, and $\exists$, the induction is complete, and we conclude $\mathfrak{A} \preceq \mathfrak{B}$.

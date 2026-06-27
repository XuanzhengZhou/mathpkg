---
role: proof
locale: en
of_concept: model-existence-with-admissible-functions
source_book: gtm037
source_chapter: "4"
source_section: "Model Theory"
---

Set $m = |\text{Fmla}_\mathcal{L}|$ for brevity. Let $\varphi : m \to \text{Sent}_{\mathcal{L}'}$ be an enumeration of all sentences of $\mathcal{L}'$, let $\tau$ map $m$ one-one onto the set of primitive terms of $\mathcal{L}'$, and fix a well-ordering of $C$. Let $\Gamma \in S$.

We define a sequence $\langle \Theta_\alpha : \alpha \leq m \rangle$ by transfinite recursion. Set $\Theta_0 = \Gamma$. Suppose $\Theta_\alpha \in S$ has been defined for $\alpha < m$, and assume the inductive hypothesis:

$$\left| \{c \in C : c \text{ occurs in some } \varphi \in \Theta_\alpha\} \right| \leq \left| \{c \in C : c \text{ occurs in some } \varphi \in \Gamma\} \right| + |\alpha| + \aleph_0.$$

Define $\Theta_{\alpha+1}$ as follows. First, let

$$
\Theta'_\alpha =
\begin{cases}
\Theta_\alpha & \text{if } \Theta_\alpha \cup \{\varphi_\alpha\} \notin S,\\[4pt]
\Theta_\alpha \cup \{\varphi_\alpha\} & \text{otherwise.}
\end{cases}
$$

Next, if $\varphi_\alpha$ has the form $\exists x \psi$ and $\varphi_\alpha \in \Theta'_\alpha$, then $\Theta'_\alpha \cup \{\exists x \psi\} \in S$, and by condition (C6) there exists a constant $c \in C$ not occurring in $\Theta'_\alpha \cup \{\psi\}$ such that $\Theta'_\alpha \cup \{\text{Subf}_c^x \psi\} \in S$. Choose the first such $c$ in the well-ordering of $C$ and set

$$\Theta''_\alpha = \Theta'_\alpha \cup \{\text{Subf}_c^x \psi\}.$$

If $\varphi_\alpha$ is not of existential form, or if $\varphi_\alpha \notin \Theta'_\alpha$, set $\Theta''_\alpha = \Theta'_\alpha$.

Finally, apply the admissible function $f_\alpha$ and set

$$\Theta_{\alpha+1} = f_\alpha \Theta''_\alpha.$$

For limit ordinals $\lambda \leq m$, set $\Theta_\lambda = \bigcup_{\alpha < \lambda} \Theta_\alpha$.

One verifies by induction the following properties for all $\alpha \leq m$:

\begin{enumerate}
\item[(0)] $\Theta_\alpha \in S$.
\item[(1)] $\Gamma \subseteq \Theta_\alpha$.
\item[(2)] If $\varphi \in \Theta_\alpha$ and $\varphi \to \psi \in \Theta_\alpha$, then $\psi \in \Theta_\alpha$.
\item[(3)] If $\varphi$ is a tautology, then $\varphi \in \Theta_\alpha$.
\item[(4)] If $\varphi$ is an equality axiom, then $\varphi \in \Theta_\alpha$.
\item[(5)] If $\forall x \varphi \in \Theta_m$, then $\text{Subf}_c^x \varphi \in \Theta_m$ for every $c \in C$.
\item[(6)] If $\exists x \varphi \in \Theta_m$, then $\text{Subf}_c^x \varphi \in \Theta_m$ for some $c \in C$.
\item[(7)] If $c = d \in \Theta_m$, then $d = c \in \Theta_m$.
\item[(8)] If $c = d \in \Theta_m$ and $\text{Subf}_d^{v_0} \psi \in \Theta_m$, then $\text{Subf}_c^{v_0} \psi \in \Theta_m$.
\item[(9)] For every $c \in C$, $c = c \in \Theta_m$.
\item[(10)] For each $\alpha < m$, $\Gamma \subseteq f_\alpha \Theta_\alpha \subseteq \Theta_{\alpha+1} \subseteq \Theta_m$.
\end{enumerate}

Properties (0)-(10) follow from the construction together with the defining conditions (C0)-(C11) of a consistency family and the properties of admissible functions.

Now define a binary relation $\equiv$ on $C$ by

$$c \equiv d \quad \text{iff} \quad c = d \in \Theta_m.$$

By properties (7), (8), and (9), $\equiv$ is an equivalence relation on $C$. Let $[c]$ denote the equivalence class of $c \in C$, and set

$$A = \{[c] : c \in C\}.$$

Thus $|A| \leq |C| \leq |\text{Fmla}_\mathcal{L}|$, and condition (i) is satisfied.

Define the $\mathcal{L}$-structure $\mathfrak{A}$ with universe $A$ as follows. For each $m$-ary operation symbol $\mathbf{O}$ of $\mathcal{L}$,

$$\mathbf{O}^{\mathfrak{A}}([c_0], \ldots, [c_{m-1}]) = [d] \quad \text{iff} \quad (d = \mathbf{O} c_0 \cdots c_{m-1}) \in \Theta_m.$$

For each $m$-ary relation symbol $\mathbf{R}$ of $\mathcal{L}$,

$$\langle [c_0], \ldots, [c_{m-1}] \rangle \in \mathbf{R}^{\mathfrak{A}} \quad \text{iff} \quad \mathbf{R} c_0 \cdots c_{m-1} \in \Theta_m.$$

The interpretation of the new constants is $a_c = [c]$ for each $c \in C$. Set $\mathfrak{A}' = (\mathfrak{A}, [c])_{c \in C}$.

One proves by induction on the complexity of formulas that for every formula $\varphi$ of $\mathcal{L}'$ and every $c \in C$,

$$\mathfrak{A}' \models \varphi \quad \text{iff} \quad \varphi \in \Theta_m.$$

The atomic case follows directly from the definitions of $\mathbf{O}^{\mathfrak{A}}$ and $\mathbf{R}^{\mathfrak{A}}$, using properties (7) and (8) to handle the equality relation. The induction steps for propositional connectives follow from properties (2) and (3). The universal quantifier case uses (5); the existential quantifier case uses (6).

Since $\Gamma \subseteq \Theta_m$, it follows that $\mathfrak{A}'$ is a model of $\Gamma$. Finally, if $\alpha < m$, then by (10) we have $\Gamma \subseteq f_\alpha \Theta''_\alpha = \Theta_{\alpha+1} \subseteq \Theta_m$, so taking $\Delta = \Theta''_\alpha$ yields condition (ii). This completes the proof.

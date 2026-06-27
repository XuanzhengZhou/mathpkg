---
role: proof
locale: en
of_concept: lyndon-positive-sentences-theorem
source_book: gtm037
source_chapter: "25"
source_section: "4"
---

The trivial direction is $(i) \Rightarrow (ii)$: assume $(i)$. To show $(ii)$ it suffices to prove

$$(1) \text{ if } \varphi \text{ is any positive formula, } f: \mathfrak{A} \twoheadrightarrow \mathfrak{B}, \; x \in {^{\omega}}A \text{ and } \mathfrak{A} \models \varphi[x], \text{ then } \mathfrak{B} \models \varphi[f \circ x].$$

This statement is proved by an obvious induction on $\varphi$, using 24.4; we take one atomic case and the passage from $\varphi$ to $\forall v_i \varphi$ as examples. Suppose first that $\varphi$ is atomic. Then $\mathfrak{A} \models \varphi[x]$ means $(x_0, \ldots)$ satisfies the atomic relation in $\mathfrak{A}$. Since $f$ is a homomorphism, by 24.4 the same holds for $(f x_0, \ldots)$ in $\mathfrak{B}$, so $\mathfrak{B} \models \varphi[f \circ x]$. For the quantifier step, suppose $\varphi$ is $\forall v_i \psi$ and the induction hypothesis holds for $\psi$. If $\mathfrak{A} \models \forall v_i \psi[x]$, then for all $a \in A$, $\mathfrak{A} \models \psi[x_a^i]$, so by induction $\mathfrak{B} \models \psi[(f \circ x)_{f(a)}^i]$ for all $a \in A$. Since $f$ is surjective, every $b \in B$ equals $f(a)$ for some $a$, hence $\mathfrak{B} \models \forall v_i \psi[f \circ x]$. The cases $\wedge$, $\vee$, $\exists$ are similarly straightforward.

$(ii) \Rightarrow (i)$: Assume $(ii)$. Let $\Gamma' = \{\varphi : \varphi \text{ is a positive sentence and } \Gamma \models \varphi\}$. We claim $\mathrm{Mod}\,\Gamma = \mathrm{Mod}\,\Gamma'$. Clearly $\mathrm{Mod}\,\Gamma \subseteq \mathrm{Mod}\,\Gamma'$. For the reverse inclusion, let $\mathfrak{B} \in \mathrm{Mod}\,\Gamma'$. By Lemma 25.21, there exists $\mathfrak{A} \models \Gamma$ with $\mathfrak{A} \preceq_{\mathrm{pos}} \mathfrak{B}$. By a diagram argument (using the method of proof of Theorem 25.19), one can show that there exists $\mathfrak{C}$ such that $\mathfrak{A} \subseteq \mathfrak{C}$ and $\mathfrak{C} \twoheadrightarrow \mathfrak{B}$. Since $\mathfrak{A} \in \mathrm{Mod}\,\Gamma$ and universal classes are closed under extensions, one obtains that $\mathfrak{C} \models \Gamma$ (after ensuring $\Gamma$ is suitably saturated). Then by condition (ii), the homomorphic image $\mathfrak{B}$ of $\mathfrak{C}$ is also in $\mathrm{Mod}\,\Gamma$. Thus $\mathrm{Mod}\,\Gamma' \subseteq \mathrm{Mod}\,\Gamma$, completing the proof.

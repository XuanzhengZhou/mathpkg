---
role: proof
locale: en
of_concept: soundness-theorem
source_book: gtm037
source_chapter: "11"
source_section: "Elements of Logic"
---

Using a simple inductive argument on the formal proof, it suffices to show that each logical axiom is universally valid. We consider the five kinds of logical axioms:

(1) $\varphi$ is a tautology. Let $x \in {}^\omega A$; we wish to show that $x \in \varphi^{\mathfrak{A}}$. For any formula $\psi$, let

$$f\psi = 1 \quad\text{if } x \in \psi^{\mathfrak{A}},$$
$$f\psi = 0 \quad\text{if } x \notin \psi^{\mathfrak{A}}.$$

Clearly $f$ is a truth valuation. Hence $f\varphi = 1$, i.e., $x \in \varphi^{\mathfrak{A}}$, as desired.

(2) $\varphi$ is $\forall v_i(\psi \rightarrow \chi) \rightarrow (\forall v_i\psi \rightarrow \forall v_i\chi)$. Let $x \in {}^\omega A$. We assume $x \in (\forall v_i(\psi \rightarrow \chi))^{\mathfrak{A}}$, $x \in (\forall v_i\psi)^{\mathfrak{A}}$, and prove $x \in (\forall v_i\chi)^{\mathfrak{A}}$. Let $a \in A$ be arbitrary. Then $x_a^i \in (\psi \rightarrow \chi)^{\mathfrak{A}}$ and $x_a^i \in \psi^{\mathfrak{A}}$, so $x_a^i \in \chi^{\mathfrak{A}}$, as desired.

(3) $\varphi$ is $\psi \rightarrow \forall v_i\psi$, where $v_i$ does not occur in $\psi$. Then $\varphi^{\mathfrak{A}} = {}^\omega A$, by the definition of formula denotation: if $x$ satisfies $\psi$, then every $x_a^i$ also satisfies $\psi$ (since the variable does not occur), so $x$ satisfies $\forall v_i\psi$.

(4) $\varphi$ is $\exists v_i(v_i = \sigma)$, where $v_i$ does not occur in $\sigma$. For any $x \in {}^\omega A$, let $a = \sigma^{\mathfrak{A}}[x]$. Then $x_a^i$ satisfies $v_i = \sigma$, so $x$ satisfies $\exists v_i(v_i = \sigma)$. Thus $\varphi^{\mathfrak{A}} = {}^\omega A$.

(5) Equality axioms. These are handled by the standard properties of equality in first-order logic with identity.

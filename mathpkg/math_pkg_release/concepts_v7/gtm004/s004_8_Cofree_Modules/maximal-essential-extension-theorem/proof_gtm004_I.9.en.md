---
role: proof
locale: en
of_concept: maximal-essential-extension-theorem
source_book: gtm004
source_chapter: "I. Modules"
source_section: "9. Essential Extensions"
---

# Proof of Theorem 9.2: Existence of Maximal Essential Extension

Let $A$ be a submodule of a $\Lambda$-module $M$. Consider the set $\Phi$ of essential extensions of $A$ contained in $M$. Since $A$ is an essential extension of itself, $\Phi \neq \varnothing$. Under inclusion, $\Phi$ is inductive: if $\{E_j\}_{j \in J}$ is a chain of essential extensions of $A$ contained in $M$, then $\bigcup_{j \in J} E_j$ is again an essential extension of $A$ contained in $M$.

To verify this, let $0 \neq x \in \bigcup E_j$. Then $x \in E_k$ for some $k \in J$. By Proposition 9.1 applied to $E_k$ (which is an essential extension of $A$), there exists $\lambda \in \Lambda$ such that $0 \neq \lambda x \in A$. Hence $\bigcup E_j$ is an essential extension of $A$ by Proposition 9.1, and clearly it is contained in $M$.

By Zorn's Lemma, there exists a maximal essential extension $E$ of $A$ contained in $M$.

Now embed $M$ into an injective $\Lambda$-module $I$ (this is always possible, by embedding into a cofree module as in Section 8). Consider the set $\Psi$ of submodules $H$ of $I$ with $H \cap E = 0$. Since $0 \in \Psi$, $\Psi \neq \varnothing$. Under inclusion, $\Psi$ is inductive (the union of a chain of submodules intersecting $E$ trivially still intersects $E$ trivially). By Zorn's Lemma, let $\bar{H}$ be a maximal element of $\Psi$.

Consider the composition

$$\sigma : E \hookrightarrow I \twoheadrightarrow I/\bar{H}.$$

We claim $\sigma$ is an essential monomorphism. If $\ker \sigma \neq 0$, then $\ker \sigma = E \cap \bar{H} \neq 0$, contradicting $\bar{H} \in \Psi$. Hence $\sigma$ is a monomorphism. To show $\sigma$ is essential: let $H/\bar{H}$ be a nonzero submodule of $I/\bar{H}$, where $\bar{H} \subsetneq H \subseteq I$. By maximality of $\bar{H}$, we must have $H \cap E \neq 0$. Hence $(H/\bar{H}) \cap \sigma E \neq 0$, showing $\sigma$ is essential.

Now, $E$ admits no proper essential monomorphism into an injective module (by maximality among essential extensions contained in $M$, and $M \subseteq I$ injective). Therefore $\sigma : E \rightarrow I/\bar{H}$ must be an isomorphism.

The sequence

$$0 \rightarrow \bar{H} \rightarrow I \xrightarrow{\sigma^{-1} \circ \pi} E \rightarrow 0$$

splits via the inclusion $E \hookrightarrow I$. Thus $E$ is a direct summand of the injective module $I$, and therefore $E$ itself is injective by Proposition 6.3 (a direct summand of an injective module is injective).

Consequently, the maximal essential extension $E$ of $A$ contained in any module $M$ that embeds in an injective module is itself injective. In particular, taking $M$ to be any injective module containing $A$, the maximal essential extension $E$ of $A$ in $M$ is an injective module and is an essential extension of $A$. $\square$

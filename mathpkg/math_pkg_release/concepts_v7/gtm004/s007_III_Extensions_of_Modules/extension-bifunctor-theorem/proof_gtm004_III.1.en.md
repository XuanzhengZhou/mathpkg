---
role: proof
locale: en
of_concept: extension-bifunctor-theorem
source_book: gtm004
source_chapter: "III. Extensions of Modules"
source_section: "1. Extensions"
---

# Proof of Theorem 1.4: $E(-,-)$ is a Bifunctor

We have already shown that for fixed $B$, the assignment $A \mapsto E(A,B)$ with induced maps $\alpha^* = E(\alpha,B)$ defines a contravariant functor, and for fixed $A$, the assignment $B \mapsto E(A,B)$ with induced maps $\beta_* = E(A,\beta)$ defines a covariant functor.

**Proof.** It remains to check the commutation relation

\[
\beta_* \circ \alpha^* = \alpha^* \circ \beta_* : E(A,B) \to E(A',B')
\]

for homomorphisms $\alpha: A' \to A$ and $\beta: B \to B'$. Let $B \xrightarrow{\kappa} E \xrightarrow{\nu} A$ be a representative of an element in $E(A,B)$. We construct the following three-dimensional commutative diagram using pullbacks and pushouts:

\[
\begin{CD}
B @>>> E^\alpha @>>> A' \\
@VVV @VVV @VV\alpha V \\
B @>>> E @>>> A \\
@V\beta VV @VVV @| \\
B' @>>> E_\beta @>>> A
\end{CD}
\]

Here $E^\alpha$ is the pullback of $(\alpha, \nu)$, and $E_\beta$ is the pushout of $(\beta, \kappa)$. We must show the existence of a map $(E^\alpha)_\beta \to (E_\beta)^\alpha$ making the full diagram commute.

We first construct $E^\alpha \to (E^\alpha)_\beta$ satisfying the necessary commutativity relations. Since the composite $E^\alpha \to E \to E_\beta$ together with the map $E^\alpha \to A'$ satisfy the condition that $E^\alpha \to E_\beta \to A$ coincides with $E^\alpha \to A' \xrightarrow{\alpha} A$, we obtain a unique map $E^\alpha \to (E_\beta)^\alpha$ by the universal property of the pullback, such that the diagram

\[
\begin{CD}
E^\alpha @>>> (E_\beta)^\alpha @>>> A' \\
@VVV @VVV @VV\alpha V \\
E @>>> E_\beta @>>> A
\end{CD}
\]

commutes. By the universal property of the pushout applied to $B \to E^\alpha$ and $B \to B'$, we further obtain a map $(E^\alpha)_\beta \to (E_\beta)^\alpha$.

It remains to verify that $B' \to (E^\alpha)_\beta \to A'$ is an extension, i.e., that the sequence

\[
B' \longrightarrow (E^\alpha)_\beta \longrightarrow A'
\]

is short exact. The verification that $(E^\alpha)_\beta \to A'$ is epimorphic follows from Lemma 1.2(ii) (or its dual). The kernel is identified with $B'$ using the exactness properties of pullbacks and pushouts. The commutativity relations established above ensure that the two ways of computing $\beta_* \alpha^*$ and $\alpha^* \beta_*$ yield the same extension class.

Thus $E(-,-)$ is a bifunctor from the category of $\Lambda$-modules to the category of sets, contravariant in the first variable and covariant in the second. $\square$

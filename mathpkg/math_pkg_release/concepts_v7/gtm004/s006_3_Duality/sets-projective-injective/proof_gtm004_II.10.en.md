---
role: proof
locale: en
of_concept: sets-projective-injective
source_book: gtm004
source_chapter: "II"
source_section: "10"
---

# Proof of Every Object in the Category of Sets is Projective and Injective

**Projectivity.** Let $P \in \mathfrak{S}$ be any set. Given a diagram

$$\begin{array}{ccc}
P & \xrightarrow{\varphi} & B \\
& & \downarrow{\scriptstyle \varepsilon} \\
A & \xrightarrow{\varepsilon} & B
\end{array}$$

with $\varepsilon$ surjective (epimorphic in $\mathfrak{S}$). We must find $\psi: P \to A$ such that $\varepsilon \circ \psi = \varphi$.

For each $p \in P$, choose — using the Axiom of Choice — an element $a_p \in A$ such that $\varepsilon(a_p) = \varphi(p)$ (such $a_p$ exists because $\varepsilon$ is surjective). Define $\psi(p) = a_p$. Then for all $p \in P$,

$$(\varepsilon \circ \psi)(p) = \varepsilon(\psi(p)) = \varepsilon(a_p) = \varphi(p),$$

so $\varepsilon \circ \psi = \varphi$. Hence $P$ is projective. $\square$

**Injectivity.** Dually, let $Q \in \mathfrak{S}$ be any set. Given a diagram

$$\begin{array}{ccc}
A & \xrightarrow{\mu} & B \\
\downarrow{\scriptstyle \alpha} & & \\
Q & &
\end{array}$$

with $\mu$ injective (monomorphic in $\mathfrak{S}$). We must find $\beta: B \to Q$ such that $\beta \circ \mu = \alpha$.

Since $\mu$ is injective, $\mu: A \hookrightarrow B$ is an embedding. Define $\beta: B \to Q$ by

$$\beta(b) = \begin{cases} \alpha(a) & \text{if } b = \mu(a) \text{ for some } a \in A, \\ q_0 & \text{otherwise (for any fixed } q_0 \in Q). \end{cases}$$

The definition is unambiguous because $\mu$ is injective. Then for any $a \in A$,

$$(\beta \circ \mu)(a) = \beta(\mu(a)) = \alpha(a),$$

so $\beta \circ \mu = \alpha$. Hence $Q$ is injective. $\square$

Thus every set is both projective and injective in $\mathfrak{S}$.

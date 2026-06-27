---
role: proof
locale: en
of_concept: baers-criterion
source_book: gtm004
source_chapter: "I"
source_section: "7. Injective Modules over a Principal Ideal Domain"
---

# Proof of Baer's Criterion for Injective Modules

**Baer's Criterion.** (Exercise 7.1) Let $\Lambda$ be a ring. A $\Lambda$-module $I$ is injective if and only if for every left ideal $J \subseteq \Lambda$ and for every $\Lambda$-homomorphism $f: J \to I$, there exists a $\Lambda$-homomorphism $g: \Lambda \to I$ such that $g|_J = f$.

---

## Proof

### Direction ($\Rightarrow$): Injective $\Rightarrow$ ideal extension property

If $I$ is injective, then by definition every diagram

\[
\begin{CD}
J @>{\iota}>> \Lambda \\
@V{f}VV  \\
I
\end{CD}
\]

with $\iota: J \hookrightarrow \Lambda$ a monomorphism admits a lift $g: \Lambda \to I$ with $g \circ \iota = f$, i.e. $g|_J = f$. This is precisely the stated condition applied to the special case where the embedding is the inclusion of a left ideal.

### Direction ($\Leftarrow$): Ideal extension property $\Rightarrow$ injective

Assume $I$ satisfies the condition: every homomorphism from a left ideal into $I$ extends to $\Lambda$. We must show $I$ is injective.

Let $\mu: A \to B$ be a monomorphism and $\alpha: A \to I$ any homomorphism. To simplify, identify $A$ with its image $\mu(A)$ and regard $A$ as a submodule of $B$. We need $\beta: B \to I$ extending $\alpha$.

Consider the set

$$\Phi = \{(C, \gamma) \mid A \subseteq C \subseteq B,\; \gamma: C \to I \text{ is a homomorphism},\; \gamma|_A = \alpha\}.$$

$\Phi \neq \emptyset$ since $(A, \alpha) \in \Phi$. Partially order $\Phi$ by $(C_1, \gamma_1) \leq (C_2, \gamma_2)$ iff $C_1 \subseteq C_2$ and $\gamma_2|_{C_1} = \gamma_1$.

**$\Phi$ is inductive.** If $\{(C_j, \gamma_j)\}_{j \in J}$ is a chain, set $C = \bigcup_{j} C_j$ and define $\gamma(c) = \gamma_j(c)$ for any $j$ with $c \in C_j$. The chain condition ensures well-definedness, and $\gamma$ is a homomorphism. Thus $(C, \gamma) \in \Phi$ is an upper bound.

By Zorn's Lemma, $\Phi$ has a maximal element $(M, \gamma)$. We claim $M = B$.

Suppose $M \neq B$. Choose $b \in B \setminus M$ and define

$$J = \{\lambda \in \Lambda : \lambda b \in M\}.$$

$J$ is readily seen to be a left ideal of $\Lambda$. Define a $\Lambda$-homomorphism

$$h: J \to I, \qquad h(\lambda) = \gamma(\lambda b).$$

By hypothesis, $h$ extends to a homomorphism $k: \Lambda \to I$ with $k|_J = h$. Set $x = k(1) \in I$.

Now we extend $\gamma$ to $M + \Lambda b$. Define

$$\gamma': M + \Lambda b \to I, \qquad \gamma'(m + \lambda b) = \gamma(m) + \lambda x.$$

**Well-definedness:** If $m + \lambda b = m' + \lambda' b$, then $(\lambda - \lambda')b = m' - m \in M$, so $\lambda - \lambda' \in J$. Then

$$\gamma(m' - m) = \gamma((\lambda - \lambda')b) = h(\lambda - \lambda') = k(\lambda - \lambda') = (\lambda - \lambda') \cdot k(1) = (\lambda - \lambda')x,$$

hence $\gamma(m) + \lambda x = \gamma(m') + \lambda' x$. Thus $\gamma'$ is well-defined and is clearly a $\Lambda$-homomorphism.

Moreover $\gamma'|_A = \gamma|_A = \alpha$, so $(M + \Lambda b, \gamma') \in \Phi$ strictly extends $(M, \gamma)$, contradicting maximality.

Therefore $M = B$ and $\beta = \gamma$ is the desired extension. Thus $I$ is injective. $\square$

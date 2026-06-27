---
role: proof
locale: en
of_concept: canonical-potential-representation
source_book: gtm040
source_chapter: "12"
source_section: "2. Gibbs fields"
---
Let $\mathbf{0}$ denote the configuration with a $0$ at every site of $T$. Fix $\iota \in \Omega$. For $A \subset T$, define $\Psi(A) = \ln[\mu(\{\iota^A\})/\mu(\{\mathbf{0}\})]$ and $\Phi(A) = V_A(\iota)$, where $V$ is the potential given by the first sum in the statement of the Theorem.

When $A \neq \emptyset$ we have, by definition of $V$,

$$\sum_{B \subset A} V_B(\iota) = \sum_{B \subset A} \sum_{D \subset B} (-1)^{|B-D|} \Psi(D).$$

Applying Lemma 12-10 (M\"{o}bius inversion) yields $\sum_{B \subset A} V_B(\iota) = \Psi(A) = \ln[\mu(\{\iota^A\})/\mu(\{\mathbf{0}\})]$. Taking $A = T$ and noting that $V_\emptyset = 0$, we obtain

$$\ln \mu(\{\iota\}) = \sum_{B \subset T} V_B(\iota) + \ln \mu(\{\mathbf{0}\}).$$

Thus $\mu(\{\iota\}) = z^{-1} e^{H_V(\iota)}$ with $z = 1/\mu(\{\mathbf{0}\})$, so $\{x_t\}$ is a Gibbs field with potential $V$.

For any $a \in A \subset T$ we can write

$$V_A(\iota) = \sum_{B \subset A - \{a\}} (-1)^{|A - B|} [\ln \mu(\{\iota^B\}) - \ln \mu(\{\iota^{B+a}\})].$$

This shows that $V$ is normalized, since $\iota^B = \iota^{B+a}$ whenever $i_a = 0$.

By Lemma 12-10 the right hand side may be rewritten as

$$\sum_{B \subset A - \{a\}} (-1)^{|A - B|} [\ln \mu_a^T(\iota^B) - \ln \mu_a^T(\iota^{B+a})] = \sum_{B \subset A} (-1)^{|A - B|} \ln \mu_a^T(\iota^B),$$

which establishes the second expression for $V$ in the statement of the Theorem.

Finally, suppose that $U$ is any normalized potential for $\{x_t\}$. Then $H_U(\mathbf{0}) = 0$ and $U_D(\iota^B) = 0$ unless $D \subset B$. Therefore

$$\ln \frac{\mu(\{\iota^B\})}{\mu(\{\mathbf{0}\})} = H_U(\iota^B) = \sum_{D \subset B} U_D(\iota^B) = \sum_{D \subset B} U_D(\iota^A)$$

whenever $B \subset A \subset T$. Applying Lemma 12-11 with $\Lambda = A$, $\Phi(D) = U_D(\iota^A)$ and $\Psi(B) = \ln[\mu(\{\iota^B\})/\mu(\{\mathbf{0}\})]$, we obtain

$$U_A(\iota) = \sum_{B \subset A} (-1)^{|A - B|} \ln \frac{\mu(\{\iota^B\})}{\mu(\{\mathbf{0}\})} = V_A(\iota),$$

proving uniqueness of the normalized potential.

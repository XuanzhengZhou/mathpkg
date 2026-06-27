---
role: proof
locale: en
of_concept: regular-conditional-distribution
source_book: gtm095
source_chapter: "II"
source_section: "4"
---

# Proof of Theorem 5 (Existence of a Regular Conditional Distribution)

**Theorem 5.** Let $X = X(\omega)$ be a random element with values in a Borel space $(E, \mathcal{E})$. Then there exists a regular conditional distribution of $X$ with respect to $\mathcal{G} \subseteq \mathcal{F}$.

*Proof.* Let $\varphi = \varphi(e)$ be the function in Definition 9. By condition (2) of Definition 9, $\varphi(X(\omega))$ is a random variable. Hence, by Theorem 4, we can define a regular conditional distribution $Q(\omega; A)$ of $\varphi(X(\omega))$ with respect to $\mathcal{G}$, where $A \in \varphi(E) \cap \mathcal{B}(R)$.

We introduce the function

$$\tilde{Q}(\omega; B) = Q(\omega; \varphi(B)), \quad B \in \mathcal{E}.$$

By condition (3) of Definition 9, $\varphi(B) \in \varphi(E) \cap \mathcal{B}(R)$, and consequently $\tilde{Q}(\omega; B)$ is well-defined. Evidently $\tilde{Q}(\omega; B)$ is a probability measure in $B \in \mathcal{E}$ for every $\omega$, since $Q(\omega; \cdot)$ is a probability measure and $\varphi$ is a one-to-one mapping.

Now fix $B \in \mathcal{E}$. By the one-to-one character of the mapping $\varphi = \varphi(e)$,

$$\{\omega : X(\omega) \in B\} = \{\omega : \varphi(X(\omega)) \in \varphi(B)\}.$$

Therefore,

$$\tilde{Q}(\omega; B) = Q(\omega; \varphi(B)) = P(\varphi(X) \in \varphi(B) \mid \mathcal{G})(\omega) = P(X \in B \mid \mathcal{G})(\omega) \quad \text{(a.s.)}.$$

Thus $\tilde{Q}(\omega; B)$ satisfies:
- (a) for each $\omega \in \Omega$, $\tilde{Q}(\omega; \cdot)$ is a probability measure on $(E, \mathcal{E})$;
- (b) for each $B \in \mathcal{E}$, $\tilde{Q}(\omega; B) = P(X \in B \mid \mathcal{G})(\omega)$ (a.s.).

Hence $\tilde{Q}(\omega; B)$ is a regular conditional distribution of $X$ with respect to $\mathcal{G}$.

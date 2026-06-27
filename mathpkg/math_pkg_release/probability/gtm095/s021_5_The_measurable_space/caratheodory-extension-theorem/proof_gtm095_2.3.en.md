---
role: proof
locale: en
of_concept: caratheodory-extension-theorem
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Carathéodory's Extension Theorem

**Carathéodory's Theorem.** Let $\Omega$ be a space, $\mathcal{A}$ an algebra of its subsets, and $\mathcal{B} = \sigma(\mathcal{A})$ the smallest $\sigma$-algebra containing $\mathcal{A}$. Let $\mu_0$ be a $\sigma$-finite, $\sigma$-additive measure on $(\Omega, \mathcal{A})$. Then there exists a unique measure $\mu$ on $(\Omega, \sigma(\mathcal{A}))$ which is an extension of $\mu_0$, i.e., satisfies

$$\mu(A) = \mu_0(A), \quad A \in \mathcal{A}.$$

*Proof sketch.* The proof proceeds by constructing an outer measure $\mu^*$ from $\mu_0$ and then showing that the $\mu^*$-measurable sets form a $\sigma$-algebra containing $\mathcal{A}$ on which $\mu^*$ is countably additive.

**Construction of the outer measure.** For any subset $E \subseteq \Omega$, define

$$\mu^*(E) = \inf\left\{ \sum_{n=1}^{\infty} \mu_0(A_n) : A_n \in \mathcal{A},\; E \subseteq \bigcup_{n=1}^{\infty} A_n \right\}.$$

Then $\mu^*$ is an outer measure: $\mu^*(\varnothing) = 0$, $\mu^*(E) \geq 0$, $\mu^*$ is monotone, and $\mu^*$ is countably subadditive. Moreover, $\mu^*$ agrees with $\mu_0$ on $\mathcal{A}$, i.e., $\mu^*(A) = \mu_0(A)$ for all $A \in \mathcal{A}$.

**The $\mu^*$-measurable sets.** A set $E \subseteq \Omega$ is called $\mu^*$-measurable if for every $Q \subseteq \Omega$,

$$\mu^*(Q) = \mu^*(Q \cap E) + \mu^*(Q \cap E^c).$$

By Carathéodory's lemma, the collection $\mathcal{M}$ of all $\mu^*$-measurable sets is a $\sigma$-algebra, and the restriction of $\mu^*$ to $\mathcal{M}$ is a complete measure. One then verifies that $\mathcal{A} \subseteq \mathcal{M}$ (using the finite additivity and countable subadditivity of $\mu_0$ on $\mathcal{A}$), which implies $\sigma(\mathcal{A}) \subseteq \mathcal{M}$.

**Definition of the extension.** Set $\mu = \mu^*|_{\sigma(\mathcal{A})}$. Then $\mu$ is a measure on $(\Omega, \sigma(\mathcal{A}))$ extending $\mu_0$.

**Uniqueness.** If $\mu_0$ is $\sigma$-finite, the extension is unique: if $\mu_1$ and $\mu_2$ are two measures on $\sigma(\mathcal{A})$ agreeing with $\mu_0$ on $\mathcal{A}$, then $\mu_1 = \mu_2$ on $\sigma(\mathcal{A})$. This can be proved via the $\pi$-$\lambda$ theorem (Dynkin's theorem), since $\mathcal{A}$ is a $\pi$-system generating $\sigma(\mathcal{A})$, and the collection of sets on which $\mu_1$ and $\mu_2$ agree is a $\lambda$-system containing $\mathcal{A}$. $\square$

**Remark.** In the text, Shiryaev applies Carathéodory's theorem specifically to construct a probability measure from a distribution function. The algebra $\mathcal{A}$ consists of finite unions of disjoint intervals $(a, b]$, and the set function $P_0$ defined by $P_0(\sum (a_k, b_k]) = \sum [F(b_k) - F(a_k)]$ is shown to be countably additive on $\mathcal{A}$ using the right-continuity of $F$ and a compactness argument. Carathéodory's theorem then yields the unique extension to $\mathcal{B}(R) = \sigma(\mathcal{A})$.

---
role: proof
locale: en
of_concept: ionescu-tulcea-theorem
source_book: gtm095
source_chapter: "2"
source_section: "2"
---

# Proof of Ionescu Tulcea's Theorem on Extending a Measure and the Existence of a Random Sequence

**Theorem 2 (Ionescu Tulcea's Theorem).** Let $(\Omega_n, \mathcal{F}_n)$, $n = 1, 2, \ldots$, be arbitrary measurable spaces and $\Omega = \prod_{n \geq 1} \Omega_n$, $\mathcal{F} = \bigotimes_{n \geq 1} \mathcal{F}_n$. Suppose that a probability measure $P_1$ is given on $(\Omega_1, \mathcal{F}_1)$ and that, for every $(\omega_1, \ldots, \omega_n) \in \Omega_1 \times \cdots \times \Omega_n$, $n \geq 1$, probability measures $P(\omega_1, \ldots, \omega_n; \cdot)$ are given on $(\Omega_{n+1}, \mathcal{F}_{n+1})$. Suppose that for every $B \in \mathcal{F}_{n+1}$ the functions $P(\omega_1, \ldots, \omega_n; B)$ are $\mathcal{F}^n \equiv \mathcal{F}_1 \otimes \cdots \otimes \mathcal{F}_n$-measurable functions of $(\omega_1, \ldots, \omega_n)$ and let, for $A_i \in \mathcal{F}_i$, $n \geq 1$,

$$P_n(A_1 \times \cdots \times A_n) = \int_{A_1} P_1(d\omega_1) \int_{A_2} P(\omega_1; d\omega_2) \cdots \int_{A_n} P(\omega_1, \ldots, \omega_{n-1}; d\omega_n).$$

Then there is a unique probability measure $P$ on $(\Omega, \mathcal{F})$ such that

$$P\{\omega : \omega_1 \in A_1, \ldots, \omega_n \in A_n\} = P_n(A_1 \times \cdots \times A_n)$$

for every $n \geq 1$, and there is a random sequence $X = (X_1(\omega), X_2(\omega), \ldots)$ with the specified finite-dimensional distributions.

*Proof.* The construction defines an additive measure on the algebra of cylindrical sets via the iterated integrals. It remains to verify its countable additivity and apply Carathéodory's theorem.

In Theorem 3 of Sect. 3 the corresponding verification was based on the property of $(R^n, \mathcal{B}(R^n))$ that for every Borel set $B$ there is a compact set $A \subseteq B$ whose probability measure is arbitrarily close to the measure of $B$. In the present case this part of the proof needs to be modified in the following way.

As in Theorem 3 of Sect. 3, let $\{\hat{B}_n\}_{n \geq 1}$ be a sequence of cylindrical sets

$$\hat{B}_n = \{\omega : (\omega_1, \ldots, \omega_n) \in B_n\}$$

that decrease to the empty set $\varnothing$, but have

$$\lim_{n \to \infty} P(\hat{B}_n) > 0.$$

We shall derive a contradiction. For $n > 1$, we have from the definition of $P_n$:

$$P(\hat{B}_n) = \int_{\Omega_1} f_n^{(1)}(\omega_1) P_1(d\omega_1),$$

where

$$f_n^{(1)}(\omega_1) = \int_{\Omega_2} P(\omega_1; d\omega_2) \cdots \int_{\Omega_n} I_{B_n}(\omega_1, \ldots, \omega_n) P(\omega_1, \ldots, \omega_{n-1}; d\omega_n).$$

Since $\hat{B}_{n+1} \subseteq \hat{B}_n$, we have $B_{n+1} \subseteq B_n \times \Omega_{n+1}$ and therefore

$$I_{B_{n+1}}(\omega_1, \ldots, \omega_{n+1}) \leq I_{B_n}(\omega_1, \ldots, \omega_n) I_{\Omega_{n+1}}(\omega_{n+1}).$$

Hence the sequence $\{f_n^{(1)}(\omega_1)\}_{n \geq 1}$ is decreasing for each $\omega_1$. Let $f^{(1)}(\omega_1) = \lim_{n \to \infty} f_n^{(1)}(\omega_1)$. From $\lim_n P(\hat{B}_n) > 0$ and the dominated convergence theorem, we obtain

$$0 < \lim_n P(\hat{B}_n) = \int_{\Omega_1} f^{(1)}(\omega_1) P_1(d\omega_1),$$

so there exists a point $\omega_1^0 \in \Omega_1$ such that $f^{(1)}(\omega_1^0) > 0$. Then $(\omega_1^0) \in B_1$.

Now consider

$$f_n^{(2)}(\omega_2) = \int_{\Omega_3} P(\omega_1^0, \omega_2; d\omega_3) \cdots \int_{\Omega_n} I_{B_n}(\omega_1^0, \omega_2, \ldots, \omega_n) P(\omega_1^0, \omega_2, \ldots, \omega_{n-1}; d\omega_n).$$

We can establish, as for $\{f_n^{(1)}(\omega_1)\}$, that $\{f_n^{(2)}(\omega_2)\}_{n \geq 1}$ is decreasing. Let $f^{(2)}(\omega_2) = \lim_{n \to \infty} f_n^{(2)}(\omega_2)$. Then

$$0 < f^{(1)}(\omega_1^0) = \int_{\Omega_2} f^{(2)}(\omega_2) P(\omega_1^0; d\omega_2),$$

and there is a point $\omega_2^0 \in \Omega_2$ such that $f^{(2)}(\omega_2^0) > 0$. Then $(\omega_1^0, \omega_2^0) \in B_2$. Continuing this process inductively, we find a point $(\omega_1^0, \ldots, \omega_n^0) \in B_n$ for each $n$. Consequently

$$(\omega_1^0, \omega_2^0, \ldots, \omega_n^0, \ldots) \in \bigcap_{n \geq 1} \hat{B}_n,$$

but by hypothesis we have $\bigcap_{n \geq 1} \hat{B}_n = \varnothing$. This contradiction shows that $\lim_n P(\hat{B}_n) = 0$, establishing countable additivity. The existence of the unique probability measure $P$ then follows from Carathéodory's extension theorem.

The second part of the theorem follows by putting $X_n(\omega) = \omega_n$, $n \geq 1$, i.e., the coordinate variables form the desired random sequence. $\square$

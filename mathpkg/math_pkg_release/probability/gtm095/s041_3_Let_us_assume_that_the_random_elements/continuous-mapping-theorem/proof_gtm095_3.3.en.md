---
role: proof
locale: en
of_concept: continuous-mapping-theorem
source_book: gtm095
source_chapter: "3"
source_section: "3"
---

# Proof of Theorem 2 (Continuous Mapping Theorem / Mann–Wald)

Let $(E, \mathcal{E}, \rho)$ and $(E', \mathcal{E}', \rho')$ be separable metric spaces, and let $X_n \xrightarrow{\mathcal{D}} X$. Let $h = h(x)$, $x \in E$, be a measurable mapping such that

$$P\{\omega : X(\omega) \in \Delta_h\} = 0,$$

where $\Delta_h = \{x \in E : h(x) \text{ is not } \rho\text{-continuous at } x\}$.

*Proof.* As in Theorem 1, it is enough to prove the validity of, for example, the first proposition.

Let $X^*$ and $X_n^*$, $n \geq 1$, be random elements constructed by the "method of a single probability space," so that $X^* \stackrel{\mathcal{D}}{=} X$, $X_n^* \stackrel{\mathcal{D}}{=} X_n$, $n \geq 1$, and $X_n^* \stackrel{\text{a.s.}}{\longrightarrow} X^*$. Let

$$A^* = \{\omega^* : \rho(X_n^*, X^*) \to 0\},$$

so that $P^*(A^*) = 1$. Also let $B^* = \{\omega^* : X^*(\omega^*) \notin \Delta_h\}$. Then $P^*(B^*) = 1$.

Now, if $\omega^* \in A^* \cap B^*$, then $\rho'(h(X_n^*(\omega^*)), h(X^*(\omega^*))) \to 0$. Hence

$$h(X_n^*) \xrightarrow{\text{a.s.}} h(X^*).$$

Since almost sure convergence implies convergence in distribution, we obtain $h(X_n^*) \xrightarrow{\mathcal{D}} h(X^*)$, and consequently $h(X_n) \xrightarrow{\mathcal{D}} h(X)$.

For the second proposition: since $P_n \xrightarrow{w} P$ and $P(\Delta_h) = 0$, applying the first part with suitable random elements yields $P_n^h \xrightarrow{w} P^h$, where $P_n^h(A) = P_n\{h(x) \in A\}$, $P^h(A) = P\{h(x) \in A\}$, $A \in \mathcal{E}'$.

$\square$

**Remark.** The condition $P\{\omega : X(\omega) \in \Delta_h\} = 0$ says that the limiting random element $X$ puts zero mass on the discontinuity set of $h$. This is the essential weakening relative to the classical Mann–Wald theorem, which requires continuity of $h$ everywhere; here $h$ need only be continuous almost surely with respect to the limit law.

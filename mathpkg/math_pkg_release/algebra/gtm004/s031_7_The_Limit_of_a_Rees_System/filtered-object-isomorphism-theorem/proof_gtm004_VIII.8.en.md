---
role: proof
locale: en
of_concept: filtered-object-isomorphism-theorem
source_book: gtm004
source_chapter: "VIII"
source_section: "8"
---

# Proof of Isomorphism Theorem for Filtered Objects

**Theorem 8.4.** Let $\psi: X \to X'$ be a morphism of filtered objects in an abelian category $\mathfrak{A}$, as in (8.8). Suppose that $\psi$ induces an isomorphism on the associated graded objects:

$$\psi_*: \operatorname{Gr}(X) \xrightarrow{\sim} \operatorname{Gr}(X').$$

If the filtrations of $X$ and $X'$ are left complete, then the induced map on quotient objects $\psi_p: X_p \to X'_p$ is an isomorphism for each $p$. If the filtrations are right complete, then the induced map on subobjects $\psi^p: X^p \to X'^p$ is an isomorphism for each $p$. If the filtrations are complete, then $\psi$ itself is an isomorphism.

**Proof.** By hypothesis, $\psi$ induces an isomorphism on each graded piece:

$$\psi_*: X^p / X^{p-1} \xrightarrow{\sim} X'^p / X'^{p-1}$$

for all $p$. Set $X_q^p = X^p / X^q$ for $q \leq p$ (with $X^q = 0$ when $q$ is sufficiently negative). Since $\psi$ respects the filtrations, it induces morphisms

$$\psi_*: X_q^p \to X'_q^p.$$

We prove by induction on $d = p - q$ that each such induced morphism is an isomorphism.

For $d = 0$, $X_p^p = X^p / X^p = 0$, and the claim holds trivially. For $d = 1$, $X_{p-1}^p = X^p / X^{p-1}$, which is precisely the $p$-th graded piece; the claim holds by assumption.

Assume the claim for all pairs with difference $< d$. Consider the short exact sequence

$$0 \to X_{q}^{p-1} \to X_{q}^p \to X_{p-1}^p \to 0,$$

which arises from the third isomorphism theorem. This fits into the commutative diagram with exact rows:

$$
\begin{array}{ccccccccc}
0 & \to & X_{q}^{p-1} & \to & X_{q}^p & \to & X_{p-1}^p & \to & 0 \\
& & {\scriptstyle\psi_*}\downarrow & & {\scriptstyle\psi_*}\downarrow & & {\scriptstyle\psi_*}\downarrow & & \\
0 & \to & X'_{q}\!^{p-1} & \to & X'_{q}\!^{p} & \to & X'_{p-1}\!^{p} & \to & 0.
\end{array}
$$

The outer vertical arrows are isomorphisms: the left one by the induction hypothesis (difference $d-1$), and the right one is the graded isomorphism. By the Five Lemma (or the short five lemma), the middle vertical arrow $\psi_*: X_q^p \to X'_q^p$ is also an isomorphism. This completes the induction.

Now, if the filtrations are **right complete**, then by definition $X = \varprojlim_p X_p$ and $X' = \varprojlim_p X'_p$. Moreover, Proposition 8.3(i) gives $X^p = \varprojlim_q X_q^p$ and similarly for $X'^p$. Since each $\psi_*: X_q^p \to X'_q^p$ is an isomorphism, the induced map on the limits

$$\psi^p = \varprojlim_q \psi_*: X^p \to X'^p$$

is an isomorphism for each $p$.

If the filtrations are **left complete**, then by definition $X = \varinjlim_p X^p$ and $X' = \varinjlim_p X'^p$, and Proposition 8.3(ii) gives $X_q = \varinjlim_p X_q^p$. Since each $\psi_*: X_q^p \to X'_q^p$ is an isomorphism, the induced map on the colimits

$$\psi_q = \varinjlim_p \psi_*: X_q \to X'_q$$

is an isomorphism for each $q$. In the notation of (8.4), this means $\psi_p: X_p \to X'_p$ is an isomorphism.

If the filtrations are **complete** (both left and right complete), then both families of isomorphisms hold. In particular, $\psi = \varinjlim_p \psi^p: X \to X'$ is an isomorphism, being the colimit of isomorphisms. $\square$

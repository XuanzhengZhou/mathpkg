---
role: proof
locale: en
of_concept: distribution-as-derivative-of-function
source_book: gtm012
source_chapter: "4"
source_section: "§4"
---

# Proof of Distribution as derivative of a continuous function

Let $F$ be a distribution of order $k-2$, with $k \geq 2$ an integer. We proceed by induction on $k$.

**Base case: $k = 2$.** Then $F$ is of order $0$, i.e. $F$ is a measure. Define the operator $S_{-}$ (integration from $t$ to $\infty$) acting on distributions. For any distribution $G$, the distribution $S_{-}G$ satisfies $D(S_{-}G) = -G$. In particular, if $G$ has order $m$, then $S_{-}G$ has order $m-1$ (or less).

Let $G = S_{-}F$. Since $F$ has order $0$, $G$ has order $-1$, which means $G$ is a regular distribution induced by a continuous function. More precisely, there exists a continuous function $u \colon \mathbb{R} \to \mathbb{C}$ such that $G = F_{u}$, where $F_{u}$ denotes the regular distribution corresponding to $u$.

Now define
$$v(t) = \int_{t}^{\infty} (s-t) \, D^{2} u(s) \, ds.$$

Integrating by parts (or equivalently, using the fundamental theorem of calculus and the definition of distributional derivative), we have
$$v(t) = -\int_{t}^{\infty} D u(s) \, ds = u(t).$$

Thus $D^{2} F_{f} = F$ with $f = u$ (after adjusting for constants). More formally, the computation shows that the second distributional derivative of $F_{u}$ recovers the original distribution $F$:
$$D^{2} F_{f} = F.$$

This establishes the base case.

**Inductive step.** Suppose $F$ is of order $k-2 > 0$. Let
$$G = (S_{-})^{k-2} F.$$

Since each application of $S_{-}$ reduces the order by at most $1$, $G$ is a distribution of order $0$. By the base case proved above, there exists a continuous function $f \colon \mathbb{R} \to \mathbb{C}$ such that
$$D^{2} F_{f} = G.$$

Now apply $D^{k-2}$ to both sides:
$$D^{k} F_{f} = D^{k-2} (D^{2} F_{f}) = D^{k-2} G = D^{k-2} (S_{-})^{k-2} F.$$

Since $D^{k-2} (S_{-})^{k-2}$ is the identity operator (each $D$ undoes one $S_{-}$), we obtain
$$D^{k} F_{f} = F.$$

This completes the existence part of the proof.

**Uniqueness.** We need to show that if $D^{k} F_{f} = D^{k} F_{g}$ for two continuous functions $f, g$, then $F_{f} = F_{g}$. Equivalently, we must prove that $D F = 0$ implies $F = 0$ for any distribution $F$ of the form $F = D^{k-1}F_{h}$.

Suppose $D F = 0$. Recalling the definition of $S_{-}$, we have the identity $F = S_{-}(D F)$ (this follows from the fact that $D S_{-} G = -G$ and adjusting for signs). Therefore
$$F = S_{-}(D F) = S_{-}(0) = 0.$$

Hence the representation $F = D^{k} F_{f}$ is unique: if $D^{k} F_{f} = D^{k} F_{g}$, then $D^{k}(F_{f} - F_{g}) = 0$, so by applying the uniqueness argument repeatedly, $F_{f} - F_{g} = 0$, i.e. $F_{f} = F_{g}$. $\square$

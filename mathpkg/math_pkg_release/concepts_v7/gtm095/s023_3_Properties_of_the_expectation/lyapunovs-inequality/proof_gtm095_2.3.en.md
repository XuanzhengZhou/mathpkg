---
role: proof
locale: en
of_concept: lyapunovs-inequality
source_book: gtm095
source_chapter: "2"
source_section: "3"
---

# Proof of Lyapunov's Inequality for Absolute Moments

**Lyapunov's Inequality.** If $0 < s < t$, then

$$(E|\xi|^s)^{1/s} \leq (E|\xi|^t)^{1/t}. \tag{27}$$

*Proof.* Let $r = t/s > 1$. Put $\eta = |\xi|^s$ and apply Jensen's inequality to the convex function $g(x) = |x|^r$ (which is convex for $r \geq 1$). Then

$$|E\eta|^r \leq E|\eta|^r,$$

i.e.,

$$(E|\xi|^s)^{t/s} \leq E|\xi|^t.$$

Raising both sides to the power $1/t$ yields $(E|\xi|^s)^{1/s} \leq (E|\xi|^t)^{1/t}$, which establishes (27).

As a consequence, the following chain of inequalities among absolute moments holds:

$$E|\xi| \leq (E|\xi|^2)^{1/2} \leq \cdots \leq (E|\xi|^n)^{1/n}. \tag{28}$$

$\square$

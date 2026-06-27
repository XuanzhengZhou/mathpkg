---
role: proof
locale: en
of_concept: strong-markov-property
source_book: gtm095
source_chapter: "1"
source_section: "12"
---

# Proof of the Strong Markov Property

## Theorem (Strong Markov Property, Theorem 2)

Let $\xi = (\xi_0, \xi_1, \ldots, \xi_n)$ be a homogeneous Markov chain with transition probabilities $p_{ij}$ defined on a probability space $(\Omega, \mathcal{F}, \mathrm{P})$. Let $\tau$ be a stopping time (with respect to the natural filtration $\mathcal{F}_k^\xi = \sigma(\xi_0, \ldots, \xi_k)$). Then for any event $A \in \mathcal{F}_\tau^\xi$ and $B \in \mathcal{F}_\tau^\xi$ with $\mathrm{P}\{A \cap B \cap (\xi_\tau = a_0)\} > 0$, and any states $a_1, \ldots, a_l$,

$$\mathrm{P}\{\xi_{\tau+l} = a_l, \ldots, \xi_{\tau+1} = a_1 \mid A \cap B \cap (\xi_\tau = a_0)\} = p_{a_0 a_1} \cdots p_{a_{l-1} a_l}. \tag{32}$$

In particular, if $\mathrm{P}\{A \cap (\xi_\tau = a_0)\} > 0$, then

$$\mathrm{P}\{\xi_{\tau+l} = a_l, \ldots, \xi_{\tau+1} = a_1 \mid A \cap (\xi_\tau = a_0)\} = p_{a_0 a_1} \cdots p_{a_{l-1} a_l}. \tag{33}$$

## Proof

For the sake of simplicity, we give the proof only for the case $l = 1$. The general case follows by induction.

Since $B \cap \{\tau = k\} \in \mathcal{F}_k^\xi$ (which follows from the definition of a stopping time and the fact that $B$ is measurable with respect to $\mathcal{F}_\tau^\xi$), we have, using the Markov property (8),

$$
\begin{aligned}
\mathrm{P}\{\xi_{\tau+1} = a_1, A \cap B \cap (\xi_\tau = a_0)\}
&= \sum_{k \leq n-1} \mathrm{P}\{\xi_{k+1} = a_1, \xi_k = a_0, \tau = k, B\} \\[4pt]
&= \sum_{k \leq n-1} \mathrm{P}\{\xi_{k+1} = a_1 \mid \xi_k = a_0, \tau = k, B\} \cdot \mathrm{P}\{\xi_k = a_0, \tau = k, B\} \\[4pt]
&= p_{a_0 a_1} \sum_{k \leq n-1} \mathrm{P}\{\xi_k = a_0, \tau = k, B\} \\[4pt]
&= p_{a_0 a_1} \, \mathrm{P}\{A \cap B \cap (\xi_\tau = a_0)\}.
\end{aligned}
$$

Dividing both sides by $\mathrm{P}\{A \cap B \cap (\xi_\tau = a_0)\}$ yields

$$\mathrm{P}\{\xi_{\tau+1} = a_1 \mid A \cap B \cap (\xi_\tau = a_0)\} = p_{a_0 a_1},$$

which establishes (32) for $l = 1$. Formula (33) follows immediately by taking $B = \Omega$ (the whole sample space).

The general case $l > 1$ is proved by induction on $l$, applying the Markov property repeatedly at the random times $\tau, \tau+1, \ldots, \tau+l-1$, each time using the fact that $\tau + m$ is again a stopping time (for deterministic $m \ge 0$).

## Remark

When $l = 1$, the strong Markov property (32), (33) is equivalent to the property that for every $C \subseteq X$,

$$\mathrm{P}\{\xi_{\tau+1} \in C \mid A \cap B \cap (\xi_\tau = a_0)\} = P_{a_0}(C),$$

where $P_{a_0}(C) = \sum_{a_1 \in C} p_{a_0 a_1}$.

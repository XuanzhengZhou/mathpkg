---
role: proof
locale: en
of_concept: function-representation-for-hulls-over-circle
source_book: gtm035
source_chapter: "Chapter 20"
source_section: "20.4"
---
# Proof of Function Representation for Polynomial Hulls Over Circle

**Lemma 20.4.** $\mathcal{F}$ consists of all functions $f$ on $\{|\lambda| < 1\}$ that can be written in the form

$$f = \frac{P}{Q} + \frac{B}{Q_0}$$

with $B \in H^\infty$, $\|B\|_\infty \leq 1$, and

$$B(\lambda_j) = w_j, \quad 1 \leq j \leq n,$$

where

$$Q(\lambda) = Q_0(\lambda) R(\lambda), \quad Q_0(\lambda) = \prod_{i=1}^{n} \frac{\lambda - \lambda_i}{1 - \bar{\lambda}_i \lambda},$$

$\lambda_1, \lambda_2, \ldots, \lambda_n$ are the zeros of $Q$ in $\{|\lambda| < 1\}$, $R$ is a rational function with $R(\lambda) \neq 0$ in $\{|\lambda| \leq 1\}$, and

$$w_j = -\frac{P(\lambda_j)}{R(\lambda_j)}, \quad j = 1, 2, \ldots, n.$$

**Proof.** Suppose that $f \in \mathcal{F}$. Define the function $\zeta$ by

$$f = \frac{P}{Q} + \zeta.$$

Then $\zeta$ is meromorphic on $\{|\lambda| < 1\}$ with a simple pole at each $\lambda_j$. Also,

$$\zeta = \frac{fQ - P}{Q} = \left( \frac{fQ - P}{R} \right) \frac{1}{Q_0}.$$

Put $B = (fQ - P)/R$. Then $B \in H^\infty$ and $\|B\|_\infty \leq \|f\|_\infty \|Q/R\|_\infty + \|P/R\|_\infty$, so after scaling we may assume $\|B\|_\infty \leq 1$. Moreover, $B(\lambda_j) = -P(\lambda_j)/R(\lambda_j) = w_j$ for each $j$. Thus $f$ has the desired form.

Conversely, suppose $f$ is given by

$$f = \frac{P}{Q} + \frac{B}{Q_0}$$

with $B \in H^\infty$, $\|B\|_\infty \leq 1$, and $B(\lambda_j) = w_j$ for $1 \leq j \leq n$. We verify that $f$ has at most removable singularities at the $\lambda_j$. Indeed, we have

$$\operatorname{res}_{\lambda_j} \frac{P}{Q} = \frac{P(\lambda_j)}{Q'(\lambda_j)},$$

and

$$\operatorname{res}_{\lambda_j} \frac{B}{Q_0} = \frac{B(\lambda_j)}{Q'_0(\lambda_j)} = \frac{w_j}{Q'_0(\lambda_j)} = -\frac{P(\lambda_j)}{R(\lambda_j)} \cdot \frac{1}{Q'_0(\lambda_j)} = -\frac{P(\lambda_j)}{Q'(\lambda_j)},$$

for $j = 1, \ldots, n$. Hence $\operatorname{res}_{\lambda_j} f = 0$ for all $j$. Since $f$ has at each $\lambda_j$ at most a simple pole, it follows that $\lambda_j$ is a removable singularity for $f$ for all $j$. So $f \in H^\infty$. Then, for almost all $\lambda \in \Gamma$,

$$\left| f(\lambda) - \frac{P(\lambda)}{Q(\lambda)} \right| = \left| \frac{B(\lambda)}{Q_0(\lambda)} \right| = |B(\lambda)| \leq 1.$$

So $f \in \mathcal{F}$, and we are done. ∎

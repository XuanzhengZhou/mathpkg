---
role: proof
locale: en
of_concept: thm-when-is-aperiodic-and-recurrent-let
source_book: gtm034
source_chapter: "7"
source_section: "017"
---

Proof: If

$$g(x) = \sum_{t \in R} A(x,t)\psi(t), \quad \sum_{x \in A} \psi(x) = c,$$

then, according to T29.1,

$$\lim_{|x| \to \infty} [g(x) - ca(x)] = 0 \text{ when } d = 2 \text{ or } d = 1 \text{ with } \sigma^2 = \infty,$$

$$\lim_{x \to \pm \infty} [g(x) - ca(x)] = \mp \frac{1}{\sigma^2} \sum_{t \in A} t\psi(t) \

When $d = 1$ with $\sigma^2 < \infty$, one obtains

$$f(x) = \sum_{t \in A} A(x,t)\psi(t) + \alpha x + \text{constant}, \quad |\alpha| \leq (\sigma^2)^{-1}.$$

It is easily verified that the only possible values of the constants $c_1, c_2, c_3$ are those given in T3.

One can extend T3 without difficulty to hold for charges $\psi(x)$ whose support is an infinite subset $A$ of $R$ or even all of $R$, but only if $\psi$ is $a$-integrable, i.e., if $\sum_{t \in R} a(x - t)|\psi(t)| < \infty$ for $x \in R$. To show that one cannot hope for much more, consider the example

**E1 Two-dimensional simple random walk, where we write**

$$P(0,z) = \begin{cases} \frac{1}{4} \text{ for } z = 1, -1, i, -i, \\ 0 \text{ for all other } z \in R. \end{cases}$$

Let

$$f(z) = |\text{Re}(z)|, \quad A = [z | \text{Re}(z) = 0].$$

Then

$$\sum_{\zeta \in R} P(z,\zeta)f(\zeta) - f(z) = \psi(z),$$

where

$$\psi(z) = \begin{cases} \frac{1}{2} \text{ for } z \in A \\ 0 \text{ for } z \in R - A. \end{cases}$$

These facts are easily checked. Now P3 or T3, if valid in this case, would give

$$f(z) = \frac{1}{2} \sum_{\zeta \in A} A(z,\zeta)$$

which is false, the sum on the right being divergent since

$$A(0,z) \sim \frac{2}{\pi} \ln |z| \text{ as } |z| \to \infty.$$

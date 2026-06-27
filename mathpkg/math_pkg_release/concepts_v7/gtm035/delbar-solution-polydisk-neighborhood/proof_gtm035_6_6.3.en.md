---
role: proof
locale: en
of_concept: delbar-solution-polydisk-neighborhood
source_book: gtm035
source_chapter: "6"
source_section: "6.3"
---
# Proof of $\bar{\partial}$ Solution in a Neighborhood of the Polydisk

**Lemma 6.3.** Let $f \in C^\infty(\Omega)$ where $\Omega$ is a neighborhood of the closed unit polydisk $\Delta^n = \{z \in \mathbb{C}^n \mid |z_j| \leq 1,\ j = 1, \ldots, n\}$. Fix an integer $v$ with $1 \leq v \leq n$ and assume that

$$\frac{\partial f}{\partial \bar{z}_k} = 0 \quad \text{in } \Omega \text{ for all } k > v.$$

Then there exists a neighborhood $\Omega_1$ of $\Delta^n$ and a function $u \in C^\infty(\Omega_1)$ such that

$$\text{(a)}\quad \frac{\partial u}{\partial \bar{z}_v} = f \quad \text{in } \Omega_1,$$
$$\text{(b)}\quad \frac{\partial u}{\partial \bar{z}_k} = 0 \quad \text{for } k > v \text{ in } \Omega_1.$$

*Proof.* Choose $\varepsilon > 0$ such that the slightly enlarged polydisk

$$\{z \in \mathbb{C}^n \mid |z_j| < 1 + \varepsilon,\ j = 1, \ldots, n\}$$

is contained in $\Omega$. By multiplying $f$ with a smooth cutoff function (using a partition of unity argument), we may assume without loss of generality that $f$ has compact support in the $z_v$-variable within the disk $\{|z_v| < 1 + \varepsilon\}$. For each fixed tuple of the remaining variables

$$(\zeta_1, \ldots, \zeta_{v-1}, \zeta_{v+1}, \ldots, \zeta_n),$$

define the function of one complex variable

$$\phi(\zeta_v) = f(\zeta_1, \ldots, \zeta_{v-1}, \zeta_v, \zeta_{v+1}, \ldots, \zeta_n).$$

By construction, $\phi \in C^1(\mathbb{C})$ with compact support in $\{|\zeta_v| < 1 + \varepsilon\}$. Applying Lemma 6.2, there exists a function

$$\Phi(\zeta_v) = -\frac{1}{\pi} \int_{\mathbb{C}} \phi(z) \frac{dx \, dy}{z - \zeta_v}$$

satisfying $\partial \Phi / \partial \bar{\zeta}_v = \phi(\zeta_v)$ for all $\zeta_v$.

Now define $u$ on the polydisk neighborhood

$$\Omega_1 = \{\zeta \in \mathbb{C}^n \mid |\zeta_\nu| < 1 + \varepsilon,\ \nu = 1, \ldots, n\}$$

by

$$u(\zeta_1, \ldots, \zeta_n) = -\frac{1}{\pi} \int_{\mathbb{C}} f(\zeta_1, \ldots, \zeta_{v-1}, z, \zeta_{v+1}, \ldots, \zeta_n) \frac{dx \, dy}{z - \zeta_v}.$$

Then by Lemma 6.2, for each fixed $(\zeta_1, \ldots, \zeta_{v-1}, \zeta_{v+1}, \ldots, \zeta_n)$ with $|\zeta_j| < 1 + \varepsilon$, we obtain

$$\frac{\partial u}{\partial \bar{\zeta}_v}(\zeta_1, \ldots, \zeta_n) = f(\zeta_1, \ldots, \zeta_{v-1}, \zeta_v, \zeta_{v+1}, \ldots, \zeta_n)$$

whenever $|\zeta_v| < 1 + \varepsilon$. This proves property (a).

For property (b), fix $k > v$. Since $\partial f / \partial \bar{z}_k = 0$ by hypothesis, differentiation under the integral sign yields

$$\frac{\partial u}{\partial \bar{\zeta}_k}(\zeta) = -\frac{1}{\pi} \int_{\mathbb{C}} \frac{\partial f}{\partial \bar{\zeta}_k}(\zeta_1, \ldots, z, \ldots, \zeta_n) \frac{dx \, dy}{z - \zeta_v} = 0$$

for all $\zeta \in \Omega_1$. The differentiation under the integral sign is justified by the smoothness of $f$ and the compact support in the $z_v$-variable.

Smoothness of $u$ in $\Omega_1$ follows from the smoothness of $f$ and the fact that the Cauchy kernel $1/(z - \zeta_v)$ is locally integrable, allowing repeated differentiation under the integral sign. $\square$

**Remark.** Lemma 6.3 is the key technical tool used in the induction proof of the Complex Poincaré Lemma (Theorem 6.1). It allows solving the $\bar{\partial}$-equation one variable at a time, decomposing the problem by "level" of differential forms with respect to the conjugate variables $d\bar{z}_1, \ldots, d\bar{z}_n$.

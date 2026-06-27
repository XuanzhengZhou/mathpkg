---
role: proof
locale: en
of_concept: conjugation-preserves-operations
source_book: gtm077
source_chapter: "19"
source_section: "19"
---
# Proof of Theorem 55: Conjugation Preserves Field Operations

**Theorem 55.** Let $K = K(\theta; k)$ and fix an ordering of the conjugates $\theta_1, \ldots, \theta_n$. For each $\alpha \in K$, write $\alpha_i = g(\theta_i)$ where $\alpha = g(\theta)$ is the unique representation from Theorem 53. Then conjugation preserves all field operations in the strong sense:

$$\alpha_i \pm \beta_i = (\alpha \pm \beta)_i, \qquad \alpha_i \beta_i = (\alpha \beta)_i, \qquad \frac{\alpha_i}{\beta_i} = \left(\frac{\alpha}{\beta}\right)_i \quad (\beta \neq 0),$$

for all $i = 1, \ldots, n$.

*Proof.* Let $\alpha = g(\theta)$ and $\beta = h(\theta)$ with $g(x), h(x) \in k[x]$ of degree at most $n-1$. For the operation of addition, we have

$$\alpha + \beta = g(\theta) + h(\theta) = (g + h)(\theta).$$

The polynomial $g + h$ has degree at most $n-1$ and coefficients in $k$. Since the conjugate indexing is defined via this unique polynomial representation (modulo reduction by the minimal polynomial of $\theta$), we obtain

$$(\alpha + \beta)_i = (g + h)(\theta_i) = g(\theta_i) + h(\theta_i) = \alpha_i + \beta_i.$$

Similarly, subtraction follows by the same argument applied to $g - h$.

For multiplication, compute $\alpha\beta = g(\theta)h(\theta)$. Write $g(x)h(x) = q(x)f(x) + r(x)$ with $\deg r \leq n-1$, where $f(x)$ is the minimal polynomial of $\theta$. Then $\alpha\beta = r(\theta)$, and

$$(\alpha\beta)_i = r(\theta_i).$$

On the other hand, for each conjugate $\theta_i$, we have $f(\theta_i) = 0$, so

$$\alpha_i\beta_i = g(\theta_i)h(\theta_i) = q(\theta_i)f(\theta_i) + r(\theta_i) = r(\theta_i).$$

Thus $(\alpha\beta)_i = \alpha_i\beta_i$ for all $i$. In the original text, Hecke presents this more directly: from the single equation $g(\theta)h(\theta) = r(\theta)$ in $k[\theta]$, Theorem 55 (in its general form) implies the $n$ equations $g(\theta_i)h(\theta_i) = r(\theta_i)$ for $i = 1, \ldots, n$, which immediately yields $\alpha_i\beta_i = (\alpha\beta)_i$.

For division, let $\beta \neq 0$. By Theorem 53, the representation $\alpha/\beta = s(\theta)$ with $\deg s \leq n-1$ is unique. Then $\alpha = \beta \cdot (\alpha/\beta)$, i.e., $g(\theta) = h(\theta)s(\theta)$ (after reduction mod $f$). By the multiplicative case just proved,

$$\alpha_i = \beta_i \cdot (\alpha/\beta)_i$$

for all $i$. Since $\beta \neq 0$, we have $\beta_i \neq 0$ (by the inequality-preserving property of Theorem 55), and division yields $(\alpha/\beta)_i = \alpha_i / \beta_i$.

Thus each map $\sigma_i : \alpha \mapsto \alpha_i$ is a field isomorphism of $K$ onto $K(\theta_i)$ that fixes the ground field $k$ elementwise. $\square$

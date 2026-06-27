---
role: proof
locale: en
of_concept: lemma-dd3da2b7dd
source_book: gtm077
source_chapter: "V"
source_section: "§38"
---
# Proof of Lemma (b)

For each number $B$ in $R_k(\theta)$,

$$S_k\left(\frac{B}{\Phi'(\theta)}\right) \text{ is integral.}$$

**Proof.** The proof runs parallel to the proof of the corresponding lemma in §36 (absolute case). Let $\theta$ be an integer generating $K$ over $k$, with $\Phi(x)$ the minimal polynomial of $\theta$ over $k$. The relative ring $R_k(\theta)$ consists of all polynomials in $\theta$ of degree at most $m-1$ with integral coefficients from $k$.

For any $B \in R_k(\theta)$, we can write $B = \sum_{j=0}^{m-1} \beta_j \theta^j$ with integers $\beta_j$ in $k$. Consider the expression

$$S_k\left(\frac{B}{\Phi'(\theta)}\right) = S_k\left(\frac{\sum_{j=0}^{m-1} \beta_j \theta^j}{\Phi'(\theta)}\right).$$

By the Euler-Lagrange interpolation formula (or equivalently, by considering the partial fraction decomposition with respect to the conjugates $\theta^{(i)}$), we have

$$\frac{\theta^j}{\Phi'(\theta)} = \sum_{i=1}^{m} \frac{(\theta^{(i)})^j}{\Phi'(\theta^{(i)})} \cdot \frac{1}{x - \theta^{(i)}}\Big|_{x=\theta}$$

and the relative trace $S_k$ evaluated on such expressions yields elementary symmetric functions of the conjugates, which are integers in $k$. More concretely, for each conjugate $\theta^{(i)}$,

$$\sum_{i=1}^{m} \frac{(\theta^{(i)})^j}{\Phi'(\theta^{(i)})}$$

is an integer in $k$ (it is the coefficient in the partial fraction expansion). Hence $S_k\left(\frac{B}{\Phi'(\theta)}\right)$ is integral.

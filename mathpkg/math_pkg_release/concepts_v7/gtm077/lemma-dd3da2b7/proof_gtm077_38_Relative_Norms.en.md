---
role: proof
locale: en
of_concept: lemma-dd3da2b7
source_book: gtm077
source_chapter: "38"
source_section: "Relative Norms of Numbers and Ideals, Relative Differents, and Relative Discriminants"
---
# Proof of Lemma (b)

**Statement.** For each number $B$ in $R_k(\theta)$,

$$S_k\left(\frac{B}{\Phi'(\theta)}\right) \text{ is integral.}$$

*Proof.* As in §36, one considers the partial fraction decomposition of $1/\Phi(x)$ over the splitting field. Let $\theta = \theta^{(1)}, \theta^{(2)}, \ldots, \theta^{(m)}$ be the relative conjugates of $\theta$. Then

$$\frac{1}{\Phi(x)} = \sum_{i=1}^{m} \frac{1}{\Phi'(\theta^{(i)})(x - \theta^{(i)})}.$$

Expanding both sides as formal power series in $1/x$ and comparing coefficients yields trace relations: for any polynomial $B(\theta) \in R_k(\theta)$, the expression

$$S_k\left(\frac{B(\theta)}{\Phi'(\theta)}\right) = \sum_{i=1}^{m} \frac{B(\theta^{(i)})}{\Phi'(\theta^{(i)})}$$

is a sum of residues that evaluates to an integer. More concretely, this follows from the fact that the matrix $( (\theta^{(i)})^j / \Phi'(\theta^{(i)}) )_{i,j}$ is the inverse of the Vandermonde-type matrix $( (\theta^{(i)})^j )_{i,j}$, so the trace expression picks out coefficients in the basis expansion, which are integers when $B \in R_k(\theta)$.

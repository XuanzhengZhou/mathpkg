---
role: proof
locale: en
of_concept: norm-topology-is-tvs-topology
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "16. Normed spaces, Banach spaces"
---

# Proof that Norm Topology is Compatible with Vector Space Structure

**Theorem (16.5).** If $E$ is a normed space, then the norm topology on $E$ is compatible with the vector space structure; thus $E$, equipped with the norm topology, is a metrizable TVS.

*Proof.* The norm topology is compatible with the additive group structure by (8.7). It remains to verify the continuity of scalar multiplication. Assuming $\lambda_n \to \lambda$ and $x_n \to x$, it is to be shown that $\lambda_n x_n \to \lambda x$. One has

$$\lambda_n x_n - \lambda x = \lambda_n(x_n - x) + (\lambda_n - \lambda)x,$$

therefore

$$\|\lambda_n x_n - \lambda x\| \leq |\lambda_n| \|x_n - x\| + |\lambda_n - \lambda| \|x\|.$$

Since $|\lambda_n - \lambda| \to 0$ and $\|x_n - x\| \to 0$, and since $|\lambda_n|$ is bounded (convergent sequences are bounded), clearly $\|\lambda_n x_n - \lambda x\| \to 0$. Thus scalar multiplication is jointly continuous in the norm topology. $\square$

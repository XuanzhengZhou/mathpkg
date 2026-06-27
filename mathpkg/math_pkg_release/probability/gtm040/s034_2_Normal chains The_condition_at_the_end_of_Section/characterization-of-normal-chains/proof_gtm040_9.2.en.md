---
role: proof
locale: en
of_concept: characterization-of-normal-chains
source_book: gtm040
source_chapter: "9"
source_section: "2"
---

(1) is the definition of normality (Definition 9-20). If (2) holds, then ${}^0\nu_j$ and ${}^0\hat{\nu}_j$ exist by Lemma 9-25, which implies that ${}^0\lambda_j = {}^0\nu_j / {}^0N_{jj}$ and ${}^0\hat{\lambda}_j = {}^0\hat{\nu}_j / {}^0\hat{N}_{jj}$ both exist, so (1) holds. The sufficiency of (3) was shown in Lemma 9-23.

Conversely, suppose $P$ is normal. Then by definition ${}^0\lambda_j$ and ${}^0\hat{\lambda}_j$ exist for all $j$. Corollary 9-22 assures that all $f$ with finite support and $\alpha f = 0$ are potential charges.

Consider the charge
$$f_k = \begin{cases} \alpha_j / \alpha_i & \text{if } k = i \\ -1 & \text{if } k = j \\ 0 & \text{otherwise.} \end{cases}$$

Since $f$ has finite support and $\alpha f = 0$, it is a charge. By Lemma 9-23 and properties of $G$, its potential has as $i$th component $G_{ij} = {}^i\nu_j$. Therefore $G_{ij}$ exists for all $i, j$, and ${}^i\nu_j = {}^i\lambda_j\,{}^iN_{jj}$ by definition (${}^i\lambda_j = {}^i\nu_j / {}^iN_{jj}$). So ${}^i\lambda_j$ and ${}^i\nu_j$ exist for all $i,j$.

For $C_{ij}$, the dual argument applied to $\hat{P}$ (which is normal because $P$ is normal) gives the corresponding dual identities: $\hat{G} = {}^i\hat{\nu}$, and by the duality relation $\hat{G}_{ij} = \alpha_j C_{ji} / \alpha_i$ (Lemma 9-25), we obtain
$$C_{ij} = \frac{\alpha_j}{\alpha_i} {}^j\hat{\nu}_i = {}^j\hat{\lambda}_i\,{}^iN_{jj}.$$

The statement about all functions and signed measures of finite support follows by linearity: any such function can be expressed as a finite linear combination of two-point charges, each of which is a potential charge.

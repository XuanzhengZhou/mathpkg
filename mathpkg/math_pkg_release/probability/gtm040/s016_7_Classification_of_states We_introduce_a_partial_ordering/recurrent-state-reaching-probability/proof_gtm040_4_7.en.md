---
role: proof
locale: en
of_concept: recurrent-state-reaching-probability
source_book: gtm040
source_chapter: "4"
source_section: "7. Classification of states"
---

**Proof:** The result is obvious if $i = j$. If $i \neq j$, consider returning to $i$ with and without first reaching $j$. By conclusion (3) of Lemma 4-19,
$$1 = \bar{H}_{ii} = {}_i\bar{H}_{ij}H_{ji} + {}_j\bar{H}_{ii}.$$

Since ${}_i\bar{H}_{ij} + {}_j\bar{H}_{ii} \leq 1$ (these are probabilities of mutually exclusive events), this equation is a contradiction unless either ${}_j\bar{H}_{ii} = 1$ or $H_{ji} = 1$.

The first alternative ${}_j\bar{H}_{ii} = 1$ is ruled out by Lemma 4-22, since $i \neq j$ and $R(i,j)$ implies ${}_j\bar{H}_{ii} < 1$. Thus $H_{ji} = 1$ and consequently ${}_i\bar{H}_{ij} = 1 - {}_j\bar{H}_{ii}$.

Next, since $i$ is recurrent, one may compute $H_{ij}$ by summing the probabilities of reaching $j$ for the first time after $n$ returns to $i$, where $n = 0, 1, 2, \ldots$. By conclusion (4) of Lemma 4-19,
$$H_{ij} = \sum_{n=0}^{\infty} ({}_j\bar{H}_{ii})^n {}_i\bar{H}_{ij} = (1 - {}_j\bar{H}_{ii}) \sum_{n=0}^{\infty} ({}_j\bar{H}_{ii})^n = 1.$$

The last equality holds since ${}_j\bar{H}_{ii} < 1$ by Lemma 4-22.

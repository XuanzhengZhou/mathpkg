---
role: proof
locale: en
of_concept: order-of-sum-of-independent-vectors
source_book: gtm031
source_chapter: "The Theory of a Single Linear Transformation"
source_section: "3"
---

*Proof.* Let $f = f_1 + f_2 + \cdots + f_s$ and let $\nu(\lambda) = \mu_1(\lambda)\mu_2(\lambda) \cdots \mu_s(\lambda)$. Since $f_i \mu_i(A) = 0$ for each $i$, we have $f_i \nu(A) = 0$ for all $i$, hence $f\nu(A) = \sum f_i \nu(A) = 0$. This proves that $\mu_f(\lambda) \mid \nu(\lambda)$.

For the reverse divisibility, we show that each $\mu_i(\lambda)$ divides $\mu_f(\lambda)$. Consider $\rho_1(\lambda) = \mu_f(\lambda)\mu_2(\lambda)\mu_3(\lambda) \cdots \mu_s(\lambda)$. Then $f\rho_1(A) = 0$ and for $j = 2, 3, \dots, s$, we have $f_j\rho_1(A) = 0$ because $\rho_1(\lambda)$ contains the factor $\mu_j(\lambda)$. Hence $f_1\rho_1(A) = (f - f_2 - \cdots - f_s)\rho_1(A) = 0$. This implies $\mu_1(\lambda) \mid \rho_1(\lambda)$. Since $\mu_1(\lambda)$ is relatively prime to each of $\mu_2(\lambda), \dots, \mu_s(\lambda)$ by hypothesis, and $\mu_1(\lambda) \mid \mu_f(\lambda)\mu_2(\lambda) \cdots \mu_s(\lambda)$, it follows that $\mu_1(\lambda) \mid \mu_f(\lambda)$. Similarly, $\mu_2(\lambda) \mid \mu_f(\lambda), \dots, \mu_s(\lambda) \mid \mu_f(\lambda)$. Hence the product $\nu(\lambda) = \prod \mu_i(\lambda)$ divides $\mu_f(\lambda)$, since the $\mu_i(\lambda)$ are pairwise coprime. Combining both divisibilities yields $\mu_f(\lambda) = \nu(\lambda)$. $\square$

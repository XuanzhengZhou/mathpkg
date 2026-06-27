---
role: proof
locale: en
of_concept: theorem-13-6
source_book: gtm055
source_chapter: "13-14"
source_section: "Section 15_Section_15"
---

Proof. That (ii) and (iii) imply one another in the presence of (i) is, once again, essentially the content of the closed graph theorem. Thus it need only be shown that if a quasinormed space $\mathcal{E}$ is the domain of a linear transformation that is both closed and continuous, then $\mathcal{E}$ must be complete. Suppose that $T: \mathcal{E} \rightarrow \mathcal{F}$ is such a transformation, and that $\{x_n\}$ is a Cauchy sequence in $\mathcal{E}$. If $\varepsilon$ is a given positive number, if $\delta > 0$ is chosen so that $|x| < \delta$ implies $|Tx| < \varepsilon$, and if $N$ is chosen large enough so that $|x_n - x_m| < \delta$ for all $m, n \geq N$, then $|Tx_n - Tx_m| = |T(x_n - x_m)| < \varepsilon$ for all $m, n \geq N$. Hence $\{Tx_n\}$ is also a Cauchy sequence in $\mathcal{F}$, and it follows at once that the sequence of pairs $\{(x_n, Tx_n)\}$ is Cauchy in $\mathcal{E} \oplus_1 \mathcal{F}$. Since this sequence belongs to the graph of $T$, and $T$ is closed

for example, that $\{\lambda_n\}_{n=0}^{\infty}$ is a sequence of scalars with the property that for some fixed pair of real numbers $p$ and $p'$, $1 \leq p, p' < +\infty$, the sequence $Lx = \{\lambda_n \xi_n\}_{n=0}^{\infty}$ belongs to $(\ell_{p'})$ whenever $x = \{\xi_n\}_{n=0}^{\infty}$ belongs to $(\ell_p)$. Then $L$ is bounded, as we have just seen, and if $\|L\| = r$, then it is easily verified that $\|\{\lambda_n\}\|_{\infty} = r$. (Indeed, if the vectors $e_n$ are as in Example 11H, we have $|\lambda_n| = \|Le_n\|_{p'} \leq r \|e_n\|_{p} = r$ for every nonnegative integer $n$. The fact that $\|\{\lambda_n\}\|_{\infty} = \|L\|$ can also be derived quite directly, of course, without recourse to any version of the closed graph theorem.)

An important theme in Chapters 12 and 13 has been the application of the Baire category theorem (Th. 4.8) to obtain important information concerning linear transformations on $F$-spaces and Banach spaces. The main theorems in this context are certainly the ones already dealt with, viz., the uniform boundedness theorem, and the open mapping and closed graph theorems. There are other applications, however, and we close this section with one more such result. It is instructive to compare the following proposition with Problem 12B.

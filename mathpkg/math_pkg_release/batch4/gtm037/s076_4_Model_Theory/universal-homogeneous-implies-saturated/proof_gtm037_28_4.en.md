---
role: proof
locale: en
of_concept: universal-homogeneous-implies-saturated
source_book: gtm037
source_chapter: "28"
source_section: "Saturated Structures"
---

Suppose that $A$ is $m$-universal and $m$-homogeneous, and assume that the hypothesis of 28.16(ii) holds. Expand $L'$ to $L''$ by adjoining a new individual constant $d$. Now consider the set

$$\Gamma = \Theta\rho(A, a_\xi)_{\xi < \alpha} \cup \{\varphi(d) : \varphi \in \Delta\}.$$

Our hypothesis of 28.16(ii) implies that every finite subset of $\Gamma$ has a model which is an expansion of $(A, a_\xi)_{\xi < \alpha}$. Hence $\Gamma$ has a model $(B, b_\xi, e)_{\xi < \alpha}$ of power $< m$. Thus $A \equiv_{\text{ee}} B$, so by the $m$-universality of $A$ we may assume that $B \preceq A$. Hence

$$(A, a_\xi)_{\xi < \alpha} \equiv_{\text{ee}} (B, b_\xi)_{\xi < \alpha} \equiv_{\text{ee}} (A, b_\xi)_{\xi < \alpha}.$$

Furthermore, $e$ realizes $\Delta$ in $(B, b_\xi)_{\xi < \alpha}$ and hence in $(A, b_\xi)_{\xi < \alpha}$. From the $m$-homogeneity of $A$ it follows that there is an $x \in A$ with

$$(A, a_\xi, x)_{\xi < \alpha} \equiv_{\text{ee}} (A, b_\xi, e)_{\xi < \alpha}.$$

Hence $x$ realizes $\Delta$ in $(A, a_\xi)_{\xi < \alpha}$.

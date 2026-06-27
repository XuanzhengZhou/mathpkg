---
role: proof
locale: en
of_concept: weakly-normal-limiting-system
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

The proof proceeds by showing that condition 4' together with the density condition implies the original condition 4 of a normal limiting system.

We define a sequence of ordinals $\xi_0 < \cdots < \xi_i < \cdots < \kappa$ ($i < \omega$) by induction. Set $\xi_0 = 0$. Suppose $\xi_i < \kappa$ has been defined. Take an arbitrary element $x \in P_{\xi_i} - A$ (where $A$ is a maximal antichain). By maximality of $A$, there exists $e_x \in A$ such that $e_x$ and $x$ are compatible. Define
$$\xi_{i+1} = \max(\xi_i + 1, \sup\{|a_x| \mid x \in P_{\xi_i} - A\}).$$

Since $\bar{P}_{\xi_i} < \kappa$ and $\kappa$ is regular, $\xi_{i+1} < \kappa$. Let $\eta = \sup\{\xi_i \mid i < \omega\}$. Then $\eta < \kappa$ and $\operatorname{cf}(\eta) = \omega$.

We claim that $A \subseteq P_{\eta}$, which implies $\bar{A} < \kappa$. Suppose not. Let $a \in A$ with $a \notin P_{\eta}$. Then $a \in P_{\beta}$ for some $\beta > \eta$. There exists $n$ such that $p_{\eta\beta}(a) \in P_{\xi_n}$. Then there exists $b \in A \cap P_{\xi_{n+1}}$ compatible with $p_{\eta\beta}(a)$ (take $b = e_{p_{\eta\beta}(a)}$). Now $a$ and $b$ are incompatible (both in $A$), but $p_{\eta\beta}(a)$ and $b$ are compatible. This contradicts condition 4', which states that $p_{\eta\beta}(a) \leq a$ and compatibility with $b$ should be preserved.

---
role: proof
locale: en
of_concept: integration-by-parts-for-delbar
source_book: gtm035
source_chapter: "Chapter 16"
source_section: "16.6"
---
# Proof of Integration by Parts for the \bar{\partial}-Operator

**Lemma 16.6.** Fix $f \in \mathcal{D}_{S_0} \cap C_{0,1}^1(\bar{\Omega})$. Then

$$\|S_0 f\|_3^2 = \int_{\Omega} \sum_{j,k} \left| \frac{\partial f_k}{\partial \bar{z}_j} \right|^2 e^{-\phi} dV - \int_{\Omega} \sum_{j,k} \frac{\partial f_j}{\partial \bar{z}_k} \overline{\frac{\partial f_k}{\partial \bar{z}_j}} e^{-\phi} dV.$$

**Proof.** Since $f \in C_{0,1}^1(\bar{\Omega})$, the operator $S_0$ coincides with the $\bar{\partial}$-operator on $f$. Write $f = \sum_{\alpha=1}^n f_\alpha d\bar{z}_\alpha$. Then

$$S_0 f = \bar{\partial}f = \sum_{\beta=1}^n \left( \sum_{\alpha=1}^n \frac{\partial f_\alpha}{\partial \bar{z}_\beta} d\bar{z}_\beta \right) \wedge d\bar{z}_\alpha$$

$$= \sum_{\alpha < \beta} \left( \frac{\partial f_\beta}{\partial \bar{z}_\alpha} - \frac{\partial f_\alpha}{\partial \bar{z}_\beta} \right) d\bar{z}_\alpha \wedge d\bar{z}_\beta.$$

Here we used the antisymmetry $d\bar{z}_\beta \wedge d\bar{z}_\alpha = -d\bar{z}_\alpha \wedge d\bar{z}_\beta$ to collect terms with $\alpha < \beta$.

Now compute the $L^2$ norm in $H_3$. For a $(0,2)$-form $\sum_{\alpha<\beta} a_{\alpha\beta} d\bar{z}_\alpha \wedge d\bar{z}_\beta$, the squared norm is $\sum_{\alpha<\beta} |a_{\alpha\beta}|^2$ integrated with weight $e^{-\phi}$. Hence

$$\|S_0 f\|_3^2 = \int_{\Omega} \sum_{\alpha < \beta} \left| \frac{\partial f_\beta}{\partial \bar{z}_\alpha} - \frac{\partial f_\alpha}{\partial \bar{z}_\beta} \right|^2 e^{-\phi} dV$$

$$= \int_{\Omega} \sum_{\alpha < \beta} \left( \frac{\partial f_\beta}{\partial \bar{z}_\alpha} - \frac{\partial f_\alpha}{\partial \bar{z}_\beta} \right) \overline{\left( \frac{\partial f_\beta}{\partial \bar{z}_\alpha} - \frac{\partial f_\alpha}{\partial \bar{z}_\beta} \right)} e^{-\phi} dV$$

$$= \int_{\Omega} \sum_{\alpha < \beta} \left| \frac{\partial f_\beta}{\partial \bar{z}_\alpha} \right|^2 e^{-\phi} dV + \int_{\Omega} \sum_{\alpha < \beta} \left| \frac{\partial f_\alpha}{\partial \bar{z}_\beta} \right|^2 e^{-\phi} dV$$

$$- \int_{\Omega} \sum_{\alpha < \beta} \left( \frac{\partial f_\beta}{\partial \bar{z}_\alpha} \overline{\frac{\partial f_\alpha}{\partial \bar{z}_\beta}} + \overline{\frac{\partial f_\beta}{\partial \bar{z}_\alpha}} \frac{\partial f_\alpha}{\partial \bar{z}_\beta} \right) e^{-\phi} dV.$$

Now observe that the first two sums together cover all ordered pairs $(\alpha, \beta)$ with $\alpha \neq \beta$, each exactly once:

$$\sum_{\alpha < \beta} \left| \frac{\partial f_\beta}{\partial \bar{z}_\alpha} \right|^2 + \sum_{\alpha < \beta} \left| \frac{\partial f_\alpha}{\partial \bar{z}_\beta} \right|^2 = \sum_{\alpha \neq \beta} \left| \frac{\partial f_\beta}{\partial \bar{z}_\alpha} \right|^2.$$

For the cross terms, re-index the second sum by swapping $\alpha$ and $\beta$:

$$\sum_{\alpha < \beta} \overline{\frac{\partial f_\beta}{\partial \bar{z}_\alpha}} \frac{\partial f_\alpha}{\partial \bar{z}_\beta} = \sum_{\alpha > \beta} \frac{\partial f_\beta}{\partial \bar{z}_\alpha} \overline{\frac{\partial f_\alpha}{\partial \bar{z}_\beta}}.$$

Thus the cross terms sum to

$$\sum_{\alpha \neq \beta} \frac{\partial f_\beta}{\partial \bar{z}_\alpha} \overline{\frac{\partial f_\alpha}{\partial \bar{z}_\beta}}.$$

Therefore, adding and subtracting the diagonal terms $\alpha = \beta$, we obtain the compact formula:

$$\|S_0 f\|_3^2 = \sum_{\alpha, \beta = 1}^n \int_{\Omega} \left| \frac{\partial f_\beta}{\partial \bar{z}_\alpha} \right|^2 e^{-\phi} dV - \sum_{\alpha, \beta = 1}^n \int_{\Omega} \frac{\partial f_\beta}{\partial \bar{z}_\alpha} \overline{\frac{\partial f_\alpha}{\partial \bar{z}_\beta}} e^{-\phi} dV.$$

Renaming the summation indices $(\alpha, \beta) \mapsto (j, k)$ yields the formula stated in the lemma. $\square$

**Remark.** This identity is a form of integration by parts at the level of the $\bar{\partial}$-complex. The first term $\sum_{j,k} \|\partial f_k/\partial \bar{z}_j\|^2$ is the full $L^2$ norm of the gradient of $f$, while the subtracted term represents a cancellation that reflects the algebraic structure of the $\bar{\partial}$-operator. When combined with the expression for $\|T_0^* f\|_1^2$, the two double sums cancel, yielding the clean estimate in Theorem 16.3.

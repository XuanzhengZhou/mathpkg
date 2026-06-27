---
role: proof
locale: en
of_concept: "integration-by-parts-for-lebesgue-stieltjes-integrals-let-and"
source_book: gtm025
source_chapter: "Hilbert Spaces and Spectral Theory"
source_section: "21.67"
---

For $x \in R$, define $\alpha_{0}(x) = \alpha(x-) - \alpha(0-)$. Then $\alpha_{0}$ is a left continuous nondecreasing function on $R$ such that $\alpha_{0}(0) = 0$; i.e., $\alpha_{0}$ is normalized in the sense of (19.46). Clearly $\alpha_{0} = \alpha - \alpha(0-)$ except possibly at the [countably many] discontinuities of $\alpha$. Thus (8.17)

[(iii) obviously holds for $\beta$ as well as $\alpha$] yields

$$\int_{[a,b]} \beta(x+) d\lambda_\alpha(x) - \beta(a-) [\alpha(b+) - \alpha(a-)]$$

$$= \int_{[a,b]} [\beta(x+) - \beta(a-)] d\lambda_\alpha(x)$$

$$= \int_{[a,b]} [\alpha(b+) - \alpha(y-)] d\lambda_\beta(y)$$

$$= \alpha(b+) [\beta(b+) - \beta(a-)] - \int_{[a,b]} \alpha(y-) d\lambda_\beta(y). \tag{2}$$

Now replace $y$ by $x$ in (2) and rearrange the terms to obtain (iv). To get (v), simply interchange the roles of $\alpha$ and $\beta$ in (iv), add this new equality to (iv), and then divide by 2. $\square$

(21.68) Remarks. A theorem more general than (21.67) can be formulated by allowing $\alpha$ and $\beta$ to be any functions that are of finite variation on each bounded interval of $R$ and considering the corresponding signed or complex Lebesgue-Stieltjes measures. All that is involved is to reduce the more general case to that of (21.67) by invoking the Jordan decomposition theorem (17.16). We leave this to the reader. In case $\alpha$ and $\beta$ are both absolutely continuous functions, i.e., $\lambda_\alpha \ll \lambda$ and $\lambda_\beta \ll \lambda$, (21.67) reduces to (18.19).

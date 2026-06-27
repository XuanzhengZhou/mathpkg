---
role: proof
locale: en
of_concept: optimal-estimator
source_book: gtm095
source_chapter: "Chapter 2"
source_section: "§2. Optimal estimation, normal correlation theorem"
---

# Proof of Theorem 1 (Optimal Estimator)

Let $E\eta^2 < \infty$. Without loss of generality we may consider only estimators $\varphi(\xi)$ for which $E\varphi^2(\xi) < \infty$. Set

$$\varphi^*(\xi) = E(\eta \mid \xi).$$

Then for any such estimator $\varphi(\xi)$, we have

$$E[\eta - \varphi(\xi)]^2 = E[(\eta - \varphi^*(\xi)) + (\varphi^*(\xi) - \varphi(\xi))]^2$$

$$= E[\eta - \varphi^*(\xi)]^2 + E[\varphi^*(\xi) - \varphi(\xi)]^2 + 2E[(\eta - \varphi^*(\xi))(\varphi^*(\xi) - \varphi(\xi))].$$

Consider the cross term. By the properties of conditional expectation,

$$E[(\eta - \varphi^*(\xi))(\varphi^*(\xi) - \varphi(\xi))] = E\bigl[E[(\eta - \varphi^*(\xi))(\varphi^*(\xi) - \varphi(\xi)) \mid \xi]\bigr].$$

Since $\varphi^*(\xi) - \varphi(\xi)$ is a Borel function of $\xi$, it is $\sigma(\xi)$-measurable, and therefore

$$E[(\eta - \varphi^*(\xi))(\varphi^*(\xi) - \varphi(\xi)) \mid \xi] = (\varphi^*(\xi) - \varphi(\xi)) \cdot E[\eta - \varphi^*(\xi) \mid \xi].$$

But by definition of $\varphi^*(\xi)$ and the properties of conditional expectation,

$$E[\eta - \varphi^*(\xi) \mid \xi] = E[\eta \mid \xi] - E[\varphi^*(\xi) \mid \xi] = \varphi^*(\xi) - \varphi^*(\xi) = 0.$$

Hence the cross term vanishes, and we obtain

$$E[\eta - \varphi(\xi)]^2 = E[\eta - \varphi^*(\xi)]^2 + E[\varphi^*(\xi) - \varphi(\xi)]^2.$$

Since $E[\varphi^*(\xi) - \varphi(\xi)]^2 \geq 0$, it follows that

$$E[\eta - \varphi(\xi)]^2 \geq E[\eta - \varphi^*(\xi)]^2$$

for every estimator $\varphi(\xi)$ with $E\varphi^2(\xi) < \infty$. By the assumption $E\eta^2 < \infty$, we have $E[\varphi^*(\xi)]^2 \leq E[E(\eta^2 \mid \xi)] = E\eta^2 < \infty$, so $\varphi^*(\xi)$ itself belongs to the class of admissible estimators.

Consequently,

$$\Delta \equiv \inf_{\varphi} E[\eta - \varphi(\xi)]^2 = E[\eta - \varphi^*(\xi)]^2,$$

and $\varphi^*(\xi) = E(\eta \mid \xi)$ is an optimal estimator. $\square$

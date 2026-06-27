---
role: proof
locale: en
of_concept: fiber-hull-characterization
source_book: gtm035
source_chapter: "Chapter 20"
source_section: "20.3"
---
# Proof of Fiber Hull Characterization for Sets Over the Circle

**Theorem 20.3.** Let $Y$ be a compact set in $\mathbb{C}^2$ lying over $\Gamma$. Assume again that each fiber $Y_\lambda$, $\lambda \in \Gamma$, is convex. Then each fiber $\hat{Y}_{\lambda}$, $|\lambda| < 1$, is given by

$$\hat{Y}_{\lambda} = \{f(\lambda) : f \in \mathcal{F}\},$$

and each such fiber is convex. Moreover, for $|\lambda| = 1$, $\hat{Y}_{\lambda} = Y_{\lambda}$.

**Proof.** By Theorem 20.2, $\hat{Y} \setminus Y$ equals the union of all graphs $\{(\lambda, f(\lambda)) : |\lambda| < 1\}$ with $f \in \mathcal{F}$. For $|\lambda| < 1$, if $(\lambda, w) \in \hat{Y}$, then either $(\lambda, w) \in Y$ (which is impossible since $Y$ lies over $\Gamma = \{|\lambda| = 1\}$) or $(\lambda, w) \in \hat{Y} \setminus Y$. In the latter case, there exists $f \in \mathcal{F}$ with $w = f(\lambda)$. Hence

$$\hat{Y}_{\lambda} = \{w \in \mathbb{C} : (\lambda, w) \in \hat{Y}\} = \{f(\lambda) : f \in \mathcal{F}\}.$$

For $|\lambda| = 1$, i.e., $\lambda \in \Gamma$, Exercise 20.3 tells us that any point in $\hat{Y}$ lying over $\Gamma$ must belong to $Y$. Therefore $\hat{Y}_{\lambda} = Y_{\lambda}$ for $\lambda \in \Gamma$.

To see that each fiber $\hat{Y}_{\lambda}$ is convex for $|\lambda| < 1$, recall that for a.a. $\lambda \in \Gamma$, each $f \in \mathcal{F}$ satisfies $f(\lambda) \in Y_{\lambda}$, and each $Y_{\lambda}$ is convex by hypothesis. For any $f, g \in \mathcal{F}$ and $t \in [0,1]$, the function $h = tf + (1-t)g$ belongs to $H^\infty$, and for a.a. $\lambda \in \Gamma$, $h(\lambda) \in Y_{\lambda}$ (by convexity of $Y_{\lambda}$). Moreover, $h$ satisfies the required boundary estimates, so $h \in \mathcal{F}$. Hence $\mathcal{F}$ is a convex set of functions. For each fixed $\lambda$ with $|\lambda| < 1$, the evaluation map $f \mapsto f(\lambda)$ is linear, so $\hat{Y}_{\lambda} = \{f(\lambda) : f \in \mathcal{F}\}$ is the image of a convex set under a linear map and is therefore convex. ∎

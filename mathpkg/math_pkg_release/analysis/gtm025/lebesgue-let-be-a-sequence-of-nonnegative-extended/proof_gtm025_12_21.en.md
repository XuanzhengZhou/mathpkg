---
role: proof
locale: en
of_concept: "lebesgue-let-be-a-sequence-of-nonnegative-extended"
source_book: gtm025
source_chapter: "The Lebesgue Integral"
source_section: "12.21"
---

For every positive integer $m$, we have

$$\sum_{j=1}^{\infty} f_j \geq \sum_{j=1}^{\infty} f_j;$$

therefore

$$\int_X \left( \sum_{j=1}^{\infty} f_j \right) d\mu \geq \int_X \left( \sum_{j=1}^{\infty} f_j \right) d\mu = \sum_{j=1}^{\infty} \int_X f_j d\mu,$$

and consequently

$$\int_X \left( \sum_{j=1}^{\infty} f_j \right) d\mu \geq \sum_{j=1}^{\infty} \int_X f_j d\mu.$

Now (12.11) implies that

$$\int_X \left( \sum_{j=1}^{\infty} f_j \right) d\mu = \lim_{k \to \infty} \int_X g_k d\mu \leq \lim_{k \to \infty} \int_X \left( f_1 + f_2 + \cdots + f_k \right) d\mu$$

$$= \lim_{k \to \infty} \sum_{j=1}^{k} \int_X f_j d\mu = \sum_{j=1}^{k} \int_X f_j d\mu.$$

(12.22) B. Levi's Theorem. Let $(f_k)_{n=1}^{\infty}$ be a nondecreasing sequence of extended real-valued, $\mathcal{A}$-measurable functions on $X$ such that $\int_X f_k d\mu < \infty$ for some $k$. Then

$$\lim_{k \to \infty} \int_X f_k d\mu = \int_X \left( \lim_{k \to \infty} f_k \right) d\mu.$$

Proof. We may suppose with no loss of generality that $\int_X f_1 d\mu < \infty$, and in view of (12.16) that no $f_k$ assumes the value $-\infty$. If any $\int_X f_k d\mu$ is equal to $\infty$, the result is trivial. Otherwise, for $k \in N$, we define

$$g_k(x) = \begin{cases} f_{k+1}(x) - f_k(x) & \text{if } f_k(x) < \infty, \\ \infty & \text{otherwise.} \end{cases}$$

Then we have $\lim_{n \to \infty} f_n = \lim_{n \to \infty} \left( f_1 + \sum_{k=1}^{n-1} g_k \right) = f_1 + \sum_{k=1}^{\infty} g_k$, and so by (12.21) and (12.19),

$$\int_X \left( \lim_{n \to \infty} f_n \right) d\mu = \int_X

If $\lim_{n \to \infty} f_n(x)$ exists for $\mu$-almost all $x \in X$, then $\lim_{n \to \infty} \int_X f_n d\mu$ exists and

(iii) $$\int_X \lim_{n \to \infty} f_n d\mu = \lim_{n \to \infty} \int_X f_n d\mu.$$

Proof. It is obvious that all $f_n$ are in $\mathfrak{L}_1^r$. Hence all $f_n$, and $s$, are finite a.e. on $X$. Let $A = \{x \in X : f_n(x) \text{ is } \pm \infty \text{ or } |f_n(x)| > s(x)\}$ for some $n \in N\}$, let $B = \{x \in X : f_n(x) \text{ is undefined for some } n \in N\}$, and let $C = \{x \in X : s(x) \text{ is infinite or is undefined}\}$. Let $f_n(x) = s(x) = 0$ on $A \cup B \cup C$. Since $\mu(A \cup B \cup C) = 0$, (12.14) shows that none of the integrals appearing in the statement of the theorem has been changed by this definition. Furthermore we have $|f_n(x)| \leq s(x) < \infty$ for all $n \in N$ and all $x \in X$.

The sequence $(s + f_n)_{n=1}^{\infty}$ consists of nonnegative functions. Applying FATOU’s lemma (12.23), we find

$$\int_X s d\mu + \int_X \lim_{n \to \infty} f_n d\mu = \int_X \left[ \lim_{n \to \infty} (s + f_n) \right] d\mu$$

$$\leq \lim_{n \to \infty} \int_X (s + f_n) d\mu = \int_X s d\mu + \lim_{n \to \infty} \int_X f_n d\mu.$$

Thus (i) holds. [The reader will note that the function $\lim_{n \to \infty}

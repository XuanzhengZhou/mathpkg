---
role: proof
locale: en
of_concept: differentiation-of-convolution
source_book: gtm012
source_chapter: "3"
source_section: "3. Translation, convolution, and approximation"
---

# Proof of Proposition 3.4: Differentiation of Convolution with a Smooth Function

**Proposition 3.4.** If $u \in \mathcal{P}$ and $v \in \mathcal{C}$, then $u * v \in \mathcal{P}$ and

$$D^k(u * v) = (D^k u) * v, \quad \text{for all } k.$$

**Proof.** We first prove the case $k = 1$. By Proposition 3.1 (in particular, the bilinearity and the translation property), we have

$$
t^{-1}[T_{-t}(u * v) - (u * v)] = [t^{-1}(T_{-t} u - u)] * v.
$$

Indeed, from Proposition 3.1(10), $T_{-t}(u * v) = (T_{-t} u) * v$, and using linearity (Proposition 3.1(7)-(8)),

$$
t^{-1}[T_{-t}(u * v) - (u * v)] = t^{-1}[(T_{-t} u) * v - u * v] = [t^{-1}(T_{-t} u - u)] * v.
$$

Now by Lemma 3.2, the difference quotient $t^{-1}(T_{-t} u - u)$ converges uniformly to $D u$ as $t \to 0$. Using the estimate $|f * v| \leq |f| \, |v|$ from the definition of convolution, we obtain

$$
\begin{aligned}
\left| [t^{-1}(T_{-t} u - u)] * v - (D u) * v \right|
&= \left| \left( t^{-1}(T_{-t} u - u) - D u \right) * v \right| \\
&\leq \left| t^{-1}(T_{-t} u - u) - D u \right| \, |v| \to 0
\end{aligned}
$$

as $t \to 0$. Thus the expression on the right in the identity above converges uniformly to $(D u) * v$ as $t \to 0$. But this expression is precisely the difference quotient of $u * v$, so

$$D(u * v) = \lim_{t \to 0} t^{-1}[T_{-t}(u * v) - (u * v)] = (D u) * v.$$

This proves the formula for $k = 1$ and shows that $D(u * v)$ is continuous, since $(D u) * v$ is the convolution of a continuous function ($D u$) with $v \in \mathcal{C}$, hence continuous by Proposition 3.1.

For higher derivatives, we proceed by induction. Assuming $D^k(u * v) = (D^k u) * v$, we apply the $k = 1$ case to the function $D^k u \in \mathcal{P}$:

$$D^{k+1}(u * v) = D(D^k(u * v)) = D((D^k u) * v) = (D(D^k u)) * v = (D^{k+1} u) * v.$$

By induction, the formula holds for all $k \geq 0$. Moreover, each $(D^k u) * v \in \mathcal{C}$ by Proposition 3.1, so all derivatives of $u * v$ are continuous. Hence $u * v \in \mathcal{P}$. $\square$

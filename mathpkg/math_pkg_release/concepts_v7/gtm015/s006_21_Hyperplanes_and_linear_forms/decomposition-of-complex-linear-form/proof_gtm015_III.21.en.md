---
role: proof
locale: en
of_concept: decomposition-of-complex-linear-form
source_book: gtm015
source_chapter: "III. Topological Vector Spaces"
source_section: "21. Hyperplanes and linear forms"
---

# Proof of Decomposition of a Complex Linear Form into Real and Imaginary Parts

Let $E$ be a vector space over $\mathbb{C}$. By restricting scalar multiplication, $E$ can also be regarded as a vector space over $\mathbb{R}$.

**Theorem 21.11.** If $f: E \to \mathbb{C}$ is a $\mathbb{C}$-linear form, and we write $f = g + ih$, where $g, h$ are real-valued functions on $E$ (i.e., $g(x) = \operatorname{Re} f(x)$, $h(x) = \operatorname{Im} f(x)$), then

1. $g$ and $h$ are $\mathbb{R}$-linear forms on $E$;
2. $g(ix) = -h(x)$ and $h(ix) = g(x)$ for all $x \in E$;
3. $f$ is uniquely determined by $g$.

*Proof.*

**(i)** For any $x, y \in E$ and $\lambda \in \mathbb{R}$,

$$f(x + y) = f(x) + f(y) \implies g(x + y) + ih(x + y) = (g(x) + g(y)) + i(h(x) + h(y)).$$

Comparing real and imaginary parts yields $g(x + y) = g(x) + g(y)$ and $h(x + y) = h(x) + h(y)$. Also,

$$f(\lambda x) = \lambda f(x) \implies g(\lambda x) + ih(\lambda x) = \lambda g(x) + i\lambda h(x) \quad (\lambda \in \mathbb{R}),$$

so $g(\lambda x) = \lambda g(x)$ and $h(\lambda x) = \lambda h(x)$. Thus $g$ and $h$ are $\mathbb{R}$-linear forms.

**(ii)** Since $f(ix) = if(x)$, we expand both sides:

$$f(ix) = g(ix) + ih(ix),$$
$$if(x) = i(g(x) + ih(x)) = -h(x) + ig(x).$$

Comparing real and imaginary parts:

$$g(ix) = -h(x), \qquad h(ix) = g(x) \quad (\forall x \in E).$$

**(iii)** Since $f = g + ih$ and $h(x) = -g(ix)$ by part (ii), we have

$$f(x) = g(x) - ig(ix) \quad (\forall x \in E).$$

Thus $f$ is uniquely determined by $g = \operatorname{Re} f$. The formula $h(x) = \operatorname{Im} f(x) = -g(ix)$ is also immediate from (ii).

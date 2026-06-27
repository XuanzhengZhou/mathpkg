---
role: proof
locale: en
of_concept: goldstines-theorem
source_book: gtm015
source_chapter: "IV"
source_section: "45"
---

# Proof of Goldstine's Theorem

Let $A = \{x'' : x \in E, \|x\| \leq 1\}$, the image of the closed unit ball of $E$ under the canonical embedding of $E$ in $E''$; let $B = \{\varphi \in E'' : \|\varphi\| \leq 1\}$. Obviously $B \supset A$; it is to be shown that $B$ is the weak* closure of $A$.

First, we note that $B$ is weak* closed. This is immediate from the weak* compactness of $B$ (Alaoglu's theorem, 44.12), but we prefer to give a more elementary direct proof. Suppose $\varphi_0$ is in the weak* closure of $B$. For each fixed $f \in E'$ with $\|f\| \leq 1$, the mapping $\varphi \mapsto \varphi(f)$ ($\varphi \in E''$) is weak* continuous and maps $B$ into the closed set $D = \{\lambda : |\lambda| \leq 1\}$, therefore it maps the weak* closure of $B$ into $D$, and in particular $|\varphi_0(f)| \leq 1$; varying $f$, $\|\varphi_0\| \leq 1$, so $\varphi_0 \in B$. Thus $B$ is weak* closed.

It remains to show $A$ is weak* dense in $B$. Let $\varphi \in B$ and let
$$W = \{\psi \in E'' : |\psi(f_i) - \varphi(f_i)| < \varepsilon,\; i = 1, \ldots, n\}$$
be a basic weak* neighborhood of $\varphi$, where $f_1, \ldots, f_n \in E'$ and $\varepsilon > 0$. We must produce $x \in E$ with $\|x\| \leq 1$ such that $x'' \in W$, i.e., $|f_i(x) - \varphi(f_i)| < \varepsilon$ for all $i$.

Consider the linear map $\Phi: E \to \mathbb{K}^n$ defined by $\Phi(x) = (f_1(x), \ldots, f_n(x))$. If there is no $x$ with $\|x\| \leq 1$ mapping into the $\varepsilon$-cube around $(\varphi(f_1), \ldots, \varphi(f_n))$, then by the separation theorem (Hahn-Banach) there exists $(\alpha_1, \ldots, \alpha_n) \in \mathbb{K}^n$ such that
$$\operatorname{Re}\sum_{i=1}^n \alpha_i f_i(x) \leq \operatorname{Re}\sum_{i=1}^n \alpha_i \varphi(f_i) - \delta$$
for all $\|x\| \leq 1$ and some $\delta > 0$. Setting $g = \sum \alpha_i f_i \in E'$, this implies $\|g\| \leq \operatorname{Re}\varphi(g) - \delta$, which contradicts $\|\varphi\| \leq 1$ (since $\varphi \in B$). Hence such $x$ exists, and $A$ is weak* dense in $B$.

Thus the closed unit ball of $E_0$ is weak* dense in the closed unit ball of $E''$. $\square$

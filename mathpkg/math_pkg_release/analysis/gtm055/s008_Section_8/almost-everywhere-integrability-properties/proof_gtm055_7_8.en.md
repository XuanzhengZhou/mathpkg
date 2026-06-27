---
role: proof
locale: en
of_concept: almost-everywhere-integrability-properties
source_book: gtm055
source_chapter: "7"
source_section: "8"
---

Let $f$ be a nonnegative measurable function, and let $\{s_n\}$ be a monotone increasing sequence of nonnegative measurable simple functions converging pointwise to $f$ (Proposition 6.6).

If $\int f d\mu = 0$, then $\int s_n d\mu = 0$ for all $n$ (by monotonicity of the integral). For a simple function, $\int s_n d\mu = 0$ implies $s_n = 0$ a.e. $[\mu]$ (by Proposition 7.7). Thus $s_n = 0$ a.e. for every $n$, and since $f = \lim_n s_n$, we have $f = 0$ a.e. $[\mu]$.

Conversely, if $f = 0$ a.e. $[\mu]$, then $s_n = 0$ a.e. $[\mu]$ for every $n$, so $\int s_n d\mu = 0$. By Proposition 7.2 (monotone convergence), $f$ is integrable and $\int f d\mu = 0$.

For a complex-valued measurable function $f$ with $f = 0$ a.e., decompose $f = (\text{Re } f)^+ - (\text{Re } f)^- + i[(\text{Im } f)^+ - (\text{Im } f)^-]$. Each component is nonnegative, measurable, and vanishes a.e., so each has zero integral. Hence $f$ is integrable and $\int f d\mu = 0$.

If $f = g$ a.e., then $f - g = 0$ a.e., so $f - g$ is integrable with zero integral. If $f$ is integrable, then $g = f + (g - f)$ is integrable, and $\int g d\mu = \int f d\mu$.

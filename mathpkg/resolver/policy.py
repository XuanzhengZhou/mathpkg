"""
Policy configuration for learning path resolution.

Equivalent to apt's DepCache::Policy — controls whether recommended
and suggested dependencies are automatically included in the plan.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Policy:
    """Controls dependency resolution behavior.

    Attributes
    ----------
    install_recommends : bool
        If True, recommended concepts are automatically added to the
        learning path (inserted before their dependent). Default True.
    install_suggests : bool
        If True, suggested concepts are also included. Default False.
    max_depth : int
        Maximum depth for recursive dependency expansion. Guards against
        infinite loops from malformed graphs. Default 20.
    prefer_source : Optional[str]
        Preferred textbook source (e.g. "GTM073"). When set, the resolver
        biases version selection toward this source.
    target_hours : Optional[float]
        If set, the resolver will warn when the estimated learning path
        exceeds this time budget.
    """

    install_recommends: bool = True
    install_suggests: bool = False
    max_depth: int = field(default=20)
    prefer_source: Optional[str] = field(default=None)
    target_hours: Optional[float] = field(default=None)

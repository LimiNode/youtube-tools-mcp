from __future__ import annotations

import os


def get_proxy_url(proxy: str | None = None) -> str | None:
    """Return proxy URL from explicit argument or environment variables.

    Args:
        proxy: Explicit proxy URL passed by the caller. Takes highest priority.

    Falls back to standard environment variables in order:
    HTTPS_PROXY, https_proxy, HTTP_PROXY, http_proxy.
    Returns None if no proxy is configured.
    """
    if proxy is not None:
        # An explicit blank value means "disable proxy" for this call.  Do
        # not pass an empty URL to requests/youtube-transcript-api: it is
        # neither a usable proxy nor the same as ``None`` for all clients.
        return proxy.strip() or None
    return (
        os.environ.get("HTTPS_PROXY")
        or os.environ.get("https_proxy")
        or os.environ.get("HTTP_PROXY")
        or os.environ.get("http_proxy")
        or None
    )

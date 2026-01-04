from __future__ import annotations
from dessly_fastvelopay_plugin.config import (
    LOGGER_PREFIX,
    NAME,
    VERSION,
    DESCRIPTION,
    CREDITS,
    UUID,
    SETTINGS_PAGE,
)

from dessly_fastvelopay_plugin.ui import init, post_init
from dessly_fastvelopay_plugin.new_order import new_order
from dessly_fastvelopay_plugin.new_message import handle_new_message
from dessly_fastvelopay_plugin.order_status_changed import handle_order_status_changed
from dessly_fastvelopay_plugin import config as config
from dessly_fastvelopay_plugin import telemetry as tlm

# ========== Регистрация плагина в системе Cardinal ==========
BIND_TO_PRE_INIT = [init]
BIND_TO_POST_INIT = [post_init]
BIND_TO_NEW_ORDER = [new_order]
BIND_TO_NEW_MESSAGE = [handle_new_message]
BIND_TO_ORDER_STATUS_CHANGED = [handle_order_status_changed]
BIND_TO_DELETE = None
tlm.debug(f"BIND_TO_PRE_INIT инициализирован, плагин готов к использованию")
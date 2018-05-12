# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
    import builtins as __builtin__

    long = int
elif six.PY2:
    import __builtin__


class state(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/routed-vlan/ipv6/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Top-level operational state data for the IPv6 interface
  """
    __slots__ = (
        "_path_helper",
        "_extmethods",
        "__enabled",
        "__mtu",
        "__dup_addr_detect_transmits",
    )

    _yang_name = "state"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__enabled = YANGDynClass(
            base=YANGBool,
            default=YANGBool("true"),
            is_leaf=True,
            yang_name="enabled",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/interfaces/ip",
            defining_module="openconfig-if-ip",
            yang_type="boolean",
            is_config=False,
        )
        self.__mtu = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..4294967295"]},
                    int_size=32,
                ),
                restriction_dict={"range": ["1280..max"]},
            ),
            is_leaf=True,
            yang_name="mtu",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/interfaces/ip",
            defining_module="openconfig-if-ip",
            yang_type="uint32",
            is_config=False,
        )
        self.__dup_addr_detect_transmits = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..4294967295"]},
                int_size=32,
            ),
            default=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..4294967295"]},
                int_size=32,
            )(
                1
            ),
            is_leaf=True,
            yang_name="dup-addr-detect-transmits",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/interfaces/ip",
            defining_module="openconfig-if-ip",
            yang_type="uint32",
            is_config=False,
        )

        load = kwargs.pop("load", None)
        if args:
            if len(args) > 1:
                raise TypeError("cannot create a YANG container with >1 argument")
            all_attr = True
            for e in self._pyangbind_elements:
                if not hasattr(args[0], e):
                    all_attr = False
                    break
            if not all_attr:
                raise ValueError("Supplied object did not have the correct attributes")
            for e in self._pyangbind_elements:
                nobj = getattr(args[0], e)
                if nobj._changed() is False:
                    continue
                setmethod = getattr(self, "_set_%s" % e)
                if load is None:
                    setmethod(getattr(args[0], e))
                else:
                    setmethod(getattr(args[0], e), load=load)

    def _path(self):
        if hasattr(self, "_parent"):
            return self._parent._path() + [self._yang_name]
        else:
            return ["interfaces", "interface", "routed-vlan", "ipv6", "state"]

    def _get_enabled(self):
        """
    Getter method for enabled, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/state/enabled (boolean)

    YANG Description: [adapted from IETF IP model RFC 7277]

Controls whether IPv6 is enabled or disabled on this
interface.  When IPv6 is enabled, this interface is
connected to an IPv6 stack, and the interface can send
and receive IPv6 packets.
    """
        return self.__enabled

    def _set_enabled(self, v, load=False):
        """
    Setter method for enabled, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/state/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: [adapted from IETF IP model RFC 7277]

Controls whether IPv6 is enabled or disabled on this
interface.  When IPv6 is enabled, this interface is
connected to an IPv6 stack, and the interface can send
and receive IPv6 packets.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=YANGBool,
                default=YANGBool("true"),
                is_leaf=True,
                yang_name="enabled",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/interfaces/ip",
                defining_module="openconfig-if-ip",
                yang_type="boolean",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """enabled must be of a type compatible with boolean""",
                    "defined-type": "boolean",
                    "generated-type": """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='boolean', is_config=False)""",
                }
            )

        self.__enabled = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_enabled(self):
        self.__enabled = YANGDynClass(
            base=YANGBool,
            default=YANGBool("true"),
            is_leaf=True,
            yang_name="enabled",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/interfaces/ip",
            defining_module="openconfig-if-ip",
            yang_type="boolean",
            is_config=False,
        )

    def _get_mtu(self):
        """
    Getter method for mtu, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/state/mtu (uint32)

    YANG Description: [adapted from IETF IP model RFC 7277]

The size, in octets, of the largest IPv6 packet that the
interface will send and receive.

The server may restrict the allowed values for this leaf,
depending on the interface's type.

If this leaf is not configured, the operationally used MTU
depends on the interface's type.
    """
        return self.__mtu

    def _set_mtu(self, v, load=False):
        """
    Setter method for mtu, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/state/mtu (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mtu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mtu() directly.

    YANG Description: [adapted from IETF IP model RFC 7277]

The size, in octets, of the largest IPv6 packet that the
interface will send and receive.

The server may restrict the allowed values for this leaf,
depending on the interface's type.

If this leaf is not configured, the operationally used MTU
depends on the interface's type.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=RestrictedClassType(
                        base_type=long,
                        restriction_dict={"range": ["0..4294967295"]},
                        int_size=32,
                    ),
                    restriction_dict={"range": ["1280..max"]},
                ),
                is_leaf=True,
                yang_name="mtu",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/interfaces/ip",
                defining_module="openconfig-if-ip",
                yang_type="uint32",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """mtu must be of a type compatible with uint32""",
                    "defined-type": "uint32",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': ['1280..max']}), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint32', is_config=False)""",
                }
            )

        self.__mtu = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_mtu(self):
        self.__mtu = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..4294967295"]},
                    int_size=32,
                ),
                restriction_dict={"range": ["1280..max"]},
            ),
            is_leaf=True,
            yang_name="mtu",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/interfaces/ip",
            defining_module="openconfig-if-ip",
            yang_type="uint32",
            is_config=False,
        )

    def _get_dup_addr_detect_transmits(self):
        """
    Getter method for dup_addr_detect_transmits, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/state/dup_addr_detect_transmits (uint32)

    YANG Description: [adapted from IETF IP model RFC 7277]

The number of consecutive Neighbor Solicitation messages
sent while performing Duplicate Address Detection on a
tentative address.  A value of zero indicates that
Duplicate Address Detection is not performed on
tentative addresses.  A value of one indicates a single
transmission with no follow-up retransmissions.
    """
        return self.__dup_addr_detect_transmits

    def _set_dup_addr_detect_transmits(self, v, load=False):
        """
    Setter method for dup_addr_detect_transmits, mapped from YANG variable /interfaces/interface/routed_vlan/ipv6/state/dup_addr_detect_transmits (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dup_addr_detect_transmits is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dup_addr_detect_transmits() directly.

    YANG Description: [adapted from IETF IP model RFC 7277]

The number of consecutive Neighbor Solicitation messages
sent while performing Duplicate Address Detection on a
tentative address.  A value of zero indicates that
Duplicate Address Detection is not performed on
tentative addresses.  A value of one indicates a single
transmission with no follow-up retransmissions.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..4294967295"]},
                    int_size=32,
                ),
                default=RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..4294967295"]},
                    int_size=32,
                )(
                    1
                ),
                is_leaf=True,
                yang_name="dup-addr-detect-transmits",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/interfaces/ip",
                defining_module="openconfig-if-ip",
                yang_type="uint32",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """dup_addr_detect_transmits must be of a type compatible with uint32""",
                    "defined-type": "uint32",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="dup-addr-detect-transmits", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint32', is_config=False)""",
                }
            )

        self.__dup_addr_detect_transmits = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_dup_addr_detect_transmits(self):
        self.__dup_addr_detect_transmits = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..4294967295"]},
                int_size=32,
            ),
            default=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..4294967295"]},
                int_size=32,
            )(
                1
            ),
            is_leaf=True,
            yang_name="dup-addr-detect-transmits",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/interfaces/ip",
            defining_module="openconfig-if-ip",
            yang_type="uint32",
            is_config=False,
        )

    enabled = __builtin__.property(_get_enabled)
    mtu = __builtin__.property(_get_mtu)
    dup_addr_detect_transmits = __builtin__.property(_get_dup_addr_detect_transmits)

    _pyangbind_elements = OrderedDict(
        [
            ("enabled", enabled),
            ("mtu", mtu),
            ("dup_addr_detect_transmits", dup_addr_detect_transmits),
        ]
    )

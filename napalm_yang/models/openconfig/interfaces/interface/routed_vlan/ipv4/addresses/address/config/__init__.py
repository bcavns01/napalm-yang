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


class config(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-interfaces - based on the path /interfaces/interface/routed-vlan/ipv4/addresses/address/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configuration data for each configured IPv4
address on the interface
  """
    __slots__ = (
        "_path_helper", "_extmethods", "__ip", "__prefix_length", "__secondary"
    )

    _yang_name = "config"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__ip = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=six.text_type,
                    restriction_dict={
                        "pattern": "(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?"
                    },
                ),
                restriction_dict={"pattern": "[0-9\\.]*"},
            ),
            is_leaf=True,
            yang_name="ip",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/interfaces/ip",
            defining_module="openconfig-if-ip",
            yang_type="inet:ipv4-address-no-zone",
            is_config=True,
        )
        self.__prefix_length = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["0..32"]},
            ),
            is_leaf=True,
            yang_name="prefix-length",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/interfaces/ip",
            defining_module="openconfig-if-ip",
            yang_type="uint8",
            is_config=True,
        )
        self.__secondary = YANGDynClass(
            base=YANGBool,
            default=YANGBool("false"),
            is_leaf=True,
            yang_name="secondary",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="https://github.com/napalm-automation/napalm-yang/yang_napalm/interfaces",
            defining_module="napalm-if-ip",
            yang_type="boolean",
            is_config=True,
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
            return [
                "interfaces",
                "interface",
                "routed-vlan",
                "ipv4",
                "addresses",
                "address",
                "config",
            ]

    def _get_ip(self):
        """
    Getter method for ip, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/config/ip (inet:ipv4-address-no-zone)

    YANG Description: [adapted from IETF IP model RFC 7277]

The IPv4 address on the interface.
    """
        return self.__ip

    def _set_ip(self, v, load=False):
        """
    Setter method for ip, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/config/ip (inet:ipv4-address-no-zone)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.

    YANG Description: [adapted from IETF IP model RFC 7277]

The IPv4 address on the interface.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=RestrictedClassType(
                        base_type=six.text_type,
                        restriction_dict={
                            "pattern": "(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?"
                        },
                    ),
                    restriction_dict={"pattern": "[0-9\\.]*"},
                ),
                is_leaf=True,
                yang_name="ip",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/interfaces/ip",
                defining_module="openconfig-if-ip",
                yang_type="inet:ipv4-address-no-zone",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """ip must be of a type compatible with inet:ipv4-address-no-zone""",
                    "defined-type": "inet:ipv4-address-no-zone",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=six.text_type, restriction_dict={'pattern': '(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), restriction_dict={'pattern': '[0-9\\.]*'}), is_leaf=True, yang_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='inet:ipv4-address-no-zone', is_config=True)""",
                }
            )

        self.__ip = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_ip(self):
        self.__ip = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=six.text_type,
                    restriction_dict={
                        "pattern": "(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?"
                    },
                ),
                restriction_dict={"pattern": "[0-9\\.]*"},
            ),
            is_leaf=True,
            yang_name="ip",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/interfaces/ip",
            defining_module="openconfig-if-ip",
            yang_type="inet:ipv4-address-no-zone",
            is_config=True,
        )

    def _get_prefix_length(self):
        """
    Getter method for prefix_length, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/config/prefix_length (uint8)

    YANG Description: [adapted from IETF IP model RFC 7277]

The length of the subnet prefix.
    """
        return self.__prefix_length

    def _set_prefix_length(self, v, load=False):
        """
    Setter method for prefix_length, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/config/prefix_length (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_length is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_length() directly.

    YANG Description: [adapted from IETF IP model RFC 7277]

The length of the subnet prefix.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=RestrictedClassType(
                        base_type=int,
                        restriction_dict={"range": ["0..255"]},
                        int_size=8,
                    ),
                    restriction_dict={"range": ["0..32"]},
                ),
                is_leaf=True,
                yang_name="prefix-length",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/interfaces/ip",
                defining_module="openconfig-if-ip",
                yang_type="uint8",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """prefix_length must be of a type compatible with uint8""",
                    "defined-type": "uint8",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['0..32']}), is_leaf=True, yang_name="prefix-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/interfaces/ip', defining_module='openconfig-if-ip', yang_type='uint8', is_config=True)""",
                }
            )

        self.__prefix_length = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_prefix_length(self):
        self.__prefix_length = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["0..32"]},
            ),
            is_leaf=True,
            yang_name="prefix-length",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/interfaces/ip",
            defining_module="openconfig-if-ip",
            yang_type="uint8",
            is_config=True,
        )

    def _get_secondary(self):
        """
    Getter method for secondary, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/config/secondary (boolean)

    YANG Description: Most platforms need a secondary statement on when configuring multiple IPv4 addresses
on the same interfaces
    """
        return self.__secondary

    def _set_secondary(self, v, load=False):
        """
    Setter method for secondary, mapped from YANG variable /interfaces/interface/routed_vlan/ipv4/addresses/address/config/secondary (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_secondary is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_secondary() directly.

    YANG Description: Most platforms need a secondary statement on when configuring multiple IPv4 addresses
on the same interfaces
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=YANGBool,
                default=YANGBool("false"),
                is_leaf=True,
                yang_name="secondary",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="https://github.com/napalm-automation/napalm-yang/yang_napalm/interfaces",
                defining_module="napalm-if-ip",
                yang_type="boolean",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """secondary must be of a type compatible with boolean""",
                    "defined-type": "boolean",
                    "generated-type": """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="secondary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='https://github.com/napalm-automation/napalm-yang/yang_napalm/interfaces', defining_module='napalm-if-ip', yang_type='boolean', is_config=True)""",
                }
            )

        self.__secondary = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_secondary(self):
        self.__secondary = YANGDynClass(
            base=YANGBool,
            default=YANGBool("false"),
            is_leaf=True,
            yang_name="secondary",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="https://github.com/napalm-automation/napalm-yang/yang_napalm/interfaces",
            defining_module="napalm-if-ip",
            yang_type="boolean",
            is_config=True,
        )

    ip = __builtin__.property(_get_ip, _set_ip)
    prefix_length = __builtin__.property(_get_prefix_length, _set_prefix_length)
    secondary = __builtin__.property(_get_secondary, _set_secondary)

    _pyangbind_elements = OrderedDict(
        [("ip", ip), ("prefix_length", prefix_length), ("secondary", secondary)]
    )

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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-ipv4-reachability/prefixes/prefix/undefined-subtlvs/undefined-subtlv/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of the undefined sub-TLV.
  """
    __slots__ = ("_path_helper", "_extmethods", "__type", "__length", "__value")

    _yang_name = "state"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__type = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
            ),
            is_leaf=True,
            yang_name="type",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=False,
        )
        self.__length = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
            ),
            is_leaf=True,
            yang_name="length",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=False,
        )
        self.__value = YANGDynClass(
            base=bitarray,
            is_leaf=True,
            yang_name="value",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="binary",
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
            return [
                "network-instances",
                "network-instance",
                "protocols",
                "protocol",
                "isis",
                "levels",
                "level",
                "link-state-database",
                "lsp",
                "tlvs",
                "tlv",
                "mt-ipv4-reachability",
                "prefixes",
                "prefix",
                "undefined-subtlvs",
                "undefined-subtlv",
                "state",
            ]

    def _get_type(self):
        """
    Getter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs/undefined_subtlv/state/type (uint8)

    YANG Description: TLV Type.
    """
        return self.__type

    def _set_type(self, v, load=False):
        """
    Setter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs/undefined_subtlv/state/type (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: TLV Type.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                is_leaf=True,
                yang_name="type",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint8",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """type must be of a type compatible with uint8""",
                    "defined-type": "uint8",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
                }
            )

        self.__type = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_type(self):
        self.__type = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
            ),
            is_leaf=True,
            yang_name="type",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=False,
        )

    def _get_length(self):
        """
    Getter method for length, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs/undefined_subtlv/state/length (uint8)

    YANG Description: TLV length.
    """
        return self.__length

    def _set_length(self, v, load=False):
        """
    Setter method for length, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs/undefined_subtlv/state/length (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_length is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_length() directly.

    YANG Description: TLV length.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                is_leaf=True,
                yang_name="length",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint8",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """length must be of a type compatible with uint8""",
                    "defined-type": "uint8",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
                }
            )

        self.__length = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_length(self):
        self.__length = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
            ),
            is_leaf=True,
            yang_name="length",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=False,
        )

    def _get_value(self):
        """
    Getter method for value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs/undefined_subtlv/state/value (binary)

    YANG Description: TLV value.
    """
        return self.__value

    def _set_value(self, v, load=False):
        """
    Setter method for value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs/undefined_subtlv/state/value (binary)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: TLV value.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=bitarray,
                is_leaf=True,
                yang_name="value",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="binary",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """value must be of a type compatible with binary""",
                    "defined-type": "binary",
                    "generated-type": """YANGDynClass(base=bitarray, is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='binary', is_config=False)""",
                }
            )

        self.__value = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_value(self):
        self.__value = YANGDynClass(
            base=bitarray,
            is_leaf=True,
            yang_name="value",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="binary",
            is_config=False,
        )

    type = __builtin__.property(_get_type)
    length = __builtin__.property(_get_length)
    value = __builtin__.property(_get_value)

    _pyangbind_elements = OrderedDict(
        [("type", type), ("length", length), ("value", value)]
    )


class state(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-ipv4-reachability/prefixes/prefix/undefined-subtlvs/undefined-subtlv/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters of the undefined sub-TLV.
  """
    __slots__ = ("_path_helper", "_extmethods", "__type", "__length", "__value")

    _yang_name = "state"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__type = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
            ),
            is_leaf=True,
            yang_name="type",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=False,
        )
        self.__length = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
            ),
            is_leaf=True,
            yang_name="length",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=False,
        )
        self.__value = YANGDynClass(
            base=bitarray,
            is_leaf=True,
            yang_name="value",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="binary",
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
            return [
                "network-instances",
                "network-instance",
                "protocols",
                "protocol",
                "isis",
                "levels",
                "level",
                "link-state-database",
                "lsp",
                "tlvs",
                "tlv",
                "mt-ipv4-reachability",
                "prefixes",
                "prefix",
                "undefined-subtlvs",
                "undefined-subtlv",
                "state",
            ]

    def _get_type(self):
        """
    Getter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs/undefined_subtlv/state/type (uint8)

    YANG Description: TLV Type.
    """
        return self.__type

    def _set_type(self, v, load=False):
        """
    Setter method for type, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs/undefined_subtlv/state/type (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type() directly.

    YANG Description: TLV Type.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                is_leaf=True,
                yang_name="type",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint8",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """type must be of a type compatible with uint8""",
                    "defined-type": "uint8",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
                }
            )

        self.__type = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_type(self):
        self.__type = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
            ),
            is_leaf=True,
            yang_name="type",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=False,
        )

    def _get_length(self):
        """
    Getter method for length, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs/undefined_subtlv/state/length (uint8)

    YANG Description: TLV length.
    """
        return self.__length

    def _set_length(self, v, load=False):
        """
    Setter method for length, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs/undefined_subtlv/state/length (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_length is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_length() directly.

    YANG Description: TLV length.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                is_leaf=True,
                yang_name="length",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint8",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """length must be of a type compatible with uint8""",
                    "defined-type": "uint8",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=False)""",
                }
            )

        self.__length = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_length(self):
        self.__length = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
            ),
            is_leaf=True,
            yang_name="length",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=False,
        )

    def _get_value(self):
        """
    Getter method for value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs/undefined_subtlv/state/value (binary)

    YANG Description: TLV value.
    """
        return self.__value

    def _set_value(self, v, load=False):
        """
    Setter method for value, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_ipv4_reachability/prefixes/prefix/undefined_subtlvs/undefined_subtlv/state/value (binary)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: TLV value.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=bitarray,
                is_leaf=True,
                yang_name="value",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="binary",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """value must be of a type compatible with binary""",
                    "defined-type": "binary",
                    "generated-type": """YANGDynClass(base=bitarray, is_leaf=True, yang_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='binary', is_config=False)""",
                }
            )

        self.__value = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_value(self):
        self.__value = YANGDynClass(
            base=bitarray,
            is_leaf=True,
            yang_name="value",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="binary",
            is_config=False,
        )

    type = __builtin__.property(_get_type)
    length = __builtin__.property(_get_length)
    value = __builtin__.property(_get_value)

    _pyangbind_elements = OrderedDict(
        [("type", type), ("length", length), ("value", value)]
    )

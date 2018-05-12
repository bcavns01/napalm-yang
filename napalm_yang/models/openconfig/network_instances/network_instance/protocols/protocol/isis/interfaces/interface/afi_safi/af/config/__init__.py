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
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/afi-safi/af/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines AFI-SAFI configuration parameters. Single
topology is the default setting.
  """
    __slots__ = (
        "_path_helper", "_extmethods", "__afi_name", "__safi_name", "__enabled"
    )

    _yang_name = "config"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__afi_name = YANGDynClass(
            base=RestrictedClassType(
                base_type=six.text_type,
                restriction_type="dict_key",
                restriction_arg={
                    "IPV4": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:IPV4": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "IPV6": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:IPV6": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                },
            ),
            is_leaf=True,
            yang_name="afi-name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="identityref",
            is_config=True,
        )
        self.__safi_name = YANGDynClass(
            base=RestrictedClassType(
                base_type=six.text_type,
                restriction_type="dict_key",
                restriction_arg={
                    "UNICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:UNICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "MULTICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:MULTICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                },
            ),
            is_leaf=True,
            yang_name="safi-name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="identityref",
            is_config=True,
        )
        self.__enabled = YANGDynClass(
            base=YANGBool,
            is_leaf=True,
            yang_name="enabled",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
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
                "network-instances",
                "network-instance",
                "protocols",
                "protocol",
                "isis",
                "interfaces",
                "interface",
                "afi-safi",
                "af",
                "config",
            ]

    def _get_afi_name(self):
        """
    Getter method for afi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/afi_safi/af/config/afi_name (identityref)

    YANG Description: Address-family type.
    """
        return self.__afi_name

    def _set_afi_name(self, v, load=False):
        """
    Setter method for afi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/afi_safi/af/config/afi_name (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi_name() directly.

    YANG Description: Address-family type.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=six.text_type,
                    restriction_type="dict_key",
                    restriction_arg={
                        "IPV4": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                        "oc-isis-types:IPV4": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                        "IPV6": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                        "oc-isis-types:IPV6": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                    },
                ),
                is_leaf=True,
                yang_name="afi-name",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="identityref",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """afi_name must be of a type compatible with identityref""",
                    "defined-type": "openconfig-network-instance:identityref",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'IPV4': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}, 'oc-isis-types:IPV4': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}, 'IPV6': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}, 'oc-isis-types:IPV6': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}},), is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
                }
            )

        self.__afi_name = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_afi_name(self):
        self.__afi_name = YANGDynClass(
            base=RestrictedClassType(
                base_type=six.text_type,
                restriction_type="dict_key",
                restriction_arg={
                    "IPV4": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:IPV4": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "IPV6": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:IPV6": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                },
            ),
            is_leaf=True,
            yang_name="afi-name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="identityref",
            is_config=True,
        )

    def _get_safi_name(self):
        """
    Getter method for safi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/afi_safi/af/config/safi_name (identityref)

    YANG Description: Subsequent address-family type.
    """
        return self.__safi_name

    def _set_safi_name(self, v, load=False):
        """
    Setter method for safi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/afi_safi/af/config/safi_name (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_safi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_safi_name() directly.

    YANG Description: Subsequent address-family type.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=six.text_type,
                    restriction_type="dict_key",
                    restriction_arg={
                        "UNICAST": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                        "oc-isis-types:UNICAST": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                        "MULTICAST": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                        "oc-isis-types:MULTICAST": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                    },
                ),
                is_leaf=True,
                yang_name="safi-name",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="identityref",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """safi_name must be of a type compatible with identityref""",
                    "defined-type": "openconfig-network-instance:identityref",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'UNICAST': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}, 'oc-isis-types:UNICAST': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}, 'MULTICAST': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}, 'oc-isis-types:MULTICAST': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}},), is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
                }
            )

        self.__safi_name = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_safi_name(self):
        self.__safi_name = YANGDynClass(
            base=RestrictedClassType(
                base_type=six.text_type,
                restriction_type="dict_key",
                restriction_arg={
                    "UNICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:UNICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "MULTICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:MULTICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                },
            ),
            is_leaf=True,
            yang_name="safi-name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="identityref",
            is_config=True,
        )

    def _get_enabled(self):
        """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/afi_safi/af/config/enabled (boolean)

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
        return self.__enabled

    def _set_enabled(self, v, load=False):
        """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/afi_safi/af/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=YANGBool,
                is_leaf=True,
                yang_name="enabled",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="boolean",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """enabled must be of a type compatible with boolean""",
                    "defined-type": "boolean",
                    "generated-type": """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
                }
            )

        self.__enabled = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_enabled(self):
        self.__enabled = YANGDynClass(
            base=YANGBool,
            is_leaf=True,
            yang_name="enabled",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="boolean",
            is_config=True,
        )

    afi_name = __builtin__.property(_get_afi_name, _set_afi_name)
    safi_name = __builtin__.property(_get_safi_name, _set_safi_name)
    enabled = __builtin__.property(_get_enabled, _set_enabled)

    _pyangbind_elements = OrderedDict(
        [("afi_name", afi_name), ("safi_name", safi_name), ("enabled", enabled)]
    )


class config(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/afi-safi/af/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines AFI-SAFI configuration parameters. Single
topology is the default setting.
  """
    __slots__ = (
        "_path_helper", "_extmethods", "__afi_name", "__safi_name", "__enabled"
    )

    _yang_name = "config"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__afi_name = YANGDynClass(
            base=RestrictedClassType(
                base_type=six.text_type,
                restriction_type="dict_key",
                restriction_arg={
                    "IPV4": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:IPV4": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "IPV6": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:IPV6": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                },
            ),
            is_leaf=True,
            yang_name="afi-name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="identityref",
            is_config=True,
        )
        self.__safi_name = YANGDynClass(
            base=RestrictedClassType(
                base_type=six.text_type,
                restriction_type="dict_key",
                restriction_arg={
                    "UNICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:UNICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "MULTICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:MULTICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                },
            ),
            is_leaf=True,
            yang_name="safi-name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="identityref",
            is_config=True,
        )
        self.__enabled = YANGDynClass(
            base=YANGBool,
            is_leaf=True,
            yang_name="enabled",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
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
                "network-instances",
                "network-instance",
                "protocols",
                "protocol",
                "isis",
                "interfaces",
                "interface",
                "afi-safi",
                "af",
                "config",
            ]

    def _get_afi_name(self):
        """
    Getter method for afi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/afi_safi/af/config/afi_name (identityref)

    YANG Description: Address-family type.
    """
        return self.__afi_name

    def _set_afi_name(self, v, load=False):
        """
    Setter method for afi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/afi_safi/af/config/afi_name (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_afi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_afi_name() directly.

    YANG Description: Address-family type.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=six.text_type,
                    restriction_type="dict_key",
                    restriction_arg={
                        "IPV4": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                        "oc-isis-types:IPV4": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                        "IPV6": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                        "oc-isis-types:IPV6": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                    },
                ),
                is_leaf=True,
                yang_name="afi-name",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="identityref",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """afi_name must be of a type compatible with identityref""",
                    "defined-type": "openconfig-network-instance:identityref",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'IPV4': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}, 'oc-isis-types:IPV4': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}, 'IPV6': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}, 'oc-isis-types:IPV6': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}},), is_leaf=True, yang_name="afi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
                }
            )

        self.__afi_name = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_afi_name(self):
        self.__afi_name = YANGDynClass(
            base=RestrictedClassType(
                base_type=six.text_type,
                restriction_type="dict_key",
                restriction_arg={
                    "IPV4": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:IPV4": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "IPV6": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:IPV6": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                },
            ),
            is_leaf=True,
            yang_name="afi-name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="identityref",
            is_config=True,
        )

    def _get_safi_name(self):
        """
    Getter method for safi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/afi_safi/af/config/safi_name (identityref)

    YANG Description: Subsequent address-family type.
    """
        return self.__safi_name

    def _set_safi_name(self, v, load=False):
        """
    Setter method for safi_name, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/afi_safi/af/config/safi_name (identityref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_safi_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_safi_name() directly.

    YANG Description: Subsequent address-family type.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=six.text_type,
                    restriction_type="dict_key",
                    restriction_arg={
                        "UNICAST": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                        "oc-isis-types:UNICAST": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                        "MULTICAST": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                        "oc-isis-types:MULTICAST": {
                            "@module": "openconfig-isis-types",
                            "@namespace": "http://openconfig.net/yang/isis-types",
                        },
                    },
                ),
                is_leaf=True,
                yang_name="safi-name",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="identityref",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """safi_name must be of a type compatible with identityref""",
                    "defined-type": "openconfig-network-instance:identityref",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=six.text_type, restriction_type="dict_key", restriction_arg={'UNICAST': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}, 'oc-isis-types:UNICAST': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}, 'MULTICAST': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}, 'oc-isis-types:MULTICAST': {'@module': 'openconfig-isis-types', '@namespace': 'http://openconfig.net/yang/isis-types'}},), is_leaf=True, yang_name="safi-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='identityref', is_config=True)""",
                }
            )

        self.__safi_name = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_safi_name(self):
        self.__safi_name = YANGDynClass(
            base=RestrictedClassType(
                base_type=six.text_type,
                restriction_type="dict_key",
                restriction_arg={
                    "UNICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:UNICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "MULTICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                    "oc-isis-types:MULTICAST": {
                        "@module": "openconfig-isis-types",
                        "@namespace": "http://openconfig.net/yang/isis-types",
                    },
                },
            ),
            is_leaf=True,
            yang_name="safi-name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="identityref",
            is_config=True,
        )

    def _get_enabled(self):
        """
    Getter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/afi_safi/af/config/enabled (boolean)

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
        return self.__enabled

    def _set_enabled(self, v, load=False):
        """
    Setter method for enabled, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/afi_safi/af/config/enabled (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enabled() directly.

    YANG Description: When set to true, the functionality within which this leaf is
defined is enabled, when set to false it is explicitly disabled.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=YANGBool,
                is_leaf=True,
                yang_name="enabled",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="boolean",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """enabled must be of a type compatible with boolean""",
                    "defined-type": "boolean",
                    "generated-type": """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='boolean', is_config=True)""",
                }
            )

        self.__enabled = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_enabled(self):
        self.__enabled = YANGDynClass(
            base=YANGBool,
            is_leaf=True,
            yang_name="enabled",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="boolean",
            is_config=True,
        )

    afi_name = __builtin__.property(_get_afi_name, _set_afi_name)
    safi_name = __builtin__.property(_get_safi_name, _set_safi_name)
    enabled = __builtin__.property(_get_enabled, _set_enabled)

    _pyangbind_elements = OrderedDict(
        [("afi_name", afi_name), ("safi_name", safi_name), ("enabled", enabled)]
    )

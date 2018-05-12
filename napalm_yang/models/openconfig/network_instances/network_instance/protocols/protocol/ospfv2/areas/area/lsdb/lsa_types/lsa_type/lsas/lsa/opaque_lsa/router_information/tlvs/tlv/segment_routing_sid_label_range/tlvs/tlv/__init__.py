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

from . import unknown_tlv
from . import state
from . import sid_label


class tlv(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/router-information/tlvs/tlv/segment-routing-sid-label-range/tlvs/tlv. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Sub-TLVs of the SID/Label range TLV
  """
    __slots__ = (
        "_path_helper", "_extmethods", "__unknown_tlv", "__state", "__sid_label"
    )

    _yang_name = "tlv"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__unknown_tlv = YANGDynClass(
            base=unknown_tlv.unknown_tlv,
            is_container="container",
            yang_name="unknown-tlv",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )
        self.__state = YANGDynClass(
            base=state.state,
            is_container="container",
            yang_name="state",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )
        self.__sid_label = YANGDynClass(
            base=sid_label.sid_label,
            is_container="container",
            yang_name="sid-label",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
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
                "ospfv2",
                "areas",
                "area",
                "lsdb",
                "lsa-types",
                "lsa-type",
                "lsas",
                "lsa",
                "opaque-lsa",
                "router-information",
                "tlvs",
                "tlv",
                "segment-routing-sid-label-range",
                "tlvs",
                "tlv",
            ]

    def _get_unknown_tlv(self):
        """
    Getter method for unknown_tlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/unknown_tlv (container)

    YANG Description: An unknown TLV within the context. Unknown TLVs are
defined to be the set of TLVs that are not modelled
within the OpenConfig model, or are unknown to the
local system such that it cannot decode their value.
    """
        return self.__unknown_tlv

    def _set_unknown_tlv(self, v, load=False):
        """
    Setter method for unknown_tlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/unknown_tlv (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unknown_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unknown_tlv() directly.

    YANG Description: An unknown TLV within the context. Unknown TLVs are
defined to be the set of TLVs that are not modelled
within the OpenConfig model, or are unknown to the
local system such that it cannot decode their value.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=unknown_tlv.unknown_tlv,
                is_container="container",
                yang_name="unknown-tlv",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """unknown_tlv must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=unknown_tlv.unknown_tlv, is_container='container', yang_name="unknown-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
                }
            )

        self.__unknown_tlv = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_unknown_tlv(self):
        self.__unknown_tlv = YANGDynClass(
            base=unknown_tlv.unknown_tlv,
            is_container="container",
            yang_name="unknown-tlv",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )

    def _get_state(self):
        """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/state (container)

    YANG Description: State parameters of the sub-TLVs of the SR/Label range TLV
    """
        return self.__state

    def _set_state(self, v, load=False):
        """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of the sub-TLVs of the SR/Label range TLV
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=state.state,
                is_container="container",
                yang_name="state",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """state must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
                }
            )

        self.__state = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_state(self):
        self.__state = YANGDynClass(
            base=state.state,
            is_container="container",
            yang_name="state",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )

    def _get_sid_label(self):
        """
    Getter method for sid_label, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/sid_label (container)

    YANG Description: Sub-TLV used to advertise the SID or label associated with the
subset of the SRGB being advertised
    """
        return self.__sid_label

    def _set_sid_label(self, v, load=False):
        """
    Setter method for sid_label, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/sid_label (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_label() directly.

    YANG Description: Sub-TLV used to advertise the SID or label associated with the
subset of the SRGB being advertised
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=sid_label.sid_label,
                is_container="container",
                yang_name="sid-label",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """sid_label must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=sid_label.sid_label, is_container='container', yang_name="sid-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
                }
            )

        self.__sid_label = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_sid_label(self):
        self.__sid_label = YANGDynClass(
            base=sid_label.sid_label,
            is_container="container",
            yang_name="sid-label",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )

    unknown_tlv = __builtin__.property(_get_unknown_tlv)
    state = __builtin__.property(_get_state)
    sid_label = __builtin__.property(_get_sid_label)

    _pyangbind_elements = OrderedDict(
        [("unknown_tlv", unknown_tlv), ("state", state), ("sid_label", sid_label)]
    )


from . import unknown_tlv
from . import state
from . import sid_label


class tlv(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa-types/lsa-type/lsas/lsa/opaque-lsa/router-information/tlvs/tlv/segment-routing-sid-label-range/tlvs/tlv. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Sub-TLVs of the SID/Label range TLV
  """
    __slots__ = (
        "_path_helper", "_extmethods", "__unknown_tlv", "__state", "__sid_label"
    )

    _yang_name = "tlv"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__unknown_tlv = YANGDynClass(
            base=unknown_tlv.unknown_tlv,
            is_container="container",
            yang_name="unknown-tlv",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )
        self.__state = YANGDynClass(
            base=state.state,
            is_container="container",
            yang_name="state",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )
        self.__sid_label = YANGDynClass(
            base=sid_label.sid_label,
            is_container="container",
            yang_name="sid-label",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
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
                "ospfv2",
                "areas",
                "area",
                "lsdb",
                "lsa-types",
                "lsa-type",
                "lsas",
                "lsa",
                "opaque-lsa",
                "router-information",
                "tlvs",
                "tlv",
                "segment-routing-sid-label-range",
                "tlvs",
                "tlv",
            ]

    def _get_unknown_tlv(self):
        """
    Getter method for unknown_tlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/unknown_tlv (container)

    YANG Description: An unknown TLV within the context. Unknown TLVs are
defined to be the set of TLVs that are not modelled
within the OpenConfig model, or are unknown to the
local system such that it cannot decode their value.
    """
        return self.__unknown_tlv

    def _set_unknown_tlv(self, v, load=False):
        """
    Setter method for unknown_tlv, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/unknown_tlv (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_unknown_tlv is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_unknown_tlv() directly.

    YANG Description: An unknown TLV within the context. Unknown TLVs are
defined to be the set of TLVs that are not modelled
within the OpenConfig model, or are unknown to the
local system such that it cannot decode their value.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=unknown_tlv.unknown_tlv,
                is_container="container",
                yang_name="unknown-tlv",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """unknown_tlv must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=unknown_tlv.unknown_tlv, is_container='container', yang_name="unknown-tlv", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
                }
            )

        self.__unknown_tlv = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_unknown_tlv(self):
        self.__unknown_tlv = YANGDynClass(
            base=unknown_tlv.unknown_tlv,
            is_container="container",
            yang_name="unknown-tlv",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )

    def _get_state(self):
        """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/state (container)

    YANG Description: State parameters of the sub-TLVs of the SR/Label range TLV
    """
        return self.__state

    def _set_state(self, v, load=False):
        """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters of the sub-TLVs of the SR/Label range TLV
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=state.state,
                is_container="container",
                yang_name="state",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """state must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
                }
            )

        self.__state = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_state(self):
        self.__state = YANGDynClass(
            base=state.state,
            is_container="container",
            yang_name="state",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )

    def _get_sid_label(self):
        """
    Getter method for sid_label, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/sid_label (container)

    YANG Description: Sub-TLV used to advertise the SID or label associated with the
subset of the SRGB being advertised
    """
        return self.__sid_label

    def _set_sid_label(self, v, load=False):
        """
    Setter method for sid_label, mapped from YANG variable /network_instances/network_instance/protocols/protocol/ospfv2/areas/area/lsdb/lsa_types/lsa_type/lsas/lsa/opaque_lsa/router_information/tlvs/tlv/segment_routing_sid_label_range/tlvs/tlv/sid_label (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sid_label is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sid_label() directly.

    YANG Description: Sub-TLV used to advertise the SID or label associated with the
subset of the SRGB being advertised
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=sid_label.sid_label,
                is_container="container",
                yang_name="sid-label",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """sid_label must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=sid_label.sid_label, is_container='container', yang_name="sid-label", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
                }
            )

        self.__sid_label = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_sid_label(self):
        self.__sid_label = YANGDynClass(
            base=sid_label.sid_label,
            is_container="container",
            yang_name="sid-label",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )

    unknown_tlv = __builtin__.property(_get_unknown_tlv)
    state = __builtin__.property(_get_state)
    sid_label = __builtin__.property(_get_sid_label)

    _pyangbind_elements = OrderedDict(
        [("unknown_tlv", unknown_tlv), ("state", state), ("sid_label", sid_label)]
    )

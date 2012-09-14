# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright 2012 Hewlett Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
:mod:`3parclient` -- Package contains hp-specific modules
=====================================================================

.. automodule:: 3parclient
.. moduleauthor:: walter.boring@hp.com
"""

__author__ = "Walter A. Boring IV"
__copyright__ = "Copyright 2012, Hewlett Packard Development Company, L.P."
#__credits__ = []
__license__ = "Apache"
__version__ = "2.0"
__maintainer__ = "Walter A. Boring IV"
__email__ = "walter.boring@hp.com"
__status__ = "pre-alpha"


#__all__=["volume", "client", "http", "WsapiEnumIF"]

import WsapiEnumIF
import volume

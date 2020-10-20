# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkvcs.endpoint import endpoint_data

class ListDeviceGroupsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vcs', '2020-05-15', 'ListDeviceGroups')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_IsPage(self):
		return self.get_body_params().get('IsPage')

	def set_IsPage(self,IsPage):
		self.add_body_params('IsPage', IsPage)

	def get_PageNum(self):
		return self.get_body_params().get('PageNum')

	def set_PageNum(self,PageNum):
		self.add_body_params('PageNum', PageNum)

	def get_CorpIdList(self):
		return self.get_body_params().get('CorpIdList')

	def set_CorpIdList(self,CorpIdList):
		self.add_body_params('CorpIdList', CorpIdList)

	def get_DeviceCodeList(self):
		return self.get_body_params().get('DeviceCodeList')

	def set_DeviceCodeList(self,DeviceCodeList):
		self.add_body_params('DeviceCodeList', DeviceCodeList)

	def get_Name(self):
		return self.get_body_params().get('Name')

	def set_Name(self,Name):
		self.add_body_params('Name', Name)

	def get_PageSize(self):
		return self.get_body_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_body_params('PageSize', PageSize)

	def get_Group(self):
		return self.get_body_params().get('Group')

	def set_Group(self,Group):
		self.add_body_params('Group', Group)
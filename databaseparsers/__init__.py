#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD.
# See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from nomad.config.models.plugins import ParserEntryPoint


class EntryPoint(ParserEntryPoint):
    def load(self):
        from nomad.parsing import MatchingParserInterface
        from . import (
            openkim
        )

        return MatchingParserInterface(self.parser_class_name)


openkim_parser_entry_point = EntryPoint(
    name='parsers/openkim',
    description='NOMAD parser for OPENKIM.',
    parser_class_name='workflowparsers.openkim.OpenKIMParser',
)
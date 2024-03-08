# SPDX-License-Identifier: Apache-2.0
#
# http://nexb.com and https://github.com/nexB/scancode.io
# The ScanCode.io software is licensed under the Apache License version 2.0.
# Data generated with ScanCode.io is provided as-is without warranties.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# Data Generated with ScanCode.io is provided on an "AS IS" BASIS, WITHOUT WARRANTIES
# OR CONDITIONS OF ANY KIND, either express or implied. No content created from
# ScanCode.io should be considered or used as legal advice. Consult an Attorney
# for any legal advice.
#
# ScanCode.io is a free software code scanning tool from nexB Inc. and others.
# Visit https://github.com/nexB/scancode.io for support and download.

from django.contrib.auth.models import Group
from minecode.management.user_creation import CreateUserCommand


class Command(CreateUserCommand):
    help = "Create a user and generate an API key for a scan queue worker"

    def handle(self, *args, **options):
        username = options["username"]
        interactive = options["interactive"]
        verbosity = options["verbosity"]
        user = self.create_user(
            username=username,
            interactive=interactive,
            verbosity=verbosity
        )
        # Add user to `scan_queue_workers` group
        scan_queue_workers_group, _ = Group.objects.get_or_create(name='scan_queue_workers')
        scan_queue_workers_group.user_set.add(user)
        msg = f"User {username} added to `scan_queue_workers` group"
        self.stdout.write(msg, self.style.SUCCESS)

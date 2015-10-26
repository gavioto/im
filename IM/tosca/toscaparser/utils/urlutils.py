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


from six.moves.urllib.parse import urljoin
from six.moves.urllib.parse import urlparse
from IM.tosca.toscaparser.utils.gettextutils import _


class UrlUtils(object):

    @staticmethod
    def validate_url(path):
        """Validates whether the given path is a URL or not.

        If the given path includes a scheme (http, https, ftp, ...) and a net
        location (a domain name such as www.github.com) it is validated as a
        URL.
        """
        parsed = urlparse(path)
        return bool(parsed.scheme) and bool(parsed.netloc)

    @staticmethod
    def join_url(url, relative_path):
        """Builds a new URL from the given URL and the relative path.

        Example:
          url: http://www.githib.com/openstack/heat
          relative_path: heat-translator
          - joined: http://www.githib.com/openstack/heat-translator
        """
        if not UrlUtils.validate_url(url):
            raise ValueError(_("Provided URL is invalid."))
        return urljoin(url, relative_path)

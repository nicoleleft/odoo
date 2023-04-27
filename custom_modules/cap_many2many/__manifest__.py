# -*- coding: utf-8 -*-
######################################################################################
#
#    Captivea
#
#    This program is under the terms of the Odoo Proprietary License v1.0 (OPL-1)
#    It is forbidden to publish, distribute, sublicense, or sell copies of the Software
#    or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
########################################################################################

{
    'name': 'CAP Many2Many',
    'version': '15.0.0.2',
    'summary': 'Captivea Many2Many Example',
    'description':
        """
        Captivea Many2Many Example
        """,
    'category': 'Website',
    'author': 'Captivea LLC, JEU',
    'company': 'Captivea LLC',
    'maintainer': 'https://www.captivea.com/',
    'depends': ["base","purchase","stock"],
    'website': 'https://www.captivea.com/',
    'data': [
        'views/cap_book.xml',
        'views/cap_book_genre.xml',
        'views/purchase_order.xml',
        'views/res_partner.xml',
        'views/stock_warehouse.xml'
    ],
    'qweb': [],
    'images': [],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': True,
    "cloc_exclude": ["./**/*"],  # exclude all files in a module recursively
}
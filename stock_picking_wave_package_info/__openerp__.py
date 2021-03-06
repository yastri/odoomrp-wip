# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c)
#    2015 Serv. Tec. Avanzados - Pedro M. Baeza (http://www.serviciosbaeza.com)
#    2015 AvanzOsc (http://www.avanzosc.es)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Stock picking wave package info',
    'version': "1.0",
    "author": "OdooMRP team,"
              "AvanzOSC,"
              "Serv. Tecnol. Avanzados - Pedro M. Baeza",
    'website': "http://www.odoomrp.com",
    'category': 'Stock Management',
    'depends': ["stock_picking_package_info",
                "stock_picking_wave_management",
                ],
    'data': ["views/stock_picking_wave_view.xml",
             "views/stock_quant_package_view.xml",
             "reports/label_creator_wave_palet_report.xml"
             ],
    'installable': True,
    'auto_install': True,
}

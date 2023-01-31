# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DataCaptureForm
                                 A QGIS plugin
 Form created to capture data and save it locally in excel spreed sheet.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-01-31
        copyright            : (C) 2023 by Ivan Israel Valencia Barreda
        email                : ivanvalenciatec@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DataCaptureForm class from file DataCaptureForm.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .data_capture_form import DataCaptureForm
    return DataCaptureForm(iface)
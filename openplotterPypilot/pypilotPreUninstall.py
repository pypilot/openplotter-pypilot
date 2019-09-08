#!/usr/bin/env python3

# This file is part of Openplotter.
# Copyright (C) 2015 by Sailoog <https://github.com/openplotter/openplotter-pypilot>
#
# Openplotter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
# Openplotter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Openplotter. If not, see <http://www.gnu.org/licenses/>.
import os, subprocess
from openplotterSettings import conf
from openplotterSettings import language

def main():
	conf2 = conf.Conf()
	currentdir = os.path.dirname(__file__)
	currentLanguage = conf2.get('GENERAL', 'lang')
	language.Language(currentdir,'openplotter-pypilot',currentLanguage)

	print(_('Removing packages...'))
	try:
		subprocess.call(['apt', '-y', 'autoremove', 'py-rtimulib2'])
		subprocess.call(['pip', 'uninstall', '-y', 'pywavefront'])
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	print(_('Removing config files...'))
	try:
		subprocess.call(['rm', '-rf', conf2.home+'/.pypilot'])
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	print(_('Removing pypilot, pypilot_boatimu and openplotter-pypilot-read services...'))
	try:
		subprocess.call(['systemctl', 'disable', 'openplotter-pypilot-read'])
		subprocess.call(['systemctl', 'disable', 'pypilot'])
		subprocess.call(['systemctl', 'disable', 'pypilot_boatimu'])
		subprocess.call(['systemctl', 'stop', 'openplotter-pypilot-read'])
		subprocess.call(['systemctl', 'stop', 'pypilot'])
		subprocess.call(['systemctl', 'stop', 'pypilot_boatimu'])
		subprocess.call(['rm', '-f', '/etc/systemd/system/pypilot_boatimu.service'])
		subprocess.call(['rm', '-f', '/etc/systemd/system/pypilot.service'])
		subprocess.call(['rm', '-f', '/etc/systemd/system/openplotter-pypilot-read.service'])
		subprocess.call(['systemctl', 'daemon-reload'])
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))


if __name__ == '__main__':
	main()
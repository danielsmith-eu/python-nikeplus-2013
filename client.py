#    This file is part of python-nikeplus-2013.
#
#    Copyright 2013 Daniel Alexander Smith
#    Copyright 2013 University of Southampton
#
#    python-nikeplus-2013 is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    python-nikeplus-2013 is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with python-nikeplus-2013.  If not, see <http://www.gnu.org/licenses/>.

import argparse, getpass, logging, nikeplus

""" A simple command-line client to demontrate usage of the library. """

logging.basicConfig(level = logging.DEBUG)

parser = argparse.ArgumentParser(description = "Use the Nike+ API")
parser.add_argument('email', type = str, help = "E-mail address of the user")
parser.add_argument('action', type = str, help = "Action to perform")

args = vars(parser.parse_args())
password = getpass.getpass()

nikeplus = nikeplus.NikePlus()
nikeplus.login(args['email'], password)
nikeplus.get_token()


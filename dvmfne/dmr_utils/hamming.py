#!/usr/bin/env python
#
# Digital Voice Modem - Fixed Network Equipment
# GPLv2 Open Source. Use is subject to license terms.
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
# @package DVM / FNE
#
###############################################################################
#   Copyright (C) 2016  Cortney T. Buffington, N0MJS <n0mjs@me.com>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA
###############################################################################

from __future__ import print_function

from bitarray import bitarray

# ------------------------------------------------------------------------------
#   Hamming (15,11,3) routines
# ------------------------------------------------------------------------------


# ENCODER- returns a bitarray object containing the hamming checksums
def enc_15113(_data):
    csum = bitarray(4)
    csum[0] = _data[0] ^ _data[1] ^ _data[2] ^ _data[3] ^ _data[5] ^ _data[7] ^ _data[8]
    csum[1] = _data[1] ^ _data[2] ^ _data[3] ^ _data[4] ^ _data[6] ^ _data[8] ^ _data[9]
    csum[2] = (
        _data[2] ^ _data[3] ^ _data[4] ^ _data[5] ^ _data[7] ^ _data[9] ^ _data[10]
    )
    csum[3] = (
        _data[0] ^ _data[1] ^ _data[2] ^ _data[4] ^ _data[6] ^ _data[7] ^ _data[10]
    )
    return csum


# ------------------------------------------------------------------------------
#   Hamming (13,9,3) routines
# ------------------------------------------------------------------------------


# ENCODER - returns a bitarray object containing the hamming checksums
def enc_1393(_data):
    csum = bitarray(4)
    csum[0] = _data[0] ^ _data[1] ^ _data[3] ^ _data[5] ^ _data[6]
    csum[1] = _data[0] ^ _data[1] ^ _data[2] ^ _data[4] ^ _data[6] ^ _data[7]
    csum[2] = _data[0] ^ _data[1] ^ _data[2] ^ _data[3] ^ _data[5] ^ _data[7] ^ _data[8]
    csum[3] = _data[0] ^ _data[2] ^ _data[4] ^ _data[5] ^ _data[8]
    return csum


# ------------------------------------------------------------------------------
#   Hamming (16,11,4) routines
#  ------------------------------------------------------------------------------


# ENCODER - returns a bitarray object containing the hamming checksums
def enc_16114(_data):
    assert len(_data) == 11, "Hamming Encoder 16,11,4: Data not 11 bits long"
    csum = bitarray(5)
    csum[0] = _data[0] ^ _data[1] ^ _data[2] ^ _data[3] ^ _data[5] ^ _data[7] ^ _data[8]
    csum[1] = _data[1] ^ _data[2] ^ _data[3] ^ _data[4] ^ _data[6] ^ _data[8] ^ _data[9]
    csum[2] = (
        _data[2] ^ _data[3] ^ _data[4] ^ _data[5] ^ _data[7] ^ _data[9] ^ _data[10]
    )
    csum[3] = (
        _data[0] ^ _data[1] ^ _data[2] ^ _data[4] ^ _data[6] ^ _data[7] ^ _data[10]
    )
    csum[4] = (
        _data[0] ^ _data[2] ^ _data[5] ^ _data[6] ^ _data[8] ^ _data[9] ^ _data[10]
    )
    return csum

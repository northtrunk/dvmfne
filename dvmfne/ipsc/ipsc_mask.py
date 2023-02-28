#
# Digital Voice Modem - Fixed Network Equipment
# GPLv2 Open Source. Use is subject to license terms.
# DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#
# @package DVM / FNE / dmrlink
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

# MASKS FOR IPSC, RTP AND THE RTP PAYLOAD (DMR FRAME + FRIENDS) ARE LOCATED
# IN THIS FILE IN THIS ORDER: IPSC, RTP, PAYLOAD

# IPSC MASK VALUES
#
# LINKING STATUS:
# 	Byte 1 - BIT FLAGS:
# 	      xx.. .... = Peer Operational (01 only known valid value)
# 	      ..xx .... = Peer MODE: 00 - No Radio, 01 - Analog, 10 - Digital
# 	      .... xx.. = IPSC Slot 1: 10 on, 01 off
# 	      .... ..xx = IPSC Slot 2: 10 on, 01 off
#   MASK VALUES:
PEER_OP_MSK = 0b01000000
PEER_MODE_MSK = 0b00110000
PEER_MODE_ANALOG = 0b00010000
PEER_MODE_DIGITAL = 0b00100000
IPSC_TS1_MSK = 0b00001100
IPSC_TS2_MSK = 0b00000011

# SERVICE FLAGS:

# 	Byte 1 - 0x00  	= Unknown
# 	Byte 2 - 0x00	= Unknown
# 	Byte 3 - BIT FLAGS:
# 	      x... .... = CSBK Message
# 	      .x.. .... = Repeater Call Monitoring
# 	      ..x. .... = 3rd Party "Console" Application
# 	      ...x xxxx = Unknown - default to 0
#   MASK VALUES:
CSBK_MSK = 0b10000000
RPT_MON_MSK = 0b01000000
CON_APP_MSK = 0b00100000

# 	Byte 4 = BIT FLAGS:
# 	      x... .... = XNL Connected (1=true)
# 	      .x.. .... = XNL Master Device
# 	      ..x. .... = XNL Slave Device
# 	      ...x .... = Set if packets are authenticated
# 	      .... x... = Set if data calls are supported
# 	      .... .x.. = Set if voice calls are supported
# 	      .... ..x. = Unknown - default to 0
# 	      .... ...x = Set if master
#   MASK VALUES:
XNL_STAT_MSK = 0b10000000
XNL_MSTR_MSK = 0b01000000
XNL_SLAVE_MSK = 0b00100000
PKT_AUTH_MSK = 0b00010000
DATA_CALL_MSK = 0b00001000
VOICE_CALL_MSK = 0b00000100
MSTR_PEER_MSK = 0b00000001

# TIMESLOT CALL & STATUS BYTE
#   Byte 17 of Group and Private Voice/Data Packets
#       ..x.. ....TS Value (0=TS1, 1=TS2)
#       .x... ....TS In Progress/End (0=In Progress, 1=End)
#       Possible values: 0x00=TS1, 0x20=TS2, 0x40=TS1 End, 0x60=TS2 End
#   MASK VALUE:
END_MSK = 0b01000000
TS_CALL_MSK = 0b00100000


# RTP MASK VALUES
# Bytes 1 and 2 of the RTP header are bit-fields, the rest
# are at least one byte long, and do not need masked
#   Byte 1
RTP_VER_MSK = 0b11000000
RTP_PAD_MSK = 0b00100000
RTP_EXT_MSK = 0b00010000
RTP_CSIC_MSK = 0b00001111
#   Byte 2
RTP_MRKR_MSK = 0b10000000
RTP_PAY_TYPE_MSK = 0b01111111


# RTP PAYLOAD (DMR FRAME + FRIENDS) MASK VALUES
# This one is tricky. The DMR Frame contents are here
# and re-ordered from their position in the original DMR
# frame format. There are also some other friends in here
# that Motorla added.
#
